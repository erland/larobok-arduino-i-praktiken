# [ANALYSPLAN] steg 1 – Metodkalibrering och bokidentitet

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4`  
Status: Genomförd  
Resultattyp: Analysunderlag. Inga kapitel eller bokmanus har ändrats.

## Syfte

Detta steg fastställer hur resten av `[ANALYSPLAN]` ska genomföras och vad analysen ska mäta. Fokus är att kalibrera analysmetoden mot bokens faktiska v4-innehåll, inte att börja redigera boken.

Steget har läst och vägt samman följande projektunderlag:

- `README.md`
- `book.yaml`
- `docs/book-specification.md`
- `docs/project-version-handbokstruktur-v4.md`
- `docs/editorial-target.md`
- `docs/chapter-typology.md`
- `docs/chapter-templates-by-type.md`
- `docs/final-structure-rule.md`
- kapitelöversikten i `chapters/`

## Övergripande identitet i v4

V4 beskriver boken som en praktisk Arduino-handbok med tydlig pedagogisk kvalitet. Den ska kunna läsas från början till slut, men dess starkaste användningsfall är att hjälpa läsaren vid arbetsbänken:

- välja rätt Arduino-kompatibelt kort,
- förstå en komponent, modul, sensor eller krets,
- hitta fungerande kopplings- och kodmönster,
- felsöka konkreta problem,
- jämföra alternativ,
- gå från experiment till mer robust lösning.

Det betyder att boken inte bör kännas som en traditionell kursbok där varje kapitel har samma lektionsram. Den ska i stället använda kapiteltypanpassade strukturer och prioritera praktisk orientering, valhjälp, felsökning, snabbreferenser och korsreferenser.

## Definition av "praktisk handbok" för denna analys

I resten av `[ANALYSPLAN]` används följande arbetsdefinition:

> En praktisk handbok är ett bokmanus där läsaren snabbt kan förstå när ett ämne är relevant, hur det används, vilka begränsningar som finns, vad som ofta går fel och vart man ska gå vidare. Pedagogik får finnas, men den ska vara användningsnära och inte formuleras som kursmål, prov, obligatoriska övningar eller skolmässig kontroll.

Det innebär att analysen inte försöker ta bort pedagogik. Den försöker göra pedagogiken mindre synlig som kursstruktur och mer integrerad i handboksnyttan.

## Identifierade kapiteltyper

V4 har redan en etablerad typologi. Den är användbar och bör ligga till grund för PLAN-H, men kommande analyssteg ska kontrollera hur väl den faktiskt följs i varje kapitel.

| Kapiteltyp | Kapitel | Förväntad funktion i handboken |
|---|---:|---|
| Inledning | 00 | Förklara hur boken används, utan interna projektreferenser. |
| Orientering | 01–04 | Ge karta, sammanhang och nödvändiga grundbegrepp. |
| Grundfunktion | 05–09 | Förklara återkommande Arduino-funktioner och kodmönster. |
| Kort och plattform | 10–16 | Hjälpa läsaren välja kortfamilj, korttyp eller utvecklingsplattform. |
| Komponent och aktuator | 17–22 | Visa praktisk användning av utgångar, laster, ljud, motorer och displayer. |
| Sensor och mätning | 23–29 | Visa vad sensorer faktiskt mäter, hur mätvärden begränsas och hur rimlighet kontrolleras. |
| Robusthet och krets | 30–34 | Stärka projekt med drivkretsar, expansion, signalanpassning, minne och ström. |
| Metod och projekt | 35–37 | Hjälpa läsaren felsöka, modularisera och bygga sammanhängande lösningar. |
| Referens | 38 | Fungera som snabbval, jämförelser och praktiskt beslutsstöd. |

## Kapitelöversikt som analysen utgår från

| Nr | Fil | Kapiteltyp | Ord | H1 |
|---:|---|---|---:|---|
| 00 | `00-inledning.md` | Inledning | 899 | Inledning — Så använder du boken |
| 01 | `ekosystem-01.md` | Orientering | 3298 | 1. Arduino-kompatibla system som ekosystem |
| 02 | `valja-ratt-kort-02.md` | Orientering | 4406 | 2. Att välja rätt kort för rätt projekt |
| 03 | `utvecklingsmiljo-bibliotek-03.md` | Orientering | 4082 | 3. Utvecklingsmiljö, bibliotek och projektstruktur |
| 04 | `elektriska-grunder-04.md` | Orientering | 4281 | 4. Elektriska grunder för programmerare |
| 05 | `digital-io-05.md` | Grundfunktion | 4238 | 5. Digital I/O, knappar och logiska signaler |
| 06 | `analog-lasning-adc-06.md` | Grundfunktion | 4082 | 6. Analog läsning, ADC och mätosäkerhet |
| 07 | `pwm-timers-07.md` | Grundfunktion | 4150 | 7. PWM, timers och tidsstyrning |
| 08 | `avbrott-watchdog-08.md` | Grundfunktion | 3828 | 8. Avbrott, watchdog och robust körning |
| 09 | `kommunikation-bussar-09.md` | Grundfunktion | 5657 | 9. Kommunikation: UART, I2C, SPI och 1-Wire |
| 10 | `klassiska-arduino-kort-10.md` | Kort och plattform | 3259 | 10. Klassiska Arduino-kort: UNO, Nano och Mega |
| 11 | `kloner-lagkostnadskort-11.md` | Kort och plattform | 4697 | 11. Kloner, lågkostnadskort och tredjepartsvarianter |
| 12 | `moderna-arduino-kort-12.md` | Kort och plattform | 4902 | 12. Moderna Arduino-kort |
| 13 | `esp8266-nodemcu-13.md` | Kort och plattform | 4264 | 13. ESP8266 och NodeMCU |
| 14 | `esp32-familjen-14.md` | Kort och plattform | 4215 | 14. ESP32-familjen i Arduino-världen |
| 15 | `raspberry-pi-pico-15.md` | Kort och plattform | 4227 | 15. Raspberry Pi Pico, RP2040 och RP2350 i Arduino-miljö |
| 16 | `smakort-specialkort-16.md` | Kort och plattform | 4767 | 16. Småkort, specialkort och avancerade utvecklingskort |
| 17 | `led-rgb-ljuseffekter-17.md` | Komponent och aktuator | 5296 | 17. LED, RGB-LED och ljuseffekter |
| 18 | `adresserbara-led-18.md` | Komponent och aktuator | 4258 | 18. Adresserbara LED: NeoPixel, WS2812 och liknande |
| 19 | `buzzers-ljudsignaler-19.md` | Komponent och aktuator | 4827 | 19. Buzzers, ljudsignaler och enkla ljudutgångar |
| 20 | `servon-motorer-20.md` | Komponent och aktuator | 5150 | 20. Servon, DC-motorer och stegmotorer |
| 21 | `relaer-mosfetar-laster-21.md` | Komponent och aktuator | 4497 | 21. Reläer, MOSFET:ar, solenoider och andra laster |
| 22 | `displayer-anvandargranssnitt-22.md` | Komponent och aktuator | 6024 | 22. Displayer och enkla användargränssnitt |
| 23 | `miljosensorer-23.md` | Sensor och mätning | 6025 | 23. Temperatur, fukt, tryck och miljösensorer |
| 24 | `ljus-farg-optiska-sensorer-24.md` | Sensor och mätning | 4972 | 24. Ljus, färg, UV och optiska sensorer |
| 25 | `avstand-narvaro-25.md` | Sensor och mätning | 4983 | 25. Avstånd, närvaro och objektupptäckt |
| 26 | `rorelse-orientering-26.md` | Sensor och mätning | 3375 | 26. Rörelse, orientering och vibration |
| 27 | `ljud-mikrofoner-27.md` | Sensor och mätning | 4202 | 27. Ljud, mikrofoner och enkla signalmätningar |
| 28 | `strom-spanning-energi-28.md` | Sensor och mätning | 4719 | 28. Ström, spänning, energi och batterimätning |
| 29 | `position-tid-identitet-29.md` | Sensor och mätning | 4337 | 29. Position, tid och identitet |
| 30 | `io-expansion-30.md` | Robusthet och krets | 5850 | 30. I/O-expansion, shift registers och multiplexers |
| 31 | `drivkretsar-31.md` | Robusthet och krets | 5535 | 31. Drivkretsar för LED, motorer och laster |
| 32 | `displaykretsar-minne-32.md` | Robusthet och krets | 5207 | 32. Displaykretsar, minne och datalagring |
| 33 | `analog-signalanpassning-33.md` | Robusthet och krets | 5933 | 33. Analog signalanpassning, op-förstärkare och komparatorer |
| 34 | `stromforsorjning-batteridrift-34.md` | Robusthet och krets | 3894 | 34. Strömförsörjning, batteridrift och robust konstruktion |
| 35 | `felsokning-35.md` | Metod och projekt | 3936 | 35. Felsökning med metod |
| 36 | `breadboard-till-modul-36.md` | Metod och projekt | 3710 | 36. Från breadboard till återanvändbar modul |
| 37 | `modular-sensor-styrstation-37.md` | Metod och projekt | 4636 | 37. Sammanhängande projekt: modulär sensor- och styrstation |
| 38 | `referens-snabbvalsguider-38.md` | Referens | 6292 | 38. Referens: snabbvalsguider och jämförelsetabeller |

## Kalibrerad analysmetod för kommande steg

Varje kapitelblock ska analyseras i tre nivåer.

### 1. Kapitelvis läsning

För varje kapitel i blocket ska analysen dokumentera:

- vilken kapiteltyp kapitlet faktiskt fungerar som,
- om rubrikstrukturen matchar kapiteltypen,
- om kapitlet har läroboksspår som bör mildras,
- om praktiska moment är motiverade,
- om quiz/kontrollfrågor bör tas bort, omformuleras eller ersättas,
- om interna projektartefakter finns i läsartexten,
- vilka konkreta formuleringar som bör ingå som åtgärdskandidater i PLAN-H.

### 2. Blockmönster

Efter varje block ska analysen sammanfatta:

- återkommande rubriker som används rätt,
- återkommande rubriker som känns mekaniska,
- överlapp mellan sektioner,
- formuleringar som låter som kursmål,
- handboksnära formuleringar som fungerar väl,
- kapiteltypsspecifika regler som bör skapas.

### 3. PLAN-H-kandidater

Varje blockrapport ska avslutas med preliminära PLAN-H-kandidater i tre nivåer:

- **Generell regel** – bör gälla många kapitel.
- **Kapiteltypsregel** – bör gälla en viss kapiteltyp.
- **Kapitelunik åtgärd** – bör gälla ett specifikt kapitel.

Detta gör att PLAN-H senare kan byggas på återkommande bevis, inte på enstaka intryck.

## Formuleringar och sektioner som särskilt ska spåras

En första maskinell inventering av v4 visar att följande mönster behöver följas upp manuellt i kommande steg.

- `Efter kapitlet ska du`: 17 träff(ar), i kapitel 01, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33.
- `ska du kunna`: 18 träff(ar), i kapitel 08, 09, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33.
- `Kontrollera att du hänger med`: 7 träff(ar), i kapitel 01, 03, 04, 05, 06, 07, 09.
- `Praktiskt test`: 49 träff(ar), i kapitel 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 m.fl. (36 kapitel).
- `Prova själv`: 7 träff(ar), i kapitel 01, 02, 04, 06, 07, 08, 09.
- `docs/lookup-index\.md`: 1 träff(ar), i kapitel 00.
- `canon`: 1 träff(ar), i kapitel 28.


### Samlad första inventering

| Mönster | Antal träffar | Antal kapitel |
|---|---:|---:|
| `Efter kapitlet ska du` | 17 | 17 |
| `ska du kunna` | 18 | 18 |
| `Du kommer att` | 3 | 3 |
| `Kontrollera att du hänger med` | 7 | 7 |
| `Praktiskt test` | 49 | 36 |
| `Prova själv` | 7 | 7 |
| `Övning` | 12 | 6 |
| `Quiz` | 0 | 0 |
| `docs/lookup-index\.md` | 1 | 1 |
| `canon` | 1 | 1 |
| `build/book\.md` | 0 | 0 |
| `projektstatus` | 0 | 0 |
| `Lärandemål` | 0 | 0 |
| `Varför detta kapitel finns` | 0 | 0 |
| `Innan vi börjar` | 0 | 0 |
| `## Snabb orientering` | 37 | 37 |
| `## Förutsättningar` | 27 | 27 |
| `## Snabb sammanfattning` | 10 | 10 |
| `## Snabbreferens` | 20 | 20 |
| `## Relaterat` | 24 | 24 |

