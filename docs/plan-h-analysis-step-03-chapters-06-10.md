# [ANALYSPLAN] steg 3 – Kapitel 06–10

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1–2 genomförda  
Status: Genomförd  
Resultattyp: Redaktionell analys. Inga kapitel eller bokmanus har ändrats.

## Omfattning

Detta steg analyserar kapitel 6–10 enligt projektets kapitelordning:

| Nr | Fil | Kapiteltyp enligt steg 1 | Funktion i boken |
|---:|---|---|---|
| 06 | `chapters/analog-lasning-adc-06.md` | Grundfunktion | Förklara analog mätning, ADC, brus, filtrering och kalibrering. |
| 07 | `chapters/pwm-timers-07.md` | Grundfunktion | Förklara PWM, timers, icke-blockerande kod och tidsstyrda mönster. |
| 08 | `chapters/avbrott-watchdog-08.md` | Grundfunktion | Förklara polling, avbrott, timeouts, watchdog och robust körning. |
| 09 | `chapters/kommunikation-bussar-09.md` | Grundfunktion | Förklara UART, I2C, SPI, 1-Wire och praktisk bussfelsökning. |
| 10 | `chapters/klassiska-arduino-kort-10.md` | Kort och plattform | Hjälpa läsaren bedöma UNO, Nano och Mega som praktiska kortval. |

Analysen har läst faktisk kapiteltext och fokuserar på om de tidiga grundfunktionskapitlen och första kortkapitlet fungerar som praktisk handbok eller om de fortfarande bär spår av kurs-/lärobok.

## Snabb kvantitativ översikt

| Kapitel | Ord | H2 | H3 | Kodblock | `Det du kan använda kapitlet till` | `Praktiskt test` | `Prova själv` | Kontroll-/quizsektion |
|---:|---:|---:|---:|---:|---|---|---|---|
| 06 | 3860 | 21 | 10 | 16 | Ja | Ja | Ja | Ja: `Kontrollera att du hänger med` |
| 07 | 3913 | 24 | 14 | 13 | Ja | Ja | Ja | Ja: `Kontrollera att du hänger med` |
| 08 | 3527 | 20 | 13 | 18 | Nej | Ja | Ja | Nej, men kravspråk i experimentmål |
| 09 | 5530 | 22 | 42 | 11 | Ja | Ja, två stycken | Ja | Ja: `Kontrollera att du hänger med` |
| 10 | 3157 | 20 | 7 | 5 | Nej | Ja | Nej | Ja: `Kontrollera ditt val` |

Tolkning: blocket har hög praktisk nytta och mycket starkt ämnesinnehåll, men använder fortfarande flera läroboksmarkörer: upprepade målformuleringar, `Praktiskt test`, `Prova själv` och kontrollfrågor. I grundfunktionskapitel är detta delvis motiverat, men formen bör göras mer handboksmässig.

## Övergripande slutsats

Kapitel 6–10 är ett av bokens viktigaste tekniska fundament. Innehållet är relevant, användbart och väl placerat: analog mätning leder naturligt till PWM och timing, timing leder till robust körning, robust körning leder till kommunikation, och därefter börjar kortfamiljerna med klassiska Arduino-kort.

Det redaktionella problemet är inte att kapitlen har praktiska moment. Tvärtom behöver flera av ämnena testas i kod och koppling för att bli begripliga. Problemet är att praktiska moment ibland presenteras som kursövningar snarare än som handboksnära valideringsmönster, felsökningsmetoder eller återanvändbara minimala testfall.

För `[PLAN-H]` bör detta block därför inte rensas från praktik. Det bör i stället normaliseras från:

- `Praktiskt test` till exempelvis `Minsta fungerande test`, `Testa i praktiken` eller `Validera kopplingen`,
- `Prova själv` till `Varianter att prova`, `Bygg vidare när du behöver` eller `Fördjupa vid behov`,
- `Kontrollera att du hänger med` till `Snabb självkontroll`, `Vanliga missförstånd` eller `Kontrollera i ditt projekt`,
- kravliknande målformuleringar till användningsnära formuleringar.

## Kapitel 06 – Analog läsning, ADC och mätosäkerhet

### Det fungerar väl

Kapitlet är ett starkt grundfunktionskapitel. Det förklarar tydligt att `analogRead()` inte ger en absolut sanning utan ett mätvärde som påverkas av referensspänning, brus, koppling, kablar, matning och kortfamilj. Det är exakt den typ av förståelse som behövs innan senare sensorkapitel.

