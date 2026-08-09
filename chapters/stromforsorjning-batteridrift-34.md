# 34. Strömförsörjning, batteridrift och robust konstruktion

## Matningsöversikt och riskbild
Många Arduino-projekt fungerar utmärkt på skrivbordet när de drivs via USB, men blir instabila så snart de får motorer, längre kablar, batterier, LED-strippar eller trådlös kommunikation. Det beror sällan på att koden plötsligt blivit sämre. Ofta beror det på att strömförsörjningen inte längre har marginaler.

Det här kapitlet handlar om övergången från bänktest till något som kan fungera under längre tid. Du behöver inte bli kraft-elektronikkonstruktör, men du behöver kunna läsa en enkel strömbudget, välja rimlig matning, förstå varför spänningsfall uppstår och känna igen tecken på brownout, brus och jordproblem.

Kapitlet knyter också ihop flera tidigare delar av boken. Sensorer behöver ofta stabil referens och låg störnivå. Displayer och LED kan ge korta strömtoppar. Motorer och reläer kan störa logiken. ESP-baserade kort kan dra mycket mer ström under Wi-Fi-aktivitet än när de bara blinkar en LED. Batteridrift kräver därför mer än att ansluta ett batteri till en Vin-pin.

## Förutsättningar

Du har redan mött flera begrepp som blir viktiga här:

- Logiknivå anger vilken spänning som används för digitala signaler.
- Gemensam jord krävs när två kretsar ska tolka varandras signaler.
- PWM och motorstyrning kan skapa snabba strömvariationer.
- Trådlösa kort kan ha tydliga strömtoppar.
- ADC-mätningar påverkas av brus, referensspänning och jorddragning.

I det här kapitlet använder vi begreppen systemspänning, strömbudget, regulator och energibudget. Skillnaden är viktig:

- **Systemspänning** handlar om vilken spänning delarna i projektet behöver.
- **Strömbudget** handlar om hur mycket ström de kan dra samtidigt.
- **Energibudget** handlar om hur länge ett batteri kan driva systemet.
- **Robust konstruktion** handlar om att systemet fortsätter fungera när verkligheten inte är lika ren som kopplingsschemat.

## USB är bekvämt men inte hela sanningen

USB är den vanligaste matningen i Arduino-projekt. Den är enkel, säker och gör att du kan programmera kortet samtidigt som det drivs. För enkla projekt räcker det långt.

Men USB har flera begränsningar:

- Strömmen kan vara begränsad av datorn, hubben eller kabeln.
- Tunna USB-kablar kan ge spänningsfall.
- Vissa kort har skyddskretsar, dioder eller regulatorer som gör att spänningen på 5 V- eller 3,3 V-sidan blir lägre än du tror.
- Motorer, reläer och LED-strippar kan kräva mer ström än kortets USB-väg bör belastas med.
- USB-matning är inte automatiskt ren, särskilt inte från billiga laddare eller brusiga datorportar.

En viktig regel är därför:

> USB är bra för utveckling, men det är inte automatiskt rätt slutmatning.

När ett projekt växer bör du börja rita matningen som en egen del av systemet, inte som något som bara “följer med” Arduino-kortet.

## Vanliga matningspunkter på Arduino-kompatibla kort

Olika kort har olika matningspinnar, men några mönster återkommer ofta.

| Matningspunkt | Typisk användning | Viktig begränsning |
|---|---|---|
| USB | Programmering och enkel drift | Begränsad ström, kabelberoende |
| Vin eller RAW | Extern inspänning till kortets regulator | Regulatorn kan bli varm och har begränsad ström |
| 5 V | 5 V-systemspänning på många klassiska kort | Kan vara utgång eller ingång beroende på kort |
| 3,3 V | Matning för 3,3 V-logik och sensorer | Ofta begränsad ström från kortets regulator |
| GND | Gemensam referens | Måste kopplas rätt mellan logik och extern matning |

Det är frestande att mata allt från kortets 5 V- eller 3,3 V-pin. Det fungerar för små sensorer, men det är ofta fel val för motorer, LED-strippar, servon och radiosystem med tydliga strömtoppar.

### Riskkontroll före inkoppling

Innan du matar ett projekt, kontrollera:

