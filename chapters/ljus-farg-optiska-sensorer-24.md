# 24. Ljus, färg, UV och optiska sensorer

## Sensoröversikt
Ljus är en av de mest användbara mätstorheterna i Arduino-projekt. En enkel ljussensor kan styra en nattlampa, visa om en kapsling är öppen, mäta om en display är läsbar, följa dygnsvariationer eller fungera som en del av ett optiskt gränssnitt. Mer avancerade optiska sensorer kan skilja mellan färger, känna av reflektion, upptäcka avbrott i en ljusstråle eller ge en uppskattning av UV-exponering.

Samtidigt är ljusmätning lätt att missförstå. En sensor mäter inte “hur ljust det är” i allmänhet. Den mäter ljus som träffar just sensorns aktiva yta, med just den spektrala känslighet sensorn råkar ha, i just den vinkel och placering där den sitter. En LDR, en digital luxsensor, en färgsensor och en IR-reflektionssensor kan alla beskrivas som ljussensorer, men de svarar på olika frågor.

Det här kapitlet hjälper dig att välja mellan vanliga ljus- och optiska sensorer:

- LDR och andra enkla analoga ljussensorer
- fotodioder och fototransistorer
- digitala luxsensorer som BH1750, VEML7700 och TSL2591
- färgsensorer som TCS34725
- APDS-9960/GY-9960-moduler som kombinerar färg, ljus, närhet och enkla gester
- UV-sensorer som VEML6075
- IR-reflektionssensorer, optiska brytare, enkla ljusbarriärer och IR-mottagare för fjärrkontroll

Målet är inte att göra optisk mätteknik till ett eget specialistområde. Kapitlet fungerar som praktiskt stöd när du behöver välja mellan relativ ljusmätning, luxmätning, färgmätning, UV-mätning och optisk detektion, och när placering, vinkel, spektral känslighet och omgivningsljus påverkar resultatet. Målet är att du ska kunna bygga Arduino-lösningar där ljus, färg eller optisk närvaro används på ett medvetet sätt, med rimliga antaganden och en tydlig valguide.

## Förutsättningar

Det här kapitlet bygger på flera tidigare kapitel:

- kapitel 4 om spänning, ström, resistorer och spänningsdelare
- kapitel 6 om analog läsning, filtrering och mätosäkerhet
- kapitel 7 om `millis()` och icke-blockerande uppdatering
- kapitel 9 om I2C och bussfelsökning
- kapitel 17 och 18 om LED, RGB-LED och adresserbara LED
- kapitel 22 om displayer och enkla användargränssnitt
- kapitel 23 om sensorprofil, placering, kalibrering och rimlighetskontroll

Ljusmätning är särskilt bra för att träna på skillnaden mellan en elektronisk signal och en verklig tolkning. Två sensorer kan ge olika värden trots att båda fungerar. Det kan bero på riktning, spektrum, avstånd, kapsling, förstärkning, upplösning eller hur biblioteket räknar om rådata.

En bra startregel är:

> Fråga först vad projektet behöver veta: ljusare eller mörkare, ungefärlig luxnivå, färg, UV-exponering eller om ett objekt bryter en optisk väg.

## Vad menas med optisk sensor?

En optisk sensor reagerar på ljus. Det kan vara synligt ljus, infrarött ljus, ultraviolett ljus eller en kombination. I Arduino-projekt används optiska sensorer ofta på fyra olika sätt.

| Behov | Typisk sensortyp | Typiskt gränssnitt | Exempel på användning |
|---|---|---|---|
| Relativ ljusnivå | LDR eller fototransistor | Analog eller digital modul | Nattläge, skymningsdetektion |
| Mätning i lux | Digital ljussensor | I2C | Loggning av belysning, displayanpassning |
| Färg eller färgtemperatur | RGB/färgsensor | I2C | Sortering, enkel färgklassning |
| UV-indikation | UV-sensor | I2C eller analog modul | UV-varning, experiment med solljus |
| Reflektion eller avbrott | IR-reflektionssensor eller optisk brytare | Digital eller analog | Linjeföljare, räknare, närvarodetektion |

Den viktigaste skillnaden är om du vill mäta ljus som en fysisk storhet eller bara använda ljus som en signal.

