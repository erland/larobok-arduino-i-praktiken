# 30. I/O-expansion, shift registers och multiplexers

## Expansionsöversikt
Förr eller senare räcker pinnarna inte till. Ett projekt som började med en knapp, en LED och en sensor växer till ett litet styrsystem med tio knappar, sexton indikatorer, flera reläer, en display och några sensorer på samma gång. Då är det lätt att tänka att lösningen alltid är ett större Arduino-kort. Ibland är det rätt. Men ofta är det bättre att låta en extern krets ta hand om fler in- och utgångar.

I/O-expansion handlar om att ge mikrokontrollern fler anslutningspunkter utan att byta hela plattformen. Det kan göras på flera sätt:

- med ett shift register som omvandlar några få signaler till många digitala utgångar
- med ett parallell-till-seriellt shift register som läser många digitala ingångar
- med en I2C-baserad I/O-expander som ger extra portar via en adress på I2C-bussen
- med en analog multiplexer som låter en ADC-ingång läsa många analoga signaler
- med en digital multiplexer eller demultiplexer som väljer mellan flera signalvägar

Det här kapitlet är viktigt eftersom I/O-expansion inte bara är en fråga om antal pinnar. Det handlar också om timing, ström, felsökning, adresskonflikter, signalriktning, kodstruktur och robusthet. En väl vald expander kan göra ett projekt enklare och mer modulärt. En dåligt vald expander kan göra felsökningen svårare än om du hade valt ett större kort från början.

Målet är inte att du ska memorera varje krets. Målet är att du ska kunna se mönstret: när du behöver fler utgångar, fler ingångar, fler analoga kanaler eller en mer modulär koppling, finns det ofta en liten krets som är bättre än att pressa in allt direkt på mikrokontrollern.

Kapitlet fungerar som stöd när du behöver välja mellan I/O-expander, shift register och multiplexer, avgöra när ett större kort är bättre och hålla kod för expanderad I/O begriplig.

## Förutsättningar

Du bör känna igen digital I/O, pull-up/pull-down, flytande ingångar, timing samt grunderna i I2C och SPI. Kapitlet bygger också på tanken från tidigare kapitel att fler anslutningar inte automatiskt gör ett projekt bättre; expansion ska väljas när den löser ett konkret pin-, kabel- eller modularitetsproblem.

## Överblick: fyra sätt att få fler pinnar

Det finns flera komponenttyper som löser olika varianter av samma problem. Namnen liknar ibland varandra, men de passar olika situationer.

| Teknik | Typiskt exempel | Bra för | Vanligt gränssnitt |
|---|---|---|---|
| Seriellt till parallellt shift register | 74HC595 | Många digitala utgångar | Data, klocka, latch |
| Parallellt till seriellt shift register | 74HC165 | Många digitala ingångar | Load, klocka, data |
| I2C-I/O-expander | MCP23017, PCF8574 | Extra digitala in- och utgångar | I2C |
| Analog multiplexer | CD74HC4067, 74HC4051 | Många analoga eller enkla digitala signaler | Adresspinnar och signalpinne |

Valet beror på vad du faktiskt behöver.

- Behöver du tända många LED eller styra många logiska utgångar? Börja med 74HC595 eller en I/O-expander.
- Behöver du läsa många knappar? Titta på 74HC165, MCP23017, PCF8574 eller en knappmatris.
- Behöver du läsa många potentiometrar eller analoga sensorer? Titta på analog multiplexer.
- Behöver du både ingångar och utgångar, gärna med enklare kod? Titta på MCP23017.
- Behöver du minimalt antal komponenter och billig expansion? Titta på PCF8574 eller 74HC-serien.
- Behöver du snabb, exakt eller parallell styrning? Överväg ett större kort eller en specialiserad drivkrets.

## När du bör välja I/O-expansion

I/O-expansion är särskilt användbart när projektet har många enkla signaler. Det kan vara knappar, DIP-switchar, status-LED, relästyrsignaler, chip select-signaler, enkla givaringångar eller val av signalväg.

Bra situationer är till exempel:

- en kontrollpanel med många knappar
- ett instrument med många statuslampor
- en liten testjigg som ska slå av och på flera signaler
- en sensorstation där kortet har få lediga GPIO
- ett projekt där du vill behålla ett litet kort men behöver fler pinnar
- en modulär konstruktion där I/O ska ligga på ett separat kort
- ett utbildningsexperiment där du vill visa seriell styrning av parallella signaler

I/O-expansion kan också göra konstruktionen tydligare. Om alla knappar sitter på en I2C-expander och alla LED på två shift register blir det enklare att se vilka delar av systemet som hör ihop.

## När du bör välja något annat

I/O-expansion är inte alltid rätt svar. Ibland är ett större eller mer passande utvecklingskort enklare.

Välj hellre ett annat kort när:

- du behöver många snabba signaler med exakt timing
- du behöver många PWM-kanaler
- du behöver många riktiga ADC-kanaler med bra noggrannhet
- du behöver driva laster med hög ström
- du redan har ett kort med tillräckligt många pinnar
- extra kretsar gör systemet svårare att bygga än ett större kort
- projektet ska felsökas av nybörjare och enkelhet är viktigare än komponentkostnad

