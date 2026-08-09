# [ANALYSPLAN] steg 6 – Kapitel 21–25

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1–5 genomförda  
Status: Genomförd  
Resultattyp: Redaktionell analys. Inga kapitel eller bokmanus har ändrats.

## Omfattning

Detta steg analyserar kapitel 21–25 enligt projektets kapitelordning:

| Nr | Fil | Kapiteltyp enligt steg 1 | Funktion i boken |
|---:|---|---|---|
| 21 | `chapters/relaer-mosfetar-laster-21.md` | Praktisk komponent / robusthet och säkerhet | Hjälpa läsaren styra laster med relä, MOSFET, drivsteg och skydd för induktiva laster. |
| 22 | `chapters/displayer-anvandargranssnitt-22.md` | Praktisk komponent / användargränssnitt | Hjälpa läsaren välja display, inmatning och enkel UI-struktur för fristående projekt. |
| 23 | `chapters/miljosensorer-23.md` | Praktisk komponent / sensor | Hjälpa läsaren välja och använda temperatur-, fukt-, tryck- och miljösensorer robust. |
| 24 | `chapters/ljus-farg-optiska-sensorer-24.md` | Praktisk komponent / sensor | Hjälpa läsaren välja och använda ljus-, färg-, UV- och optiska sensorer. |
| 25 | `chapters/avstand-narvaro-25.md` | Praktisk komponent / sensor | Hjälpa läsaren välja mellan avståndsmätning, närvaro och objektupptäckt. |

Analysen har läst faktisk kapiteltext och fokuserar särskilt på hur senare komponentkapitel använder praktiska tester, valguider, sensorprofiler, felsökning och kontrollsektioner. Blocket är viktigt eftersom det visar hur boken fungerar när den lämnar grundläggande komponenter och går in i mer användningsnära systemdelar.

## Snabb kvantitativ översikt

| Kapitel | Ord | H2 | H3 | Kodblock | `Det du kan använda kapitlet till` | `Praktiskt test` | `Prova vidare` | Kontrollsektion | `Valguide` | `Snabbval` |
|---:|---:|---:|---:|---:|---|---|---|---|---|---|
| 21 | 4169 | 26 | 13 | 3 | Ja | Ja, tre förekomster | Nej | Ja: `Kontrollera ditt val` | Nej | Ja |
| 22 | 5545 | 32 | 10 | 8 | Ja | Ja, två förekomster | Nej | Ja: `Kontrollera ditt val` | Nej | Ja |
| 23 | 5476 | 28 | 14 | 4 | Ja | Ja | Ja | Ja: `Kontrollera ditt val` | Ja | Ja |
| 24 | 4535 | 32 | 8 | 2 | Ja | Nej | Ja | Ja: `Kontrollera ditt val` | Ja | Ja |
| 25 | 4538 | 31 | 13 | 9 | Ja | Ja | Ja | Ja: `Kontrollera ditt val` | Ja | Ja |

Tolkning: kapitel 21–25 har tydlig handboksnytta och är bland bokens mest praktiskt relevanta block. Samtidigt syns ett återkommande strukturellt mönster: varje kapitel har ett avsnitt med lärandemålsliknande formulering, någon form av praktiskt moment och en kontrollsektion. Det fungerar när ämnet är konkret, men rubrikerna och frågeformen gör fortfarande att texten delvis låter som kursmaterial.

## Övergripande slutsats

Kapitel 21–25 är innehållsmässigt mycket starka. De behandlar sådant som läsaren faktiskt behöver när Arduino-projekt ska bli användbara: laststyrning, lokala gränssnitt, miljömätning, optisk mätning och närvarodetektion. Blocket visar också att boken har blivit mer mogen efter tidigare utvecklingssteg. De nyare tilläggen om solenoider, APDS-9960 och analoga Hall-sensorer ligger redaktionellt rätt och stärker bokens praktiska bredd.

