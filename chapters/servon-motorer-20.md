# 20. Servon, DC-motorer och stegmotorer

## Rörelseöversikt
Det här kapitlet hjälper dig välja och använda rörelse i Arduino-projekt: servo, kontinuerlig servo, DC-motor eller stegmotor. Använd det när något ska vridas, snurra, flyttas, öppnas, stängas eller ge fysisk återkoppling.

Kapitlet hjälper dig framför allt att:

- välja rätt motortyp för projektets rörelse
- förstå varför motorer nästan alltid behöver separat drivning eller separat matning
- koppla styrsignal, matning och gemensam jord på ett säkrare sätt
- skriva rörelsekod som inte blockerar resten av systemet
- felsöka ryckande servon, svaga motorer, tappade steg och reset vid belastning
- känna igen vanliga motor- och drivmoduler som PCA9685, ULN2003, L298N, DRV8833, L9110S och A4988/DRV8825

## Förutsättningar

Du bör känna till digital I/O, PWM och grundläggande strömförsörjning. Se särskilt kapitel 4 om elektriska grunder, kapitel 7 om PWM och kapitel 34 om matning, batteridrift och störningar.

## Tre typer av rörelse

Det är lätt att säga “motor” om allt som rör sig, men valet blir enklare om du först frågar vilken typ av rörelse du behöver.

| Behov | Typiskt val | Kommentar |
|---|---|---|
| Vrid något till en ungefärlig vinkel | Standardservo | Enkel att använda, men begränsat rörelseområde. |
| Snurra kontinuerligt med enkel hastighetsstyrning | DC-motor | Bra för hjul, fläktar och pumpar, men behöver ofta återkoppling för exakt position. |
| Flytta i många små steg | Stegmotor | Bra för kontrollerad rörelse, men kan tappa steg om den överbelastas. |
| Styra en borstlös motor | ESC + borstlös motor | Vanligt för drönare, RC och kraftigare rotation. |
| Dra eller trycka linjärt | Linjär aktuator, servo eller stegmotor med mekanik | Valet beror på kraft, slaglängd och precision. |

I praktiska Arduino-projekt är servon ofta enklast att börja med. De har inbyggd styrning och kräver bara en styrsignal, matning och jord. DC-motorer kräver mer drivkretslogik men är enkla när du bara vill snurra något. Stegmotorer är mer strukturerade, men kräver rätt drivare, strömbegränsning och acceleration för att bli pålitliga.

## Servo: position med enkel styrsignal

En standardservo är en liten motorenhet med motor, växellåda, positionsåterkoppling och intern styrelektronik i samma kapsling. Du skickar en styrpuls som motsvarar önskad position. Servon försöker sedan vrida axeln till den positionen och hålla den där.

Det gör servon mycket användbara för:

- små mekaniska indikatorer
- luckor och spjäll
- pan-tilt-fästen för sensorer eller kameror
- enkla robotarmar
- modellbygge och RC-liknande projekt
- fysisk återkoppling i interaktiva installationer

En vanlig hobbyservo har tre ledare:

| Ledare | Typisk färg | Funktion |
|---|---|---|
| GND | Brun eller svart | Jord. |
| VCC | Röd | Matning, ofta cirka 5 V beroende på servo. |
| Signal | Orange, gul eller vit | Styrpuls från mikrokontrollern. |

Färger kan variera. Kontrollera alltid servo, modul eller datablad innan du kopplar.

### Servosignal

En hobbyservo styrs normalt med återkommande pulser. I Arduino-världen behöver du oftast inte generera pulserna själv. Du använder biblioteket `Servo` och anger en vinkel eller pulsbredd.

Exempel:

```cpp
#include <Servo.h>

const int servoPin = 9;

Servo pointerServo;

void setup() {
  pointerServo.attach(servoPin);
  pointerServo.write(90);
}

void loop() {
  pointerServo.write(30);
  delay(1000);

  pointerServo.write(150);
  delay(1000);
}
```

Det här är ett enkelt test, men det använder `delay()`. I ett riktigt projekt vill du ofta undvika det så att sensorer, LED, ljud och kommunikation fortfarande kan uppdateras.

### Icke-blockerande servorörelse

En bättre struktur är att flytta servon stegvis med `millis()`.

```cpp
#include <Servo.h>

const int servoPin = 9;

Servo pointerServo;

int currentAngle = 20;
int targetAngle = 160;

unsigned long lastMoveMs = 0;
const unsigned long moveIntervalMs = 20;

void setup() {
  Serial.begin(115200);
  pointerServo.attach(servoPin);
  pointerServo.write(currentAngle);
}

void loop() {
  updateServo();

  // Här kan annan kod köras:
  // readSensors();
  // updateStatusLed();
  // handleSerialCommands();
}

void updateServo() {
  unsigned long now = millis();

  if (now - lastMoveMs < moveIntervalMs) {
    return;
  }

  lastMoveMs = now;

  if (currentAngle < targetAngle) {
    currentAngle++;
    pointerServo.write(currentAngle);
  } else if (currentAngle > targetAngle) {
    currentAngle--;
    pointerServo.write(currentAngle);
  } else {
    if (targetAngle == 160) {
      targetAngle = 20;
    } else {
      targetAngle = 160;
    }
  }
}
```