En skymningssensor behöver kanske bara veta om det är mörkt nog för att tända en lampa. En logger för arbetsbelysning behöver mer stabila värden och en definierad enhet. En färgsorterare behöver kontrollerad belysning och kort avstånd till objektet. En optisk brytare behöver snabb och pålitlig detektion, inte vackra luxvärden.

## LDR: den enkla relativa ljussensorn

En LDR, light-dependent resistor, är ett motstånd vars resistans ändras med ljusnivån. Den är billig, lätt att koppla och vanlig i startkit. Den används normalt i en spänningsdelare där Arduino läser mittpunkten med `analogRead()`.

En LDR är bra när du behöver en enkel relativ ljusnivå:

- mörkt eller ljust
- dag eller natt
- täckt eller inte täckt
- ungefärlig förändring över tid

Den är sämre när du behöver:

- snabb respons
- god noggrannhet
- stabilitet mellan exemplar
- definierad luxmätning
- bra kontroll över spektral känslighet

En LDR är alltså ofta rätt val för ett inspirerande experiment, men sällan rätt val för en mätare där värdet ska betyda samma sak i flera exemplar eller miljöer.

## Koppla LDR som spänningsdelare

En vanlig koppling är:

- ena sidan av LDR till 3,3 V eller 5 V
- andra sidan av LDR till analog ingång
- ett fast motstånd från analog ingång till GND

Då blir analogvärdet högre när LDR-resistansen minskar med mer ljus. Om du byter plats på LDR och motstånd blir riktningen omvänd.

Typiska startvärden för det fasta motståndet är 10 kΩ eller 47 kΩ, men rätt värde beror på LDR, ljusnivå och vad du vill mäta. För skymningsdetektion räcker ofta ett experimentellt val. För ett mer reproducerbart system bör du mäta råvärden i den faktiska miljön.

Ett vanligt misstag är att skriva kod som antar att 0 betyder mörkt och 1023 betyder ljust. På ett annat kort kan ADC-upplösningen vara annorlunda, och med en annan koppling kan riktningen vara omvänd.

## Exempel: läsa LDR utan att låsa programmet

Det här exemplet visar en enkel struktur för återkommande analog ljusmätning. Det använder filtrering och hysteresis så att en status-LED inte blinkar snabbt runt gränsen.

```cpp
const int lightPin = A0;
const int statusLedPin = 9;

const unsigned long sampleIntervalMs = 100;

const int darkThreshold = 320;
const int brightThreshold = 380;

unsigned long lastSampleMs = 0;
float filteredLight = 0.0;
bool isDark = false;

void setup() {
  pinMode(statusLedPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  unsigned long now = millis();

  if (now - lastSampleMs >= sampleIntervalMs) {
    lastSampleMs = now;

    int raw = analogRead(lightPin);

    if (filteredLight == 0.0) {
      filteredLight = raw;
    } else {
      filteredLight = filteredLight * 0.85 + raw * 0.15;
    }

    if (!isDark && filteredLight < darkThreshold) {
      isDark = true;
    }

    if (isDark && filteredLight > brightThreshold) {
      isDark = false;
    }

    digitalWrite(statusLedPin, isDark ? HIGH : LOW);

    Serial.print("raw=");
    Serial.print(raw);
    Serial.print(" filtered=");
    Serial.print(filteredLight);
    Serial.print(" isDark=");
    Serial.println(isDark ? "yes" : "no");
  }
}
```

Notera att gränsvärdena i exemplet inte är universella. De ska mätas fram med seriell plotter eller logg i den miljö där projektet används.

## Fotodiod och fototransistor

Fotodioder och fototransistorer reagerar ofta snabbare än LDR och används när du behöver mer kontrollerad optisk detektion. I Arduino-sammanhang ser du dem ofta som färdiga moduler snarare än rena komponenter.

En fototransistor kan användas för:

- optisk brytare
- reflektionssensor
- pulsräkning
- enkel IR-detektion
- ljusbarriär

Den kan kopplas analogt eller digitalt beroende på modul. Många moduler har en justerbar komparator och ger en digital utgång när ljusnivån passerar en tröskel. Det är praktiskt, men du tappar information om hur nära tröskeln signalen ligger.

Välj analog läsning när du vill förstå signalen. Välj digital modul när du bara behöver ett robust ja/nej efter att tröskeln är justerad.

## Digitala luxsensorer

