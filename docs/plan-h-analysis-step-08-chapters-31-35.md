# [ANALYSPLAN] steg 8 – Kapitel 31–35

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1–7 genomförda  
Status: Genomförd  
Resultattyp: Redaktionell analys. Inga kapitel eller bokmanus har ändrats.

## Omfattning

Detta steg analyserar kapitel 31–35 enligt projektets kapitelordning:

| Nr | Fil | Kapiteltyp enligt steg 1 | Funktion i boken |
|---:|---|---|---|
| 31 | `chapters/drivkretsar-31.md` | Robusthet / drivning / praktisk komponent | Hjälpa läsaren välja rätt drivkrets mellan mikrokontroller och last. |
| 32 | `chapters/displaykretsar-minne-32.md` | Systemfunktion / data / displayunderlag | Hjälpa läsaren välja lagring, displaydrivning och status-/loggningsstrategi. |
| 33 | `chapters/analog-signalanpassning-33.md` | Teori/begrepp / robusthet / praktisk krets | Hjälpa läsaren förstå när analoga signaler behöver skydd, filter, förstärkning eller tröskelbeslut. |
| 34 | `chapters/stromforsorjning-batteridrift-34.md` | Robusthet / säkerhet / systemdesign | Hjälpa läsaren bygga stabil matning, batteridrift och robusta kopplingar. |
| 35 | `chapters/felsokning-35.md` | Metod / felsökning / handboksverktyg | Ge läsaren ett systematiskt arbetssätt för felsökning av Arduino-projekt. |

Blocket är särskilt viktigt för `[PLAN-H]` eftersom det samlar bokens mest handboksnära systemkapitel: drivning, datalagring, analog anpassning, strömförsörjning och felsökning. Om tidigare kapitel lär ut komponenter, visar detta block hur läsaren får projekten att fungera robust i praktiken.

## Snabb kvantitativ översikt

| Kapitel | Ord | H2 | H3 | Kodblock | `Det du kan använda kapitlet till` | `Praktiskt test` | `Prova vidare` | Kontrollsektion | `Valguide` | `Snabbval` | Felsökning |
|---:|---:|---:|---:|---:|---|---:|---|---|---|---|---|
| 31 | 5535 | 24 | 16 | 15 | Ja | 1 | Ja | Nej | Ja | Ja | Ja |
| 32 | 5207 | 33 | 25 | 10 | Ja | 1 | Ja | `Kontrollera ditt val` | Nej | Ja | Ja |
| 33 | 5933 | 29 | 21 | 12 | Ja | 2 | Ja | `Kontrollera ditt val` | Nej | Ja | Ja |
| 34 | 3894 | 24 | 17 | 7 | Ja | 1 | Ja | `Kontrollera ditt val` | Nej | Ja | Ja |
| 35 | 3936 | 22 | 19 | 9 | Nej | 1 | Nej | `Kontrollera arbetssättet` | Nej | Nej | Ja |

Tolkning: kapitel 31–35 har hög teknisk nytta och stark koppling till verkliga problem. De innehåller många handboksnära avsnitt som `Felsökning`, `Vanliga misstag`, `Snabbval`, säkerhetsruta och valguide. Samtidigt återkommer läroboksspår i `Efter kapitlet ska du kunna`, `Praktiskt test`, `Prova vidare` och kontrollfrågor. I detta block bör `[PLAN-H]` därför inte ta bort praktiken, utan byta ram: från övning till verifiering, riskkontroll, beslutsguide och felsökningsmönster.

## Kapitel 31 – Drivkretsar för LED, motorer och laster

### Handboksidentitet

Kapitel 31 är ett av bokens tydligaste handbokskapitel. Det har ett konkret problem: en Arduino-pinne är en styrsignal, inte en kraftutgång. Kapitlet hjälper läsaren välja mellan transistor, MOSFET, ULN2803, H-brygga, stegmotordrivare, LED-drivare, relädrivning och PCA9685. PLAN5-tilläggen kring DRV8833, L9110S och induktiva laster sitter naturligt i kapitlet eftersom de förstärker den centrala frågan: vilken drivlösning passar lasten?

Kapitlets styrka är att det inte bara beskriver komponenter, utan hela kedjan:

```text
Arduino-pinne -> drivkrets -> last
```

