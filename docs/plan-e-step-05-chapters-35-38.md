# PLAN-E steg E5 – Kapitel 35–38

**Datum:** 2026-07-02  
**Utgångspunkt:** `arduino-i-praktiken-projekt-plan-e-steg-04-kapitel-27-34.zip`

## Syfte

Förstärka de avslutande metod- och referenskapitlen med korta, praktiska metodmönster utan att lägga till nya komponentexperiment eller arbetsboksuppgifter.

## Genomförda ändringar

### Kapitel 35 – Felsökning med metod

- Lade till `Typiska minimisketcher för felsökning`.
- Tabellen kopplar vanliga problem till rätt minimisketch, till exempel diagnostisk startsketch, I2C-scanner, råvärdesläsare, ingångstest, PWM-test och spänningslogg.
- Justerade formuleringen kring pinout så den låter mer som praktiskt sparande än dokumentationsuppgift.

### Kapitel 36 – Från breadboard till återanvändbar modul

- Lade till `Före och efter: från lös sketch till modul`.
- Visar skillnaden mellan direkt pinlogik i huvudloopen och ett enklare modulgränssnitt som `fan.update(temperature)`.
- Förklarar varför modulering gör pinout, aktiv nivå, säker standardstatus och diagnostik lättare att hålla ihop.
- I modul-README-exemplet ändrades `Syfte` till `Vad modulen gör`.

### Kapitel 37 – Sammanhängande projekt

- Lade till `Så hänger projektet ihop med tidigare mönster`.
- Tabellen visar hur slutprojektets delar bygger på tidigare mönster: I2C-sensor, OLED-display, status-LED, buzzer, styrutgång, seriell diagnostik och strömförsörjning.
- Förstärkte principen att en krånglande del bör felsökas som eget mönster innan den integreras igen.

### Kapitel 38 – Referens och snabbval

- Justerade snabbguidens sista steg från dokumentationsspråk till praktiskt sparspråk:
  `Spara pin mapping, adresser och matning när första testet fungerar`.
- Ingen ny exempelbyggnad har lagts till i referenskapitlet.

## Kontroll

- Inga nya komponentexperiment har lagts till.
- De nya tilläggen är korta handboksrutor, tabeller eller metodmönster.
- Inga H4-rubriker har införts.
- Kodblocken i ändrade kapitel är balanserade.
- `build/book.md` har byggts om efter ändringarna.