Rubriker som `Referensspänningen är mätningens linjal`, `Brus är normalt`, `Hysteresis för stabila beslut` och `Felsökning av analoga mätningar` har god handbokskänsla. De hjälper läsaren förstå praktiska felmoder snarare än att bara memorera begrepp.

Avsnittet `Praktiskt test: kalibrerad analog läsning med potentiometer` är ämnesmässigt motiverat. Potentiometern fungerar som ett återanvändbart testverktyg för analog läsning, filtrering och kalibrering.

### Problem

Kapitlet har både `Praktiskt test`, `Prova själv` och `Kontrollera att du hänger med`. Kombinationen gör att kapitlet upplevs mer som en lektionsmodul än som en handbokssida, trots att innehållet är praktiskt.

`Det du kan använda kapitlet till` är bättre än "Efter kapitlet ska du kunna", men följande formulering förstärker fortfarande kurskänslan:

> Kapitlet hjälper dig att:

Det är inte fel, men när samma formulering återkommer i flera kapitel blir den mekanisk. För detta kapitel skulle en mer handboksnära variant kunna vara:

> Använd kapitlet när du behöver tolka analoga värden, stabilisera brusiga mätningar eller avgöra om en analog ingång är rätt lösning.

`Prova själv` innehåller flera uppgifter som liknar kursövningar. De är relevanta, men bör troligen omformas till valfria varianter eller felsökningsscenarier. Exempelvis är `Test 3: mät matningens betydelse` praktiskt värdefullt men bör kännas som "kontrollera ditt projekt" snarare än "besvara frågor".

`Kontrollera att du hänger med` bör inte ligga kvar i sin nuvarande form. Frågorna är bra, men rubriken signalerar kontroll och examination.

### Rekommendation inför PLAN-H

- Behåll praktiskt analogtest, men byt rubrik till en mer handboksnära testform.
- Slå ihop eller underordna `Prova själv` som `Varianter och felsökningsscenarier`.
- Ersätt kontrollfrågorna med `Vanliga missförstånd` eller `Snabb kontroll i ditt projekt`.
- Mjukgör `Kapitlet hjälper dig att` till en användningsorienterad introduktion.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg |

## Kapitel 07 – PWM, timers och tidsstyrning

### Det fungerar väl

Kapitlet är mycket viktigt för hela boken. Det binder ihop digital I/O, analogt tänkande, PWM, `millis()` och icke-blockerande kod. Den röda tråden är stark: läsaren går från enkel styrning till kodmönster som krävs i mer realistiska projekt.

Avsnitten om `delay()`, `millis()`, flera samtidiga aktiviteter och timerresurser har hög praktisk nytta. Kapitlet förklarar inte bara hur man skriver kod, utan varför vissa Arduino-exempel blir sköra när projektet växer.

`Snabbreferens` är ett positivt exempel på handboksformat. Tabellen kopplar begrepp till praktiska frågor och bör fungera som förebild för fler grundfunktionskapitel.

### Problem

Även här finns samma trestegsmönster:

- `Praktiskt test: icke-blockerande LED-fade`
- `Prova själv`
- `Kontrollera att du hänger med`

Det praktiska testet är motiverat, men det innehåller en målsektion:

> Efter experimentet ska du ha:

Den formuleringen är mildare än "ska du kunna", men den ligger fortfarande nära kurs-/labbinstruktion. I en handbok vore det bättre att rama in avsnittet som ett minimalt återanvändbart testfall:

> Det här testet visar att PWM, `millis()` och seriell loggning kan köras utan att blockera varandra.

`Prova själv` är ganska omfattande och innehåller fyra test. Vissa är mycket bra som handbokstillägg, särskilt `Jämför PWM på två kort`, eftersom det tränar läsaren i portabilitet. Men formen bör vara valfri och praktisk, inte uppgiftslik.

`Kontrollera att du hänger med` bör ersättas. Frågorna om PWM, duty cycle, `delay()`, rollover och DAC är värdefulla, men de bör hellre placeras under `Vanliga missförstånd`, `Kontrollera i ditt projekt` eller `Snabb felsökningskontroll`.

### Rekommendation inför PLAN-H

- Behåll kapitlets praktiska test, eftersom icke-blockerande kod behöver visas konkret.
- Byt `Praktiskt test` till `Minsta fungerande test: PWM utan delay`.
- Gör `Prova själv` till `Varianter att prova vid behov`.
- Ersätt kontrollfrågor med `Vanliga missförstånd om PWM och tid`.
- Behåll `Snabbreferens` som positiv mall.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg |

## Kapitel 08 – Avbrott, watchdog och robust körning

### Det fungerar väl

