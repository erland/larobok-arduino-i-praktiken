# PLAN-H steg 08 – Slutblocket som verktygsdel

Datum: 2026-07-01  
Bas: `arduino-i-praktiken-projekt-PLAN-H-steg-07.zip`  
Status: Genomfört

## Syfte

Steg H8 gör bokens avslutande block mer verktygsorienterat. Fokus ligger på kapitel 36–38:

- kapitel 36 som modul- och arbetschecklista,
- kapitel 37 som integrationsordning och projektmall,
- kapitel 38 som renare referensdel och mallbibliotek.

Inga nya komponenter har lagts till och inga tekniska huvudspår har ändrats.

## Ändrade kapitel

- `chapters/breadboard-till-modul-36.md`
- `chapters/modular-sensor-styrstation-37.md`
- `chapters/referens-snabbvalsguider-38.md`

## Genomförda ändringar

### Kapitel 36

- Lade till `Modulchecklista före nästa steg` som konkret arbetsverktyg för övergången från breadboard till modul.
- Gjorde slutdelen mer mallorienterad:
  - `Arbetsmönster` blev `Modulmall i praktiken`.
  - `Kontroll 1–4` blev `Steg 1–4`.
  - `Fördjupning` blev `Nästa nivå`.
- Ersatte avslutande frågelista med en handlingsinriktad `Modulchecklista`.
- Bytte sammanfattningsrubriken `Checklista` till `Snabbreferens`.

### Kapitel 37

- Lade till `Projektmall före integration` som stöd för kort, sensor, presentation, status, styrutgång och felsökning.
- Justerade beskrivningen från övningsprojekt till referensprojekt.
- Gjorde slutdelen mer integrationsorienterad:
  - `Arbetsmönster` blev `Integrationsordning i praktiken`.
  - `Kontroll 1–5` blev `Steg 1–5`.
  - `Fördjupning` blev `Nästa nivå`.
- Ersatte avslutande frågelista med `Projektkontroll före nästa version`.
- Bytte sammanfattningsrubriken `Checklista` till `Snabbreferens`.

### Kapitel 38

- Rensade en kvarvarande hänvisning till gammal rubrikfamilj genom att ersätta `Snabb orientering` med mer neutral referenstext.
- Förtydligade att `Arbetsmall: gör en egen valguide` är ett beslutsverktyg.
- Omvandlade `Bygg din egen snabbguide` till `Egen referensmall`.
- Ersatte `Kontroll 1–4` med `Mall 1–4`.
- Ersatte avslutande frågelista med en handlingsinriktad `Användningschecklista`.

## Kontroller

- `build/book.md` har byggts om.
- Inga H4-rubriker (`####`) har införts.
- Inga interna plan- eller filreferenser har återinförts i kapiteltexterna.
- Sakmaterial, komponenturval och kapitelordning är oförändrade.

## Bedömning

Steg H8 stärker bokens avslutning. Kapitel 36 fungerar tydligare som moduliseringsverktyg, kapitel 37 som integrationsmall och kapitel 38 som referens- och mallkapitel. Slutblocket känns därmed mer som en praktisk handboksdel och mindre som ett kursavslut.