Digitala ljussensorer är ofta bättre än LDR när du vill ha stabilare och mer meningsfulla mätvärden. De kommunicerar ofta via I2C och ger antingen råvärden eller beräknade luxvärden.

Vanliga exempel i Arduino-projekt är:

- BH1750
- VEML7700
- TSL2561 och TSL2591
- MAX44009 och liknande ljussensorer

En digital luxsensor är ofta rätt val när projektet behöver:

- jämförbara värden över tid
- bättre dynamiskt område
- mindre analogt brus
- enkel I2C-koppling
- luxvärde snarare än bara rå ADC-nivå

Samtidigt ska luxvärden inte övertolkas. Sensorernas optiska respons är inte identisk med mänskligt seende, placeringen påverkar mycket och kapsling kan ändra mätningen kraftigt.

## BH1750, VEML7700 och TSL2591

BH1750 är vanlig i billiga moduler och passar enkla luxmätningar. Den är lätt att använda, men kan vara mindre flexibel än mer avancerade sensorer.

VEML7700 är en modern ambient light sensor med I2C-gränssnitt. Den är ett bra val när du vill ha en kompakt digital ljussensor med bättre kontroll än en enkel LDR. Enligt Vishays datablad har VEML7700 I2C-stöd för standard och fast mode upp till 400 kHz, vilket gör den enkel att använda i vanliga Arduino-I2C-system.

TSL2591 är en mer avancerad digital ljussensor med stort dynamiskt område. Adafruits guide beskriver den som en high dynamic range digital light sensor med I2C och konfigurerbar gain och integrationstid. Den passar bättre när ljusnivån kan variera mycket, till exempel mellan mörka inomhusmiljöer och starkare belysning.

I praktiken kan valet se ut så här:

| Sensor | Välj när | Var försiktig med |
|---|---|---|
| LDR | Du behöver billig relativ ljusnivå | Dålig reproducerbarhet och långsam respons |
| BH1750 | Du vill ha enkel luxmätning via I2C | Begränsat omfång och varierande modulkvalitet |
| VEML7700 | Du vill ha modern digital ambient light sensor | Kontrollera matning, bibliotek och kapsling |
| TSL2591 | Du behöver stort dynamiskt område | Luxvärdet kan ändå behöva tolkas med försiktighet |

## Färgsensorer

En färgsensor mäter inte färg på samma sätt som ett mänskligt öga. Den mäter normalt ljus i flera kanaler, ofta röd, grön, blå och clear. Ett bibliotek kan sedan ge råvärden, färgtemperatur, lux eller enkla RGB-tolkningar.

TCS34725 är en vanlig färgsensor i makerprojekt. Den har RGB- och clear-kanaler, I2C-gränssnitt och används ofta på breakout boards med inbyggd vit LED. Den inbyggda belysningen är viktig: färgmätning blir mycket mer stabil när ljuskällan, avståndet och vinkeln är kontrollerade.

Färgsensorer passar för:

- enkel färgklassificering
- sortering av färgade objekt
- detektion av färgmarkeringar
- experiment med ljus och material
- kalibrerad jämförelse mellan ett fåtal kända färger

De passar sämre för:

- exakt färgmätning utan kalibrering
- varierande avstånd och belysning
- blanka eller transparenta material
- miljöer där omgivningsljuset ändras mycket

Ett robust färgprojekt behöver ofta mer mekanik än man först tror. Sensorn bör sitta på fast avstånd från objektet, ha skärmad belysning och kalibreras mot exempel på de färger som ska skiljas åt.

## Färgmätning som klassificering

I Arduino-projekt är det ofta bättre att tänka “klassificering” än “exakt färg”. Frågan blir då inte: vilken exakt RGB-färg är objektet? Frågan blir: liknar objektet mest röd, grön, blå, gul eller okänd i just vår uppställning?

Ett enkelt arbetssätt är:

1. Läs råvärden för röd, grön, blå och clear.
2. Normalisera RGB-värdena mot clear eller totalnivå.
3. Samla exempeldata för varje färgklass.
4. Sätt trösklar eller använd närmaste referensvärde.
5. Lägg till klassen “okänd” när värdena inte matchar tillräckligt bra.

Detta är mer praktiskt än att försöka översätta sensorns råvärden till en perfekt färgmodell.