- Vilken inspänning får kortet enligt dokumentationen?
- Är 5 V-pinnen en säker ingång, en utgång eller båda?
- Hur mycket ström kan 3,3 V-regulatorn leverera?
- Behöver lasten separat matning?
- Behöver signalen nivåskiftas mellan 5 V och 3,3 V?
- Finns gemensam jord mellan styrkortet och den externa lasten?

Om du inte vet svaret bör du inte gissa med dyrare komponenter inkopplade.

## Regulatorer: linjär, buck, boost och buck-boost

En regulator gör om en spänning till en annan. I Arduino-projekt möter du oftast fyra typer.

| Typ | Vad den gör | När den passar | Typisk nackdel |
|---|---|---|---|
| Linjär regulator | Sänker spänning genom att bränna bort överskott som värme | Små strömmar, låg brusnivå, enkelhet | Blir varm vid stor spänningsskillnad och hög ström |
| Buck-regulator | Sänker spänning effektivt med switchteknik | Batteri eller adapter med högre spänning än systemet | Kan ge switchbrus |
| Boost-regulator | Höjer spänning | Batteri med lägre spänning än lasten behöver | Strömmen på batterisidan kan bli hög |
| Buck-boost-regulator | Höjer eller sänker spänning | Batterier vars spänning rör sig över och under målspänningen | Mer komplex och ibland dyrare |

En klassisk fallgrop är att mata Vin med hög spänning och samtidigt förvänta sig att kortets regulator ska driva flera servon eller LED-moduler. En linjär regulator kan då behöva omvandla mycket effekt till värme.

Effekten som regulatorn måste göra sig av med kan uppskattas så här:

```text
värmeeffekt = (inspänning - utspänning) × ström
```

Om du matar en linjär 5 V-regulator med 12 V och drar 300 mA blir värmen:

```text
(12 V - 5 V) × 0,3 A = 2,1 W
```

Det är mycket för en liten regulator på ett utvecklingskort. Den kan bli het, stänga ner eller göra projektet instabilt.

## Strömbudget: börja med lasten, inte kortet

En strömbudget är en enkel lista över hur mycket ström projektets delar behöver. Den behöver inte vara perfekt, men den ska fånga storleksordningen och de värsta fallen.

Exempel:

| Del | Typisk ström | Max eller topp | Kommentar |
|---|---:|---:|---|
| Mikrokontrollerkort | 50 mA | 250 mA | Wi-Fi kan ge toppar på vissa kort |
| BME280-sensor | låg | låg | Ofta försumbar i enkel budget |
| OLED-display | 10–30 mA | 50 mA | Beror på ljusstyrka och innehåll |
| Servo | 100–300 mA | 800 mA eller mer | Start/stall ger hög toppström |
| LED-strip, 10 RGB-pixlar | varierar | upp till cirka 600 mA | Full vit på hög ljusstyrka är värst |

Det viktiga är inte att siffrorna blir exakta på första försöket. Det viktiga är att du upptäcker när projektet inte längre är ett “Arduino-kort plus lite smådelar”, utan ett system där lasten dominerar.

### Enkel tumregel

Dela upp systemet i tre grupper:

- **Logik:** mikrokontroller, nivåskiftare, små IC-kretsar.
- **Mätning:** sensorer, ADC, referenser, analoga delar.
- **Laster:** motorer, servon, reläer, LED-strippar, solenoider, buzzers.

Logik och mätning vill ha stabil matning. Laster kan dra stora och snabba strömtoppar. Därför ska laster ofta ha egen matningsgren, även om jorden delas.

## Separat matning och gemensam jord

När du styr en motor, servo, LED-strip eller relämodul är det vanligt att använda separat matning för lasten. Arduino-kortet skickar styrsignal, men lasten får sin ström från en egen regulator eller adapter.

Principen är:

```text
Arduino GND  -----+
                  +-- gemensam jord
Extern GND   -----+

Arduino signal ----- styringång på drivmodul
Extern +V     ----- lastens plusmatning
```

Gemensam jord behövs för att styrsignalen ska ha samma referens på båda sidor. Utan gemensam jord kan mottagaren inte säkert veta vad Arduino menar med HIGH eller LOW.

Det finns undantag, till exempel optokopplade moduler och isolerade drivningar. Men i vanliga lågspänningsprojekt är gemensam jord nästan alltid nödvändig.

### När separat matning är särskilt viktig

Använd separat matning när projektet innehåller:

- servon
- DC-motorer
- stegmotorer
- solenoider
- reläspolar
- LED-strippar
- kraftiga buzzers
- värmeelement eller andra större laster
- trådlösa kort med tydliga strömtoppar tillsammans med andra laster

Det är bättre att planera separat matning från början än att felsöka slumpmässiga omstarter senare.

## Avkoppling och lokala kondensatorer

Avkopplingskondensatorer används för att ge kretsar lokal energireserv och minska störningar. De sitter nära den komponent som behöver stabil matning.

Två typer förekommer ofta:

- små keramiska kondensatorer, till exempel 100 nF nära IC-kretsar
- större elektrolyt- eller tantal-/polymerkondensatorer, till exempel 10–1000 µF nära laster eller matningsingångar

I Arduino-moduler finns ofta viss avkoppling redan på breakout-kortet. Men vid motorer, LED-strippar och längre kablar kan du ändå behöva extra kondensatorer.

### Praktiskt exempel

För en adresserbar LED-strip kan en större kondensator nära strippen minska risken för att första pixlarna flimrar eller att mikrokontrollern startar om när ljusstyrkan ändras snabbt.

För ett servo kan en separat matning med rimlig strömmarginal och kondensator nära servot göra större skillnad än ändringar i koden.

## Spänningsfall i kablar och breadboard

En koppling på breadboard ser ofta elektriskt kort ut, men vid högre ström kan även kablar, kontaktpunkter och breadboard-skenor ge spänningsfall. Detta blir tydligt med LED-strippar och motorer.

Symptom kan vara:

- displayen blinkar när motor startar
- mikrokontrollern startar om vid servorörelse
- sensordata får plötsliga spikar
- LED-strippen ändrar färg längst bort från matningen
- I2C-bussen slutar fungera när lasten aktiveras

Åtgärder:

- använd grövre ledare för lastström
- mata LED-strippar från flera punkter vid längre längder
- håll högströmsvägar borta från känsliga analoga signaler
- dra jord så att motorström inte delar samma tunna väg som ADC-referenser
- flytta från breadboard till skruvterminal, lödd prototyp eller distributionskort när strömmen ökar

Breadboard är utmärkt för logik och små sensorer. Det är inte alltid rätt plats för flera ampere, motorströmmar eller långvarig drift.

## Batteridrift: kapacitet är inte samma sak som tillgänglig ström

Batterier anges ofta i mAh. Det är lätt att tolka detta som “hur mycket ström batteriet kan ge”, men mAh beskriver kapacitet över tid under vissa villkor. Ett batteri kan ha hög kapacitet men ändå vara dåligt på att leverera stora toppströmmar.

Några vanliga batterityper i Arduino-projekt:

| Batterityp | Styrka | Begränsning |
|---|---|---|
| AA/AAA alkaliska | Enkla, lättillgängliga | Spänning faller, begränsad toppström |
| NiMH | Uppladdningsbara, tåligare mot ström | Lägre cellspänning än alkaliska |
| LiPo/Li-ion | Hög energitäthet, bra för portabla projekt | Kräver laddskydd, underspänningsskydd och respekt |
| USB powerbank | Enkel 5 V-källa | Kan stänga av vid låg last |
| 9 V-blockbatteri | Bekvämt fysiskt format | Ofta dåligt val för motorer och längre drift |

9 V-blockbatteriet är en klassisk Arduino-fälla. Det kan fungera för små tester, men är ofta olämpligt för motorer, servon, LED-strippar och projekt som ska köras länge.

### Enkel batteriberäkning

Om projektet i genomsnitt drar 100 mA och batteriet har användbar kapacitet på 2000 mAh blir den idealiserade drifttiden:

```text
2000 mAh / 100 mA = 20 timmar
```

I verkligheten blir tiden ofta kortare på grund av regulatorförluster, temperatur, batteriets urladdningskurva och att kapacitet anges vid vissa testförhållanden.

Därför bör du se beräkningen som en första uppskattning, inte som ett löfte.

## Sleep-lägen och energibudget

För batteridrivna projekt är genomsnittlig ström viktigare än strömmen i aktivt läge. Ett kort som drar mycket under en kort Wi-Fi-sändning kan ändå fungera länge om det sover resten av tiden.

Tänk på ett projekt i tre lägen:

| Läge | Exempel | Fråga |
|---|---|---|
| Aktivt | Läser sensor, uppdaterar display, skickar data | Hur länge är systemet vaket? |
| Väntar | Låg aktivitet men inte riktig sleep | Kan väntetiden kortas eller göras sovande? |
| Sleep | Mikrokontroller och sensorer i lågförbrukning | Vad väcker systemet igen? |

Pseudologiken kan se ut så här:

```cpp
void loop() {
  wakeSensors();
  Measurement data = readSensors();

  if (shouldReport(data)) {
    connectNetwork();
    sendMeasurement(data);
    disconnectNetwork();
  }

  prepareSensorsForSleep();
  enterSleepForMinutes(5);
}
```

Detta är inte komplett kod för ett visst kort. Sleep-funktioner skiljer sig mycket mellan AVR, ESP32, RP2040 och andra plattformar. Poängen är arbetssättet: gör det aktiva arbetet kort, stäng av det som inte behövs och välj väckningsstrategi medvetet.

### Glöm inte kringkomponenterna

Ett vanligt misstag är att optimera mikrokontrollerns sleep-läge men lämna sensorer, regulatorer, lysdioder och nivåskiftare aktiva. Då blir resultatet sämre än väntat.

Kontrollera därför:

- kortets power LED
- USB-seriechip
- spänningsregulatorns egenförbrukning
- sensorns sleep-läge
- pull-up-motstånd som drar konstant ström
- spänningsdelare som ligger inkopplad hela tiden
- moduler som saknar riktig avstängning

För riktigt låg förbrukning kan ett bare module- eller specialkort vara bättre än ett bekvämt utvecklingskort.

## Brownout, omstarter och märkliga fel

Brownout betyder att spänningen sjunker under vad mikrokontrollern behöver för stabil drift. Vissa kort har brownout-detektering och startar om. Andra kan bete sig mer otydligt.

Tecken på strömproblem:

- kortet startar om när Wi-Fi aktiveras
- seriell monitor visar startmeddelanden mitt i programmet
- servon rycker och koden verkar “hänga sig”
- I2C-enheter försvinner sporadiskt
- mätvärden får hopp när en last slås på
- LED blinkar till när motor startar
- problemet försvinner när du kopplar bort lasten

Felsökningsstrategi:

1. Koppla bort alla laster.
2. Kör bara mikrokontroller och seriell loggning.
3. Lägg till sensorer en i taget.
4. Lägg till display.
5. Lägg till en last i taget med separat matning.
6. Mät spänningen vid kortet, inte bara vid nätadaptern.
7. Mät spänningen under händelsen som orsakar felet.

Mät alltid där problemet uppstår. En adapter kan visa 5,0 V medan kortet bara får 4,4 V under en servotopp.

## Nätspänning och säkerhetsgränser

Arduino-projekt bör normalt hålla sig till lågspänning. Att styra nätspänning kräver kunskap, rätt kapsling, säkringar, isolationsavstånd och ofta behörighet eller gällande elsäkerhetskrav beroende på miljö.

I den här boken är huvudprincipen:

> Låt Arduino styra lågspänningssidan. Använd färdiga, godkända produkter för nätspänning när det är möjligt.

Exempel på säkrare vägval:

- Använd lågspännings-LED i stället för att bygga egen nätspänningsdimmer.
- Använd färdig smart plug eller certifierad reläenhet i stället för öppen nätspänningskoppling.
- Håll experiment på breadboard till lågspänning.
- Kapsla alltid system som kan kortslutas eller beröras.
- Använd säkring där en strömkälla kan leverera farligt hög ström.

En USB-powerbank är ofta en mycket bättre experimentkälla än en öppen nätadapterkoppling.

## Riskkontroll: strömbudget och svag matning

Använd den här kontrollen när ett projekt startar om, beter sig instabilt eller ska köras längre än ett kort skrivbordstest.

### Kontrollera matningskartan

Skriv eller rita kort:

- var plusmatning kommer in
- vilka delar som drivs från kortet
- vilka delar som har separat matning
- var jordpunkterna möts
- vilka pinnar som bara är styrsignaler

Exempel:

| Del | Matning | Ungefärlig ström | Kommentar |
|---|---|---|---|
| Arduino-kort | USB eller 5 V-regulator | 30-80 mA | varierar mellan kort |
| OLED | 3,3 V eller 5 V | 10-30 mA | låg men inte noll |
| Servo | separat 5 V | 200-800 mA topp | ska normalt inte matas från kortet |
| Sensor | 3,3 V eller 5 V | 1-20 mA | kontrollera datablad |