Det här mönstret är viktigare än själva servon. Samma princip kommer tillbaka i motorstyrning, sensormätning och användargränssnitt: gör lite arbete ofta i stället för att låsa programmet i långa väntan.

### Servo och matning

En av de vanligaste fallgroparna är att driva servon direkt från Arduino-kortets 5 V-pin och anta att allt är bra eftersom servon rör sig utan belastning. En liten servo kan ibland fungera så i ett kort experiment, men det är inte en robust design.

Servon kan dra betydligt mer ström när de:

- startar från stillastående
- bromsar snabbt
- håller position under belastning
- når mekaniskt stopp
- rör en trög mekanism
- är av låg kvalitet eller har kärv växellåda

Ett mer robust servoprojekt använder ofta separat 5 V-matning för servon. Då ska jord vara gemensam mellan servomatningen och Arduino-kortet.

Grundprincip:

```text
Arduino GND  -------- Servo power GND
Arduino pin  -------- Servo signal
Servo +5 V   -------- Extern 5 V-matning
Servo GND    -------- Extern 5 V GND
```

Gemensam jord behövs för att styrsignalen ska ha samma referens. Utan gemensam jord kan servon rycka, ignorera signalen eller bete sig slumpmässigt.

### När servo är rätt val

Välj servo när:

- du behöver styra en position snarare än bara hastighet
- rörelseområdet är begränsat
- lasten är liten nog för servons vridmoment
- du vill ha enkel kod och enkel koppling
- precisionen inte behöver vara industriell
- mekanismen kan tolerera lite spel och ryck

Välj något annat när:

- axeln måste rotera kontinuerligt med kontrollerad hastighet
- du behöver mycket kraft under lång tid
- mekanismen kan slå hårt i ändlägen
- du behöver exakt linjär rörelse
- du behöver tyst, jämn eller mycket långvarig drift
- servon skulle stå och kämpa mot en konstant mekanisk last

### Många servon med PCA9685

När du bara styr en eller två servon kan en vanlig PWM-kompatibel pinne och biblioteket `Servo` räcka långt. När projektet växer till många servon blir det däremot lättare att använda en separat servodrivarmodul. Den vanligaste i Arduino-sammanhang är **PCA9685**, en I2C-styrd PWM-driver med många kanaler.

PCA9685 är vanlig i robotarmar, pan-tilt-lösningar, animatronik, små benrobotar och andra projekt där flera servon ska röra sig oberoende av varandra.

PCA9685 hjälper med:

- många PWM-kanaler via I2C
- jämnare uppdatering än om all servostyrning görs direkt från mikrokontrollern
- enklare kabeldragning när många servon ska samlas på en modul
- möjlighet att låta logik och servomatning hanteras tydligare som separata delar

Den löser däremot inte strömproblemet. Servona behöver fortfarande en matning som klarar belastningen, och mikrokontroller, PCA9685-modul och servomatning behöver gemensam jord.

En bra tumregel:

> PCA9685 gör många servosignaler enklare. Den gör inte många servon strömsnåla.

Kontrollera särskilt:

- att servomatningen är dimensionerad för flera servon samtidigt
- att GND är gemensam mellan kort, PCA9685 och servomatning
- att I2C-adressen inte krockar med andra moduler
- att servona inte slår i mekaniska ändlägen
- att kablar och kontakter klarar den förväntade strömmen

## Kontinuerlig servo

En kontinuerlig servo ser ofta ut som en vanlig hobbyservo men fungerar mer som en liten växlad DC-motor med servoingång. I stället för att `write(90)` betyder “gå till 90 grader” betyder det ofta “stanna ungefär”. Lägre värden roterar åt ett håll, högre värden åt andra hållet och avståndet från stoppunkten påverkar hastigheten.

Exempel:

```cpp
#include <Servo.h>

const int servoPin = 9;

Servo wheelServo;

void setup() {
  wheelServo.attach(servoPin);
}

void loop() {
  wheelServo.write(90);   // ungefär stopp
  delay(1000);

  wheelServo.write(70);   // rotera åt ena hållet
  delay(1000);

  wheelServo.write(90);   // stopp
  delay(1000);

  wheelServo.write(110);  // rotera åt andra hållet
  delay(1000);
}
```

