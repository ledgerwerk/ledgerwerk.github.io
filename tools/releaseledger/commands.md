---
layout: default
title: releaseledger commands
description: releaseledger CLI command reference
permalink: /tools/releaseledger/commands/
---

# releaseledger commands

## Root options

```text
releaseledger --cwd PATH ...
releaseledger --json ...
releaseledger --version
```

`--cwd` runs as if started from another directory. `--json` emits deterministic JSON envelopes.

## Project commands

```text
releaseledger init [--releaseledger-dir PATH] [--project-name NAME] [--external-dir] [--force]
releaseledger storage where
releaseledger config show
releaseledger config set releaseledger_dir PATH [--external-dir]
```

## Release commands

```text
releaseledger release create VERSION [metadata options]
releaseledger release update VERSION [metadata options] [--clear-*] [--force]
releaseledger release tag VERSION [metadata options]
releaseledger release finalize VERSION [--released-at YYYY-MM-DD] [--changelog-file PATH]
releaseledger release cancel VERSION [--reason TEXT] [--superseded-by VERSION]
releaseledger release rename OLD_VERSION NEW_VERSION [correction options]
releaseledger release chain check
releaseledger release chain repair [--dry-run] [--apply]
releaseledger release list
releaseledger release show VERSION
```

`release tag` creates a released release. `release finalize` transitions an existing release to released. `release cancel` records a never-shipped release as an audit tombstone. `release rename` moves a release bundle and can update entries and changelog sections.

## Entry commands

```text
releaseledger entry add VERSION --kind KIND --summary TEXT [metadata options]
releaseledger entry add-many VERSION --file FILE [--dry-run]
releaseledger entry update VERSION ENTRY_ID [metadata options]
releaseledger entry show VERSION ENTRY_ID
releaseledger entry import VERSION --file FILE [--replace] [--source-ledger LEDGER]
releaseledger entry list VERSION
releaseledger entry lint VERSION [--strict] [--include-status STATUS]...
releaseledger entry prompt VERSION [--source-ref REF]... [--context-file FILE]
```

`entry add-many` expects YAML with a top-level `entries` list.

## Changelog commands

```text
releaseledger changelog VERSION [--format markdown|json] [--output PATH]
releaseledger build VERSION [--target-file PATH] [--dry-run] [--replace-existing] [--strict]
releaseledger build [VERSION] [--all] [--target-file CHANGELOG.md] [--strict]
```

`changelog` renders review context. `build` writes final changelog sections. `build` without a version rebuilds the full changelog from ledger state.

## Review commands

```text
releaseledger review VERSION [--target-file PATH] [--strict] [--git] [--git-base REF] [--git-head REF] [--require-audit-sheet]
```

Review is read-only. It combines release state, entry coverage, orphan detection, entry lint, and a strict changelog dry run into one deterministic report.

## Git-first commands

```text
releaseledger git range VERSION [--base REF] [--head REF]
releaseledger git range next --base REF [--head REF]
releaseledger git import VERSION --base REF [--head REF] [--status draft] --output PATH
releaseledger git import next --base REF [--head REF] --output PATH
```

`git range` prints candidate entries from a commit range. `git import` creates a YAML batch for review and curation.

## Commit audit sheet commands

```text
releaseledger audit init VERSION [--base REF] [--head REF] [--overwrite]
releaseledger audit show VERSION [--format markdown|json] [--output PATH]
releaseledger audit update VERSION --file PATH
releaseledger audit validate VERSION [--strict] [--include-internal]
releaseledger audit sync VERSION
```

The audit sheet maps commits to reviewer decisions and release entries. Commit subjects are evidence-only and must not become changelog prose.

## Branch commands

```text
releaseledger branch status
releaseledger branch start BRANCH --parent PARENT
releaseledger branch merge BRANCH --into TARGET --release VERSION
```

## Changelog section correction

```text
releaseledger changelog-section remove-section VERSION --target-file PATH [--ignore-missing] [--dry-run]
releaseledger changelog-section rename-section OLD_VERSION NEW_VERSION --target-file PATH [--ignore-missing] [--replace-existing] [--dry-run]
```
