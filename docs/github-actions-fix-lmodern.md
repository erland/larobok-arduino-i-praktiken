# GitHub Actions fix: lmodern i PDF-export

## Problem

Preview-workflow föll i PDF-steget med:

```text
LaTeX Error: File `lmodern.sty' not found.
```

EPUB hann skapas, men PDF-exporten stoppade `scripts/export-book.py all` och därmed även `scripts/build_book.py`.

## Orsak

Pandocs PDF-export via XeLaTeX använder LaTeX-mallen som kan kräva paketet `lmodern`. Ubuntu-runnern hade XeLaTeX installerat, men inte paketet som innehåller `lmodern.sty`.

## Åtgärd

Både Preview- och Release-workflow installerar nu:

```bash
texlive-xetex
texlive-latex-extra
texlive-fonts-recommended
texlive-lang-european
lmodern
fonts-texgyre
```

`lmodern` åtgärdar det rapporterade felet. `texlive-lang-european` ger extra marginal för svensk språk- och avstavningshantering i PDF-exporten.

## Berörda workflows

- `.github/workflows/02-build-preview.yml`
- `.github/workflows/03-release.yml`
