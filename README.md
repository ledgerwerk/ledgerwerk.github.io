# ledgerwerk.github.io

## Generated tool docs

The Markdown files under `tools/archledger/`, `tools/taskledger/`, `tools/releaseledger/`, and `tools/ledgercore/` are generated from the corresponding `ledgerwerk/*/docs` directories.
Do not edit those generated files by hand. Run:

```bash
python3 scripts/sync_tool_docs.py --source _vendor/archledger/docs --dest tools/archledger --tool archledger
python3 scripts/sync_tool_docs.py --source _vendor/taskledger/docs --dest tools/taskledger --tool taskledger
python3 scripts/sync_tool_docs.py --source _vendor/releaseledger/docs --dest tools/releaseledger --tool releaseledger
python3 scripts/sync_tool_docs.py --source _vendor/ledgercore/docs --dest tools/ledgercore --tool ledgercore
```

Use temporary checkouts under `_vendor/` for local sync runs. `_vendor/` is ignored and should be removed after validation.