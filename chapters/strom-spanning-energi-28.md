# 28. Ström, spänning, energi och batterimätning

## Mät- och energibild
Många Arduino-projekt börjar med frågan “fungerar sensorn?”, men förr eller senare kommer en annan fråga: “hur mycket ström drar systemet?” Det kan handla om ett batteridrivet projekt, en motor som stör mikrokontrollern, en LED-strip som kräver separat matning eller en sensorstation som ska logga energiförbrukning över tid.

Ström, spänning och energi är nära släkt, men de svarar på olika frågor.

- **Spänning** beskriver elektrisk potential mellan två punkter.
- **Ström** beskriver hur mycket laddning som flödar genom en del av kretsen.
- **Effekt** beskriver hur snabbt energi används eller levereras.
- **Energi** beskriver hur mycket som använts över tid.
- **Batterinivå** är en tolkning, inte bara ett rått spänningsvärde.

Det här kapitlet hjälper dig att mäta dessa storheter på en nivå som passar Arduino-projekt. Vi går igenom enkla spänningsdelare, strömsensorer, shuntmotstånd, Hall-effektsensorer, batterimätning och färdiga mätkretsar som ofta används i hobby- och prototypsystem.

Målet är inte att ersätta en riktig multimeter, ett oscilloskop eller en certifierad energimätare. Målet är att kunna bygga projekt som förstår sin egen matning, kan upptäcka låg batterinivå, kan uppskatta strömförbrukning och kan logga säkra lågspänningsmätningar.

Kapitlet fungerar som stöd när du behöver mäta lågspända DC-system, uppskatta strömförbrukning, tolka batterinivå och välja mellan spänningsdelare, shuntmätning, digital mätkrets, Hall-sensor och färdig batterimodul.

## Förutsättningar

Du bör känna igen följande från tidigare kapitel:

- analog läsning och ADC-upplösning
- referensspänning och mätosäkerhet
- gemensam jord
- spänningsdelare
- filtrering och medelvärde
- I2C som buss för digitala sensormoduler
- skillnaden mellan kortets matning och signalnivåer

Det här kapitlet använder också en viktig säkerhetsregel:

Mät bara sådant du förstår elektriskt och som ligger inom säkra lågspänningsnivåer. Direkt mätning på nätspänning, elcentraler, vägguttag, okända batteripack eller kraftsystem ska inte göras med Arduino-projektkopplingar. Använd färdiga, isolerade och godkända mätlösningar om projektet behöver information från sådana system.

## Grundrelationerna

I praktiska Arduino-projekt räcker ofta tre relationer långt.

Spänning, ström och resistans hänger ihop genom Ohms lag:

```text
U = R * I
```

Effekt beräknas som spänning gånger ström:

```text
P = U * I
```

Energi kan uppskattas genom att summera effekt över tid:

```text
E = P * t
```

I svensk teknisk text används ofta `U` för spänning, `I` för ström och `P` för effekt. I engelska bibliotek och datablad används ofta `V`, `I` och `P`. I bokens kod använder vi engelska variabelnamn, men i förklaringen använder vi de svenska termerna.

Ett enkelt exempel:

- Ett projekt drivs med 5 V.
- Det drar 120 mA.
- Effekten är 5 V * 0,12 A = 0,6 W.
- Om det kör i 10 timmar används ungefär 6 Wh.

Detta är en idealiserad beräkning. I verkligheten påverkas resultatet av regulatorförluster, batteriets spänningskurva, temperatur, vilolägen, pulserande laster och mätfel.

## Vad vill du egentligen mäta?

Innan du väljer mätmetod behöver du formulera frågan. Många felval beror på att man mäter fel storhet.

| Fråga | Mätstorhet | Typisk lösning |
|---|---|---|
| Är batteriet på väg att ta slut? | Batterispänning eller batteristatus | Spänningsdelare, batteri-IC eller laddmodul |
| Hur mycket ström drar projektet just nu? | Ström | USB-mätare, multimeter, shuntbaserad sensor eller Hall-sensor |
| Hur mycket energi har projektet använt? | Energi över tid | Strömsensor plus tidsloggning |
| Varför startar kortet om när motorn går? | Spänningsfall och strömtoppar | Multimeter, oscilloskop, loggning och bättre matning |
| Hur mycket ström drar projektet i sleep? | Mycket låg ström | Multimeter med lågströmsområde eller specialiserad strömmätare |
| Är solpanelen tillräcklig? | Spänning, ström och energi över tid | Ström-/spänningssensor och loggning |

