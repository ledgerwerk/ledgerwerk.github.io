---
layout: default
title: releaseledger changelog rendering
description: releaseledger changelog and review workflow
permalink: /tools/releaseledger/changelog/
---

# releaseledger changelog rendering

## Two-step model

`releaseledger changelog` renders review context. Use it when a human or coding agent needs release metadata, entries, target-file guidance, and optional lint findings.

`releaseledger build` renders the final changelog section and inserts it into the target file. Use `--dry-run` before writing and `--replace-existing` when re-rendering an existing release section.

## Full changelog rebuild

`releaseledger build` without a version, or `releaseledger build --all`, rebuilds the complete target file from ledger state.

Default behavior:

- Excludes internal entries.
- Excludes non-released releases.
- Preserves the `## [Unreleased]` body.
- Rewrites the whole target file.

## Strict builds

`releaseledger build --strict` blocks on entry lint errors, empty included entries unless `--allow-empty` is supplied, and release source refs that are not covered by included entries.

## Release review

`releaseledger review VERSION` is the preferred pre-build gate. It combines release state, entry coverage, orphan detection, entry lint, and a strict changelog dry run into one deterministic report.

Expected source refs are classified as `covered`, `draft_only`, `rejected_only`, `internal_only`, or `missing`.

Run review before adding new entries. If a `source_ref` is already covered by an accepted entry, update that entry instead of adding a duplicate.

```text
releaseledger review 0.5.0
releaseledger --json review 0.5.0
releaseledger review 0.5.0 --strict --target-file CHANGELOG.md
```

## Section correction

When a release section in the target changelog is stale, use section helpers instead of hand-editing:

```text
releaseledger changelog-section rename-section OLD NEW --target-file CHANGELOG.md
releaseledger changelog-section remove-section VERSION --target-file CHANGELOG.md
```

`release rename --rename-changelog-section` and `release cancel --remove-changelog-section` apply the same corrections as part of release correction workflows.
