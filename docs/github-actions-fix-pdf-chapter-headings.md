# GitHub Actions exportfix: PDF-kapitelrubriker och sidbrytning

Den här justeringen uppdaterar exportpipelinen efter granskning av preview-filerna.

## Ändringar

- PDF-kapitelrubriker renderas typografiskt på två rader:
  - kapitelnummer
  - kapitelnamn
- Avståndet mellan kapitelnummer och kapitelnamn är minskat.
- Varje H1/kapitel börjar på ny sida i PDF.
- PDF-TOC behåller kompakt kapitelrubrik på en rad och `toc_depth: 1`.
- EPUB-kapitelrubriker behåller två rader, men med tätare avstånd mellan raderna.
- Genererade EPUB/PDF-filer hålls utanför projekt-zippen och skapas av GitHub Actions.

## Tekniskt

PDF-formatet styrs via `build/pdf-header.tex`, som skapas av `scripts/export-book.py` vid export. Markdownmanuset ändras inte.