Det viktigaste redaktionella problemet är inte innehållet utan **funktionsnamnen på sektionerna**. Flera kapitel innehåller praktiska delar som är väl motiverade men rubriceras som `Praktiskt test`, `Test 1`, `Test 2` eller `Kontrollera ditt val`. I en handbok bör samma innehåll oftare presenteras som:

- `Minsta fungerande koppling`
- `Verifiera kopplingen`
- `Dokumentera modulen`
- `Sensorprofil`
- `Valchecklista`
- `Felsökning före användning`
- `Jämför alternativ`
- `När den här lösningen inte passar`

Detta block ger därför en viktig regel för `[PLAN-H]`: **praktik ska inte tas bort generellt i komponentkapitel, men den ska byta identitet från övning till arbetsmönster, referensmönster, verifiering eller felsökningsstöd.**

## Kapitel 21 – Reläer, MOSFET:ar, solenoider och andra laster

### Det fungerar väl

Kapitlet har mycket stark handboksidentitet. Det behandlar ett av de vanligaste och viktigaste problemen i Arduino-projekt: att skilja mellan styrsignal och lastström. Det praktiska värdet är högt eftersom kapitlet hjälper läsaren undvika verkliga fel: att driva laster direkt från GPIO, glömma gemensam jord, välja fel MOSFET, missa flyback-diod eller hantera aktiv låg relälogik fel.

Särskilt bra fungerar:

- huvudprincipen att Arduino-pinnen ska styra men inte bära lastström,
- översikten över relä, MOSFET, transistorarray och drivmodul,
- avsnitten om logic-level MOSFET, gate-motstånd och pulldown,
- avsnitten om induktiva laster, flyback-diod och solenoider,
- säkerhetsrutan om att hålla nätspänning utanför experimentkopplingar,
- snabbvalet som hjälper läsaren välja styrprincip.

Detta kapitel är ett positivt exempel på där praktiska moment verkligen hör hemma. Laststyrning måste verifieras praktiskt eftersom små detaljer i matning, jord och skydd påverkar säkerhet och funktion.

### Läroboksspår

Kapitlet har tre `Praktiskt test`-nivåer:

1. `Praktiskt test: styr en lågspänd last med MOSFET`
2. `Praktiskt test: relä med säker vilologik`
3. ett generellt `Praktiskt test` med `Test 1`, `Test 2`, `Test 3` och `Fördjupning`

Det gör att praktiken känns upprepande, trots att innehållet i sig är relevant. De två första praktiska momenten är egentligen referensexempel/verifieringsmönster. Det sista är snarare beslutsövning, dokumentationsstöd och kodmönster.

Formuleringen `Efter kapitlet ska du kunna` förekommer också och bör ersättas med en mer stödjande handboksformulering.

### Rekommendation för PLAN-H

Kapitlet bör inte kortas hårt. Det bör struktureras om så att praktiken får tydligare funktion:

- `Praktiskt test: styr en lågspänd last med MOSFET` bör bli `Minsta fungerande MOSFET-koppling` eller `Verifiera en MOSFET-styrd last`.
- `Praktiskt test: relä med säker vilologik` bör bli `Verifiera relämodulens aktiva nivå och startläge`.
- Det generella `Praktiskt test` bör bli `Arbetsmönster: välj och dokumentera en laststyrning`.
- `Kontrollera ditt val` bör bli `Valchecklista före laststyrning`.

Kapitlet bör dessutom kunna fungera som modell för säkerhetskritiska komponentkapitel: praktiken behålls men skrivs som verifiering, riskkontroll och dokumentation.

## Kapitel 22 – Displayer och enkla användargränssnitt

### Det fungerar väl

Kapitlet är omfattande och relevant. Det behandlar inte bara displaymoduler utan även användargränssnitt som systemdel: displaytyp, inmatning, menystruktur, uppdateringsintervall, bussdelning och minnespåverkan. Det är handboksnära eftersom läsaren ofta behöver välja mellan LCD, OLED, TFT, e-paper, sifferdisplay och LED-matris innan projektet blir fristående.