## Preliminära hypoteser inför steg 2–12

Detta är inte slutliga beslut, utan hypoteser som ska prövas i kapitelblocken.

### Hypotes 1: V4 är redan på väg mot handbok, men bär kvar läroboksspår

Projektets styrdokument pekar tydligt mot handbok. Samtidigt finns fortfarande formuleringar som `Efter kapitlet ska du...`, `ska du kunna...` och `Kontrollera att du hänger med`. Dessa bör inte automatiskt tas bort överallt, men deras funktion behöver prövas. De kan ofta ersättas med mer stödjande formuleringar som:

- `I det här kapitlet får du en praktisk överblick över...`
- `Du får se hur du skiljer på...`
- `Kapitlet hjälper dig att välja mellan...`
- `När du är klar har du en känsla för...`
- `Använd kapitlet när du behöver avgöra...`

### Hypotes 2: "Praktiskt test" och "Prova själv" överlappar delvis

`Praktiskt test` förekommer mycket ofta och `Prova själv` förekommer framför allt i de tidiga kapitlen. I praktiska komponentkapitel kan sådana sektioner vara motiverade. I rent teoretiska eller orienterande kapitel kan de däremot göra boken mer kurslik.

Kommande analys ska därför skilja på:

- bänktest med verklig komponent,
- kodmönster som faktiskt hjälper senare kapitel,
- teoriexperiment som mest finns där för att varje kapitel ska ha aktivitet,
- reflektions- eller dokumentationsuppgift som bättre hör hemma som valguide eller checklista.