Kapitel 8 har redan en betydligt mer handboksnära inledning än kapitel 6 och 7. Det börjar med konkret användning:

> Använd det när ett projekt missar snabba signaler, fastnar i väntan, behöver säkra standardlägen eller måste kunna återhämta sig efter låsningar.

Detta är exakt den typ av formulering som passar boken. Den fokuserar på situationer där kapitlet behövs, inte på vad läsaren ska examineras på.

Kapitlet gör också ett bra redaktionellt val genom att börja med `Polling först`. Det ger praktiskt beslutsstöd och motverkar ett vanligt nybörjarmisstag: att använda interrupt för snabbt eller för ofta.

Avsnitten om ISR-begränsningar, `volatile`, timeouts, säkra standardlägen, watchdog och brownout har stark handbokskänsla. De hjälper läsaren undvika svårfelsökta problem.

### Problem

Trots den starka handboksramen finns läroboksspår i experimentdelen:

> Efter experimentet ska du kunna:

Det gör att ett annars praktiskt avsnitt låter som kursmål. Det borde ersättas med något i stil med:

> Testet ger dig ett jämförbart mönster för att se när polling räcker och när interrupt är motiverat.

`Prova själv` innehåller flera bra scenarier, men rubriken och uppgiftsformen gör att de låter som övningar. Särskilt `Avbrott eller polling?` är egentligen ett utmärkt beslutsstöd och bör kanske flyttas eller omformas till `Välj polling eller interrupt`.

Kapitel 8 saknar `Kontrollera att du hänger med`, vilket är positivt. Det visar att kapitlet redan har börjat röra sig mot handboksformat.

### Rekommendation inför PLAN-H

- Använd kapitel 8 som positiv modell för handboksinledning.
- Byt experimentets målformulering.
- Omforma `Prova själv` till beslutsstöd och robusthetschecklista.
- Behåll testet, men gör det tydligare som valideringsmönster snarare än labbuppgift.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 4,5/5 |
| Läroboksspår | Låg–medel |
| Behov av redaktionell åtgärd | Låg–medel |
| Risk vid ändring | Låg |

## Kapitel 09 – Kommunikation: UART, I2C, SPI och 1-Wire

### Det fungerar väl

Kapitlet är omfattande men mycket användbart. Det fungerar både som orientering och praktiskt beslutsstöd. Det förklarar inte bara vad UART, I2C, SPI och 1-Wire är, utan hjälper läsaren välja buss, förstå felmoder och felsöka.

Formuleringen i inledningen är i grunden bra:

> Målet med kapitlet är inte att du ska memorera varje elektrisk detalj. Målet är att du ska kunna välja rätt buss, koppla den rimligt säkert, känna igen vanliga fel och skriva testkod som snabbt visar om problemet ligger i mjukvara, bibliotek, koppling eller komponentval.

Den tydliggör att kapitlet är praktiskt. Samtidigt innehåller den "Målet med kapitlet" och "ska kunna", vilket är just den typ av formulering som bör mildras i PLAN-H. Innehållet bör behållas men uttryckas mer som användningsnytta.

`Snabb jämförelse`, `Felsökningsmetod`, `Vanliga misstag` och `Snabbreferens` fungerar mycket bra. De är typiska handbokssektioner.

### Problem

Kapitlet har två `Praktiskt test`-sektioner:

- `Praktiskt test: två I2C-enheter på samma buss`
- `Praktiskt test: UART-loopback`

Båda är relevanta, men två praktiska test plus `Prova själv` plus `Kontrollera att du hänger med` gör kapitlet tungt och kurslikt. För ett kapitel på över 5500 ord kan detta upplevas som en hel workshop.

Det andra problemet är att `Prova själv` i detta kapitel nästan är en egen metodsektion. `Skapa en personlig bussguide`, `Byt buss, behåll funktion` och `Dokumentera ett fel` är bra aktiviteter, men de passar bättre som valfria arbetsmönster eller checklistor än som övningsuppgifter.

`Kontrollera att du hänger med` bör ersättas. Frågorna är ämnesmässigt bra, men rubriken och numrerad provfrågeform förstärker lärobokskänslan.

### Rekommendation inför PLAN-H

- Behåll I2C-testet som huvudsakligt praktiskt test, eftersom det visar adresser, pullups och gemensam buss.
- Gör UART-loopback till en kort `Minimal kontroll: UART-loopback`, inte ett lika stort praktiskt test.
- Omforma `Prova själv` till `Bygg din egen bussreferens` eller `Fördjupa vid behov`.
- Ersätt kontrollfrågorna med `Vanliga missförstånd om bussar` och `Kontrollera vid felsökning`.
- Mjukgör "Målet med kapitlet..." till en användningsorienterad formulering.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Medel |