## APDS-9960-baserade gest-, färg- och närhetssensorer

APDS-9960 är en vanlig optisk sensorkrets som ofta säljs på breakoutkort under namn som APDS-9960 eller GY-9960. Den kan användas för att mäta färg, omgivande ljus och närhet. Vissa moduler och bibliotek använder också sensorns riktningsdata för enkla handgester, till exempel svep åt vänster, höger, upp eller ned.

Det viktiga är att se modulen som en liten I2C-baserad optisk sensor, inte som en magisk gestkamera. Den mäter ljus och reflektion nära sensorn. Gestdetekteringen fungerar bäst när handen rör sig på ungefär rätt avstånd, i kontrollerad belysning och med sensorn placerad så att rörelsen faktiskt passerar över mätområdet.

APDS-9960/GY-9960 passar när du vill:

- prova geststyrning utan kamera
- känna av om en hand eller ett objekt är nära sensorn
- läsa ungefärlig färg eller ljusnivå via I2C
- bygga ett litet användargränssnitt där handen kan byta läge utan fysisk knapp
- kombinera närhet och enkel färginformation i samma modul

Se upp med:

- att modulen ofta behöver ett bibliotek
- att gestdetektering påverkas starkt av avstånd, omgivningsljus och mekanisk placering
- att breakoutkort kan ha olika spänningskrav och olika nivåskiftning
- att färgmätning fortfarande kräver kontrollerad belysning och kalibrering
- att sensorn inte ersätter kamera, exakt avståndsmätare eller robust industriell närvarodetektion

En bra första testsketch bör bara visa råa värden för ljus, färg och närhet i seriell monitor. När du vet att sensorn svarar stabilt kan du lägga till gestbibliotekets tolkning och koppla gesterna till ett enkelt tillstånd, till exempel nästa vy, föregående vy eller pausa/starta.

## UV-sensorer

UV-sensorer mäter ultraviolett ljus, ofta med fokus på UVA och UVB eller en beräknad UV-indexliknande uppskattning. VEML6075 är ett exempel på en I2C-baserad UVA/UVB-sensor som används i Arduino- och makerprojekt. Adafruits VEML6075-breakout beskrivs som en sensor för UVA, UVB och UV-index med I2C och stöd för både Arduino och CircuitPython.

UV-mätning kräver extra försiktighet i tolkningen. En enkel modul ger inte automatiskt samma kvalitet som en kalibrerad UV-mätare. Kapsling, glas, plast, moln, vinkel mot solen och skuggning påverkar resultatet. Många material släpper igenom synligt ljus men blockerar stora delar av UV-ljuset.

Välj UV-sensor när:

- du vill jämföra UV-nivåer under olika förhållanden
- du vill bygga en pedagogisk UV-indikator
- du vill logga trend snarare än exakt medicinsk eller säkerhetskritisk exponering

Välj inte enkel UV-modul som enda beslutsunderlag för hälsa, skydd eller certifierad mätning.

## IR-reflektion och optiska brytare

IR-reflektionssensorer använder ofta en IR-LED och en fototransistor. Sensorn skickar ut infrarött ljus och mäter hur mycket som reflekteras tillbaka. De används i linjeföljare, objektdetektion och enkla avståndsnära tillämpningar.

Optiska brytare, eller slot sensors, har en sändare och mottagare på var sin sida av en springa. När ett objekt bryter ljusstrålen ändras signalen. De är användbara för:

- räkna rotationer eller pulser
- upptäcka om en flik passerar
- känna av mekaniska ändlägen
- bygga enkla hastighetsmätare

IR-reflektion påverkas starkt av:

- objektets färg och material
- avstånd
- vinkel
- omgivande IR-ljus
- om sensorn är skärmad

En svart matt yta kan ge mycket svag reflektion. En blank yta kan ge stark men vinkelberoende reflektion. Därför bör IR-reflektionssensorer testas med de faktiska materialen från projektet.

## IR-fjärrkontroll och mottagarmoduler

En IR-mottagarmodul, till exempel TSOP- eller VS1838B-liknande moduler, används inte främst för att mäta ljus. Den är byggd för att ta emot modulerade signaler från en IR-fjärrkontroll. Det gör den till en praktisk inmatningsmodul snarare än en allmän ljussensor.

IR-fjärrkontroll passar bra när projektet ska styras på avstånd men ändå står synligt, till exempel:

- byta vy på en display
- starta och stoppa ett experiment
- välja läge i en enkel meny
- styra LED-effekter eller ljudsignaler
- återanvända en billig fjärrkontroll i ett hobbyprojekt

En sådan mottagare har ofta tre anslutningar: VCC, GND och signal. Signalpinnen kopplas till en digital ingång. Själva avkodningen görs normalt med ett bibliotek, eftersom fjärrkontroller använder pulserade protokoll snarare än vanlig HIGH/LOW-logik.

Det viktiga är att inte behandla IR-fjärr som säker eller robust radiokommunikation. Den kräver ofta fri sikt, kan störas av starkt ljus och fungerar olika beroende på fjärrkontroll, protokoll och mottagarmodul. Okända knappkoder bör ignoreras, och projektet bör ha ett säkert standardläge om fjärrsignalen uteblir.

| Fråga | Praktiskt svar |
|---|---|
| Är det en ljussensor? | Nej, inte i vanlig mening. Den är en mottagare för modulerad IR-kommunikation. |
| Behöver jag ADC? | Nej, signalen läses normalt digitalt via bibliotek. |
| Krävs fri sikt? | Ja, i de flesta praktiska byggen. |
| Passar det som menyinmatning? | Ja, särskilt tillsammans med displaykapitlet. |
| Passar det för säkerhetskritisk styrning? | Nej, använd robustare kommunikation och failsafe-logik. |

Om du använder IR-fjärr som del av ett lokalt användargränssnitt hör valet också ihop med kapitel 22. Om du behöver längre räckvidd, kommunikation genom väggar eller dubbelriktad data är alternativen i kapitel 9 bättre.

## Analog eller digital optisk modul?

Många optiska moduler har både analog och digital utgång. Den analoga utgången visar ungefär hur stark signalen är. Den digitala utgången går via en komparator och blir HIGH eller LOW beroende på en potentiometerinställning.

| Val | Fördel | Nackdel |
|---|---|---|
| Analog utgång | Du ser signalens styrka och kan filtrera i kod | Kräver ADC och egen tröskellogik |
| Digital utgång | Enkel ja/nej-signal | Tröskeln är ofta svår att dokumentera och reproducera |
| I2C-sensor | Stabilare data och konfiguration | Kräver bibliotek, adress och bussfelsökning |
| Ren komponent | Maximal kontroll | Kräver mer analog design |

För experiment rekommenderas ofta att börja analogt om modulen erbjuder det. När du har förstått signalen kan du avgöra om digital tröskel räcker.

## Placering, kapsling och geometri

Optiska sensorer påverkas mycket av geometri. Det räcker inte att koppla rätt pinnar. Du behöver också tänka på hur ljuset når sensorn.

Frågor att dokumentera:

- Sitter sensorn riktad uppåt, åt sidan eller mot ett objekt?
- Är sensorn skuggad av kapslingen?
- Finns ett fönster framför sensorn, och släpper det igenom relevant våglängd?
- Kan LED eller display på samma enhet lysa direkt på sensorn?
- Ändras avståndet till objektet?
- Är ytan matt, blank, transparent eller färgad?
- Behöver sensorn skärmas från omgivningsljus?

En ljussensor för displayanpassning bör ofta sitta så att den ser samma ljusmiljö som användaren, men inte direkt träffas av displayens eget ljus. En färgsensor bör ofta ha kontrollerad belysning och fast avstånd. En IR-reflektionssensor bör testas med mekaniken på plats, inte bara i handen över ett skrivbord.

## Filtrering och hysteresis för ljus

Ljusvärden varierar. De kan ändras snabbt när någon passerar, när en lampa flimrar, när solen går i moln eller när sensorn råkar få en reflex. Därför bör ljusdata ofta filtreras innan den styr ett beslut.

Vanliga strategier:

- glidande medelvärde
- exponentiellt filter
- medianfilter för korta spikar
- hysteresis för tröskelbeslut
- minsta tid innan tillstånd får ändras

För skymningsstyrning är hysteresis nästan alltid viktig. Du vill inte att en lampa ska tända och släcka flera gånger när ljusnivån ligger nära gränsen.

## Typiskt mönster: ljuströskel med hysteresis