Det är en mycket bra handboksmodell. Den bör bevaras och gärna lyftas ännu mer i `[PLAN-H]`.

### Läroboksspår

Avsnittet `Det du kan använda kapitlet till` börjar med:

```text
Efter kapitlet ska du kunna:
```

Det är tydligt läroboksspråk. Innehållet i punkterna är bra, men ramen gör att kapitlet låter som en kursmodul. För en handbok vore en bättre riktning:

```text
När du använder kapitlet får du stöd för att:
```

eller:

```text
Kapitlet hjälper dig att:
```

Det praktiska testet är relevant, men rubriken `Praktiskt test: samma last med tre drivlösningar` låter delvis som en laboration. I just detta kapitel bör testet inte tas bort, eftersom det är ett bra referensmönster. Det bör däremot byta identitet till exempelvis:

- `Referensmönster: samma last med tre drivlösningar`
- `Verifiera drivkedjan med en enkel last`
- `Jämför drivlösningar utan att riskera kortet`

`Prova vidare` är i huvudsak bra beslutsstöd, särskilt delen där läsaren klassificerar drivbehov för olika laster. Men rubriken `Test 1`, `Test 2`, `Test 3` gör det mer kurslikt än nödvändigt. Det bör kunna bli:

- `Beslutsövning` om boken vill behålla pedagogiken.
- `Välj drivlösning för vanliga laster` om boken ska kännas mer som handbok.
- `Rita signalvägen innan du kopplar` för andra delen.

### Rekommendation för PLAN-H

Kapitel 31 bör i `[PLAN-H]` betraktas som ett positivt modellkapitel för robusthet och drivning, men med rubriknormalisering. Bevara valguiden, snabbvalet, säkerhetsrutan och felsökningen. Gör om lärandemål och testformuleringar till handboksnära språk.

## Kapitel 32 – Displaykretsar, minne och datalagring

### Handboksidentitet

Kapitel 32 har hög praktisk relevans eftersom det behandlar en vanlig övergång i Arduino-projekt: från att bara visa något i seriell monitor till att lagra data, visa status och hantera minnesbegränsningar. Orienteringen är stark eftersom den börjar med valfrågor:

- När räcker intern EEPROM?
- När är extern EEPROM eller FRAM bättre?
- När är SD-kort rätt val?
- När bör data visas direkt och när bör den loggas?

Detta är exakt den typ av beslutsstöd en handbok bör ge.

### Läroboksspår

Kapitlet har samma lärandemålsram:

```text
Efter kapitlet ska du kunna:
```

Här bör punkterna hellre presenteras som praktiska användningsfall, till exempel:

```text
Använd kapitlet när du behöver:
```

Det praktiska testet `liten datalogger med statusdisplay` är välmotiverat. Det är inte ett teoriexperiment utan ett användbart referensmönster. Däremot är omfattningen relativt stor: SD-kort, analogt mätvärde, statusmodell, seriell statusvy och möjlig OLED-utbyggnad. Som handbok skulle avsnittet fungera bättre om det tydligare kallades:

- `Referensmönster: liten datalogger med status`
- `Minsta fungerande loggning med statusfält`
- `Byggblock: mätvärde, status och loggrad`

`Kontrollera ditt val` består av åtta frågor. Flera är bra beslutsfrågor, men formen är quizlik. De bör i `[PLAN-H]` göras om till en checklista:

```text
Checklista innan du väljer lagring
```

Frågorna kan formuleras om till praktiska kontroller:

- Hur ofta kommer du att skriva data?
- Ska datan överleva strömavbrott?
- Behöver du läsa datan i en dator?
- Hur mycket RAM använder displaybiblioteket?
- Måste skrivningen kunna misslyckas utan att resten av systemet stoppar?

### Rekommendation för PLAN-H

Kapitel 32 bör bli ett tydligare besluts- och systemmönsterkapitel. Det behöver inte kortas kraftigt, men det bör få mindre övningsspråk och mer tydlig vägledning kring val av lagringsstrategi, displaystrategi och statusmodell.

## Kapitel 33 – Analog signalanpassning, op-förstärkare och komparatorer

### Handboksidentitet

Kapitel 33 är det mest teoretiskt tunga kapitlet i blocket, men ämnet kräver viss teori. Det lyckas ofta hålla teorin praktisk genom att koppla den till konkreta problem: för svag signal, fel spänningsnivå, brus, hög impedans, negativ signal, tröskelbeslut och skydd av ADC-ingång.

