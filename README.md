# CLI for myDATA by ΑΑΔΕ (IARP)

Python interface for IARP's myDATA service.

## Building

Install [Poetry](https://python-poetry.org/). Then, install the project
dependencies:

```console
poetry install
```

### Adding new XSD schemas

Whenever there's an API update, myDATA devs include the XML schemas for the
latest API. You can include them in the project as follows:

* Add the XML schemas under `schemas/<version>` dir. For example, for the 1.0.8
  XSDs, we added them with:

  ```console
  cp -r '/path/to/version v1.0.8 XSDs' schemas/1.0.8
  ```

* Generate Python classes from the new XSDs. For example, for the 1.0.8 XSDs, we
  generated Python classes with:


  ```console
  poetry run xsdata -r schemas/1.0.8/ -p mydata.models_v1_0_8 -ss single-package
  ```