### Mät på rätt plats

Mät spänningen där lasten faktiskt sitter, inte bara vid matningskällan. Om spänningen sjunker när servo, motor, radio eller LED-strip aktiveras är problemet ofta matning, kabel, breadboard eller jorddragning.

### Testa separat lastmatning

För laster med ryckig eller hög ström är separat matning ofta det första praktiska testet. Koppla då alltid gemensam jord mellan lastmatning och mikrokontroller, om inte kopplingen uttryckligen är galvaniskt isolerad.

### Tecken på svag matning

- Kortet startar om när lasten aktiveras.
- Seriell monitor tappar kontakt.
- Sensordata får plötsliga orimliga värden.
- Displayen blinkar eller fryser.
- Wi-Fi- eller radiomoduler fungerar bara ibland.

## Kodexempel: logga spänningsrelaterade händelser

Det här kodexemplet visar ett arbetssätt för att upptäcka symptom. Det mäter inte matningsspänningen direkt på alla kort, men det loggar tidpunkter, lastläge och ett analogt mätvärde. Du kan använda samma struktur när du felsöker spänningsfall eller störningar.

```cpp
const int loadPin = 9;
const int sensePin = A0;

unsigned long lastToggleMs = 0;
bool loadEnabled = false;

int readAverageAnalog(int pin, int samples) {
  long total = 0;

  for (int i = 0; i < samples; i++) {
    total += analogRead(pin);
    delay(2);
  }

  return total / samples;
}

void setup() {
  pinMode(loadPin, OUTPUT);
  digitalWrite(loadPin, LOW);

  Serial.begin(115200);
  delay(500);

  Serial.println("Power stability experiment");
  Serial.println("time_ms,load,analog_value");
}

void loop() {
  const unsigned long now = millis();

  if (now - lastToggleMs >= 3000) {
    lastToggleMs = now;
    loadEnabled = !loadEnabled;
    digitalWrite(loadPin, loadEnabled ? HIGH : LOW);
  }

  const int value = readAverageAnalog(sensePin, 16);

  Serial.print(now);
  Serial.print(",");
  Serial.print(loadEnabled ? "on" : "off");
  Serial.print(",");
  Serial.println(value);

  delay(250);
}
```

Använd inte detta som direkt styrning av en motor eller större last utan drivkrets. `loadPin` ska styra en säker last, en drivmodul eller ett testläge.

## Riskkontroll före längre drift

Innan ett projekt lämnas inkopplat, batteridrivet eller utan ständig uppsikt bör matningen kontrolleras som ett eget delsystem.

- Kontrollera polaritet innan batteri eller adapter ansluts.
- Kontrollera att regulatorn har marginal för både inspänning och lastström.
- Kontrollera att kablar, kontakter och breadboard inte bär mer ström än de bör.
- Kontrollera temperatur på regulator, batteri, laddmodul och drivare efter några minuters drift.
- Kontrollera vad som händer när största lasten startar.
- Kontrollera att batteritypen laddas med rätt laddare och skydd.
- Kontrollera att projektet inte kan kortslutas lätt i kapsling eller transport.

Ett projekt som fungerar på skrivbordet kan fortfarande behöva bättre matning innan det blir robust.

## Vanliga misstag

- **Misstag:** Att driva servo eller motor direkt från Arduino-kortets 5 V-pin.
  - **Varför det händer:** Servot har tre kablar och ser ut som en enkel modul.
  - **Hur man undviker det:** Använd separat matning med tillräcklig ström och gemensam jord.

- **Misstag:** Att mata Vin med hög spänning och samtidigt belasta kortets regulator hårt.
  - **Varför det händer:** Vin ser ut som en allmän matningsingång.
  - **Hur man undviker det:** Räkna på regulatorns värme och använd extern buck-regulator när lasten kräver mer ström.

- **Misstag:** Att bara mäta spänningen vid adaptern.
  - **Varför det händer:** Det känns naturligt att kontrollera strömkällan.
  - **Hur man undviker det:** Mät även vid kortet och vid lasten, särskilt när lasten startar.

