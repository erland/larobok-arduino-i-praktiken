# 17. LED, RGB-LED och ljuseffekter

## Komponentöversikt
LED är ofta den första utenheten i ett Arduino-projekt. Det kan låta trivialt: en pinne, ett motstånd och en liten lampa. Men LED är också ett mycket bra sätt att lära sig praktisk styrning av hårdvara.

En LED kan vara en enkel statusindikator. Den kan visa att ett program startat, att en sensor svarar, att en buss har fel eller att ett batteri håller på att ta slut. Flera LED kan bli ett litet användargränssnitt. RGB-LED kan visa tillstånd med färg. LED-matriser och segmentdisplayer kan visa siffror, symboler och enkel grafik. LED-effekter kan också vara ett helt projekt i sig, särskilt när du kombinerar ljus med sensorer, knappar, ljud eller nätverksdata.

Det här kapitlet handlar om vanliga LED, RGB-LED och enklare ljuseffekter. Adresserbara LED, till exempel NeoPixel och WS2812, får ett eget kapitel efter detta eftersom de fungerar mer som digitala kommunikationsenheter än som vanliga LED.

Målet är att du ska kunna använda LED på ett sätt som är elektriskt rimligt, läsbart i kod och användbart i verkliga projekt. En erfaren programmerare kan ofta skriva LED-koden snabbt, men de praktiska felen brukar ligga i ström, motstånd, pin-belastning, polaritet, färglogik och blockerande effekter.

I praktiken används LED främst för status, felsökning, enkla varningar och visuell återkoppling. Kapitlet visar därför både elektriska grunder och kodmönster som går att återanvända i senare projekt.

## Förutsättningar

Du har redan mött digital I/O, PWM och elektriska grunder. I det här kapitlet använder vi särskilt dessa begrepp:

- En digital utgång kan sättas till `HIGH` eller `LOW`.
- En PWM-utgång kan växla snabbt mellan av och på så att LED upplevs som dimmad.
- En mikrokontrollerpinne kan bara leverera eller ta emot begränsad ström.
- En LED är polariserad och leder ström främst i en riktning.
- Ett seriemotstånd används för att begränsa strömmen.

Vi använder engelska namn i koden, men svensk brödtext. Det gör exemplen lättare att jämföra med dokumentation och bibliotek.

## LED som status, inte bara dekoration

En LED kan ha flera roller i ett projekt.

Den enklaste rollen är **indikator**. Den visar att något är sant:

- Kortet har startat.
- En knapp är nedtryckt.
- En sensor svarar.
- Ett fel har inträffat.
- Systemet väntar på Wi-Fi.
- En mätning pågår.
- Ett batteri är lågt.

En mer avancerad roll är **återkoppling**. Då visar LED inte bara ett tillstånd, utan hjälper användaren förstå systemet. Exempel:

- Långsam blinkning betyder vänteläge.
- Snabb blinkning betyder aktiv mätning.
- Fast rött ljus betyder fel.
- Grönt ljus betyder klart.
- Gult ljus betyder varning.
- Pulserande ljus betyder att systemet lever men inte gör något viktigt.

En tredje roll är **uttryck**. Då används ljus som en del av upplevelsen: färgövergångar, ljusmönster, reaktion på ljud, interaktiv installation eller visuell representation av sensordata.

Det är bra att skilja på dessa roller. En statusindikator ska vara lätt att förstå och robust. En ljuseffekt kan vara mer experimentell. Blanda inte ihop dem i kodstrukturen om projektet ska växa.

## Vanlig LED

En vanlig LED har två ben:

- **Anod**: den positiva sidan.
- **Katod**: den negativa sidan.

På många lösa LED är det längre benet anod och det kortare benet katod. Den platta sidan på LED-kroppen markerar ofta katoden. På moduler och kretskort ska du i stället läsa märkningen, eftersom benlängd inte alltid är relevant.

En LED har ett framspänningsfall, ofta kallat forward voltage. Det betyder att LED börjar lysa när spänningen över den når en viss nivå. Typiska ungefärliga värden är:

| LED-färg | Typiskt framspänningsfall | Kommentar |
|---|---:|---|
| Röd | 1,8–2,2 V | Låg framspänning. |
| Gul/orange | 1,9–2,2 V | Liknar röd. |
| Grön | 2,0–3,2 V | Beror på LED-typ. |
| Blå | 2,8–3,4 V | Högre framspänning. |
| Vit | 2,8–3,4 V | Är normalt blå LED med fosfor. |

Värdena är ungefärliga. För ett experiment räcker de ofta. För en produkt eller stark LED ska du läsa databladet.

## Varför LED behöver strömbegränsning

