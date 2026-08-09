# [ANALYSPLAN] steg 9 – Kapitel 36–38

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1–8 genomförda  
Status: Genomförd  
Resultattyp: Redaktionell analys. Inga kapitel eller bokmanus har ändrats.

## Omfattning

Detta steg analyserar kapitel 36–38 enligt projektets kapitelordning:

| Nr | Fil | Kapiteltyp enligt steg 1 | Funktion i boken |
|---:|---|---|---|
| 36 | `chapters/breadboard-till-modul-36.md` | Metod / modulering / robusthet | Hjälpa läsaren gå från fungerande breadboard-experiment till återanvändbar modul med dokumenterad koppling och kodstruktur. |
| 37 | `chapters/modular-sensor-styrstation-37.md` | Sammanhängande projekt / metod / integration | Knyta ihop bokens komponent- och systemkunskap i en anpassningsbar sensor- och styrstation. |
| 38 | `chapters/referens-snabbvalsguider-38.md` | Referens / snabbval / uppslagskapitel | Ge läsaren snabb väg från fråga, komponent, modul eller felsymptom till rimligt första beslut. |

Blocket är särskilt viktigt för `[PLAN-H]` eftersom det avslutar boken och visar hur läsaren förväntas använda allt tidigare innehåll. Kapitel 36–37 fungerar som övergång från byggpraktik till återanvändbara arbetssätt, medan kapitel 38 fungerar som bokens huvudsakliga referens- och navigationsnav.

## Snabb kvantitativ översikt

| Kapitel | Ord | H2 | H3 | Kodblock | `Snabb orientering` | `Praktiskt test` | `Praktiskt arbetspass` | Kontrollsektion | `Relaterat` | Referens-/snabbvalskaraktär |
|---:|---:|---:|---:|---:|---|---:|---:|---|---|---|
| 36 | 2875 | 25 | 5 | 16 | Ja | 0 | 1 | `Kontrollera arbetssättet` | Nej | Medel |
| 37 | 3553 | 33 | 6 | 17 | Ja | 0 | 1 | `Kontrollera arbetssättet` | Ja | Medel–hög |
| 38 | 5281 | 27 | 17 | 1 | Nej, men har `Så använder du referensen` | 1 | 0 | `Kontrollera ditt val` | Ja | Mycket hög |

Tolkning: kapitel 36–38 är mer handboksnära än många tidigare block eftersom de inte inleds med klassiska lärandemål. De använder i stället orientering, metod, checklista och referenstabeller. Samtidigt finns fortfarande kurslika element i `Praktiskt arbetspass`, `Test 1`, `Test 2`, `Praktiskt test` och kontrollfrågor. I detta block bör `[PLAN-H]` framför allt skydda den starka praktiska nyttan men byta vissa rubriker och slutsektioner till tydligare handboksformat.

## Kapitel 36 – Från breadboard till återanvändbar modul

### Handboksidentitet

Kapitel 36 fungerar mycket väl som övergångskapitel mellan experiment och mer hållbara projekt. Det är inte ett rent komponentkapitel och inte ett teorikapitel. Det är ett metodkapitel som lär ut arbetssätt: pinout-dokumentation, kopplingsbeskrivning, hårdvarukonfiguration, wrapper-klass, testsketch, versionsanteckningar, märkning och mekanisk stabilitet.

Kapitlets starkaste handboksvärde är att det hjälper läsaren med ett vanligt praktiskt problem som ofta inte behandlas i enklare Arduino-material: projektet fungerade på breadboard en gång, men hur gör man det begripligt, flyttbart och återanvändbart? Den centrala frågan är mycket handboksnära:

```text
Hur gör jag ett fungerande experiment till något jag kan använda igen?
```

Kapitlet innehåller många praktiska mönster snarare än abstrakta regler. Exempelvis fungerar `Testsketch som modulens kontrakt`, `Modulmapp i projektet`, `Konfiguration per kortfamilj` och `Versioner och beroenden` som direkt användbara arbetssätt.

### Läroboksspår

Kapitlet har inte den tidigare tydliga formuleringen `Efter kapitlet ska du kunna`, vilket är positivt. `Snabb orientering` är här mer naturligt användningsinriktad än kravliknande:

```text
Det här kapitlet handlar om övergången från experiment till modul.
```

Det kurslika spåret finns främst i `Praktiskt arbetspass`, där underrubrikerna är `Test 1`, `Test 2`, `Test 3`, `Test 4` och `Fördjupning`. Innehållet är bra, men rubrikerna gör kapitlet mer arbetsbokslikt än handbokslikt.

Även `Kontrollera arbetssättet` är formulerat som frågor:

```text
Vad är den praktiska skillnaden mellan ett fungerande breadboard-experiment och en återanvändbar modul?
```

Frågorna är relevanta, men de bör i `[PLAN-H]` troligen bli en konkret checklista eller ett beslutstest. Exempel:

- `Checklista: är experimentet redo att bli modul?`
- `Riskkontroll innan du bygger om`
- `Modulens minsta dokumentation`

### Rekommendation för PLAN-H

Kapitel 36 bör bevaras nästan helt innehållsmässigt. Det är en viktig brygga mellan bokprojektets komponentdel och projekt-/referensdel. `[PLAN-H]` bör däremot byta rubrikram i slutet:

- `Praktiskt arbetspass` kan bli `Arbetsmönster: gör experimentet återanvändbart`.
- `Test 1–4` kan bli `Dokumentera kopplingen`, `Samla konfigurationen`, `Skapa modulgränssnitt`, `Spara diagnostisk testsketch`.
- `Kontrollera arbetssättet` kan bli `Checklista: en återanvändbar modul bör ha`.

## Kapitel 37 – Sammanhängande projekt: modulär sensor- och styrstation

### Handboksidentitet

Kapitel 37 är bokens integrationskapitel. Det fungerar som ett sammanhängande projekt, men är lyckligtvis inte skrivet som ett enda facit. Det presenteras som en projektmall som kan anpassas till flera användningsfall: miljöstation, verkstadsmonitor, växthusvakt, batteridriven datalogger, IoT-nod eller statuspanel.

Det är en stark lösning för bokens avslutning. Kapitlet visar hur tidigare delar kan kombineras utan att läsaren tvingas följa ett exakt workshopspår. Handbokskänslan är starkast i avsnitt som:

- `Välj ambitionsnivå`
- `Kortval`
- `Komponentförslag`
- `Programarkitektur`
- `Integrationsplan`
- `Felsökning i projektet`
- `Valguide för projektvarianter`
- `När du bör välja en annan lösning`
- `Dokumentera slutprojektet`

Dessa avsnitt gör kapitlet till en anpassningsbar projektmall snarare än ett skolprojekt.

### Läroboksspår

Även här finns en kursliknande slutram. `Praktiskt arbetspass` innehåller flera teststeg:

- `Test 1: Bygg grundstationen med stubbar`
- `Test 2: Lägg till verklig miljösensor`
- `Test 3: Lägg till display`
- `Test 4: Lägg till styrutgång`
- `Test 5: Gör en kortvalsjämförelse`
- `Fördjupning: Gör projektet uppkopplat`

Innehållet är mycket relevant, men ordet `Test` gör det mer kurslikt än nödvändigt. Eftersom detta är ett projektkapitel bör inte momenten tas bort. De bör snarare göras om till en integrationsordning:

- `Integrationssteg 1: starta med stubbar`
- `Integrationssteg 2: anslut verklig sensor`
- `Integrationssteg 3: lägg till presentation`
- `Integrationssteg 4: anslut styrutgång`
- `Integrationssteg 5: jämför kortval`
- `Utbyggnad: nätverk och loggning`

`Kontrollera arbetssättet` är återigen i frågeform och bör hellre bli en projektchecklista. Frågorna är bra men bör inte kännas som quiz. De kan omformas till exempelvis:

- `Projektchecklista innan du går vidare`
- `Kontrollpunkter för ett robust slutprojekt`
- `Besluts- och felsökningspunkter`

### Rekommendation för PLAN-H

Kapitel 37 bör betraktas som ett starkt projektkapitel och behållas. Det bör inte förenklas bort. Däremot bör `[PLAN-H]` göra kapitlet tydligare som **projektmall** snarare än **övningskapitel**.

Viktigast är att byta slutsektionernas rubriker:

- `Praktiskt arbetspass` -> `Integrationsordning` eller `Bygg projektet stegvis`.
- `Test 1–5` -> `Steg 1–5` eller `Integrationssteg`.
- `Kontrollera arbetssättet` -> `Projektchecklista`.

Kapitlets `Relaterat`-sektion fungerar bra. Den är selektiv och problemlösande, inte mekanisk. Den bör bevaras som positiv modell.

## Kapitel 38 – Referens: snabbvalsguider och jämförelsetabeller

### Handboksidentitet

Kapitel 38 är bokens tydligaste referenskapitel och ett av de viktigaste kapitlen för den praktiska handboksidentiteten. Inledningen säger uttryckligen:

```text
Det här kapitlet är inte tänkt som en vanlig lektion.
```

Det är helt rätt riktning. Kapitlet fungerar som snabb väg från fråga till beslut och är fyllt av tabeller, snabbval, felsökningsingångar, dokumentationsmönster och riskkontroller.

