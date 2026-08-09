# PLAN-E steg 03 – Kapitel 17–26

**Datum:** 2026-07-02  
**Utgångspunkt:** `arduino-i-praktiken-projekt-plan-e-steg-02-kapitel-09-16.zip`  
**Leverans:** `arduino-i-praktiken-projekt-plan-e-steg-03-kapitel-17-26.zip`

## Syfte

Steg E3 förstärker det redan starka komponentblocket med små praktiska exempelrutor och tydligare typiska användningsmönster. Målet är att öka handboksnyttan utan att lägga till stora nya experiment eller göra kapitlen längre än nödvändigt.

## Genomförda ändringar

### Kapitel 18 – Adresserbara LED

Lade till:

`Praktisk tumregel: räkna ström innan du ökar antalet pixlar`

Avsnittet förtydligar kopplingen mellan pixelantal, global ljusstyrka, separat matning, gemensam jord och nivåanpassning för 3,3 V-kort.

### Kapitel 19 – Buzzers och ljudsignaler

Omformade avsnittet om ljud som systemstatus till:

`Typiska ljudkoder i ett projekt`

Tabellen visar vanliga ljudkoder för start, knappbekräftelse, fel, larm, låg batterinivå och tyst läge. Referensmönstret har samtidigt fått mer konsekvent handbokston.

### Kapitel 23 – Miljösensorer

Lade till:

`Placering är en del av mätningen`

Avsnittet betonar att sensorplacering, luftflöde, värmekällor, kapsling och stabiliseringstid påverkar mätresultatet lika mycket som kod och bibliotek.

### Kapitel 24 – Ljus, färg, UV och optiska sensorer

Lade till:

`Typiskt mönster: ljuströskel med hysteresis`

Avsnittet visar hur optiska sensorer ofta används som praktiskt beslutsstöd för nattläge, dimning, status eller optisk detektering.

### Kapitel 26 – Rörelse, orientering och vibration

Lade till:

`Vanliga användningar av samma rörelsemönster`

Avsnittet visar hur samma basmönster kan användas för vält låda, dörr/lock, skakning, ovanlig vibration och rörelseaktiverad funktion.

### Konsekvensputs i kapitel 17–26

I berörda kapitel byttes kvarvarande `### Material` till `### Det här används i exemplet` där rubriken fanns kvar. Några återstående formuleringar kring experiment/test i samma block gjordes mer handboksnära utan att ändra tekniskt innehåll.

## Uppdaterade filer

- `chapters/led-rgb-ljuseffekter-17.md`
- `chapters/adresserbara-led-18.md`
- `chapters/buzzers-ljudsignaler-19.md`
- `chapters/relaer-mosfetar-laster-21.md`
- `chapters/displayer-anvandargranssnitt-22.md`
- `chapters/miljosensorer-23.md`
- `chapters/ljus-farg-optiska-sensorer-24.md`
- `chapters/avstand-narvaro-25.md`
- `chapters/rorelse-orientering-26.md`
- `build/book.md`
- `docs/PLAN-E-implementation-log.md`
- `docs/plan-e-step-03-chapters-17-26.md`
- `docs/project-status.md`

## Kontroll

- Inga H4-rubriker finns i ändrade kapitel.
- Kodblocken i ändrade kapitel är balanserade.
- Kapitel 17–26 har inte kvar `### Material`.
- Nya avsnitt är korta referensrutor eller användningsmönster, inte övningar.
