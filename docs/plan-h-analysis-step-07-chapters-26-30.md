# [ANALYSPLAN] steg 7 – Kapitel 26–30

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1–6 genomförda  
Status: Genomförd  
Resultattyp: Redaktionell analys. Inga kapitel eller bokmanus har ändrats.

## Omfattning

Detta steg analyserar kapitel 26–30 enligt projektets kapitelordning:

| Nr | Fil | Kapiteltyp enligt steg 1 | Funktion i boken |
|---:|---|---|---|
| 26 | `chapters/rorelse-orientering-26.md` | Praktisk komponent / sensor | Hjälpa läsaren välja mellan tilt, vibration, accelerometer, gyro, magnetometer och IMU. |
| 27 | `chapters/ljud-mikrofoner-27.md` | Praktisk komponent / sensor | Hjälpa läsaren använda ljudsensorer, mikrofonmoduler och enkla ljudhändelser utan att övertolka mätvärden. |
| 28 | `chapters/strom-spanning-energi-28.md` | Robusthet / mätning / säkerhet | Hjälpa läsaren mäta spänning, ström, effekt, energi och batteristatus på säker nivå. |
| 29 | `chapters/position-tid-identitet-29.md` | Systemfunktion / metod / komponent | Hjälpa läsaren välja lösningar för position, tid, identifiering och händelseloggar. |
| 30 | `chapters/io-expansion-30.md` | Praktisk komponent / systemarkitektur | Hjälpa läsaren välja och felsöka I/O-expansion, shift registers, multiplexers och I2C-expanders. |

Blocket är särskilt viktigt eftersom det ligger i övergången mellan sensorhandbok, systemfunktioner och mer arkitektoniska byggblock. Kapitel 26–27 fortsätter sensorlinjen från kapitel 23–25, kapitel 28 skiftar mot mätning och säkerhet, kapitel 29 mot systemdesign och kapitel 30 mot strukturerad utbyggnad av mikrokontrollerns I/O.

## Snabb kvantitativ översikt

| Kapitel | Ord | H2 | H3 | Kodblock | `Det du kan använda kapitlet till` | `Praktiskt test` | `Prova vidare` | Kontrollsektion | `Valguide` | `Snabbval` | Felsökning |
|---:|---:|---:|---:|---:|---|---|---|---|---|---|---|
| 26 | 3121 | 24 | 13 | 4 | Ja | Ja | Ja | Nej | Ja | Ja | Nej |
| 27 | 3828 | 24 | 13 | 8 | Ja | Ja | Ja | Ja: `Kontrollera ditt val` | Nej | Ja | Nej |
| 28 | 4342 | 30 | 14 | 20 | Ja | Ja | Ja | Ja: `Kontrollera ditt val` | Ja | Ja | Nej, men säkerhetsruta |
| 29 | 4183 | 20 | 29 | 11 | Ja | Ja | Ja | Ja: `Kontrollera ditt val` | Ja | Ja | Nej |
| 30 | 5590 | 28 | 29 | 15 | Ja | Ja, två förekomster | Ja | Ja: `Kontrollera ditt val` | Nej | Ja | Ja |

Tolkning: kapitel 26–30 är praktiskt starka och rika på användbar problemlösning. Blocket har mindre ren quizkänsla än de tidiga teorikapitlen, men fortfarande tydliga läroboksspår i formuleringen `Efter kapitlet ska du kunna` och i flera `Prova vidare`-avsnitt som fungerar mer som uppgifter än som handboksstöd. Kapitel 30 är det mest handboksnära i blocket tack vare ett tydligt felsökningsavsnitt.

## Övergripande slutsats

Kapitel 26–30 fungerar innehållsmässigt väl i en praktisk Arduino-handbok. De behandlar verkliga situationer där läsaren behöver välja sensor, förstå begränsningar, validera mätdata, undvika övertolkning och bygga system som inte bara blinkar utan tolkar omvärlden. Särskilt kapitel 28 och 30 har hög handboksnytta eftersom de hjälper läsaren undvika fel som annars leder till trasig hårdvara, instabila mätningar eller svår felsökning.