Särskilt bra fungerar:

- bredden i displayöversikten,
- avsnitten om knappar, encoder, joystick, keypad, touch och IR-fjärr,
- resonemanget om UI-tillstånd,
- varningen för att uppdatera displayen okontrollerat i varje varv av `loop()`,
- felsökningsinriktade delar om I2C-adresser, bussdelning, SPI-pinnkonflikter och minnesfrågan,
- avsnittet om när display inte är rätt lösning.

Kapitlet hjälper läsaren att fatta bättre designbeslut snarare än att bara koppla en display.

### Läroboksspår

Kapitlet är långt och använder både `Praktiskt test: liten mätpanel med OLED och knapp` och ett senare generellt `Praktiskt test` med fem tester. Det senare innehåller bland annat att byta displaytyp på pappret, lägga till statusvy, göra displayuppdateringen smartare, planera ett gränssnitt med rotary encoder och välja rätt inmatning. Det är bra material, men rubriken `Praktiskt test` samlar för många olika funktioner.

`Kontrollera ditt val` är formulerat som quizfrågor. Frågorna är relevanta, men i handboksformat skulle de göra mer nytta som checklista för displayval och UI-design.

### Rekommendation för PLAN-H

Kapitlet bör delas redaktionellt i tydligare funktioner utan att nödvändigtvis delas upp i flera kapitel:

- huvudexemplet bör heta `Referensmönster: liten mätpanel med OLED och knapp`,
- pappersanalysen bör bli `Valchecklista: välj displaytyp`,
- statusvyn och smartare uppdatering bör bli `Förbättra gränssnittet`,
- rotary encoder-delen bör bli `Designmönster: encoderstyrd meny`,
- `Kontrollera ditt val` bör bli `Checklista före displayval`.

Kapitlet bör också granskas för längd i senare PLAN-H. Det är användbart, men riskerar att bli ett av bokens mest täta kapitel. En lösning kan vara att behålla allt men göra rubrikerna mer navigerbara.

## Kapitel 23 – Temperatur, fukt, tryck och miljösensorer

### Det fungerar väl

Kapitlet är ett starkt sensorhandbokskapitel. Det gör rätt sak redaktionellt: det behandlar inte miljösensorer som bara enkla moduler utan som mätproblem. Texten betonar placering, självuppvärmning, uppdateringsintervall, kabelproblem, kalibrering och rimlighetskontroll. Det är precis den typ av material som skiljer en handbok från en lista med kopplingsscheman.

Särskilt bra fungerar:

- distinktionen mellan att få ett värde och att göra en bra mätning,
- jämförelsen mellan DHT, DS18B20, BMP280/BME280, SHT/AHT och luftkvalitetssensorer,
- varningarna kring MQ-gassensorer och säkerhetskritiska tillämpningar,
- valguiden för vanliga miljösensorer,
- sensorprofilen som dokumentationsverktyg,
- avsnitten om placering, fysisk design, filtrering och kalibrering.

Kapitlet har stark handboksidentitet eftersom det hjälper läsaren att undvika feltolkade mätvärden.

### Läroboksspår

`Praktiskt test: miljölogger med jämförelse` är motiverat, men `Prova vidare` innehåller tester som delvis fungerar som övningar. Exempelvis `Gör en sensorprofil`, `Jämför två sensorer` och `Bygg en enkel väderstationsnod` är mycket relevanta, men de bör snarare beskrivas som återanvändbara arbetsmönster.

`Kontrollera ditt val` har tolv frågor. Frågorna är bra men bör inte ligga som quiz. Flera av dem är egentligen riskkontroller: självuppvärmning, sensorval, uppdateringsintervall, I2C-fel, hysteresis, jordfukt och MQ-säkerhet.

### Rekommendation för PLAN-H

Kapitlet bör bevara sin praktiska struktur men ändra rubriklogiken:

- `Praktiskt test: miljölogger med jämförelse` bör bli `Referensmönster: miljölogger med jämförelse`.
- `Prova vidare` bör bli `Arbetsmönster för miljömätning`.
- `Test 1: Gör en sensorprofil` bör bli `Sensorprofil`.
- `Test 2: Jämför två sensorer` bör bli `Jämför och rimlighetskontrollera mätvärden`.
- `Kontrollera ditt val` bör bli `Riskkontroll före miljömätning`.

Detta kapitel bör fungera som modell för sensorprofilformatet i andra sensorkapitel.

## Kapitel 24 – Ljus, färg, UV och optiska sensorer

### Det fungerar väl

Kapitlet har stark handboksnytta och bra ämnesmässig avgränsning. Det gör en viktig distinktion: en ljussensor mäter inte ljus i allmänhet, utan ljus som träffar en viss aktiv yta med viss spektral känslighet och placering. Det är en mycket handboksnära observation eftersom den hjälper läsaren förstå varför enkla experiment ger oväntade resultat.

Särskilt bra fungerar:

- förklaringen av skillnaden mellan LDR, fototransistor, digital luxsensor, färgsensor, UV-sensor och IR-reflektion,
- avsnitten om placering, kapsling, geometri, filtrering och hysteresis,
- tillägget om APDS-9960/GY-9960,
- valguiden,
- dokumentation av optisk sensorprofil,
- felsökning kring mättnad, omgivningsljus, reflexer och egna LED/displaykällor.

Kapitlet har en bättre struktur än flera tidigare komponentkapitel eftersom huvudexemplen är rubricerade som `Exempel` och `Variation` snarare än `Praktiskt test`.

### Läroboksspår

Det finns fortfarande `Efter kapitlet ska du kunna`, `Prova vidare` och `Kontrollera ditt val`. `Prova vidare` är i praktiken en samling bra arbetsmönster men är formulerat som tester. `Kontrollera ditt val` är quizliknande, trots att frågorna är praktiskt relevanta.

### Rekommendation för PLAN-H

Kapitlet kräver mindre strukturell ändring än kapitel 21–23. Det bör främst normaliseras i ton och slutdelar:

- `Det du kan använda kapitlet till` bör skrivas om från kravlista till användningsnytta.
- `Prova vidare` bör bli `Arbetsmönster för optiska sensorer`.
- testerna bör byta namn till `Kartlägg ljusintervall`, `Jämför relativ mätning och luxmätning`, `Bygg en optisk detektor` och `Fördjupning: enkel färgklassificering`.
- `Kontrollera ditt val` bör bli `Checklista före optisk mätning`.

Kapitlets befintliga `Exempel`/`Variation`-struktur bör bevaras som positiv modell.

## Kapitel 25 – Avstånd, närvaro och objektupptäckt

### Det fungerar väl

Kapitlet är ett starkt exempel på praktiskt beslutsstöd. Det börjar med rätt fråga: vad vill projektet egentligen veta? Avstånd, närvaro och passage är inte samma sak. Den distinktionen gör kapitlet mycket handboksnära.

Särskilt bra fungerar:

- uppdelningen mellan avstånd, närvaro och objektupptäckt,
- jämförelsen mellan ultraljud, IR, ToF, PIR, radar/mmWave, reed switch, Hall-sensorer och ljusbarriär,
- avsnittet om att undvika låsning med `pulseIn`,
- avsnitten om hysteresis och tidslogik,
- valguiden,
- sensorprofilen,
- tillägget om analoga Hall-sensorer och 49E-typ.

Kapitlet ger läsaren ett bra beslutsunderlag och bör behålla sin bredd.

### Läroboksspår

Kapitlet har både praktiskt exempel, `Praktiskt test: jämför två närvarotekniker`, `Prova vidare` och `Kontrollera ditt val`. Här är praktiken ofta motiverad, men rubrikerna gör att slutdelen känns som en övningsserie. `Test 2: Jämför PIR och avståndsmätning` är egentligen ett mycket bra valideringsmönster för verkliga projekt och bör presenteras som sådant.

### Rekommendation för PLAN-H