### Hypotes 3: Inledningen behöver rensas från interna artefakter

Den maskinella inventeringen hittar en läsartextreferens till `docs/lookup-index.md`. Sådana interna filreferenser ska sannolikt inte finnas i boken. I PLAN-H bör de ersättas med läsarvända referenser, exempelvis `referenskapitlet` eller `snabbvalsguiderna i slutet av boken`.

### Hypotes 4: Kapiteltypologin är rätt, men mallarna behöver stramas åt

V4 har redan starka styrdokument för kapiteltyper. PLAN-H bör därför inte uppfinna en ny struktur från grunden. Den bör i stället:

- kontrollera hur väl varje kapitel följer sin typ,
- minska mekanisk rubrikanvändning,
- ta bort skolsektioner där de inte behövs,
- bevara praktiska tester där de ger verklig handboksnytta,
- stärka valhjälp, felsökning och snabbreferenser.

### Hypotes 5: PLAN-H bör bli en redaktionell saneringsplan, inte en ny innehållsplan

PLAN1–PLAN5 har framför allt utökat och strukturerat innehållet. PLAN-H bör sannolikt inte lägga till fler komponenter. Den bör fokusera på:

- ton,
- rubrikstruktur,
- sektionernas funktion,
- handbokskänsla,
- läsarvänd navigation,
- intern artefaktrensning,
- konsekvent användning av kapiteltypologi.