Som referens i boken använder vi tre nivåer:

- **Enkel mätning:** spänningsdelare och ADC.
- **Modulmätning:** färdig sensor som INA219/INA226 eller liknande.
- **Systemmätning:** loggning över tid, energiberäkning och koppling till strömbudget.

## Mäta spänning med ADC

En mikrokontroller kan ofta mäta spänning på en analog ingång, men bara inom ett begränsat intervall. På många 5 V-kort får ingången inte gå över 5 V. På många 3,3 V-kort får den inte gå över 3,3 V, och ibland ännu lägre beroende på kortets ADC och dämpning.

Det betyder att du aldrig ska koppla en okänd spänning direkt till en analog ingång.

För att mäta en högre DC-spänning använder man ofta en spänningsdelare.

```text
Vin ---- R1 ----o---- R2 ---- GND
                o---- A0
```

Spänningen vid A0 blir:

```text
Vout = Vin * R2 / (R1 + R2)
```

Om `R1` är 100 kΩ och `R2` är 47 kΩ blir delningsfaktorn:

```text
47 / (100 + 47) är ungefär 0,32
```

En batterispänning på 8,4 V blir då ungefär 2,7 V på A0. Det kan vara säkert för ett 3,3 V-kort om komponenterna och felmarginalerna är rimliga.

### Välj motstånd med marginal

En spänningsdelare ska inte dimensioneras exakt mot maxgränsen. Lämna marginal för:

- batteriet kan vara högre än nominell spänning när det är fulladdat
- resistorer har tolerans
- ADC-referensen kan variera
- brus och transienter kan ge korta toppar
- felkopplingar händer under prototypande

Om ett 3,3 V-kort ska mäta ett 2S Li-ion-batteri bör du dimensionera för mer än 8,4 V, inte bara för nominella 7,4 V.

### Hög resistans ger lägre belastning men sämre mätning

En spänningsdelare drar alltid lite ström. Om motstånden är låga belastar den batteriet mer. Om motstånden är höga blir mätningen känsligare för ADC-ingångens egenskaper, brus och läckströmmar.

I många experiment fungerar motstånd i storleksordningen tiotals till några hundra kiloohm bra. Vid batteridrivna projekt kan man också koppla spänningsdelaren via en transistor eller MOSFET så att den bara är aktiv när man mäter. Det hör ihop med kapitel 34 om strömförsörjning och batteridrift.

## Exempel: mäta batterispänning med spänningsdelare

Anta att vi vill mäta en extern batterispänning som delas ner till A0. Koden nedan använder tydliga konstanter så att kopplingen kan dokumenteras.

```cpp
const int batteryPin = A0;

const float adcReferenceVoltage = 3.3;
const int adcMaxValue = 1023;

// Vin ---- R1 ---- A0 ---- R2 ---- GND
const float r1Ohms = 100000.0;
const float r2Ohms = 47000.0;

float readBatteryVoltage() {
  const int sampleCount = 20;
  long total = 0;

  for (int i = 0; i < sampleCount; i++) {
    total += analogRead(batteryPin);
    delay(2);
  }

  float raw = total / float(sampleCount);
  float measuredAtPin = raw * adcReferenceVoltage / adcMaxValue;
  float dividerRatio = r2Ohms / (r1Ohms + r2Ohms);

  return measuredAtPin / dividerRatio;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  float batteryVoltage = readBatteryVoltage();

  Serial.print("Battery voltage: ");
  Serial.print(batteryVoltage, 2);
  Serial.println(" V");

  delay(1000);
}
```

Det här är ett pedagogiskt exempel. I ett riktigt projekt behöver du kontrollera ADC-upplösningen för kortet. Vissa kort använder 10 bitar som standard, andra kan använda 12 bitar eller konfigurerbar upplösning. Du behöver också kontrollera faktisk referensspänning och kalibrera mot multimeter om värdet ska vara mer än ungefärligt.

## ADC-upplösning och referensspänning

I kapitel 6 såg vi att ADC-värden inte är magiska. De är en kvantisering av en analog spänning relativt en referens.

Om referensen är 3,3 V och ADC:n är 10-bitars får du värden 0 till 1023. Varje steg motsvarar ungefär:

```text
3,3 V / 1024 är ungefär 0,0032 V
```

Men om spänningsdelaren delar ner batterispänningen med faktor 0,32 motsvarar ett ADC-steg ungefär:

```text
0,0032 V / 0,32 är ungefär 0,010 V
```

Det är fortfarande användbart för batteriövervakning, men inte nödvändigtvis för precisionsmätning.

För bättre mätning kan du:

- kalibrera mot en multimeter
- använda stabilare referensspänning
- använda extern ADC
- använda digital mätkrets
- filtrera över flera mätningar
- dokumentera toleranser i stället för att låtsas att värdet är exakt

## Batterispänning är inte samma sak som batteriprocent

Det är frestande att skriva kod som säger:

```text
3,0 V = 0 %
4,2 V = 100 %
```

För ett Li-ion-cellsexempel kan det se rimligt ut, men det är förenklat. Batteriers urladdningskurvor är inte linjära. Spänningen påverkas av kemi, temperatur, ålder, belastning och återhämtning efter last.

Olika batterityper beter sig olika:

| Batterityp | Typisk egenskap | Konsekvens för Arduino-projekt |
|---|---|---|
| Alkaline AA | Spänningen sjunker gradvis | Spänning kan ge grov status |
| NiMH AA | Ganska platt kurva under stor del av urladdningen | Procent från spänning blir osäker |
| Li-ion/LiPo | Tydlig men icke-linjär kurva | Kräver marginal och skydd |
| LiFePO4 | Plattare kurva än Li-ion | Spänning är grov indikator |
| Blybatteri | Beror starkt på last och vila | Kräver försiktig tolkning |

För bokens projekt räcker ofta tre statusnivåer bättre än falsk precision:

- **OK:** batteriet ligger inom normalt arbetsområde.
- **Lågt:** projektet bör minska aktivitet eller varna.
- **Kritiskt:** projektet bör spara data och stänga av säkert om möjligt.

## Exempel: batteristatus med hysteresis

Hysteresis förhindrar att status hoppar fram och tillbaka när spänningen ligger nära en gräns.

```cpp
enum BatteryState {
  BATTERY_OK,
  BATTERY_LOW,
  BATTERY_CRITICAL
};

BatteryState batteryState = BATTERY_OK;

BatteryState updateBatteryState(float voltage) {
  switch (batteryState) {
    case BATTERY_OK:
      if (voltage < 3.55) {
        batteryState = BATTERY_LOW;
      }
      break;

    case BATTERY_LOW:
      if (voltage < 3.35) {
        batteryState = BATTERY_CRITICAL;
      } else if (voltage > 3.70) {
        batteryState = BATTERY_OK;
      }
      break;

    case BATTERY_CRITICAL:
      if (voltage > 3.50) {
        batteryState = BATTERY_LOW;
      }
      break;
  }

  return batteryState;
}
```

Gränserna är exempel, inte universella rekommendationer. För ett riktigt batteri behöver du välja nivåer utifrån batterityp, skyddskrets, regulator och vilken minsta spänning projektet faktiskt tål.

## Mäta ström

Spänning mäts mellan två punkter. Ström mäts genom en del av kretsen. Det är en viktig skillnad.

För att mäta ström måste mätningen normalt placeras i serie med lasten, eller så behöver du en sensor som känner av magnetfältet runt en ledare. Det är därför strömmätning ofta känns mer besvärlig än spänningsmätning.

Det finns tre vanliga metoder i Arduino-projekt:

- multimeter eller USB-effektmätare för manuell mätning
- shuntmotstånd med förstärkare eller färdig mätkrets
- Hall-effektsensor för isolerad eller kontaktlös strömmätning

## Shuntmotstånd

Ett shuntmotstånd är ett litet känt motstånd som placeras i serie med lasten. När ström går genom motståndet uppstår ett litet spänningsfall.

```text
Vshunt = I * Rshunt
```

Om shunten är 0,1 Ω och strömmen är 500 mA blir spänningsfallet:

```text
0,5 A * 0,1 Ω = 0,05 V
```

Det är bara 50 mV. En vanlig Arduino-ADC kan ha svårt att mäta så små spänningar noggrant, särskilt om signalen ligger ovanpå en högre matningsspänning. Därför används ofta en förstärkare eller en färdig strömmätningskrets.

