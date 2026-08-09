# 7. PWM, timers och tidsstyrning

## Tidsstyrning i praktiken
Många Arduino-projekt börjar med att tända en LED, läsa en knapp eller skriva ett värde till seriell monitor. Ganska snart vill man också styra något över tid: dimma en LED, skapa en mjuk övergång, låta en buzzer pipa i ett mönster, styra en motor ungefärligt, skicka mätvärden var femte sekund eller låta flera saker hända samtidigt utan att programmet låser sig.

Det är här PWM, timers och tidsstyrning blir centrala. För en erfaren programmerare är den viktiga insikten att Arduino-koden inte är “parallell” bara för att flera saker står i samma `loop()`. Om du använder `delay()` för att vänta blockerar du hela programmet. Det kan fungera i ett minimalt demoexempel, men det blir snabbt ett problem när programmet samtidigt ska läsa knappar, uppdatera en display, sampla en sensor, styra en LED-effekt och reagera på fel.

PWM, eller pulsbreddsmodulering, är ett sätt att skapa en styrsignal där utgången växlar snabbt mellan LOW och HIGH. Genom att ändra hur stor del av tiden signalen är HIGH kan vi styra upplevd ljusstyrka, ungefärlig motoreffekt eller en styringång på vissa moduler. Timers och tidsstyrning gör att vi kan planera när saker ska hända utan att stoppa resten av programmet.

Det här kapitlet binder ihop flera tidigare begrepp. Du använder digitala utgångar från kapitel 5, analoga värden från kapitel 6 och börjar bygga ett kodmönster som återkommer i kommande kapitel om aktuatorer, sensorer, kommunikation och robusta system.

Det praktiska värdet är framför allt att du kan använda `analogWrite()` för LED-dimning och enkel effektstyrning, känna igen skillnaden mellan duty cycle, frekvens och upplösning, och skriva tidsstyrd kod med `millis()` i stället för `delay()`. Samma mönster hjälper dig också att förstå varför PWM beter sig olika på olika kort och när timerresurser kan krocka med bibliotek för servo, ljud, motorer eller kommunikation.

## Förutsättningar

Du behöver ha med dig några begrepp från tidigare kapitel:

- från kapitel 4: spänning, ström, seriemotstånd och att en mikrokontrollerpinne bara klarar begränsad last
- från kapitel 5: digitala utgångar, HIGH, LOW och varför större laster behöver drivsteg
- från kapitel 6: att ett numeriskt värde i kod inte automatiskt betyder att den elektriska signalen är exakt eller kontinuerlig

Det är också viktigt att hålla isär två saker:

- **PWM som elektrisk signal:** en snabb växling mellan LOW och HIGH.
- **Tidsstyrning i programmet:** kod som bestämmer när saker ska ske.

De två hänger ofta ihop, men de är inte samma sak. Du kan använda PWM utan att själv skriva tidskod, till exempel med `analogWrite()`. Du kan också använda tidsstyrning utan PWM, till exempel för att läsa en sensor var tionde sekund.

## PWM som princip

PWM står för *pulse-width modulation*, på svenska ofta pulsbreddsmodulering. Signalen är digital: den är antingen LOW eller HIGH. Det som ändras är hur stor andel av en period signalen är HIGH.

Den andelen kallas **duty cycle**.

| Duty cycle | Signalens beteende | Typisk effekt |
|---|---|---|
| 0 % | Alltid LOW | LED släckt, ingen styrsignal |
| 25 % | HIGH en fjärdedel av tiden | Svagare ljus eller lägre effekt |
| 50 % | HIGH halva tiden | Mellannivå |
| 75 % | HIGH tre fjärdedelar av tiden | Starkare ljus eller högre effekt |
| 100 % | Alltid HIGH | Fullt på |

För en LED uppfattar ögat den snabba växlingen som en lägre ljusstyrka. För en DC-motor kan PWM ge ungefärlig hastighetsstyrning, förutsatt att motorn drivs via rätt drivkrets. För en värmelast kan PWM användas som långsam effektstyrning, men då med andra tidskonstanter och ofta med större hänsyn till säkerhet.

