# EPUB-export efter post-v5-justeringar

## Utgångspunkt

Projektet exporterades efter de samlade post-v5-justeringarna av kapitel 1–38, senast dokumenterade i `docs/post-v5-chapters-33-38-adjustment.md`.

## Export

Genererad fil:

- `exports/arduino-i-praktiken.epub`

## Kontroller

Följande kontroller genomfördes före/vid export:

- `scripts/export-book.py validate` kördes utan projektvarningar.
- `build/book.md` byggdes om via projektets exportscript.
- EPUB exporterades med projektets Pandoc-baserade standard.
- EPUB-navigation (`nav.xhtml`) finns.
- Navigationsfilen är markerad som icke-linjär i EPUB-spine.
- EPUB-TOC bygger på kapitelnivå enligt projektstandard.

## Sökta äldre rubriker och interna spår

Följande gamla rubriker/formuleringar hittades inte i EPUB-exporten:

- `Praktiskt test`
- `Prova själv`
- `Prova vidare`
- `Snabb orientering`
- `Efter kapitlet ska`
- `docs/lookup-index.md`

## Kommentar

Exporten är skapad för läsning/test efter den redaktionella rensningen av kapitel 1–38. Denna export ersätter inte versionssättning till en ny huvudversion, utan är en post-v5-export från aktuell projektstatus.