### High-side och low-side

En shunt kan placeras på högsidan eller lågsidan.

```text
High-side:
+V ---- shunt ---- load ---- GND

Low-side:
+V ---- load ---- shunt ---- GND
```

Low-side är enklare att mäta eftersom spänningsfallet ligger nära jord. Nackdelen är att lasten inte längre har exakt samma jord som resten av systemet. Det kan störa mätning, kommunikation eller styrning.

High-side bevarar lastens jord bättre men kräver mätkrets som klarar common-mode-spänningen. Färdiga kretsar som INA219/INA226-liknande moduler används ofta för detta.

## Digitala ström- och spänningssensorer

I Arduino-projekt är färdiga I2C-moduler ofta enklast. Många bygger på shuntmätning och kan rapportera busspänning, shuntspänning, ström och ibland effekt.

Typiska egenskaper:

- I2C-gränssnitt
- mätning av busspänning
- mätning av shuntspänning
- beräknad ström
- beräknad effekt
- konfigurerbar mätområde och upplösning
- färdiga bibliotek

Exempel på vanliga kretsfamiljer i hobbyprojekt är INA219 och INA226. Det exakta mätområdet beror på modulens shuntmotstånd, konfiguration och bibliotek.

### När digital mätkrets passar

Välj en INA219/INA226-liknande modul när:

- du vill mäta lågspänd DC-last
- du vill ha både spänning och ström
- du vill logga effekt över tid
- du vill slippa bygga egen analog förstärkning
- mätområdet passar projektets ström och spänning

Välj något annat när:

- strömmen är mycket hög
- spänningen ligger utanför modulens område
- lasten är AC eller nätspänning
- du behöver galvanisk isolation
- du behöver mäta mycket korta strömtoppar
- noggrannheten är säkerhetskritisk eller debiteringsgrundande

## Exempel: läsa INA219-liknande modul

Kodens exakta bibliotek kan variera. Exemplet visar ett vanligt kodmönster: initiera sensorn, läs busspänning, shuntspänning, ström och effekt.

```cpp
#include <Wire.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 powerSensor;

void setup() {
  Serial.begin(115200);

  if (!powerSensor.begin()) {
    Serial.println("Could not find INA219 sensor");
    while (true) {
      delay(100);
    }
  }

  Serial.println("INA219 ready");
}

void loop() {
  float busVoltage = powerSensor.getBusVoltage_V();
  float shuntVoltageMv = powerSensor.getShuntVoltage_mV();
  float currentMa = powerSensor.getCurrent_mA();
  float powerMw = powerSensor.getPower_mW();

  Serial.print("Bus voltage: ");
  Serial.print(busVoltage, 3);
  Serial.print(" V, shunt: ");
  Serial.print(shuntVoltageMv, 3);
  Serial.print(" mV, current: ");
  Serial.print(currentMa, 1);
  Serial.print(" mA, power: ");
  Serial.print(powerMw, 1);
  Serial.println(" mW");

  delay(1000);
}
```

Det här är ett exempel på biblioteksmönster, inte ett löfte om att alla moduler beter sig likadant. Kontrollera alltid modulens koppling, shuntvärde, spänningsgränser, bibliotek och kalibreringsläge.

## Hall-effektsensorer för ström

En Hall-effektsensor mäter magnetfält som uppstår av ström. I många strömsensormoduler går ledaren genom eller nära sensorn. Fördelen är att mätningen kan vara elektriskt isolerad från mätsignalen, beroende på modulens konstruktion.

Hall-baserade strömsensorer passar ofta när:

- strömmen är högre än vad en liten shuntmodul passar för
- du vill minska spänningsfallet i mätningen
- du vill ha isolation mellan last och mikrokontroller
- du mäter både positiv och negativ ström i vissa applikationer

De har också nackdelar:

- offset kan driva med temperatur
- nollpunkten kan behöva kalibreras
- små strömmar kan vara svåra att mäta noggrant
- analoga varianter kräver ADC och filtrering
- moduler varierar mycket i kvalitet

För hobbyprojekt används Hall-sensorer ofta för grov strömdetektering: “drar motorn ungefär så mycket som väntat?” snarare än precisionsmätning.

## Effekt och energi över tid

Effekt är ögonblicksvärde. Energi kräver tid.

Om du läser spänning och ström varje sekund kan du uppskatta energi genom att summera effekt över tid.

