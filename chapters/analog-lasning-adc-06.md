# 6. Analog läsning, ADC och mätosäkerhet

## Mätfunktion i praktiken
Digitala signaler är enkla att resonera om: en pinne är LOW eller HIGH, åtminstone i den modell vi använder i koden. Analoga signaler är annorlunda. De kan anta många nivåer mellan GND och en referensspänning, och de påverkas av brus, komponenttoleranser, kablar, matning, sensorns egen elektronik och mikrokontrollerns ADC.

För en erfaren programmerare är det frestande att se `analogRead()` som en funktion som returnerar ett tal. Det gör den också, men talet är inte “sanningen”. Det är ett mätvärde från en viss analog ingång, vid en viss tidpunkt, med en viss referensspänning, i ett visst brusläge och med en viss upplösning. Om du bygger kod som om mätvärdet vore exakt kommer projektet ofta fungera på skrivbordet men bete sig sämre när kablarna blir längre, batteriet sjunker, temperaturen ändras eller kortet byts ut.

Det här kapitlet handlar därför inte bara om att läsa analoga värden. Det handlar om att förstå vad värdena betyder, hur du gör dem användbara och när du bör välja en annan lösning än en enkel analog ingång. Vi går från grundprincipen bakom ADC till praktiska mätstrategier, filtrering, kalibrering och ett referensmönster där du mäter en potentiometer på ett sätt som går att återanvända i senare sensorprojekt.

I praktiken ger kapitlet stöd när du behöver tolka `analogRead()` i relation till referensspänning och kortfamilj, skilja mellan upplösning och faktisk mätnoggrannhet, känna igen vanliga felkällor och göra mätvärden stabilare med filtrering, kalibrering och hysteresis. Samma resonemang hjälper dig också att avgöra när en analog ingång räcker och när en digital sensor eller extern ADC är ett bättre val.

## Förutsättningar

Du behöver ha med dig några begrepp från tidigare kapitel:

- **Logiknivå:** olika kort arbetar med olika spänningsnivåer, ofta 5 V eller 3,3 V.
- **Gemensam jord:** mätningen saknar mening om sensorn och kortet inte delar referens.
- **Spänningsdelare:** två motstånd kan skapa en lägre spänning som kan mätas av en analog ingång.
- **Strömbudget:** sensorer och moduler påverkar matningen, och matningen påverkar mätningen.
- **Pinout:** alla pinnar som ser analoga ut är inte likvärdiga på alla kort.

Koppla aldrig en analog ingång till en spänning som överstiger kortets tillåtna område. En 5 V-signal kan vara normal på ett klassiskt UNO-kort men skadlig för ett 3,3 V-kort. Kontrollera alltid kortets dokumentation innan du ansluter en sensor eller spänningsdelare.

## Vad en ADC faktiskt gör

ADC står för analog-to-digital converter, analog-till-digital-omvandlare. Den mäter en analog spänning och omvandlar den till ett heltal. I Arduino-koden ser det ofta ut så här:

```cpp
const int sensorPin = A0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int rawValue = analogRead(sensorPin);
  Serial.println(rawValue);
  delay(200);
}
```

På många klassiska Arduino-kort ger `analogRead()` ett värde mellan 0 och 1023. Det innebär inte att ADC:n vet den exakta spänningen. Det betyder att mätområdet har delats upp i 1024 steg. Om referensspänningen är 5 V motsvarar ett steg ungefär 4,9 mV. Om referensspänningen är 3,3 V motsvarar ett steg ungefär 3,2 mV.

| ADC-upplösning | Antal steg | Typiskt maxvärde | Stegstorlek vid 5 V | Stegstorlek vid 3,3 V |
|---|---|---|---|---|
| 10 bit | 1024 | 1023 | cirka 4,9 mV | cirka 3,2 mV |
| 12 bit | 4096 | 4095 | cirka 1,2 mV | cirka 0,8 mV |
| 16 bit | 65536 | 65535 | cirka 0,076 mV | cirka 0,050 mV |

Tabellen visar den teoretiska stegstorleken. Den säger inte att mätningen automatiskt är så noggrann. En 12-bitars ADC kan ge fler steg än en 10-bitars ADC, men om brus, referensspänning eller sensorkoppling är dålig blir de extra stegen inte särskilt användbara.

