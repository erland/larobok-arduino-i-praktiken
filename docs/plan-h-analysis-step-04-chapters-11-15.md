# [ANALYSPLAN] steg 4 – Kapitel 11–15

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1–3 genomförda  
Status: Genomförd  
Resultattyp: Redaktionell analys. Inga kapitel eller bokmanus har ändrats.

## Omfattning

Detta steg analyserar kapitel 11–15 enligt projektets kapitelordning:

| Nr | Fil | Kapiteltyp enligt steg 1 | Funktion i boken |
|---:|---|---|---|
| 11 | `chapters/kloner-lagkostnadskort-11.md` | Kort och plattform | Hjälpa läsaren identifiera och bedöma kloner, lågkostnadskort och tredjepartsvarianter. |
| 12 | `chapters/moderna-arduino-kort-12.md` | Kort och plattform | Hjälpa läsaren bedöma moderna officiella Arduino-kort och portering från klassiska kort. |
| 13 | `chapters/esp8266-nodemcu-13.md` | Kort och plattform | Placera ESP8266/NodeMCU som billig Wi-Fi-plattform i Arduino-miljön. |
| 14 | `chapters/esp32-familjen-14.md` | Kort och plattform | Ge karta över ESP32-familjen, varianter, pinout, nätverk och typiska fallgropar. |
| 15 | `chapters/raspberry-pi-pico-15.md` | Kort och plattform | Förklara Pico/RP2040/RP2350 som Arduino-kompatibel experimentplattform. |

Analysen har läst faktisk kapiteltext och fokuserar särskilt på plattformskapitlens roll: ska de fungera som guide, referens, kortvalsunderlag eller kursmoment?

## Snabb kvantitativ översikt

| Kapitel | Ord | H2 | H3 | Kodblock | `Praktiskt test` | `Prova vidare` | Kontrollsektion | `Valguide` | `Snabbval` |
|---:|---:|---:|---:|---:|---|---|---|---|---|
| 11 | 4617 | 25 | 22 | 8 | Ja | Ja | Ja: `Kontrollera ditt val` | Ja | Ja |
| 12 | 4730 | 20 | 24 | 7 | Ja | Ja | Ja: `Kontrollera ditt val` | Ja | Ja |
| 13 | 4192 | 22 | 13 | 6 | Ja | Ja | Ja: `Kontrollera ditt val` | Ja | Ja |
| 14 | 4124 | 24 | 12 | 7 | Ja | Nej | Ja: `Kontrollera ditt val` | Ja | Ja |
| 15 | 4104 | 21 | 17 | 11 | Ja | Nej | Ja: `Kontrollera ditt val` | Ja | Ja |

Tolkning: blocket har stark handboksnytta eftersom det hjälper läsaren välja och bedöma plattformar. Samtidigt finns ett återkommande mönster där varje kapitel nästan alltid slutar med praktiskt test, kontrollfrågor och snabbval. Det ger konsekvens, men riskerar också att göra plattformskapitlen mer kurslika och längre än de behöver vara.

## Övergripande slutsats

Kapitel 11–15 är i grunden ett av bokens mest handboksnära block. Ämnet lämpar sig naturligt för handbok: läsaren behöver kunna identifiera kort, förstå skillnader, välja rätt plattform, undvika pinout- och spänningsfällor och dokumentera sitt val. Många avsnitt fungerar redan som beslutsstöd snarare än traditionell undervisning.

Det redaktionella problemet är främst att **kapitlen ibland behandlar plattformskunskap som en serie övningar**. I stället för att fråga läsaren vad hen lärt sig bör kapitlen hjälpa läsaren att fatta bättre kortval och felsöka verkliga projekt.

För `[PLAN-H]` bör detta block därför inte rensas hårt. Det bör renodlas:

- `Praktiskt test` bör i plattformskapitel ofta bli `Kortprofil`, `Minsta fungerande verifiering`, `Porteringstest` eller `Validera kortet`.
- `Prova vidare` bör inte formuleras som övningar utan som frivilliga arbetsmönster: `Fördjupa kortprofilen`, `Jämför alternativ`, `Portera ett befintligt exempel`.
- `Kontrollera ditt val` bör behållas som idé men byta form till `Snabb kontroll före kortval`, `Valfrågor` eller `Beslutschecklista`.
- `Snabbval` fungerar väl, men bör placeras så att det inte känns som en efterhandsbilaga efter quiz. I flera kapitel skulle `Snabbval` kunna komma före kontroll-/valfrågor eller ersätta dem.

## Kapitel 11 – Kloner, lågkostnadskort och tredjepartsvarianter

### Det fungerar väl

Kapitlet har mycket stark handboksidentitet. Det behandlar ett verkligt problem: läsaren har ett kort i handen men vet inte exakt vad det är, hur det ska väljas i Arduino IDE eller vilka risker som följer med pinout, USB-chip, bootloader och logiknivå.

Särskilt bra fungerar:

- skillnaden mellan formfaktorklon, mikrokontrollerkompatibilitet, API-kompatibilitet och modulkompatibilitet,
- avsnitten om CH340, CP210x och FTDI,
- bootloader som felsökningslager,
- skillnaden mellan pinout, silkscreen och kod,
- valguiden mellan lågkostnadskort och bättre dokumenterade/officiella kort,
- praktiskt test som går ut på att skapa en kortidentitet.

Kapitlets praktiska test är mer motiverat än flera tidigare teoriövningar. Att identifiera ett okänt kort är en verklig handbokssituation, inte ett konstruerat skolmoment.

### Läroboksspår

Kapitlet har både `Praktiskt test`, `Prova vidare`, `Kontrollera ditt val` och flera övningsformuleringar. Det gör slutdelen något kursbokslik trots att innehållet är användbart.

Exempel på struktur som bör justeras i PLAN-H:

- `Prova vidare` innehåller `Övning 1`, `Övning 2`, `Övning 3` och `Fördjupning`.
- `Kontrollera ditt val` består av tio frågor som delvis fungerar som quiz.
- `Snabbval` kommer efter kontrollfrågorna, trots att det är mer direkt användbart för handboksläsaren.

### Rekommendation för PLAN-H

Kapitlet bör inte kortas kraftigt. Det bör i stället byta redaktionell ram:

- Byt `Praktiskt test: identifiera ett okänt kompatibelt kort` till exempelvis `Skapa en kortidentitet`.
- Byt `Prova vidare` till `Fördjupa kortprofilen`.
- Gör övningarna till praktiska arbetskort eller checklistor.
- Byt `Kontrollera ditt val` till `Snabb kontroll innan du använder kortet`.
- Flytta eller integrera `Snabbval` närmare valguiden.

### Bedömning

| Aspekt | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg |

## Kapitel 12 – Moderna Arduino-kort

### Det fungerar väl

Kapitlet har en tydlig handboksuppgift: hjälpa läsaren förstå när moderna officiella Arduino-kort är bättre än klassiska kort, kloner, ESP-kort eller RP2040/RP2350-kort. Det är särskilt starkt när det jämför val utifrån projektkrav snarare än modellnamn.

Särskilt bra fungerar:

- att kapitlet undviker att bli en kortkatalog,
- avsnittet om varför modernare inte automatiskt betyder enklare,
- valguiden med projektkrav och rekommenderad kortfamilj,
- jämförelsen mellan moderna Arduino-kort och andra kortfamiljer,
- avsnittet om portering: pinnummer, spänning, analog läsning, PWM, timers och bibliotek.

Kapitlet har bra potential att fungera som beslutsstöd.

### Läroboksspår

Kapitlets praktiska test är relevant, men omfattningen gör att det nästan blir ett kurslabb. Det kombinerar digital knapp/LED, analog läsning, PWM och I2C i samma test. Det kan vara användbart, men bör ramas in som ett **porteringstest** snarare än ett experiment.

`Prova vidare` innehåller flera övningar som är bra i sak men skolmässigt presenterade:

- skapa kortprofil,
- portera kapitel 5-experiment,
- jämföra uppkopplingsvägar,
- analysera biblioteksportabilitet.