Många optiska projekt behöver inte exakt luxvärde. De behöver ett stabilt beslut: mörkt eller ljust, nattläge eller dagläge, objekt syns eller syns inte. Då är en tröskel med hysteresis ofta bättre än att reagera direkt på varje nytt råvärde.

Ett robust mönster består av fyra delar:

- filtrera råvärdet lätt,
- använd en övre och en nedre tröskel,
- ändra tillstånd först när värdet passerar rätt gräns,
- använd tillståndet till nattläge, dimning, status eller optisk detektering.

En enkel tillståndsmodell kan se ut så här:

| Tillstånd | Byt till annat tillstånd när |
|---|---|
| `DARK` | filtrerat värde går över den övre tröskeln |
| `BRIGHT` | filtrerat värde går under den nedre tröskeln |

Skillnaden mellan trösklarna är det som hindrar fladder när ljuset ligger nära gränsen.

## Exempel: sensorstyrd RGB-status

Det här mönstret använder en LDR eller analog ljussensor för att styra färg på en RGB-LED. Poängen är inte att skapa exakt luxmätning, utan att bygga ett robust mönster för relativ ljusnivå.

### Det här används i exemplet

- Arduino-kompatibelt kort
- LDR eller analog ljussensormodul
- fast motstånd, exempelvis 10 kΩ, om du använder lös LDR
- RGB-LED med tre seriemotstånd eller liten RGB-modul
- kopplingskablar och breadboard

### Koppling

Använd en spänningsdelare för LDR:

- LDR till 3,3 V eller 5 V enligt kortets logiknivå
- fast motstånd till GND
- mittpunkten till `A0`

Koppla RGB-LED med seriemotstånd till tre PWM-pinnar. Kontrollera om din RGB-LED har gemensam anod eller gemensam katod, eftersom logiken blir omvänd.

### Kod

Exemplet antar gemensam katod. Anpassa `setColor()` om din modul använder gemensam anod.

```cpp
const int lightPin = A0;

const int redPin = 9;
const int greenPin = 10;
const int bluePin = 11;

const unsigned long sampleIntervalMs = 100;

unsigned long lastSampleMs = 0;
float filteredLight = 0.0;

int observedMin = 1023;
int observedMax = 0;

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  Serial.begin(115200);
}

void loop() {
  unsigned long now = millis();

  if (now - lastSampleMs >= sampleIntervalMs) {
    lastSampleMs = now;

    int raw = analogRead(lightPin);
    observedMin = min(observedMin, raw);
    observedMax = max(observedMax, raw);

    if (filteredLight == 0.0) {
      filteredLight = raw;
    } else {
      filteredLight = filteredLight * 0.85 + raw * 0.15;
    }

    int level = mapConstrained(filteredLight, observedMin, observedMax, 0, 255);

    if (level < 85) {
      setColor(0, 0, 180);
    } else if (level < 170) {
      setColor(0, 180, 0);
    } else {
      setColor(180, 120, 0);
    }

    Serial.print("raw=");
    Serial.print(raw);
    Serial.print(" filtered=");
    Serial.print(filteredLight);
    Serial.print(" min=");
    Serial.print(observedMin);
    Serial.print(" max=");
    Serial.print(observedMax);
    Serial.print(" level=");
    Serial.println(level);
  }
}

int mapConstrained(float value, int inMin, int inMax, int outMin, int outMax) {
  if (inMax <= inMin + 5) {
    return outMin;
  }

  float ratio = (value - inMin) / float(inMax - inMin);
  ratio = constrain(ratio, 0.0, 1.0);

  return int(outMin + ratio * (outMax - outMin));
}

void setColor(int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}
```

### Förväntat resultat

När du täcker sensorn, riktar den mot ljus eller ändrar rumsbelysning ska RGB-LED växla mellan olika statusfärger. Seriell monitor visar råvärde, filtrerat värde och observerat min/max.

Det viktiga i mönstret är att koden lär sig ett ungefärligt intervall från miljön. Det gör mönstret mer tolerant mot olika LDR-exemplar och olika kopplingar. I en färdig produkt bör du däremot dokumentera kalibreringsläget och spara gränser på ett kontrollerat sätt.

## Variation: digital luxsensor på I2C

Byt ut LDR-delen mot en I2C-baserad sensor som BH1750, VEML7700 eller TSL2591. Då förändras mönstrets karaktär:

- du får mer meningsfulla ljusvärden
- du behöver installera rätt bibliotek
- du behöver kontrollera I2C-adress
- du behöver välja mätintervall, gain eller integrationstid om biblioteket ger stöd för det
- du bör hantera sensorns maximala och minimala mätområde

En bra variation är att visa luxvärdet på en OLED från kapitel 22 och samtidigt låta en LED eller NeoPixel från kapitel 18 visa nivåklasser.

## Variation: enkel färgklassificering

Med en TCS34725-liknande färgsensor kan experimentet bli en enkel färgklassificerare.

Arbetssätt:

1. Montera sensorn med fast avstånd till objektet.
2. Använd samma belysning varje gång.
3. Logga råvärden för några kända färger.
4. Normalisera RGB mot clear-kanalen.
5. Sätt enkla referensvärden.
6. Klassificera nya objekt som närmast kända färg eller okänd.

Det här är ett bra exempel på varför praktiska experiment ofta kräver mekanisk konsekvens. Om du håller objektet med handen på olika avstånd blir färgklassificeringen sämre än om du bygger en enkel hållare.

## Variation: optisk räknare

Med en optisk brytare kan du skapa en räknare. När ett hjul, en flik eller ett papper passerar bryts ljusstrålen. Arduino räknar händelser och kan räkna hastighet eller antal.

För långsamma rörelser kan polling räcka. För snabbare pulser kan interrupt vara rätt val, men då gäller råden från kapitel 8: håll interrupt handler kort och låt huvudprogrammet bearbeta resultatet.

## Felsökning

När en optisk sensor beter sig konstigt, börja med att avgöra om problemet är elektriskt, optiskt eller logiskt.

| Symptom | Trolig orsak | Kontroll |
|---|---|---|
| Analogvärdet ändras inte | Fel koppling, fel pinne eller trasig spänningsdelare | Mät spänningen på analog pinne med multimeter |
| Värdet går åt “fel” håll | LDR och motstånd sitter omvänt jämfört med kodens antagande | Logga råvärde vid mörkt och ljust |
| Värdet hoppar mycket | Brus, flimrande ljus eller dålig matning | Filtrera, mät matning och testa annan ljuskälla |
| Digital modul växlar slumpmässigt | Tröskel nära signalnivån | Justera potentiometer eller läs analog utgång |
| I2C-sensor hittas inte | Fel adress, saknad matning eller fel SDA/SCL | Kör I2C-scanner och kontrollera pinout |
| Luxvärdet verkar orimligt | Sensor mättad, fel gain eller dålig placering | Ändra integrationstid/gain och jämför med känd miljö |
| Färgsensor blandar ihop färger | Varierande avstånd eller belysning | Bygg hållare och kalibrera mot kända objekt |
| IR-reflektion fungerar bara ibland | Ytan reflekterar olika vid olika vinklar | Testa med rätt material och skärma sensorn |

## Vanliga misstag

- **Misstag:** Att använda LDR-värde som om det vore lux.
  - **Varför det händer:** Analogvärdet känns numeriskt och exakt.
  - **Hur man undviker det:** Beskriv LDR-värdet som relativ nivå om du inte har kalibrerat mot en relevant referens.

- **Misstag:** Att testa färgsensor i handen och sedan förvänta sig stabil klassificering.
  - **Varför det händer:** Sensorn fungerar i demoexempel men geometrin ändras hela tiden.
  - **Hur man undviker det:** Använd fast avstånd, kontrollerad belysning och exempeldata från den riktiga mekaniken.

- **Misstag:** Att glömma att display, LED eller statusljus påverkar ljussensorn.
  - **Varför det händer:** Man tänker på sensorn elektriskt men inte optiskt.
  - **Hur man undviker det:** Placera sensorn så att den mäter omgivningen, inte projektets egna ljuskällor.

- **Misstag:** Att sätta en digital tröskel utan hysteresis.
  - **Varför det händer:** Ett enkelt `if` fungerar på skrivbordet.
  - **Hur man undviker det:** Använd separata gränser för på och av, eller kräva stabil nivå under viss tid.

- **Misstag:** Att välja UV-sensor för säkerhetskritiska beslut.
  - **Varför det händer:** Sensorbiblioteket kan ge ett UV-indexliknande värde.
  - **Hur man undviker det:** Använd enkla UV-moduler för pedagogik och trend, inte som certifierad skyddsmätning.

