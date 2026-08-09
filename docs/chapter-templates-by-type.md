# Kapiteltyper och rubrikfamiljer

Detta är en intern redaktionell stilreferens för projektet efter `[PLAN-H]` steg H5. Den ska användas när nya kapitel skapas eller när befintliga kapitel redigeras, så att boken fortsätter kännas som en praktisk handbok snarare än en kursbok.

## Grundprincip

Rubriker ska hjälpa läsaren att snabbt förstå vad ett avsnitt gör:

- orienterar,
- hjälper till med val,
- visar ett referensmönster,
- verifierar en koppling,
- varnar för risk,
- ger felsökningsordning,
- eller fungerar som uppslagsreferens.

Undvik rubriker som låter som prov, kursmoment eller intern projektadministration.

## Kapiteltyper

### Inledning

Använd för `00-inledning.md`.

Passande rubriker:

- Vad boken handlar om
- Vem boken är för
- Hur boken är upplagd
- Så använder du boken som uppslagsverk
- Säkerhet och rimliga gränser

Undvik interna filreferenser och projektartefakter.

### Orienterings- och beslutskapitel

Exempel: Arduino-ekosystem, kortval, utvecklingsmiljö och elektriska grunder.

Passande rubriker:

- Snabb överblick
- Beslutsöversikt
- Arbetsmiljö i korthet
- Begrepp i praktiken
- Viktiga samband att känna igen
- Vanliga missförstånd
- Snabb sammanfattning

### Grundfunktionskapitel

Exempel: digital I/O, analog läsning, PWM, avbrott och kommunikationsbussar.

Passande rubriker:

- Grundfunktion i praktiken
- Mätfunktion i praktiken
- Tidsstyrning i praktiken
- Robust körning i praktiken
- Kommunikationsval i praktiken
- Referensmönster
- Snabb kontroll i praktiken
- Vanliga fel

### Kort- och plattformskapitel

Exempel: UNO, Nano, Mega, kloner, moderna Arduino-kort, ESP8266, ESP32, Pico och småkort.

Passande rubriker:

- Kortprofil i korthet
- Bedöm kortet med detta i åtanke
- Kortfamiljen i praktiken
- Plattformen i praktiken
- När kortet passar
- När du bör välja något annat
- Porteringstest
- Valguide

### Komponent- och sensorkapitel

Exempel: LED, buzzers, motorer, displayer, sensorer, I/O-expansion, drivkretsar och minne.

Passande rubriker:

- Komponentöversikt
- Sensoröversikt
- Modulöversikt
- Expansionsöversikt
- Drivsteg i praktiken
- Vad komponenten gör
- När den passar
- Koppling i praktiken
- Referensmönster
- Verifiera modulen
- Vanliga problem
- Valchecklista

### Robusthets- och säkerhetskapitel

Exempel: laster, strömmätning, signalanpassning, strömförsörjning och felsökning.

Passande rubriker:

- Riskbild och styrprincip
- Mät- och energibild
- Signalanpassning i praktiken
- Matningsöversikt och riskbild
- Felsökningsöversikt
- Riskkontroll
- Säker koppling
- Felsökningsordning
- Vanliga misstag

### Metod- och projektkapitel

Exempel: från breadboard till modul och modulär sensor-/styrstation.

Passande rubriker:

- Arbetsmönster i korthet
- Projektöversikt
- Arbetsmönster
- Stegvis integration
- Modulchecklista
- Testordning
- Felsökningsstrategi
- Arbetschecklista

### Referenskapitel

Exempel: snabbvalsguider och jämförelsetabeller.

Passande rubriker:

- Så använder du referensen
- Snabbindex
- Snabbval
- Välj efter behov
- Jämförelsetabell
- Checklista
- Felsökningshjälp
- Mall

Referenskapitel ska inte ha quiz-, övnings- eller kursstruktur.

## Formuleringar att undvika

- Efter kapitlet ska du kunna
- Kontrollera att du hänger med
- Testa dina kunskaper
- Praktiskt test
- Prova själv
- Prova vidare
- Praktiskt arbetspass
- Interna plan- eller filnamn i läsartext, till exempel `PLAN5`, `docs/`, `build/`, `canon` eller `project-status`

## Underhållsregel

När nya kapitel läggs till ska kapiteltypen anges i projektets redaktionella dokumentation. Rubrikval ska följa kapiteltypen, inte en mekanisk standardmall.

## Användning tillsammans med stilguiden

Denna fil beskriver främst rubrikfamiljer per kapiteltyp. För ton, formuleringar, ersättningsmönster, praktiska moment, riskkontroller och korsreferenser används även:

- `docs/handbook-editorial-style-guide.md`

När framtida kapitel läggs till eller ändras ska redaktören först välja kapiteltyp och därefter använda rubriker och formuleringar som stödjer kapitlets funktion som handbok.