Kontinuerliga servon är praktiska i små robotprojekt, men de ska inte misstas för positionerande servon. De vet normalt inte exakt var de är. Om du behöver position behöver du antingen en vanlig servo, en stegmotor, encoderåterkoppling eller annan mätning.

## DC-motor: enkel rotation med extern drivare

En DC-motor är enkel som komponent: ge den spänning och den snurrar. Byt polaritet och den snurrar åt andra hållet. Sänk den genomsnittliga effekten med PWM och den snurrar långsammare.

Men DC-motorer är inte enkla för en mikrokontrollerpinne. En pinne ska inte driva en motor direkt. Motorn behöver en drivare som kan hantera ström, induktiva störningar och ofta riktning.

DC-motorer passar för:

- hjul
- fläktar
- pumpar
- små transportband
- vibration
- enkel rotation där exakt position inte krävs

### Varför H-brygga används

För att styra riktning på en DC-motor används ofta en H-brygga. Den låter drivaren koppla motorns båda terminaler så att strömmen kan gå åt ena eller andra hållet.

En typisk motordrivarmodul har signaler som:

| Signal | Funktion |
|---|---|
| IN1 | Riktning eller halvbryggestyrning. |
| IN2 | Riktning eller halvbryggestyrning. |
| EN eller PWM | Aktiverar motor och styr hastighet med PWM. |
| VM eller Vmotor | Separat motorström. |
| VCC eller logic | Logikmatning för modulen. |
| GND | Gemensam jord. |

Modulnamn och signaler varierar. Vissa billiga moduler bygger på äldre drivkretsar med högre spänningsfall. Modernare MOSFET-baserade drivare är ofta effektivare.

### Grundläggande DC-motorkod

Det här exemplet visar principen för en enkel H-brygga med två riktningspinnar och en PWM-pinne.

```cpp
const int motorIn1Pin = 7;
const int motorIn2Pin = 8;
const int motorPwmPin = 9;

void setup() {
  pinMode(motorIn1Pin, OUTPUT);
  pinMode(motorIn2Pin, OUTPUT);
  pinMode(motorPwmPin, OUTPUT);

  stopMotor();
}

void loop() {
  driveForward(180);
  delay(2000);

  stopMotor();
  delay(1000);

  driveReverse(180);
  delay(2000);

  stopMotor();
  delay(1000);
}

void driveForward(int speedValue) {
  digitalWrite(motorIn1Pin, HIGH);
  digitalWrite(motorIn2Pin, LOW);
  analogWrite(motorPwmPin, constrain(speedValue, 0, 255));
}

void driveReverse(int speedValue) {
  digitalWrite(motorIn1Pin, LOW);
  digitalWrite(motorIn2Pin, HIGH);
  analogWrite(motorPwmPin, constrain(speedValue, 0, 255));
}

void stopMotor() {
  analogWrite(motorPwmPin, 0);
  digitalWrite(motorIn1Pin, LOW);
  digitalWrite(motorIn2Pin, LOW);
}
```

Som testkod är detta tydligt, men den är fortfarande blockande. I ett mer komplett system skulle du skapa en motorfunktion som uppdateras med tidslogik på samma sätt som servot.

### Hastighet är inte samma sak som PWM-värde

Ett vanligt misstag är att tro att `analogWrite(128)` betyder “halv hastighet”. Det betyder bara ungefär 50 procent duty cycle på styrsignalen. Motorns faktiska hastighet beror på:

- matningsspänning
- last
- friktion
- motorstorlek
- drivkretsens spänningsfall
- PWM-frekvens
- batteriets skick
- mekanikens tröghet

Om du behöver verklig hastighetskontroll behöver du återkoppling, till exempel encoder, hall-sensor eller annan mätning. Utan återkoppling gör du öppen styrning: du begär en effekt, inte en garanterad hastighet.

### Startström och stallström

DC-motorer kan dra mycket hög ström när de står stilla eller blockeras. Detta kallas ofta stallström. Det är en viktigare siffra än den ström motorn drar när den snurrar fritt utan last.

Om motorns stallström är större än drivaren eller matningen klarar kan följden bli:

- mikrokontrollern startar om
- regulatorn blir varm
- drivkretsen stänger av sig
- batterispänningen sjunker
- kommunikationen blir instabil
- motorn blir svag eller ryckig
- komponenter skadas

När du väljer drivare bör du därför inte bara titta på “typisk ström” utan även på start- och blockeringsfall.

### L298N: vanlig, men ofta inte bästa moderna valet

**L298N** är en mycket vanlig motor-driver-modul i Arduino-kit och elektronikbutiker. Den används ofta för små DC-motorer och ibland som första H-brygga i robotprojekt. Den är praktisk eftersom den ofta har skruvterminaler, tydliga ingångar och färdig modulform.