Ett bra sätt att tänka är:

- **Upplösning:** hur många steg ADC:n kan skilja mellan.
- **Noggrannhet:** hur nära mätvärdet ligger det verkliga värdet.
- **Precision:** hur lika mätvärdena blir när du mäter samma sak flera gånger.

Det är möjligt att ha hög upplösning men dålig noggrannhet. Det är också möjligt att ha stabila men systematiskt felaktiga mätvärden. Därför behöver analog mätning nästan alltid kalibrering eller åtminstone rimlighetskontroll.

## Referensspänningen är mätningens linjal

En ADC mäter inte “volt” direkt. Den jämför ingångsspänningen med en referens. Om referensen är 5 V och ingången är ungefär halva referensen får du ett värde nära mitten av ADC-området. Om referensen är 3,3 V och ingången fortfarande är 2,5 V får du ett annat förhållande.

En förenklad omräkning från råvärde till spänning kan se ut så här:

```cpp
float adcToVoltage(int rawValue, float referenceVoltage, int adcMaxValue) {
  return (rawValue * referenceVoltage) / adcMaxValue;
}
```

För ett 10-bitars område använder man ofta 1023 som maxvärde när man översätter det högsta möjliga råvärdet till referensspänningen. I praktiska mätningar är det viktigare att vara konsekvent och dokumentera formeln än att fastna i sista decimalen.

```cpp
const int sensorPin = A0;
const float referenceVoltage = 5.0;
const int adcMaxValue = 1023;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int rawValue = analogRead(sensorPin);
  float voltage = (rawValue * referenceVoltage) / adcMaxValue;

  Serial.print("raw=");
  Serial.print(rawValue);
  Serial.print(" voltage=");
  Serial.println(voltage, 3);

  delay(250);
}
```

Problemet är att `referenceVoltage` ofta inte är exakt 5,0 V eller exakt 3,3 V. USB-matning kan ligga lite över eller under 5 V. En regulator kan variera med last. Batteridrift förändras över tid. Om sensorns utsignal och ADC:ns referens påverkas av samma matning kan vissa fel delvis ta ut varandra. Om de inte gör det kan mätningen driva.

Detta är en av de viktigaste praktiska insikterna i analog mätning: spänningen du tror att du mäter och spänningen ADC:n använder som referens är båda delar av systemet.

## Analoga ingångar skiljer sig mellan kortfamiljer

I kapitel 2 introducerades kortval som en teknisk kompromiss. Analoga ingångar är ett område där skillnaderna mellan kortfamiljer ofta märks tydligt.

Klassiska UNO- och Nano-kort har analoga ingångar som många exempel bygger på. De är enkla, väldokumenterade och passar bra för potentiometrar, LDR-baserade spänningsdelare och enklare analoga sensorer. Moderna 3,3 V-kort kan ha fler ADC-kanaler, annan upplösning och andra begränsningar. ESP32-baserade kort är kraftfulla, men deras ADC-beteende kräver mer uppmärksamhet om du vill ha stabila och jämförbara mätvärden. RP2040-baserade kort har andra styrkor och begränsningar.

Det betyder inte att ett kort är “bra” och ett annat “dåligt”. Det betyder att analog mätning bör vara en del av kortvalet.

| Projektbehov | Kortegenskap att kontrollera |
|---|---|
| Mäta enkel potentiometer | Antal analoga ingångar och exempelstöd |
| Mäta svag sensorsignal | ADC-brus, referens, eventuell förstärkning |
| Mäta flera analoga sensorer | Antal ADC-kanaler eller behov av multiplexer |
| Batterimätning | Tillåtet spänningsområde och spänningsdelarens strömförbrukning |
| Jämförbara mätvärden över tid | Stabil referens och kalibrering |
| Hög noggrannhet | Extern ADC eller digital sensor kan vara bättre |

En vanlig fälla är att flytta en analog sketch från ett 5 V-kort till ett 3,3 V-kort utan att ändra spänningsdelare, referensspänning eller antaganden i koden. Koden kompilerar, men mätområdet och säkerhetsmarginalerna har förändrats.

