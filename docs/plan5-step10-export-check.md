# PLAN5 steg 10: Markdown- och exportkontroll

Kontroll genomförd: 2026-07-01

## Resultat

| Kontrollpunkt | Resultat |
|---|---|
| Inga H4-rubriker i kapiteltext | Godkänd |
| Exakt en H1 per kapitel | Godkänd |
| Inga gamla kursrubriker i kapiteltext | Godkänd |
| Inga `## Se också` | Godkänd |
| Stabil grundvalidering av listor och tabeller | Godkänd |
| Stängda kodblock | Godkänd |
| `build/book.md` uppdaterad | Godkänd |
| EPUB-export | Godkänd |
| PDF-export | Godkänd |
| Kapitel 38 och lookup-index kontrollerade mot PLAN5-tilläggen | Godkänd |

## Exportkontroll

Exportscriptet kördes med målet `all` och skapade:

- `exports/arduino-i-praktiken.epub`
- `exports/arduino-i-praktiken.pdf`

PDF-metadata kontrollerades med `pdfinfo`:

- titel: Arduino i praktiken
- författare: Erland Lindmark
- antal sidor: 754

EPUB-filen kontrollerades som zip-paket:

- `EPUB/nav.xhtml` finns
- `EPUB/content.opf` finns
- navigationsfilen ligger inte som vanlig lässida i läsflödet (`linear="no"`)
- ingen separat synlig sida med rubriken `Innehållsförteckning` hittades i EPUB-innehållet

## Slutsats

PLAN5 steg 10 är godkänt. Projektet är redo för steg 11: skapande av slutversionen `handbokstruktur-v4`.
