# PLAN-E steg E4 – kapitel 27–34

Datum: 2026-07-02  
Utgångspunkt: `arduino-i-praktiken-projekt-plan-e-steg-03-kapitel-17-26.zip`

## Syfte

Steg E4 förstärker exempel- och referensmönster i kapitel 27–34 utan att göra blocket till en övningsdel. Målet är att göra typisk användning tydligare: ljudtrigger, mätlogg, händelserad, I/O-expansion, drivsteg, dataloggning, analog signalanpassning och robust matning.

## Ändrade kapitel

- `chapters/ljud-mikrofoner-27.md`
- `chapters/strom-spanning-energi-28.md`
- `chapters/position-tid-identitet-29.md`
- `chapters/io-expansion-30.md`
- `chapters/drivkretsar-31.md`
- `chapters/displaykretsar-minne-32.md`
- `chapters/analog-signalanpassning-33.md`
- `chapters/stromforsorjning-batteridrift-34.md`

## Genomförda ändringar

### Kapitel 27

Lade till `Typiska ljudmönster`, en kort tabell som kopplar ljudmoduler till praktiska användningsfall:

- klapp/knackning,
- grov bullernivå,
- enkel digital ljudtrigger,
- statusindikator,
- mer avancerad ljudanalys med I2S eller specialiserad signalbehandling.

### Kapitel 28

Gjorde mindre konsekvensputs i referensmönstret för batteri- och lastmonitor:

- `### Material` ersattes med `### Det här används i exemplet`,
- kvarvarande formulering om nätspänning i experiment ersattes med mönsterformulering.

### Kapitel 29

Förstärkte händelsemönstret:

- ersatte kvarvarande `Det här experimentet` med referensmönsterspråk,
- rättade verbformen i listan över vad systemet kan göra,
- lade till `Typisk händelserad` med exempelrad och fältförklaring.

### Kapitel 30

Förtydligade 74HC595-valet:

- 74HC595 ger fler logiska utgångar, inte mer lastström,
- större laster ska styras via separat drivsteg,
- `### Material` ersattes med `### Det här används i exemplet`.

### Kapitel 31

Gjorde jämförelsemönstret mer konsekvent:

- `### Material` ersattes med `### Det här används i exemplet`,
- dokumentationsformulering ändrades till mer praktiskt sparspråk.

### Kapitel 32

Förstärkte dataloggerexemplet:

- lade till `Typisk loggrad med statusfält`,
- visade CSV-rader med `status` och `error`,
- justerade kodens header och loggrad så loggformatet speglar status/fel,
- ersatte `Experimentet tränar` med referensmönsterspråk.

### Kapitel 33

Gjorde de två verifieringsavsnitten mer återanvändbara:

- `Verifiera tröskelkretsen: analog mätning och digital utgång` blev `Referensmönster: analog tröskel med hysteres`,
- `Verifiera signalvägen: enkel analog lågpassfiltrering` blev `Referensmönster: enkel analog lågpassfiltrering`.

### Kapitel 34

Tonade ned kvarvarande experimentformuleringar i matnings- och snabbvalstext.

## Kontroll

- Inga H4-rubriker finns i ändrade kapitel.
- Kodblock är balanserade.
- Kapitel 27–34 innehåller inte längre `### Material`, `### Syfte`, `### Mål`, `Det här experimentet`, `I det här experimentet`, `experimentlogg`, `## Verifiera` eller `Experimentet tränar`.
- `build/book.md` har byggts om.