Det är också vanligt att blanda lösningar. Ett Arduino Mega kan ge många pinnar direkt, medan ett litet ESP32-kort kan använda I/O-expansion för en kontrollpanel. Ett RP2040-baserat kort kan ha många GPIO men ändå använda en expander för att hålla kablaget till en frontpanel rent och modulärt.

## Shift register: fler utgångar med 74HC595

Ett shift register är en krets som flyttar bitar ett steg i taget. Det klassiska exemplet för Arduino är 74HC595, som ofta används för att få åtta digitala utgångar från tre mikrokontrollerpinnar.

Du skickar in en bitström på en datapinne. För varje klockpuls flyttas bitarna ett steg. När alla åtta bitar är på plats aktiverar du en latch-signal så att utgångarna uppdateras samtidigt.

Det praktiska resultatet är att du kan styra åtta utgångar med tre pinnar:

- data
- clock
- latch

74HC595 passar särskilt bra för LED, logiska styrsignaler och chip select-liknande signaler. Den är också pedagogiskt bra, eftersom den gör relationen mellan bitar och fysiska utgångar tydlig.

### Grundidé

Tänk dig att du vill tända LED 0, 3 och 7. Då kan du skapa ett byte där varje bit representerar en utgång.

```cpp
byte outputState = 0b10001001;
```

När detta byte skickas till ett 74HC595 hamnar varje bit på en utgång. Exakt vilken bit som hamnar på vilken pinne beror på koppling och bitordning.

### Typisk koppling

En vanlig koppling använder dessa Arduino-pinnar:

| Arduino-pin | 74HC595-signal | Syfte |
|---|---|---|
| 8 | Latch | Uppdaterar utgångarna |
| 11 | Data | Skickar bitar |
| 12 | Clock | Flyttar in bitar |
| 5 V eller 3,3 V | VCC | Matning enligt vald logiknivå |
| GND | GND | Gemensam jord |
| GND | OE | Aktiverar utgångar |
| VCC | MR | Hindrar reset |

OE betyder output enable och MR betyder master reset. I enkla tester kopplas OE ofta till GND och MR till VCC, men i mer avancerade projekt kan de styras av mikrokontrollern.

### Exempel: åtta LED via 74HC595

Följande kod visar grundprincipen. Varje LED ska ha lämpligt seriemotstånd. Kretsens totala strömgränser måste respekteras, så använd låga LED-strömmar och driv inte stora laster direkt.

```cpp
const int latchPin = 8;
const int dataPin = 11;
const int clockPin = 12;

byte outputState = 0;

void writeOutputs(byte value) {
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, MSBFIRST, value);
  digitalWrite(latchPin, HIGH);
}

void setup() {
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);

  writeOutputs(outputState);
}

void loop() {
  for (int bitIndex = 0; bitIndex < 8; bitIndex++) {
    outputState = 1 << bitIndex;
    writeOutputs(outputState);
    delay(150);
  }
}
```

Det här är inte den mest avancerade koden, men den är bra som första test. Den bekräftar att data, clock och latch sitter rätt.

### Flera 74HC595 i kedja

En styrka med 74HC595 är att flera kretsar kan kopplas i kedja. Då kan du få 16, 24 eller fler utgångar med samma tre styrpinnar. Data skickas genom den första kretsen vidare till nästa.

Koden behöver då skicka flera byte innan latch aktiveras.

```cpp
const int latchPin = 8;
const int dataPin = 11;
const int clockPin = 12;

void writeTwoRegisters(byte highByte, byte lowByte) {
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, MSBFIRST, highByte);
  shiftOut(dataPin, clockPin, MSBFIRST, lowByte);
  digitalWrite(latchPin, HIGH);
}
```

Bitordningen kan kännas förvirrande första gången. Om LED-mönstret går åt “fel håll” är det sällan ett stort problem. Antingen ändrar du bitordning i koden eller dokumenterar hur dina utgångar är mappade.

## Läsa många ingångar med 74HC165

Om 74HC595 gör om seriell data till parallella utgångar gör 74HC165 ungefär motsatsen. Den läser flera parallella ingångar och skickar ut dem seriellt till mikrokontrollern.

Det passar för:

- många knappar
- DIP-switchar
- enkla digitala givare
- paneler där flera tillstånd ska läsas samtidigt

Grundidén är att kretsen först fångar läget på sina ingångar. Sedan klockar mikrokontrollern ut bitarna en i taget.

### Typisk struktur

Du använder ofta tre signaler:

- load eller latch för att fånga ingångsläget
- clock för att skifta ut bitarna
- data från shiftregistret till mikrokontrollern

Det är viktigt att varje ingång har ett definierat läge. Knappar behöver pull-up eller pull-down. Annars läser shiftregistret flytande signaler och resultatet blir opålitligt.

### Exempel: läsa åtta knappar

