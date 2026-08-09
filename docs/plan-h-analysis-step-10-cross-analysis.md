# [ANALYSPLAN] steg 10 – Tväranalys av hela boken

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1–9 genomförda  
Status: Genomförd  
Resultattyp: Tväranalys och syntes. Inga kapitel eller bokmanus har ändrats.

## Omfattning

Detta steg väger samman samtliga tidigare analysrapporter:

- `docs/plan-h-analysis-step-01-method-and-identity.md`
- `docs/plan-h-analysis-step-02-chapters-00-05.md`
- `docs/plan-h-analysis-step-03-chapters-06-10.md`
- `docs/plan-h-analysis-step-04-chapters-11-15.md`
- `docs/plan-h-analysis-step-05-chapters-16-20.md`
- `docs/plan-h-analysis-step-06-chapters-21-25.md`
- `docs/plan-h-analysis-step-07-chapters-26-30.md`
- `docs/plan-h-analysis-step-08-chapters-31-35.md`
- `docs/plan-h-analysis-step-09-chapters-36-38.md`

Tväranalysen är inte en ny kapitelgranskning rad för rad. Den sammanställer mönster som återkommer över hela boken och formulerar underlag för steg 11, där åtgärderna ska prioriteras.

## Övergripande slutsats

Boken är i grunden redan en stark praktisk Arduino-handbok. De kapitelvisa analyserna visar att innehållet är relevant, användbart och ofta mycket nära den handboksidentitet som v4 eftersträvar. Problemet är därför inte huvudsakligen innehållsmängd, teknisk täckning eller kapitelordning.

Den återkommande svagheten är i stället det redaktionella lagret: flera kapitel använder ett språk och en yttre struktur som påminner om lärobok eller kursmaterial. Framför allt gäller detta formuleringar som liknar lärandemål, rubriker som `Praktiskt test`, överlapp mellan praktiska sektioner, och avslutande kontrollfrågor. Dessa delar gör att läsaren ibland kan uppleva boken som något som ska studeras och examineras, snarare än som ett arbetsverktyg.

`[PLAN-H]` bör därför inte bli en plan för mer innehåll. Den bör bli en redaktionell handboksplan som gör bokens befintliga innehåll mer konsekvent, mer läsarorienterat och mer användbart i praktiken.

## Inventering av återkommande textmönster

Följande inventering har gjorts i kapitelkatalogen som stöd för tväranalysen. Siffrorna ska användas som indikatorer, inte som exakta beslut om alla förekomster.

| Mönster | Antal förekomster | Tolkning |
|---|---:|---|
| `## Snabb orientering` | 37 | Nästan hela boken använder samma orienteringsrubrik. Det ger konsekvens men kan också kännas mekaniskt. |
| `Efter kapitlet ska` | 18 | Tydligt läroboksspråk. Bör ersättas med mjukare användningsformuleringar. |
| `## Praktiskt test` / `### Praktiskt test` | 45 | Mycket vanligt. Bör inte tas bort generellt, men måste byta funktion och rubrik efter kapiteltyp. |
| `## Prova själv` / `### Prova själv` | 7 | Förekommer främst i tidiga kapitel och överlappar ofta `Praktiskt test`. |
| `## Prova vidare` / `### Prova vidare` | 16 | Förekommer ofta i senare kapitel. Kan ofta bli arbetsmönster, variant eller vidare tillämpning. |
| Rubriker som börjar med `Kontrollera` | 38 | Vanligt avslut. Bör oftast bli checklista, riskkontroll, felsökningsordning eller vanliga missförstånd. |
| `docs/lookup-index.md` i kapiteltext | 1 | Intern projektartefakt i läsartext. Bör tas bort. |
| `PLAN5` i kapiteltext | 2 | Internt planspråk i läsartext. Bör ersättas med neutral rubrik. |

## Återkommande problem

### 1. Läroboksspråk i handboksram

Mönstret syns i flera kapiteltyper men är tydligast när `Snabb orientering` används som en form av lärandemål. Formuleringar som `Efter kapitlet ska du kunna` fungerar pedagogiskt, men signalerar krav och prestation. Det passar sämre i en praktisk handbok där läsaren ofta slår upp ett avsnitt för att lösa ett problem.

