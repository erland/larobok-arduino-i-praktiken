# Exportförberedande granskning

Datum: 2026-06-30  
Bok: *Arduino i praktiken*  
Undertitel: *Din guide till Arduino och elektronikkretsar*  
Författare: Erland Lindmark

## Sammanfattning

Projektet är i huvudsak exportklart som manusprojekt. Kapitelordningen finns i metadata, samtliga kapitel i metadata finns i `chapters/`, rubriknivåerna följer H1-H3, tabellerna är giltiga markdown-tabeller och listblocken har normaliserats för stabilare rendering.

Granskningen identifierade och åtgärdade några mindre exportproblem:

- saknade kataloger för `exports/`, `assets/cover/` och `assets/images/` efter zip/extrahering,
- boxritningstecken i två kod-/diagramblock som gav PDF-fontvarningar,
- några listor som saknade tomrad före listblock,
- exportscriptet skapade inte `exports/` automatiskt innan Pandoc kördes,
- exportscriptets validering kunde förbättras så att den ignorerar rubriker inne i kodblock och varnar tydligare om omslagsbild saknas.

## Kontroller

| Område | Resultat | Kommentar |
|---|---|---|
| Metadata | Godkänt | Titel, undertitel, författare, språk, identifierare, datum, version och kapitelordning finns. Datum uppdaterat till 2026-06-30. |
| Kapitelordning | Godkänt | 39 filer i ordning: `00-inledning.md` plus kapitel 1-38. |
| Rubriknivåer | Godkänt | Kapitel har exakt en H1 utanför kodblock. Inga H4-H6 hittades i boktext. |
| Kodblock | Godkänt | Kodblock är balanserade. Rubriker inne i markdown-exempel behandlas som kodexempel. |
| Tabeller | Godkänt | Tabeller har separatorrad, jämnt cellantal och tomrad före/efter. |
| Listor | Åtgärdat | Listblock med saknad tomrad före listan normaliserades. |
| Bildreferenser | Godkänt med notering | Inga kapitelbilder refereras. Metadata pekar på `assets/cover/cover.png`, men själva omslagsbilden är ännu inte skapad. |
| EPUB-pipeline | Godkänt | Scriptet använder Pandoc EPUB3 med `--toc --toc-depth=1` och EPUB-CSS. |
| PDF-pipeline | Godkänt med lokal verktygsreservation | Scriptet använder Pandoc och `xelatex`. I denna miljö kunde PDF-export köras efter teckenkorrigering, men användarens lokala dator behöver Pandoc och en PDF-engine installerad. |
| Projektstruktur | Åtgärdat | Saknade tomma kataloger återskapades med `.gitkeep`. |

## Åtgärdade filer

- `chapters/valja-ratt-kort-02.md`
- `chapters/utvecklingsmiljo-bibliotek-03.md`
- `chapters/raspberry-pi-pico-15.md`
- `chapters/stromforsorjning-batteridrift-34.md`
- `chapters/breadboard-till-modul-36.md`
- `chapters/modular-sensor-styrstation-37.md`
- `scripts/export-book.py`
- `scripts/export-book.sh`
- `docs/export-metadata.yaml`
- `book.yaml`
- `exports/.gitkeep`
- `assets/cover/.gitkeep`
- `assets/images/.gitkeep`

## Kvarstående noteringar före skarp EPUB/PDF-export

### Omslag

Boken är konfigurerad för omslag via:

```yaml
cover_image: "assets/cover/cover.png"
```

Filen finns ännu inte. Det är inte ett manusfel, men slutlig EPUB med omslag kräver att `assets/cover/cover.png` skapas eller att `cover_image` lämnas tomt tills omslaget är klart.

Omslagsprompten finns i:

```text
assets/image-prompts/COVER.md
```

### Lokala exportkrav

För lokal export behövs:

- Python 3
- PyYAML
- Pandoc
- för PDF: `xelatex` eller annan Pandoc-kompatibel PDF-engine

Validering:

```bash
scripts/export-book.sh validate
```

EPUB:

```bash
scripts/export-book.sh epub --allow-warnings
```

PDF:

```bash
scripts/export-book.sh pdf --allow-warnings
```

Flaggan `--allow-warnings` behövs tills omslagsbilden finns, eftersom valideringen medvetet varnar för saknad `assets/cover/cover.png`.

## Rekommenderat nästa steg

Nästa steg är att skapa eller välja omslagsbild, lägga den som `assets/cover/cover.png`, och därefter köra faktisk EPUB/PDF-export.