PLAN5-tilläggen om LM393/digitala tröskelmoduler och I2C logic level converter sitter naturligt. LM393 passar direkt i kapitlets komparatorlogik. Logic level converter är egentligen nära kapitel 9 och 4, men placeringen här fungerar eftersom kapitlet handlar om anpassning mellan signal och mikrokontroller.

### Läroboksspår

Även här börjar användningsavsnittet med:

```text
Efter kapitlet ska du kunna:
```

Det bör ändras. I ett analogt ämne är detta extra viktigt, eftersom läsaren annars kan känna att kapitlet kräver analog konstruktörskompetens. Snabb orientering säger redan något bra:

```text
Det här kapitlet är inte tänkt att göra dig till analog konstruktör.
```

Denna mjuka förväntanssättning bör få styra resten av kapitlet.

Kapitel 33 har två `Praktiskt test`-sektioner:

- tröskeldetektor med analog mätning och digital utgång
- enkel analog lågpassfiltrering

Båda är relevanta, men dubbla praktiska test gör kapitlet mer lärobokslikt. I `[PLAN-H]` bör de särskiljas:

- Det första bör bli `Referensmönster: tröskelbeslut med hysteres`.
- Det andra bör bli `Verifiera effekten av ett RC-filter`.

`Prova vidare` innehåller flera bra moment, men också tydliga uppgiftsformuleringar. Exempelvis `Dimensionera en spänningsdelare` är mycket relevant, men bör vara en beräkningschecklista eller ett återanvändbart mönster snarare än ett test.

### Rekommendation för PLAN-H

Kapitel 33 bör inte förenklas bort, men det bör få en mildare tröskel. Det ska framstå som ett kapitel läsaren konsulterar när en signal inte beter sig, inte som ett prov på analog elektronik. `[PLAN-H]` bör stärka kapitlets roll som beslutsstöd:

- direktkoppla
- dämpa
- filtrera
- buffra
- förstärka
- jämföra
- använda färdig modul

Detta skulle göra kapitlet mer handboksnära utan att minska teknikvärdet.

## Kapitel 34 – Strömförsörjning, batteridrift och robust konstruktion

### Handboksidentitet

Kapitel 34 är mycket viktigt för bokens professionella kvalitet. Det behandlar ett av de vanligaste skälen till att Arduino-projekt fungerar på skrivbordet men fallerar i verklig användning: svag eller felaktig strömförsörjning.

Kapitlet har stark handboksnytta genom strömbudget, separat matning, gemensam jord, avkoppling, spänningsfall, batteridrift, sleep-lägen, brownout och säkerhet kring nätspänning. Här är praktisk analys helt motiverad.

### Läroboksspår

Det tydligaste problemet är formuleringen:

```text
Efter kapitlet ska läsaren kunna:
```

Den avviker dessutom från tilltalet i övriga kapitel genom att använda tredje person. Detta bör korrigeras i `[PLAN-H]`.

`Praktiskt test: gör en strömbudget och hitta svag matning` är bra och bör behållas, men rubriken kan bli mer handboksnära:

- `Arbetsmönster: gör en strömbudget`
- `Verifiera matningen innan du bygger vidare`
- `Riskkontroll: hitta svag matning`

`Prova vidare` är praktiskt men delvis överlappande med huvudtestet. Eftersom strömbudgeten redan är ett arbetsmönster bör `Prova vidare` sannolikt kortas eller göras till `Fördjupning och varianter`.

`Kontrollera ditt val` har tio frågor och känns som quiz. Här bör det i stället bli:

```text
Checklista innan projektet får egen matning
```

eller:

```text
Säkerhetskontroll före batteridrift
```

### Rekommendation för PLAN-H

Kapitel 34 bör vara ett av de kapitel där `[PLAN-H]` prioriterar rubrik- och formändring, inte innehållsförkortning. Kapitlets värde är högt, men den pedagogiska ramen bör skifta från kurs till riskkontroll och robusthetsmetod.

## Kapitel 35 – Felsökning med metod

### Handboksidentitet