`Kontrollera ditt val` är bättre än `Kontrollera att du hänger med`, men består fortfarande av frågeformat som ligger nära quiz.

### Rekommendation för PLAN-H

Kapitlet bör bli ett tydligare portering- och beslutskapitel:

- Byt `Praktiskt test: jämför samma sketch på klassiskt och modernt kort` till `Porteringstest: samma sketch på två kort`.
- Gör `Prova vidare` till `Porteringschecklista och jämförelser`.
- Behåll frågorna i sak men konvertera dem till `När du väljer modernt kort, kontrollera särskilt`.
- Lägg större vikt vid beslutstabellen och minska känslan av lektionsuppgifter.

### Bedömning

| Aspekt | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg |

## Kapitel 13 – ESP8266 och NodeMCU

### Det fungerar väl

Kapitlet är praktiskt välriktat. Det förklarar varför ESP8266 inte bara är en UNO med Wi-Fi, utan en egen plattform med särskilda begränsningar: 3,3 V-logik, boot-pinnar, D/GPIO-mappning, A0-område, strömspikar och nätverksbeteende.

Särskilt bra fungerar:

- distinktionen mellan ESP8266-chip, modul och utvecklingskort,
- avsnitten om NodeMCU-pinnar och GPIO-pinnar,
- genomgången av boot-relaterade pinnar,
- timeout-tänk i Wi-Fi-kod,
- praktisk struktur för ESP8266-projekt,
- valguide och snabbval.

Kapitlet ligger nära bokens handboksidentitet eftersom det hjälper läsaren undvika verkliga fel.

### Läroboksspår

`Praktiskt test: Wi-Fi-baserad sensorindikator` är praktiskt relevant, men formuleras delvis som ett träningsmoment. Formuleringen `Målet är att träna på robust projektstruktur, pinout-dokumentation och nätverksfelsökning` är pedagogiskt rimlig men något kurslik.

`Prova vidare` innehåller tre test som i praktiken är bra arbetsmönster:

- dokumentera ESP8266-kort,
- I2C-scanner,
- webbsida med sensorvärde.

De bör inte heta test i en handbok om de inte är minimala verifieringstester. De kan i stället bli `Tre användbara verifieringar`.

`Kontrollera ditt val` fungerar bättre än ren quiz, men bör omvandlas till besluts- och riskkontroll.

### Rekommendation för PLAN-H

Kapitlet bör behålla sina praktiska moment, men få mer handboksnära rubriker:

- `Praktiskt test` → `Minsta fungerande Wi-Fi-nod`.
- `Prova vidare` → `Tre verifieringar för ESP8266-projekt`.
- `Kontrollera ditt val` → `Kontrollera innan du väljer ESP8266`.
- Betona reservläge, timeout och pinoutdokumentation som återanvändbara mönster, inte som övningsmål.

### Bedömning

| Aspekt | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg |

## Kapitel 14 – ESP32-familjen i Arduino-världen

### Det fungerar väl

Kapitlet har en tydlig och vuxen handbokston i början. Det förklarar att ESP32 är en familj, inte ett kort, och att läsaren inte ska memorera varje variant utan kunna resonera om val och begränsningar. Det är en mycket bra handboksposition.

Särskilt bra fungerar:

- frågorna i `Snabb orientering`, eftersom de är beslutsfrågor snarare än lärandemål,
- skillnaden mellan chip, modul och utvecklingskort,
- avsnitten om 3,3 V, pinout, boot-pinnar och ADC,
- att Wi-Fi, BLE, deep sleep och bussar behandlas som praktiska plattformsfrågor,
- `Felsökning` och `Vanliga misstag`, som är mycket handboksnära.

Kapitel 14 är ett positivt exempel för hur plattformskapitel kan låta mer som handbok än lärobok.

### Läroboksspår

Det största läroboksspåret är det praktiska testets `Mål`-avsnitt:

> Efter experimentet ska du ha ...

Detta liknar målformuleringar från en kurs eller workshop. Själva testet är däremot relevant. Ett ESP32-kapitel bör absolut innehålla en minimal nätverks- eller sensorverifiering.