## När analog läsning är rätt val

Analog läsning är ett bra val när signalen naturligt varierar inom kortets tillåtna område och när kraven på noggrannhet är rimliga. Typiska exempel är:

- potentiometrar
- enkla ljussensorer med LDR
- vissa temperatur-, fukt- eller trycksensorer med analog utgång
- spänningsdelare för säker lågspänningsmätning
- reglage, vred och enkla användargränssnitt
- relativa mätningar där exakta enheter inte är avgörande

Analog läsning är särskilt bra i testfasen. Den gör det lätt att förstå hur en sensor förändras över tid. Med seriell plotter kan du snabbt se om signalen är stabil, brusig, långsam, snabb, inverterad eller begränsad till ett oväntat område.

Men analog läsning är inte alltid rätt val.

Välj hellre digital sensor eller extern krets när:

- du behöver hög noggrannhet utan omfattande egen kalibrering
- kabeln är lång och miljön är brusig
- sensorn redan finns som I2C- eller SPI-modul med färdig kompensation
- mätvärdet behöver vara reproducerbart mellan flera exemplar
- du mäter mycket små signaler
- du behöver galvanisk isolering eller säker mätning i svårare miljöer

Ett BME280-liknande digitalt sensorkort kan till exempel vara bättre än en enkel analog miljösensor om du vill ha kalibrerad temperatur, luftfuktighet och tryck. En extern ADC kan vara bättre om du behöver fler bitar, differentialmätning eller stabilare referens än kortets inbyggda ADC erbjuder.

## Från råvärde till meningsfullt värde

Ett råvärde från `analogRead()` är sällan det du vill visa för användaren. Du vill ofta översätta det till en spänning, procent, fysisk enhet eller kategoriserad nivå.

Arduino-funktionen `map()` används ofta i enkla exempel:

```cpp
int percent = map(rawValue, 0, 1023, 0, 100);
```

Det är enkelt men har begränsningar. `map()` arbetar med heltal och klipper inte automatiskt resultatet till målområdet. För mer kontrollerad kod kan du skriva en egen funktion med flyttal och tydlig begränsning.

```cpp
float clampFloat(float value, float minValue, float maxValue) {
  if (value < minValue) {
    return minValue;
  }

  if (value > maxValue) {
    return maxValue;
  }

  return value;
}

float mapFloat(float value, float inMin, float inMax, float outMin, float outMax) {
  float normalized = (value - inMin) / (inMax - inMin);
  normalized = clampFloat(normalized, 0.0, 1.0);
  return outMin + normalized * (outMax - outMin);
}
```

Med den funktionen kan du kalibrera ett faktiskt mätområde. En potentiometer kanske inte ger exakt 0 och 1023 i praktiken. Den kanske ger 12 i ena ändläget och 1008 i det andra. Då är det bättre att använda uppmätta gränser.

```cpp
const int potMin = 12;
const int potMax = 1008;

int rawValue = analogRead(A0);
float positionPercent = mapFloat(rawValue, potMin, potMax, 0.0, 100.0);
```

Den här typen av kalibrering gör koden mer robust och mer ärlig. Du låtsas inte att hårdvaran följer ett idealiskt intervall, utan använder det intervall du faktiskt har mätt.

## Brus är normalt

Analoga mätvärden rör sig ofta lite även när sensorn verkar ligga stilla. Det kan bero på ADC-brus, matningsbrus, elektromagnetiska störningar, kabeldragning, kontaktproblem, sensorns egen variation eller att miljön faktiskt förändras.

Ett vanligt nybörjarmisstag är att försöka få bort allt brus. Ett bättre mål är att förstå hur mycket brus som är normalt och välja en stabiliseringsmetod som passar användningen.