Kapitlet bör redaktionellt renodlas:

- `Praktiskt test: jämför två närvarotekniker` bör bli `Verifiera två närvarotekniker i samma miljö`.
- `Prova vidare` bör bli `Arbetsmönster för avstånd och närvaro`.
- `Test 1: Bygg en närhetsindikator` bör bli `Referensmönster: närhetsindikator`.
- `Test 2: Jämför PIR och avståndsmätning` bör bli `Validera sensorvalet i miljön`.
- `Test 3: Gör en passageräknare` bör bli `Referensmönster: passageräknare`.
- `Kontrollera ditt val` bör bli `Valchecklista för närvaro och objektupptäckt`.

Kapitlet är särskilt viktigt för `[PLAN-H]` eftersom det visar att handboksformatet kan behålla praktiska moment utan att låta som kursuppgifter.

## Återkommande mönster i kapitel 21–25

### 1. `Efter kapitlet ska du kunna` är fortfarande standardformulering

Alla fem kapitel använder en kravliknande formulering i avsnittet `Det du kan använda kapitlet till`. Den fungerar pedagogiskt men inte optimalt för handbokstonen.

För `[PLAN-H]` bör formuleringen ersättas blockvis, inte mekaniskt med samma mening överallt. Exempel:

- `Det här kapitlet hjälper dig att välja och verifiera...`
- `Här får du stöd för att jämföra...`
- `Efter genomgången blir det lättare att känna igen...`
- `Använd kapitlet när du behöver avgöra...`

### 2. Praktik är motiverad men fel rubricerad

I detta block bör praktiska moment i regel behållas. Det gäller särskilt kapitel 21, 22, 23 och 25. Däremot bör `Praktiskt test` nästan aldrig vara en allmän rubrik när flera olika typer av moment blandas.

För `[PLAN-H]` bör praktiken delas efter funktion:

| Nuvarande funktion | Föreslagen handboksfunktion |
|---|---|
| Fullt kopplingsexempel | `Minsta fungerande koppling` eller `Referensmönster` |
| Kontroll av modulbeteende | `Verifiera modulen` |
| Pappersval eller jämförelse | `Valchecklista` eller `Jämför alternativ` |
| Vidare experiment | `Arbetsmönster` eller `Fördjupning` |
| Risk-/säkerhetsfrågor | `Riskkontroll` |
| Felsökningsfrågor | `Felsökningschecklista` |

### 3. `Kontrollera ditt val` är nästan rätt men fortfarande quizlikt

Titeln `Kontrollera ditt val` är bättre än `Kontrollera att du hänger med`, men frågorna är ofta fortfarande formulerade som kunskapskontroll. I detta block bör innehållet ofta bevaras, men göras om till listor som läsaren kan använda före koppling eller komponentval.

Exempel på bättre rubriker:

- `Checklista före laststyrning`
- `Checklista före displayval`
- `Riskkontroll före miljömätning`
- `Checklista före optisk mätning`
- `Valchecklista för närvaro och objektupptäckt`

### 4. Sensorprofiler är ett starkt handboksgrepp

Kapitel 23, 24 och 25 använder idén om sensorprofil eller dokumentation av sensorval. Detta är mycket värdefullt och bör lyftas som generell PLAN-H-regel för sensorkapitel. Det hjälper läsaren dokumentera gränssnitt, matning, logiknivå, mätintervall, placering, felkällor och antaganden.

### 5. Säkerhets- och riskavsnitt bör bevaras

Kapitel 21 och 23 har särskilt viktiga säkerhets- och riskmarkeringar: nätspänning, induktiva laster, solenoider, hobbygasmoduler och säkerhetskritiska tillämpningar. Dessa avsnitt bör inte tonas ned i jakten på kortare text. Däremot kan de formateras tydligare som `Riskkontroll` eller `Säkerhetsruta`.

### 6. Relaterat fungerar bättre här än i tidiga kapitel