## Kapitel 10 – Klassiska Arduino-kort: UNO, Nano och Mega

### Det fungerar väl

Kapitel 10 markerar övergången från grundfunktioner till kort- och plattformsval. Det är en bra övergång. Kapitlet är tydligt praktiskt: det hjälper läsaren bedöma när klassiska kort fortfarande är bra och när moderna alternativ är bättre.

Rubriker som `Bedöm kortet med detta i åtanke`, `När klassiska kort är rätt val`, `När du bör välja något annat`, `Felsökning`, `Vanliga misstag`, `Sammanfattande valbild`, `Kontrollera ditt val` och `Snabbval` passar handboksidentiteten bättre än traditionella lärandemål.

`Snabbval` är en stark sektion. Den sammanfattar kortets styrkor, begränsningar, vanliga fel och alternativ.

### Problem

Kapitlet har ändå ett `Praktiskt test: portera samma sensorprojekt mellan UNO, Nano och Mega`. Testet är relevant för portabilitet, men det kräver tillgång till flera kort och kan därför kännas mer som en workshop än som nödvändig handboksläsning.

Här finns en viktig skillnad mot kapitel 6–9: detta är ett kortvalskapitel, inte ett grundfunktionskapitel. För kortvalskapitel bör praktiska test vara valfria eller formuleras som `Portabilitetskontroll` snarare än som experiment.

`Kontrollera ditt val` fungerar bättre än `Kontrollera att du hänger med`, eftersom rubriken är kopplad till beslut snarare än kunskapskontroll. Den bör därför inte tas bort generellt. Däremot bör frågorna kanske omvandlas till checklista med praktiska beslutspunkter.

### Rekommendation inför PLAN-H

- Behåll kapitlets beslutsstöd och snabbval.
- Omforma praktiskt test till `Portabilitetskontroll` eller `Testa om projektet är UNO/Nano/Mega-portabelt`.
- Behåll `Kontrollera ditt val`, men gör den mer checklistelik.
- Använd kapitel 10 som positiv mall för kommande kortkapitel: jämförelse, valbild, vanliga misstag och snabbval.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 4,5/5 |
| Läroboksspår | Låg–medel |
| Behov av redaktionell åtgärd | Låg–medel |
| Risk vid ändring | Låg |

## Återkommande mönster i kapitel 06–10

### 1. Grundfunktionskapitlen behöver praktik, men inte kursram

Kapitel 6–9 bör inte tömmas på praktiska test. De behandlar funktioner som blir begripliga först när läsaren ser dem i kod eller koppling:

- analog mätning behöver råvärde, filtrering och kalibrering,
- PWM behöver upplevd effekt och timing,
- interrupt behöver jämföras med polling,
- kommunikation behöver minimal testkod.

Däremot bör testavsnitten formuleras som handboksnära valideringar, inte labbar.

### 2. `Det du kan använda kapitlet till` är bättre än lärandemål, men bör varieras

Formuleringen fungerar bättre än "Efter kapitlet ska du kunna", men när den återkommer i kapitel 6, 7 och 9 blir den mönsterartad. PLAN-H bör ge alternativ som:

- `Använd kapitlet när...`
- `Det här kapitlet hjälper när...`
- `Du får framför allt stöd för att...`
- `Här får du praktiska riktlinjer för...`

### 3. `Praktiskt test` och `Prova själv` överlappar

Kapitel 6, 7, 8 och 9 har båda. Detta är inte alltid fel, men sektionerna behöver tydligare funktion:

- Ett huvudtest bör visa minsta fungerande mönster.
- Varianter bör vara tydligt valfria.
- Teorifrågor bör inte ligga under praktiska rubriker.
- Om kapitlet redan har ett långt test bör `Prova själv` kortas eller göras till checklista.

### 4. Kontrollfrågor bör inte ligga kvar som quiz

Kapitel 6, 7 och 9 har `Kontrollera att du hänger med`. Kapitel 10 har `Kontrollera ditt val`.

Skillnaden är viktig:

- `Kontrollera att du hänger med` låter som prov.
- `Kontrollera ditt val` låter som beslutsstöd.

PLAN-H bör därför inte radera alla kontrollsektioner. Den bör omvandla dem utifrån kapiteltyp.

### 5. Kapitel 8 och 10 är positiva modeller

Kapitel 8 fungerar väl som robusthetsorienterat grundfunktionskapitel. Det börjar med användningssituationer och prioriterar val mellan polling, interrupt, timeouts och watchdog.