`Kontrollera ditt val` är bättre än traditionella kunskapsfrågor, men innehåller fortfarande tio quizliknande frågor.

### Rekommendation för PLAN-H

Kapitel 14 bör användas som modell för flera andra plattformskapitel, men justera slutramen:

- Byt `Mål` i praktiskt test till `Det här verifierar testet`.
- Byt `Praktiskt test: ESP32 som Wi-Fi-baserad sensorindikator` till `Verifiering: ESP32 med Wi-Fi, timeout och lokal drift`.
- Byt `Kontrollera ditt val` till `Riskkontroll innan du väljer ESP32`.
- Behåll `Felsökning` och `Vanliga misstag` nästan oförändrade, eftersom de stärker handbokskänslan.

### Bedömning

| Aspekt | Bedömning |
|---|---|
| Handbokskänsla | 4,5/5 |
| Läroboksspår | Låg–medel |
| Behov av redaktionell åtgärd | Låg–medel |
| Risk vid ändring | Låg |

## Kapitel 15 – Raspberry Pi Pico, RP2040 och RP2350 i Arduino-miljö

### Det fungerar väl

Kapitlet är starkt som orienterande plattformskapitel. Det förklarar Pico som ett sidospår i Arduino-världen utan att överdriva eller förminska plattformen. Det gör även bra skillnad mellan Pico, Pico W, Pico 2, Pico 2 W, RP2040 och RP2350.

Särskilt bra fungerar:

- att kapitlet tydligt säger när Pico är rätt respektive fel val,
- avsnitten om PIO, USB, analog mätning, flera kärnor och samtidighet,
- praktisk betoning på GP-nummer, pinout och 3,3 V-logik,
- `Valguide`, `Vanliga misstag`, `Felsökning` och `Sammanfattande valbild`.

Kapitlet har redan flera handbokselement som bör återanvändas i PLAN-H.

### Läroboksspår

Det praktiska testet är relevant men mycket labbliknande: potentiometer, knapp, LED, kopplingsidé, kod och förväntat resultat. Det passar bra om läsaren faktiskt har Pico framför sig, men i ett plattformskapitel bör testets roll vara tydligare: det är en **lokal verifiering av I/O, ADC, pullup och pinout**, inte en övning som alla måste göra.

`Kontrollera ditt val` innehåller flera bra beslutsfrågor, men bör formateras som valhjälp snarare än kunskapskontroll.

### Rekommendation för PLAN-H

- Byt `Praktiskt test: Pico som lokal sensor- och styrnod` till `Verifiering: Pico som lokal I/O-nod`.
- Gör `Viktig kontroll` i testet mer framträdande, eftersom det är handboksnyttan.
- Byt `Kontrollera ditt val` till `Välj Pico med dessa frågor`.
- Behåll `Sammanfattande valbild`; den är en bra kandidat för återanvändbar struktur i andra plattformskapitel.

### Bedömning

| Aspekt | Bedömning |
|---|---|
| Handbokskänsla | 4,5/5 |
| Läroboksspår | Låg–medel |
| Behov av redaktionell åtgärd | Låg–medel |
| Risk vid ändring | Låg |

## Återkommande mönster i kapitel 11–15

### 1. Plattformskapitlen är mer handboksnära än de tidiga teorikapitlen

Det här blocket har tydligare användningsnytta än kapitel 1–10. Läsaren får hjälp med faktiska val:

- vilket kort passar,
- vilka risker finns,
- vilka pinnar ska undvikas,
- vilken spänning gäller,
- vilken dokumentation behövs,
- vilka alternativ bör övervägas.

Det är precis rätt riktning för boken.

### 2. `Snabb orientering` fungerar bättre när den är en karta, inte ett mål

Kapitel 14 och 15 visar den bästa formen: de förklarar varför kapitlet finns och vilka frågor det hjälper läsaren besvara. Kapitel 13 är också nära. Kapitel 11 och 12 har starkt innehåll, men kan bli ännu mer fokuserade genom att göra orienteringen kortare och mer beslutsinriktad.

PLAN-H bör därför inte avskaffa `Snabb orientering`, utan definiera dess funktion:

> `Snabb orientering` ska ge användningskarta och beslutsfrågor, inte lärandemål.

### 3. `Praktiskt test` är motiverat men bör byta namn

I plattformskapitel finns ofta ett legitimt behov av verifiering. Man måste ibland testa USB, boardval, blink, I2C, Wi-Fi, pinout eller analog läsning. Men rubriken `Praktiskt test` är för generell och låter ibland som kursmoment.

Bättre rubriker för PLAN-H:

- `Skapa en kortprofil`
- `Minsta fungerande verifiering`
- `Porteringstest`
- `Verifiera pinout och boardval`
- `Verifiering: Wi-Fi, timeout och lokal drift`
- `Verifiering: lokal I/O-nod`

### 4. `Prova vidare` bör ersättas eller begränsas

Kapitel 11–13 använder `Prova vidare`. Innehållet är ofta värdefullt men presenteras som övningar. I en handbok bör detta hellre bli frivilliga arbetsmönster:

- `Fördjupa kortprofilen`
- `Jämför två kort`
- `Portera ett befintligt exempel`
- `Dokumentera plattformen i projektets README`
- `Verifiera I2C på detta kort`

PLAN-H bör avråda från rubriken `Övning` i plattformskapitel om det inte uttryckligen är en workshopdel.

### 5. `Kontrollera ditt val` är bättre än quiz men kan bli ännu mer handbok

Till skillnad från `Kontrollera att du hänger med` är `Kontrollera ditt val` närmare handbokstänk. Men frågeformen och placeringen efter `Prova vidare` gör att den ändå kan läsas som quiz.

Bättre format:

- `Snabb kontroll före kortval`
- `Riskkontroll`
- `Valfrågor`
- `Checklista innan du bygger`
- `När detta kort är rätt val`

### 6. `Snabbval` fungerar väl men bör prioriteras

`Snabbval` är ett av de mest handboksnära elementen i blocket. Det bör inte ligga efter quizliknande kontrollfrågor på ett sätt som gör att läsaren möter det sist. I flera kapitel bör `Snabbval` antingen:

- komma direkt efter `Valguide`,
- ersätta delar av `Kontrollera ditt val`,
- eller fungera som avslutande referens utan extra quiz.

## Förslag till PLAN-H-regler från detta block

1. **Plattformskapitel ska primärt vara val- och riskstöd.**  
   De ska hjälpa läsaren välja kort, dokumentera kortprofil, förstå begränsningar och verifiera minimalt innan projektet växer.

2. **`Praktiskt test` byts normalt till mer exakt rubrik i plattformskapitel.**  
   Exempel: `Kortprofil`, `Porteringstest`, `Minsta fungerande verifiering`, `Verifiera boardval och pinout`.

3. **`Prova vidare` ska inte vara standard i plattformskapitel.**  
   Om innehållet behövs ska det omformas till arbetsmönster, checklistor eller frivilliga fördjupningar utan skolordet `Övning`.

4. **`Kontrollera ditt val` behålls i sak men byter format.**  
   Frågor bör bli beslutschecklistor, riskkontroller eller valmatriser.

5. **`Snabbval` ska lyftas fram som handbokselement.**  
   Det bör placeras före eller i direkt anslutning till valguide och inte gömmas efter quizliknande frågor.

6. **Kapitel 14 och 15 kan användas som positiva strukturmodeller.**  
   De har tydligare handbokston och bra balans mellan karta, praktiska risker, felsökning och valbild.

7. **Kapitel 11 och 12 behöver främst rubrik- och slutdelsnormalisering.**  
   Innehållet är starkt, men slutramen bör göras mindre kurslik.

## Sammanfattande bedömning för blocket

| Bedömningsområde | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg |

Kapitel 11–15 är ett starkt block. Det bör inte skrivas om i grunden. PLAN-H bör framför allt göra slutdelarna mer handboksnära: praktiska test ska bli verifieringar, övningar ska bli arbetsmönster, och kontrollfrågor ska bli besluts- eller riskchecklistor. Då kan blocket bli en modell för hur plattforms- och kortkapitel ska fungera i hela boken.