Samtidigt är L298N en äldre bipolär H-brygga med relativt höga spänningsförluster. Det betyder att en märkbar del av energin kan bli värme i drivaren i stället för rörelse i motorn. Vid batteridrift eller högre motorström är en modern MOSFET-baserad motor-driver ofta bättre.

L298N kan vara rimlig när:

- du lär dig principen för riktning och PWM
- motorerna är små och kraven låga
- modulen redan finns i ett startkit
- effektivitet inte är avgörande
- du accepterar värme och spänningsfall som del av experimentet

Välj hellre modernare motor-driver när:

- projektet ska gå på batteri länge
- motorn drar hög startström
- drivaren blir varm
- motorn känns svag trots tillräcklig matning
- projektet ska bli en mer permanent lösning


### DRV8833 och L9110S i små motorprojekt

När du väljer drivare för små DC-motorer behöver du inte automatiskt börja med L298N. Två vanliga alternativ i små robot- och kitprojekt är **DRV8833** och **L9110S**.

DRV8833 är ofta ett bättre val än L298N när projektet är litet, batteridrivet och använder små motorer. Den är vanligtvis effektivare och mer kompakt, men du måste fortfarande kontrollera motorström, stallström, kylning och matningsspänning.

L9110S är enklare och billigare. Den kan fungera för små, lätta DC-motorer i enkla robotbyggen, men den är inte rätt val för tyngre laster eller motorer som riskerar att fastna mekaniskt. Om du är osäker: välj drivare efter motorns start- och stallström, inte efter att modulen råkar finnas i lådan.


## Stegmotor: rörelse i diskreta steg

En stegmotor rör sig i steg. Den är byggd så att magnetfält i motorlindningarna flyttar rotorn mellan diskreta positioner. Med rätt drivare kan du säga åt motorn att ta ett visst antal steg i en riktning.

Stegmotorer används ofta när man vill ha repeterbar rörelse utan direkt positionssensor:

- 3D-skrivare
- CNC-liknande småmaskiner
- kameraskjutare
- vridbord
- pumpar
- precisionsmekanik
- instrument och indikatorer

En viktig skillnad mot servo är att en stegmotor normalt inte vet om den faktiskt lyckades ta stegen. Den antar att rörelsen skedde. Om lasten är för hög eller accelerationen för snabb kan den tappa steg.

### Unipolära och bipolära stegmotorer

I Arduino-projekt möter du ofta två typer:

| Typ | Vanligt exempel | Kommentar |
|---|---|---|
| Unipolär liten stegmotor | 28BYJ-48 med ULN2003-modul | Billig, långsam, enkel, ofta 5 V. |
| Bipolär stegmotor | NEMA 17 med A4988/DRV8825/TMC-drivare | Vanlig i 3D-skrivare och mer kraftfulla projekt. |

Den lilla 28BYJ-48 är vanlig i startkit. Den är bra för att lära sig principerna men är långsam och har växellåda med spel. En NEMA 17 med strömbegränsande drivare är mer relevant för mekaniska system men kräver mer omsorg kring matning, strömgräns, kylning och acceleration.

### Steg och riktning med drivare

Många moderna stegmotordrivare använder två huvudsignaler:

| Signal | Funktion |
|---|---|
| STEP | Varje puls betyder ett steg eller mikro-steg. |
| DIR | Anger riktning. |
| ENABLE | Aktiverar eller avaktiverar drivaren. |
| VMOT | Motormatning. |
| GND | Gemensam jord och motormatningens retur. |
| Logic VCC | Logikmatning på vissa moduler. |

Det gör Arduino-koden enkel på ytan:

```cpp
const int stepPin = 3;
const int dirPin = 4;
const int enablePin = 5;

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enablePin, OUTPUT);

  digitalWrite(enablePin, LOW); // vanligt på många drivare, men kontrollera modulen
  digitalWrite(dirPin, HIGH);
}

void loop() {
  for (int i = 0; i < 200; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(800);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(800);
  }

  delay(1000);

  digitalWrite(dirPin, !digitalRead(dirPin));
}
```

Det här är pedagogiskt men blockande. För jämnare och mer robust rörelse använder man ofta ett bibliotek eller en egen tidsstyrd step-generator.

### 28BYJ-48 och ULN2003: klassisk kit-stegmotor

En mycket vanlig kombination i Arduino-kit är **28BYJ-48** tillsammans med en **ULN2003-driverkort**. Den dyker ofta upp i nybörjarpaket eftersom motorn är billig, drivmodulen är enkel och det finns många exempel.

Kombinationen passar bra för:

- långsamma indikatorer
- små vridbord
- enkla mekaniska demonstrationer
- projekt där låg kostnad är viktigare än hög precision och kraft

Den passar sämre när du behöver hög hastighet, högt moment eller exakt mekanisk prestanda. 28BYJ-48 har ofta växellåda, och växellådan kan ge glapp. Det gör den användbar för enkla rörelser, men inte idealisk för allt som kräver exakt positionering.