Det viktiga är att PWM inte gör pinnen till en riktig analog utgång. En pinne som kör PWM växlar fortfarande mellan två logiska nivåer. Om kortet använder 5 V-logik växlar signalen mellan 0 V och ungefär 5 V. Om kortet använder 3,3 V-logik växlar den mellan 0 V och ungefär 3,3 V.

## Duty cycle, frekvens och upplösning

Tre egenskaper är särskilt viktiga.

### Duty cycle

Duty cycle anger hur stor del av perioden signalen är HIGH. I Arduino-miljön anges den ofta som ett heltal. På många klassiska Arduino-kort används `analogWrite(pin, value)` där `value` ligger mellan 0 och 255.

```cpp
analogWrite(9, 0);     // 0 % ungefär: av
analogWrite(9, 64);    // cirka 25 %
analogWrite(9, 128);   // cirka 50 %
analogWrite(9, 255);   // 100 %: på
```

På kort med högre PWM-upplösning kan andra intervall förekomma, eller så finns funktioner för att konfigurera upplösning. Därför ska du inte utgå från att alla kort beter sig exakt som en klassisk Arduino UNO.

### Frekvens

Frekvensen anger hur många PWM-perioder som sker per sekund. För LED-dimning vill man normalt ha en frekvens som inte uppfattas som flimmer. För motorer kan frekvensen påverka ljud, vridmoment, värme och drivkretsens beteende. För vissa moduler behöver PWM-frekvensen ligga inom ett visst intervall.

En vanlig fallgrop är att bara ändra duty cycle och glömma frekvensen. Det fungerar ofta i enkla LED-tester men kan bli viktigt för motorer, buzzers, LED-drivare, switchade laster och mätningar med oscilloskop eller logikanalysator.

### Upplösning

Upplösningen anger hur många steg duty cycle kan ha. Med 8 bitar får du 256 steg, alltså 0–255. Med 10 bitar får du 1024 steg, alltså 0–1023. Högre upplösning kan ge mjukare övergångar, men den praktiska nyttan beror på frekvens, hårdvara och vad du styr.

För LED-effekter är också ögats upplevelse icke-linjär. En matematisk ökning från 0 till 255 upplevs inte som lika stora ljussteg. Därför används ibland gammakorrigering eller tabeller för mer visuellt jämna effekter. Vi håller oss här till grundprincipen, men återkommer till mer praktisk LED-styrning i kapitlen om LED och adresserbara LED.

## `analogWrite()` är inte samma sak som `analogRead()`

Namnen kan lura. `analogRead()` läser ett analogt värde via ADC. `analogWrite()` skapar på många kort en PWM-signal. Den skriver alltså inte nödvändigtvis en analog spänning.

Det här är extra viktigt när man kopplar in moduler som har en ingång märkt “analog”, “control”, “PWM” eller liknande. Kontrollera alltid vad modulen faktiskt förväntar sig:

- En PWM-ingång vill ofta ha en digital pulssignal.
- En analog styringång kan vilja ha en faktisk spänning.
- En digital ingång kan bara tolka LOW eller HIGH.
- En servosignalingång vill ha pulser med särskild timing, inte vanlig LED-PWM.

Om du behöver en mer äkta analog spänning finns några alternativ:

- använda ett kort med DAC, om kortet har det
- filtrera PWM med lågpassfilter, om signalen inte behöver ändras snabbt
- använda en extern DAC via I2C eller SPI
- välja en modul som accepterar PWM direkt

Det här är ett typiskt exempel på bokens återkommande princip: börja med att förstå signaltypen, inte bara funktionsnamnet i koden.

## PWM på olika Arduino-kompatibla kort

På klassiska Arduino-kort är PWM ofta kopplad till vissa pinnar. De är markerade i dokumentation eller på silkscreen, ofta med `~`. På andra kortfamiljer kan fler pinnar ha PWM-stöd, men implementationen kan se annorlunda ut.

Det finns flera skillnader att vara uppmärksam på:

- vilka pinnar som stöder PWM
- standardfrekvens
- standardupplösning
- om PWM delar timerresurser med andra funktioner
- om kortet använder 5 V- eller 3,3 V-logik
- hur bibliotek för motorer, servon, ljud eller LED påverkar timers

För portabel kod bör du därför dokumentera vad mönstret kräver:

```cpp
const int statusLedPin = 9;  // Must support PWM on the selected board.
```

