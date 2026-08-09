# [PLAN] Batchjustering 1: orienteringskapitel

Datum: 2026-06-30  
Plansteg: 7. Batchjustera resten av kapitlen  
Batch: 1 av 7  
Omfattning: Kapitel 1–4  
Status: Genomförd.

## Syfte

Denna batch harmoniserar bokens orienteringskapitel med den slutliga strukturregeln i `docs/final-structure-rule.md`.

Målet är att kapitlen 1–4 ska fungera som en praktisk karta in i boken, utan att kännas som formella kurslektioner. De ska fortfarande kunna läsas i ordning, men också vara lätta att slå upp när läsaren behöver förstå ekosystem, kortval, arbetsmiljö eller elektriska grundbegrepp.

## Kapitel som ingår

| Kapitel | Fil | Status | Kommentar |
|---:|---|---|---|
| 1 | `chapters/ekosystem-01.md` | Batchjusterat | Kursliknande inledning ersatt med `Snabb orientering` och kort `Förutsättningar`. |
| 2 | `chapters/valja-ratt-kort-02.md` | Tidigare pilotjusterat | Bevarat som redan justerat orienteringskapitel. |
| 3 | `chapters/utvecklingsmiljo-bibliotek-03.md` | Batchjusterat | Inledning, övningsrubrik, quizrubrik och avslutning anpassade till handboksstruktur. |
| 4 | `chapters/elektriska-grunder-04.md` | Batchjusterat | Inledning, praktiska tester och kontrollfrågor anpassade till orienteringsmall. |

## Genomförda strukturändringar

- `Varför detta kapitel finns`, `Lärandemål` och `Innan vi börjar` har ersatts av `Snabb orientering` och vid behov `Förutsättningar`.
- `Övningar` har ersatts med `Prova själv` där kapitlet fortfarande behöver aktiva moment.
- `Praktiskt experiment` har ersatts med `Praktiskt test` för att ge mer handbokston.
- `Quiz/reflektionsfrågor` och `Quiz och reflektionsfrågor` har ersatts med `Kontrollera att du hänger med`.
- `Nästa steg` har ersatts med `Se också`.
- Kapitel 2 har inte skrivits om på nytt eftersom det redan fungerade som pilot för orienteringskapitel.

## Redaktionell bedömning

Batchen lyckades väl. Kapitel 1, 3 och 4 har nu en tydligare praktisk start och mindre skolbokskänsla. Kapitel 2 ligger redan nära den önskade strukturen och behövde därför inte ändras i denna batch.

Orienteringsdelen fungerar nu bättre som första ingång till boken:

- kapitel 1 ger kartan över Arduino-ekosystemet,
- kapitel 2 hjälper läsaren välja kort,
- kapitel 3 gör experiment reproducerbara,
- kapitel 4 ger den elektriska miniminivån för resten av boken.

## Rekommenderad nästa batch

Nästa steg är **Batch 2: kapitel 5–9**, det vill säga grundfunktionskapitlen. Där bör fokus ligga på att ersätta kursmarkörer med mer praktiska rubriker som `Grundidé`, `När du använder detta`, `Kodmönster`, `Felsökning`, `Praktiskt test`, `Snabb sammanfattning` och `Se också`.