Tänk på:

- kontrollera om motorn är 5 V eller annan spänning
- mata inte motorn direkt från mikrokontrollerpinnen
- använd ULN2003-modulen eller annan lämplig drivning
- räkna med långsam rörelse
- undvik att överbelasta växellådan

### A4988 och DRV8825: vanliga STEP/DIR-drivare

För bipolära stegmotorer, till exempel NEMA 17-liknande motorer, är **A4988** och **DRV8825** vanliga drivmoduler. De används ofta i 3D-skrivare, små CNC-maskiner, kameraskjutare och mer seriösa positioneringsprojekt.

De skiljer sig från enklare ULN2003-lösningar genom att de arbetar med strömbegränsning, microstepping och STEP/DIR-styrning. Mikrokontrollern skickar alltså stegimpulser och riktning, medan drivaren hanterar motorströmmar.

Var särskilt noga med:

- att ställa in strömbegränsning innan motorn belastas
- att ge drivaren tillräcklig kylning
- att inte koppla loss motorn medan drivaren är spänningssatt
- att använda acceleration i koden
- att skilja mellan logikmatning och motormatning
- att kontrollera motorström, inte bara motorspänning

En A4988- eller DRV8825-modul kan göra stegmotorstyrning mycket kraftfull, men den kräver mer respekt än en enkel LED-modul. Fel strömgräns eller dålig kylning är vanliga orsaker till tappade steg, överhettning och instabil rörelse.

### Acceleration spelar roll

En stegmotor kan inte alltid gå från stillastående till hög stegfrekvens direkt. Den behöver accelerera. Om du kräver för snabb start kan den surra, hoppa eller tappa steg.

Det betyder att robust stegmotorstyrning ofta behöver:

- låg starthastighet
- acceleration
- maxhastighet
- rimlig last
- rätt strömgräns
- stabil motormatning
- mekanisk friktion som är lägre än motorns moment

För experiment kan du börja enkelt, men så fort rörelsen blir mekaniskt viktig bör du använda ett bibliotek som stödjer acceleration eller skriva motsvarande logik själv.

## Jämförelse: när väljer du vad?

| Egenskap | Servo | DC-motor | Stegmotor |
|---|---|---|---|
| Primär styrning | Position | Hastighet/riktning | Steg/riktning |
| Behöver drivare? | Inbyggd i hobbyservo | Ja | Ja |
| Behöver separat matning? | Ofta | Ja | Ja |
| Exakt position utan extra sensor | Ungefär, inom servons område | Nej | Ofta relativt, men kan tappa steg |
| Kontinuerlig rotation | Inte standardservo | Ja | Ja, men stegvis |
| Enkel att börja med | Mycket | Med modul | Med rätt modul |
| Vanlig fallgrop | Ryck på grund av svag matning | För hög startström | Tappade steg eller fel strömgräns |
| Typiska projekt | Lucka, visare, pan-tilt | Hjul, fläkt, pump | Vridbord, linjär rörelse, positionering |

En praktisk valregel:

- Välj **servo** när du vill flytta något mellan vinklar.
- Välj **DC-motor** när något ska snurra och exakt position inte är huvudkravet.
- Välj **stegmotor** när du vill styra förflyttning i många små steg och kan hantera drivare, matning och acceleration.

Vanliga moduler ändrar inte motortypens grundegenskaper, men de påverkar hur lätt projektet blir att bygga. PCA9685 är praktisk när många servon ska styras. L298N är vanlig för DC-motorer men ofta mindre effektiv än modernare drivers. ULN2003 + 28BYJ-48 är en enkel kitkombination för långsam stegrörelse. A4988 och DRV8825 passar bättre för bipolära stegmotorer som behöver STEP/DIR och strömbegränsning.

Beslutsstöd för vanliga motorval:

- Välj **servo** när projektet behöver en tydlig mekanisk position och rörelsen ryms inom servons område.
- Välj **DC-motor med H-brygga** när riktning och hastighet är viktigare än exakt position.
- Välj **stegmotor** när rörelsen ska delas upp i kontrollerade steg och konstruktionen kan hantera strömgräns och acceleration.
- Välj **PCA9685** när många servosignaler ska styras, men dimensionera fortfarande servomatningen separat.

## Motorer och strömförsörjning

Motorer gör strömförsörjning viktigare än nästan allt annat i projektet. Problemen kommer ofta inte från koden utan från att spänningen sjunker, jord refererar fel eller störningar kommer tillbaka in i systemet.

Tänk på följande:

- Använd separat matning för motorer när lasten är mer än mycket liten.
- Koppla gemensam jord mellan motormatning, drivare och mikrokontroller.
- Dimensionera matning för startström, inte bara normal drift.
- Sätt avkoppling nära drivare och servo.
- Håll motorkablar och känsliga sensorsignaler separerade när det går.
- Lägg inte tung motorström genom breadboard om strömmen är hög.
- Kontrollera att drivaren klarar motorströmmen och kan kylas.
- Testa motor utan mekanisk last först och öka belastning stegvis.

En vanlig kopplingsprincip är:

```text
Arduino pin(s)  ---- styrsignaler ---- Motordrivare
Arduino GND     ---------------------- Motordrivare GND
Motormatning +  ---------------------- Motordrivare VMOT
Motormatning -  ---------------------- Motordrivare GND
Motor           ---------------------- Motordrivare motorutgångar
```

Notera att mikrokontrollern och motordrivaren delar GND, men att motorns effektström inte ska tas från en GPIO-pinne.

## Kodstruktur för rörelse

När motorer ingår i ett större projekt är det frestande att skriva kod som “gör rörelsen färdig” innan resten av programmet fortsätter. Det fungerar i ett isolerat test men blir snabbt problematiskt.

En bättre struktur är att behandla rörelse som ett tillstånd:

- Vad är målet?
- Vad är nuvarande riktning eller position?
- När uppdaterades rörelsen senast?
- Finns timeout?
- Finns fel eller stoppvillkor?
- Ska status visas med LED eller ljud?

Ett enkelt exempel för servo kan se ut så här:

```cpp
enum MotionState {
  MOTION_IDLE,
  MOTION_MOVING_TO_LOW,
  MOTION_MOVING_TO_HIGH
};

MotionState motionState = MOTION_IDLE;

int currentAngle = 90;
int lowAngle = 30;
int highAngle = 150;

unsigned long lastMotionUpdateMs = 0;
const unsigned long motionIntervalMs = 20;

void startMoveToLow() {
  motionState = MOTION_MOVING_TO_LOW;
}

void startMoveToHigh() {
  motionState = MOTION_MOVING_TO_HIGH;
}

void updateMotion() {
  unsigned long now = millis();

  if (now - lastMotionUpdateMs < motionIntervalMs) {
    return;
  }

  lastMotionUpdateMs = now;

  if (motionState == MOTION_MOVING_TO_LOW) {
    if (currentAngle > lowAngle) {
      currentAngle--;
      pointerServo.write(currentAngle);
    } else {
      motionState = MOTION_IDLE;
    }
  }

  if (motionState == MOTION_MOVING_TO_HIGH) {
    if (currentAngle < highAngle) {
      currentAngle++;
      pointerServo.write(currentAngle);
    } else {
      motionState = MOTION_IDLE;
    }
  }
}
```

Poängen är inte att detta är den enda rätta arkitekturen. Poängen är att rörelse får en egen uppdateringsfunktion. Då kan du kombinera den med sensorer, displayer, ljud och kommunikation utan att rörelsen låser allt annat.

## Referensmönster: servo som fysisk sensorindikator

Det här referensmönstret visar en fysisk indikator som visar ett mätvärde med en servo. Mönstret kombinerar analog läsning, filtrering, servo och icke-blockerande uppdatering utan att kräva kraftig motorlast.

### Vad mönstret visar

Mönstret använder en liten visare som rör sig mellan två vinklar beroende på ett analogt värde. I första versionen används en potentiometer som sensorersättning. Samma struktur kan senare användas för ljus, temperatur, avstånd eller annan mätning.

### Du behöver

- Arduino-kompatibelt kort
- liten hobbyservo
- potentiometer, exempelvis 10 kOhm
- extern 5 V-matning för servo om servon inte är mycket liten
- gemensam jord mellan Arduino och servomatning
- kopplingskablar
- gärna en enkel pappersvisare eller liten arm på servohornet

### Kopplingsprincip

Potentiometer:

```text
Potentiometer ena ytterben  -> 5 V eller 3,3 V enligt kortets logik
Potentiometer andra ytterben -> GND
Potentiometer mittben        -> analog ingång A0
```

Servo:

```text
Servo signal -> digital pin 9
Servo VCC    -> extern 5 V eller lämplig servomatning
Servo GND    -> gemensam GND
Arduino GND  -> gemensam GND
```

Kontrollera att den analoga ingången aldrig får högre spänning än kortet tillåter. På ett 3,3 V-kort ska potentiometern normalt kopplas mellan 3,3 V och GND, inte mellan 5 V och GND.

### Kod