En ännu bättre vana är att lägga pinout och antaganden högt upp i koden:

```cpp
/*
  Board assumptions:
  - statusLedPin must support PWM.
  - LED is connected through a suitable resistor to GND.
  - PWM output controls only a small indicator LED, not a load.
*/

const int statusLedPin = 9;
```

När du byter kort ska du kontrollera pinout och dokumentation innan du antar att samma pinne fungerar på samma sätt.

## Timers som underliggande resurs

En timer är en hårdvaruresurs i mikrokontrollern som kan räkna tid oberoende av din vanliga programlogik. Timers används för många saker:

- PWM-generering
- tidsfunktioner som `millis()` och `micros()`
- servoimpulser
- ton- eller ljudgenerering
- vissa bibliotek för motorstyrning
- tidskritiska protokoll och specialfunktioner

Du behöver inte förstå alla registerdetaljer för att använda Arduino effektivt, men du behöver förstå att timers är begränsade resurser. Två bibliotek kan ibland vilja använda samma timer. En ändring av PWM-frekvens på en pinne kan påverka en annan pinne. Ett servobibliotek kan påverka PWM på vissa pinnar på vissa kort.

Det här är en viktig skillnad mellan demo och robust projekt. I ett demoexempel syns konflikten sällan. I ett större projekt med servo, LED-dimning, buzzer, motor och tidsstyrda sensorer kan den bli mycket tydlig.

En praktisk tumregel är:

- använd standardfunktioner först
- ändra inte timerfrekvens eller låg nivå-konfiguration om du inte måste
- dokumentera när ett bibliotek använder timerresurser
- testa kombinationer tidigt, inte först när hela projektet är färdigt

## `delay()` och varför det blir problem

`delay(ms)` pausar programmet i ett antal millisekunder. Under tiden går inte din vanliga `loop()` vidare. En LED-blinkning med `delay()` är lätt att förstå:

```cpp
const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(500);
  digitalWrite(ledPin, LOW);
  delay(500);
}
```

Det här är pedagogiskt för ett första exempel, men det skalar dåligt. Om programmet väntar 500 ms kan det inte samtidigt reagera snabbt på en knapp, uppdatera en LED-effekt mjukt, läsa en sensor med rätt intervall eller hantera kommunikation.

Problemet är inte att `delay()` alltid är förbjudet. Problemet är att `delay()` är blockerande. I små testsketcher är det okej. I återanvändbara testmönster och systemkapitel ska vi oftast använda `millis()`.

## Icke-blockerande tid med `millis()`

`millis()` returnerar hur många millisekunder som gått sedan programmet startade, som ett heltalsvärde. I stället för att stoppa programmet kan vi kontrollera om tillräckligt mycket tid har passerat.

Grundmönstret är:

```cpp
const unsigned long blinkIntervalMs = 500;

unsigned long lastBlinkMs = 0;
bool ledOn = false;

void loop() {
  unsigned long now = millis();

  if (now - lastBlinkMs >= blinkIntervalMs) {
    lastBlinkMs = now;
    ledOn = !ledOn;
    digitalWrite(LED_BUILTIN, ledOn ? HIGH : LOW);
  }

  // Other code can run here.
}
```

Notera uttrycket:

```cpp
now - lastBlinkMs >= blinkIntervalMs
```

Det är bättre än att jämföra `now >= lastBlinkMs + blinkIntervalMs`, eftersom subtraktionsmönstret fungerar bättre när `millis()` förr eller senare rullar över sitt maxvärde. Du behöver inte göra något särskilt vid rollover om du håller dig till detta mönster med `unsigned long`.

## Flera saker samtidigt i samma `loop()`

Styrkan med `millis()` blir tydlig när flera aktiviteter ska ske med olika intervall.

