# Post-v5-justering: kapitel 10–16

Status: Genomfört 2026-07-02.

## Syfte

Rensa bort återstående kurs- och lärobokskänsla i kortkapitlen 10–16 utan att ta bort praktiskt användbara tester som faktiskt verifierar koppling, pinout, uppladdning, kommunikation eller kortbeteende.

Principen för detta steg var:

- behåll praktiska kontroller som mäter, verifierar eller felsöker något konkret,
- ta bort avslutande checklistor och övningsliknande dokumentationsuppgifter,
- tona ned ord som `experimentlogg`, `övning` och tomma arbetsblad,
- behåll sakmaterial, kod och rekommendationer där de fungerar som handboksstöd.

## Ändrade kapitel

### Kapitel 10

Fil: `chapters/klassiska-arduino-kort-10.md`

- Tog bort sektionen `Valchecklista`.

Motiv: kapitlet innehåller redan val- och jämförelsestöd i huvudtext, snabbreferens, sammanfattande valbild och snabbval.

### Kapitel 11

Fil: `chapters/kloner-lagkostnadskort-11.md`

- Tog bort `Kortprofil: identifiera ett okänt kompatibelt kort`.
- Tog bort `Nästa praktiska kontroll`.
- Tog bort `Valchecklista`.

Motiv: de borttagna avsnitten fungerade mer som dokumentationsövningar än som direkt handboksstöd. Huvudtext, valguide, exempel, vanliga misstag och snabbreferens behåller den praktiska nyttan.

### Kapitel 12

Fil: `chapters/moderna-arduino-kort-12.md`

- Bytte `Porteringstest: jämför samma sketch på klassiskt och modernt kort` till `Porteringskontroll mellan klassiskt och modernt kort`.
- Tonade ned experimentformuleringar till kontrollformuleringar.
- Tog bort `Resultattabell för experimentet`.
- Tog bort `Nästa praktiska kontroll`.
- Tog bort `Valchecklista`.

Motiv: portering mellan klassiska och moderna kort är en praktisk risk som bör finnas kvar, men tomma resultatmallar och kursövningar gör kapitlet mer lärobokslikt.

### Kapitel 13

Fil: `chapters/esp8266-nodemcu-13.md`

- Behöll `Referensmönster: Wi-Fi-baserad sensorindikator`, men gjorde inledningen mer handboksnära.
- Ersatte experimentlogg- och dokumentationsspråk med praktisk kontroll.
- Kortade `Vanliga varianter` till praktiska varianter:
  - I2C-scanner,
  - webbsida med sensorvärde,
  - reservläge utan Wi-Fi.
- Tog bort dokumentations- och jämförelseuppgifter.
- Tog bort `Valchecklista`.

Motiv: Wi-Fi, I2C och lokal fallback är praktiska verifieringar. Dokumentera-kortet- och jämför-kort-uppgifter är däremot mer lärobokslika.

### Kapitel 14

Fil: `chapters/esp32-familjen-14.md`

- Behöll referensmönstret, men gjorde det mindre kurslikt.
- Bytte `Mål` till `Vad mönstret verifierar`.
- Ersatte tom kortprofilstabell med kortare `Kortkontroll före koppling`.
- Tog bort `Valchecklista`.

Motiv: ESP32-referensmönstret är praktiskt värdefullt, men tomma arbetsblad och målformuleringar passar sämre i en handbok.

### Kapitel 15

Fil: `chapters/raspberry-pi-pico-15.md`

- Behöll referensmönstret eftersom det verifierar analog signal, digital ingång, LED-styrning, 3,3 V-logik och seriell monitor.
- Tonade ned experimentloggsspråk till praktisk pinoutkontroll.
- Tog bort `Valchecklista`.

Motiv: praktiken mäter och verifierar konkret funktion, men avslutande frågor och experimentloggsformuleringar var onödigt kurslika.

### Kapitel 16

Fil: `chapters/smakort-specialkort-16.md`

- Bytte `Kortprofil: utvärdera ett specialkort` till `Minsta kontroll innan du använder ett specialkort`.
- Gjorde avsnittet till praktisk verifiering i stället för dokumentationsövning.
- Bytte steg-rubriker till kontroll-rubriker.
- Tog bort `Nästa praktiska kontroll`.
- Tog bort `Valchecklista`.

Motiv: specialkort behöver praktisk verifiering innan användning, men inte övningspaket med flera dokumentationsuppgifter.

## Uppdaterade projektfiler

- `build/book.md` har byggts om.
- `docs/plan-h-implementation-log.md` har uppdaterats.
- `docs/project-status.md` har uppdaterats.

## Kontroll

Kontrollerat för kapitel 10–16:

- inga `## Valchecklista` finns kvar,
- inga `## Nästa praktiska kontroll` finns kvar,
- inga `### Övning` finns kvar,
- ingen `Resultattabell` finns kvar,
- inga `experimentlogg`-formuleringar finns kvar,
- inga H4-rubriker har införts.