```cpp
const int loadPin = 8;
const int clockPin = 12;
const int dataPin = 11;

byte readInputs() {
  digitalWrite(loadPin, LOW);
  delayMicroseconds(5);
  digitalWrite(loadPin, HIGH);

  byte value = 0;

  for (int bitIndex = 0; bitIndex < 8; bitIndex++) {
    value <<= 1;

    if (digitalRead(dataPin) == HIGH) {
      value |= 1;
    }

    digitalWrite(clockPin, HIGH);
    delayMicroseconds(2);
    digitalWrite(clockPin, LOW);
  }

  return value;
}

void setup() {
  pinMode(loadPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, INPUT);

  digitalWrite(loadPin, HIGH);
  digitalWrite(clockPin, LOW);

  Serial.begin(115200);
}

void loop() {
  byte inputs = readInputs();

  Serial.print("Inputs: ");
  Serial.println(inputs, BIN);

  delay(100);
}
```

I ett verkligt knappsystem behöver du också debouncing. Det kan göras i kod på samma sätt som för vanliga digitala ingångar, men nu gäller det bitar i ett byte i stället för enskilda Arduino-pinnar.

## I2C-expander: MCP23017

MCP23017 är en populär I2C-baserad I/O-expander med 16 digitala I/O-pinnar. Den är mer avancerad än ett enkelt shift register. Den har register för riktning, pullups, utgångsvärden, ingångsvärden och ibland interruptfunktioner beroende på bibliotek och konfiguration.

Den passar när du vill ha många digitala in- och utgångar med relativt enkel kabeldragning.

Fördelar:

- 16 I/O på en enda I2C-adress
- varje pinne kan ofta konfigureras som ingång eller utgång
- interna pullups finns tillgängliga
- flera kretsar kan ofta användas på samma buss med olika adresser
- kod kan bli tydligare än med rå bit-skiftning

Nackdelar:

- långsammare än direkt GPIO
- beroende av I2C-bussen
- adresskonflikter kan uppstå
- kräver bibliotek eller registerkod
- inte avsedd för hög lastström

### När MCP23017 är ett bra val

MCP23017 är ofta ett bra val för kontrollpaneler. Du kan koppla många knappar, status-LED, små styrsignaler eller enkla väljare till samma expander. Om du bygger ett projekt med display, encoder, några knappar och flera LED kan en I/O-expander göra huvudkortets pinout mycket renare.

Den är också bra när mikrokontrollern har få pinnar, till exempel på ett litet ESP8266- eller XIAO-kort.

### Exempel: kapsla in expanderad I/O

Biblioteken varierar, men följande exempel visar principen med ett vanligt MCP23017-biblioteksmönster. Anpassa include-fil och klassnamn efter det bibliotek du använder.

```cpp
#include <Wire.h>
#include <Adafruit_MCP23X17.h>

Adafruit_MCP23X17 io;

const int ledPin = 0;
const int buttonPin = 8;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  if (!io.begin_I2C(0x20)) {
    Serial.println("MCP23017 not found");
    while (true) {
      delay(100);
    }
  }

  io.pinMode(ledPin, OUTPUT);
  io.pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  bool pressed = io.digitalRead(buttonPin) == LOW;

  io.digitalWrite(ledPin, pressed ? HIGH : LOW);

  delay(20);
}
```

Det här liknar vanlig Arduino-kod. Det är också poängen: en bra expanderlösning gör resten av programmet begripligt.

## I2C-expander: PCF8574

PCF8574 är en enklare I2C-expander med åtta I/O-linjer. Den används ofta i billiga moduler, särskilt LCD-backpacks för 16x2-LCD. Den kan också användas för knappar, små utgångar och enklare paneler.

PCF8574 är praktisk men har ett annorlunda I/O-beteende än många förväntar sig. Den beskrivs ofta som quasi-bidirectional. Det betyder förenklat att samma pinne kan fungera som ingång eller utgång beroende på hur den skrivs och belastas, men den beter sig inte exakt som en vanlig Arduino-pin.

Fördelar:

- billig
- enkel
- vanligt förekommande
- fungerar bra för många lågkravsprojekt
- används i många LCD-I2C-moduler

Nackdelar:

- bara åtta I/O per krets
- svagare och mer speciellt utgångsbeteende än många väntar sig
- mindre flexibel än MCP23017
- bibliotekskvalitet varierar
- bör inte användas som allmän högeffektsutgång

### När PCF8574 passar

PCF8574 passar när du behöver några extra digitala signaler och kraven är enkla. Den är särskilt vanlig när du köper en billig I2C-LCD-modul. Då behöver du oftast inte tänka på kretsen direkt, men det är bra att förstå att LCD-modulen egentligen drivs via en sådan expander.

För egna konstruktioner är MCP23017 ofta tydligare om du behöver mer kontroll. PCF8574 är bäst när låg kostnad, enkelhet och tillgänglighet är viktigare än flexibilitet.

## I2C-expander: PCF8575