Samtidigt visar blocket tydligt varför `[PLAN-H]` behövs. Den faktiska substansen är ofta handboksmässig, men rubriker och avsnittstitlar drar fortfarande texten mot kursbok. Mönstret `Efter kapitlet ska du kunna`, `Praktiskt test`, `Prova vidare` och `Kontrollera ditt val` återkommer även när innehållet egentligen borde paketeras som valguide, referensmönster, verifiering, riskkontroll eller felsökningschecklista.

## Kapitelvis analys

## Kapitel 26 – Rörelse, orientering och vibration

### Styrkor

Kapitlet har en tydlig praktisk funktion: det hjälper läsaren skilja mellan olika rörelse- och orienteringssensorer som ofta blandas ihop. Inledningen är handboksnära eftersom den tidigt korrigerar vanliga missförstånd:

- accelerometer är inte position
- gyro är inte absolut riktning
- magnetometer påverkas av omgivningen
- vibrationssensor säger att något skakade, inte varför

Det är exakt den typ av förklarande begränsning som en praktisk handbok bör innehålla.

Kapitlet har också en bra valstruktur. `Valguide`, `Snabb överblick` och `Snabbval` stödjer läsaren som vill välja komponent utan att läsa kapitlet som kurs. Avsnittet `Vanliga misstag` är särskilt relevant i ett sensorområde där feltolkningar är vanliga.

### Läroboksspår

Kapitlet använder formuleringen:

> Efter kapitlet ska du kunna:

Den efterföljande listan är innehållsmässigt bra, men tonen är kravställande. För en handbok vore det bättre att formulera samma material som användningsnytta, till exempel:

> Kapitlet hjälper dig att känna igen när du behöver tilt, vibration, accelerometer, gyro, magnetometer eller IMU – och vilka felkällor som brukar avgöra valet.

`Praktiskt test: lutnings- och skakindikator` är motiverat, men rubriken `Praktiskt test` gör att texten känns som en laboration. Eftersom testet faktiskt visar ett återanvändbart mönster bör det i `[PLAN-H]` snarare klassas som `Referensmönster: lutning och skakning` eller `Verifiera rörelsedata`.

`Prova vidare` innehåller flera bra idéer men är uppgiftsliknande. I en handbok bör de delas upp i mer problemorienterade rubriker, exempelvis `Bygg vidare när...`, `Jämför sensortyper` eller `Dokumentera sensorprofil`.

### Rekommendation för PLAN-H

- Ersätt lärandemålsformuleringen med en användningsorienterad introduktion.
- Behåll praktiken, men byt `Praktiskt test` till `Referensmönster` eller `Verifiera rörelsesensorn`.
- Gör `Prova vidare` till praktiska vidareval snarare än testuppgifter.
- Överväg att införa begreppet `sensorprofil` även här, eftersom kapitlet redan handlar om axlar, mätområde, uppdateringshastighet och felkällor.

## Kapitel 27 – Ljud, mikrofoner och enkla signalmätningar

### Styrkor

Kapitlet har hög handboksnytta eftersom det tidigt sätter rätt förväntningar. Det gör tydligt att billiga ljudsensorer ofta kan upptäcka ljudhändelser men sällan mäta verkliga decibelnivåer eller identifiera ljud. Det är en viktig praktisk varning.

Kapitlet blev också tydligt stärkt av PLAN5 genom att KY-037 och vanliga ljudsensormoduler får en mer konkret roll. Det passar bokens uppslagskaraktär eftersom många läsare faktiskt har denna typ av modul i Arduino-kit.

Det praktiska testet om ljudstyrd statusindikator är relevant. Det visar tidsfönster, peak-to-peak, tröskel, indikator och vidare förbättring. Innehållet är inte ett onödigt teoriexperiment utan ett realistiskt minimum för att undvika fladdrande ljudtriggers.

### Läroboksspår

Även här finns:

> Efter kapitlet ska du kunna:

Listan är bra, men bör omvandlas till handboksnytta. Exempel:

> Kapitlet hjälper dig att välja mellan enkel ljudtrigger, analog mikrofonmodul och digital mikrofon – och att undvika vanliga feltolkningar kring brus, trösklar och decibel.