- **Misstag:** Att optimera sleep-kod men glömma kringkomponenter.
  - **Varför det händer:** Kodperspektivet dominerar.
  - **Hur man undviker det:** Mät hela systemet och kontrollera regulatorer, sensorer, lysdioder och spänningsdelare.

- **Misstag:** Att dra all jord genom tunna breadboard-skenor.
  - **Varför det händer:** Breadboarden gör det lätt att tänka på jord som en perfekt punkt.
  - **Hur man undviker det:** Separera högströmsvägar från känslig logik och använd stabilare koppling vid högre ström.

- **Misstag:** Att underskatta startström och toppström.
  - **Varför det händer:** Datablad och exempel fokuserar ofta på normal drift.
  - **Hur man undviker det:** Planera marginaler och testa värsta fall: motorstart, full ljusstyrka, Wi-Fi-sändning och reläslag.

## Felsökning

- Om kortet startar om: mät spänningen på kortets matningspinne samtidigt som lasten aktiveras.
- Om Wi-Fi, display eller motor gör systemet instabilt: kontrollera strömtoppar och lägg till lokal avkoppling nära den del som drar mycket ström.
- Om batteritiden blir mycket kortare än väntat: räkna på faktisk ström i drift, sleep och viloläge för alla moduler.
- Om sensormätningar blir brusiga: kontrollera regulator, jorddragning, kablar och om lasten delar samma matningsväg.
- Om regulatorn blir varm: kontrollera inspänning, lastström och förlusteffekt, särskilt för linjära regulatorer.

## Snabb sammanfattning

- Strömförsörjning är en systemfråga, inte bara en kabel till Arduino-kortet.
- USB är bekvämt för utveckling men inte alltid rätt slutmatning.
- Laster som motorer, servon, reläer och LED-strippar bör ofta ha separat matning.
- Gemensam jord krävs i vanliga lågspänningssystem där Arduino styr externa drivmoduler.
- Linjära regulatorer kan bli varma när spänningsskillnad och ström är stora.
- Buck- och boost-regulatorer är ofta bättre för batteri och större laster.
- Batterikapacitet i mAh säger inte hela sanningen om toppström och verklig drifttid.
- Sleep-lägen hjälper bara om hela systemets energiförbrukning hanteras.
- Brownout och omstarter är ofta tecken på spänningsfall, störningar eller för svag matning.
- Mät spänningen där problemet uppstår, inte bara vid strömkällan.

## Säkerhetsruta: batterier och regulatorer ska behandlas som energikällor

Även små batterier kan leverera tillräckligt med ström för att skada komponenter, smälta ledare eller skapa värme. LiPo-celler kräver särskild respekt: använd laddare och skyddskretsar som är avsedda för celltypen.

Testa ny strömförsörjning med strömbegränsning när det är möjligt. Koppla in lasten stegvis och kontrollera spänning, polaritet och temperatur innan projektet lämnas utan uppsikt.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | USB, batteri, 3,3 V, 5 V eller annan systemspänning |
| Typiskt gränssnitt | Matning snarare än databuss |
| Välj när | projektet ska bli robust, batteridrivet eller fältdugligt |
| Välj inte när | det bara är ett kort bänkexperiment med USB |
| Vanliga fel | brownout, fel polaritet, för svag regulator, jordloopar |
| Alternativ att överväga | USB-matning, buck/boost, LiPo-modul, laboratorieaggregat |

Använd referensrutan som en snabb kontroll innan du bygger första testet. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

Snabbt matningsval:

- Välj **USB** bara när lasten är liten och projektet är ett enkelt bänktest.
- Välj **separat 5 V- eller 6 V-matning** när servon, motorer eller LED-strippar ingår.
- Välj **buck-regulator** när högre inspänning ska bli stabil lägre systemspänning.
- Välj **boost-regulator** när batterispänningen kan ligga under den spänning projektet behöver.
- Välj **laboratorieaggregat** när du felsöker okänd strömförbrukning eller misstänkta spänningsdippar.

## Relaterat

- När lasten styrs från en pinne, relä, MOSFET eller drivkrets, kontrollera först kapitel 21 och 31.
- När sensorer eller ADC-värden driver iväg, jämför med kapitel 6 och kapitel 33 innan du byter sensor.
- När projektet startar om eller bara fungerar på USB, använd felsökningsordningen i kapitel 35.
- När projektet ska bli återanvändbar modul eller sensorstation, gå vidare till kapitel 36 och 37.