```cpp
const int heartbeatLedPin = LED_BUILTIN;
const int pwmLedPin = 9;

const unsigned long heartbeatIntervalMs = 1000;
const unsigned long fadeIntervalMs = 10;
const unsigned long logIntervalMs = 1000;

unsigned long lastHeartbeatMs = 0;
unsigned long lastFadeMs = 0;
unsigned long lastLogMs = 0;

bool heartbeatOn = false;
int brightness = 0;
int fadeStep = 1;

void setup() {
  pinMode(heartbeatLedPin, OUTPUT);
  pinMode(pwmLedPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  unsigned long now = millis();

  updateHeartbeat(now);
  updateFade(now);
  updateLog(now);

  // Sensor reads, button handling and communication can be added here.
}

void updateHeartbeat(unsigned long now) {
  if (now - lastHeartbeatMs < heartbeatIntervalMs) {
    return;
  }

  lastHeartbeatMs = now;
  heartbeatOn = !heartbeatOn;
  digitalWrite(heartbeatLedPin, heartbeatOn ? HIGH : LOW);
}

void updateFade(unsigned long now) {
  if (now - lastFadeMs < fadeIntervalMs) {
    return;
  }

  lastFadeMs = now;

  brightness += fadeStep;

  if (brightness <= 0 || brightness >= 255) {
    fadeStep = -fadeStep;
    brightness = constrain(brightness, 0, 255);
  }

  analogWrite(pwmLedPin, brightness);
}

void updateLog(unsigned long now) {
  if (now - lastLogMs < logIntervalMs) {
    return;
  }

  lastLogMs = now;

  Serial.print("brightness=");
  Serial.println(brightness);
}
```

Det här är ett kodmönster som vi kommer återanvända. Varje funktion gör lite arbete och returnerar snabbt. Programmet upplevs som att flera saker sker samtidigt, men allt körs fortfarande i en enda `loop()`.

## Periodisk uppgift som återanvändbart mönster

När ett program växer kan du göra tidsstyrningen tydligare genom att skapa en liten struktur för återkommande uppgifter.

```cpp
struct PeriodicTask {
  unsigned long intervalMs;
  unsigned long lastRunMs;
};

bool shouldRun(PeriodicTask &task, unsigned long now) {
  if (now - task.lastRunMs < task.intervalMs) {
    return false;
  }

  task.lastRunMs = now;
  return true;
}
```

Sedan kan du använda den så här:

```cpp
PeriodicTask sensorTask = { 1000, 0 };
PeriodicTask ledTask = { 10, 0 };
PeriodicTask logTask = { 2000, 0 };

void loop() {
  unsigned long now = millis();

  if (shouldRun(sensorTask, now)) {
    readSensor();
  }

  if (shouldRun(ledTask, now)) {
    updateLedEffect();
  }

  if (shouldRun(logTask, now)) {
    printStatus();
  }
}
```

Det här är inte en full task scheduler. Det är bara ett enkelt och begripligt mönster som räcker långt i Arduino-projekt. För den här bokens målgrupp är det också ett bra sätt att tänka modulärt utan att göra varje mönster onödigt abstrakt.

## PWM, LED och seriemotstånd

När du dimmar en enkel LED med PWM behöver LED:en fortfarande ett seriemotstånd. PWM begränsar inte strömmen på ett säkert sätt. När signalen är HIGH ser LED:en samma elektriska situation som vid vanlig digital utgång, bara under kortare delar av tiden.

En förenklad koppling är:

- PWM-pinne till seriemotstånd
- seriemotstånd till LED-anod
- LED-katod till GND

Eller tvärtom, beroende på hur du väljer att koppla, men principen är densamma: LED-strömmen måste begränsas.

Om du styr många LED, LED-strippar eller starkare ljuskällor behöver du extern matning och drivsteg. Det kommer i senare kapitel. Här håller vi oss till en enkel indikator-LED.

## PWM och motorer

PWM används ofta för motorstyrning, men en mikrokontrollerpinne ska inte driva en motor direkt. Motorn behöver en drivkrets, exempelvis MOSFET, H-brygga eller färdig motordrivarmodul. Motorn kan dessutom skapa störningar, spänningsdippar och induktiva spikar.

För motorer behöver du tänka på:

- motorns startström
- separat matning
- gemensam jord mellan logik och drivsteg, om drivningen inte är isolerad
- flyback-skydd eller inbyggt skydd i drivmodulen
- PWM-frekvens som passar drivaren och motorn
- värme i drivkretsen

I detta kapitel använder vi PWM med LED eftersom det är säkert och lätt att observera. Motorer får en egen fördjupning senare.

## PWM och servon