Särskilt starka delar är:

- `Snabbindex: börja i rätt kapitel`
- `Snabbguide: från projektidé till första test`
- `Snabbval: vilket kort ska jag börja med?`
- `Snabbval: kommunikationsbuss`
- `Snabbval: sensor efter mätuppgift`
- `Snabbval: drivkrets eller direkt pinne?`
- `Snabbval: felsökning efter symptom`
- `Snabbval: dokumentation du bör skapa`

Detta är exakt den typ av material som gör boken användbar som uppslagsverk efter första genomläsning.

### PLAN5-tilläggets synlighet

Avsnittet `Snabbguide: PLAN5-tillägg i praktiken` är funktionellt och gör PLAN5-komponenterna lätta att hitta. Det hjälper läsaren förstå var solenoid, DRV8833, L9110S, LM393, level shifter, KY-037, LM386, APDS-9960, PCF8575 och analog Hall-sensor hör hemma.

Men rubriken innehåller en intern utvecklingsetikett:

```text
PLAN5-tillägg
```

Det är inte lika problematiskt som en filreferens till `docs/lookup-index.md`, men det är fortfarande ett projektinternt namn. En läsare som inte följt bokprojektets utvecklingshistorik behöver inte veta att detta var PLAN5. I `[PLAN-H]` bör rubriken ändras till något läsarcentrerat, exempelvis:

- `Snabbguide: vanliga kompletterande moduler`
- `Snabbguide: moduler som ofta dyker upp i Arduino-kit`
- `Snabbguide: när projektet behöver mer än standardexemplen`

Även första stycket bör justeras så att det inte nämner PLAN5 utan beskriver funktionen direkt.

### Referensstruktur och navigation

Kapitel 38 har mycket god uppslagsstruktur. Snabbindexet och snabbvalsrubrikerna gör kapitlet lätt att skumma. Det är en styrka att rubrikerna ofta börjar med `Snabbval:` eftersom läsaren direkt ser vilken fråga avsnittet besvarar.

Samtidigt kan kapitlet bli ännu mer användbart genom att `[PLAN-H]` gör tre saker:

1. **Byt utvecklingsetiketter mot läsaretiketter.**  
   `PLAN5-tillägg` bör bort ur läsartexten.

2. **Minska kursramen i slutet.**  
   `Praktiskt test: gör en egen valguide`, `Bygg din egen snabbguide` och `Kontrollera ditt val` är innehållsmässigt bra, men låter som övningar. I ett referenskapitel bör de bli mallar och checklistor.

3. **Gör referensen ännu mer självständig.**  
   Kapitel 38 bör vara lätt att använda utan att läsaren läser allt från början. Det kan därför vinna på tydligare rubriker som `Mall: projektspecifik valguide`, `Mall: komponentkort`, `Checklista: kontrollera ditt val`.

### Läroboksspår

Kapitel 38 innehåller inte klassiska lärandemål, men har flera tydliga kursmoment:

```text
Praktiskt test: gör en egen valguide
```

```text
Bygg din egen snabbguide
```

```text
Kontrollera ditt val
```

Dessa bör inte raderas. De är mycket användbara. Problemet är rubriken och ramen, inte innehållet. För en handbok bör de omformas till referensverktyg:

- `Praktiskt test: gör en egen valguide` -> `Mall: gör en projektspecifik valguide`
- `Bygg din egen snabbguide` -> `Mallar för egna snabbguider`
- `Test 1–4` -> `Kortvalsmall`, `Sensormall`, `Risklista`, `Komponentmall`
- `Kontrollera ditt val` -> `Slutchecklista innan du kopplar`

### Rekommendation för PLAN-H

Kapitel 38 bör vara ett huvudmål för `[PLAN-H]`, inte för att innehållet är svagt, utan för att kapitlet är strategiskt viktigt. Om referenskapitlet får helt handboksnära rubriker kan det fungera som bokens nav.

De viktigaste åtgärderna bör vara:

- Ta bort `PLAN5` ur rubrik och brödtext.
- Byt `Praktiskt test` till `Mall`.
- Byt `Bygg din egen snabbguide` till en tydlig mall-/referenssektion.
- Byt `Kontrollera ditt val` till `Slutchecklista`.
- Överväg att lyfta `Snabbindex` ännu tidigare i bokens inledning, men utan interna filreferenser.
- Behåll tabellerna och snabbvalsguiderna.

## Blockövergripande mönster

### 1. Kapitel 36–37 är metod- och projektkapitel, inte vanliga övningskapitel