En LED är inte som en glödlampa eller ett vanligt motstånd. När den börjar leda kan strömmen öka kraftigt om den inte begränsas. Därför ska du normalt inte koppla en lös LED direkt mellan en Arduino-pinne och jord.

Den klassiska lösningen är ett seriemotstånd.

```text
Arduino pin ---- resistor ---- LED ---- GND
```

eller:

```text
5V/3.3V ---- resistor ---- LED ---- Arduino pin
```

I första kopplingen lyser LED när pinnen är `HIGH`. I andra kopplingen lyser LED när pinnen är `LOW`, eftersom pinnen då sänker ström till jord. Den andra varianten kallas ibland aktiv låg logik.

För indikatorer är strömmen ofta mycket lägre än många tror. En modern LED kan lysa tydligt redan vid 1–5 mA. Du behöver sällan 20 mA för en statusindikator.

## Välja seriemotstånd

En enkel beräkning är:

```text
R = (V_supply - V_led) / I_led
```

Exempel med 5 V, röd LED och 5 mA:

```text
R = (5 V - 2 V) / 0,005 A = 600 ohm
```

Ett standardvärde på 680 ohm fungerar bra. Även 1 kΩ fungerar ofta utmärkt för en indikator.

Exempel med 3,3 V, röd LED och 3 mA:

```text
R = (3,3 V - 2 V) / 0,003 A = 433 ohm
```

Ett standardvärde på 470 ohm eller 1 kΩ kan fungera beroende på önskad ljusstyrka.

Praktiska tumregler:

| Matning/logik | LED-färg | Rimligt startmotstånd | Kommentar |
|---|---|---:|---|
| 5 V | Röd/gul/grön | 330 Ω–1 kΩ | 1 kΩ räcker ofta för status. |
| 5 V | Blå/vit | 470 Ω–1 kΩ | Blå/vit kan vara starka även vid låg ström. |
| 3,3 V | Röd/gul | 330 Ω–1 kΩ | Bra för ESP32/Pico-liknande kort. |
| 3,3 V | Blå/vit | 220 Ω–680 Ω | Mindre marginal eftersom framspänningen är högre. |

Om du bara bygger en statusindikator är 1 kΩ ofta ett säkert och behagligt startvärde. Om LED lyser för svagt kan du minska motståndet, men kontrollera strömgränserna för kortet.

## Source och sink

En mikrokontrollerpinne kan ofta både leverera ström och ta emot ström.

När pinnen levererar ström till LED säger man att den **source:ar** ström:

```text
PIN HIGH -> resistor -> LED -> GND
```

När pinnen tar emot ström från LED säger man att den **sink:ar** ström:

```text
VCC -> resistor -> LED -> PIN LOW
```

Många äldre mikrokontrollers var bättre på att sänka ström än att leverera ström, men du ska inte bygga på gamla tumregler utan att kontrollera kortets specifikation. För en enstaka indikator-LED med låg ström spelar det oftast ingen större roll. För många LED eller högre ström spelar det stor roll.

## Inbyggd LED

Många Arduino-kompatibla kort har en inbyggd LED. Den används ofta i exempel som `Blink`.

På klassiska Arduino UNO sitter den vanligtvis på pinne 13. Men på andra kort kan den sitta på en annan pinne, vara aktiv låg eller saknas helt. Därför är det bättre att använda konstanten `LED_BUILTIN` när du bara vill använda kortets inbyggda LED.

```cpp
const int statusLedPin = LED_BUILTIN;

void setup() {
  pinMode(statusLedPin, OUTPUT);
}

void loop() {
  digitalWrite(statusLedPin, HIGH);
  delay(500);
  digitalWrite(statusLedPin, LOW);
  delay(500);
}
```

Det här är ett bra första test, men i riktiga projekt vill du ofta undvika `delay()`. Vi kommer strax tillbaka till det.

## Vanlig LED som statusindikator

En enkel statusindikator kan byggas med `digitalWrite`.

```cpp
const int statusLedPin = 8;

void setup() {
  pinMode(statusLedPin, OUTPUT);
  digitalWrite(statusLedPin, LOW);
}

void loop() {
  bool systemReady = true;

  if (systemReady) {
    digitalWrite(statusLedPin, HIGH);
  } else {
    digitalWrite(statusLedPin, LOW);
  }
}
```

Det här är lätt att förstå, men inte särskilt flexibelt. I ett större projekt vill du ofta samla statuslogiken på ett ställe.

