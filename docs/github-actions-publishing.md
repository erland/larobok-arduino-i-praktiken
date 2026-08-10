# GitHub Actions-publicering

Detta dokument beskriver GitHub Actions-stödet som infördes i version `plan-e-final-rubrikputs-github-actions`.

## Placering

`.github/` ligger i projektroten, på samma nivå som `README.md`.

```text
README.md
.github/
  workflows/
    01-validate.yml
    02-build-preview.yml
    03-release.yml
scripts/
  validate_project.py
  build_book.py
  export-book.py
styles/
  epub.css
  pdf.css
exports/
```

## Workflow: Validate

`01-validate.yml` körs på pull request och push till `main` när relevanta filer ändras.

Den kör:

```bash
python3 scripts/validate_project.py .
python3 scripts/export-book.py validate
```

Syftet är snabb kontroll av projektstruktur, kapitelordning, markdownregler och exportmetadata.

## Workflow: Build Preview

`02-build-preview.yml` startas manuellt via `workflow_dispatch`.

Den gör följande:

1. installerar Python-beroendet `PyYAML`,
2. kör projektvalidering,
3. installerar låst Pandoc-version `3.1.11.1`,
4. installerar XeLaTeX och nödvändiga LaTeX-paket för PDF,
5. bygger EPUB och PDF via `scripts/build_book.py`,
6. publicerar ett gemensamt Actions-artifact: `arduino-i-praktiken-preview`.

Artifactet innehåller:

- `arduino-i-praktiken.epub`
- `arduino-i-praktiken.pdf`

## Workflow: Release

`03-release.yml` körs när en tagg som matchar `v*` pushas.

Den bygger EPUB och PDF och laddar upp dem som separata GitHub Release-assets.

## Anpassning från bifogat referenskit

Referenskitet var skapat för ett Romanskaparen-projekt. Det har därför anpassats till detta projekts faktiska struktur:

- `kapitel/` har ersatts av `chapters/`.
- `publishing/` har inte införts; projektets befintliga `styles/` och `scripts/export-book.py` används.
- Projektets `book.yaml` styr kapitelordning och metadata.
- Preview-artifact heter `arduino-i-praktiken-preview`.
- Release-assets heter `arduino-i-praktiken.epub` och `arduino-i-praktiken.pdf`.
- Valideringen är anpassad till Arduino-handbokens standard och kontrollerar inte romanprojektspecifika filer.

## Korrigering: LaTeX-paket i GitHub Actions

En tidig Preview-körning kunde falla på PDF-steget med felet `lmodern.sty not found`.
Workflow-stegen för Preview och Release installerar därför även:

- `lmodern`
- `texlive-lang-european`

`lmodern` behövs av Pandocs standardmall vid LaTeX/PDF-export. `texlive-lang-european` ger bättre marginal för svensk språk- och avstavningshantering.
## Exportformat efter fix 3

- EPUB och PDF byggs av GitHub Actions, inte genom att färdiga exportfiler lagras i projekt-zippen.
- EPUB visar kapitelnummer och kapitelnamn på två rader i kapiteltexten, men TOC-posten är kompakt.
- PDF visar också kapitelnummer och kapitelnamn på två rader i kapiteltexten.
- PDF startar varje nytt kapitel på ny sida.
- PDF-innehållsförteckningen använder endast första rubriknivån.