Det vore fel att ta bort praktiken från kapitel 36–37. De handlar just om att omsätta bokens kunskap i fungerande arbetssätt och projekt. Men rubrikramen bör ändras från `Test` och `Praktiskt arbetspass` till `Arbetsmönster`, `Integrationsordning`, `Projektmall` och `Checklista`.

### 2. Kapitel 38 bör bli renare referens

Kapitel 38 är redan mycket nära ett professionellt referenskapitel, men det störs av två saker:

- intern utvecklingsetikett: `PLAN5`
- övningsramar i slutet

Båda är enkla att åtgärda utan att förlora innehåll.

### 3. Kontrollfrågor återkommer även i slutblocket

Kapitel 36, 37 och 38 avslutas alla med kontrollfrågor. Detta är konsekvent med tidigare kapitel, men det förstärker också lärobokskänslan. I slutdelen av boken bör kontrollfrågor i stället bli checklistor, projektkontroller eller beslutsstöd.

### 4. `Relaterat` fungerar bäst när det är selektivt

Kapitel 37 och 38 har `Relaterat`. I kapitel 37 är det kort och funktionellt. Detta bekräftar den tidigare PLAN3-principen: relaterat-avsnitt bör vara selektiva och problemlösande, inte mekaniska.

### 5. Inga direkta filreferenser hittades i kapitel 36–38

I detta block hittades inga direkta referenser till `docs/lookup-index.md`, `build/book.md`, `canon` eller projektstatus. Däremot hittades intern projektterminologi i form av `PLAN5-tillägg`, vilket bör hanteras som en närliggande kategori: läsartext ska inte förutsätta kunskap om projektets interna arbetsplaner.

## Bedömning per kapitel

| Kapitel | Handbokskänsla | Läroboksspår | Behov av redaktionell åtgärd | Risk vid ändring | Kommentar |
|---:|---:|---|---|---|---|
| 36 | 4/5 | Medel | Medel | Låg | Stark metodnytta; byt slutdel från test/frågor till arbetsmönster och checklista. |
| 37 | 4/5 | Medel | Medel | Medel | Bra projektmall; praktiken ska behållas men bli integrationsordning snarare än övningspass. |
| 38 | 5/5 | Medel | Medel–hög | Låg | Mycket viktigt referenskapitel; ta bort `PLAN5`-etikett och gör övningsdelar till mallar/checklistor. |

## Förslag till regler för [PLAN-H]

1. **Projektinternt planspråk ska bort ur läsartexten.**  
   Precis som filreferenser bör interna etiketter som `PLAN5` inte synas i bokens kapitel. De kan finnas i projektstatus och versionsdokument, men inte i boktext.

2. **Metodkapitel får ha arbetsmoment, men de bör heta arbetsmönster.**  
   Kapitel 36 bör inte tappa sina praktiska moment. De bör byta från `Test` till `Arbetsmönster`, `Modulchecklista` eller `Dokumentationssteg`.

3. **Projektkapitel bör ha integrationsordning.**  
   Kapitel 37 bör rama in momenten som stegvis integration och projektmall, inte som kursövningar.

4. **Referenskapitel ska använda mallar och checklistor, inte övningar.**  
   Kapitel 38 bör ersätta `Praktiskt test`, `Bygg din egen snabbguide` och `Kontrollera ditt val` med mall-/checklisteformat.

5. **Slutdelen bör visa hur boken används efter första läsning.**  
   Kapitel 36–38 bör stärka bokens roll som arbetsverktyg: återanvändbar modul, projektmall och snabbvalsguide.

6. **Bevara snabbvalstabellerna.**  
   Snabbvalsguiderna är en av bokens största styrkor och bör inte kortas ned i en redaktionell rensning.

## Samlad slutsats

Kapitel 36–38 bekräftar att boken har en stark handboksidentitet i sin slutdel. Kapitel 36 lär ut ett hållbart arbetssätt för att göra experiment återanvändbara. Kapitel 37 visar hur bokens delar kan kombineras i ett verkligt projekt utan att låsa läsaren till ett facit. Kapitel 38 fungerar som ett snabbt referensnav för kortval, sensorer, bussar, drivning, strömförsörjning, felsökning och dokumentation.

Det viktigaste inför `[PLAN-H]` är därför inte att minska innehållet, utan att byta ram. Slutblockets praktiska moment bör göras om från test/övning/kontrollfrågor till arbetsmönster, integrationsordning, mallar, checklistor och beslutspunkter.

Särskilt kapitel 38 bör få en renare läsarorienterad identitet. `PLAN5-tillägg i praktiken` bör inte stå kvar i boktexten. Det bör bli en neutral snabbguide för vanliga kompletterande moduler. Med den ändringen och med mall-/checklisteformat i slutet kan kapitel 38 fungera ännu tydligare som bokens professionella referenskapitel.
