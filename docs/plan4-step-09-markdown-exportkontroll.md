# [PLAN4] Steg 9: Markdown- och exportkontroll

## Syfte

Detta steg kontrollerar att kompletteringarna från `[PLAN4]` steg 1–8 fortfarande ger ett stabilt bokprojekt som kan byggas till Markdown, EPUB och PDF.

Kontrollen omfattar:

- kapitelstruktur och rubriknivåer,
- tidigare borttagna kursrubriker,
- `Se också`/`Relaterat`-principen,
- kodblock, tabeller och bildreferenser,
- lokal exportpipeline,
- EPUB-navigation,
- PDF-rendering genom stickprov.

## Kontrollerade filer och export

| Område | Resultat |
|---|---|
| Kapitelordning | Godkänd |
| Antal kapitel inklusive inledning | 39 |
| Exakt en H1 per kapitel | Godkänd |
| H4 eller djupare rubriker | Inga hittade |
| Obalanserade kodblock | Inga hittade |
| Saknade bildreferenser | Inga hittade |
| Gamla kursrubriker som H2/H3 | Inga hittade |
| `## Se också` | Inga hittade |
| Kapitel med både `Snabb sammanfattning` och `Snabbreferens` | Inga hittade |
| `Relaterat` | Finns kvar selektivt i 24 kapitel |
| `scripts/export-book.py validate` | Godkänd utan varningar |
| `build/book.md` | Ombyggd |
| EPUB-export | Godkänd |
| PDF-export | Godkänd |
| EPUB-navigation | `EPUB/nav.xhtml` finns |
| EPUB-nav i spine | Satt till `linear="no"` |
| PDF-stickprov | Renderat utan fel |

## Exportkommandon

Följande kommandon kördes från projektroten:

```bash
python3 scripts/export-book.py validate
python3 scripts/export-book.py all
```

Resultat:

```text
Validering klar utan varningar.
Skapade exports/arduino-i-praktiken.epub
Skapade exports/arduino-i-praktiken.pdf
```

## PDF-kontroll

PDF-filen granskades med projektets export och en separat PDF-inspektion.

Resultat:

- PDF-filen skapades utan exportfel.
- PDF-dokumentet är inte krypterat.
- Metadata innehåller titel och författare.
- Typsnitt är inbäddade.
- Stickprov av renderade sidor gjordes från början, mitten och slutet av dokumentet.

## EPUB-kontroll

EPUB-filen kontrollerades som zip-baserad EPUB.

Resultat:

- `EPUB/nav.xhtml` finns.
- `EPUB/content.opf` finns.
- Navigationsfilen är inte en vanlig linjär lässida.
- EPUB-filen skapades om efter `[PLAN4]` steg 8.

## Bedömning

`[PLAN4]` steg 9 är **godkänt**.

Projektet är redo för nästa plansteg:

> **[PLAN4] 10. Skapa ny projektversion**

Rekommenderad nästa version:

```text
arduino-i-praktiken-projekt-handbokstruktur-v3.zip
```