PCF8575 är nära släkt med PCF8574, men ger 16 I/O-linjer i stället för 8. Den dyker ofta upp som enkel I2C-expander när du vill ha fler digitala signaler utan att gå hela vägen till en mer funktionsrik krets som MCP23017.

Tänk på PCF8575 som en större enkel expander, inte som en ersättare för alla specialkretsar. Den passar bra för enkla digitala signaler, knappar, LED-indikeringar, små styrsignaler och långsamma paneler där I2C-hastigheten räcker.

Fördelar:

- 16 I/O på en I2C-krets
- enkel att använda i många praktiska projekt
- bra när PCF8574-liknande moduler inte räcker till
- minskar antalet ledningar till knapp- och LED-paneler

Begränsningar:

- ersätter inte PWM-drivers
- ska inte driva hög ström direkt
- passar inte snabb sampling eller tidskritiska signaler
- har enklare I/O-beteende än mer avancerade expandrar
- kräver att du kontrollerar bibliotek, adress och logiknivå för just din modul

### När PCF8575 passar

PCF8575 passar när du behöver många enkla digitala signaler och kan acceptera att uppdateringen går via I2C. Den är ett rimligt val för kontrollpaneler, status-LED, relästyrsignaler via separat drivkrets och långsamma digitala ingångar.

Den är däremot fel val om du behöver mjuk PWM på många kanaler, läsa snabba pulser, driva motorer direkt eller samla in tidskritiska signaler. Då är en PWM-driver, en interruptkapabel I/O-expander, en specialkrets eller ett större mikrokontrollerkort oftast bättre.

## Analoga multiplexers

En digital I/O-expander ger fler digitala pinnar. En analog multiplexer löser ett annat problem: den låter flera signaler dela på samma analoga ingång.

Vanliga kretsar är till exempel:

- 74HC4051, ofta 8 kanaler
- CD74HC4067, ofta 16 kanaler
- 74HC4052, två separata 4-kanals multiplexers
- 74HC4053, tre separata 2-kanals switchar

En analog multiplexer fungerar som en styrbar signalväljare. Du väljer kanal med adresspinnar, väntar kort på att signalen ska stabiliseras och läser sedan den gemensamma signalpinnen med ADC.

### När analog multiplexer passar

En analog multiplexer passar bra för:

- många potentiometrar
- flera enkla analoga sensorer
- resistiva sensormatriser
- testpunkter där bara en signal behöver läsas åt gången
- experiment där hastigheten inte är extremt hög

Den passar sämre för:

- mycket svaga signaler
- signaler med höga krav på noggrannhet
- snabba signaler
- långa kablar utan filtrering
- sensorer som inte tål att kopplas via switchresistans
- system där flera signaler måste mätas exakt samtidigt

En analog multiplexer är inte en riktig flerkanalig ADC. Den låter bara en ADC-ingång titta på en signal i taget.

### Exempel: läsa 16 potentiometrar med CD74HC4067

Följande exempel visar principen. Fyra adresspinnar väljer kanal. Den gemensamma signalen läses på A0.

```cpp
const int selectPins[] = {2, 3, 4, 5};
const int analogPin = A0;

void selectChannel(int channel) {
  for (int bitIndex = 0; bitIndex < 4; bitIndex++) {
    int bitValue = (channel >> bitIndex) & 1;
    digitalWrite(selectPins[bitIndex], bitValue);
  }
}

int readMuxChannel(int channel) {
  selectChannel(channel);
  delayMicroseconds(50);
  return analogRead(analogPin);
}

void setup() {
  Serial.begin(115200);

  for (int bitIndex = 0; bitIndex < 4; bitIndex++) {
    pinMode(selectPins[bitIndex], OUTPUT);
  }
}

void loop() {
  for (int channel = 0; channel < 16; channel++) {
    int value = readMuxChannel(channel);

    Serial.print("CH");
    Serial.print(channel);
    Serial.print(": ");
    Serial.print(value);
    Serial.print("  ");
  }

  Serial.println();
  delay(250);
}
```

Den korta väntan efter kanalval är viktig. ADC-ingången och multiplexern behöver tid att stabilisera sig, särskilt om källimpedansen är hög.

## Multiplexer, demultiplexer och matrix-tänkande

Orden multiplexer och demultiplexer dyker ofta upp tillsammans.

En multiplexer väljer en av flera ingångar och skickar den till en gemensam utgång. En demultiplexer gör motsatsen: den skickar en gemensam signal till en av flera utgångar. Många analoga switchkretsar kan i praktiken användas åt båda håll, eftersom signalvägen fungerar som en styrbar switch.

Det här är användbart när du vill välja mellan flera signaler, men inte behöver alla samtidigt.

Exempel:

- välj en av flera analoga sensorer
- välj en av flera testpunkter
- välj vilken rad eller kolumn i en knappmatris som ska aktiveras
- välj vilken enhet som ska få en enable-signal
- skapa enkel skanning av många kontakter