| Symptom | Möjlig orsak | Praktisk åtgärd |
|---|---|---|
| Värdet hoppar några steg | Normalt ADC-brus | Medelvärde eller lågpassfilter |
| Värdet hoppar kraftigt | Flytande ingång eller dålig jord | Kontrollera koppling och gemensam jord |
| Värdet ändras när USB-kabeln rör sig | Matning eller mekanisk kontakt | Kontrollera kabel, breadboard och matningspunkt |
| Värdet påverkas av motor/relä | Störningar från last | Separera matning, avkoppla och flytta kablar |
| Värdet ligger nära max | För hög ingångsspänning eller fel referens | Mät med multimeter och kontrollera spänningsdelare |
| Värdet når aldrig fullt område | Sensorområde eller kalibrering | Använd uppmätta min/max i koden |

Brus är inte bara ett problem. Ibland är variationen information. En ljudsensor, vibrationssensor eller strömsensor kan vara intressant just för att signalen varierar. Men då behöver koden mäta rätt egenskap: medelvärde, toppvärde, variation, tröskelpassage eller trend.

## Medelvärde

Den enklaste stabiliseringen är att läsa flera gånger och ta medelvärdet.

```cpp
int readAverageAnalog(int pin, int samples) {
  long sum = 0;

  for (int i = 0; i < samples; i++) {
    sum += analogRead(pin);
    delay(2);
  }

  return sum / samples;
}
```

Detta fungerar bra för långsamma signaler som temperatur, ljusnivå eller potentiometerläge. Nackdelen är att funktionen blockerar programmet medan den läser. Med 20 mätningar och 2 ms paus tar funktionen minst 40 ms. Det är inget problem i ett enkelt test men kan vara fel i ett mer responsivt system.

För många projekt är det bättre att använda ett löpande filter som uppdateras lite i taget.

## Exponentiellt glidande medelvärde

Ett exponentiellt glidande medelvärde, ofta kallat exponential moving average, ger en enkel lågpassfiltrering utan att lagra många mätvärden.

```cpp
const int sensorPin = A0;

float filteredValue = 0.0;
const float alpha = 0.15;

void setup() {
  Serial.begin(115200);
  filteredValue = analogRead(sensorPin);
}

void loop() {
  int rawValue = analogRead(sensorPin);
  filteredValue = alpha * rawValue + (1.0 - alpha) * filteredValue;

  Serial.print("raw:");
  Serial.print(rawValue);
  Serial.print(" filtered:");
  Serial.println(filteredValue);

  delay(50);
}
```

`alpha` styr hur snabbt filtret reagerar. Ett lågt värde ger stabilare men långsammare signal. Ett högre värde reagerar snabbare men släpper igenom mer brus.

| Alpha | Beteende | Passar för |
|---|---|---|
| 0,05 | Mycket mjukt, långsamt | Långsamma miljömätningar |
| 0,15 | Balanserat | Reglage, ljus, enkel sensorvisning |
| 0,30 | Snabbare, mer brus | Interaktiv kontroll |
| 0,70 | Mycket snabb respons | När signalen ska följa rörelse tydligt |

Det finns inget perfekt värde. Välj utifrån projektet och dokumentera valet.

## Hysteresis för stabila beslut

Filtrering stabiliserar mätvärdet. Hysteresis stabiliserar beslut. Om du styr något baserat på en tröskel, till exempel “tänd LED när ljuset är under 30 procent”, kan värdet pendla runt gränsen och få utgången att blinka.

Med hysteresis använder du två gränser: en för att slå på och en annan för att slå av.

```cpp
const int sensorPin = A0;
const int ledPin = 13;

const int turnOnBelow = 300;
const int turnOffAbove = 360;

bool ledEnabled = false;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int rawValue = analogRead(sensorPin);

  if (!ledEnabled && rawValue < turnOnBelow) {
    ledEnabled = true;
  }

  if (ledEnabled && rawValue > turnOffAbove) {
    ledEnabled = false;
  }

  digitalWrite(ledPin, ledEnabled ? HIGH : LOW);

  Serial.print("raw=");
  Serial.print(rawValue);
  Serial.print(" led=");
  Serial.println(ledEnabled ? "on" : "off");

  delay(50);
}
```

Hysteresis är ett av de mest användbara mönstren i praktiska Arduino-system. Det används inte bara för ljus, utan också för temperaturstyrning, nivåvakter, batterivarningar och många andra beslut där mätvärdet kan ligga nära en gräns.

## Spänningsdelare som mätverktyg

