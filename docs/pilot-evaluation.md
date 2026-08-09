# [PLAN] Utvärdering av pilotkapitel

Datum: 2026-06-30  
Plansteg: 5. Utvärdera pilotkapitlen  
Status: Genomförd.

## Syfte

Detta dokument utvärderar pilotjusteringen av kapitel 2, 8, 13, 20 och 38 mot den redaktionella målbilden: boken ska fungera som en praktisk Arduino-handbok med lärobokskvalitet, inte som en traditionell kursbok med samma formella kapitelmall överallt.

## Utvärderade kapitel

| Kapitel | Fil | Kapiteltyp | Bedömning |
|---:|---|---|---|
| 2 | `chapters/valja-ratt-kort-02.md` | Orienteringskapitel | Lyckad. Kapitlet fungerar bättre som vägledning och beslutsstöd. |
| 8 | `chapters/avbrott-watchdog-08.md` | Grundfunktionskapitel | Lyckad. Avsnitten leder tydligare från problem till robust lösning. |
| 13 | `chapters/esp8266-nodemcu-13.md` | Kort- och plattformskapitel | Mycket lyckad. Kapitlet är tydligare som val- och riskguide. |
| 20 | `chapters/servon-motorer-20.md` | Komponent- och aktuator-kapitel | Lyckad. Handboksnyttan stärks genom fokus på val, matning, kodstruktur och felsökning. |
| 38 | `chapters/referens-snabbvalsguider-38.md` | Referenskapitel | Mycket lyckad. Kapitlet beter sig nu som referens snarare än vanlig lektion. |

## Kontroll mot utvärderingsfrågor

### Känns inledningen mindre skolaktig?

Ja. De formella rubrikerna `Varför detta kapitel finns`, `Lärandemål` och `Innan vi börjar` har ersatts av `Snabb orientering`, `Förutsättningar` eller `Så använder du referensen`. Det ger en mer vuxen och praktisk ton.

### Går det snabbare att förstå vad kapitlet hjälper läsaren med?

Ja. Pilotkapitlen börjar snabbare med praktisk nytta, användningsområde eller beslutssituation. Det passar bättre för läsare som slår upp ett specifikt ämne.

### Är `Förutsättningar` lagom kort?

Delvis. Rubriken fungerar, men bör användas sparsamt. I vissa kapitel kan den med fördel vara mycket kort eller helt bakas in i `Snabb orientering`.

Rekommendation: använd `Förutsättningar` bara när kapitlet kräver specifik hårdvara, tidigare begrepp eller särskilda säkerhetsvillkor.

### Är `Prova själv` och `Praktiskt test` bättre än `Övningar`?

Ja. De nya rubrikerna passar bokens användningssätt bättre. De låter mindre som skoluppgifter och mer som praktiska experiment.

Rekommendation: använd `Praktiskt test` när aktiviteten är tydligt instruerad och `Prova själv` när aktiviteten är mer explorativ.

### Bör `Kontrollera ditt val` behållas, kortas eller tas bort i fler kapitel?

Den bör behållas selektivt, inte som standard. Den passar bäst i kapitel där läsaren gör ett val, exempelvis kort, sensor, drivkrets, kommunikationsbuss eller strömförsörjning.

Rekommendation: undvik quizkänsla. Formulera frågorna som beslutsstöd.

### Är `Se också` mer användbart än `Nästa steg`?

Ja. `Se också` är tydligare för en handbok och fungerar bättre när läsaren hoppar mellan kapitel.

Rekommendation: varje kapitel bör ha 3–6 relevanta korsreferenser, inte en lång lista.

## Samlad bedömning

Pilotjusteringen är lyckad. Den nya strukturen gör boken mer skumbar, mer praktisk och mer användbar som uppslagsverk, utan att ta bort den pedagogiska tydligheten.

Den största vinsten är att kapitlen nu börjar med läsarens situation och praktiska beslut, snarare än med formella kursmål.

## Små justeringar före batchning

Innan hela boken batchjusteras bör följande regler fastställas:

1. `Förutsättningar` ska vara valfri och kort.
2. `Kontrollera ditt val` ska bara användas i beslutsorienterade kapitel.
3. `Praktiskt test` ska prioriteras framför `Övningar`.
4. `Se också` ska ersätta `Nästa steg` i hela boken.
5. Referenskapitlet ska behålla sin egen struktur och inte följa övriga kapitelmallar.
6. Kapitelmallarna ska ses som riktlinjer, inte tvingande rubriklistor.

## Rekommendation

Gå vidare till nästa plansteg: fastställ slutlig strukturregel och använd pilotkapitlen som stilmall för resten av boken.