Matrix-tänkande är när du organiserar ingångar eller utgångar i rader och kolumner. Ett tangentbord är ett klassiskt exempel. I stället för att ha en pinne per knapp kan du skanna rader och kolumner. Det minskar antalet pinnar men kräver mer kod och ibland dioder för att undvika ghosting.

## Jämförelse: vilken lösning ska du välja?

Följande tabell är en praktisk startpunkt.

| Behov | Bra förstaval | Alternativ | Kommentar |
|---|---|---|---|
| Många enkla LED | 74HC595 | MCP23017, LED-driver | Kontrollera total ström. |
| Många knappar | MCP23017 | 74HC165, knappmatris | Pullups och debouncing behövs. |
| Billig enkel I2C-I/O | PCF8574 | MCP23017, PCF8575 | Bra för enkla paneler. |
| 16 enkla I2C-I/O utan avancerade funktioner | PCF8575 | MCP23017 | Passar knappar, LED och långsam styrning. |
| Många digitala utgångar med få pinnar | 74HC595 | SPI-I/O-expander | Kan kedjekopplas. |
| Många digitala ingångar med få pinnar | 74HC165 | MCP23017 | Kräver stabila ingångsnivåer. |
| Många analoga sensorer | CD74HC4067 | större kort, extern ADC | Inte samtidig mätning. |
| Högre analog noggrannhet | extern ADC | bättre kort | Multiplexer kan försämra precision. |
| Snabb parallell styrning | större mikrokontroller | specialkrets | I2C kan bli flaskhals. |
| Många laster | drivkrets plus expander | större kort plus drivkrets | Expandern styr, drivkretsen driver. |

Ett vanligt misstag är att välja expander utifrån antal pinnar och först senare upptäcka att signaltypen inte passar. Börja därför alltid med frågan: “Vad ska pinnen faktiskt göra?”

Snabbt expansionsval:

- Välj **74HC595** för många enkla utgångar, särskilt LED-status.
- Välj **74HC165** för många enkla digitala ingångar.
- Välj **MCP23017** när du vill ha flexibel I2C-I/O med tydligare riktning per pinne.
- Välj **PCF8575** när du behöver många enkla I2C-I/O och kraven är långsamma.
- Välj **CD74HC4067** för många analoga kanaler, men inte när samtidighet eller hög precision krävs.

## Ström och elektriska begränsningar

Expanderkretsar har egna strömgränser. De är ofta lägre än vad man intuitivt tänker när man ser åtta eller sexton utgångar. Även om en pinne kan tända en LED betyder det inte att alla pinnar kan driva starka LED samtidigt.

Tänk på tre nivåer:

- ström per pinne
- total ström genom kretsens matningspinnar
- vad mikrokontrollerns eller regulatorns matning kan leverera

För LED-experiment är det klokt att använda försiktiga strömmar. En status-LED behöver ofta inte 20 mA. I många fall räcker några milliampere, särskilt med moderna LED.

För laster gäller samma regel som tidigare i boken:

> En I/O-expander ska normalt styra en drivkrets, inte vara drivkretsen.

Om en expanderpinne ska styra ett relä, en solenoid, en motor eller en längre LED-strip bör den styra en transistor, MOSFET, ULN2803 eller specialiserad driver.

## Logiknivåer och matning

Många äldre 74HC-kretsar och Arduino UNO-liknande kort används ofta vid 5 V. Moderna ESP32-, ESP8266-, RP2040- och många småkort använder 3,3 V-logik. Det betyder att du måste kontrollera vilken logiknivå kretsen, kortet och modulen använder.

I2C-expanderkort kan vara extra luriga. En modul kan matas med 5 V men ha pullup-motstånd till 5 V på SDA och SCL. Det är inte automatiskt säkert för ett 3,3 V-kort. Om du använder ESP32, ESP8266, RP2040 eller andra 3,3 V-kort ska du kontrollera I2C-pullups och behov av nivåskiftning.

För 74HC-serien gäller att ingångarnas HIGH-tröskel beror på matningsspänningen. En 5 V-matad 74HC-krets är inte alltid garanterad att tolka 3,3 V som HIGH i alla lägen. En 74HCT-variant kan ibland vara bättre när en 3,3 V-signal ska in i en 5 V-logikkrets, eftersom HCT-familjen har TTL-liknande ingångströsklar.

Det här är en typisk punkt där databladet är viktigare än forumexempel.

## Hastighet och uppdateringsfrekvens

I/O-expansion kan påverka hur snabbt signaler kan uppdateras.

Direkt GPIO är snabbast och enklast. Shift register kan vara snabba, särskilt om du använder hårdvaru-SPI eller optimerad kod. I2C-expander är ofta långsammare, men tillräckligt för knappar, indikatorer och paneler.

Frågan är inte bara “hur snabb är kretsen?” utan “hur snabbt behöver projektet vara?”

- En knappanel kan läsas 20 till 100 gånger per sekund.
- Status-LED kan uppdateras några gånger per sekund eller när tillstånd ändras.
- En LED-matris behöver ofta snabbare och mer regelbunden uppdatering.
- Motorstyrning med PWM bör inte göras med långsam I2C-expander.
- Snabba pulser och encoder-signaler bör ofta gå direkt till mikrokontrollern eller till specialiserad krets.