```text
Wh += W * hours
```

En sekund är 1/3600 timme. Om projektet drar 0,5 W under en sekund adderas:

```text
0,5 / 3600 är ungefär 0,000139 Wh
```

Kodmönstret kan se ut så här:

```cpp
float energyWh = 0.0;
unsigned long lastSampleMs = 0;

void updateEnergy(float voltage, float currentA) {
  unsigned long now = millis();

  if (lastSampleMs == 0) {
    lastSampleMs = now;
    return;
  }

  unsigned long elapsedMs = now - lastSampleMs;
  lastSampleMs = now;

  float powerW = voltage * currentA;
  float elapsedHours = elapsedMs / 3600000.0;

  energyWh += powerW * elapsedHours;
}
```

Det här ger en uppskattning, inte en certifierad energimätning. Noggrannheten beror på mätfel i både spänning och ström, samplingstakt, lastens variation och sensorns kalibrering.

## Strömtoppar och varför mätningen kan ljuga

Många Arduino-system drar inte konstant ström. Ett ESP32-kort kan dra mer när Wi-Fi sänder. En motor kan dra mycket mer vid start än under stabil drift. En LED-strip kan dra kraftigt olika beroende på färg och ljusstyrka. En sensor kan ha korta mätpulser.

Om du läser ström en gång per sekund kan du missa snabba toppar. Det kan ge två problem:

- energiberäkningen blir för låg
- du missar orsaken till att systemet startar om

När du misstänker strömtoppar behöver du ofta:

- tätare sampling
- kondensatorer nära lasten
- kraftigare regulator
- separat matning för last
- oscilloskop eller snabbare mätutrustning
- loggning av minsta spänning över tid

Ett enkelt Arduino-knep är att logga lägsta uppmätta batterispänning eller matningsspänning under en period. Det fångar inte alla transienter, men det kan visa om systemet sjunker under en kritisk nivå.

## Mäta egen matningsspänning

Ibland vill projektet veta sin egen matningsspänning. På vissa mikrokontrollers kan man mäta en intern referens mot matningen, eller matningen mot en intern referens. Hur detta görs varierar kraftigt mellan kortfamiljer.

På klassiska AVR-baserade kort finns tekniker för att läsa intern bandgap-referens. På ESP32, RP2040 och moderna Arduino-kort ser lösningarna annorlunda ut och är beroende av kärna, ADC, kalibrering och kortets matningsarkitektur.

Därför använder vi i den här boken en enklare huvudregel:

- Om du behöver portabel och tydlig batterimätning, använd en extern spänningsdelare eller mätmodul.
- Om du optimerar för ett specifikt kort, dokumentera exakt metod i projektets egna anteckningar så att mätningen går att återskapa senare.
- Om värdet ska styra säker avstängning, verifiera med multimeter och praktiskt test.

## Mäta batteridrivna projekt

Batteridrivna Arduino-projekt kräver mer än en spänningsmätning. Du behöver ofta veta:

- batterityp
- fulladdad spänning
- lägsta säkra spänning
- regulatorns dropout-spänning
- kortets minsta stabila matning
- ström i aktivt läge
- ström i vänteläge
- ström vid radiosändning eller motorstart
- hur ofta sensorer och utenheter aktiveras

Ett projekt kan ha låg genomsnittlig förbrukning men ändå kräva hög toppström. Det är särskilt vanligt med radio, motorer, LED-strippar och sensorer som värmer eller pulsar.

## Enkel strömbudget

En strömbudget är en uppskattning av hur mycket ström projektet använder i olika lägen.

| Del | Ström | Aktiv tid | Kommentar |
|---|---|---|---|
| Mikrokontroller aktiv | 80 mA | 10 s per minut | Exempelvärde |
| Mikrokontroller sleep | 2 mA | 50 s per minut | Beror mycket på kort |
| Sensor | 5 mA | 10 s per minut | Kan slås av mellan mätningar |
| LED-status | 10 mA | 2 s per minut | Kan dimmas eller blinkas kort |
| Radio | 180 mA | 1 s per minut | Toppström viktig |

Denna tabell är inte en beräkning för ett specifikt kort. Den visar tankemodellen. I kapitel 34 går vi djupare in i strömförsörjning, regulatorer, batteridrift och robust konstruktion.

