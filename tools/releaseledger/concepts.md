---
layout: default
title: releaseledger concepts
description: Core concepts in releaseledger
permalink: /tools/releaseledger/concepts/
---

# releaseledger concepts

## Git-first

Releaseledger is git-first. Git tags and commit ranges define the shipped change set. The canonical evidence is every commit reachable from the release target and absent from the previous release.

Taskledger, issue trackers, and pull requests can enrich entries, but releaseledger works correctly with only git.

## Source refs

A source ref is a coverage identity.

Accepted refs include:

- Global refs such as `tl:task-0006` or `github:pr-42`.
- Git commit refs such as `git:<7-to-40 hex sha>`.

`git-range:*`, `git-tag:*`, and `git-branch:*` are release metadata markers. They are useful as boundaries but do not create missing-coverage rows.

## Release

A release is a versioned `release.md` record with YAML front matter and optional Markdown body. It tracks status, previous version, release date, source boundaries, source refs, and changelog file metadata.

Release statuses: `planned`, `draft`, `candidate`, `released`, `yanked`, and `canceled`.

`canceled` means the release was never shipped. It is excluded from previous-version inference and public changelog builds by default.

## Entry

An entry is one release-note item stored under `releases/<version>/entries/entry-NNNN.md`.

Entry kinds: `added`, `changed`, `fixed`, `removed`, `deprecated`, `security`, `docs`, `quality`, and `internal`.

Entry statuses: `draft`, `accepted`, and `rejected`. Changelog builds include accepted entries by default.

## Event

Events are append-only operation rows. They omit wall-clock timestamps and before/after deltas. Git history supplies chronology; per-record revisions validate file changes.

## Commit audit sheet

A commit audit sheet is a per-release review artifact. It maps every commit in the selected git range to a reviewer decision and, when applicable, to a release entry.

Its purpose is to prevent release notes from becoming copied commit subjects. Public changelog entries should be written from reviewed behavior, API/docs impact, changed paths, tests, and diff evidence.

Decisions: `needs_review`, `accepted`, `grouped`, `internal`, and `rejected`.

Strict review fails when rows remain uninspected, when public rows lack accepted entry coverage, or when an entry summary matches a commit subject.

## Versioning and indexes

Release and entry files contain `versioning.schema_version` and `versioning.revision`. New records start at revision 1, and revisions increase by exactly one for meaningful changes.

Releaseledger rebuilds `indexes/releases.json` and `indexes/entries.json` after mutations. Indexes are derived state and should remain deterministic.