```cpp
const int statusLedPin = 8;

enum class SystemState {
  Starting,
  Ready,
  Warning,
  Error
};

SystemState currentState = SystemState::Starting;

void setup() {
  pinMode(statusLedPin, OUTPUT);
  Serial.begin(115200);

  currentState = SystemState::Ready;
}

void loop() {
  updateStatusLed(currentState);
}

void updateStatusLed(SystemState state) {
  switch (state) {
    case SystemState::Starting:
      digitalWrite(statusLedPin, HIGH);
      break;

    case SystemState::Ready:
      digitalWrite(statusLedPin, LOW);
      break;

    case SystemState::Warning:
      digitalWrite(statusLedPin, HIGH);
      break;

    case SystemState::Error:
      digitalWrite(statusLedPin, HIGH);
      break;
  }
}
```

Än så länge ser flera tillstånd likadana ut. Nästa steg är att låta olika tillstånd få olika mönster.

## Blink utan delay

`delay()` är användbart i små tester men problematiskt i program som ska läsa sensorer, hantera knappar eller kommunicera. Med `delay()` står programmet stilla.

Ett bättre mönster är att använda `millis()`.

```cpp
const int statusLedPin = 8;

unsigned long previousBlinkMillis = 0;
const unsigned long blinkIntervalMs = 500;
bool ledIsOn = false;

void setup() {
  pinMode(statusLedPin, OUTPUT);
}

void loop() {
  updateBlink();
  readInputs();
  updateOtherOutputs();
}

void updateBlink() {
  unsigned long now = millis();

  if (now - previousBlinkMillis >= blinkIntervalMs) {
    previousBlinkMillis = now;
    ledIsOn = !ledIsOn;
    digitalWrite(statusLedPin, ledIsOn ? HIGH : LOW);
  }
}

void readInputs() {
  // Read buttons or sensors here.
}

void updateOtherOutputs() {
  // Update other outputs here.
}
```

Det viktiga är inte bara att LED blinkar. Det viktiga är att LED blinkar samtidigt som resten av programmet kan fortsätta arbeta.

## Flera blinkmönster

Ett statusljus blir mer användbart om olika tillstånd ger olika mönster.

Exempel:

| Tillstånd | LED-mönster | Betydelse |
|---|---|---|
| Starting | Snabb blinkning | Systemet startar. |
| Ready | Fast ljus | Systemet är redo. |
| Waiting | Långsam blinkning | Systemet väntar på händelse. |
| Error | Dubbelblink | Fel behöver åtgärdas. |

Här är en enkel implementation för tre mönster.

```cpp
const int statusLedPin = 8;

enum class SystemState {
  Starting,
  Ready,
  Waiting,
  Error
};

SystemState currentState = SystemState::Starting;

unsigned long previousMillis = 0;
bool ledIsOn = false;

void setup() {
  pinMode(statusLedPin, OUTPUT);
  Serial.begin(115200);

  currentState = SystemState::Waiting;
}

void loop() {
  updateStatusLed(currentState);

  // Example state change for testing.
  if (millis() > 10000) {
    currentState = SystemState::Ready;
  }
}

void updateStatusLed(SystemState state) {
  switch (state) {
    case SystemState::Starting:
      blinkAtInterval(100);
      break;

    case SystemState::Ready:
      setLed(true);
      break;

    case SystemState::Waiting:
      blinkAtInterval(800);
      break;

    case SystemState::Error:
      blinkAtInterval(200);
      break;
  }
}

void blinkAtInterval(unsigned long intervalMs) {
  unsigned long now = millis();

  if (now - previousMillis >= intervalMs) {
    previousMillis = now;
    ledIsOn = !ledIsOn;
    setLed(ledIsOn);
  }
}

void setLed(bool on) {
  digitalWrite(statusLedPin, on ? HIGH : LOW);
}
```

Den här koden är enkel, men har en begränsning: om du byter mellan blinkmönster kan `previousMillis` och `ledIsOn` följa med från föregående tillstånd. I enkla projekt är det acceptabelt. I mer ordnade projekt kan du lägga till kod som upptäcker tillståndsbyte och nollställer mönstret.

## PWM och ljusstyrka

Med PWM kan du styra upplevd ljusstyrka. På många Arduino-kompatibla kort används `analogWrite()` för PWM, trots att utsignalen inte är en riktig analog spänning.

```cpp
const int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  analogWrite(ledPin, 32);
  delay(1000);

  analogWrite(ledPin, 128);
  delay(1000);

  analogWrite(ledPin, 255);
  delay(1000);
}
```

På klassisk Arduino UNO brukar `analogWrite()` använda värden 0–255. På andra kort kan upplösning, frekvens och implementation skilja sig. På ESP32 finns till exempel annan PWM-hantering under huven. Därför ska kod som är tänkt att flyttas mellan kort hålla PWM-antaganden tydliga.

