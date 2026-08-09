# Redaktionellt förbättringspass

Datum: 2026-06-30  
Fas: Redaktionell förbättring efter progressionsgranskning  
Omfattning: Begränsad strukturell förbättring utan ändrad kapitelordning.

## Syfte

Detta pass åtgärdar de viktigaste rekommendationerna från progressionsgranskningen:

- tydligare förstaförklaringar av begrepp som används tidigt,
- mer konsekventa referensrutor i teknik- och komponentkapitel,
- säkerhetsrutor i kapitel med högre elektrisk eller praktisk risk,
- fler korsreferenser mellan grunder, komponentkapitel och systembygge.

## Genomförda åtgärder

### Förstaförklaringar

Följande kapitel har fått extra begreppsförklaringar:

- Kapitel 1: Arduino core, board package och bibliotek.
- Kapitel 4: logiknivå och gemensam jord.
- Kapitel 5: pull-up, pull-down och open drain.
- Kapitel 9: nivåskiftning och bussdisciplin.
- Kapitel 11: bootloader, USB-seriechip och pinout.

### Säkerhetsrutor

Följande kapitel har fått tydligare säkerhetsrutor:

- Kapitel 18: strömbudget för adresserbara LED.
- Kapitel 20: motorer som induktiva laster.
- Kapitel 21: reläer, MOSFET:ar och lågspänningsavgränsning.
- Kapitel 28: säker mätning av ström och spänning.
- Kapitel 31: drivkretsar, värme, polaritet och skydd.
- Kapitel 33: analoga ingångsgränser.
- Kapitel 34: batterier, regulatorer och energikällor.

### Referensrutor

Kapitel 10–34 har fått en mer konsekvent referensruta med:

- typisk spänning,
- typiskt gränssnitt,
- välj när,
- välj inte när,
- vanliga fel,
- alternativ att överväga.

Det stärker bokens funktion som uppslagsverk utan att göra kapitelordningen mer fragmenterad.

### Korsreferenser

Följande kapitel har fått extra korsreferenser till relevanta grundkapitel och närliggande komponentkapitel:

- Kapitel 17, 18, 20, 21
- Kapitel 23–28
- Kapitel 30–33
- Kapitel 37

## Bedömning efter passet

Bokens progression är fortfarande densamma, men läsaren får fler stödstrukturer när kapitlen används separat som referens. Förbättringarna gör framför allt tre saker:

1. De minskar risken att viktiga begrepp används innan de förklarats.
2. De gör sensor-, aktuator- och IC-kapitel mer konsekventa.
3. De lyfter säkerhetsfrågor där praktiska experiment annars kan misstolkas som ofarliga standardkopplingar.

## Kvarvarande rekommenderade steg

Nästa pass bör vara en exportförberedande granskning:

- kontrollera rubriknivåer och listor,
- kontrollera att tabeller renderas stabilt,
- kontrollera att metadata och kapitelordning är korrekta,
- provköra exportscriptet där lokal Pandoc-miljö finns,
- besluta om omslagsbild ska genereras eller endast prompten ska behållas.

## Ändrade filer

Se projektstatus för sammanfattning och respektive kapitel för infogade redaktionella sektioner.
