import pathlib
import subprocess
import zipfile

import click


@click.command()
@click.option("--api-version", help="The version of the myDATA API")
@click.argument(
    "filename",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
def ingest(api_version, filename):
    """Ingest XSD schemas from FILENAME and make them default."""
    root_dir = pathlib.Path(__file__).parent.parent
    api_version_underscore = api_version.replace(".", "_")
    models_module = f"mydata.models_{api_version_underscore}"
    docs_md = root_dir / "docs" / f"models_v{api_version_underscore}.md"
    schema_dir = root_dir / "schemas" / api_version

    with zipfile.ZipFile(filename) as xsd_zip:
        xsd_zip.extractall(schema_dir)

    # XXX: It seems that recent XSDs from AADE have a file like
    # InvoicesDoc-v2.0.0_aade_detailed.xsd, which is slightly different from
    # the non-detailed (?) one. For instance, the `itemCode` / `itemDesc`
    # fields are required in the detailed version.
    #
    # If this file remains in the schemas, then xsdata will pick it and will
    # produce bad Python models, that will break parsing. For this reason, we
    # remove it here.
    aade_detailed_xsd = (
        schema_dir / f"InvoicesDoc-v{api_version}_aade_detailed.xsd"
    )
    aade_detailed_xsd.unlink(missing_ok=True)

    xsdata_cmd = [
        "xsdata",
        "generate",
        "-ss",
        "single-package",
        "-ds",
        "Google",
        "-r",
        schema_dir,
        "-p",
        models_module,
    ]
    subprocess.run(xsdata_cmd, check=True)

    with open(docs_md, "w+") as f:
        pydoc_cmd = ["pydoc-markdown", "-m", models_module, "--render-toc"]
        subprocess.run(pydoc_cmd, check=True, stdout=f)


if __name__ == "__main__":
    ingest()