## Säker mätkoppling: batteri- och lastmonitor

Det här referensmönstret visar en enkel monitor som mäter batterispänning via spänningsdelare och visar status med seriell utskrift och LED. Om du har en INA219/INA226-liknande modul kan du också mäta lastström.

### Vad kopplingen visar

Kopplingen visar hur du kan:

- mäta en spänning via spänningsdelare
- räkna om ADC-värde till faktisk spänning
- använda hysteresis för batteristatus
- skilja mellan mätvärde och tolkad status
- se hur en last påverkar batteri- eller matningsspänning

### Det här används i exemplet

- Arduino-kompatibelt kort
- två resistorer för spänningsdelare, exempelvis 100 kΩ och 47 kΩ
- LED med seriemotstånd, eller inbyggd LED
- extern lågspänningskälla eller batterihållare inom säkert område
- multimeter för kontrollmätning
- valfritt: INA219/INA226-liknande I2C-modul
- valfritt: liten DC-last, LED-stripsegment eller motor med separat och säker matning

Använd inte nätspänning i det här mönstret.

### Kopplingsprincip

För spänningsmätningen:

```text
Batteri + ---- R1 ----o---- R2 ---- Batteri -
                      o---- A0
```

Koppla batteriets minus till kortets GND om batteriet också är referens för mätningen. Kontrollera att spänningen vid A0 aldrig kan överstiga kortets tillåtna nivå.

För I2C-mätmodul följer du modulens dokumentation. Grundprincipen är att sensorn placeras i serie med lasten enligt modulens märkning. Kontrollera särskilt vilken sida som är matning och vilken sida som är last.

### Kod

Koden nedan mäter batterispänning via A0 och använder en LED för status. Anpassa `adcReferenceVoltage`, `adcMaxValue`, `r1Ohms` och `r2Ohms` till ditt kort och din koppling.

```cpp
const int batteryPin = A0;
const int statusLedPin = LED_BUILTIN;

const float adcReferenceVoltage = 3.3;
const int adcMaxValue = 1023;

const float r1Ohms = 100000.0;
const float r2Ohms = 47000.0;

enum BatteryState {
  BATTERY_OK,
  BATTERY_LOW,
  BATTERY_CRITICAL
};

BatteryState batteryState = BATTERY_OK;
unsigned long lastPrintMs = 0;
unsigned long lastBlinkMs = 0;
bool ledOn = false;

float readAveragedAdcVoltage() {
  const int sampleCount = 30;
  long total = 0;

  for (int i = 0; i < sampleCount; i++) {
    total += analogRead(batteryPin);
    delay(2);
  }

  float raw = total / float(sampleCount);
  return raw * adcReferenceVoltage / adcMaxValue;
}

float readBatteryVoltage() {
  float pinVoltage = readAveragedAdcVoltage();
  float dividerRatio = r2Ohms / (r1Ohms + r2Ohms);

  return pinVoltage / dividerRatio;
}

BatteryState updateBatteryState(float voltage) {
  switch (batteryState) {
    case BATTERY_OK:
      if (voltage < 3.55) {
        batteryState = BATTERY_LOW;
      }
      break;

    case BATTERY_LOW:
      if (voltage < 3.35) {
        batteryState = BATTERY_CRITICAL;
      } else if (voltage > 3.70) {
        batteryState = BATTERY_OK;
      }
      break;

    case BATTERY_CRITICAL:
      if (voltage > 3.50) {
        batteryState = BATTERY_LOW;
      }
      break;
  }

  return batteryState;
}

const char* batteryStateName(BatteryState state) {
  switch (state) {
    case BATTERY_OK:
      return "OK";
    case BATTERY_LOW:
      return "LOW";
    case BATTERY_CRITICAL:
      return "CRITICAL";
    default:
      return "UNKNOWN";
  }
}

void updateStatusLed(BatteryState state) {
  unsigned long now = millis();

  if (state == BATTERY_OK) {
    digitalWrite(statusLedPin, HIGH);
    return;
  }

  unsigned long interval = state == BATTERY_LOW ? 600 : 150;

  if (now - lastBlinkMs >= interval) {
    lastBlinkMs = now;
    ledOn = !ledOn;
    digitalWrite(statusLedPin, ledOn ? HIGH : LOW);
  }
}

void setup() {
  pinMode(statusLedPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  float batteryVoltage = readBatteryVoltage();
  BatteryState state = updateBatteryState(batteryVoltage);

  updateStatusLed(state);

  unsigned long now = millis();
  if (now - lastPrintMs >= 1000) {
    lastPrintMs = now;

    Serial.print("Battery voltage: ");
    Serial.print(batteryVoltage, 2);
    Serial.print(" V, state: ");
    Serial.println(batteryStateName(state));
  }
}
```

