# [PLAN-H] Steg H7 – Förstärk riskkontroller och vanliga misstag

Datum: 2026-07-01  
Status: Genomförd  
Bas: `arduino-i-praktiken-projekt-PLAN-H-steg-06.zip`

## Syfte

Steg H7 stärker bokens praktiska trygghet utan att ändra komponenturval, kapitelordning eller tekniska huvudspår. Målet är att göra risker mer skannbara där läsaren sannolikt arbetar med ström, laster, motorer, drivkretsar, mätning, analog signalanpassning, strömförsörjning och felsökning.

## Genomförda ändringar

Följande kapitel har fått förstärkta riskkontroller eller tydligare risknära handboksstöd:

- `chapters/elektriska-grunder-04.md`
- `chapters/servon-motorer-20.md`
- `chapters/relaer-mosfetar-laster-21.md`
- `chapters/strom-spanning-energi-28.md`
- `chapters/drivkretsar-31.md`
- `chapters/analog-signalanpassning-33.md`
- `chapters/stromforsorjning-batteridrift-34.md`
- `chapters/felsokning-35.md`

`build/book.md` har byggts om efter kapiteländringarna.

## Redaktionell princip

Ändringarna följer handboksprincipen från `[PLAN-H]`:

- risk ska vara lätt att skanna,
- risk ska kopplas till praktiska beslut,
- risk ska inte formuleras som provfrågor,
- säkerhetsråd ska vara konkreta och handlingsbara,
- boken ska inte bli skrämmande eller överdrivet varningsdriven.

## Införda eller förstärkta riskavsnitt

### Kapitel 4 – Elektriska grunder

Ny sektion:

- `Riskkontroll före koppling`

Syfte: ge läsaren en enkel kontroll innan grundkopplingar provas, särskilt kring logiknivå, LED-motstånd, flytande ingångar, gemensam jord och olämpliga laster direkt på GPIO.

### Kapitel 20 – Servon, DC-motorer och stegmotorer

Ny sektion:

- `Riskkontroll före motorstart`

Syfte: fånga motorrelaterade risker innan mekanik eller högre strömmar kopplas in, till exempel separat matning, gemensam jord, resetbeteende, värme och okontrollerad start.

### Kapitel 21 – Reläer, MOSFET:ar, solenoider och andra laster

Ny sektion:

- `Riskkontroll före lasttest`

Syfte: göra lastklassning, flyback-skydd, startström, säker vilonivå och lågspänningsprov tydligare innan verklig last ansluts.

### Kapitel 28 – Ström, spänning, energi och batterimätning

Ny sektion:

- `Riskkontroll före mätning`

Syfte: tydliggöra att mätning också kan vara en riskkälla, särskilt vid ADC-ingångar, strömmätning, shuntar, isolation och okända spänningar.

### Kapitel 31 – Drivkretsar

Ny sektion:

- `Riskkontroll före val av drivkrets`

Syfte: hjälpa läsaren välja drivkrets utifrån lasttyp, startström, styrsätt, skydd, värme, logiknivå och resetbeteende snarare än bara maxström.

### Kapitel 33 – Analog signalanpassning

Ny sektion:

- `Riskkontroll före analog inkoppling`

Syfte: fånga typiska analoga risker som signalområde, bortkopplad sensor, op-förstärkarens matningsområde, utgångssving, hysteres och filter.

### Kapitel 34 – Strömförsörjning och batteridrift

Ny sektion:

- `Riskkontroll före längre drift`

Syfte: flytta fokus från “det fungerar på bordet” till robust drift, temperatur, polaritet, regulatorval, batterityp, kablar och kapsling.

### Kapitel 35 – Felsökning

Ny sektion:

- `Riskkontroll när något beter sig fel`

Syfte: ge en tydlig felsökningsregel: bryt matningen, koppla bort större laster och gå tillbaka till säkrare testläge när fel kan skada komponenter.

## Avgränsning

Steget har inte:

- lagt till nya komponenter,
- ändrat kodexempel i sak,
- ändrat kapitelordning,
- skapat nya kapitel,
- gjort säkerhetstexten mer dramatisk än nödvändigt.

## Kontroll

Kontroller genomförda efter ändring:

- `build/book.md` är ombyggd från aktuell kapitelordning.
- Inga H4-rubriker (`####`) har införts.
- Inga interna projektspår som `PLAN5`, `docs/lookup-index.md` eller `build/book.md` har införts i kapiteltexter.
- Ändringarna är begränsade till riskkontroller, vanliga misstag och handboksnära stöd.