`Prova vidare` innehåller praktiska delar som egentligen är dokumentations- och stabiliseringsmönster. `Test 1: Skapa en ljudprofil` är till exempel mycket handboksrelevant, men ordet `Test` får det att kännas mer som uppgift än som arbetsmetod.

`Kontrollera ditt val` består av frågor. Flera frågor är användbara, men de bör bli checklista eller varningsruta:

- `Tolka inte råvärdet som decibel`
- `Använd tidsfönster, inte enskilda samples`
- `Se upp för egen buzzer nära mikrofon`
- `Välj I2S först när projektet behöver råare ljuddata och kortet orkar`

### Rekommendation för PLAN-H

- Behåll ljudkapitlets varningsnivå och praktiska realism.
- Byt `Praktiskt test` till `Referensmönster: stabil ljudindikator`.
- Byt `Test 1: Skapa en ljudprofil` till `Dokumentera ljudprofilen`.
- Omvandla `Kontrollera ditt val` till `Valchecklista för ljudmätning` eller `Snabb kontroll före koppling`.
- Lägg gärna till en kort felsökningschecklista eftersom ljudmätning är brus- och miljökänsligt.

## Kapitel 28 – Ström, spänning, energi och batterimätning

### Styrkor

Detta är ett av blockets viktigaste kapitel för praktisk robusthet. Kapitlet hjälper läsaren skilja mellan spänning, ström, effekt, energi och batteristatus. Det gör också något mycket handboksnära: det sätter gränser för vad man får och inte får mäta med Arduino-experimentkopplingar.

Avsnitt som spänningsdelare, ADC-upplösning, batterispänning kontra batteriprocent, shuntmätning, digitala strömsensorer och strömtoppar har tydlig praktisk funktion. Säkerhetsrutan om att inte mäta okända eller farliga spänningar direkt bör absolut bevaras och gärna förstärkas visuellt i senare redigering.

Kapitlet har även starka `Vanliga misstag`, bland annat direktkoppling av okänd spänning, gemensam jord, batteriprocent och fel mätmetod för ström.

### Läroboksspår och intern artefakt

Formuleringen `Efter kapitlet ska du kunna` återkommer och bör ersättas av en mjukare handboksformulering.

`Praktiskt test: batteri- och lastmonitor` är innehållsmässigt motiverat men har kursliknande moment som `Du ska träna på att`. I en handbok bör detta bli:

- `Referensmönster: säker batterimätning`
- `Verifiera: spänningsdelare och lastpåverkan`
- `Dokumentera mätområdet innan koppling`

Kapitlet innehåller också en internliknande formulering:

> dokumentera exakt metod i projektets canon eller README

`canon` är ett internt arbetsbegrepp i bokprojektet och bör inte förekomma i läsartexten. Även `README` kan kännas som utvecklarartefakt om det inte är tydligt att det syftar på läsarens eget projekt. För läsarversionen bör detta ersättas med något i stil med:

> dokumentera exakt metod i projektets tekniska anteckningar eller kopplingsdokumentation

Detta är en viktig observation inför `[PLAN-H]` eftersom tidigare steg också identifierade interna filreferenser i inledningen.

### Rekommendation för PLAN-H

- Ersätt `Efter kapitlet ska du kunna` med handboksnytta.
- Byt `Praktiskt test` till `Referensmönster: säker batteri- och lastmätning`.
- Ta bort eller omformulera `canon` i läsartexten.
- Behåll säkerhetsrutan, men gör den till en tydligt prioriterad handboksruta.
- Omvandla `Kontrollera ditt val` till `Säkerhets- och valchecklista`.
- Var extra försiktig så att redigering inte försvagar säkerhetsbudskapet.

## Kapitel 29 – Position, tid och identitet

### Styrkor

Kapitlet är handboksmässigt starkt eftersom det utgår från systembehov snarare än en enskild komponent. Det svarar på tre praktiska frågor: var, när och vem. Det gör kapitlet mer moget än ett rent komponentkapitel.

Särskilt bra är avsnitten som förklarar när GNSS är rätt eller fel val, när RTC behövs, när nätverkstid passar, och varför RFID-UID inte är samma sak som säker autentisering. Detta är tydligt beslutsstöd.

