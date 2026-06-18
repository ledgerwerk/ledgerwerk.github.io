---
layout: tool-doc
title: "releaseledger development"
description: "Development workflow for releaseledger"
permalink: /tools/releaseledger/development/
nav_tool: releaseledger
generated_from: releaseledger/docs
source_path: docs/development.md
---
<!-- GENERATED from releaseledger/docs. Do not edit by hand. -->

# Development

## Setup

```bash
python -m pip install -e ".[dev]"
```

## Validation

```bash
pytest -q
ruff check .
mypy releaseledger
python -m build
```

## Documentation

```bash
python -m pip install -e ".[docs]"
sphinx-build -b html docs docs/_build/html
```

## Packaging

The package uses setuptools and setuptools-scm. `releaseledger/_version.py` is
generated version metadata and is included in the context pack for inspection.

## Typing

The project ships `py.typed` and targets Python 3.10 or newer.