### Kontrollera mätningen

Gör minst tre mätningar:

1. Mät spänningen direkt med multimeter.
2. Läs Arduino-värdet i seriell monitor.
3. Beräkna skillnaden och notera om du behöver kalibrera.

Dokumentera:

- kortmodell
- ADC-upplösning
- antagen referensspänning
- R1 och R2
- uppmätt batterispänning
- uppmätt spänning vid A0
- skillnad mot multimeter
- valda statusgränser

### Variation med last

Lägg till en kontrollerad lågspänningslast och observera hur spänningen påverkas när lasten aktiveras. Det kan vara en liten LED-last, ett relä utan nätansluten last eller en motor med separat säker matning.

Frågor att undersöka:

- sjunker spänningen när lasten startar?
- återhämtar sig spänningen när lasten stängs av?
- behöver statuslogiken filtrering eller hålltid?
- är matningen dimensionerad för toppströmmen?

## Riskkontroll före mätning

Mätning känns passiv, men fel mätkoppling kan skada både kort och mätutrustning.

- Kontrollera om du mäter spänning, ström, effekt eller energi.
- Kontrollera högsta möjliga spänning innan signalen når ADC eller mätmodul.
- Kontrollera att strömmätning sker i rätt strömväg och att mätområdet räcker.
- Kontrollera shuntens effektförlust om du mäter större strömmar.
- Kontrollera om mätningen kräver gemensam jord eller isolation.
- Testa först med låg spänning och känd last.
- Mät aldrig okänd nätspänning eller stora batteripack med hobbykopplingar.

När mätningen påverkar säkerhet eller batteriskydd bör du använda färdig mätmodul, säkring och marginal.

## Vanliga misstag

- **Misstag: Att koppla en okänd spänning direkt till analog ingång.**
  - **Varför det händer:** Det är lätt att tänka att ADC:n “mäter spänning” utan att tänka på maxgränsen.
  - **Hur man undviker det:** Använd spänningsdelare, skydd och multimeter. Kontrollera högsta möjliga spänning innan du kopplar.

- **Misstag: Att glömma gemensam jord.**
  - **Varför det händer:** Batteri, sensor och Arduino kan se ut som separata system.
  - **Hur man undviker det:** Koppla gemensam referens när signalen kräver det, men var försiktig med system där isolation behövs.

- **Misstag: Att tolka batterispänning som exakt procent.**
  - **Varför det händer:** Procent känns användarvänligt.
  - **Hur man undviker det:** Använd hellre statusnivåer eller batterispecifik urladdningskurva.

- **Misstag: Att välja fel mätmetod för ström.**
  - **Varför det händer:** Spänning och ström blandas ofta ihop.
  - **Hur man undviker det:** Kom ihåg att ström mäts genom lasten, inte bara på en punkt.

- **Misstag: Att missa strömtoppar.**
  - **Varför det händer:** Medelvärden och långsam sampling ser stabila ut.
  - **Hur man undviker det:** Testa startögonblick, radiosändning, motorstart och maximal LED-ljusstyrka separat.

- **Misstag: Att använda en sensor utanför sitt mätområde.**
  - **Varför det händer:** Många moduler säljs som “current sensor” utan att användaren kontrollerar maxström, maxspänning och shuntvärde.
  - **Hur man undviker det:** Läs modulens specifikation och lämna marginal.

- **Misstag: Att mäta nätspänning med hobbykoppling.**
  - **Varför det händer:** Det finns många exempel online som ser enkla ut.
  - **Hur man undviker det:** Gör det inte. Använd godkända isolerade produkter och etablerade säkerhetsmetoder.

## Valguide

Välj **spänningsdelare** när:

- du mäter enkel DC-spänning inom säkert område
- du kan beräkna maxspänning med marginal
- noggrannhetskraven är måttliga
- du vill förstå grunden

Välj **INA219/INA226-liknande modul** när:

