# [PLAN] Batchjustering 6: robusthets- och kretskapitel

## Omfattning

Detta dokument sammanfattar genomförd batchjustering enligt `[PLAN]` steg 7, batch 6.

Batchen omfattar kapitel 30–34:

| Kapitel | Fil | Kapiteltyp |
|---:|---|---|
| 30 | `chapters/io-expansion-30.md` | Robusthets- och kretskapitel |
| 31 | `chapters/drivkretsar-31.md` | Robusthets- och kretskapitel |
| 32 | `chapters/displaykretsar-minne-32.md` | Robusthets- och kretskapitel |
| 33 | `chapters/analog-signalanpassning-33.md` | Robusthets- och kretskapitel |
| 34 | `chapters/stromforsorjning-batteridrift-34.md` | Robusthets- och kretskapitel |

## Redaktionell princip

Kapitlen har justerats från en mer traditionell kursboksstruktur till en mer handboksnära struktur. Målet är att läsaren snabbt ska kunna använda kapitlen för praktiska val, robustare kopplingar och felsökning.

Särskild prioritet i denna batch:

- tydligare snabb orientering,
- praktisk nytta i stället för formella lärandemål,
- kortare och mer funktionella förutsättningar,
- praktiska test i stället för övningskänsla,
- tydligare felsökning i hårdvarunära kapitel,
- snabbreferenser och snabbval,
- `Se också` i stället för kursmässigt `Nästa steg`.

## Genomförda strukturändringar

| Tidigare rubrik | Ny hantering |
|---|---|
| `Varför detta kapitel finns` | `Snabb orientering` |
| `Lärandemål` | `Det du kan använda kapitlet till` |
| `Innan vi börjar` | `Förutsättningar` |
| `Praktiskt experiment` | `Praktiskt test` |
| `Övningar` | `Prova vidare` |
| `Övning N` | `Test N` |
| `Quiz/reflektionsfrågor` | `Kontrollera ditt val` |
| `Quiz och reflektionsfrågor` | `Kontrollera ditt val` |
| `Referenssammanfattning` | `Snabbreferens` |
| `Referensruta: snabbval` | `Snabbval` |
| `Nästa steg` | `Se också` |

## Kapitelvisa noteringar

### Kapitel 30: I/O-expansion, shift registers och multiplexers

Kapitlet har harmoniserats mot en praktisk krets- och valguide. Befintlig felsökningsdel har bevarats och de avslutande sektionerna har gjorts mer uppslagsverksvänliga.

### Kapitel 31: Drivkretsar för LED, motorer och laster

Kapitlet har fått tydligare handboksstruktur kring drivval och praktiska tester. En separat `Felsökning`-sektion har lagts till eftersom drivkretsar ofta ger fel som ser ut som kodfel men i själva verket handlar om jord, matning, strömgränser, induktiva laster eller PWM.

### Kapitel 32: Displaykretsar, minne och datalagring

Kapitlet har harmoniserats mot snabbare orientering, praktiska val och referensstruktur. Befintlig felsökning har bevarats eftersom kombinationen display, minne, SPI/I2C och SD-kort ofta kräver konkret felsökningsstöd.

### Kapitel 33: Analog signalanpassning, op-förstärkare och komparatorer

Kapitlet har fått tydligare praktisk struktur för val mellan direktkoppling, filtrering, förstärkning, skydd och färdiga moduler. En separat `Felsökning`-sektion har lagts till med fokus på brus, mättnad, common-mode-problem, hysteres och jordning.

### Kapitel 34: Strömförsörjning, batteridrift och robust konstruktion

Kapitlet har gjorts mer handboksnära med fokus på strömbudget, robust konstruktion och felsökning. En separat `Felsökning`-sektion har lagts till eftersom strömproblem ofta uppträder som slumpmässiga omstarter, mätbrus eller instabil trådlös kommunikation.

## Kontroll efter batch

Efter batchjusteringen har följande kontroller gjorts:

- De gamla kursrubrikerna är borttagna ur kapitel 30–34.
- Inga H4-rubriker används i de justerade kapitlen.
- `build/book.md` är uppdaterad från aktuell kapitelordning.
- Kapitlen följer den fastställda strukturregeln i `docs/final-structure-rule.md`.

## Nästa steg

Fortsätt med `[PLAN]` steg 7, batch 7: metod-, projekt- och referenskapitlen 35–38.