För experiment och statusljus räcker ofta `analogWrite()`. För motorer, servon, ljud och adresserbara LED krävs andra mönster.

## Fade utan delay

En fade-effekt bör också skrivas utan blockerande `delay()` om den ska kombineras med sensorer eller kommunikation.

```cpp
const int ledPin = 9;

int brightness = 0;
int fadeStep = 5;

unsigned long previousFadeMillis = 0;
const unsigned long fadeIntervalMs = 20;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  updateFade();
  readSensors();
}

void updateFade() {
  unsigned long now = millis();

  if (now - previousFadeMillis >= fadeIntervalMs) {
    previousFadeMillis = now;

    brightness += fadeStep;

    if (brightness <= 0 || brightness >= 255) {
      fadeStep = -fadeStep;
      brightness = constrain(brightness, 0, 255);
    }

    analogWrite(ledPin, brightness);
  }
}

void readSensors() {
  // Sensor code can run without being blocked by the fade.
}
```

Detta mönster är värt att lära sig. Det återkommer i många former: LED-effekter, ljudmönster, displayuppdateringar, sensorintervall och timeout-hantering.

## Ljusstyrka upplevs inte linjärt

Ett PWM-värde på 128 känns inte alltid som exakt halva ljusstyrkan. Ögat uppfattar ljus ungefär logaritmiskt. Dessutom har olika LED olika effektivitet och spridningsvinkel.

För enkla statusljus spelar det sällan någon roll. För snygga fade-effekter kan du använda en enkel korrigeringstabell eller matematisk kurva. Men börja enkelt. För mycket optimering i första versionen gör ofta koden svårare att förstå.

En praktisk kompromiss är att undvika det allra svagaste intervallet om LED flimrar eller knappt syns, och att inte köra full styrka om det bländar.

## RGB-LED

En RGB-LED innehåller tre LED i samma kapsel: röd, grön och blå. Genom att styra varje kanal separat kan du skapa olika färger.

Det finns två vanliga typer:

- **Common cathode**: alla katoder är gemensamma och kopplas till GND.
- **Common anode**: alla anoder är gemensamma och kopplas till VCC.

Med common cathode lyser en kanal när pinnen sätts hög eller PWM-värdet ökas.

Med common anode blir logiken inverterad: kanalen lyser när pinnen sänker ström. Ett högt PWM-värde kan då betyda mindre ljus beroende på hur du skriver koden.

Det är mycket vanligt att blanda ihop dessa typer. Om RGB-LED beter sig “bakvänt” är det en av de första sakerna du bör kontrollera.

## Koppling av RGB-LED

Varje färgkanal behöver egen strömbegränsning. Använd alltså normalt tre motstånd, inte ett gemensamt.

```text
Red pin ---- resistor ---- red channel
Green pin -- resistor ---- green channel
Blue pin --- resistor ---- blue channel
```

Eftersom färgerna har olika framspänning och ljusstyrka kan motstånden behöva olika värden om du vill balansera färgen. För experiment går det ofta bra med samma värde, till exempel 330 Ω eller 1 kΩ, men färgmixen blir inte perfekt.

## Styra RGB-LED med PWM

Här är ett enkelt exempel för common cathode RGB-LED.

```cpp
const int redPin = 9;
const int greenPin = 10;
const int bluePin = 11;

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  setColor(255, 0, 0);
  delay(1000);

  setColor(0, 255, 0);
  delay(1000);

  setColor(0, 0, 255);
  delay(1000);

  setColor(255, 80, 0);
  delay(1000);

  setColor(80, 0, 255);
  delay(1000);
}

void setColor(int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}
```

För common anode kan du invertera värdena.

```cpp
void setColorCommonAnode(int red, int green, int blue) {
  analogWrite(redPin, 255 - red);
  analogWrite(greenPin, 255 - green);
  analogWrite(bluePin, 255 - blue);
}
```

Det är bättre att gömma inversionen i en funktion än att sprida `255 - value` över hela programmet.

## Färg som status

RGB-LED är särskilt användbar för systemstatus.

| Färg | Möjlig betydelse | Kommentar |
|---|---|---|
| Blå | Startar eller konfigurerar | Vanligt i uppkopplade system. |
| Grön | Klart eller OK | Lätt att förstå. |
| Gul/orange | Varning eller väntan | Bra mellanläge. |
| Röd | Fel | Ska användas tydligt och sparsamt. |
| Lila | Specialläge eller service | Kan vara projektspecifikt. |
| Släckt | Av, sleep eller ingen information | Var tydlig med vad släckt betyder. |

