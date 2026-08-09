# [PLAN-H] steg H12 – Exportkontroll och ny projektversion

Datum: 2026-07-01  
Bas: `arduino-i-praktiken-projekt-PLAN-H-steg-11.zip`  
Resultat: `handbokstruktur-v5`

## Syfte

Avsluta `[PLAN-H]` som ny stabil projektversion efter den redaktionella handbokskonsolideringen.

## Genomfört

- Version uppdaterad från `handbokstruktur-v4` till `handbokstruktur-v5`.
- `book.yaml` och `docs/export-metadata.yaml` har uppdaterats.
- `README.md` och `docs/book-specification.md` har uppdaterats med `[PLAN-H]` som genomförd redaktionell runda.
- Ny versionsfil har skapats: `docs/project-version-handbokstruktur-v5.md`.
- `build/book.md` har byggts om via lokal exportpipeline.
- EPUB och PDF har skapats i `exports/`.
- Markdownvalidering har körts utan projektvarningar före export.

## Exportkontroll

Kontrollerat:

- metadata finns för titel, undertitel, författare, språk, version, datum och identifierare,
- kapitelordningen följer metadata,
- `chapters/00-inledning.md` ligger först,
- inga H4-rubriker har införts,
- inga obalanserade kodblock rapporterades,
- inga gamla kursrubriker från PLAN-H-rensningen rapporterades i kapiteltexterna,
- EPUB/PDF skapades från `build/book.md`.


## Utförd teknisk kontroll

- `scripts/export-book.py validate` returnerade: `Validering klar utan varningar.`
- `scripts/export-book.py all` skapade:
  - `exports/arduino-i-praktiken.epub`
  - `exports/arduino-i-praktiken.pdf`
- PDF-inspektion:
  - antal sidor: 765
  - kryptering: nej
  - dokumenttitel: Arduino i praktiken
  - författare: Erland Lindmark
- EPUB-inspektion:
  - `EPUB/nav.xhtml` finns
  - `content.opf` innehåller `linear="no"` för nav-posten
  - navigerbar TOC finns
- Renderingsprov av PDF har gjorts på sidorna 1–3, 10, 50 och 100.
- Kontrollsökning i `chapters/` visar inga kvarvarande förekomster av de gamla rubrikerna:
  - `Praktiskt test`
  - `Prova själv`
  - `Prova vidare`
  - `Snabb orientering`
  - `Kontrollera att du hänger med`


## Resultat

Projektet är redo att användas som ny stabil basversion:

```text
arduino-i-praktiken-projekt-handbokstruktur-v5.zip
```

## Kommentar

`[PLAN-H]` har varit en redaktionell konsolidering, inte en ny innehållsutbyggnad. Den tekniska bredden från `handbokstruktur-v4` är bevarad, medan språk, rubriker, checklistor, riskkontroller, beslutsstöd och referensstruktur har gjorts mer handboksnära.