Om du märker att expanderkoden tar mycket tid i loop-funktionen är lösningen ofta att uppdatera mer sällan, skriva bara när värdet ändras eller flytta snabbare signaler till direkta pinnar.

## Kodstruktur: dölj expansionen bakom funktioner

Ett projekt blir snabbt svårläst om halva koden består av bitmasker, registeradresser och magiska pin-nummer. Därför bör du kapsla in expanderad I/O.

I stället för att skriva direkt till bitar överallt kan du skapa funktioner med meningsfulla namn.

```cpp
const byte STATUS_READY = 0b00000001;
const byte STATUS_ERROR = 0b00000010;
const byte STATUS_ACTIVE = 0b00000100;

byte panelOutputs = 0;

void setPanelOutput(byte mask, bool enabled) {
  if (enabled) {
    panelOutputs |= mask;
  } else {
    panelOutputs &= ~mask;
  }

  writeOutputs(panelOutputs);
}

void showReady(bool enabled) {
  setPanelOutput(STATUS_READY, enabled);
}

void showError(bool enabled) {
  setPanelOutput(STATUS_ERROR, enabled);
}

void showActive(bool enabled) {
  setPanelOutput(STATUS_ACTIVE, enabled);
}
```

Resten av programmet kan då skriva:

```cpp
showReady(true);
showError(false);
showActive(systemIsRunning);
```

Det är mycket tydligare än att sprida bitoperationer över hela projektet.

För större projekt kan du skapa en liten klass, men börja enkelt. Målet är att resten av koden ska uttrycka projektets avsikt, inte expanderkretsens detaljer.

## Bitmasker utan att göra koden oläslig

I/O-expansion leder ofta till bitmasker. Det är kraftfullt men kan bli otydligt.

En bitmask är ett värde där varje bit representerar ett tillstånd. Om bit 0 betyder “ready LED”, bit 1 betyder “error LED” och bit 2 betyder “active LED” kan ett enda byte beskriva alla tre.

Använd namngivna konstanter i stället för råa binärtal i hela koden.

```cpp
const byte LED_READY = 1 << 0;
const byte LED_ERROR = 1 << 1;
const byte LED_ACTIVE = 1 << 2;
const byte LED_NETWORK = 1 << 3;
```

Då blir koden självförklarande.

```cpp
panelOutputs |= LED_NETWORK;
panelOutputs &= ~LED_ERROR;
```

Om du arbetar med 16 bitar kan du använda `uint16_t`.

```cpp
uint16_t inputState = 0;
```

För en erfaren programmerare är detta inte svårt, men det är lätt att glömma dokumentationen. Lägg därför alltid en tabell i kommentar eller dokumentation som visar vilken fysisk utgång som motsvarar vilken bit.

## Referensmönster: åtta LED med 74HC595 och valbar utbyggnad

Det här referensmönstret visar en liten utgångsmodul med ett 74HC595. Det visar hur få mikrokontrollerpinnar kan styra många utgångar och ger en struktur som senare kan byggas ut till relästyrning, statuspanel eller LED-indikator.

Använd 74HC595 när du behöver fler **logiska utgångar**. Kretsen ger inte automatiskt mer lastström. LED med rimliga motstånd är ett bra första test, men reläer, motorer, solenoider och LED-strippar behöver separata drivsteg.

### Det här används i exemplet

Du behöver:

- ett Arduino-kompatibelt kort
- ett 74HC595 eller kompatibelt shift register
- åtta LED
- åtta seriemotstånd, till exempel 330 ohm till 1 kohm beroende på LED och matning
- breadboard och kopplingskablar
- gärna en 100 nF kondensator nära kretsens matningspinnar
- valfritt: ett andra 74HC595 för kedjekoppling

### Kopplingsidé

Koppla data, clock och latch till tre digitala pinnar. Koppla 74HC595 till samma logikspänning som mikrokontrollern om det är möjligt. Koppla OE till GND och MR till VCC för ett första test. Varje utgång går via ett motstånd till en LED.

En typisk kopplingsöversikt ser ut så här:

| Funktion | Mikrokontrollerpinne | 74HC595-signal | Kommentar |
|---|---|---|---|
| Data | 11 | SER/DS | Bitar in till registret |
| Clock | 12 | SHCP/SRCLK | Flyttar bitar |
| Latch | 8 | STCP/RCLK | Uppdaterar utgångar |
| Output enable | GND | OE | Aktiv låg |
| Reset | VCC | MR/SRCLR | Aktiv låg |

Namnen på pinnarna varierar mellan datablad och moduler. Kontrollera alltid pinouten för just din krets.

### Kod

