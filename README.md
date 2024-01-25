# CLI for myDATA by ΑΑΔΕ (IARP)

Python interface for IARP's myDATA service.

## Building

Install [Poetry](https://python-poetry.org/). Then, install the project
dependencies:

```
poetry install
```

### Adding new XSD schemas

Whenever there's an API update, myDATA devs include the XML schemas for the
latest API. You can include them in the project as follows:

* Add the XML schemas under `schemas/<version>` dir. For example, for the 1.0.8
  XSDs, we added them with:

  ```
  cp -r '/path/to/version v1.0.8 XSDs' schemas/1.0.8
  ```

* Generate Python classes from the new XSDs. For example, for the 1.0.8 XSDs, we
  generated Python classes with:


  ```
  poetry run xsdata -ss single-package -ds Google -r schemas/1.0.8/ -p mydata.models_v1_0_8
  ```

* Generate Markdown documentation from the generated Python classes with:

  ```
  poetry run pydoc-markdown -m mydata.models_v1_0_8 --render-toc > docs/models_v1_0_8.md
  ```
