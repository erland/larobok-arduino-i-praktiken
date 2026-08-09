# EPUB-export

## Export
- Fil: `exports/arduino-i-praktiken.epub`
- Titel: Arduino i praktiken
- Undertitel: Din guide till Arduino och elektronikkretsar
- Författare: Erland Lindmark
- Språk: sv-SE
- Skapad med: Pandoc EPUB3
- Datum: 2026-06-30

## Kontroller
- Projektets markdownvalidering: godkänd utan varningar.
- Omslag: `assets/cover/cover.png` inbäddat i EPUB.
- EPUB-navigation: `nav.xhtml` finns.
- EPUB-TOC: genererad med `--toc --toc-depth=1`.
- Synlig innehållsförteckningssida: ingen separat markdown-TOC skapad.
- `nav.xhtml` i spine: satt till `linear="no"` så den inte visas som vanlig lässida.
- CSS: `styles/epub.css` används och är anpassad för luftig EPUB-layout.

## Kommentar
EPUB-filen är skapad lokalt med projektets Pandoc-pipeline. `epubcheck` fanns inte installerat i miljön, så formell EPUBCheck-validering kunde inte köras här.
