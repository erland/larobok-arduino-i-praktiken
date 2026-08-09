# [PLAN2] Batch 2: grundfunktioner och korsreferenser

Datum: 2026-07-01  
Status: Genomförd  
Omfattning: kapitel 5–9

## Syfte

Denna batch granskar och justerar `Se också` i grundfunktionskapitlen enligt `[PLAN2]`.

Målet är att ta bort linjära övergångar till nästa kapitel och bara behålla korsreferenser som hjälper läsaren att lösa ett konkret problem, välja rätt teknik eller hitta ett relevant fördjupningskapitel.

## Granskade kapitel

| Kapitel | Fil | Beslut |
|---:|---|---|
| 5 | `chapters/digital-io-05.md` | `Se också` ersatt med `Relaterat`, eftersom digital I/O har tydliga beroenden till avbrott, bussar och laster. |
| 6 | `chapters/analog-lasning-adc-06.md` | `Se också` ersatt med `Relaterat`, med fokus på sensorer, energimätning och signalanpassning. |
| 7 | `chapters/pwm-timers-07.md` | `Se också` ersatt med `Relaterat`, med konkreta kopplingar till LED, ljud, motorer och robust tidsstyrning. |
| 8 | `chapters/avbrott-watchdog-08.md` | `Se också` ersatt med `Relaterat`, med kopplingar till digital I/O, tidsstyrning och felsökning. |
| 9 | `chapters/kommunikation-bussar-09.md` | `Se också` ersatt med `Relaterat`, med kopplingar till displayer, sensorer, expansion, minne och felsökning. |

## Redaktionellt beslut

Grundfunktionskapitlen behöver fler korsreferenser än orienteringskapitlen, men de ska inte fungera som linjära övergångar.

I denna batch har därför alla `Se också`-avsnitt tagits bort och ersatts av korta `Relaterat`-sektioner där hänvisningarna är problemorienterade.

## Princip som tillämpades

En korsreferens behölls eller lades till endast om den uppfyllde minst ett av följande kriterier:

- den hjälper läsaren välja rätt teknik,
- den pekar på ett faktiskt tekniskt beroende,
- den hjälper vid felsökning,
- den kopplar en grundfunktion till senare praktisk användning.

## Resultat

Batchen gör kapitel 5–9 mindre kursbokslika utan att ta bort viktiga tekniska samband.

`Relaterat` används här inte som mekanisk standardrubrik, utan som ett konkret stöd för uppslagsläsning i de kapitel där grundfunktioner återkommer i många senare delar av boken.