```cpp
const int latchPin = 8;
const int dataPin = 11;
const int clockPin = 12;

byte outputState = 0;

void writeOutputs(byte value) {
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, MSBFIRST, value);
  digitalWrite(latchPin, HIGH);
}

void setOutput(int index, bool enabled) {
  if (index < 0 || index > 7) {
    return;
  }

  byte mask = 1 << index;

  if (enabled) {
    outputState |= mask;
  } else {
    outputState &= ~mask;
  }

  writeOutputs(outputState);
}

void setup() {
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);

  writeOutputs(outputState);
}

void loop() {
  for (int index = 0; index < 8; index++) {
    setOutput(index, true);
    delay(100);
  }

  for (int index = 0; index < 8; index++) {
    setOutput(index, false);
    delay(100);
  }
}
```

### Förväntat resultat

LED tänds en efter en och släcks sedan en efter en. Om ordningen är omvänd eller verkar förskjuten är det troligen bitordning eller fysisk koppling som skiljer sig från antagandet. Det är ett dokumentationsproblem, inte nödvändigtvis ett funktionsfel.

### Variation 1: statuspanel

Byt ut sekvensen mot namngivna statuslägen.

```cpp
const byte STATUS_POWER = 1 << 0;
const byte STATUS_READY = 1 << 1;
const byte STATUS_ACTIVE = 1 << 2;
const byte STATUS_ERROR = 1 << 3;
```

Låt olika kombinationer representera olika systemtillstånd.

### Variation 2: kedjekoppla två register

Lägg till ett andra 74HC595 och uppdatera koden så att du skickar två byte. Dokumentera vilka LED som hör till första och andra kretsen.

### Variation 3: styr laster via drivkrets

Använd 74HC595-utgångarna för att styra ingångar på ULN2803 eller MOSFET-modul. Driv inte större laster direkt från 74HC595.

## Referensmönster: läsa många knappar med MCP23017

Det här mönstret visar en annan stil: I2C-baserad expansion. Det passar när många ingångar ska läsas via MCP23017.

### Det här används i exemplet

Du behöver:

- ett Arduino-kompatibelt kort
- en MCP23017-modul eller lös krets med korrekt koppling
- flera knappar
- I2C-anslutning med SDA och SCL
- lämpliga pullups, internt i kretsen eller externt
- bibliotek för MCP23017

### Kopplingsidé

Koppla MCP23017 till I2C-bussen. Koppla knappar mellan expanderpinnar och GND. Använd interna pullups i expandern om biblioteket stöder det.

Kontrollera I2C-adressen innan du felsöker kod eller koppling. Vanlig startadress är ofta 0x20, men adresspinnar kan ändra detta.

### Kodprincip

```cpp
#include <Wire.h>
#include <Adafruit_MCP23X17.h>

Adafruit_MCP23X17 io;

const int buttonCount = 4;
const int buttonPins[buttonCount] = {0, 1, 2, 3};

bool previousState[buttonCount] = {false, false, false, false};

void setup() {
  Serial.begin(115200);
  Wire.begin();

  if (!io.begin_I2C(0x20)) {
    Serial.println("MCP23017 not found");
    while (true) {
      delay(100);
    }
  }

  for (int i = 0; i < buttonCount; i++) {
    io.pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

void loop() {
  for (int i = 0; i < buttonCount; i++) {
    bool pressed = io.digitalRead(buttonPins[i]) == LOW;

    if (pressed != previousState[i]) {
      previousState[i] = pressed;

      Serial.print("Button ");
      Serial.print(i);
      Serial.print(": ");
      Serial.println(pressed ? "pressed" : "released");
    }
  }

  delay(20);
}
```

### Förväntat resultat

När du trycker på en knapp ska seriell monitor visa vilken knapp som ändrat läge. Om alla knappar verkar tryckta eller släppta samtidigt är pullup-konfigurationen eller kopplingen troligen fel.

### Utbyggnad

LED kan läggas på andra portar i samma expander, men vid många indikatorer är ett separat 74HC595 ofta enklare och tydligare.

## Vanliga misstag

- **Misstag: Att tro att fler pinnar betyder mer ström.**
  - Varför det händer: En expander med 16 I/O ser ut som en större Arduino-port.
  - Hur du undviker det: Läs strömgränser och använd drivkretsar för laster.

- **Misstag: Att koppla 5 V-I2C-pullups till ett 3,3 V-kort.**
  - Varför det händer: Många moduler döljer pullup-motstånd på kortet.
  - Hur du undviker det: Kontrollera modulens schema eller mät vilospänningen på SDA och SCL.

- **Misstag: Att använda I2C-expander för snabba signaler.**
  - Varför det händer: `digitalRead`-liknande bibliotek gör expandern lätt att använda.
  - Hur du undviker det: Låt snabba pulser, PWM och encoder-signaler gå direkt till mikrokontrollern eller till specialiserade kretsar.

- **Misstag: Att inte dokumentera bitordning.**
  - Varför det händer: Första testet fungerar och projektet går vidare.
  - Hur du undviker det: Skapa en tabell över bitnummer, fysisk pinne och funktion direkt.

- **Misstag: Att glömma debouncing på expanderade knappar.**
  - Varför det händer: Fokus ligger på I2C eller shift register, inte på knappens mekanik.
  - Hur du undviker det: Behandla expanderade knappar som vanliga knappar med studs.