Kapitel 10 fungerar väl som kortvalskapitel. Det har tydligt beslutsstöd, valbild och snabbval.

Dessa två kapitel bör användas som stilreferenser i PLAN-H.

## Förslag till generella PLAN-H-regler från steg 3

### Regel H-06: Grundfunktionskapitel får ha praktiska test, men bara med tydlig handboksfunktion

Ett praktiskt test i kapitel 5–9 bör vara ett minimalt, återanvändbart valideringsmönster. Rubriken bör signalera praktisk kontroll, inte labb.

Rekommenderade rubriker:

- `Minsta fungerande test`
- `Testa i praktiken`
- `Validera kopplingen`
- `Kontrollera funktionen`
- `Praktiskt mönster`

### Regel H-07: `Prova själv` bör göras valfritt och kapiteltypanpassat

`Prova själv` bör inte användas mekaniskt. Möjliga ersättningar:

- `Varianter att prova`
- `Bygg vidare vid behov`
- `Fördjupa när projektet kräver det`
- `Kontrollera i ditt projekt`
- `Felsökningsscenarier`

### Regel H-08: Quizrubriker ska ersättas, men innehållet kan ofta återanvändas

`Kontrollera att du hänger med` bör normalt ersättas med:

- `Vanliga missförstånd`
- `Snabb självkontroll`
- `Kontrollera i ditt projekt`
- `Felsökningsfrågor`
- `Beslutsfrågor`

Frågor som är direkt kopplade till val, felsökning eller risk kan behållas i omarbetad form.

### Regel H-09: Kortvalskapitel bör prioritera beslut framför experiment

Kapitel 10–16 bör inte ha praktiska test som huvudstruktur om de egentligen handlar om plattformsval. De bör i stället ha:

- jämförelser,
- valfrågor,
- risker,
- begränsningar,
- portabilitetskontroller,
- snabbval.

### Regel H-10: Målformuleringar bör skrivas om till användningsnytta

Formuleringar som innehåller `Målet med kapitlet är...`, `ska du kunna` eller `Efter experimentet ska du...` bör skrivas om till formuleringar som säger när och hur läsaren använder avsnittet.

Exempel:

| Mindre lämpligt | Mer handboksnära |
|---|---|
| Efter experimentet ska du kunna... | Testet ger ett mönster för att... |
| Målet med kapitlet är att du ska kunna... | Använd kapitlet när du behöver... |
| Kapitlet hjälper dig att förklara... | Kapitlet ger praktiskt stöd för att... |

## Prioriterade åtgärder för PLAN-H från detta block

| Prioritet | Åtgärd | Berörda kapitel | Effekt |
|---|---|---|---|
| Hög | Ersätt `Kontrollera att du hänger med` med handboksformat | 06, 07, 09 | Minskar prov-/lärobokskänsla. |
| Hög | Omforma `Praktiskt test` till `Minsta fungerande test` eller motsvarande | 06–10 | Gör praktiken mer handboksnära. |
| Medel | Slå ihop eller nedtona `Prova själv` där den överlappar praktiskt test | 06–09 | Minskar mekanisk kapitelmall och uppgiftskänsla. |
| Medel | Mjukgör mål- och kravformuleringar | 07, 08, 09 | Gör tonen mindre examinerande. |
| Medel | Gör kapitel 10:s praktiska test till portabilitetskontroll | 10 | Anpassar kortkapitel till beslutsstöd. |
| Låg | Använd `Snabbreferens` och `Snabbval` som positiv mall | 07, 08, 09, 10 | Stärker handbokskänsla i kommande redigering. |

## Samlad bedömning av blocket

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg–medel |

Kapitel 6–10 är innehållsmässigt starka och bör inte skrivas om i grunden. PLAN-H bör huvudsakligen ändra ramar, rubriker och avsnittens funktion. Den viktigaste principen är att behålla praktiken men ta bort känslan av kursmoment och quiz.

## Slutsats

Steg 3 bekräftar mönstret från steg 2, men med en viktig nyansering: i grundfunktionskapitlen är praktiska test ofta nödvändiga. Problemet är inte praktiken i sig, utan hur den är redaktionellt paketerad.

För `[PLAN-H]` bör kapitel 6–9 därför få en särskild regelgrupp för grundfunktionskapitel: de får ha praktiska test, men dessa ska vara minimala, återanvändbara och kopplade till felsökning eller validering. Kapitel 10 visar samtidigt att kort- och plattformskapitel bör styras mer av jämförelser, portabilitet och beslut än av experiment.