Försök hålla färglogiken konsekvent genom hela projektet. Om rött betyder fel i ett kapitel bör det inte betyda “aktiv” i nästa experiment.

## Ett mer strukturerat RGB-statusljus

I ett växande projekt kan du använda en liten struktur för färg.

```cpp
struct RgbColor {
  int red;
  int green;
  int blue;
};

const RgbColor COLOR_OFF = {0, 0, 0};
const RgbColor COLOR_READY = {0, 180, 0};
const RgbColor COLOR_WARNING = {255, 80, 0};
const RgbColor COLOR_ERROR = {255, 0, 0};
const RgbColor COLOR_WAITING = {0, 0, 180};

const int redPin = 9;
const int greenPin = 10;
const int bluePin = 11;

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  setColor(COLOR_WAITING);
}

void loop() {
  bool sensorOk = true;
  bool batteryLow = false;

  if (!sensorOk) {
    setColor(COLOR_ERROR);
  } else if (batteryLow) {
    setColor(COLOR_WARNING);
  } else {
    setColor(COLOR_READY);
  }
}

void setColor(RgbColor color) {
  analogWrite(redPin, color.red);
  analogWrite(greenPin, color.green);
  analogWrite(bluePin, color.blue);
}
```

Det här är inte en stor arkitektur. Det är bara tillräckligt mycket struktur för att undvika magiska tal överallt.

## LED-moduler

Många LED säljs som moduler i stället för lösa komponenter. En LED-modul kan redan ha seriemotstånd, transistor, kontakt, märkta pinnar eller flera LED i samma kort.

Det är praktiskt, men kontrollera alltid vad modulen innehåller. En modul med märkningen `S`, `+` och `-` kan till exempel vara tänkt för direkt anslutning till en mikrokontrollerpinne, medan en lös LED kräver eget motstånd.

Vanliga LED-moduler:

| Modul | Typisk användning | Kontrollera |
|---|---|---|
| Enkel LED-modul | Status och test | Har den seriemotstånd? |
| Trafikljusmodul | Röd/gul/grön status | Gemensam jord eller gemensam VCC? |
| RGB-modul | Färgstatus | Common anode/cathode, motstånd. |
| Laser-modul | Pekare eller brytstråle | Ström, säkerhet, drivning. |
| LED-matris | Symboler och enklare grafik | Drivkrets, multiplexning, bibliotek. |
| 7-segmentsdisplay | Siffror | Common anode/cathode, drivström. |

Moduler minskar tröskeln, men gör det ibland svårare att förstå exakt vad som händer. För lärande är det bra att ibland bygga med lös LED och motstånd.

## När en pinne räcker

En mikrokontrollerpinne räcker ofta för:

- En enskild indikator-LED med låg ström.
- En RGB-LED där varje kanal körs med låg ström.
- En färdig LED-modul med inbyggt motstånd och låg ström.
- Debug- eller statusblink.

Men det förutsätter att du håller dig inom kortets strömgränser. Kontrollera både gräns per pinne och total gräns för mikrokontrollern eller kortet.

En viktig praktisk regel är att inte planera för maximal ström i normalfallet. Om databladet säger att en pinne absolut maximalt klarar ett visst värde betyder det inte att du bör designa för det värdet.

## När du behöver transistor, MOSFET eller drivkrets

Du behöver extern drivning när:

- Du ska styra många LED.
- LED drar mer ström än en pinne bör hantera.
- Du använder LED-strippar.
- Du använder starka power-LED.
- Du vill styra 12 V- eller 24 V-ljus.
- Du vill separera logikmatning från lastmatning.
- Du vill ha bättre robusthet.

För DC-laster och LED-strippar är MOSFET ofta ett bra val. För många enkla utgångar kan ULN2803 eller liknande drivkrets vara praktisk. För LED-matriser finns färdiga drivkretsar som hanterar multiplexning och ström bättre än direktstyrning.

Vi går djupare in i drivkretsar i senare kapitel. Här räcker huvudprincipen: en Arduino-pinne ska styra lasten, inte vara lasten.

## Flera LED och pin-budget

Många LED kan snabbt äta upp alla pinnar. Om du behöver många indikatorer finns flera alternativ:

| Behov | Möjlig lösning |
|---|---|
| Några få LED | Direkt från pinnar med motstånd. |
| Många enkla LED | Shift register, I/O-expander eller LED-drivare. |
| Många individuellt styrbara färg-LED | Adresserbara LED. |
| Siffror | 7-segmentsdisplay med drivkrets. |
| Symboler eller enkel grafik | LED-matris med drivmodul. |
| Status för många interna tillstånd | Display eller seriell logg kan vara bättre. |