Servon är en vanlig källa till begreppsförvirring. Ett hobbyservo styrs ofta med pulser, men det är inte samma sak som vanlig `analogWrite()`-PWM för LED-dimning. Servon förväntar sig typiskt återkommande styrpulser med en viss pulslängd som motsvarar position.

I Arduino använder man normalt ett servobibliotek i stället för `analogWrite()`:

```cpp
#include <Servo.h>

Servo pointerServo;

void setup() {
  pointerServo.attach(9);
}

void loop() {
  pointerServo.write(30);
  delay(500);
  pointerServo.write(150);
  delay(500);
}
```

Exemplet ovan använder `delay()` för enkelhet, men i senare kapitel ska vi styra servon utan blockerande väntan. Poängen här är att servoimpulser är en särskild typ av tidsstyrd signal och att servobibliotek kan använda timerresurser som påverkar annan PWM på vissa kort.

## PWM och buzzers

En passiv buzzer eller piezo kan styras med en fyrkantsvåg i hörbart frekvensområde. Arduino-funktionen `tone()` kan användas på många klassiska kort för att skapa ton. Det är lätt att tro att `analogWrite()` och `tone()` är samma typ av sak eftersom båda växlar en pinne över tid, men syftet är olika.

- `analogWrite()` används ofta för duty cycle-styrning vid en viss PWM-frekvens.
- `tone()` används för att skapa en frekvens som motsvarar en ton.
- En aktiv buzzer behöver ofta bara HIGH/LOW eftersom den har inbyggd oscillator.
- En passiv buzzer behöver en växlande signal för att skapa ljud.

Även här kan timerresurser spela roll. Om ett projekt använder servo, tone, motor-PWM och tidskritiska LED-bibliotek samtidigt ska du testa kombinationen tidigt.

## När PWM är rätt val

PWM är ofta rätt val när du vill styra effekt eller upplevd nivå med enkel digital hårdvara.

Typiska användningar:

- dimma en enkel LED
- styra ljusstyrka i en LED-list via MOSFET
- styra ungefärlig hastighet på DC-motor via drivkrets
- styra en fläkt som accepterar PWM
- skapa enkel värmestyrning med lämplig drivning
- mata en lågpassfilterkrets för att få en långsamt varierande spänning

PWM är mindre lämpligt när du behöver:

- en exakt analog spänning
- lågbrusig mätsignal
- ljud av hög kvalitet
- exakt motorposition utan återkoppling
- styrning av last utan rätt drivsteg
- kompatibilitet utan att kontrollera kortets PWM-stöd

## Referensmönster: icke-blockerande LED-fade

Det här referensmönstret visar en PWM-styrd LED-effekt som ändrar ljusstyrka utan `delay()`. Samtidigt blinkar den inbyggda LED:en som heartbeat och programmet skriver status till seriell monitor. Det visar att flera aktiviteter kan ske samtidigt i en enkel Arduino-sketch.

### Vad mönstret visar

Mönstret visar hur du:

- kopplar en LED till en PWM-kompatibel pinne
- skapar en mjuk fade-effekt med `analogWrite()`
- använder `millis()` för icke-blockerande tidsstyrning
- kör flera periodiska uppgifter i samma `loop()`
- gör kortets antaganden tydliga i koden

### Det här används i exemplet

Du behöver:

- ett Arduino-kompatibelt kort
- en LED
- ett seriemotstånd, exempelvis 220–1000 ohm beroende på LED och matning
- kopplingskablar
- breadboard
- USB-kabel
- dator med Arduino IDE eller motsvarande miljö

### Koppling

Använd en pinne som stöder PWM på ditt kort. I många UNO-liknande exempel används pinne 9, men kontrollera alltid ditt kort.

En enkel koppling:

- PWM-pinne 9 till seriemotstånd
- seriemotstånd till LED-anod
- LED-katod till GND

Om LED:en inte lyser när programmet körs, kontrollera först polaritet, GND och att pinnen verkligen stöder PWM.

### Kod