Det praktiska testet med tidsstämplad RFID- eller knapphändelse är också relevant eftersom det visar ett systemmönster: händelse, tid, nod-ID, feedback och loggrad. Det är mer än en övning; det är ett återanvändbart designmönster.

### Läroboksspår

Även här används `Efter kapitlet ska du kunna`. Innehållet bör göras om till en handboksnära introduktion:

> Kapitlet hjälper dig att välja mellan GNSS, RTC, nätverkstid, RFID/NFC och enklare ID-lösningar när ett projekt behöver veta var, när eller vilken enhet som är inblandad.

`Prova vidare` innehåller flera mycket bra arbetsmoment, men de är skrivna som kursuppgifter. `Test 1: Välj tidskälla` och `Test 2: Jämför positionslösningar` bör hellre bli handboksformat:

- `Valchecklista: tidskälla`
- `Jämförelse: positionslösningar`
- `Mönster: händelserad`
- `Riskkontroll: RFID är identifiering, inte säker autentisering`

`Kontrollera ditt val` är innehållsmässigt relevant men frågeformen känns skollik. Den kan bli `Beslutspunkter innan du bygger`.

### Rekommendation för PLAN-H

- Behandla kapitlet som `systemfunktion` snarare än sensor- eller komponentkapitel.
- Byt `Praktiskt test` till `Designmönster: tidsstämplad händelse`.
- Omvandla `Prova vidare` till valchecklistor och designmallar.
- Förstärk varningen kring RFID-UID och autentisering som en säkerhets-/begränsningsruta.
- Behåll kopplingen mellan nod-ID, tid och loggning eftersom den är mycket handboksrelevant.

## Kapitel 30 – I/O-expansion, shift registers och multiplexers

### Styrkor

Kapitel 30 är ett av blockets bästa exempel på praktisk handbok. Det börjar med ett konkret problem: pinnarna räcker inte. Därefter jämför det flera lösningar och hjälper läsaren välja mellan shift register, I/O-expander, analog multiplexer och större kort.

PLAN5-tillägget PCF8575 verkar sitta naturligt i strukturen eftersom kapitlet redan behandlar PCF8574 och MCP23017. Den extra 16-bitarsvarianten förstärker referensnyttan utan att kräva ett nytt kapitel.

Kapitlet har också ett explicit `Felsökning`-avsnitt. Detta är ett starkt handboksgrepp som bör återanvändas mer i andra kapitel. Felsökningen är uppdelad efter 74HC595, 74HC165, MCP23017/PCF8574/PCF8575 och analog multiplexer, vilket gör den direkt användbar.

### Läroboksspår

Kapitlet använder `Efter kapitlet ska du kunna`, vilket bör ersättas med en mjukare och mer användningsorienterad formulering.

Det finns två `Praktiskt test`-sektioner:

- `Praktiskt test: åtta LED med 74HC595 och valbar utbyggnad`
- `Praktiskt test: läsa många knappar med MCP23017`

Båda är relevanta, men rubrikerna bör skiljas åt efter funktion. Det första är ett referensmönster för utgångsexpansion, det andra ett referensmönster för ingångsexpansion. I `[PLAN-H]` bör de inte båda heta `Praktiskt test`, eftersom det döljer deras olika roll.

`Prova vidare` är delvis uppgift, delvis beslutsstöd. `Test 1: Välj expansionstyp` är egentligen en valguide. `Test 2: Dokumentera bitmappning` är en dokumentationsmetod. `Test 4: Multiplexer och stabiliseringstid` är en teknisk verifiering.

### Rekommendation för PLAN-H

- Använd kapitel 30 som positiv modell för hur `Felsökning` kan fungera i handboken.
- Byt dubbla `Praktiskt test` till:
  - `Referensmönster: utgångsexpansion med 74HC595`
  - `Referensmönster: många knappar med I2C-expander`
- Omvandla `Prova vidare` till `Valövning`, `Dokumentationsmönster` och `Verifiering`.
- Omvandla `Kontrollera ditt val` till `Valchecklista för I/O-expansion`.
- Bevara och eventuellt lyft fram jämförelsen mellan större kort och extern expansion.

