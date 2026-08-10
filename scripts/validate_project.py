#!/usr/bin/env python3
"""Deterministisk validering för Arduino i praktiken.

Valideringen är avsedd för både lokal körning och GitHub Actions.
Den använder endast Python-standardbiblioteket och projektets faktiska struktur.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REQUIRED_PATHS = (
    "README.md",
    "book.yaml",
    "docs/export-metadata.yaml",
    "chapters/00-inledning.md",
    "scripts/export-book.py",
    "scripts/build_book.py",
    "styles/epub.css",
    "styles/pdf.css",
    ".github/workflows/01-validate.yml",
    ".github/workflows/02-build-preview.yml",
    ".github/workflows/03-release.yml",
)

FORBIDDEN_READER_MARKERS = (
    "Praktiskt test",
    "Prova själv",
    "Prova vidare",
    "Efter kapitlet ska",
    "Kontrollera att du hänger med",
    "experimentlogg",
    "docs/lookup-index.md",
)

WORK_MARKERS = ("TODO", "FIXME", "[PLACEHOLDER]")


def add_error(errors: list[str], message: str) -> None:
    errors.append(message)
    print(f"ERROR: {message}", file=sys.stderr)


def parse_book_yaml(path: Path) -> dict[str, object]:
    """Läs de metadatafält CI behöver utan extern YAML-parser."""
    data: dict[str, object] = {}
    chapters: list[str] = []
    in_chapters = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if stripped == "chapters:":
            in_chapters = True
            data["chapters"] = chapters
            continue

        if in_chapters:
            if stripped.startswith("- "):
                chapters.append(stripped[2:].strip().strip("'\""))
                continue
            if line and not line.startswith((" ", "\t")):
                in_chapters = False

        if not in_chapters and ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip().strip("'\"")
            if key:
                data[key] = value

    return data


def is_table_separator(line: str) -> bool:
    return bool(re.match(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$", line.strip()))


def count_table_cells(line: str) -> int:
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        return -1
    return len(stripped.strip("|").split("|"))


def validate_chapter(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not text.strip():
        add_error(errors, f"Tom kapitel-/manusfil: {path}")

    if text.count("```") % 2 != 0:
        add_error(errors, f"Obalanserade kodblock: {path}")

    in_code = False
    h1_count = 0

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue

        if re.match(r"^#{4,6}\s+", line):
            add_error(errors, f"H4 eller djupare rubrik i {path} rad {idx}")

        if re.match(r"^#(?!#)\s+", line):
            h1_count += 1

        if re.match(r"^###\s+(Mål|Syfte|Material|Reflektion)\s*$", line):
            add_error(errors, f"Gammal labbrubrik i {path} rad {idx}: {stripped}")

        if stripped.startswith("|") and stripped.endswith("|"):
            cells = count_table_cells(line)
            if idx < len(lines) and lines[idx].strip().startswith("|"):
                next_cells = count_table_cells(lines[idx])
                if cells > 0 and next_cells > 0 and cells != next_cells:
                    add_error(errors, f"Tabellrader med olika antal celler i {path} rad {idx}")

            if idx == 1 or not lines[idx - 2].strip().startswith("|"):
                if idx < len(lines) and not is_table_separator(lines[idx]):
                    add_error(errors, f"Möjlig tabell utan separatorrad i {path} rad {idx}")

    if h1_count != 1:
        add_error(errors, f"{path} ska ha exakt en H1-rubrik, hittade {h1_count}")

    for marker in FORBIDDEN_READER_MARKERS:
        if marker in text:
            add_error(errors, f"Förbjudet läsarspår i {path}: {marker}")

    for marker in WORK_MARKERS:
        if marker in text:
            add_error(errors, f"Arbetsmarkör kvar i {path}: {marker}")


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(root.rglob("*.md")):
        if any(part in {".git"} for part in md.relative_to(root).parts):
            continue
        text = md.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            if " " in target and not target.startswith(("./", "../")):
                target = target.split(" ", 1)[0]
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if not candidate.exists():
                add_error(errors, f"Trasig intern Markdown-länk i {md.relative_to(root)}: {target}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []

    if not root.is_dir():
        add_error(errors, f"Projektkatalogen finns inte: {root}")
        return 1

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            add_error(errors, f"Obligatorisk projektsökväg saknas: {rel}")

    book_yaml = root / "book.yaml"
    if book_yaml.exists():
        metadata = parse_book_yaml(book_yaml)
        for key in ("title", "author", "language", "version", "identifier"):
            if not metadata.get(key):
                add_error(errors, f"book.yaml saknar metadatafält: {key}")

        chapters = metadata.get("chapters")
        if not isinstance(chapters, list) or not chapters:
            add_error(errors, "book.yaml saknar kapitelordning.")
        else:
            seen: set[str] = set()
            for rel in chapters:
                if rel in seen:
                    add_error(errors, f"Dubblett i kapitelordning: {rel}")
                seen.add(rel)
                chapter_path = root / rel
                if not chapter_path.exists():
                    add_error(errors, f"Kapitel i book.yaml saknas: {rel}")
                else:
                    validate_chapter(chapter_path, errors)

            actual = sorted(str(p.relative_to(root)).replace("\\", "/") for p in (root / "chapters").glob("*.md"))
            missing_from_metadata = [p for p in actual if p not in seen]
            if missing_from_metadata:
                add_error(errors, f"Kapitel saknas i book.yaml: {', '.join(missing_from_metadata)}")

    validate_markdown_links(root, errors)

    if errors:
        print(f"Validering misslyckades med {len(errors)} fel.", file=sys.stderr)
        return 1

    print("Validering klar utan fel.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