Kapitel 35 är sannolikt ett av bokens mest handboksnära kapitel. Det handlar inte om att lära sig en komponent, utan om att ge läsaren ett arbetssätt. Kapitelstrukturen är mer naturligt metodisk än flera tidigare kapitel: minimal reproduktion, seriell loggning, multimeter, digital I/O, analog mätning, PWM/motorer/laster, I2C, SPI, UART, logikanalysator, oscilloskop, bibliotek, strömförsörjning, intermittenta fel och diagnostiska testsketcher.

Detta är kärnmaterial för en praktisk handbok.

### Läroboksspår

Kapitlet saknar `Det du kan använda kapitlet till`, vilket gör att det inte har samma tydliga lärandemålsproblem som kapitel 31–34. Det har däremot `Praktiskt test: felsök ett I2C-problem metodiskt`. I detta kapitel är praktiken helt motiverad eftersom felsökning är en metodfärdighet. Rubriken bör ändå kunna bli mer handboksnära:

- `Felsökningsmönster: I2C-problem steg för steg`
- `Diagnostisk arbetsgång: I2C-modul hittas inte`
- `Exempel på felsökningsrapport`

`Kontrollera arbetssättet` är formulerat som kontrollfrågor. Här finns bra innehåll, men det bör bli en checklista eller principruta:

```text
Kontrollera felsökningsordningen
```

eller:

```text
Vanliga principer som sparar tid
```

Kapitlet har också en `Checklista`, vilket redan är ett starkt handboksformat. Därför bör kontrollfrågorna inte behövas i sin nuvarande form. Vissa frågor kan flyttas in i checklistan, andra kan omvandlas till felsökningsprinciper.

### Rekommendation för PLAN-H

Kapitel 35 bör användas som modell för hur boken kan kännas mer som handbok. Det har redan rätt identitet. PLAN-H bör främst:

- byta `Praktiskt test` till `Felsökningsmönster`
- omvandla `Kontrollera arbetssättet` till principchecklista
- låta `Checklista` bli slutpunkt i kapitlet

## Återkommande mönster i kapitel 31–35

### 1. Praktiken är relevant men rubrikerna gör den kurslik

Till skillnad från tidiga teorikapitel är de praktiska momenten här ofta mycket motiverade. Problemet är inte att de finns, utan att de heter `Praktiskt test`, `Test 1`, `Test 2` och `Prova vidare`. För detta block bör `[PLAN-H]` behålla mycket av innehållet men ändra ramen.

Rekommenderade ersättningar:

| Nuvarande rubrik | Rekommenderad handboksrubrik |
|---|---|
| `Praktiskt test` | `Referensmönster`, `Verifiera kopplingen`, `Arbetsmönster`, `Felsökningsmönster` |
| `Prova vidare` | `Varianter`, `Nästa beslut`, `Fördjupning`, `Bygg vidare när detta fungerar` |
| `Test 1`, `Test 2` | Beskrivande underrubriker utan testkänsla |
| `Kontrollera ditt val` | `Valchecklista`, `Riskkontroll`, `Checklista före inkoppling` |
| `Kontrollera arbetssättet` | `Principer för metodisk felsökning` |

### 2. `Efter kapitlet ska du kunna` bör ersättas i kapitel 31–34

Kapitel 31–34 använder lärandemålsramen. Kapitel 34 använder dessutom tredje person: `Efter kapitlet ska läsaren kunna`. Dessa formuleringar bör ingå i en generell PLAN-H-regel.

Bättre standardformuleringar:

- `Använd kapitlet när du behöver:`
- `Kapitlet hjälper dig att:`
- `Här får du stöd för att:`
- `Efter genomgången har du en praktisk modell för att:`

Den sista är mer pedagogisk men fortfarande mindre kravställande än `ska du kunna`.

### 3. Kontrollfrågor bör inte raderas rakt av

I detta block är många kontrollfrågor egentligen bra diagnostiska eller beslutande frågor. Att ta bort dem helt skulle minska nyttan. De bör i stället omvandlas:

- frågequiz -> checklista
- kunskapskontroll -> riskkontroll
- kontroll av förståelse -> kontroll före inkoppling
- repetitionsfrågor -> felsökningsprinciper

### 4. Snabbval fungerar bra

`Snabbval` i kapitel 31–34 fungerar som handboksformat. Det bör bevaras och eventuellt göras mer konsekvent i andra kapitel. I detta block ger snabbvalen en tydlig väg in till kapitlet för läsare som vill fatta beslut snabbt.