## Återkommande mönster i kapitel 26–30

## 1. Innehållet är mer handbok än rubrikerna antyder

I flera kapitel är själva innehållet praktiskt och moget, men rubrikerna gör att det upplevs mer som kursmaterial. Detta gäller särskilt:

- `Efter kapitlet ska du kunna`
- `Praktiskt test`
- `Prova vidare`
- `Kontrollera ditt val`

Materialet bör i de flesta fall bevaras men paketeras om.

## 2. `Efter kapitlet ska du kunna` finns i alla fem kapitel

Alla fem analyserade kapitel använder samma kravliknande formulering. Det bör bli en generell PLAN-H-regel att denna formulering ersätts i hela boken med mer stödjande och varierade formuleringar.

Rekommenderade ersättningsmönster:

- `Kapitlet hjälper dig att...`
- `Här får du stöd för att välja mellan...`
- `Efter genomgången har du en praktisk bild av...`
- `Målet är att göra det lättare att...`
- `Använd kapitlet när du behöver...`

Viktigt: ersättningarna bör varieras så att boken inte får en ny mekanisk standardfras.

## 3. Praktiska moment är ofta motiverade, men rubriken är för generell

I detta block bör praktiken i regel inte tas bort. Till skillnad från vissa tidiga teorikapitel är praktiska moment här ofta nödvändiga för att förstå sensorbeteende, mätning, loggning eller I/O-expansion.

Däremot bör `Praktiskt test` delas upp efter funktion:

| Nuvarande rubrik | Mer handboksnära funktion |
|---|---|
| `Praktiskt test` för sensor | `Verifiera sensorn` eller `Referensmönster` |
| `Praktiskt test` för mätning | `Säker mätkoppling` eller `Verifiera mätområdet` |
| `Praktiskt test` för systemdesign | `Designmönster` |
| Två praktiska test i samma kapitel | Skilj på `utgångsmönster`, `ingångsmönster`, `felsökning` eller `utbyggnad` |

## 4. `Prova vidare` är ofta bra material men fel inramat

I kapitel 26–30 är `Prova vidare` sällan onödigt. Däremot är formen ofta mer kursövning än handbok. Många `Test`-rubriker kan bli:

- `Dokumentera...`
- `Jämför...`
- `Välj...`
- `Verifiera...`
- `Bygg vidare när...`
- `Riskkontroll...`

## 5. Kontrollfrågor bör bli checklistor, inte quiz

`Kontrollera ditt val` är bättre än `Kontrollera att du hänger med`, men frågeformen drar fortfarande mot lärobok. I detta block bör kontrollsektionerna bli:

- valchecklista
- säkerhetschecklista
- felsökningsordning
- beslutspunkter innan koppling
- vanliga feltolkningar

## 6. Kapitel 30 visar värdet av riktig felsökning

Kapitel 30 har ett tydligt `Felsökning`-avsnitt och fungerar därmed som modell för andra tekniskt praktiska kapitel. Felsökningsformatet är mer handboksnära än quiz och bör återanvändas särskilt i kapitel där läsaren sannolikt fastnar på koppling, adress, matning, logiknivå, brus, timing eller bibliotek.

## 7. Interna artefakter förekommer mindre men finns fortfarande

I kapitel 28 finns formuleringen `projektets canon eller README`. `canon` bör tas bort ur läsartexten. Om `README` används bör det antingen syfta tydligt på läsarens eget projekt eller ersättas med `projektdokumentation`.

Detta bekräftar att `[PLAN-H]` bör innehålla ett separat steg för att söka igenom hela bokmanuset efter interna arbetsbegrepp.

## Handbokskänsla per kapitel

| Kapitel | Handbokskänsla | Läroboksspår | Behov av åtgärd | Risk vid ändring | Kommentar |
|---:|---:|---|---|---|---|
| 26 | 4/5 | Medel | Medel | Låg | Bra sensorval och missförstånd, men praktiken bör rubriceras om. |
| 27 | 4/5 | Medel | Medel | Låg–medel | Starkt praktiskt innehåll; bör få valchecklista och eventuellt felsökning. |
| 28 | 4/5 | Medel | Medel–hög | Medel | Viktigt säkerhetskapitel; redigering måste bevara varningar och gränser. |
| 29 | 4/5 | Medel | Medel | Låg–medel | Bra systemkapitel; bör omformas till designmönster och beslutspunkter. |
| 30 | 4,5/5 | Låg–medel | Medel | Låg | Mycket handboksnära, särskilt felsökningen. Rubriker behöver normaliseras. |