```cpp
/*
  Non-blocking PWM fade reference pattern.

  Board assumptions:
  - pwmLedPin must support PWM.
  - LED is connected through a suitable resistor to GND.
  - LED_BUILTIN is available for heartbeat.
  - Serial monitor is set to 115200 baud.
*/

const int pwmLedPin = 9;
const int heartbeatLedPin = LED_BUILTIN;

const unsigned long fadeIntervalMs = 8;
const unsigned long heartbeatIntervalMs = 500;
const unsigned long logIntervalMs = 1000;

unsigned long lastFadeMs = 0;
unsigned long lastHeartbeatMs = 0;
unsigned long lastLogMs = 0;

int brightness = 0;
int fadeStep = 1;
bool heartbeatOn = false;

void setup() {
  pinMode(pwmLedPin, OUTPUT);
  pinMode(heartbeatLedPin, OUTPUT);

  Serial.begin(115200);
  Serial.println("PWM fade pattern started");
}

void loop() {
  unsigned long now = millis();

  updateFade(now);
  updateHeartbeat(now);
  updateLog(now);
}

void updateFade(unsigned long now) {
  if (now - lastFadeMs < fadeIntervalMs) {
    return;
  }

  lastFadeMs = now;

  brightness += fadeStep;

  if (brightness >= 255) {
    brightness = 255;
    fadeStep = -1;
  }

  if (brightness <= 0) {
    brightness = 0;
    fadeStep = 1;
  }

  analogWrite(pwmLedPin, brightness);
}

void updateHeartbeat(unsigned long now) {
  if (now - lastHeartbeatMs < heartbeatIntervalMs) {
    return;
  }

  lastHeartbeatMs = now;
  heartbeatOn = !heartbeatOn;
  digitalWrite(heartbeatLedPin, heartbeatOn ? HIGH : LOW);
}

void updateLog(unsigned long now) {
  if (now - lastLogMs < logIntervalMs) {
    return;
  }

  lastLogMs = now;

  Serial.print("brightness=");
  Serial.print(brightness);
  Serial.print(", fadeStep=");
  Serial.println(fadeStep);
}
```

### Förväntat beteende

När koden körs ska den externa LED:en mjukt öka och minska i ljusstyrka. Den inbyggda LED:en ska blinka i annat tempo. Seriell monitor ska visa ljusstyrkevärden ungefär en gång per sekund.

Testa sedan att ändra:

- `fadeIntervalMs`
- `fadeStep`
- `heartbeatIntervalMs`
- PWM-pinne

Observera vad som händer om `fadeStep` blir större, till exempel 5 eller 10. Effekten går snabbare men kan också upplevas mindre mjuk.

### Gör mönstret lättare att återanvända

Lägg till en kommentar i början av filen där du dokumenterar:

- vilket kort du använde
- vilken pinne som användes för PWM
- om kortet använder 5 V eller 3,3 V-logik
- vilket motstånd du använde
- om LED:en var kopplad aktiv HIGH eller aktiv LOW
- vilken PWM-upplösning du antar i koden

Det här gör mönstret lättare att flytta till andra kort.

## Variant: LED-fade styrd av analog ingång

Du kan kombinera kapitel 6 och 7 genom att låta en potentiometer styra PWM-värdet. Varianten nedan håller även läsningen tidsstyrd med `millis()`, så att huvudprogrammet inte blockeras.

```cpp
const int potPin = A0;
const int pwmLedPin = 9;

const unsigned long sampleIntervalMs = 20;
unsigned long lastSampleMs = 0;

void setup() {
  pinMode(pwmLedPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  unsigned long now = millis();

  if (now - lastSampleMs >= sampleIntervalMs) {
    lastSampleMs = now;

    int raw = analogRead(potPin);
    int brightness = map(raw, 0, 1023, 0, 255);
    brightness = constrain(brightness, 0, 255);

    analogWrite(pwmLedPin, brightness);

    Serial.print("raw=");
    Serial.print(raw);
    Serial.print(", brightness=");
    Serial.println(brightness);
  }

  // Annan tidsstyrd kod kan köras här.
}
```

Exemplet visar en viktig begränsning: `map(raw, 0, 1023, 0, 255)` antar 10-bitars ADC. På andra kort kan ADC-upplösningen vara en annan, eller kunna konfigureras.

En mer portabel variant är att definiera gränserna själv:

```cpp
const int analogMin = 0;
const int analogMax = 1023;
const int pwmMin = 0;
const int pwmMax = 255;

int brightness = map(raw, analogMin, analogMax, pwmMin, pwmMax);
brightness = constrain(brightness, pwmMin, pwmMax);
```