```cpp
#include <Servo.h>

const int sensorPin = A0;
const int servoPin = 9;

const int minAngle = 20;
const int maxAngle = 160;

Servo indicatorServo;

float filteredValue = 0.0;
int currentAngle = 90;

unsigned long lastReadMs = 0;
unsigned long lastServoMs = 0;

const unsigned long readIntervalMs = 20;
const unsigned long servoIntervalMs = 20;

void setup() {
  Serial.begin(115200);

  indicatorServo.attach(servoPin);
  indicatorServo.write(currentAngle);

  int initialRaw = analogRead(sensorPin);
  filteredValue = initialRaw;
}

void loop() {
  updateSensor();
  updateServoPosition();
}

void updateSensor() {
  unsigned long now = millis();

  if (now - lastReadMs < readIntervalMs) {
    return;
  }

  lastReadMs = now;

  int raw = analogRead(sensorPin);

  const float alpha = 0.08;
  filteredValue = filteredValue + alpha * (raw - filteredValue);

  Serial.print("raw=");
  Serial.print(raw);
  Serial.print(" filtered=");
  Serial.println(filteredValue);
}

void updateServoPosition() {
  unsigned long now = millis();

  if (now - lastServoMs < servoIntervalMs) {
    return;
  }

  lastServoMs = now;

  int targetAngle = map((int)filteredValue, 0, 1023, minAngle, maxAngle);
  targetAngle = constrain(targetAngle, minAngle, maxAngle);

  if (currentAngle < targetAngle) {
    currentAngle++;
  } else if (currentAngle > targetAngle) {
    currentAngle--;
  }

  indicatorServo.write(currentAngle);
}
```

### Kontrollera detta

Vrid potentiometern långsamt och observera hur servon rör sig. Titta samtidigt på seriella monitorn.

Notera särskilt:

- Rör sig servon jämnt?
- Rycker den när den är nära ett läge?
- Blir rörelsen stabilare med filtrering?
- Orkar servon hålla visaren?
- Påverkas mikrokontrollern när servon rör sig snabbt?
- Startar kortet om när servon belastas?

### Förbättringar

Bygg vidare med en eller flera förbättringar:

- Lägg till LED-status: grön för låg nivå, gul för mellanläge, röd för hög nivå.
- Lägg till en buzzer som varnar när mätvärdet passerar ett tröskelvärde.
- Byt potentiometern mot en ljussensor.
- Lägg till dödzon så att servon inte rör sig för små mätvariationer.
- Gör vinkelskalan 0–100 procent i stället för rå ADC.
- Logga min- och maxvärde under en mätperiod.


## Riskkontroll före motorstart

Motorer bör kontrolleras innan de får driva mekanik, hjul, pumpar eller armar.

- Testa först utan mekanisk belastning.
- Använd separat matning när motor eller servo kan dra mer ström än kortet klarar.
- Kontrollera gemensam jord mellan styrkort, drivare och extern matning.
- Kontrollera att motorn inte kan starta okontrollerat vid reset eller uppladdning av kod.
- Börja med låg hastighet, kort körtid och enkel rörelse.
- Känn efter värme i motor, drivare och regulator efter ett kort test.
- Stoppa testet om kortet startar om, servot rycker eller drivaren blir varm.

Den här kontrollen ersätter inte datablad, men den fångar många fel innan de blir svåra att felsöka.

## Vanliga misstag

- **Misstag:** Att driva en motor direkt från en GPIO-pinne.
  - **Varför det händer:** En liten motor ser enkel ut och har bara två ledare.
  - **Hur man undviker det:** Använd servoelektronik, H-brygga, MOSFET, ESC eller annan drivkrets mellan mikrokontroller och motor.

- **Misstag:** Att mata servon från Arduino-kortets 5 V-pin utan att räkna på strömmen.
  - **Varför det händer:** Det fungerar ofta i ett obelastat test.
  - **Hur man undviker det:** Använd separat servomatning när servon belastas eller när flera servon används.

- **Misstag:** Att glömma gemensam jord.
  - **Varför det händer:** Man tänker på matning och signal som separata system.
  - **Hur man undviker det:** Koppla GND mellan mikrokontroller, drivare och extern matning så att styrsignaler får gemensam referens.

- **Misstag:** Att tolka PWM-värde som faktisk motorhastighet.
  - **Varför det händer:** `analogWrite()` ger ett tal mellan 0 och 255 som ser ut som en hastighetsprocent.
  - **Hur man undviker det:** Kom ihåg att PWM styr effekt ungefärligt. Använd encoder eller annan återkoppling om hastigheten måste vara känd.

- **Misstag:** Att behandla L298N som ett modernt effektivt standardval.
  - **Varför det händer:** Modulen är vanlig i kit och exempel, så den verkar vara förstahandsvalet.
  - **Hur man undviker det:** Använd den gärna för principtest, men välj modernare MOSFET-baserad driver när verkningsgrad, batteritid eller högre motorström är viktigt.

- **Misstag:** Att använda A4988 eller DRV8825 utan att ställa in strömbegränsning.
  - **Varför det händer:** STEP/DIR-koden kan se korrekt ut även när drivaren är elektriskt fel inställd.
  - **Hur man undviker det:** Ställ in strömgräns enligt motor och driver, kontrollera kylning och börja med låg hastighet.