Det bör inte ersättas av en enda standardfras. Om alla kapitel får samma nya formulering riskerar boken bara att byta en mekanisk mall mot en annan. `[PLAN-H]` bör därför ange en liten uppsättning kapiteltypsbaserade alternativ.

Rekommenderad riktning:

- Orienteringskapitel: `Här får du en överblick över...`
- Grundfunktionskapitel: `Kapitlet hjälper dig förstå när och varför...`
- Komponentkapitel: `Du får stöd för att välja, koppla och felsöka...`
- Robusthetskapitel: `Kapitlet hjälper dig undvika vanliga fel kring...`
- Referenskapitel: `Använd kapitlet när du snabbt vill jämföra...`

### 2. Mekanisk användning av `Snabb orientering`

`Snabb orientering` är inte fel i sig. Den hjälper läsaren att snabbt förstå kapitlets riktning. Problemet är att den används nästan överallt och ofta får samma inre logik, oavsett kapiteltyp. I en handbok bör orienteringen vara mer situationsbunden.

Rekommenderad riktning:

- Behåll en kort orienterande start i de flesta kapitel.
- Byt inte nödvändigtvis rubriken överallt.
- Ändra innehållet så att det beskriver praktisk nytta, val, risker eller användningssituationer.
- I rena referens- och slutkapitel kan orienteringen ersättas av `Så använder du kapitlet`.

### 3. Otydlig funktion för `Praktiskt test`

`Praktiskt test` är det mest centrala tvärmönstret. Det används för många olika saker:

- första fungerande koppling,
- verifiering av sensor eller modul,
- riskkontroll,
- huvudexempel,
- felsökningsmetod,
- experiment,
- vidare övning.

Detta skapar överlapp och gör att boken ibland känns som kursmaterial. Samtidigt visar analysen att praktiska moment ofta är bokens styrka. De ska inte rensas bort generellt.

Rekommenderad riktning:

- Teori- och orienteringskapitel ska endast ha praktiska moment om de ger verklig handboksnytta.
- Grundfunktionskapitel kan ha `Minsta fungerande verifiering`.
- Komponentkapitel bör ha `Minsta fungerande koppling`, `Referensmönster` eller `Verifiera modulen`.
- Robusthetskapitel bör ha `Riskkontroll`, `Säker testkoppling` eller `Felsökningsmönster`.
- Metodkapitel bör ha `Arbetsmönster`, `Dokumentationssteg` eller `Modulchecklista`.
- Referenskapitel bör inte ha övningsliknande praktiska moment utan mallar, checklistor och beslutstabeller.

### 4. Överlapp mellan `Praktiskt test`, `Prova själv` och `Prova vidare`

I flera kapitel finns mer än ett praktiskt slutmoment. Det kan vara motiverat i komponentkapitel, men i tidiga teori- och orienteringskapitel blir det lätt för mycket. Det gör också att kapitlen får en skolbokskänsla.

Rekommenderad riktning:

- Varje kapitel bör normalt ha högst ett primärt praktiskt moment.
- Om flera moment behövs ska de ha tydligt olika funktioner.
- `Prova själv` bör i många fall tas bort eller omvandlas till `Använd detta när...`, `Nästa praktiska steg` eller `Variant`.
- `Prova vidare` bör inte låta som extraövning utan som vidare tillämpning, utbyggnad eller arbetsmönster.

### 5. Kontrollfrågor och quizkänsla

Rubriker som `Kontrollera att du hänger med`, `Kontrollera ditt val` och liknande kan vara användbara, men de bör inte upplevas som quiz. De fungerar bäst när de hjälper läsaren fatta beslut eller undvika fel.

Rekommenderad riktning:

- Ta bort ren kunskapskontroll i handboksdelar.
- Ersätt med `Snabb kontroll i praktiken`, `Vanliga missförstånd`, `Checklista innan du fortsätter`, `Riskkontroll`, `Valchecklista` eller `Felsökningsordning`.
- I teorikapitel bör kontrollfrågor hellre bli `Vanliga missförstånd`.
- I komponentkapitel bör de bli `Kontrollera innan du kopplar`.
- I referenskapitel bör de bli mallar eller beslutstabeller.

### 6. Interna projektartefakter i läsartext

Två interna artefakttyper har identifierats som särskilt tydliga:

- `docs/lookup-index.md` i inledningen.
- `PLAN5` i kapitel 38.

Dessa hör hemma i projektets arbetsdokument, inte i bokens läsartext. De bryter illusionen av en färdig handbok och bör tas bort eller omformuleras neutralt.

Rekommenderad riktning:

- `docs/lookup-index.md` ersätts med en läsarvänlig hänvisning till referenskapitlet.
- `PLAN5-tillägg i praktiken` ersätts med en neutral rubrik, exempelvis `Snabbguide: vanliga kompletterande moduler`.
- `[PLAN-H]` bör göra en generell sökning efter interna plan-, fil- och projektreferenser.

### 7. Kapitelmallar behöver styras av kapiteltyp

Bokens starkaste kapitel är de där formen matchar funktionen. Kapitel 35 fungerar bra eftersom felsökning behandlas som metod. Kapitel 38 fungerar bra när det agerar ren referens. Kapitel 2 fungerar bra när det hjälper läsaren välja kort. Problemen uppstår främst när samma rubriker återkommer oavsett om kapitlet är teori, plattform, komponent, robusthet, metod eller referens.

`[PLAN-H]` bör därför inte införa en gemensam mall för alla kapitel. Den bör införa kapiteltypsspecifika ramar.

## Rekommenderade kapitelmallar per kapiteltyp

### A. Inledning

Syfte: etablera bokens användning, målgrupp och handboksidentitet.

Rekommenderad struktur:

1. Vad boken hjälper dig med.
2. Vem boken är för.
3. Så använder du boken.
4. Hur kapitlen är uppbyggda.
5. Hänvisning till referenskapitlet, utan interna filnamn.
6. Vad boken inte försöker vara.

Bör undvika:

- interna dokumentreferenser,
- projektstatusspråk,
- löften som låter som kursmål.

### B. Orienteringskapitel

Exempel: kapitel 1–3 och delar av 10–16.

Syfte: ge karta, valhjälp och begreppslig orientering.

Rekommenderad struktur:

1. Varför området spelar roll.
2. Så känner du igen huvudalternativen.
3. När respektive alternativ passar.
4. Vanliga missförstånd.
5. Beslutschecklista.
6. Relaterat.

Bör normalt inte ha:

- teoriexperiment,
- quiz,
- flera praktiska slutmoment.

### C. Grundfunktionskapitel

Exempel: ADC, PWM, avbrott, kommunikation och digital I/O.

Syfte: förklara funktioner som läsaren behöver för praktiska projekt.

Rekommenderad struktur:

1. Grundidé.
2. När funktionen används.
3. Minsta fungerande verifiering.
4. Vanliga fel och begränsningar.
5. Arbetsmönster.
6. Sammanfattning eller checklista.

Bör ha praktiska moment endast när de är direkt användbara som felsöknings- eller verifieringsmönster.

### D. Kort- och plattformskapitel

Exempel: klassiska kort, kloner, moderna kort, ESP8266, ESP32, Pico och specialkort.

Syfte: hjälpa läsaren välja, portera och förstå skillnader.

Rekommenderad struktur:

1. Kortprofil.
2. Styrkor.
3. Begränsningar.
4. När kortet passar.
5. Portering eller verifiering.
6. Risker och vanliga fel.
7. Valchecklista.

Bör undvika alltför övningsliknande slutfrågor.

### E. Praktiska komponentkapitel

Exempel: LED, buzzers, servon, sensorer, displayer och I/O-expansion.

Syfte: hjälpa läsaren välja, koppla, testa och felsöka komponenter.

Rekommenderad struktur:

1. Vad komponenten gör.
2. När den passar.
3. Kopplingsprincip.
4. Minsta fungerande koppling eller referensmönster.
5. Vanliga misstag.
6. Felsökning.
7. Varianter och begränsningar.
8. Relaterat.

Praktiska moment bör oftast behållas, men namnges efter sin funktion.

### F. Robusthets- och säkerhetskapitel

Exempel: laster, drivkretsar, signalanpassning, strömförsörjning och felsökning.

Syfte: förebygga fel, skador, instabila projekt och feltolkade mätningar.

Rekommenderad struktur:

1. Riskbild.
2. Vad som ofta går fel.
3. Säker grundkoppling eller riskkontroll.
4. Rekommenderat arbetsmönster.
5. Felsökningsordning.
6. Checklista innan du kopplar vidare.
7. Relaterat.

Dessa kapitel bör inte tappa praktik, men praktiken måste kännas som kontroll och robusthet, inte som kursövning.

### G. Metod- och projektkapitel

Exempel: breadboard till modul och modular sensor-/styrstation.

Syfte: visa arbetssätt, dokumentation, integration och återanvändning.

Rekommenderad struktur:

1. Arbetsmål.
2. Arbetsordning.
3. Modulchecklista eller integrationsordning.
4. Beslutspunkter.
5. Dokumentationsmall.
6. Vanliga fallgropar.
7. Återanvändning.

Bör inte ha quiz. Praktik ska vara arbetssteg.

### H. Referenskapitel

Exempel: kapitel 38.

Syfte: fungera som snabb uppslagsdel.

Rekommenderad struktur:

1. Så använder du referensen.
2. Snabbvalstabeller.
3. Jämförelser.
4. Checklistor.
5. Mallar.
6. Felsökningsvägar.
7. Neutrala kompletteringsguider.

Bör inte ha:

- `Praktiskt test`,
- `Bygg din egen snabbguide` som övning,
- interna plannamn,
- kontrollfrågor.

## Ersättningskarta för återkommande formuleringar

| Nuvarande formulering/rubrik | Problem | Rekommenderad ersättning |
|---|---|---|
| `Efter kapitlet ska du kunna...` | Låter som lärandemål/krav. | `Kapitlet hjälper dig att...`, `Här får du en överblick över...`, `Du får stöd för att...` |
| `Efter kapitlet ska du framför allt kunna skilja på...` | Skolmässigt och kravställande. | `Du får hjälp att se skillnaden mellan...`, `Här ser du hur du skiljer på...` |
| `Praktiskt test` | Otydlig funktion och kurskänsla. | `Minsta fungerande verifiering`, `Verifiera modulen`, `Referensmönster`, `Riskkontroll`, `Arbetsmönster` |
| `Prova själv` | Kan kännas som övning. | `Nästa praktiska steg`, `Använd detta när...`, `Variant`, eller tas bort i teorikapitel. |
| `Prova vidare` | Kan kännas som extraövning. | `Bygg vidare när...`, `Variant`, `Utbyggnad`, `Arbetsmönster` |
| `Kontrollera att du hänger med` | Quizkänsla. | `Vanliga missförstånd`, `Snabb kontroll i praktiken`, `Tänk på` |
| `Kontrollera ditt val` | Kan kännas som kontrollfrågor. | `Valchecklista`, `Beslutspunkter`, `Riskkontroll` |
| `Kontrollera arbetssättet` | Kan kännas examinerande. | `Checklista för arbetssättet`, `Felsökningsordning`, `Innan du fortsätter` |
| `docs/lookup-index.md` | Intern projektfil. | `referenskapitlet i slutet av boken` |
| `PLAN5-tillägg i praktiken` | Internt planspråk. | `Vanliga kompletterande moduler i praktiken` |

## Kapitelgrupper som kräver redigering

### Låg risk, hög effekt

Dessa ändringar bör kunna göras utan att tekniskt innehåll påverkas.

- Inledningen: ta bort intern filreferens.
- Kapitel 38: ta bort `PLAN5` ur läsartext.
- Alla kapitel: ersätt `Efter kapitlet ska...`-formuleringar.
- Alla kapitel: omvandla kontrollfrågor till checklistor, missförstånd eller riskkontroll.
- Kapitel där `Praktiskt test` bara är rubrikproblem: byt rubrik och kort ingress.

### Medel risk, hög effekt

Dessa ändringar kräver mer redaktionellt omdöme.

- Kapitel 1–4: minska skolbokskänsla i de tidiga kapitlen.
- Kapitel 6–9: behåll funktionstester men gör dem till verifieringsmönster.
- Kapitel 11–16: gör kortkapitel mer konsekventa som kortprofiler/valstöd.
- Kapitel 17–25: ge komponentkapitel en tydligare referensmönsterstruktur.
- Kapitel 31–35: bevara robusthetspraktik men rama in den som riskkontroll och felsökning.

### Högre risk, bör göras varsamt

