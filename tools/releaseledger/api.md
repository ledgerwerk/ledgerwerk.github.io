---
layout: default
title: releaseledger Python API
description: Public releaseledger API surface
permalink: /tools/releaseledger/api/
---

# releaseledger Python API

Integrations should prefer public `releaseledger.api` modules over internal service paths.

## Public modules

| Area | Module |
| --- | --- |
| Release API | `releaseledger.api.releases` |
| Entry API | `releaseledger.api.entries` |
| Changelog API | `releaseledger.api.changelog` |
| Config API | `releaseledger.api.config` |
| Errors | `releaseledger.errors` |
| Release model | `releaseledger.domain.release` |
| Entry model | `releaseledger.domain.entry` |
| Event model | `releaseledger.domain.event` |

## Local API documentation

The releaseledger repository already contains Sphinx API docs in `docs/api.rst`. For a later, generated API reference, build Sphinx in the source repository and publish the generated HTML under `/tools/releaseledger/api/reference/`.
