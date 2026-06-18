<!-- GENERATED from ledgercore/docs. Do not edit by hand. -->
---
layout: default
title: "ledgercore"
description: "Shared primitives for ledgerwerk tools"
permalink: /tools/ledgercore/
generated_from: ledgercore/docs
source_path: docs/index.md
---
# ledgercore documentation

Welcome to the `ledgercore` documentation.

`ledgercore` is a small, typed Python library for projects that store structured
records as files. It provides reusable primitives for atomic writes, YAML front
matter, deterministic JSON/YAML storage, safe relative paths, config discovery,
numeric IDs, and cross-ledger references.

## Installation

```bash
pip install ledgercore
```

Requirements: Python 3.10+, PyYAML.

## Quick start

See the [project README](https://github.com/ledgerwerk/ledgercore#readme) for a
hands-on introduction.

## Documentation index

<div class="cards">
  <section class="card"><h3><a href="{{ '/tools/ledgercore/api/' | relative_url }}">Python API</a></h3><p>Public API modules exposed by ledgercore.</p></section>
  <section class="card"><h3><a href="{{ '/tools/ledgercore/references/' | relative_url }}">References</a></h3><p>Global refs, local refs, and cross-ledger reference helpers.</p></section>
  <section class="card"><h3><a href="{{ '/tools/ledgercore/storage/' | relative_url }}">Storage</a></h3><p>Atomic writes, safe paths, metadata, and deterministic storage helpers.</p></section>
  <section class="card"><h3><a href="{{ '/tools/ledgercore/release/' | relative_url }}">Release</a></h3><p>Versioning, validation, and release publication workflow.</p></section>
</div>
