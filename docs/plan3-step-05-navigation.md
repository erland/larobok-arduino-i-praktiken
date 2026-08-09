# [PLAN3] Steg 5: Inledning, kapitel 38 och uppslagsindex

Datum: 2026-07-01  
Status: Genomfört

## Syfte

Det här steget kontrollerar att bokens tre navigeringsnivåer fungerar tillsammans utan att upprepa varandra i onödan:

- `chapters/00-inledning.md`
- `chapters/referens-snabbvalsguider-38.md`
- `docs/lookup-index.md`

Målet är att inledningen ska förklara hur boken används, kapitel 38 ska vara läsarens praktiska snabbguide och `lookup-index.md` ska vara ett redaktionellt stöd för framtida uppdateringar.

## Beslut

| Del | Beslut |
|---|---|
| Inledningen | Ska förklara läslägen och visa att kapitel 38 är snabbvägen vid konkreta val. Den ska inte duplicera hela snabbindexet. |
| Kapitel 38 | Ska bära den detaljerade läsarnavigeringen och snabbvalstabellerna. |
| `docs/lookup-index.md` | Ska vara ett tematiskt arbetsindex för redaktör och framtida versioner, inte en ersättning för kapitel 38. |

## Genomförda ändringar

- Inledningens uppslagsverkssektion kortades och gjordes mer principiell.
- Inledningen pekar nu tydligare på kapitel 38 som praktisk snabbguide.
- Inledningen nämner `docs/lookup-index.md` som projektets tematiska uppslagsindex och redaktörsstöd.
- Kapitel 38 uppdaterades så att det inte längre hänvisar till `Se också`.
- `docs/lookup-index.md` fick en tydligare ansvarsfördelning mellan inledning, kapitel 38 och uppslagsindex.
- `docs/lookup-index.md` förtydligades som redaktionellt arbetsstöd, medan kapitel 38 är läsarens primära snabbguide i boken.

## Resultat

Navigeringen är nu tydligare uppdelad:

| Navigeringsnivå | Roll |
|---|---|
| Inledningen | Förklarar hur boken kan läsas och när läsaren bör börja i kapitel 38. |
| Kapitel 38 | Ger praktiska snabbval, jämförelsetabeller och beslutsguider. |
| Uppslagsindexet | Ger ett tematiskt register för redaktionell kontroll och framtida uppdateringar. |

## Bedömning

Steget är godkänt. Boken har nu en renare navigeringsmodell: inledningen förklarar, kapitel 38 guidar läsaren och `lookup-index.md` stödjer projektets fortsatta underhåll.
