import click
import dataclasses
import functools
import json
import logging
import rich.table
import rich.console
import rich.tree

from . import client
from .models_v1_0_8 import AadeBookInvoiceType, InvoicesDoc


def printer(obj, fmt):
    if fmt == "xml":
        print(obj.xml)
    else:
        del(obj.xml)
        dct = dataclasses.asdict(obj)
        if fmt == "pretty":
            rich.inspect(dct)
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


@cli.command()
@click.pass_obj
def send_invoice(c):
    invoice = AadeBookInvoiceType()
    invoices = InvoicesDoc(invoice=[invoice])
    resp = c.send_invoices(invoices)


@cli.command()
@click_options_gen(client.PARAMS_REQUEST_DOCS)
@click.option("-o", "--output", type=click.Choice(["xml", "pretty"]),
              default="xml")
@click.pass_obj
def request_docs(c, output, **options):
    resp = c.request_docs(**options)
    printer(resp, output)


@cli.command()
@click_options_gen(client.PARAMS_REQUEST_DOCS)
@click.option("-o", "--output", type=click.Choice(["xml", "pretty"]),
              default="xml")
@click.pass_obj
def request_transmitted_docs(c, output, **options):
    resp = c.request_transmitted_docs(**options)
    printer(resp, output)