Dessa ändringar kan påverka bokens praktiska nytta om de görs för hårt.

- Ta bort praktiska moment i komponentkapitel. Detta bör normalt inte göras.
- Korta kapitel 38 för mycket. Snabbvalstabellerna är en central styrka.
- Standardisera alla kapitel till en enda ny mall. Det skulle motverka analysens slutsats.

## Tvärgående handboksprinciper inför [PLAN-H]

1. **Boken ska kännas som ett arbetsverktyg, inte som en kurs.**  
   Språk och rubriker ska hjälpa läsaren att fatta beslut, koppla rätt och felsöka.

2. **Praktik ska behållas när den har verklig projektnytta.**  
   Praktiska moment är inte problemet. Problemet är när de presenteras som övning eller test utan tydlig handboksfunktion.

3. **Kapiteltypen ska styra strukturen.**  
   Teori, orientering, komponenter, robusthet, metod och referens behöver olika mallar.

4. **Kontroll ska riktas mot projektet, inte mot läsaren.**  
   Undvik att kontrollera om läsaren “hänger med”. Hjälp läsaren kontrollera kopplingen, valet, risken eller felsökningsordningen.

5. **Interna projekttermer ska bort från boktexten.**  
   Filnamn, planbeteckningar och arbetsdokument hör hemma i `docs/`, inte i läsarens bok.

6. **Variation är bättre än en ny mekanisk mall.**  
   `[PLAN-H]` bör ge regler och rubrikfamiljer, inte tvinga alla kapitel att låta likadant.

7. **Bevara bokens styrkor.**  
   Beslutsstöd, vanliga fel, snabbvalstabeller, sensorprofiler, riskkontroller och felsökning är bokens starkaste element.

## Föreslagen åtgärdslogik för steg 11

Steg 11 bör inte lista åtgärder kapitel för kapitel i första hand. Det bör prioritera åtgärder i följande lager:

1. **Rensa interna artefakter.**  
   Låg risk och hög professionaliserande effekt.

2. **Byt läroboksspråk i orienteringar.**  
   Hög synlighet, låg teknisk risk.

3. **Omvandla kontrollfrågor till handboksformat.**  
   Stor effekt på ton och läsupplevelse.

4. **Normalisera praktiska sektioner efter kapiteltyp.**  
   Störst arbete men också störst kvalitetslyft.

5. **Inför kapiteltypsspecifika slutformat.**  
   Säkerställer att boken inte faller tillbaka i en mekanisk mall.

6. **Stärk referens- och beslutsstödet.**  
   Särskilt i kapitel 38 och i komponent-/robusthetskapitel.

## Risker inför [PLAN-H]

### Risk 1: För hård rensning

Om praktiska moment tas bort för brett kan boken förlora sin styrka. `[PLAN-H]` bör därför skilja tydligt mellan teoriexperiment som kan tas bort och verifieringsmönster som ska behållas.

### Risk 2: Ny mekanisk standardisering

Om alla rubriker byts till samma nya rubrik blir resultatet bara en ny mall. Planen bör använda rubrikfamiljer och kapiteltyp, inte en enda global ersättning.

### Risk 3: Referenskapitlet blir för långt eller för rensat

Kapitel 38 är viktigt som snabbnav. Det bör få renare struktur, men snabbvalstabeller och checklistor ska bevaras.

### Risk 4: Stilförändringen påverkar tekniskt innehåll

Eftersom `[PLAN-H]` är redaktionell bör den undvika teknisk omskrivning om det inte behövs för förståelse, säkerhet eller navigering.

## Slutsats

Tväranalysen bekräftar att boken inte behöver en ny innehållsplan i första hand. Den behöver en redaktionell handboksplan.

`[PLAN-H]` bör därför fokusera på att:

- ta bort interna projektspår ur läsartexten,
- byta lärandemålsformuleringar mot användningsnytta,
- omvandla quiz och kontrollfrågor till checklistor, missförstånd och riskkontroller,
- omklassificera praktiska moment efter deras verkliga funktion,
- införa kapiteltypsspecifika rubrikfamiljer,
- och bevara de praktiska styrkor som redan finns i v4.

Med dessa ändringar kan boken behålla sin bredd och tekniska användbarhet, men kännas mer som en professionell handbok och mindre som en kursbok.
