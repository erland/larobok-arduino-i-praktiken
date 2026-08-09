# [PLAN] Steg 10: Progressionskontroll

Datum: 2026-06-30  
Bok: *Arduino i praktiken*  
Syfte: Kontrollera att boken fortfarande fungerar från början till slut efter strukturjusteringarna, samtidigt som den kan användas som uppslagsverk.

## Sammanfattande bedömning

Progressionen är **godkänd**.

Min bedömning är att kapitelordningen bör behållas. Boken börjar med orientering, kortval, utvecklingsmiljö och elektriska grunder innan den går vidare till I/O, analog läsning, timing, kommunikation, kortfamiljer, komponenter, sensorer, robust kretsbyggande, felsökning, modularisering och snabbvalsguider.

Efter batchjusteringarna har boken fått en bättre balans mellan två läslägen:

- **Läsning från början till slut:** grundbegrepp och praktiskt arbetssätt byggs upp stegvis.
- **Uppslagsläsning:** läsaren kan hoppa till ett kort, en komponent, sensor, krets eller felsökningssituation och ändå få praktisk orientering.

Det finns inga skäl att flytta kapitel i detta steg.

## Kontrollpunkter

| Kontrollpunkt | Bedömning | Kommentar |
|---|---|---|
| Kapitelordningen bygger upp rätt grund | Godkänd | Kapitel 1–4 ger ekosystem, kortval, utvecklingsmiljö och elektronikgrund innan de tekniska blocken börjar. |
| Grundfunktioner kommer före komponent- och sensorkatalog | Godkänd | Kapitel 5–9 behandlar digital I/O, ADC, PWM, avbrott och kommunikationsbussar innan komponenter och sensorer. |
| Kortfamiljerna ligger på rätt plats | Godkänd | Kapitel 10–16 fungerar bra före praktiska komponent- och sensorkapitel, eftersom kortval påverkar pinnar, spänning, bibliotek och kommunikation. |
| Komponenter och aktuatorer kommer före sensorer | Godkänd | Det ger läsaren praktisk kontroll över utsignaler, motorer, displayer och laster innan mätkapitlen breddas. |
| Sensor- och mätkapitlen är tematiskt samlade | Godkänd | Kapitel 23–29 fungerar väl som uppslagsblock. |
| Robusthets- och kretskapitlen kommer efter praktiska behov | Godkänd | Kapitel 30–34 blir mer meningsfulla när läsaren redan sett behov av fler pinnar, drivning, minne, signalanpassning och strömförsörjning. |
| Felsökning och modularisering kommer i slutet | Godkänd | Kapitel 35–37 fungerar som övergång från experiment till återanvändbara projekt. |
| Kapitel 38 fungerar som snabbguide | Godkänd | Referenskapitlet fungerar nu tydligare som ingång för uppslagsläsning. |

## Begreppsordning

Boken använder vissa begrepp tidigt innan de får ett helt eget kapitel. Det är acceptabelt för målgruppen, eftersom läsaren är en erfaren programmerare med viss Arduino-vana. De tidiga omnämnandena bör däremot vara korta och praktiskt förklarade när de kan påverka förståelsen.

| Begrepp | Tidig användning | Huvudförklaring | Bedömning |
|---|---|---|---|
| ADC | Förekommer i ekosystem/kortval | Kapitel 6 | Acceptabelt, eftersom analog läsning snart förklaras. |
| PWM | Förekommer i inledning/kortval | Kapitel 7 | Acceptabelt, men bör inte användas som självklart för nybörjare. |
| UART, I2C, SPI och 1-Wire | Förekommer i kort- och miljöresonemang | Kapitel 9 | Godkänd ordning. Kommunikationskapitlet ligger före sensor- och modulblocken. |
| Pull-up/pull-down | Förekommer tidigt | Kapitel 4–5 | Godkänd ordning. Begreppet ligger nära elektriska grunder och digital I/O. |
| 5 V och 3,3 V | Förekommer från början | Kapitel 4 och plattformskapitlen | Godkänd ordning. Detta är ett säkerhets- och kompatibilitetsbegrepp som behöver komma tidigt. |
| MOSFET och induktiv last | Förekommer i säkerhetssammanhang | Kapitel 21 och 31 | Acceptabelt, eftersom tidig säkerhetsvarning är viktigare än strikt begreppsordning. |
| Watchdog | Förekommer i timing/robusthet | Kapitel 8 | Godkänd ordning. |
| Deep sleep, Wi-Fi och BLE | Förekommer i kortfamiljskapitlen | Kapitel 13–16 och senare systemresonemang | Godkänd ordning för plattformsval. |

## Fristående läsbarhet

Boken fungerar nu bättre som uppslagsverk än före justeringarna. De flesta kapitel har en tydligare öppning med `Snabb orientering`, följt av praktisk användning, valhjälp, misstag, felsökning, test eller snabbreferens.

Bedömning:

- Kapitel 10–16 kan läsas fristående som kort- och plattformsval.
- Kapitel 17–34 kan läsas fristående när läsaren vill använda en viss komponent, sensor eller krets.
- Kapitel 35–37 bör helst läsas efter praktiska erfarenheter, men fungerar även som metodstöd.
- Kapitel 38 fungerar som snabb ingång till resten av boken.

## Nivåkontroll

Målgruppen är erfarna programmerare med viss Arduino-vana. Nivån är konsekvent med detta.

Styrkor:

- Boken förklarar elektronik praktiskt utan att bli en ren nybörjarkurs.
- Kod- och systemresonemang kan hålla högre tempo än i en absolut nybörjarbok.
- De nya rubrikerna gör att läsaren snabbare hittar val, risker, felsökning och praktiskt test.

Risker att bevaka vid senare finputsning:

- Vissa kapitel kan fortfarande vara informationsrika och bör inte byggas ut mer utan tydligt uppslagsvärde.
- Tidiga kort- och ekosystemkapitel bör fortsätta använda korta förstaförklaringar när de nämner begrepp som förklaras mer senare.
- Felsökningskapitel och strömförsörjningskapitel får inte bli för avancerade utan praktiska hållpunkter.

## Strukturell kontroll

Följande snabbkontroller gjordes på kapitelmanuset:

| Kontroll | Resultat |
|---|---|
| Varje kapitel har exakt en H1-rubrik utanför kodblock | Godkänt |
| Inga H4-rubriker hittades utanför kodblock | Godkänt |
| Gamla kursrubriker som H2/H3 hittades inte | Godkänt |
| Kapitelordningen i `book.yaml` är konsekvent från inledning till kapitel 38 | Godkänt |
| `build/book.md` är sammanslagen enligt projektets kapitelordning | Godkänt |
| H1-rubriker som förekommer i kodblock påverkar inte kapitelstrukturen | Noterat, ej problem |

## Rekommendation

Gå vidare till **[PLAN] 11. Kontrollera markdown och exportbarhet**.

Ingen kapitelomflyttning behövs. Jag rekommenderar inte heller någon större omskrivning innan exportkontrollen. Eventuella små språkliga förstaförklaringar kan tas i ett senare finputs-/kvalitetspass om användaren vill.