En spänningsdelare består av två motstånd och används ofta för att skala ned en spänning så att den kan mätas av en analog ingång.

```text
Vin --- R1 --- mätpunkt --- R2 --- GND
                 mätpunkt -> A0
```

Spänningen vid A0 blir lägre än `Vin`. Förenklat gäller:

```text
Vout = Vin * R2 / (R1 + R2)
```

Om du vill mäta ett batteri på upp till 12 V med ett 3,3 V-kort behöver du välja motstånd som gör att A0 aldrig överstiger 3,3 V. Du behöver också tänka på strömmen genom motstånden, ADC:ns ingångsegenskaper, toleranser och säkerhetsmarginal. En spänningsdelare som fungerar på papper kan bli dålig om motstånden är för höga, om kablarna är långa eller om ingången behöver stabiliseras med kondensator.

I den här boken använder vi spänningsdelare för säkra lågspänningsmätningar. Mät inte nätspänning med en enkel spänningsdelare. Nätspänning kräver särskild isolering, skydd och kompetens och ligger utanför bokens praktiska lågspänningsprojekt.

## Potentiometern som analogt testverktyg

En potentiometer är ett av de bästa verktygen för att förstå analog läsning. Den fungerar som en justerbar spänningsdelare.

En vanlig koppling är:

```text
Potentiometer ytterpinne 1 -> GND
Potentiometer mittpinne   -> A0
Potentiometer ytterpinne 2 -> 5V eller 3V3
```

Vilken ytterpinne som går till GND respektive matning avgör om värdet ökar eller minskar när du vrider medurs. Om riktningen blir fel kan du byta ytterpinnarna eller invertera värdet i kod.

Potentiometern är användbar eftersom du vet vad som borde hända: råvärdet ska röra sig mjukt från lågt till högt när du vrider. Om det hoppar, fastnar eller beter sig ryckigt har du ett bra felsökningsfall utan att en komplex sensor stör analysen.

## Referensmönster: kalibrerad analog läsning med potentiometer

Det här referensmönstret visar råvärde, filtrerat värde och kalibrerad procent. Poängen är inte att potentiometern i sig är spännande, utan att skapa ett analogt mönster som kan återanvändas för ljusgivare, reglage, trycksensorer och andra analoga moduler.

### Det här används i exemplet

Du behöver:

- ett Arduino-kompatibelt kort med minst en analog ingång
- en potentiometer, exempelvis 10 kOhm
- kopplingskablar
- breadboard
- USB-kabel
- Arduino IDE eller motsvarande miljö
- gärna multimeter för att kontrollera matning och mittspänning

### Koppling

Koppla potentiometern som spänningsdelare.

| Potentiometer | Anslutning |
|---|---|
| Ytterpinne 1 | GND |
| Mittpinne | A0 |
| Ytterpinne 2 | 5V på 5 V-kort eller 3V3 på 3,3 V-kort |

Kontrollera att mittpinnen aldrig kan få högre spänning än kortets analoga ingång tål. På ett 3,3 V-kort ska potentiometern normalt kopplas mellan GND och 3V3, inte mellan GND och 5 V.

### Steg 1: läs råvärde

Ladda upp en minimal sketch.

```cpp
const int potPin = A0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int rawValue = analogRead(potPin);
  Serial.println(rawValue);
  delay(100);
}
```

Öppna seriell monitor eller seriell plotter. Vrid långsamt potentiometern. Notera lägsta och högsta värde du faktiskt ser. Spara värdena tillsammans med kopplingen om de ska användas senare.

### Steg 2: filtrera värdet

Byt till denna version.

```cpp
const int potPin = A0;

float filteredValue = 0.0;
const float alpha = 0.15;

void setup() {
  Serial.begin(115200);
  filteredValue = analogRead(potPin);
}

void loop() {
  int rawValue = analogRead(potPin);
  filteredValue = alpha * rawValue + (1.0 - alpha) * filteredValue;

  Serial.print("raw:");
  Serial.print(rawValue);
  Serial.print(" filtered:");
  Serial.println(filteredValue);

  delay(50);
}
```