För referens och felsökning är LED mycket bra. För komplex information blir display eller seriell logg ofta tydligare.

## Multiplexning

Multiplexning innebär att du tänder olika LED mycket snabbt i tur och ordning så att ögat uppfattar dem som tända samtidigt. Det används i LED-matriser och 7-segmentsdisplayer.

Principen är enkel, men implementationen kräver timing, strömberäkning och ibland drivtransistorer. Om du gör det manuellt kan det störa annan kod om du inte är försiktig. Därför är färdiga drivkretsar ofta bättre, till exempel för LED-matriser.

I den här boken är multiplexning främst något du ska känna igen. Du behöver inte skriva en egen komplett LED-matrisdrivrutin för att använda en LED-matris i ett Arduino-projekt.

## LED och strömförsörjning

LED-problem är ofta strömproblem.

En enda LED är enkel. En RGB-LED är fortfarande enkel. Men många LED, starka LED eller LED-strippar kan dra mycket ström. Då räcker inte USB-matningen eller mikrokontrollerkortets regulator.

Typiska symptom på för svag matning:

- Kortet startar om när ljuset tänds.
- LED flimrar.
- Färger blir fel när flera kanaler lyser.
- Seriell kommunikation tappar anslutning.
- Sensorer får konstiga värden när LED-effekten körs.
- ESP8266/ESP32 tappar Wi-Fi när LED tänds.

Åtgärder:

- Använd separat matning för LED-lasten.
- Koppla gemensam jord mellan logik och LED-matning.
- Lägg avkopplingskondensator nära lasten.
- Minska maximal ljusstyrka i mjukvara.
- Använd transistor eller MOSFET.
- Dimensionera kablar och kontakter för strömmen.

Gemensam jord är särskilt viktig. Om Arduino och LED-matning inte delar referens kan styrsignalen bli meningslös eller instabil.

## LED som felsökningsverktyg

En LED är ibland bättre än seriell loggning. Den fungerar även när USB inte är anslutet, när seriell port används till annat eller när enheten sitter i en låda.

Bra felsökningsmönster:

- En kort blink vid start.
- Tre snabba blink om en sensor saknas.
- Långsam blink om systemet väntar på nätverk.
- Fast ljus när setup är klar.
- Felkod med antal blinkningar.

Undvik däremot att skapa så många blinkkoder att ingen förstår dem. Om ett projekt behöver många felkoder är en display, logg eller seriell utskrift bättre.

## Kodmönster: status-LED som liten modul

Här är ett mer återanvändbart exempel. Det använder en enkel klass för att hålla statuslogiken samlad.

```cpp
class StatusLed {
public:
  StatusLed(int pin) : pin(pin) {}

  void begin() {
    pinMode(pin, OUTPUT);
    set(false);
  }

  void set(bool on) {
    isOn = on;
    digitalWrite(pin, isOn ? HIGH : LOW);
  }

  void blink(unsigned long intervalMs) {
    unsigned long now = millis();

    if (now - previousMillis >= intervalMs) {
      previousMillis = now;
      set(!isOn);
    }
  }

private:
  int pin;
  bool isOn = false;
  unsigned long previousMillis = 0;
};

StatusLed statusLed(8);

enum class SystemState {
  Starting,
  Ready,
  Waiting,
  Error
};

SystemState state = SystemState::Starting;

void setup() {
  statusLed.begin();
  state = SystemState::Waiting;
}

void loop() {
  updateSystemState();
  updateStatusOutput();
}

void updateSystemState() {
  if (millis() > 15000) {
    state = SystemState::Ready;
  }
}

void updateStatusOutput() {
  switch (state) {
    case SystemState::Starting:
      statusLed.blink(100);
      break;

    case SystemState::Ready:
      statusLed.set(true);
      break;

    case SystemState::Waiting:
      statusLed.blink(800);
      break;

    case SystemState::Error:
      statusLed.blink(200);
      break;
  }
}
```

Det här är inte tänkt som ett komplett bibliotek. Det visar hur du kan börja separera hårdvarustyrning från systemlogik.

## Referensmönster: statusljus med flera lägen

Mönstret visar ett statusljus som kan visa fyra tillstånd:

- Startar
- Väntar
- Aktiv
- Fel

Du kan bygga mönstret med en enkel LED eller med RGB-LED. RGB-varianten ger tydligare återkoppling, men enkel LED räcker om du fokuserar på blinkmönster.

### Det här används i exemplet

För enkel LED:

- Arduino-kompatibelt kort.
- 1 LED.
- 1 seriemotstånd, till exempel 470 Ω eller 1 kΩ.
- Breadboard och kopplingskablar.