- **Misstag:** Att ignorera material och yta vid IR-reflektion.
  - **Varför det händer:** Sensorn verkar mäta avstånd eller närvaro i exempel.
  - **Hur man undviker det:** Testa med projektets faktiska material, färger, vinklar och avstånd.

## Valguide

| Behov | Rekommenderad start | När du bör välja något annat |
|---|---|---|
| Nattläge eller enkel skymningsdetektion | LDR i spänningsdelare | När mätvärdet måste vara jämförbart mellan enheter |
| Displayanpassning efter omgivningsljus | Digital luxsensor | När placeringen inte kan göras representativ |
| Ljusstyrkeloggning | VEML7700, BH1750 eller TSL2591 | När ljusnivån varierar utanför sensorns område |
| Mycket varierande ljusnivåer | TSL2591-liknande sensor | När du bara behöver enkel ja/nej-detektion |
| Enkel färgklassificering | TCS34725-liknande färgsensor | När avstånd och belysning inte kan kontrolleras |
| UV-trend eller UV-experiment | VEML6075-liknande sensor | När mätningen är säkerhetskritisk |
| Linjeföljning eller objektreflektion | IR-reflektionssensor | När objektets material varierar för mycket |
| Pulser eller mekanisk passagedetektion | Optisk brytare | När smuts, damm eller mekanisk tolerans blockerar ljusvägen |
| Fjärrstyrd meny eller lägesval | IR-mottagare och fjärrkontroll | När signalen måste gå genom väggar eller vara säkerhetskritisk |

Snabbt optiskt val:

- Välj **LDR** när relativ ljusförändring räcker.
- Välj **digital luxsensor** när ljusnivåer ska jämföras mellan tester eller platser.
- Välj **färgsensor** bara när avstånd, ljus och objekt kan hållas tillräckligt kontrollerade.
- Välj **optisk brytare** när något passerar en bestämd punkt.
- Välj **APDS-9960** när du vill kombinera närhet, färg, ljus eller enkel gest i samma I2C-modul.

## Snabb överblick

- Optiska sensorer mäter ljus, men olika sensorer svarar på olika frågor.
- LDR är bäst för enkel relativ ljusnivå, inte exakt luxmätning.
- Digitala ljussensorer via I2C ger ofta mer stabila och användbara värden.
- Färgsensorer kräver kontrollerad belysning och fast geometri för att bli pålitliga.
- UV-sensorer passar bra för pedagogik och trendmätning men ska inte användas som certifierade skyddsinstrument.
- IR-reflektion och optiska brytare är ofta bättre för detektion än för egentlig mätning.
- IR-fjärrkontroll hör hemma som inmatning, inte som exakt ljusmätning.
- Placering, vinkel, kapsling och omgivningsljus är lika viktiga som kod och koppling.
- Filtrering och hysteresis gör optiska beslut mycket mer robusta.
- Dokumentera alltid optisk sensorprofil, särskilt ljuskälla, avstånd och placering.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Beror på sensor/modul |
| Typiskt gränssnitt | Analogt, digitalt, I2C eller puls |
| IR-fjärr | Digital mottagarmodul med avkodningsbibliotek |
| Välj när | ljus, färg, reflektion, optisk passage eller IR-inmatning ska användas |
| Välj inte när | miljön har okontrollerat ljus utan möjlighet till kapsling |
| Vanliga fel | mättnad, omgivningsljus, fel avstånd, blank yta |
| APDS-9960/GY-9960 | I2C-modul för färg, ljus, närhet och enkla gester |
| Alternativ att överväga | ToF, mekanisk brytare, kamera, radio, Wi-Fi, BLE eller kabelburen kommunikation |

Använd referensrutan som en snabb kontroll innan du bygger projektet. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När sensorn ger ett analogt ljusvärde, använd kapitel 6 för trösklar, kalibrering och rimlighetskontroll.
- När modulen använder I2C eller SPI, jämför med kapitel 9 innan du felsöker själva sensorn.
- När optisk inmatning blir en del av ett användargränssnitt, gå vidare till kapitel 22.
- När värdena påverkas av omgivningsljus, placering eller kablage, använd felsökningsmönstren i kapitel 35.