I senare kapitel kommer vi återkomma till hur sensordata styr aktuatorer. Det här är den enklaste formen av samma idé: mät något, översätt värdet och styr en utgång.
## Vanliga misstag

- **Misstag:** Att tro att `analogWrite()` ger en äkta analog spänning.
  - **Varför det händer:** Namnet låter som motsatsen till `analogRead()`.
  - **Hur man undviker det:** Beskriv signalen som PWM om den växlar mellan LOW och HIGH, och använd DAC eller filter när du behöver en faktisk analog nivå.

- **Misstag:** Att använda `delay()` i alla tidsstyrda exempel.
  - **Varför det händer:** `delay()` är lätt att förstå och finns i många introduktionsexempel.
  - **Hur man undviker det:** Använd `millis()` för återkommande uppgifter så fort programmet ska göra mer än en sak.

- **Misstag:** Att välja en pinne som inte stöder PWM.
  - **Varför det händer:** Alla digitala pinnar ser ofta lika ut i koden.
  - **Hur man undviker det:** Kontrollera pinout och dokumentera att pinnen måste ha PWM-stöd.

- **Misstag:** Att styra motorer, reläer eller LED-strippar direkt från en mikrokontrollerpinne.
  - **Varför det händer:** Samma kod fungerar för en liten LED och ger intryck av att pinnen “styr lasten”.
  - **Hur man undviker det:** Använd drivkrets, MOSFET, relämodul eller motor-driver och separat matning där det behövs.

- **Misstag:** Att ändra timerinställningar utan att förstå sidokonsekvenser.
  - **Varför det händer:** Exempel på nätet visar ibland registerändringar för att ändra PWM-frekvens.
  - **Hur man undviker det:** Börja med standardfunktioner, ändra låg nivå-konfiguration bara när du behöver det och testa alla bibliotek tillsammans.

- **Misstag:** Att jämföra tid med `now >= previous + interval`.
  - **Varför det händer:** Uttrycket ser intuitivt ut.
  - **Hur man undviker det:** Använd `now - previous >= interval` med `unsigned long` för robustare hantering av rollover.

## Praktiska tidsmönster att återanvända

Blink utan `delay()` är grundmönstret för tidsstyrd kod. När ett projekt ska blinka, läsa, logga och uppdatera utgångar samtidigt är det bättre att ge varje aktivitet ett eget tidsintervall än att stapla `delay()`-anrop.

Några mönster som ofta räcker långt:

- En heartbeat-LED kan blinka med ett eget `lastHeartbeatMs` utan att blockera resten av programmet.
- Flera samtidiga intervall bör ha separata tidsvariabler och helst egna funktioner.
- En analog ingång kan styra fade-hastighet, intervall eller steglängd, men bör inte stoppa huvudloopen.
- En enkel task-struktur med namn som `readInputTask`, `updateOutputTask` och `logTask` gör små projekt lättare att förstå.
- PWM-beteende kan skilja mellan kort. Kontrollera därför pinne, upplösning och frekvens när ljus, motorer eller ljud beter sig oväntat.

## Snabbreferens

| Begrepp | Kort förklaring | Praktisk fråga |
|---|---|---|
| PWM | Digital signal med varierande duty cycle | Stöder pinnen PWM? |
| Duty cycle | Andel av perioden som signalen är HIGH | Vilken nivå vill jag uppnå? |
| Frekvens | Antal perioder per sekund | Ger signalen flimmer, ljud eller fel styrning? |
| Upplösning | Antal möjliga duty cycle-steg | Behöver övergången vara mjuk? |
| Timer | Hårdvaruresurs för tid och signaler | Krockar något bibliotek med PWM? |
| `delay()` | Blockerande väntan | Kan programmet göra annat under tiden? |
| `millis()` | Millisekundräknare sedan start | Kan jag tidsstyra utan att blockera? |
| Rollover | När tidsräknaren börjar om | Använder jag subtraktionsmönstret? |

## Relaterat

- Använd kapitel 17 när PWM används för LED-dimning och mjuka ljuseffekter.
- Använd kapitel 19 och 20 när timing påverkar ljud, servon eller motorstyrning.
- Använd kapitel 8 när tidsstyrningen behöver kombineras med avbrott, timeouts eller watchdog.