Öppna seriell plotter. Jämför råvärde och filtrerat värde. Vrid snabbt och långsamt. Fundera på om filtret känns för trögt eller för nervöst.

### Steg 3: kalibrera till procent

Använd de min- och maxvärden du faktiskt mätte i steg 1. Byt `calibratedMin` och `calibratedMax` till dina värden.

```cpp
const int potPin = A0;

const int calibratedMin = 12;
const int calibratedMax = 1008;

float filteredValue = 0.0;
const float alpha = 0.15;

float clampFloat(float value, float minValue, float maxValue) {
  if (value < minValue) {
    return minValue;
  }

  if (value > maxValue) {
    return maxValue;
  }

  return value;
}

float mapFloat(float value, float inMin, float inMax, float outMin, float outMax) {
  float normalized = (value - inMin) / (inMax - inMin);
  normalized = clampFloat(normalized, 0.0, 1.0);
  return outMin + normalized * (outMax - outMin);
}

void setup() {
  Serial.begin(115200);
  filteredValue = analogRead(potPin);
}

void loop() {
  int rawValue = analogRead(potPin);
  filteredValue = alpha * rawValue + (1.0 - alpha) * filteredValue;

  float percent = mapFloat(filteredValue, calibratedMin, calibratedMax, 0.0, 100.0);

  Serial.print("raw:");
  Serial.print(rawValue);
  Serial.print(" filtered:");
  Serial.print(filteredValue, 1);
  Serial.print(" percent:");
  Serial.println(percent, 1);

  delay(50);
}
```

Nu har du ett användbart analogt mönster:

- läs råvärde
- filtrera
- kalibrera
- översätt till meningsfullt område
- logga både råvärde och bearbetat värde

Det är mycket lättare att felsöka analog kod om du alltid kan se råvärdet.

### Steg 4: lägg till hysteresis

Lägg till en LED eller använd den inbyggda LED-pinnen om kortet har en sådan. Målet är att LED ska tändas när potentiometern går under en låg nivå och släckas först när den går över en högre nivå.

```cpp
const int potPin = A0;
const int ledPin = 13;

const int calibratedMin = 12;
const int calibratedMax = 1008;

const float turnOnBelowPercent = 35.0;
const float turnOffAbovePercent = 45.0;

float filteredValue = 0.0;
const float alpha = 0.15;

bool ledEnabled = false;

float clampFloat(float value, float minValue, float maxValue) {
  if (value < minValue) {
    return minValue;
  }

  if (value > maxValue) {
    return maxValue;
  }

  return value;
}

float mapFloat(float value, float inMin, float inMax, float outMin, float outMax) {
  float normalized = (value - inMin) / (inMax - inMin);
  normalized = clampFloat(normalized, 0.0, 1.0);
  return outMin + normalized * (outMax - outMin);
}

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  filteredValue = analogRead(potPin);
}

void loop() {
  int rawValue = analogRead(potPin);
  filteredValue = alpha * rawValue + (1.0 - alpha) * filteredValue;

  float percent = mapFloat(filteredValue, calibratedMin, calibratedMax, 0.0, 100.0);

  if (!ledEnabled && percent < turnOnBelowPercent) {
    ledEnabled = true;
  }

  if (ledEnabled && percent > turnOffAbovePercent) {
    ledEnabled = false;
  }

  digitalWrite(ledPin, ledEnabled ? HIGH : LOW);

  Serial.print("percent:");
  Serial.print(percent, 1);
  Serial.print(" led:");
  Serial.println(ledEnabled ? "on" : "off");

  delay(50);
}
```

Det här kodexemplet innehåller medvetet samma byggstenar som senare återkommer i sensorkapitlen: rådata, filtrering, kalibrering, tröskel och stabilt beslut.

## Från potentiometer till sensor

En potentiometer är ett kontrollerat testverktyg. Den gör det lätt att se om analog läsning, filtrering, kalibrering och hysteresis fungerar innan du kopplar in en verklig sensor.

När mönstret flyttas till en sensor behöver du normalt kontrollera fler saker:

- En verklig sensor kan ha brus, offset, tröghet och miljöberoende värden.
- Mät faktisk min- och maxnivå i projektets miljö i stället för att anta idealvärden.
- Behåll råvärdet i seriell utskrift medan du felsöker.
- Behåll filtrering om värdet hoppar.
- Behåll hysteresis om värdet ska styra ett läge eller en utgång.
- Byt bara en sak i taget: först potentiometer mot sensor, sedan trösklar och kalibrering.

Samma struktur kan alltså användas för många analoga givare, men gränserna måste komma från den faktiska kopplingen.

## Felsökning av analoga mätningar

När ett analogt värde är fel, börja inte med att byta bibliotek eller skriva om all kod. Arbeta från hårdvara till mjukvara.

1. Mät matningsspänningen med multimeter.
2. Mät spänningen på den analoga pinnen mot GND.
3. Kontrollera att GND är gemensam mellan kort och sensor.
4. Kontrollera att ingångsspänningen ligger inom tillåtet område.
5. Kör en minimal testsketch som bara skriver ut råvärdet.
6. Rör kablar och komponenter försiktigt och se om värdet hoppar.
7. Testa med potentiometer för att avgöra om pinnen och ADC:n fungerar.
8. Lägg till filtrering först när råvärdet är begripligt.

Det sista steget är viktigt. Filtrering kan dölja problem. Ett medelvärde av dåliga mätningar är fortfarande en dålig mätning.

## Vanliga misstag

- **Misstag: Att anta att `analogRead()` betyder samma sak på alla kort.**
  - Varför det händer: Arduino-API:t ser likadant ut även när hårdvaran skiljer sig.
  - Hur man undviker det: Dokumentera kortfamilj, ADC-upplösning, referensspänning och tillåtet ingångsområde.

- **Misstag: Att mata en analog ingång med för hög spänning.**
  - Varför det händer: Många exempel utgår från 5 V-kort, medan moderna kort ofta använder 3,3 V.
  - Hur man undviker det: Kontrollera pinout och datablad. Använd spänningsdelare eller nivåanpassning där det är säkert och lämpligt.

- **Misstag: Att tolka råvärde som fysisk enhet.**
  - Varför det händer: Ett råvärde ser exakt ut, men saknar sammanhang.
  - Hur man undviker det: Översätt råvärdet till spänning, procent eller kalibrerad enhet och spara formeln i koden.

- **Misstag: Att filtrera bort symptom i stället för att lösa grundfelet.**
  - Varför det händer: Ett medelvärde gör utskriften lugnare.
  - Hur man undviker det: Kontrollera först jord, matning, koppling och mätområde.

- **Misstag: Att använda för snäva trösklar.**
  - Varför det händer: Man väljer en enda gräns utan att ta hänsyn till brus.
  - Hur man undviker det: Använd hysteresis eller tydliga dödband när mätvärden styr beslut.

- **Misstag: Att bara logga bearbetade värden.**
  - Varför det händer: Procent eller färdiga enheter känns mer användbara.
  - Hur man undviker det: Logga råvärde och bearbetat värde åtminstone under utveckling.

## Snabb sammanfattning

- En ADC omvandlar analog spänning till ett digitalt heltal, inte till en absolut sanning.
- Referensspänningen avgör hur råvärdet ska tolkas.
- Upplösning, noggrannhet och precision är olika saker.
- Analoga mätningar påverkas av brus, matning, koppling, kabeldragning och komponenttoleranser.
- Råvärden bör ofta filtreras, kalibreras och översättas till meningsfulla enheter.
- Hysteresis gör beslut stabilare när mätvärden ligger nära en tröskel.
- Potentiometern är ett bra testverktyg för att förstå ADC, filtrering och kalibrering.
- För hög noggrannhet, lång kabeldragning eller komplexa mätningar kan en digital sensor eller extern ADC vara bättre.

## Relaterat

- Använd kapitel 23 och 24 när ADC-värdena kommer från miljö-, ljus- eller färgsensorer och behöver tolkas som verkliga mätvärden.
- Använd kapitel 28 när mätningen gäller spänning, ström eller energi och riskerar att påverka kretsen som mäts.
- Använd kapitel 33 när signalen är brusig, för svag, för hög eller behöver filtreras innan den når ADC-ingången.
