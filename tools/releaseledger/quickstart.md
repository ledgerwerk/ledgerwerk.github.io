---
layout: default
title: releaseledger quickstart
description: Quickstart for releaseledger
permalink: /tools/releaseledger/quickstart/
---

# releaseledger quickstart

## Install

```bash
python -m pip install releaseledger
```

For development:

```bash
python -m pip install -e ".[dev]"
```

## Initialize a project

```bash
releaseledger init
```

This creates `.releaseledger.toml` and the default state layout:

```text
.releaseledger/
  ledgers/
    main/
      releases/
      events/
      indexes/
```

## Create a release and attach the git range

```bash
releaseledger release create 1.2.0   --previous 1.1.0   --released-at 2026-06-14

releaseledger release update 1.2.0   --git-base v1.1.0   --git-head HEAD
```

## Generate entries from git commits

```bash
releaseledger git import 1.2.0   --base v1.1.0   --head HEAD   --status draft   --output /tmp/1.2.0-entries.yaml
```

Edit the YAML to curate summaries, then run:

```bash
releaseledger entry add-many 1.2.0 --file /tmp/1.2.0-entries.yaml --dry-run
releaseledger entry add-many 1.2.0 --file /tmp/1.2.0-entries.yaml
```

## Review coverage and build the changelog

```bash
releaseledger review 1.2.0 --git --strict
releaseledger build 1.2.0   --release-date 2026-06-14   --strict   --target-file CHANGELOG.md
```

## Optional taskledger provenance

Use global refs when a release entry comes from another ledger:

```bash
releaseledger entry add 1.2.0   --kind added   --summary "Added release review gate"   --source-ref tl:task-0103
```
