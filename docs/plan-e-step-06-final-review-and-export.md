# PLAN-E steg E6 – Slutkontroll och export

**Datum:** 2026-07-02  
**Utgångspunkt:** Projektversion efter PLAN-E steg E5.  
**Status:** Genomförd.

## Genomfört

- Skapade `docs/example-coverage-review.md`.
- Granskade kvarvarande läroboksmarkörer i kapitelmanus.
- Justerade två kvarvarande formuleringar med `övning` där de gav fel ton.
- Byggde om `build/book.md`.
- Kör EPUB-export enligt projektstandard.
- Kontrollerade EPUB-navigation och att ingen synlig text-innehållsförteckning ligger som vanlig lässida.

## Mindre språkjusteringar i E6

- `chapters/esp8266-nodemcu-13.md`: bytte en formulering om webbsida från övningsspråk till praktiskt testspråk.
- `chapters/modular-sensor-styrstation-37.md`: bytte `övningsprojekt` till `sammanhållet referensprojekt`.

## Slutlig bedömning

PLAN-E har förbättrat bokens exempeltäckning utan att återinföra labb-/lärobokston. Nya tillägg är korta, praktiska och återanvändbara: mönster, tabeller, tumregler och referensrutor snarare än stora nya experiment.

## Exportkontroll

- Markdownvalidering: utan varningar.
- EPUB skapad: `exports/arduino-i-praktiken-plan-e-final.epub`.
- EPUB använder navigerbar EPUB-TOC på H1-nivå.
- `nav.xhtml` finns kvar och är markerad som `linear="no"` i spine.
- Ingen synlig text-Innehållsförteckning hittades i EPUB-flödet.
- Kvarvarande träffar på `uppgift` är tekniska användningar av ordet, inte skoluppgifter.
