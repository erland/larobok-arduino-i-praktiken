# [PLAN3] Steg 6: Markdown- och exportkontroll

Datum: 2026-07-01  
Status: Genomfört

## Syfte

Detta steg kontrollerar att projektet efter `[PLAN3]` steg 1–5 fortfarande är stabilt för lokal export till Markdown, EPUB och PDF.

Kontrollen gäller särskilt:

- kapitelordning,
- rubriknivåer,
- gamla kursrubriker,
- kvarvarande `Se också`,
- kodblock,
- bildreferenser,
- överlapp mellan `Snabb sammanfattning` och `Snabbreferens`,
- lokal exportpipeline.

## Genomförda kontroller

| Kontroll | Resultat |
|---|---|
| Kapitel enligt metadata | Godkänd |
| Saknade kapitel | Inga |
| Exakt en H1 per kapitel | Godkänd |
| H4 eller djupare rubriker | Inga hittade |
| Obalanserade kodblock | Inga hittade |
| Saknade bildreferenser | Inga hittade |
| Gamla kursrubriker som H2/H3 | Inga hittade |
| `## Se också` | Inga hittade |
| Kapitel med både `Snabb sammanfattning` och `Snabbreferens` | Inga hittade |
| `scripts/export-book.py validate` | Godkänd utan varningar |
| `scripts/export-book.py markdown` | `build/book.md` skapad |
| `scripts/export-book.py epub` | EPUB skapad |
| `scripts/export-book.py pdf` | PDF skapad |

## Mindre korrigering

PDF-exporten fungerade, men LaTeX/Pandoc gav först varningar om tecknet `≈` i monospaced font. För att undvika fontvarningar och göra exporten robustare ersattes dessa förekomster med svensk löptext, till exempel `är ungefär`.

Berörda kapitel:

- `chapters/elektriska-grunder-04.md`
- `chapters/strom-spanning-energi-28.md`
- `chapters/analog-signalanpassning-33.md`

## Exportresultat

Följande filer har uppdaterats eller skapats:

- `build/book.md`
- `exports/arduino-i-praktiken.epub`
- `exports/arduino-i-praktiken.pdf`

EPUB-kontroll:

- `EPUB/nav.xhtml` finns.
- `content.opf` innehåller `itemref idref="nav" linear="no"`.
- EPUB-navigationen är därmed kvar, men ska inte visas som vanlig lässida.

PDF-kontroll:

- PDF skapades med Pandoc och `xelatex`.
- PDF har 729 sidor.
- Dokumentmetadata innehåller titel och författare.
- PDF har innehållsförteckning/outline.
- Ett stickprov renderades till bild för att kontrollera att PDF-filen går att läsa/rendera.

## Bedömning

`[PLAN3]` steg 6 är godkänt.

Projektet är redo för `[PLAN3]` steg 7: skapa `handbokstruktur-v2`.