- du vill mäta både spänning och ström i lågspända DC-projekt
- I2C passar i systemet
- du vill logga effekt över tid
- modulens mätområde passar lasten

Välj **Hall-effektsensor** när:

- strömmen är högre
- isolation eller låg påverkan på kretsen är viktig
- grov strömmätning räcker
- du accepterar offset och kalibrering

Välj **multimeter eller specialiserad strömmätare** när:

- du felsöker mycket låg ström
- du behöver kontrollera sleep-förbrukning
- du vill verifiera Arduino-systemets egna mätningar
- resultatet behöver högre tillförlitlighet

Välj **färdig batteri- eller laddningsmodul med statusutgång** när:

- projektet ska drivas av Li-ion/LiPo
- laddning, skydd och batteristatus är viktigare än att bygga allt själv
- du vill minska risken i batterihanteringen

Snabb beslutsrad:

- Mät **spänning** först när du misstänker matningsfall eller batterinivåproblem.
- Mät **ström** när lasten beter sig oväntat, regulatorn blir varm eller batteritiden inte stämmer.
- Mät **effekt över tid** när energibudget, sleep-läge eller fältdrift är viktig.
- Använd **extern modul** när mätningen ska ingå i projektet, och **multimeter** när du verifierar projektet.

## Snabbreferens

| Mätning | Enkel metod | Bättre metod | Viktig risk |
|---|---|---|---|
| DC-spänning | Spänningsdelare till ADC | Extern ADC eller digital mätmodul | För hög spänning på ADC |
| Batteristatus | Spänning och statusgränser | Batteri-IC eller kalibrerad kurva | Falsk batteriprocent |
| DC-ström | Multimeter i serie | Shuntmodul eller Hall-sensor | Felkoppling eller för hög ström |
| Effekt | Spänning * ström | Digital power monitor | Missade toppar |
| Energi | Summerad effekt över tid | Dataloggning med kalibrerad sensor | Sampling och mätfel |
| Sleep-ström | Multimeter | Specialiserad lågströmsmätare | Instrumentets påverkan |

## Snabb sammanfattning

- Spänning mäts mellan två punkter; ström mäts genom en del av kretsen.
- En analog ingång får aldrig utsättas för högre spänning än kortet tål.
- Spänningsdelare är enkel och användbar, men kräver marginal, kalibrering och förståelse för ADC:n.
- Batteriprocent från spänning är ofta missvisande; statusnivåer är ofta bättre.
- Shuntmätning ger ström genom ett känt litet motstånd, men små spänningsfall kräver bra mätkrets.
- INA219/INA226-liknande moduler är praktiska för lågspänd DC-mätning av spänning, ström och effekt.
- Hall-effektsensorer kan vara bättre för högre strömmar eller när isolation är viktig.
- Energi beräknas genom att summera effekt över tid, men sampling och mätfel påverkar resultatet.
- Strömtoppar kan vara viktigare än medelström när systemet startar om eller beter sig instabilt.
- Direkt mätning av nätspänning hör inte hemma i Arduino-prototyper.

## Säkerhetsruta: mät inte okända eller farliga spänningar direkt

Mätkapitel lockar lätt till att ansluta allt möjligt till Arduino-kortet. Gör inte det. Mät bara spänningar och strömmar inom komponenternas säkra område och med tydlig gemensam referens.

Nätspänning, stora batteripack, induktiva laster och okända energikällor kräver isolering, rätt mätutrustning och skydd. För bokens experiment används lågspänning, begränsad ström och färdiga sensormoduler.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Beror på mätområde och modul |
| Typiskt gränssnitt | Analogt, I2C, Hall-sensor eller shunt |
| Välj när | du behöver förstå förbrukning, batteri eller lastström |
| Välj inte när | mätningen gäller farlig spänning utan isolering |
| Vanliga fel | fel shuntområde, gemensam jord-problem, överspänning på ADC |
| Alternativ att överväga | USB-mätare, laboratorieaggregat, färdig energimodul |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När mätningen går via ADC, börja med kapitel 6 om upplösning, referensspänning och kalibrering.
- När signalen behöver spänningsdelare, filter, förstärkning eller nivåanpassning, använd kapitel 33.
- När mätningen ska förklara omstarter, batteritid eller instabil drift, jämför med kapitel 34 och 35.
- När mätvärden ska loggas eller visas över tid, gå vidare till kapitel 29 och 32.