`Relaterat`-avsnitten i blocket är i huvudsak funktionella. De hänvisar till kapitel om digitala signaler, analog läsning, bussar, matning, felsökning och andra komponentområden. De stör inte på samma sätt som interna projektreferenser. I `[PLAN-H]` bör de behållas men kontrolleras för relevans och längd.

## Rekommenderade generella regler till [PLAN-H]

1. **Komponentkapitel ska få behålla praktiska moment, men rubrikerna ska spegla handboksfunktion.**  
   `Praktiskt test` bör ersättas av mer precisa rubriker som `Referensmönster`, `Minsta fungerande koppling`, `Verifiera modulen`, `Valchecklista` eller `Arbetsmönster`.

2. **Säkerhetskritiska komponentkapitel ska prioriteras för riskkontroll.**  
   Kapitel 21 bör få särskild behandling eftersom laststyrning kan skada komponenter eller skapa farliga situationer om läsaren gör fel.

3. **Sensorprofil bör bli standardgrepp i sensorkapitel.**  
   Kapitel 23–25 visar att sensorprofil är ett bra sätt att göra boken mer handboksnära och mindre kurslik.

4. **`Kontrollera ditt val` bör ersättas av användbara checklistor.**  
   Frågorna ska inte primärt kontrollera läsarens kunskap utan hjälpa läsaren fatta beslut och undvika fel.

5. **`Det du kan använda kapitlet till` ska omskrivas med stödjande ton.**  
   Undvik `Efter kapitlet ska du kunna`. Variera formuleringen efter kapiteltyp.

6. **Dubbla eller tredubbla praktiska sektioner ska normaliseras.**  
   Kapitel 21 och 22 bör särskilt granskas så att ett huvudexempel inte blandas ihop med verifiering, vidarearbete och beslutsövningar.

## Kapitelvis bedömning

| Kapitel | Handbokskänsla | Läroboksspår | Behov av redaktionell åtgärd | Risk vid ändring | Kommentar |
|---:|---:|---|---|---|---|
| 21 | 5/5 | Medel | Medel | Medel | Mycket viktig praktisk och säkerhetsnära text. Praktiska moment bör behållas men rubriceras om. |
| 22 | 4/5 | Medel | Medel–hög | Medel | Innehållsrikt och användbart, men långt och strukturellt tätt. Behöver tydligare handboksrubriker. |
| 23 | 5/5 | Medel | Medel | Låg–medel | Stark sensorhandbok. Sensorprofil och riskkontroll bör lyftas. |
| 24 | 5/5 | Låg–medel | Låg–medel | Låg | Redan relativt handboksnära. Mest ton- och slutdelsjustering. |
| 25 | 5/5 | Medel | Medel | Låg–medel | Starkt beslutsstöd. Praktiska moment bör bli verifiering och arbetsmönster. |

## Prioriterade observationer till tväranalysen

- Kapitel 21–25 bekräftar att praktiska moment inte ska tas bort generellt. I komponent- och sensorkapitel är de ofta centrala.
- Den största förbättringen är att ge varje praktiskt moment en tydlig funktion: referens, verifiering, felsökning, val eller fördjupning.
- `Kontrollera ditt val` är ett steg i rätt riktning jämfört med rena quizrubriker, men bör fortfarande göras om till checklistor.
- Sensorprofilformatet bör övervägas som återkommande handboksgrepp.
- Laststyrning, matning, gasmoduler, UV och säkerhetskritiska tillämpningar bör hanteras med tydliga riskrutor.
- Kapitel 24 visar en positiv modell där `Exempel` och `Variation` kan ersätta ett allmänt `Praktiskt test`.

## Rekommenderad status inför nästa analyssteg

Steg 6 är genomfört. Nästa steg bör analysera kapitel 26–30, där boken går vidare till fler sensorer, ljud/mikrofoner, lagring, tid, I/O-expansion och moduler som ofta används i mer sammansatta projekt. Där bör analysen särskilt kontrollera om sensorprofil, verifiering och felsökningsmönster kan bli konsekventa över flera kapitel.