För RGB-variant:

- Arduino-kompatibelt kort med minst tre PWM-pinnar.
- 1 RGB-LED.
- 3 seriemotstånd, till exempel 330 Ω–1 kΩ.
- Breadboard och kopplingskablar.

### Koppling med enkel LED

Koppla:

```text
Pin 8 -> resistor -> LED anode
LED cathode -> GND
```

Om LED inte lyser, kontrollera polariteten.

### Koppling med RGB-LED

För common cathode:

```text
Red pin 9 -> resistor -> red channel
Green pin 10 -> resistor -> green channel
Blue pin 11 -> resistor -> blue channel
Common cathode -> GND
```

För common anode kopplas den gemensamma anslutningen till VCC och PWM-värdena inverteras i koden.

### Kod för enkel LED

```cpp
const int statusLedPin = 8;

enum class SystemState {
  Starting,
  Waiting,
  Active,
  Error
};

SystemState state = SystemState::Starting;

unsigned long stateStartedAt = 0;
unsigned long previousBlinkMillis = 0;
bool ledIsOn = false;

void setup() {
  pinMode(statusLedPin, OUTPUT);
  stateStartedAt = millis();
}

void loop() {
  updateDemoState();
  updateStatusLed();
}

void updateDemoState() {
  unsigned long elapsed = millis() - stateStartedAt;

  if (elapsed < 3000) {
    state = SystemState::Starting;
  } else if (elapsed < 8000) {
    state = SystemState::Waiting;
  } else if (elapsed < 13000) {
    state = SystemState::Active;
  } else {
    state = SystemState::Error;
  }
}

void updateStatusLed() {
  switch (state) {
    case SystemState::Starting:
      blinkLed(100);
      break;

    case SystemState::Waiting:
      blinkLed(800);
      break;

    case SystemState::Active:
      setLed(true);
      break;

    case SystemState::Error:
      blinkLed(200);
      break;
  }
}

void blinkLed(unsigned long intervalMs) {
  unsigned long now = millis();

  if (now - previousBlinkMillis >= intervalMs) {
    previousBlinkMillis = now;
    ledIsOn = !ledIsOn;
    setLed(ledIsOn);
  }
}

void setLed(bool on) {
  digitalWrite(statusLedPin, on ? HIGH : LOW);
}
```

### Kod för RGB-LED

```cpp
const int redPin = 9;
const int greenPin = 10;
const int bluePin = 11;

struct RgbColor {
  int red;
  int green;
  int blue;
};

const RgbColor COLOR_OFF = {0, 0, 0};
const RgbColor COLOR_STARTING = {0, 0, 180};
const RgbColor COLOR_WAITING = {255, 80, 0};
const RgbColor COLOR_ACTIVE = {0, 180, 0};
const RgbColor COLOR_ERROR = {255, 0, 0};

enum class SystemState {
  Starting,
  Waiting,
  Active,
  Error
};

SystemState state = SystemState::Starting;
unsigned long stateStartedAt = 0;

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  stateStartedAt = millis();
}

void loop() {
  updateDemoState();
  updateStatusColor();
}

void updateDemoState() {
  unsigned long elapsed = millis() - stateStartedAt;

  if (elapsed < 3000) {
    state = SystemState::Starting;
  } else if (elapsed < 8000) {
    state = SystemState::Waiting;
  } else if (elapsed < 13000) {
    state = SystemState::Active;
  } else {
    state = SystemState::Error;
  }
}

void updateStatusColor() {
  switch (state) {
    case SystemState::Starting:
      setColor(COLOR_STARTING);
      break;

    case SystemState::Waiting:
      setColor(COLOR_WAITING);
      break;

    case SystemState::Active:
      setColor(COLOR_ACTIVE);
      break;

    case SystemState::Error:
      setColor(COLOR_ERROR);
      break;
  }
}

void setColor(RgbColor color) {
  analogWrite(redPin, color.red);
  analogWrite(greenPin, color.green);
  analogWrite(bluePin, color.blue);
}
```

### Testa

Kontrollera att:

- LED visar tydligt olika tillstånd.
- Programmet inte använder `delay()`.
- Statuslogiken ligger i egna funktioner.
- Färg- eller blinkmönstren går att ändra utan att ändra hela programmet.
- Kopplingen inte blir varm.
- LED inte bländar i normal användning.

### Utbyggnad

Bygg vidare genom att låta en verklig händelse styra status:

- En knapp växlar mellan aktiv och väntande.
- En potentiometer styr ljusstyrkan.
- En sensor som inte svarar ger felstatus.
- Seriella kommandon ändrar läge.
- Ett Wi-Fi-projekt visar anslutningsstatus med färg.

