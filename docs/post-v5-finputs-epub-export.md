# Post-v5 EPUB-export efter finputs

Datum: 2026-07-02

Utgångspunkt: `arduino-i-praktiken-projekt-v5-post-finputs-03-07-08-09-13.zip`

## Utfört

- Export körd via projektets lokala exportpipeline.
- `build/book.md` byggdes om från kapitelordningen i metadata.
- EPUB skapades i `exports/arduino-i-praktiken.epub`.
- EPUB-navigationen kontrollerades.
- `nav.xhtml` finns kvar som EPUB-navigation och ligger inte som vanlig lässida i spine.
- EPUB-exporten har kontrollerats mot kvarvarande äldre läroboksspår.

## Extra finputs före export

Vid exportkontrollen hittades några kvarvarande ordval som inte passade den nya handbokstonen. De justerades före slutlig EPUB-export:

- `experimentlogg` ersattes i kapitel 5, 6 och 23 med projektanteckningar eller projektinformation.
- `I experimentet` ersattes i kapitel 28 med en referensmönsterformulering.

## Kontrollresultat

Följande formuleringar förekommer inte i den exporterade EPUB-filen:

- `Praktiskt test`
- `Prova själv`
- `Prova vidare`
- `Snabb orientering`
- `Efter kapitlet ska`
- `docs/lookup-index.md`
- `I det här experimentet`
- `I experimentet`
- `experimentlogg`
- `### Mål`
- `### Syfte`
- `### Material`
- `### Reflektion`

