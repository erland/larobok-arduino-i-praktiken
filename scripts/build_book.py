#!/usr/bin/env python3
"""Bygg EPUB/PDF för GitHub Actions och lokal preview.

Det här är ett tunt CI-orienterat lager ovanpå projektets ordinarie exportpipeline:
`scripts/export-book.py`. Bygglogiken ligger därmed i scripts, medan GitHub Actions
bara installerar verktyg, startar validering/build och publicerar artifacts.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
EPUB_NS = "http://www.idpf.org/2007/ops"
OPF_NS = "http://www.idpf.org/2007/opf"
XHTML_NS = "http://www.w3.org/1999/xhtml"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def validate_epub(path: Path) -> None:
    if not path.exists():
        raise RuntimeError(f"EPUB saknas: {path}")

    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            raise RuntimeError("EPUB-fel: mimetype ligger inte först.")
        if archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise RuntimeError("EPUB-fel: mimetype är komprimerad.")

        container = ET.fromstring(archive.read("META-INF/container.xml"))
        rootfile = container.find(".//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile")
        if rootfile is None:
            raise RuntimeError("EPUB-fel: OPF-root saknas.")
        opf_name = rootfile.attrib["full-path"]
        opf = ET.fromstring(archive.read(opf_name))
        ns = {"opf": OPF_NS}
        manifest = opf.find("opf:manifest", ns)
        spine = opf.find("opf:spine", ns)
        if manifest is None or spine is None:
            raise RuntimeError("EPUB-fel: manifest/spine saknas.")

        nav_item = next(
            (
                item for item in manifest.findall("opf:item", ns)
                if "nav" in item.attrib.get("properties", "").split()
            ),
            None,
        )
        if nav_item is None:
            raise RuntimeError("EPUB-fel: nav.xhtml saknas i manifestet.")

        nav_id = nav_item.attrib["id"]
        nav_refs = [
            ref for ref in spine.findall("opf:itemref", ns)
            if ref.attrib.get("idref") == nav_id
        ]
        if nav_refs and any(ref.attrib.get("linear") != "no" for ref in nav_refs):
            raise RuntimeError("EPUB-fel: nav.xhtml är linjär i spine.")

        nav_path = (Path(opf_name).parent / nav_item.attrib["href"]).as_posix()
        nav_root = ET.fromstring(archive.read(nav_path))
        nav_ns = {"x": XHTML_NS, "epub": EPUB_NS}
        anchors = nav_root.findall(".//x:nav[@epub:type='toc']//x:a", nav_ns)
        chapter_labels = ["".join(anchor.itertext()).strip() for anchor in anchors]
        numbered = [label for label in chapter_labels if label[:1].isdigit()]
        if len(numbered) < 38:
            raise RuntimeError(f"EPUB-fel: TOC verkar ofullständig ({len(numbered)} numrerade kapitelposter).")


def copy_outputs(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    expected = [
        (ROOT / "exports" / "arduino-i-praktiken.epub", output_dir / "arduino-i-praktiken.epub"),
        (ROOT / "exports" / "arduino-i-praktiken.pdf", output_dir / "arduino-i-praktiken.pdf"),
    ]
    for src, dst in expected:
        if not src.exists():
            raise RuntimeError(f"Förväntad exportfil saknas: {src}")
        shutil.copy2(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(ROOT / "exports"))
    parser.add_argument("--skip-project-validator", action="store_true")
    args = parser.parse_args()

    if not args.skip_project_validator:
        run([sys.executable, "scripts/validate_project.py", "."])

    run([sys.executable, "scripts/export-book.py", "all"])

    epub = ROOT / "exports" / "arduino-i-praktiken.epub"
    validate_epub(epub)

    copy_outputs(Path(args.output_dir))
    print(f"Byggde EPUB/PDF till {Path(args.output_dir).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