### 5. PLAN5-tillägg sitter naturligt

I kapitel 31 och 33 syns PLAN5-tilläggen tydligast. De verkar ligga rätt:

- DRV8833 och L9110S passar i H-brygge-/motordrivardelen.
- Induktiva laster passar i drivkrets- och skyddsdelen.
- LM393 passar i komparator-/tröskelresonemanget.
- Logic level converter passar som signalanpassningskomplettering, även om den också har tydlig koppling till kommunikationskapitlet.

Det finns inget i detta block som tyder på att PLAN5 har brutit kapitelstrukturen. Däremot bör `[PLAN-H]` eventuellt stärka korsreferenserna så att nivåomvandling också pekar tydligare mot kommunikationsbussar och 3,3 V/5 V-problematik.

### 6. Kapitel 35 är en modell för handbokston

Kapitel 35 visar hur boken kan fungera när den inte försöker vara kurs. Det är metodiskt, praktiskt och situationsbaserat. Det bör användas som stilreferens i PLAN-H när kontrollfrågor och tester i andra kapitel görs om till checklistor och arbetsmönster.

## Bedömning per kapitel

| Kapitel | Handbokskänsla | Läroboksspår | Behov av redaktionell åtgärd | Risk vid ändring | Kommentar |
|---:|---:|---|---|---|---|
| 31 | 5/5 | Medel | Medel | Låg | Mycket starkt drivningskapitel; ändra främst rubriker och lärandemålsram. |
| 32 | 4/5 | Medel | Medel | Medel | Bra systemkapitel; behöver mer checklista/beslut och mindre quizform. |
| 33 | 4/5 | Medel–hög | Medel–hög | Medel | Tekniskt tungt men viktigt; bör mildra kravkänsla och strukturera praktiken. |
| 34 | 5/5 | Medel | Medel | Låg | Mycket viktigt robusthetskapitel; bör omformas till riskkontroll och arbetsmönster. |
| 35 | 5/5 | Låg–medel | Låg–medel | Låg | Nära idealet för handbok; kontrollfrågor bör bli principchecklista. |

## Förslag till regler för [PLAN-H]

1. **Byt lärandemål till användningsnytta.**  
   Alla förekomster av `Efter kapitlet ska du kunna` och varianter bör ersättas med mjukare handboksformuleringar.

2. **Behåll praktiska moment i robusthetskapitel, men byt rubrikfamilj.**  
   Kapitel 31–35 bör inte tappa sina praktiska moment. De bör byta från `Praktiskt test` till `Referensmönster`, `Verifiering`, `Riskkontroll`, `Arbetsmönster` eller `Felsökningsmönster`.

3. **Gör kontrollfrågor till checklistor.**  
   I kapitel 32–35 bör `Kontrollera ditt val` och `Kontrollera arbetssättet` omvandlas till checklistor, beslutspunkter eller principer.

4. **Särskilj teori, beslut och verifiering.**  
   Kapitel 33 behöver tydligare skilja mellan analog förklaring, val av anpassning och praktisk verifiering.

5. **Använd kapitel 35 som stilmodell.**  
   Felsökningskapitlets metodiska ton bör fungera som referens för fler robusthets- och systemkapitel.

6. **Stärk korsreferenser utan interna dokumentreferenser.**  
   Inga interna projektartefakter hittades i kapitel 31–35. Däremot bör PLAN-H stärka läsarvänliga hänvisningar mellan drivning, signalanpassning, strömförsörjning och felsökning.

## Samlad slutsats

Kapitel 31–35 är ett av bokens starkaste block och bekräftar att projektet fungerar bäst när det är en praktisk handbok för beslut, robusthet och felsökning. Innehållet bör i huvudsak bevaras. Den redaktionella åtgärden bör inte vara att korta ned eller ta bort praktik, utan att ändra språk och kapitelram.

Det viktigaste inför `[PLAN-H]` är att detta block visar skillnaden mellan **praktik som kursövning** och **praktik som handboksverktyg**. I kapitel 31–35 är praktiken oftast motiverad, men den bör kallas och ramas in som referensmönster, verifiering, riskkontroll och felsökningsmetod. Om detta görs konsekvent kommer boken att behålla sin tekniska nytta men kännas mindre som lärobok och mer som en professionell Arduino-handbok.
