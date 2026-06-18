<!-- GENERATED from releaseledger/docs. Do not edit by hand. -->
---
layout: default
title: "releaseledger"
description: "Project-local release management for coding workflows"
permalink: /tools/releaseledger/
generated_from: releaseledger/docs
source_path: docs/index.md
---
# releaseledger

Project-local release management for coding workflows.

`releaseledger` stores release records, release-note entries, append-only
events, and deterministic JSON indexes in a project-local or explicitly external
state directory. It also renders reviewable changelog context and final
`CHANGELOG.md` sections.


## Design constraints

Releaseledger is standalone. It depends on `ledgercore` for storage and
reference primitives, but it does not import taskledger or inspect taskledger
state. External provenance is represented by explicit global refs such as
`tl:task-0103`.

<div class="cards">
  <section class="card"><h3><a href="{{ '/tools/releaseledger/quickstart/' | relative_url }}">Quickstart</a></h3><p>Initialize a project, import git entries, review coverage, and build a changelog.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/concepts/' | relative_url }}">Concepts</a></h3><p>Release records, entries, source refs, events, commit audit sheets, and indexes.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/commands/' | relative_url }}">Commands</a></h3><p>CLI command groups and common workflows.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/changelog/' | relative_url }}">Changelog</a></h3><p>Two-step changelog rendering, strict review, and section correction.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/storage/' | relative_url }}">Storage</a></h3><p>Default layout, external state directories, and diagnostics.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/api/' | relative_url }}">Python API</a></h3><p>Public modules to use from integrations.</p></section>
  <section class="card"><h3><a href="{{ '/tools/releaseledger/development/' | relative_url }}">Development</a></h3><p>Development setup, validation, and release maintenance.</p></section>
</div>