- **Misstag:** Att använda en stegmotor utan acceleration.
  - **Varför det händer:** Enkel testkod med snabba pulser kan se korrekt ut.
  - **Hur man undviker det:** Börja med låg stegfrekvens, öka stegvis och använd acceleration när lasten blir verklig.

- **Misstag:** Att låta motorn slå i mekaniskt stopp.
  - **Varför det händer:** Koden antar att rörelseområdet är säkert.
  - **Hur man undviker det:** Begränsa vinklar, använd ändlägesbrytare eller mekanisk design som tål fel.

- **Misstag:** Att felsöka motorproblem som kodproblem.
  - **Varför det händer:** Symptomen ser slumpmässiga ut: reset, brusiga mätvärden eller förlorad kommunikation.
  - **Hur man undviker det:** Mät matning, testa utan last, separera motorström och kontrollera avkoppling innan du skriver om koden.

## Kontrollpunkter för rörelsekod och motorstart

Använd punkterna när servo, DC-motor eller stegmotor beter sig opålitligt.

- Servokod bör inte blockera huvudloopen om projektet samtidigt ska läsa sensorer, blinka status-LED eller kommunicera.
- Om en servo rycker: kontrollera separat servomatning, gemensam jord och mekanisk last.
- Vid DC-motor: börja med låg PWM, tydlig stoppfunktion och extern drivare som klarar startströmmen.
- Om mikrokontrollerkortet startar om när motorn startar är matningen troligen för svag eller för dåligt avkopplad.
- Vid stegmotor: börja långsamt och lägg till acceleration innan du höjer hastigheten.
- Om en stegmotor tappar steg: sänk hastighet, kontrollera strömgräns, matning, last och acceleration.
## Snabb sammanfattning

- Vanliga moduler hjälper dig komma igång, men de ersätter inte kontroll av ström, värme, jord och mekanisk belastning.
- Servo passar bäst när du vill styra en begränsad vinkel eller fysisk position.
- Kontinuerlig servo passar enklare rotation men ger normalt inte positionskontroll.
- DC-motor passar kontinuerlig rotation, men behöver drivare och ofta återkoppling för exakt hastighet.
- Stegmotor passar diskret och repeterbar rörelse, men kan tappa steg om lasten, hastigheten eller accelerationen är fel.
- Motorer ska normalt inte drivas direkt från en mikrokontrollerpinne.
- Separat matning och gemensam jord är centrala principer i motorprojekt.
- `analogWrite()` styr PWM-duty cycle, inte garanterad motorhastighet.
- Rörelsekod bör skrivas icke-blockerande så att sensorer, LED, ljud och kommunikation kan fortsätta fungera.
- Felsök motorprojekt elektriskt först: matning, jord, drivare, last och störningar.

## Säkerhetsruta: motorer är inte logiska laster

Motorer är induktiva och kan dra höga startströmmar. De ska nästan aldrig drivas direkt från en mikrokontrollerpinne. Använd lämplig drivkrets, separat matning och kontrollera att jord är gemensam där styrsignaler delas.

Var också beredd på störningar. En motor som fungerar ensam kan få sensorer, displayer eller kommunikation att bete sig märkligt när den startar. Avkoppling, korta ledningar och separerad matning är ofta lika viktiga som rätt kod.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Separat lastmatning, styrlogik ofta 3,3 V eller 5 V |
| Typiskt gränssnitt | PWM, servoimpuls, H-brygga, driver eller styrsignal |
| Välj när | rörelse, position eller mekanisk kraft behövs |
| Välj inte när | du bara behöver visuell återkoppling |
| Vanliga fel | direktdriven motor, för svag matning, störningar, saknad gemensam jord |
| Många servon | PCA9685 kan samla många servosignaler, men kräver fortfarande ordentlig servomatning |
| Klassisk kit-stegmotor | 28BYJ-48 + ULN2003 passar enkla långsamma rörelser |
| Bipolär stegmotor | A4988 eller DRV8825 passar när STEP/DIR, strömbegränsning och microstepping behövs |
| Vanlig DC-motormodul | L298N fungerar för principtest men är ofta ineffektiv jämfört med moderna MOSFET-drivers |
| Alternativ att överväga | servo, DC-motor, stegmotor, solenoid |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När problemet handlar om styrsignal, timing eller PWM, jämför med kapitel 7.
- När motorn kräver mer ström än kortet kan ge, gå vidare till kapitel 21 och 31 innan du testar igen.
- När servo eller motor rycker, stannar eller startar om kortet, börja med strömförsörjningen i kapitel 34.
- När felet bara uppstår i ett större bygge, använd felsökningsordningen i kapitel 35.