## Föreslagna PLAN-H-regler från steg 7

## Regel H-7.1: Byt lärandemål mot användningsnytta

Alla förekomster av `Efter kapitlet ska du kunna` i kapitel 26–30 bör ersättas av användningsorienterade formuleringar. Regeln bör sannolikt gälla hela boken.

## Regel H-7.2: Behåll praktiska moment i sensor-, mät- och expansionskapitel

Till skillnad från tidiga teorikapitel bör praktiska moment här normalt behållas. De bör däremot byta namn och funktion:

- sensor → `Verifiera sensorn`
- mätning → `Säker mätkoppling` eller `Verifiera mätområdet`
- systemfunktion → `Designmönster`
- I/O-expansion → `Referensmönster`

## Regel H-7.3: Gör `Prova vidare` till arbetsmönster

`Prova vidare` bör inte tas bort generellt. I kapitel 26–30 bör det omformas till dokumentations-, jämförelse-, verifierings- och beslutsmönster.

## Regel H-7.4: Ersätt frågebaserade kontrollavsnitt med checklistor

`Kontrollera ditt val` bör i detta block ersättas av:

- `Valchecklista`
- `Säkerhetschecklista`
- `Beslutspunkter`
- `Felsökningsordning`
- `Vanliga feltolkningar`

## Regel H-7.5: Sök och ta bort interna arbetsbegrepp i hela bokmanuset

Utöver tidigare identifierad `docs/lookup-index.md` finns nu även `canon` i läsartext. `[PLAN-H]` bör innehålla en global sökning efter interna projektartefakter och ersätta dem med läsarnära uttryck.

## Regel H-7.6: Använd kapitel 30:s felsökningsformat som positiv modell

Kapitel 30 visar ett praktiskt sätt att felsöka lager för lager. Detta format bör användas som modell i fler kapitel där fel uppstår genom koppling, adress, matning, timing, nivåer eller bibliotek.

## Prioriterade observationer att föra vidare till tväranalysen

1. Alla fem kapitel har samma kravformulering `Efter kapitlet ska du kunna`.
2. Praktiska moment är i detta block oftast motiverade, men behöver mer handboksnära rubriker.
3. `Kontrollera ditt val` bör inte bli quiz; det bör bli checklista eller felsökning.
4. Kapitel 28 innehåller `canon`, vilket bekräftar behovet av global sanering av interna arbetsord.
5. Kapitel 30 är ett positivt exempel på felsökningsstruktur.
6. Sensorprofil, dokumentation av mätområde, felkällor och verifiering bör bli återkommande handboksgrepp.
7. Systemkapitel som 29 bör behandlas som designmönster, inte som komponentövning.

## Slutsats för steg 7

Kapitel 26–30 stärker boken som praktisk handbok. De är inte huvudsakligen problematiska kapitel; tvärtom innehåller de mycket av den typ av beslutsstöd, begränsningar, varningar och felsökning som boken bör bygga vidare på. Det redaktionella problemet är främst att de fortfarande använder samma skolnära yttre struktur som många tidigare kapitel.

Den viktigaste slutsatsen är därför att `[PLAN-H]` inte bör rensa bort praktiska moment i detta block. Den bör i stället omklassificera dem. Här ska `Praktiskt test` oftast bli referensmönster, verifiering, säker mätkoppling eller designmönster. `Prova vidare` ska bli arbetsmönster och dokumentationsstöd. `Kontrollera ditt val` ska bli checklista, riskkontroll eller felsökningsordning.

Detta block visar också att boken nu har tillräckligt innehållsmässigt djup. Nästa kvalitetslyft bör därför inte vara fler komponenter utan ett konsekvent redaktionellt lager som gör varje kapiteltyp tydligare och mer handboksnära.
