#!/usr/bin/env python3
"""Sync Sphinx/MyST Markdown docs into Jekyll-compatible tool docs.

This script intentionally does not modify source repositories. It creates a
reviewable generated Jekyll projection in ledgerwerk.github.io/tools/<tool>/.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

DEFAULT_TOOL = "archledger"

TOOL_REPOS = {
    "archledger": "https://github.com/ledgerwerk/archledger",
    "taskledger": "https://github.com/ledgerwerk/taskledger",
    "releaseledger": "https://github.com/ledgerwerk/releaseledger",
    "ledgercore": "https://github.com/ledgerwerk/ledgercore",
}

TITLE_OVERRIDES = {
    "archledger": {
        "index": "archledger",
        "cli": "archledger CLI guide",
        "configuration": "archledger configuration",
        "source-model": "archledger source model",
        "source-tracking": "archledger source tracking",
        "build-and-export": "archledger build and export",
        "release-process": "archledger release process",
        "agent-workflow": "archledger agent workflow",
        "api": "archledger Python API",
    },
    "taskledger": {
        "index": "taskledger",
        "usage": "taskledger usage",
        "full_task_cycle": "taskledger full task cycle",
        "architecture_taskledger_split": "taskledger architecture split",
        "multi_repo": "taskledger multi-repo workflows",
        "api": "taskledger Python API",
        "public_surface": "taskledger public surface",
        "command_contract": "taskledger command contract",
        "transfer": "taskledger transfer",
        "sync": "taskledger sync",
        "service_boundary_whitelist": "taskledger service boundary whitelist",
    },
    "releaseledger": {
        "index": "releaseledger",
        "quickstart": "releaseledger quickstart",
        "concepts": "releaseledger concepts",
        "commands": "releaseledger commands",
        "changelog": "releaseledger changelog",
        "storage": "releaseledger storage",
        "api": "releaseledger Python API",
        "development": "releaseledger development",
    },
    "ledgercore": {
        "index": "ledgercore",
        "api": "ledgercore Python API",
        "references": "ledgercore references",
        "storage": "ledgercore storage",
        "release": "ledgercore release process",
    },
}

DESCRIPTION_OVERRIDES = {
    "archledger": {
        "index": "Source-first arc42 architecture documentation records",
        "cli": "Command line workflows for archledger",
        "configuration": "Configuration reference for archledger",
        "source-model": "Canonical source format and records for archledger",
        "source-tracking": "Workspace source tracking for archledger",
        "build-and-export": "Native builds, exports, and diagram handling for archledger",
        "release-process": "Release workflow for archledger",
        "agent-workflow": "Agent workflow for maintaining archledger documentation",
        "api": "Python API modules for archledger",
    },
    "taskledger": {
        "index": "Task-first durable state for staged coding work",
        "usage": "Command usage and common taskledger workflows",
        "full_task_cycle": "End-to-end taskledger task lifecycle",
        "architecture_taskledger_split": "Taskledger architecture and split boundaries",
        "multi_repo": "Multi-repository taskledger workflows",
        "api": "Python API modules for taskledger",
        "public_surface": "Supported public surface for integrations",
        "command_contract": "Command behavior and output contracts",
        "transfer": "Task transfer and handoff workflows",
        "sync": "Taskledger sync workflows",
        "service_boundary_whitelist": "Allowed service boundary imports",
    },
    "releaseledger": {
        "index": "Project-local release management for coding workflows",
        "quickstart": "Initialize releaseledger and publish a changelog",
        "concepts": "Release records, entries, refs, events, and indexes",
        "commands": "CLI command groups and common releaseledger workflows",
        "changelog": "Changelog context, review, and rendering workflows",
        "storage": "Releaseledger storage layout and diagnostics",
        "api": "Python API modules for releaseledger",
        "development": "Development workflow for releaseledger",
    },
    "ledgercore": {
        "index": "Shared primitives for ledgerwerk tools",
        "api": "Python API modules for ledgercore",
        "references": "Cross-ledger reference primitives",
        "storage": "Storage helpers and file layout primitives",
        "release": "Release workflow for ledgercore",
    },
}

CARD_LABELS = {
    "archledger": {
        "cli": ("CLI guide", "Command groups, JSON usage, initialization, records, links, references, and source commands."),
        "configuration": ("Configuration", "Project configuration, ID segment modes, build options, and tracking settings."),
        "source-model": ("Source model", "Markdown and AsciiDoc source fragments, records, metadata, and arc42 assembly."),
        "source-tracking": ("Source tracking", "Snapshot files, change detection, and drift review."),
        "build-and-export": ("Build and export", "Native builds, converter-backed exports, diagram records, and source migration."),
        "release-process": ("Release process", "Versioning, checks, and release publication workflow."),
        "agent-workflow": ("Agent workflow", "Recommended commands and boundaries for coding agents."),
        "api": ("Python API", "Public API modules exposed by archledger."),
    },
    "taskledger": {
        "usage": ("Usage", "CLI usage, actor identity, tasks, questions, plans, implementation, validation, and handoffs."),
        "full_task_cycle": ("Full task cycle", "End-to-end planning, implementation, validation, and review lifecycle."),
        "architecture_taskledger_split": ("Architecture split", "Taskledger architecture boundaries and package split notes."),
        "multi_repo": ("Multi-repo", "Patterns for using taskledger across multiple repositories."),
        "api": ("Python API", "Public API modules exposed by taskledger."),
        "public_surface": ("Public surface", "Supported imports and extension points for integrations."),
        "command_contract": ("Command contract", "Command behavior and output contract reference."),
        "transfer": ("Transfer", "Task transfer, export, import, and handoff workflows."),
        "sync": ("Sync", "Synchronization workflows and safety checks."),
        "service_boundary_whitelist": ("Service boundaries", "Allowed service boundary imports and enforcement guidance."),
    },
    "releaseledger": {
        "quickstart": ("Quickstart", "Initialize a project, import git entries, review coverage, and build a changelog."),
        "concepts": ("Concepts", "Release records, entries, source refs, events, commit audit sheets, and indexes."),
        "commands": ("Commands", "CLI command groups and common workflows."),
        "changelog": ("Changelog", "Two-step changelog rendering, strict review, and section correction."),
        "storage": ("Storage", "Default layout, external state directories, and diagnostics."),
        "api": ("Python API", "Public modules to use from integrations."),
        "development": ("Development", "Development setup, validation, and release maintenance."),
    },
    "ledgercore": {
        "api": ("Python API", "Public API modules exposed by ledgercore."),
        "references": ("References", "Global refs, local refs, and cross-ledger reference helpers."),
        "storage": ("Storage", "Atomic writes, safe paths, metadata, and deterministic storage helpers."),
        "release": ("Release", "Versioning, validation, and release publication workflow."),
    },
}


def generated_header(tool: str) -> str:
    return f"<!-- GENERATED from {tool}/docs. Do not edit by hand. -->"


def extract_h1(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else fallback


def yaml_string(value: str) -> str:
    return '"' + value.replace('"', '\\"') + '"'


def convert_code_block_directives(text: str) -> str:
    """Convert common MyST code-block fences to standard Markdown fences."""
    text = re.sub(r"^(```+)\{code-block\}\s+([A-Za-z0-9_+-]+)\s*$", r"\1\2", text, flags=re.MULTILINE)
    return re.sub(r"^(```+)\{code-block\}\s*$", r"\1", text, flags=re.MULTILINE)


def convert_myst_anchors(text: str) -> str:
    """Convert MyST explicit anchors, e.g. (init)=, to stable HTML anchors."""
    return re.sub(
        r"^\(([A-Za-z0-9_.:-]+)\)=$",
        r'<a id="\1"></a>',
        text,
        flags=re.MULTILINE,
    )


def extract_automodule_names(text: str) -> list[str]:
    modules = re.findall(
        r"^```\{automodule\}\s+([^\n]+)\n.*?^```\s*$",
        text,
        flags=re.DOTALL | re.MULTILINE,
    )
    return [module.strip() for module in modules]


def convert_automodule_page(text: str) -> str:
    """Replace Sphinx automodule directives with a Jekyll-friendly module list."""
    modules = extract_automodule_names(text)
    if not modules:
        return text

    lines = [
        "# " + extract_h1(text, "API reference"),
        "",
        "The public Python API is organized around these modules:",
        "",
    ]
    lines.extend(f"- `{module}`" for module in modules)
    lines.extend(
        [
            "",
            "Install the package locally to inspect generated API details with Python help tools, IDE indexers, or the Sphinx package docs.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_toctree_entries(text: str) -> list[str]:
    entries: list[str] = []
    for block in re.findall(r"^```\{toctree\}\n(.*?)^```\s*$", text, flags=re.DOTALL | re.MULTILINE):
        for raw_line in block.splitlines():
            line = raw_line.strip()
            if not line or line.startswith(":"):
                continue
            titled = re.match(r"^.+<([A-Za-z0-9_./-]+)>$", line)
            target = titled.group(1) if titled else line
            if re.match(r"^[A-Za-z0-9_./-]+$", target):
                entries.append(Path(target).stem)

    seen: set[str] = set()
    deduped: list[str] = []
    for entry in entries:
        if entry not in seen:
            seen.add(entry)
            deduped.append(entry)
    return deduped


def strip_sphinx_indices_section(text: str) -> str:
    return re.sub(
        r"\n*## Indices and tables\n\n(?:- \{ref\}`[^`]+`\n?)+",
        "\n",
        text,
        flags=re.MULTILINE,
    )


def card_label(tool: str, entry: str) -> tuple[str, str]:
    labels = CARD_LABELS.get(tool, {})
    return labels.get(entry, (entry.replace("_", " ").replace("-", " ").title(), "Documentation page."))


def convert_toctree_index(text: str, tool: str) -> str:
    """Replace Sphinx toctree blocks with the card grid used by ledgerwerk."""
    if "```{toctree}" not in text:
        return text

    entries = parse_toctree_entries(text)
    intro = re.sub(r"\n?^```\{toctree\}\n.*?^```\s*\n?", "\n", text, flags=re.DOTALL | re.MULTILINE)
    intro = strip_sphinx_indices_section(intro).strip()

    cards = ['<div class="cards">']
    for entry in entries:
        label, description = card_label(tool, entry)
        href = "{{ '/tools/" + tool + "/" + entry + "/' | relative_url }}"
        cards.append(
            f'  <section class="card"><h3><a href="{href}">{label}</a></h3>'
            f"<p>{description}</p></section>"
        )
    cards.append("</div>")

    return intro + "\n\n" + "\n".join(cards) + "\n"


def transform_body(text: str, tool: str) -> str:
    body = text.replace("\r\n", "\n").replace("\r", "\n")
    body = convert_code_block_directives(body)
    body = convert_myst_anchors(body)
    body = convert_automodule_page(body)
    body = convert_toctree_index(body, tool)
    return body.strip() + "\n"


def front_matter(slug: str, source_name: str, tool: str, source_text: str) -> str:
    permalink = f"/tools/{tool}/" if slug == "index" else f"/tools/{tool}/{slug}/"
    fallback_title = extract_h1(source_text, f"{tool} {slug.replace('_', ' ').replace('-', ' ')}")
    title = TITLE_OVERRIDES.get(tool, {}).get(slug, fallback_title)
    description = DESCRIPTION_OVERRIDES.get(tool, {}).get(slug, f"{title} documentation")

    return "\n".join(
        [
            "---",
            "layout: tool-doc",
            f"title: {yaml_string(title)}",
            f"description: {yaml_string(description)}",
            f"permalink: {permalink}",
            f"nav_tool: {tool}",
            f"generated_from: {tool}/docs",
            f"source_path: docs/{source_name}",
            "---",
            "",
        ]
    )


def render_page(src: Path, tool: str) -> str:
    slug = src.stem
    source_text = src.read_text(encoding="utf-8")
    body = transform_body(source_text, tool)
    return front_matter(slug, src.name, tool, source_text) + generated_header(tool) + "\n\n" + body


def nav_entries(tool: str, source_files: list[Path]) -> list[dict]:
    """Build ordered nav entries for a tool.

    Order: index first, then the curated TITLE_OVERRIDES keys, then any
    remaining source files sorted by stem. Each entry has slug, title, url.
    """
    curated = TITLE_OVERRIDES.get(tool, {})
    stems = {path.stem: path for path in source_files}

    order: list[str] = []
    seen: set[str] = set()
    if "index" in stems:
        order.append("index")
        seen.add("index")
    for slug in curated:
        if slug in stems and slug not in seen:
            order.append(slug)
            seen.add(slug)
    for slug in sorted(stems):
        if slug not in seen:
            order.append(slug)
            seen.add(slug)

    entries: list[dict] = []
    for slug in order:
        title = curated.get(slug, slug.replace("_", " ").replace("-", " ").title())
        permalink = f"/tools/{tool}/" if slug == "index" else f"/tools/{tool}/{slug}/"
        entries.append({"slug": slug, "title": title, "url": permalink})
    return entries


def render_nav_yaml(tool: str, entries: list[dict]) -> str:
    lines = [
        f"# GENERATED from {tool}/docs. Do not edit by hand.",
        f"tool: {tool}",
        "entries:",
    ]
    for entry in entries:
        lines.append(f"  - slug: {entry['slug']}")
        lines.append(f"    title: {yaml_string(entry['title'])}")
        lines.append(f"    url: {entry['url']}")
    return "\n".join(lines) + "\n"


def write_nav_data(tool: str, entries: list[dict], data_dir: Path) -> Path:
    nav_dir = data_dir / "tool_nav"
    nav_dir.mkdir(parents=True, exist_ok=True)
    out = nav_dir / f"{tool}.yml"
    out.write_text(render_nav_yaml(tool, entries), encoding="utf-8", newline="\n")
    return out


def sync_docs(
    source_dir: Path,
    dest_dir: Path,
    tool: str,
    clean: bool,
    data_dir: Path | None = None,
) -> tuple[list[Path], Path | None]:
    if tool not in TOOL_REPOS:
        raise SystemExit(f"unsupported tool: {tool}")
    if not source_dir.is_dir():
        raise SystemExit(f"source docs directory does not exist: {source_dir}")

    if data_dir is None:
        # tools/<tool> -> tools -> repo root -> _data
        data_dir = dest_dir.resolve().parent.parent / "_data"

    if clean and dest_dir.exists():
        shutil.rmtree(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    source_files = sorted(source_dir.glob("*.md"))
    if not source_files:
        raise SystemExit(f"no markdown files found in {source_dir}")

    written: list[Path] = []
    for src in source_files:
        out = dest_dir / src.name
        out.write_text(render_page(src, tool), encoding="utf-8", newline="\n")
        written.append(out)

    nav_file = write_nav_data(tool, nav_entries(tool, source_files), data_dir)

    return written, nav_file


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path, help="Path to a ledgerwerk tool docs directory")
    parser.add_argument("--dest", required=True, type=Path, help="Destination, e.g. tools/archledger")
    parser.add_argument("--tool", default=DEFAULT_TOOL, choices=sorted(TOOL_REPOS))
    parser.add_argument("--no-clean", action="store_true", help="Do not delete destination before writing")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=None,
        help="Repository _data directory for the generated tool_nav files (default: <dest>/../../_data)",
    )
    args = parser.parse_args()

    written, nav_file = sync_docs(
        source_dir=args.source,
        dest_dir=args.dest,
        tool=args.tool,
        clean=not args.no_clean,
        data_dir=args.data_dir,
    )
    for path in written:
        print(path)
    if nav_file is not None:
        print(nav_file)


if __name__ == "__main__":
    main()