## Bedömningsmall för kommande kapitelblock

Varje kapitel i blockrapporterna ska bedömas enligt denna mall:

```markdown
### Kapitel X – Titel

- Kapiteltyp enligt projektet:
- Faktisk upplevelse:
- Handbokskänsla: 1–5
- Läroboksspår: låg / medel / hög
- Behov av redaktionell åtgärd: låg / medel / hög
- Risk vid ändring: låg / medel / hög

Observationer:
- ...

Konkreta PLAN-H-kandidater:
- ...
```

Varje blockrapport ska dessutom avslutas med:

```markdown
## Blockslutsats

## Återkommande mönster

## Föreslagna generella regler till PLAN-H

## Föreslagna kapiteltypsregler till PLAN-H

## Kapitelunika åtgärdskandidater

## Frågor att följa upp i senare steg
```

## Första rekommenderade arbetsordning

Den ursprungliga `[ANALYSPLAN]` behålls, men från och med detta steg ska blockrapporterna vara mer bevisbaserade. Det betyder:

1. Läs kapitlen i blocket.
2. Extrahera faktiska rubriker och återkommande formuleringar.
3. Bedöm varje kapitel separat.
4. Skriv blockslutsats.
5. Lista tydliga PLAN-H-kandidater.
6. Uppdatera analysloggen.
7. Packa ny projekt-zip.

## Avgränsning

Detta steg har inte ändrat:

- kapitelmanus,
- `build/book.md`,
- exporter,
- metadata,
- bokens innehåll.

Det har bara skapat analysunderlag för kommande steg.