- **Misstag: Att använda analog multiplexer för signaler som kräver hög precision utan kontroll.**
  - Varför det händer: 16 analoga kanaler på en modul låter som en billig flerkanals-ADC.
  - Hur du undviker det: Ta hänsyn till switchresistans, källimpedans, stabiliseringstid och ADC-egenskaper.

- **Misstag: Att låta expanderlogiken spridas över hela programmet.**
  - Varför det händer: Det är enkelt att börja med bitoperationer direkt i `loop()`.
  - Hur du undviker det: Kapsla in expanderad I/O bakom namngivna funktioner.

## Felsökning

När I/O-expansion inte fungerar är det viktigt att testa lager för lager.

Börja med matning och jord. Kontrollera att kretsen får rätt spänning och att mikrokontroller och expander har gemensam jord. Kontrollera sedan styrsignalerna. För I2C-expander, kör en I2C-scanner och bekräfta adressen. För shift register, testa ett enkelt vandrande LED-mönster innan du kopplar in resten av projektet.

För 74HC595:

- kontrollera att latch, clock och data inte är omkastade
- kontrollera OE och MR
- kontrollera LED-polaritet och motstånd
- testa både MSBFIRST och LSBFIRST om ordningen verkar konstig
- kontrollera att matningsspänningen matchar logiknivån

För 74HC165:

- kontrollera load-signalen
- kontrollera att ingångarna inte flyter
- kontrollera clock-polaritet
- läs långsamt först och skriv ut råa bitmönster
- testa med fasta HIGH/LOW-kopplingar innan knappar används

För MCP23017, PCF8574 eller PCF8575:

- kör I2C-scanner
- kontrollera SDA/SCL-pinnar för just ditt kort
- kontrollera adresspinnar
- kontrollera pullups och logiknivå
- prova ett minimalt biblioteksexempel
- kontrollera att biblioteket stöder den kretsvariant du använder

För analog multiplexer:

- läs en kanal i taget
- koppla en kanal till GND och en annan till VCC för tydlig test
- lägg in kort stabiliseringstid efter kanalval
- kontrollera adresspinnarnas ordning
- minska källimpedansen eller öka väntetiden om värdena smetar mellan kanaler

En logikanalysator är mycket användbar för shift register och I2C. Men även utan instrument kan du komma långt genom att isolera problemet: matning först, sedan kommunikation, sedan en kanal, sedan alla kanaler.

## Snabbreferens

| Komponenttyp | Exempel | Styrkor | Begränsningar |
|---|---|---|---|
| Seriellt till parallellt shift register | 74HC595 | Billigt, kedjekopplingsbart, bra för utgångar | Kräver bitordning och latch, begränsad ström |
| Parallellt till seriellt shift register | 74HC165 | Bra för många digitala ingångar | Kräver stabila ingångar och egen läsrutin |
| I2C-I/O-expander | MCP23017 | Flexibel, 16 I/O, pullups, tydlig kod | I2C-hastighet, adresshantering, begränsad ström |
| Enkel I2C-expander | PCF8574 | Billig, vanlig, enkel | Speciellt I/O-beteende, mindre flexibel |
| 16-bitars enkel I2C-expander | PCF8575 | Fler enkla I/O än PCF8574 | Inte PWM, hög ström eller snabb sampling |
| Analog multiplexer | CD74HC4067 | Många analoga kanaler med få pinnar | Inte samtidig mätning, påverkar precision |
| Knappmatris | Rader och kolumner | Många knappar med få pinnar | Kräver skanning, debounce och ibland dioder |

En praktisk tumregel:

- 74HC595 för många enkla utgångar.
- 74HC165 för många enkla ingångar.
- MCP23017 för flexibel digital I/O via I2C.
- PCF8574 för billig enkel I2C-expansion.
- PCF8575 när du vill ha samma enkla typ av I2C-expansion men behöver 16 I/O.
- CD74HC4067 eller liknande för många analoga kanaler.
- Större kort eller specialkrets när hastighet, precision eller strömkrav är viktigare än pinbesparing.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Beror på kretsfamilj, ofta 3,3 V eller 5 V |
| Typiskt gränssnitt | I2C, SPI, parallella signaler eller analoga vägar |
| Välj när | du behöver fler pinnar eller välja mellan många signaler |
| Välj inte när | du egentligen behöver mer prestanda eller separat mikrokontroller |
| Vanliga fel | adresskonflikt, fel riktning, långsam uppdatering, flytande ingångar |
| Alternativ att överväga | större kort, shift register, multiplexer, I/O-expander |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När expandern inte hittas, börja med I2C- eller SPI-felsökning i kapitel 9.
- När du flyttar många digitala signaler från kortet till en expander, repetera grundbeteendet i kapitel 5.
- När flera moduler fungerar var för sig men inte tillsammans, använd felsökningsordningen i kapitel 35.
- När expansionen ingår i en större sensorstation, jämför med kapitel 37.
