# [PLAN2] Batch 5: sensor- och mätkapitel – korsreferenser

Datum: 2026-07-01  
Plansteg: [PLAN2] batch 5  
Kapitel: 23–29  
Status: Genomförd

## Syfte

Batch 5 granskar `Se också`, `Korsreferens` och liknande hänvisningar i sensor- och mätkapitlen.

Målet är att sensoravsnitten ska fungera som uppslagskapitel. Hänvisningar ska därför bara finnas kvar när de hjälper läsaren med ett konkret val, en mätprincip, signalbehandling, elektriska krav eller felsökning.

## Beslut per kapitel

| Kapitel | Fil | Beslut |
|---:|---|---|
| 23 | `miljosensorer-23.md` | Linjärt `Se också` togs bort. Tidigare `Korsreferens` omformulerades till `Relaterat` med fokus på kommunikationsbussar och I2C-felsökning. |
| 24 | `ljus-farg-optiska-sensorer-24.md` | Linjärt `Se också` togs bort. Tidigare `Korsreferens` omformulerades till `Relaterat` med fokus på analog mätning och I2C/SPI. |
| 25 | `avstand-narvaro-25.md` | Linjärt `Se också` togs bort. Tidigare `Korsreferens` omformulerades till `Relaterat` med fokus på digitala signaler, analog mätning och seriella sensormoduler. |
| 26 | `rorelse-orientering-26.md` | Linjärt `Se också` togs bort. Tidigare `Korsreferens` omformulerades till `Relaterat` med fokus på avbrott, watchdog och robust körning. |
| 27 | `ljud-mikrofoner-27.md` | Linjärt `Se också` togs bort. Tidigare `Korsreferens` omformulerades till `Relaterat` med fokus på analoga signaler och timing. |
| 28 | `strom-spanning-energi-28.md` | Linjärt `Se också` togs bort. Tidigare `Korsreferens` omformulerades till `Relaterat` med fokus på ADC, strömbudget och felsökning. |
| 29 | `position-tid-identitet-29.md` | Linjärt `Se också` ersattes med `Relaterat`, eftersom kapitlet har praktiska kopplingar till kommunikation, minne, loggning och felsökning. |

## Redaktionell bedömning

Batch 5 bör inte behålla sekventiella övergångar mellan sensorkapitel. Sensorerna är tematiskt besläktade, men läsaren kommer ofta att slå upp ett specifikt mätproblem snarare än läsa sensorerna i ordning.

De kvarvarande `Relaterat`-sektionerna motiveras därför av praktiska beroenden:

- mätprinciper,
- signalnivåer,
- bussar och bibliotek,
- felsökning,
- strömförsörjning,
- loggning och datalagring.

## Resultat

- Mekaniska `Se också`-avsnitt är borttagna ur kapitel 23–29.
- Tidigare `Korsreferens`-rubriker har ersatts av mer problemorienterade `Relaterat`-sektioner.
- Kapitel 29 har fått en kort `Relaterat`-sektion i stället för en linjär övergång till kapitel 30.
- Hänvisningarna stödjer uppslagsläsning snarare än kapitelordning.

## Kontroll

Efter batchen ska projektet valideras med exportscriptet och `build/book.md` byggas om.