## Vanliga misstag

- **Misstag: Att koppla en lös LED utan seriemotstånd.**
  - Varför det händer: LED ser ut som en enkel lampa och många exempel visar kopplingen förenklat.
  - Hur du undviker det: Använd alltid seriemotstånd för lös LED om du inte vet att modulen redan har strömbegränsning.

- **Misstag: Att använda för låg resistans för att få starkare ljus.**
  - Varför det händer: LED lyser starkare när strömmen ökar.
  - Hur du undviker det: Börja med högre motstånd, till exempel 1 kΩ för indikatorer, och minska bara om du behöver mer ljus.

- **Misstag: Att glömma total strömgräns.**
  - Varför det händer: En LED fungerar, så tio LED antas också fungera.
  - Hur du undviker det: Räkna total ström och använd drivkrets eller transistor när många LED ska lysa samtidigt.

- **Misstag: Att blanda ihop common anode och common cathode på RGB-LED.**
  - Varför det händer: De kan se likadana ut.
  - Hur du undviker det: Testa en kanal i taget och kapsla inversionen i en funktion.

- **Misstag: Att använda `delay()` i ljuseffekter.**
  - Varför det händer: Det är det enklaste sättet att få blink och fade att fungera.
  - Hur du undviker det: Använd `millis()` för effekter som ska fungera samtidigt med sensorer, knappar och kommunikation.

- **Misstag: Att låta LED-kod spridas över hela programmet.**
  - Varför det händer: En status-LED känns liten och oviktig.
  - Hur du undviker det: Samla LED-styrning i funktioner eller en liten klass.

- **Misstag: Att använda färger inkonsekvent.**
  - Varför det händer: Färger väljs spontant i olika delar av projektet.
  - Hur du undviker det: Bestäm en enkel färgstandard, till exempel grön för OK, gul för väntan och röd för fel.

- **Misstag: Att driva LED-strippar eller starka LED från kortets 5 V-pinne utan kontroll.**
  - Varför det händer: 5 V-pinnen känns som en strömkälla.
  - Hur du undviker det: Kontrollera strömbehovet och använd separat matning när lasten växer.

## Kontrollpunkter för LED-kod

Använd punkterna när LED-koden beter sig fel eller när en indikator ska bli tydligare i ett större projekt.

- Kontrollera att varje lös LED har rätt seriemotstånd.
- Kontrollera polaritet innan du felsöker koden.
- Undvik `delay()` om LED-signalen ska fungera samtidigt som sensorer, motorer eller kommunikation.
- Använd egna funktioner för statuslägen i stället för att sprida blinklogik över hela programmet.
- Dokumentera bara färger och blinkmönster om de faktiskt används som felkoder eller driftlägen.
## Snabbreferens

| Fråga | Praktiskt svar |
|---|---|
| Behöver en lös LED motstånd? | Ja, normalt alltid. |
| Är 1 kΩ för mycket? | Ofta inte för statusindikatorer. |
| Kan en pinne driva en LED direkt? | Ja, om strömmen är låg och inom gränserna. |
| Kan en pinne driva många LED? | Vanligtvis inte utan drivkrets eller annan strategi. |
| Ska RGB-LED ha ett eller tre motstånd? | Tre, ett per färgkanal. |
| Varför lyser RGB bakvänt? | Troligen common anode eller inverterad modul. |
| När används PWM? | När ljusstyrka ska styras. |
| När används MOSFET? | När lasten kräver mer ström eller annan spänning än pinnen klarar. |
| När bör man välja adresserbara LED? | När många individuella färgpunkter ska styras med få pinnar. |
| Varför undvika `delay()`? | För att programmet ska kunna läsa sensorer, knappar och kommunikation samtidigt. |


## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Beror på koppling, ofta kortets logiknivå |
| Typiskt gränssnitt | Digital I/O eller PWM |
| Välj när | du behöver enkel status, feedback eller ljuseffekt |
| Välj inte när | du behöver många individuellt styrbara LED |
| Vanliga fel | saknat seriemotstånd, för hög pinström, fel polaritet |
| Alternativ att överväga | adresserbara LED, display, buzzer |

Använd referensrutan som en snabb kontroll innan du bygger projektet. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat


- Använd kapitel 7 när ljuset ska dimmas mjukt, tidsstyras eller uppdateras utan `delay()`.
- Använd kapitel 21 när LED-installationen kräver transistor, MOSFET eller annan laststyrning.
- Använd kapitel 34 när många LED:ar kräver separat matning, säkring, gemensam jord eller tydligare strömbudget.
