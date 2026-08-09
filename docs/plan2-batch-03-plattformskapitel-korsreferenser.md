# [PLAN2] Batch 3: kort- och plattformskapitel

Datum: 2026-07-01  
Omfattning: kapitel 10–16  
Status: Genomförd

## Syfte

Batch 3 granskar `Se också` och korsreferenser i kort- och plattformskapitlen.

Målet är att undvika linjära övergångar mellan kortfamiljer och i stället låta kapitlen fungera som fristående valguider. Läsaren ska kunna slå upp ett kort eller en plattform utan att känna att kapitlet förutsätter att nästa kapitel läses direkt efteråt.

## Bedömningsregel

För plattformskapitlen behålls korsreferenser bara om de hjälper läsaren att göra ett konkret val mellan kort, förstå en faktisk kompatibilitetsfråga eller undvika ett praktiskt fel.

Mekaniska hänvisningar av typen "i nästa kapitel går vi vidare till..." tas bort.

## Granskade kapitel

| Kapitel | Fil | Beslut |
|---:|---|---|
| 10 | `klassiska-arduino-kort-10.md` | `Se också` togs bort. Kapitlet har redan `Snabbval` och konkreta alternativ. |
| 11 | `kloner-lagkostnadskort-11.md` | `Se också` togs bort. Avsnittet upprepade främst övergången till moderna Arduino-kort. |
| 12 | `moderna-arduino-kort-12.md` | `Se också` togs bort. Hänvisningarna till ESP8266/ESP32 hör bättre hemma i `Snabbval` och kapitel 38. |
| 13 | `esp8266-nodemcu-13.md` | `Se också` togs bort. Jämförelsen med ESP32 finns redan som valfråga och alternativ i kapitlet. |
| 14 | `esp32-familjen-14.md` | `Se också` togs bort. Jämförelsen med Pico/RP2040 ska hanteras som valstöd, inte som linjär övergång. |
| 15 | `raspberry-pi-pico-15.md` | `Se också` togs bort. Kapitlet står bättre som egen plattformsreferens. |
| 16 | `smakort-specialkort-16.md` | `Se också` togs bort. Övergången till LED/aktuatorer var mer kursbokslik än uppslagsnyttig. |

## Resultat

Alla `Se också`-sektioner i kapitel 10–16 har tagits bort.

Bedömningen är att dessa avsnitt främst fungerade som linjära övergångar mellan kapitel. För en uppslagsverksorienterad bok ger det bättre läsupplevelse att låta varje plattformskapitel avslutas med `Snabbval`, där praktiska val, risker och alternativ redan sammanfattas.

## Kvarvarande navigering

Navigering mellan kortfamiljer och plattformar ska i första hand ske via:

- `Snabbval` i respektive kapitel,
- kapitel 38: `referens-snabbvalsguider-38.md`,
- `docs/lookup-index.md`,
- punktvisa hänvisningar i brödtext där det finns ett faktiskt tekniskt beroende.

## Kontroll

Efter ändringen har projektet kontrollerats med exportscriptets markdownvalidering.

Resultat:

```text
Validering klar utan varningar.
```

## Nästa steg

Fortsätt med `[PLAN2]` batch 4: komponenter och aktuatorer, kapitel 17–22.
