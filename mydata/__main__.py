import click
import dataclasses
import functools
import json
import logging
import qrcode
import rich
import rich.table
import rich.console
import rich.tree
import rich.pretty
import sys

from . import client
from .models_v1_0_8 import AadeBookInvoiceType, InvoicesDoc


def printer(obj, fmt):
    if fmt == "xml":
        print(obj.xml)
    else:
        del(obj.xml)
        dct = dataclasses.asdict(obj)
        if fmt == "pretty":
            rich.pretty.pprint(dct)
        else:
            raise ValueError(f"Unexpected format type: {fmt}")


# HACK: I bet there's a simpler way to do it.
def click_options_gen(params):
    def decorator(func):
        dec_func = func
        for p, info in params.items():
            name = "--" + p.replace("_", "-")
            is_required = info.get("required")
            t = info.get("type")
            if is_required:
                click_dec = click.option(name)
            else:
                click_dec = click.option(name, default=None)
            dec_func = click_dec(dec_func)
        return dec_func
    return decorator


@click.group()
@click.option("--username")
@click.option("--token")
@click.option("-v", "--verbose", count=True)
@click.option("--prod", is_flag=True, default=False)
@click.pass_context
def cli(ctx, username, token, verbose, prod):
    fmt = "[%(levelname)-5s] %(message)s"
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format=fmt)
    if verbose > 1:
        import http.client

        http.client.HTTPConnection.debuglevel = 1
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True
    ctx.obj = client.Client(username, token, prod)


@cli.group()
@click.pass_context
def api(ctx):
    pass


@api.command()
@click.pass_obj
def send_invoice(c):
    invoice = AadeBookInvoiceType()
    invoices = InvoicesDoc(invoice=[invoice])
    resp = c.send_invoices(invoices)


@api.command()
@click_options_gen(client.PARAMS_REQUEST_DOCS)
@click.option("-o", "--output", type=click.Choice(["xml", "pretty"]),
              default="xml")
@click.pass_obj
def request_docs(c, output, **options):
    resp = c.request_docs(**options)
    printer(resp, output)


@api.command()
@click_options_gen(client.PARAMS_REQUEST_DOCS)
@click.option("-o", "--output", type=click.Choice(["xml", "pretty"]),
              default="xml")
@click.pass_obj
def request_transmitted_docs(c, output, **options):
    resp = c.request_transmitted_docs(**options)
    printer(resp, output)


@cli.group()
@click.pass_context
def invoices(ctx):
    pass


@invoices.command()
@click_options_gen(client.PARAMS_REQUEST_DOCS)
@click.pass_obj
def list(c, **options):
    if options["mark"] is None:
        options["mark"] = 0
    resp = c.request_transmitted_docs(**options)
    if resp.continuation_token:
        raise RuntimeError(
            "Pagination is not implemented, please narrow down your search"
        )

    invoices = resp.invoices_doc.invoice
    table = rich.table.Table(title="Invoices")
    table.add_column("MARK")
    table.add_column("A/A")
    table.add_column("Counter Part")
    table.add_column("Date")
    table.add_column("Total Gross")
    table.add_column("Cancelled")

    for inv in invoices:
        date = str(inv.invoice_header.issue_date)
        cancelled = "Yes" if inv.cancelled_by_mark else "No"
        counter_part = inv.counterpart.vat_number if inv.counterpart else "-"

        table.add_row(
            str(inv.mark),
            str(inv.invoice_header.aa),
            counter_part,
            date,
            str(inv.invoice_summary.total_gross_value),
            cancelled,
        )

    console = rich.console.Console()
    console.print(table)


def get_invoice(c, mark):
    """Get a single invoice from a MARK."""
    start_mark = str(int(mark) - 1)
    resp = c.request_transmitted_docs(mark=start_mark, max_mark=mark)
    if resp.invoices_doc is None:
        print(
            f"Could not find a document withe provided MARK: {mark}",
            file=sys.stderr
        )
        exit(1)
    elif len(resp.invoices_doc.invoice) > 1:
        raise RuntimeError("BUG! Received more than one invoices")

    inv = resp.invoices_doc.invoice[0]
    # FIXME: This is not quite accurate.
    inv.xml = resp.xml
    return inv


@invoices.command()
@click.argument("mark")
@click.option("-o", "--output", type=click.Choice(["xml", "pretty"]),
              default="pretty")
@click.pass_obj
def show(c, mark, output):
    inv = get_invoice(c, mark)
    printer(inv, output)


@invoices.command()
@click.argument("mark")
@click.option("-f", "--file")
@click.pass_obj
def qr(c, mark, file):
    inv = get_invoice(c, mark)
    if inv.qr_code_url is None:
        print("Invoice found, but does not have QR code URL", file=sys.stderr)
        exit(1)
    qrcode.make(inv.qrcode).save(file)
