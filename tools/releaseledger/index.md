---
layout: default
title: releaseledger
description: Project-local release management for coding workflows
permalink: /tools/releaseledger/
---

# releaseledger

`releaseledger` is a standalone release-state ledger for Python projects and other source repositories. It stores releases, release-note entries, operation events, and deterministic JSON indexes in a project-local file layout.

It is **git-first**: release boundaries and commit ranges are treated as the canonical evidence of what shipped. Taskledger tasks, GitHub issues, and pull requests can be recorded as provenance, but they are optional context.

<div class="cards">
  <section class="card"><h3><a href="{{ '/tools/releaseledger/quickstart/' | relative_url }}">Quickstart</a></h3><p>Initialize a project, import git entries, review coverage, and build a changelog.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/concepts/' | relative_url }}">Concepts</a></h3><p>Release records, entries, source refs, events, commit audit sheets, and indexes.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/commands/' | relative_url }}">Commands</a></h3><p>CLI command groups and common workflows.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/changelog/' | relative_url }}">Changelog</a></h3><p>Two-step changelog rendering, strict review, and section correction.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/storage/' | relative_url }}">Storage</a></h3><p>Default layout, external state directories, and diagnostics.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/api/' | relative_url }}">Python API</a></h3><p>Public modules to use from integrations.</p></section>
</div>

## Install

```bash
python -m pip install releaseledger
```

For local development:

```bash
python -m pip install -e ".[dev]"
```

## Minimal workflow

```bash
releaseledger init
releaseledger release create 1.2.0 --previous 1.1.0 --released-at 2026-06-14
releaseledger release update 1.2.0 --git-base v1.1.0 --git-head HEAD
releaseledger git import 1.2.0 --base v1.1.0 --head HEAD --status draft --output /tmp/entries.yaml
releaseledger entry add-many 1.2.0 --file /tmp/entries.yaml --dry-run
releaseledger entry add-many 1.2.0 --file /tmp/entries.yaml
releaseledger review 1.2.0 --git --strict
releaseledger build 1.2.0 --release-date 2026-06-14 --strict --target-file CHANGELOG.md
```
