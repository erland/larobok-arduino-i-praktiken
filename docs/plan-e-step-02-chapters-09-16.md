# PLAN-E steg E2 – kapitel 9–16

**Datum:** 2026-07-02  
**Utgångspunkt:** `arduino-i-praktiken-projekt-plan-e-steg-01-kapitel-01-08.zip`  
**Omfattning:** kapitel 9–16

## Syfte

Steg E2 stärker kort- och plattformskapitlen så att de tydligare visar respektive tekniks praktiska särart. Fokus ligger på återanvändbara referensmönster och korta förstärkningar, inte på stora nya övningar.

## Genomförda ändringar

### Kapitel 9 – Kommunikation

- Lade till `Praktiskt SPI-mönster: en buss, flera chip select`.
- Förtydligade att SPI-enheter delar buss men behöver varsin CS.
- Lade till praktiska felkällor: CS-viloläge, logiknivå, bibliotekspinnar och kopplingslängd.

### Kapitel 10 – Klassiska Arduino-kort

- Omformade `Porteringstest: samma sensorprojekt mellan UNO, Nano och Mega` till `Referensmönster: samma lilla projekt på UNO, Nano och Mega`.
- Bytte labbliknande rubriker till handboksrubriker.
- Förtydligade skillnader mellan UNO, Nano och Mega: formfaktor, seriella portar, pinout, `LED_BUILTIN` och konfigurationsblock.
- Justerade kod och utskrifter till portabilitetsmönster i stället för test/experiment.

### Kapitel 11 – Kloner och lågkostnadskort

- Lade till `Praktisk kontroll: identifiera kortet innan du felsöker koden`.
- Förtydligade att kortidentitet, USB-seriechip, board-val, pinout och logiknivå bör kontrolleras innan applikationskod felsöks.

### Kapitel 12 – Moderna Arduino-kort

- Lade till `Vad moderna kort ofta ger dig utöver klassiska kort`.
- Omformade porteringskontrollen till `Referensmönster: portering från klassiskt till modernt Arduino-kort`.
- Gjorde mönstret mer handboksnära och förtydligade skillnader i ADC-skala, PWM, I2C-pinnar, USB-start, logiknivå och bibliotekskompatibilitet.

### Kapitel 13 – ESP8266

- Bytte kvarvarande `Variationer` i referensmönstret till `Anpassningar`.
- Justerade formulering så vidarebyggnad beskrivs som anpassningar, inte variationer/övningsspår.

### Kapitel 14 – ESP32

- Justerade referensmönstret för Wi-Fi-baserad sensorindikator med konsekvent handbokston.
- Lade till `ESP32-specifik variant: deep sleep för batterinod`.
- Mönstret visar hur ESP32 kan vakna, läsa ett värde, indikera kort och gå till deep sleep.
- Förtydligade att exakt väckningspinne, strömförbrukning och deep-sleep-beteende beror på utvecklingskort och anslutna moduler.

### Kapitel 15 – Raspberry Pi Pico, RP2040 och RP2350

- Lade till `Picos unika styrka: stabil timing och PIO`.
- Förtydligade när Pico är starkt: lokal styrning, många GPIO, stabil timing, specialprotokoll och PIO-användning via bibliotek.
- Justerade referensmönstrets rubriker till mer konsekvent handbokston.

### Kapitel 16 – Småkort och specialkort

- Omformade `Minsta kontroll innan du använder ett specialkort` till `Referensmönster: kortprofil innan specialkortet byggs in`.
- Bytte sex kontrolluppgifter till praktiska delrubriker: identifiera kortet, kontrollera USB/seriell monitor, välj säkra testpinnar, kontrollera buss och fatta beslut före integration.
- Ersatte frågetabell med beslutstabell som förklarar praktisk betydelse.

## Kontroll

- `build/book.md` är ombyggd.
- Inga H4-rubriker finns i ändrade kapitel.
- Kodblocken i ändrade kapitel är balanserade.
- Följande äldre läroboksspår finns inte kvar i kapitel 9–16: `I det här experimentet`, `I experimentet`, `experimentlogg`, `### Syfte`, `### Mål`, `### Material`, `Kontroll 1`.
