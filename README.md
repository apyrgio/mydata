[![Supported Python Versions](https://img.shields.io/pypi/pyversions/mydata-client)](https://pypi.org/project/mydata-client/)
[![PyPI version](https://badge.fury.io/py/mydata-client.svg)](https://badge.fury.io/py/mydata-client)

# CLI / HTTP client for myDATA

This project allows users to interact with [myDATA](https://www.aade.gr/en/mydata)
("my Digital Accounting and Tax Application") either via a Python HTTP client or
from the CLI.

## Install

Install it with `pip`:

```
python -m pip install mydata-client
```

## Usage

> [!WARNING]
> The tool is not suitable yet for production use. We **strongly** suggest that
> you use it for experimenting only with the development sandbox that myDATA
> provides.

> [!NOTE]
> Oh, you may also find the docs a bit... lacking :grimacing:

If you want to interact programmatically with myDATA's API, you can use the HTTP
client under `mydata/client.py`. The Python dataclasses that bind to XML
documents can be found in the `mydata/models*` modules, depending on which
version of the API you want to use.

There is also a proof-of-concept CLI that you can use:

```
mydata --username <username> <command>
```

There are two command groups that you can invoke:

* The `api` command group, which is unopinionated and straight up hits the
  endpoint that you ask.
* The `invoice` command group, which is heavily opinionated and adds some helper
  commands to work with invoices. Basically, it's there to assist the list ->
  retrieve -> copy -> edit -> validate -> send lifecycle of an invoice.

## Building

Install [Poetry](https://python-poetry.org/). Then, install the project
dependencies:

```
poetry install
```

### Adding new XSD schemas

Whenever there's an API update, myDATA devs include the XML schemas for the
latest API. You can include them in the project as follows:

* Download the XSD zipfile from the myDATA page, and take note of its version
  number (e.g., 1.0.10).
* Run the following command:

  ```
  poetry run ingest-xsd --api-version 1.0.10 /path/to/xsd.zip
  ```

* Commit the final result


## License

Licensed under MPL-2.0. Please read the [`NOTICE.md`](NOTICE.md) and
[`LICENSE`](LICENSE) files for the full copyright and license information.

## Useful links

* [myDATA REST API documentation](https://www.aade.gr/epiheiriseis/mydata-ilektronika-biblia-aade/mydata/tehnikes-prodiagrafes-ekdoseis-mydata)
* [myDATA developer sandbox](https://www.aade.gr/epiheiriseis/mydata-ilektronika-biblia-aade/mydata/dokimastiko-periballon)
