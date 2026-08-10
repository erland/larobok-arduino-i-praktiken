# GitHub Actions fix: EPUB-rubriker och PDF-standard

Datum: 2026-08-10

## Bakgrund

Preview-workflowen byggde EPUB/PDF, men två exportdetaljer behövde justeras:

- EPUB-kapitelrubriker skulle visas på två rader: kapitelnummer och kapitelnamn.
- PDF skulle ha omslagsbild och innehållsförteckning på endast första rubriknivån.
- Projekt-zippen behövde inte längre innehålla genererade EPUB/PDF-filer eftersom GitHub Actions kan skapa dem.

## Genomförda ändringar

- `scripts/export-book.py` skapar nu en EPUB-specifik `build/book-epub.md` där H1-rubriker på formen `# 12. Titel` renderas med separata span-element för nummer och titel.
- `styles/epub.css` formaterar `.chapter-number` och `.chapter-title` som två tydliga rader.
- PDF-exporten använder `exports.pdf.toc_depth` från metadata och standarden är nu `1`.
- PDF-exporten lägger in omslagsbilden från `cover_image` med en LaTeX-header före titelsida och innehållsförteckning.
- Genererade `.epub` och `.pdf`-filer har tagits bort från projekt-zippen. `exports/.gitkeep` lämnas kvar.

## Kontroll

- `scripts/export-book.py validate` ska köras utan varningar.
- Preview-workflowen ska skapa EPUB och PDF som artifact.
- EPUB ska ha navigerbar TOC med H1-nivå.
- PDF ska ha omslag och TOC med endast kapitelrubriker.
