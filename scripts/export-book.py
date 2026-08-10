#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import html
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Saknar Python-paketet PyYAML. Installera med: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]


def load_metadata() -> dict:
    candidates = [ROOT / "book.yaml", ROOT / "docs" / "export-metadata.yaml"]
    data: dict = {}
    for path in candidates:
        if path.exists():
            with path.open("r", encoding="utf-8") as f:
                loaded = yaml.safe_load(f) or {}
                data.update(loaded)
    return data


def lang_tag(metadata: dict) -> str:
    language = metadata.get("language", "sv")
    if language == "sv":
        return "sv-SE"
    if language == "en":
        return "en-US"
    return str(language)


def count_table_cells(line: str) -> int:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return -1
    return len([c for c in stripped.strip("|").split("|")])


def is_table_separator(line: str) -> bool:
    return bool(re.match(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$", line.strip()))


def validate_markdown(chapter_paths: list[Path], metadata: dict) -> list[str]:
    warnings: list[str] = []
    image_pattern = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")

    cover = metadata.get("cover_image")
    if cover and not (ROOT / cover).exists():
        warnings.append(f"Metadata anger cover_image='{cover}', men filen saknas. Export fortsätter utan omslag om bilden inte skapas.")

    for path in chapter_paths:
        if not path.exists():
            warnings.append(f"Saknat kapitel: {path}")
            continue

        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        if text.count("```") % 2 != 0:
            warnings.append(f"{path}: ojämnt antal kodblockmarkörer.")

        in_code = False
        h1_count = 0

        for idx, line in enumerate(lines):
            stripped = line.strip()

            if stripped.startswith("```"):
                in_code = not in_code
                continue

            if in_code:
                continue

            if re.match(r"^#{4,6}\s", line):
                warnings.append(f"{path}: innehåller H4 eller djupare rubrik nära rad {idx + 1}.")

            if re.match(r"^#(?!#)\s+", line):
                h1_count += 1

            # Listor bör ha tomrad före första listpunkten om den följer direkt efter brödtext.
            if re.match(r"^\s{0,6}([-*+]|\d+\.)\s+", line):
                prev = lines[idx - 1] if idx > 0 else ""
                prev_is_list = bool(re.match(r"^\s{0,6}([-*+]|\d+\.)\s+", prev))
                if idx > 0 and prev.strip() and not prev_is_list:
                    warnings.append(f"{path}: lista saknar tomrad före rad {idx + 1}.")

            if stripped.startswith("|") and stripped.endswith("|"):
                if idx == 0 or not lines[idx - 1].strip().startswith("|"):
                    if idx > 0 and lines[idx - 1].strip():
                        warnings.append(f"{path}: tabell saknar tomrad före rad {idx + 1}.")
                    if idx + 1 >= len(lines) or not is_table_separator(lines[idx + 1]):
                        warnings.append(f"{path}: möjlig tabell utan korrekt separatorrad nära rad {idx + 1}.")
                cells = count_table_cells(line)
                if cells > 0 and idx + 1 < len(lines) and lines[idx + 1].strip().startswith("|"):
                    next_cells = count_table_cells(lines[idx + 1])
                    if next_cells > 0 and cells != next_cells:
                        warnings.append(f"{path}: tabellrader med olika antal celler nära rad {idx + 1}.")
                if idx + 1 < len(lines) and not lines[idx + 1].strip().startswith("|") and lines[idx + 1].strip():
                    warnings.append(f"{path}: tabell saknar tomrad efter rad {idx + 1}.")

        if h1_count != 1:
            warnings.append(f"{path}: bör ha exakt en H1-rubrik, hittade {h1_count}.")

        for match in image_pattern.finditer(text):
            target = match.group(1).split("#")[0]
            if target.startswith(("http://", "https://")):
                continue
            image_path = (path.parent / target).resolve()
            if not image_path.exists():
                warnings.append(f"{path}: bildreferens saknas: {target}")

    return warnings


def build_markdown(metadata: dict, chapter_paths: list[Path]) -> Path:
    build_dir = ROOT / "build"
    build_dir.mkdir(exist_ok=True)
    out = build_dir / "book.md"
    parts: list[str] = []

    for path in chapter_paths:
        if not path.exists():
            raise FileNotFoundError(f"Saknat kapitel: {path}")
        parts.append(path.read_text(encoding="utf-8").rstrip() + "\n")

    out.write_text("\n\n".join(parts), encoding="utf-8")
    return out


def build_epub_markdown(book_md: Path) -> Path:
    """Skapa en EPUB-specifik markdownfil med delade kapitelrubriker.

    Kapitelrubriker på formen "# 12. Kapitelnamn" renderas i EPUB som två rader:
    kapitelnummer och kapitelnamn. Den ordinarie build/book.md lämnas oförändrad så
    källmanus och andra exporter kan fortsätta använda vanlig markdown.
    """
    out = ROOT / "build" / "book-epub.md"
    source = book_md.read_text(encoding="utf-8")

    def replace(match: re.Match[str]) -> str:
        number = match.group(1)
        title = match.group(2).strip()
        safe_title = html.escape(title, quote=False)
        return (
            f'# <span class="chapter-number">{number}.</span>'
            f'<br />'
            f'<span class="chapter-title">{safe_title}</span>'
        )

    transformed = re.sub(r"^#\s+(\d+)\.\s+(.+?)\s*$", replace, source, flags=re.MULTILINE)
    out.write_text(transformed, encoding="utf-8")
    return out


def latex_escape(text: str) -> str:
    """Escape minimal LaTeX-specialtecken i rubriktext för PDF-specifik markdown."""
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def build_pdf_markdown(book_md: Path) -> Path:
    """Skapa PDF-specifik markdown med typografiska H1-rubriker.

    PDF-exporten behöver delade kapitelrubriker och sidbrytning före varje H1,
    men TOC ska fortfarande visa kompakt kapitelrubrik på en rad. Detta görs med
    raw LaTeX-kommandon i en tillfällig PDF-markdownfil. Källmanus och
    build/book.md lämnas oförändrade.
    """
    out = ROOT / "build" / "book-pdf.md"
    source = book_md.read_text(encoding="utf-8")

    def replace_numbered(match: re.Match[str]) -> str:
        number = latex_escape(match.group(1))
        title = latex_escape(match.group(2).strip())
        return f"\\ArduinoChapter{{{number}}}{{{title}}}"

    def replace_unnumbered(match: re.Match[str]) -> str:
        title = latex_escape(match.group(1).strip())
        return f"\\ArduinoFrontChapter{{{title}}}"

    transformed = re.sub(r"^#\s+(\d+)\.\s+(.+?)\s*$", replace_numbered, source, flags=re.MULTILINE)
    transformed = re.sub(r"^#\s+([^#\n].+?)\s*$", replace_unnumbered, transformed, flags=re.MULTILINE)
    out.write_text(transformed, encoding="utf-8")
    return out


def build_pdf_header(metadata: dict) -> Path:
    """Skapa LaTeX-header för PDF-export."""
    out = ROOT / "build" / "pdf-header.tex"
    cover = metadata.get("cover_image")
    cover_exists = bool(cover and (ROOT / cover).exists())
    cover_path = str((ROOT / cover).resolve()).replace("\\", "/") if cover_exists else ""

    cover_block = ""
    if cover_exists:
        cover_block = (
            "\\AtBeginDocument{%\n"
            "  \\thispagestyle{empty}%\n"
            "  \\begin{center}%\n"
            "  \\vspace*{0.5cm}%\n"
            f"  \\includegraphics[width=0.92\\textwidth,height=0.88\\textheight,keepaspectratio]{{{cover_path}}}%\n"
            "  \\end{center}%\n"
            "  \\clearpage%\n"
            "}%\n"
        )

    out.write_text(
        "\\usepackage{graphicx}\n"
        "\\usepackage{hyperref}\n"
        "\n"
        "% PDF-specifika kapitelkommandon. TOC-posten är kompakt, rubriken i flödet delas på två rader.\n"
        "\\newcommand{\\ArduinoChapter}[2]{%\n"
        "  \\clearpage%\n"
        "  \\phantomsection%\n"
        "  \\addcontentsline{toc}{section}{#1. #2}%\n"
        "  \\begin{center}%\n"
        "    {\\fontsize{19}{22}\\selectfont\\normalfont #1.}\\\\[-0.12em]%\n"
        "    {\\fontsize{25}{29}\\selectfont\\bfseries #2}%\n"
        "  \\end{center}%\n"
        "  \\vspace{1.0em}%\n"
        "}\n"
        "\\newcommand{\\ArduinoFrontChapter}[1]{%\n"
        "  \\clearpage%\n"
        "  \\phantomsection%\n"
        "  \\addcontentsline{toc}{section}{#1}%\n"
        "  \\begin{center}%\n"
        "    {\\fontsize{25}{29}\\selectfont\\bfseries #1}%\n"
        "  \\end{center}%\n"
        "  \\vspace{1.0em}%\n"
        "}\n"
        "\n"
        f"{cover_block}",
        encoding="utf-8",
    )
    return out


def run_pandoc(args: list[str]) -> None:
    if shutil.which("pandoc") is None:
        raise RuntimeError("Pandoc saknas. Installera Pandoc och kör exporten igen.")
    subprocess.run(args, cwd=ROOT, check=True)


def patch_epub_nav(epub_path: Path) -> None:
    """Efterkontrollera och normalisera EPUB-navigationen.

    Pandoc skapar en korrekt nav.xhtml, men vissa versioner placerar även
    navigationen i spine som en vanlig lässida. Projektstandarden vill behålla
    nav.xhtml som EPUB-navigation men inte visa den som en vanlig textsida.
    Därför sätts nav-item i spine till linear="no" när den finns där.

    EPUB-kapitelrubriker delas visuellt i brödtexten med span-element. I läsarens
    navigations-TOC ska samma rubrik däremot visas kompakt som "12. Kapitelnamn".
    """
    with zipfile.ZipFile(epub_path, "r") as zf:
        names = zf.namelist()
        nav_names = [name for name in names if name.endswith("nav.xhtml") or name.endswith("nav.html")]
        if not nav_names:
            print("Varning: EPUB verkar sakna nav.xhtml/nav.html.", file=sys.stderr)
            return

        opf_names = [name for name in names if name.endswith(".opf")]
        if not opf_names:
            print("Varning: EPUB verkar sakna OPF-fil.", file=sys.stderr)
            return

        opf_name = opf_names[0]
        nav_name = nav_names[0]
        opf_text = zf.read(opf_name).decode("utf-8")
        nav_text = zf.read(nav_name).decode("utf-8")

    # Sätt itemref idref="nav" till linear="no" om det ligger i spine.
    patched_opf = re.sub(
        r'<itemref\s+idref="nav"\s*/>',
        '<itemref idref="nav" linear="no" />',
        opf_text,
    )
    patched_opf = re.sub(
        r'<itemref\s+idref="nav"\s+linear="yes"\s*/>',
        '<itemref idref="nav" linear="no" />',
        patched_opf,
    )

    def compact_nav_heading(match: re.Match[str]) -> str:
        prefix, number, title, suffix = match.groups()
        return f"{prefix}{number}. {title}{suffix}"

    patched_nav = re.sub(
        r'(<a\s+[^>]*>)<span class="chapter-number">(\d+)\.</span>\s*<br\s*/?>\s*<span class="chapter-title">([^<]+)</span>(</a>)',
        compact_nav_heading,
        nav_text,
    )

    if patched_opf == opf_text and patched_nav == nav_text:
        return

    tmp = epub_path.with_suffix(".tmp.epub")
    with zipfile.ZipFile(epub_path, "r") as src, zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == opf_name:
                data = patched_opf.encode("utf-8")
            elif item.filename == nav_name:
                data = patched_nav.encode("utf-8")
            dst.writestr(item, data)

    tmp.replace(epub_path)


def export_epub(metadata: dict, book_md: Path) -> Path:
    exports = ROOT / "exports"
    exports.mkdir(exist_ok=True)
    out = exports / "arduino-i-praktiken.epub"
    epub_md = build_epub_markdown(book_md)
    cmd = [
        "pandoc", str(epub_md),
        "--from=gfm",
        "--to=epub3",
        "--toc",
        "--toc-depth=1",
        f"--metadata=title:{metadata.get('title', '')}",
        f"--metadata=subtitle:{metadata.get('subtitle', '')}",
        f"--metadata=author:{metadata.get('author', '')}",
        f"--metadata=lang:{lang_tag(metadata)}",
        "--css=styles/epub.css",
        f"--output={out}",
    ]
    cover = metadata.get("cover_image")
    if cover and (ROOT / cover).exists():
        cmd.insert(-1, f"--epub-cover-image={cover}")
    run_pandoc(cmd)
    patch_epub_nav(out)
    return out


def export_pdf(metadata: dict, book_md: Path) -> Path:
    exports = ROOT / "exports"
    exports.mkdir(exist_ok=True)
    out = exports / "arduino-i-praktiken.pdf"
    pdf_toc_depth = int(((metadata.get("exports") or {}).get("pdf") or {}).get("toc_depth", 1))
    pdf_md = build_pdf_markdown(book_md)
    cmd = [
        "pandoc", str(pdf_md),
        "--from=markdown+raw_tex",
        "--pdf-engine=xelatex",
        "--toc",
        f"--toc-depth={pdf_toc_depth}",
        f"--metadata=title:{metadata.get('title', '')}",
        f"--metadata=subtitle:{metadata.get('subtitle', '')}",
        f"--metadata=author:{metadata.get('author', '')}",
        f"--metadata=lang:{lang_tag(metadata)}",
        f"--output={out}",
    ]
    pdf_header = build_pdf_header(metadata)
    cmd.insert(-1, f"--include-in-header={pdf_header}")
    run_pandoc(cmd)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Exportera bokprojektet till EPUB/PDF.")
    parser.add_argument("target", choices=["validate", "markdown", "epub", "pdf", "all"], nargs="?", default="validate")
    parser.add_argument("--allow-warnings", action="store_true", help="Fortsätt export trots valideringsvarningar.")
    args = parser.parse_args()

    metadata = load_metadata()
    chapters = metadata.get("chapters", [])
    if not metadata.get("title"):
        print("Metadata saknar title.", file=sys.stderr)
        return 1
    if not metadata.get("author"):
        print("Metadata saknar author.", file=sys.stderr)
        return 1
    if metadata.get("language") not in {"sv", "en"}:
        print("Metadata language måste vara sv eller en.", file=sys.stderr)
        return 1
    if not metadata.get("identifier"):
        print("Metadata saknar identifier.", file=sys.stderr)
        return 1
    if not metadata.get("date"):
        print("Metadata saknar date.", file=sys.stderr)
        return 1
    if not chapters:
        print("Metadata saknar kapitelordning.", file=sys.stderr)
        return 1

    chapter_paths = [(ROOT / c) for c in chapters]
    warnings = validate_markdown(chapter_paths, metadata)
    if warnings:
        print("Valideringsvarningar:", file=sys.stderr)
        for w in warnings:
            print(f"- {w}", file=sys.stderr)
        if not args.allow_warnings and args.target not in {"validate", "markdown"}:
            print("Export stoppad. Kör med --allow-warnings om du vill fortsätta ändå.", file=sys.stderr)
            return 1

    if args.target == "validate":
        if warnings:
            print("Validering klar med varningar.")
        else:
            print("Validering klar utan varningar.")
        return 0

    book_md = build_markdown(metadata, chapter_paths)
    if args.target == "markdown":
        print(f"Skapade {book_md}")
        return 0

    if args.target in {"epub", "all"}:
        out = export_epub(metadata, book_md)
        print(f"Skapade {out}")

    if args.target in {"pdf", "all"}:
        out = export_pdf(metadata, book_md)
        print(f"Skapade {out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
