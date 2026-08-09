# 25. Avstånd, närvaro och objektupptäckt

## Sensoröversikt
Många Arduino-projekt behöver veta om något finns i närheten, hur långt bort något är, om en person rör sig i rummet eller om ett objekt passerar en viss punkt. Det kan handla om en robot som inte ska köra in i väggen, en parkeringsindikator, en automatisk belysning, en nivåmätare, en räknare på ett transportband eller en installation som reagerar när någon närmar sig.

Det är frestande att tänka att alla sådana problem löses med “en avståndssensor”. I praktiken är avstånd, närvaro och objektupptäckt tre olika typer av frågor:

- **Avstånd:** Hur långt bort är objektet?
- **Närvaro:** Finns någon eller något i området?
- **Passage eller objektupptäckt:** Har något brutit en stråle, passerat en punkt eller kommit nära en yta?

Olika sensorer är bra på olika frågor. En ultraljudssensor kan ge ett ungefärligt avstånd men störas av mjuka material, vinklar och små objekt. En PIR-sensor är bra på mänsklig rörelse men säger inte hur långt bort personen är. En Time-of-Flight-sensor kan vara kompakt och snabb på korta avstånd, men påverkas av ytor, synfält och omgivningsljus. En IR-reflektionssensor är utmärkt nära en yta men fungerar dåligt som allmän rumssensor.

Det här kapitlet hjälper dig att välja mellan vanliga tekniker:

- ultraljud
- IR-avstånd och IR-reflektion
- Time-of-Flight och laserbaserad avståndsmätning
- PIR-rörelsesensorer
- radar och mmWave-moduler
- reed switch, hallgivare och mekaniska brytare
- ljusbarriärer och enklare optiska passagedetektorer

Kapitlet fungerar som praktiskt stöd när du behöver skilja mellan avståndsmätning, närvarodetektion och objektupptäckt, välja sensor utifrån miljö, synfält och objektmaterial, och felsöka falska positiva, falska negativa och instabila mätvärden. Målet är att du ska kunna välja sensor efter problemets karaktär, inte efter vilken modul som råkar ligga i lådan.

## Förutsättningar

Det här kapitlet bygger på tidigare kapitel om digital I/O, analog läsning, tidsstyrning och kommunikationsbussar. Flera av sensorerna i kapitlet använder enkla digitala signaler, men andra använder analog spänning, I2C, UART eller mer avancerade bibliotek.

Du behöver inte kunna signalbehandling på djupet, men du bör ha med dig tre principer:

- En sensor mäter bara det den fysiskt kan se, höra eller känna av.
- Ett mätvärde behöver ofta filtreras innan det används som beslut.
- En närvarosignal blir robustare om den har tidslogik och hysteresis.

I praktiska projekt är det ofta bättre att göra en enkel sensor stabil än att välja en avancerad sensor och använda den naivt.

## Först: vad är frågan?

Innan du väljer sensor bör du formulera vad projektet faktiskt behöver veta.

| Fråga | Exempel | Typiska sensorer |
|---|---|---|
| Hur långt bort är objektet? | Robot, nivåmätning, parkeringshjälp | Ultraljud, ToF, IR-avstånd |
| Finns en person i området? | Automatisk belysning, rumssensor | PIR, radar/mmWave |
| Har något passerat en punkt? | Räknare, optisk grind, dörrsensor | Ljusbarriär, brytare, hallgivare |
| Är något mycket nära? | Linjeföljare, endstop, närhetsbrytare | IR-reflektion, mikrobrytare, reed switch |
| Är en dörr/lucka öppen? | Kapsling, fönster, säkerhetsläge | Reed switch, mikrobrytare, hallgivare |
| Finns ett objekt i en zon? | Pappersdetektion, behållare, robot | IR-reflektion, ToF, ultraljud |

Det är stor skillnad mellan “detektera att någon rör sig i ett rum” och “mäta 23 cm till en kartong”. PIR är ofta bra för det första men dålig för det andra. Ultraljud kan vara användbart för det andra men säger inte säkert att objektet är en människa.

## Viktiga valkriterier

Avstånds- och närvarosensorer påverkas mycket av miljön. Använd därför en enkel valmodell.

| Kriterium | Fråga att ställa |
|---|---|
| Mätområde | Är objektet 5 cm, 50 cm, 5 m eller längre bort? |
| Objektets material | Är ytan hård, mjuk, mörk, blank, genomskinlig eller vinklad? |
| Synfält | Ska sensorn se en punkt, en kon eller ett större område? |
| Respons | Behöver du millisekunder, sekunder eller bara långsam status? |
| Miljö | Finns solljus, damm, vatten, vind, ljud, vibration eller människor? |
| Gränssnitt | Digital pinne, analog spänning, I2C, UART eller specialbibliotek? |
| Strömförbrukning | Ska sensorn vara aktiv hela tiden eller väcka systemet ibland? |
| Falska utslag | Vad är värst: missa ett objekt eller reagera på fel objekt? |

När du väljer sensor bör du också bestämma vad systemet ska göra vid osäkerhet. En robot kan sakta ned om mätningen är instabil. En larmsensor kanske ska kräva flera bekräftade observationer innan den reagerar. En räknare kanske ska ignorera nya passager under en kort spärrtid.

## Ultraljud: enkel avståndsmätning med ekon

Ultraljudssensorer, till exempel HC-SR04-liknande moduler, skickar ut en ljudpuls och mäter tiden tills ekot kommer tillbaka. Eftersom ljudet färdas till objektet och tillbaka kan avståndet beräknas från tiden.

De är populära eftersom de är billiga, lätta att förstå och fungerar med enkla digitala pinnar. De är också pedagogiska: de visar tydligt hur tidsmätning kan bli ett fysiskt mätvärde.

Ultraljud passar bra när:

- objektet är relativt stort
- ytan reflekterar ljud
- mätningen sker på kort till medellångt avstånd
- precision på centimeter-nivå räcker
- sensorn kan riktas ungefär mot objektet

Ultraljud passar sämre när:

- objektet är mjukt, vinklat eller mycket litet
- miljön är trång med många reflektioner
- sensorn sitter nära bullriga eller vibrerande delar
- mycket snabba mätningar krävs
- sensorn måste vara mycket liten
- projektet ska fungera robust utomhus i varierande miljö

En viktig praktisk detalj är spänning. Många klassiska HC-SR04-moduler drivs med 5 V och ger 5 V på echo-signalen. Det är okej för många klassiska Arduino-kort, men inte för 3,3 V-kort som ESP8266, ESP32 och Raspberry Pi Pico utan nivåanpassning. Kontrollera alltid modulens specifikation och kortets tolerans.

## Exempel: mäta avstånd med ultraljud

Det här mönstret använder en ultraljudsmodul med trigger- och echo-pinne. Poängen är inte att bygga den perfekta ultraljudsdrivrutinen, utan att skapa ett tydligt och felsökningsbart mätmönster.

### Det här används i exemplet

- Arduino-kompatibelt kort
- ultraljudsmodul med trigger och echo
- kopplingskablar
- eventuell nivådelare eller nivåskiftare för echo om kortet är 3,3 V
- ett plant objekt att mäta mot

### Koppling

För ett 5 V-tolerant Arduino-kort kan en typisk koppling vara:

| Modul | Arduino |
|---|---|
| VCC | 5 V |
| GND | GND |
| TRIG | Digital pinne 8 |
| ECHO | Digital pinne 7 |

För ett 3,3 V-kort bör du inte anta att echo-pinnen är säker. Använd nivåanpassning om modulen ger 5 V på echo.

### Kod

```cpp
const int trigPin = 8;
const int echoPin = 7;

const unsigned long timeoutMicros = 30000UL;

float readDistanceCm() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(3);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  unsigned long duration = pulseIn(echoPin, HIGH, timeoutMicros);

  if (duration == 0) {
    return -1.0;
  }

  return duration / 58.0;
}

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  digitalWrite(trigPin, LOW);

  Serial.begin(115200);
  while (!Serial) {
    ;
  }

  Serial.println("Ultrasonic distance test");
}

void loop() {
  float distanceCm = readDistanceCm();

  if (distanceCm < 0) {
    Serial.println("No echo");
  } else {
    Serial.print("Distance: ");
    Serial.print(distanceCm, 1);
    Serial.println(" cm");
  }

  delay(200);
}
```

### Förväntat resultat

När du flyttar ett plant objekt framför sensorn ska avståndet förändras. Värdena bör vara relativt stabila om objektet är tillräckligt stort, står vinkelrätt mot sensorn och befinner sig inom modulens användbara område.

Om du får `No echo` ofta betyder det inte nödvändigtvis att sensorn är trasig. Det kan bero på fel koppling, fel pinne, för långt avstånd, för svagt eko, vinklad yta eller för kort tid mellan mätningar.

## Undvik att låsa programmet med pulseIn

Funktionen `pulseIn()` är enkel men blockerande. Det betyder att programmet väntar tills pulsen kommer eller tills timeout löper ut. I ett litet test är det acceptabelt. I ett större projekt kan det göra att knappar, displayer, motorstyrning och kommunikation känns tröga.

Det finns tre vanliga strategier:

- sätt alltid en rimlig timeout
- mät inte oftare än sensorn klarar av
- använd ett bibliotek eller egen tillståndsmaskin om resten av programmet måste vara responsivt

För en robot med motorer och flera sensorer bör du vara försiktig med lång blockerande väntan. För en enkel nivåmätare som uppdaterar två gånger per sekund kan `pulseIn()` med timeout vara tillräckligt.

## Enkel filtrering av avstånd

Avståndsmätningar hoppar ofta. Börja inte med avancerad filtrering. Börja med tydlig statuslogik.

Ett enkelt sätt är att ta flera mätningar och använda medianliknande eller medelvärdesbaserad logik. Ett ännu enklare sätt är att bara acceptera rimliga värden.

```cpp
bool isValidDistance(float distanceCm) {
  return distanceCm >= 2.0 && distanceCm <= 250.0;
}

float readFilteredDistanceCm() {
  const int sampleCount = 5;
  float sum = 0.0;
  int validCount = 0;

  for (int i = 0; i < sampleCount; i++) {
    float value = readDistanceCm();

    if (isValidDistance(value)) {
      sum += value;
      validCount++;
    }

    delay(30);
  }

  if (validCount == 0) {
    return -1.0;
  }

  return sum / validCount;
}
```

Detta är fortfarande blockerande eftersom det tar flera mätningar i följd. För snabba tester är det tydligt. I mer responsiva projekt bör du sprida mätningarna över tid med `millis()`.

## IR-avstånd och IR-reflektion

IR-sensorer använder infrarött ljus. Det finns flera typer, och de ska inte blandas ihop.

En **IR-reflektionssensor** skickar ut IR-ljus och mäter hur mycket som reflekteras tillbaka. Den är vanlig i linjeföljare, hinderindikatorer, enkla närhetssensorer och optiska räknare.

En **IR-avståndssensor** är mer specialiserad och kan ge analog eller digital uppskattning av avstånd inom ett visst område.

IR-reflektion passar bra när:

- objektet är nära
- du vill upptäcka svart/vitt, kant, linje eller närhet
- sensorn kan sitta nära ytan
- låg kostnad och enkel koppling är viktig

IR-reflektion passar sämre när:

- objektets färg och material varierar mycket
- omgivningsljus är starkt eller okontrollerat
- du behöver exakt avstånd
- ytan är blank, genomskinlig eller mycket mörk

Många billiga IR-moduler har en potentiometer och en digital utgång. Det är praktiskt, men kom ihåg att potentiometern bara ställer en tröskel. Den gör inte sensorn noggrann.

## ToF: Time-of-Flight på korta avstånd

Time-of-Flight-sensorer mäter avstånd genom att analysera ljusets flygtid eller fasrelaterade egenskaper. I Arduino-projekt används ofta små I2C-moduler i VL53-serien eller liknande.

ToF-sensorer passar bra när:

- sensorn ska vara kompakt
- du vill ha digital mätning via I2C
- objektet är på kort till medellångt avstånd
- ultraljud är för stort, för långsamt eller störs av geometri
- du vill mäta i en smalare riktning än ultraljud ofta ger

ToF passar sämre när:

- objektet är mycket mörkt, blankt eller genomskinligt
- starkt omgivningsljus stör
- mätavståndet är utanför sensorns praktiska område
- flera sensorer med samma I2C-adress ska användas utan planering
- projektet kräver absolut precision utan kalibrering

Många ToF-sensorer har också ett synfält. Det betyder att mätvärdet inte nödvändigtvis kommer från en perfekt punkt. Om flera objekt finns i synfältet kan sensorn rapportera ett värde som beror på modulens interna algoritm.

## PIR: rörelse från värmestrålning

PIR står för passive infrared. En PIR-sensor mäter inte avstånd och ser inte vanliga objekt på samma sätt som en kamera. Den reagerar på förändringar i infraröd värmestrålning, ofta från människor eller djur som rör sig genom sensorns zoner.

PIR passar bra när:

- du vill veta om en människa rör sig i ett område
- snabb exakt avståndsmätning inte behövs
- projektet får reagera med viss fördröjning
- strömförbrukningen ska vara låg
- du bygger belysning, närvarologik eller enkel automation

PIR passar sämre när:

- personen sitter stilla
- du behöver veta avstånd
- du behöver detektera små föremål
- sensorn tittar mot värmekällor, fönster eller solbelysta ytor
- du vill räkna personer exakt

PIR-moduler har ofta justering för känslighet och hålltid. Hålltid betyder att utgången fortsätter vara aktiv en stund efter rörelsen. Det är praktiskt för belysning men kan vara förvirrande i experiment om du tror att utgången ska följa rörelsen direkt.

## Exempel: stabil PIR-närvaro

En PIR-modul har ofta en digital utgång. Den kan läsas som en vanlig digital ingång. Men för att få en användbar närvarosignal är det klokt att hålla status aktiv en stund efter senaste rörelse.

```cpp
const int pirPin = 6;
const unsigned long presenceHoldMs = 30000UL;

bool presence = false;
unsigned long lastMotionMs = 0;

void setup() {
  pinMode(pirPin, INPUT);

  Serial.begin(115200);
  while (!Serial) {
    ;
  }

  Serial.println("PIR presence test");
}

void loop() {
  unsigned long now = millis();
  bool motion = digitalRead(pirPin) == HIGH;

  if (motion) {
    lastMotionMs = now;
  }

  presence = (now - lastMotionMs) < presenceHoldMs;

  Serial.print("motion=");
  Serial.print(motion ? "yes" : "no");
  Serial.print(" presence=");
  Serial.println(presence ? "yes" : "no");

  delay(500);
}
```

Skillnaden mellan `motion` och `presence` är viktig. `motion` är vad sensorn säger just nu. `presence` är systemets tolkning: “vi betraktar området som upptaget eftersom rörelse nyligen har upptäckts”.

## Radar och mmWave-moduler

Radar- och mmWave-moduler har blivit vanliga i hobby- och IoT-projekt. De kan i vissa fall upptäcka närvaro även när en person sitter relativt stilla, vilket en klassisk PIR ofta missar. Vissa moduler kan också ge grov avstånds- eller zoninformation.

Radar/mmWave passar bra när:

- stillasittande närvaro är viktig
- PIR ger för många missar
- sensorn får sitta dold bakom vissa material
- projektet kan hantera mer konfiguration
- strömförbrukning och pris är acceptabla

Radar/mmWave passar sämre när:

- du behöver enkel digital logik utan inställningar
- miljön har mycket rörelse som fläktar, gardiner eller vibrationer
- exakt objektidentifiering krävs
- du behöver mycket låg strömförbrukning
- du vill förstå varje mätning lika enkelt som med en knapp eller PIR

Många mmWave-moduler kommunicerar via UART och kräver konfiguration. Det gör dem kraftfulla men också mer projektberoende. För en första prototyp är det ofta klokt att testa modulen med leverantörens exempel och logga rå status innan du bygger in den i ett större system.

## Reed switch, hallgivare och mekaniska brytare

Ibland är den bästa närvarosensorn inte optisk, akustisk eller radarbaserad. Om du vill veta om en dörr är öppen, om en lucka är stängd eller om en magnet passerar en punkt kan en enkel brytare vara robustare än en avancerad sensor.

En **reed switch** är en magnetpåverkad brytare. Den används ofta för dörrar och fönster. En **hallgivare** mäter magnetfält elektroniskt och kan vara mer hållbar eller snabbare i vissa tillämpningar. En **mikrobrytare** är mekanisk och ger en tydlig kontakt när något trycker på den.

Dessa lösningar passar bra när:

- objektet kan förses med magnet eller fysisk aktivering
- du vill ha tydlig ja/nej-status
- miljön är svår för optik eller ultraljud
- robusthet är viktigare än kontaktlös mätning
- du behöver en endstop eller referensposition

De passar sämre när:

- sensorn inte får röra objektet
- objektet varierar i position
- det är svårt att montera magnet eller mekanik
- du behöver avstånd snarare än status

I många praktiska system är en brytare det mest professionella valet eftersom den minskar osäkerheten. En 3D-skrivare, CNC-maskin eller kapsling behöver ofta veta att en viss position är nådd, inte uppskatta ungefärligt avstånd dit.

## Analoga Hall-sensorer och 49E-typ

En reedkontakt och en digital Hall-sensor används ofta som magnetisk av/på-detektering: finns magneten tillräckligt nära eller inte? En **analog Hall-sensor**, till exempel 49E- eller OH49E-typ, fungerar annorlunda. Den ger en varierande spänning som ändras med magnetfältet i stället för en ren digital status.

Det gör analoga Hall-sensorer användbara när du vill se en ungefärlig förändring snarare än bara ett läge. De kan till exempel användas för enkel positionsindikering, när en magnet närmar sig en punkt, när en axel roterar förbi en sensor eller när du vill jämföra hur starkt ett magnetfält är på olika avstånd.

Skillnaden är viktig:

- **Reedkontakt:** mekanisk magnetpåverkad brytare med tydlig av/på-status.
- **Digital Hall-sensor:** elektronisk magnetdetektering med digital utgång.
- **Analog Hall-sensor:** magnetdetektering med analog spänning som behöver läsas med analog ingång.

En analog Hall-sensor är alltså mer flexibel, men också mindre direkt. Du behöver ofta kalibrera vad som räknas som nära, långt bort eller mittläge i just din mekanik. Små förändringar i magnetens vinkel, avstånd och placering kan påverka värdet mycket.

Ett praktiskt arbetssätt är att först skriva ut råvärden från `analogRead()` medan du flyttar magneten genom hela den tänkta rörelsen. Därefter väljer du gränser eller tolkar intervallet. Undvik att börja med fasta antaganden från ett exempel på nätet, eftersom magnet, sensorvariant, matningsspänning och montering påverkar resultatet.

Analoga Hall-sensorer passar bra när:

- du vill se ungefärlig magnetposition eller rörelse
- du kan montera magnet och sensor stabilt
- du kan kalibrera värdena i det färdiga projektet
- du behöver mer information än bara av/på

De passar sämre när:

- du bara behöver veta om en lucka är stängd
- mekaniken är glapp eller magnetens bana varierar
- du inte vill kalibrera
- du behöver exakt positionsmätning utan separat referenssystem

Om målet bara är en robust magnetisk kontakt är reedkontakt eller digital Hall-sensor ofta enklare. Om målet är att följa en förändring över tid kan en analog Hall-sensor vara ett bättre verktyg.

## Ljusbarriär och passagedetektion

En ljusbarriär består av en sändare och en mottagare. När något bryter strålen ändras signalen. Det kan göras med synligt ljus, IR-LED, fototransistor, färdig optisk gaffel eller industriell fotocell.

Ljusbarriärer passar bra när:

- objekt passerar en bestämd punkt
- du vill räkna objekt
- du kan placera sändare och mottagare mittemot varandra
- du vill ha snabb och tydlig detektion

De passar sämre när:

- objektens bana varierar mycket
- miljön är dammig eller smutsig
- solljus kan träffa mottagaren
- installationen inte tillåter justering

I hobbyprojekt kan en enkel IR-sändare och mottagare fungera. I mer robusta system är färdiga optiska givare ofta enklare att använda eftersom de har bättre mekanik, filtrering och signalutgång.

## Hysteresis och tidslogik

När en sensor används för beslut behöver du ofta hysteresis. Hysteresis betyder att systemet inte byter status fram och tillbaka vid samma gräns.

Anta att du vill tända en varnings-LED när ett objekt är närmare än 20 cm. Om mätvärdet hoppar mellan 19,8 och 20,2 cm kommer LED:en blinka. Med hysteresis kan du slå på vid 20 cm men inte slå av förrän objektet är längre bort än 25 cm.

```cpp
const float nearLimitCm = 20.0;
const float farLimitCm = 25.0;

bool objectIsNear = false;

void updateNearState(float distanceCm) {
  if (distanceCm < 0) {
    return;
  }

  if (!objectIsNear && distanceCm <= nearLimitCm) {
    objectIsNear = true;
  }

  if (objectIsNear && distanceCm >= farLimitCm) {
    objectIsNear = false;
  }
}
```

Hysteresis kan också vara tidsbaserad. Du kan kräva att ett objekt ska vara nära i minst 300 ms innan systemet reagerar, eller att sensorn ska vara fri i 2 sekunder innan status återställs.

## Jämförelsemönster: två närvarotekniker

Det här jämförelsemönstret visar skillnaden mellan att mäta avstånd och att tolka närvaro. Välj gärna ultraljud plus PIR, eller ToF plus PIR om du har en ToF-modul.

### Vad mönstret visar

Mönstret skapar en liten beslutslogik som ger statusarna:

- `CLEAR`
- `OBJECT_NEAR`
- `MOTION_DETECTED`
- `PRESENCE_HOLD`

### Det här används i exemplet

- Arduino-kompatibelt kort
- ultraljuds- eller ToF-sensor
- PIR-sensor
- LED eller seriell monitor för status
- eventuell nivåskiftning för 3,3 V-kort
- kopplingskablar

### Koppling

Använd en koppling som passar dina moduler. Kontrollera särskilt:

- kortmodell
- matningsspänning
- vilka pinnar som används
- om nivåskiftning behövs
- ungefärligt mätområde
- hur sensorerna är riktade

För ultraljudsexemplet kan du återanvända trigger och echo från tidigare kod. PIR-sensorn kopplas till en digital ingång.

### Kod

```cpp
const int trigPin = 8;
const int echoPin = 7;
const int pirPin = 6;
const int statusLedPin = 13;

const unsigned long distanceIntervalMs = 200;
const unsigned long presenceHoldMs = 15000;

const float nearLimitCm = 25.0;
const float farLimitCm = 35.0;

unsigned long lastDistanceReadMs = 0;
unsigned long lastMotionMs = 0;

float latestDistanceCm = -1.0;
bool objectIsNear = false;

float readDistanceCm() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(3);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  unsigned long duration = pulseIn(echoPin, HIGH, 30000UL);

  if (duration == 0) {
    return -1.0;
  }

  return duration / 58.0;
}

void updateNearState(float distanceCm) {
  if (distanceCm < 0) {
    return;
  }

  if (!objectIsNear && distanceCm <= nearLimitCm) {
    objectIsNear = true;
  }

  if (objectIsNear && distanceCm >= farLimitCm) {
    objectIsNear = false;
  }
}

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(pirPin, INPUT);
  pinMode(statusLedPin, OUTPUT);

  digitalWrite(trigPin, LOW);

  Serial.begin(115200);
  while (!Serial) {
    ;
  }

  Serial.println("Distance and presence comparison");
}

void loop() {
  unsigned long now = millis();

  if (now - lastDistanceReadMs >= distanceIntervalMs) {
    lastDistanceReadMs = now;
    latestDistanceCm = readDistanceCm();
    updateNearState(latestDistanceCm);
  }

  bool motionDetected = digitalRead(pirPin) == HIGH;

  if (motionDetected) {
    lastMotionMs = now;
  }

  bool presenceHold = (now - lastMotionMs) < presenceHoldMs;

  digitalWrite(statusLedPin, objectIsNear || presenceHold ? HIGH : LOW);

  Serial.print("distance_cm=");
  Serial.print(latestDistanceCm, 1);
  Serial.print(" object_near=");
  Serial.print(objectIsNear ? "yes" : "no");
  Serial.print(" motion=");
  Serial.print(motionDetected ? "yes" : "no");
  Serial.print(" presence_hold=");
  Serial.println(presenceHold ? "yes" : "no");

  delay(100);
}
```

### Förväntat resultat

När du placerar ett objekt nära avståndssensorn ska `object_near` bli `yes`. När objektet flyttas bort ska statusen inte slå av direkt vid samma gräns, utan först när avståndet passerar den högre gränsen.

När du rör dig framför PIR-sensorn ska `motion` bli `yes` när modulen reagerar. `presence_hold` ska ligga kvar en stund efter rörelsen.

Det viktiga är att du ser skillnaden mellan en direkt sensorobservation och en systemstatus. Sensorn ger data. Programmet tolkar data.

## Variation: byt ultraljud mot ToF

Om du har en ToF-modul på I2C kan du behålla samma beslutslogik men byta ut funktionen som läser avstånd. Då blir mönstret ett bra exempel på abstraktion: resten av programmet behöver inte veta exakt vilken sensor som används, så länge den får ett avstånd i centimeter eller millimeter.

Skapa gärna en funktion med samma idé:

```cpp
float readDistanceCm() {
  // Läs din ToF-sensor här och returnera centimeter.
  // Returnera -1.0 om mätningen misslyckas.
  return -1.0;
}
```

Detta är ett bra sätt att undvika att hela projektet blir låst till en viss sensormodul.

## Variation: passageräknare med ljusbarriär

Om du har en optisk brytare eller ljusbarriär kan du bygga en enkel passageräknare. Nyckeln är att räkna övergången från fri stråle till bruten stråle, inte att räkna varje loopvarv där strålen är bruten.

```cpp
const int beamPin = 5;

bool previousBlocked = false;
unsigned long count = 0;

void setup() {
  pinMode(beamPin, INPUT_PULLUP);

  Serial.begin(115200);
  while (!Serial) {
    ;
  }
}

void loop() {
  bool blocked = digitalRead(beamPin) == LOW;

  if (blocked && !previousBlocked) {
    count++;

    Serial.print("Passage count: ");
    Serial.println(count);
  }

  previousBlocked = blocked;
}
```

Beroende på modul kan logiken vara inverterad. Testa alltid med seriell monitor innan du bygger vidare.

## Variation: dörrsensor med reed switch

En reed switch kan kopplas som en vanlig knapp med intern pullup. Med en magnet på dörren och reed switch på karmen får du en tydlig öppen/stängd-signal.

```cpp
const int reedPin = 4;

void setup() {
  pinMode(reedPin, INPUT_PULLUP);

  Serial.begin(115200);
  while (!Serial) {
    ;
  }
}

void loop() {
  bool switchClosed = digitalRead(reedPin) == LOW;

  Serial.println(switchClosed ? "Closed" : "Open");

  delay(250);
}
```

Det här är ofta mer robust än att försöka avgöra dörrstatus med avståndssensor.

## Felsökning

Börja alltid med ett minimalt testprogram för en sensor i taget. När avstånds- eller närvarosensorer beter sig konstigt är problemet ofta fysiskt, inte programmeringsmässigt.

| Symptom | Trolig orsak | Test |
|---|---|---|
| Ultraljud ger alltid timeout | Fel echo/trig, ingen gemensam jord, för långt avstånd | Testa nära plant objekt och kontrollera pinout |
| Ultraljud hoppar mycket | Vinklad yta, mjukt objekt, reflektioner | Testa mot plan bok eller vägg |
| 3,3 V-kort beter sig instabilt | Echo-signal eller modulutgång är 5 V | Kontrollera nivåskiftning |
| PIR reagerar inte direkt | Uppvärmningstid eller hålltid | Vänta, läs modulens beteende och logga utgången |
| PIR reagerar på fel saker | Värmekälla, sol, luftdrag, placering | Rikta om sensorn och testa miljön |
| IR-reflektion fungerar bara ibland | Objektets färg/material varierar | Testa flera ytor och justera tröskel |
| ToF ger konstiga värden | Synfält, blank yta, omgivningsljus | Testa matt objekt och kortare avstånd |
| Ljusbarriär dubbelräknar | Ingen flankdetektering eller studs | Räkna övergångar och lägg till spärrtid |
| mmWave reagerar för mycket | För känslig zon eller rörliga objekt i miljön | Minska känslighet och logga rå status |

## Vanliga misstag

- **Misstag:** Att välja PIR för att mäta avstånd.
  - **Varför det händer:** PIR-moduler marknadsförs ofta som rörelsesensorer och kan uppfattas som allmänna närvarosensorer.
  - **Hur man undviker det:** Använd PIR för rörelse/närvaro, inte avstånd. Välj ultraljud, ToF eller IR-avstånd om du behöver distans.

- **Misstag:** Att använda ultraljud mot fel typ av objekt.
  - **Varför det händer:** Sensorn känns enkel och ger centimeter direkt i många exempel.
  - **Hur man undviker det:** Testa objektets form, vinkel och material. Planera för timeout och ogiltiga värden.

- **Misstag:** Att glömma nivåskiftning på 3,3 V-kort.
  - **Varför det händer:** Modulen har fyra enkla pinnar och ser kompatibel ut.
  - **Hur man undviker det:** Kontrollera signalnivå på varje utgång, särskilt echo från 5 V-ultraljudsmoduler.

- **Misstag:** Att fatta beslut på ett enstaka mätvärde.
  - **Varför det händer:** Exempelkod visar ofta `if (distance < limit)` direkt.
  - **Hur man undviker det:** Använd hysteresis, tidsfilter och ogiltighetskontroll.

- **Misstag:** Att tro att “närvaro” är ett råvärde.
  - **Varför det händer:** Det är lätt att koppla sensorutgång direkt till systemstatus.
  - **Hur man undviker det:** Skilj mellan sensorobservation, tolkad status och beslut.

## Valguide

| Behov | Rekommenderad startpunkt | Kommentar |
|---|---|---|
| Enkel avståndsmätning till vägg eller stort objekt | Ultraljud | Billigt och pedagogiskt, men känsligt för geometri |
| Kompakt kortdistansmätning | ToF | Bra med I2C, men testa ytor och synfält |
| Linjeföljning eller nära reflektion | IR-reflektion | Enkel och billig, men ytkänslig |
| Mänsklig rörelse i rum | PIR | Bra för rörelse, inte stillasittande närvaro |
| Stillasittande mänsklig närvaro | Radar/mmWave | Kraftfullt men mer konfigurationskrävande |
| Dörr, lucka eller ändläge | Reed switch, hallgivare eller mikrobrytare | Ofta robustare än avståndsmätning |
| Passageräkning i bestämd punkt | Ljusbarriär eller optisk gaffel | Räkna övergångar, inte loopvarv |
| Enkel hinderdetektion på robot | Ultraljud eller ToF | Välj efter avstånd, formfaktor och miljö |
| Närhet till mörk eller blank yta | Testa flera tekniker | Optik kan vara opålitlig utan mekanisk kontroll |

Snabbt närvaroval:

- Välj **ultraljud** när objektet är relativt stort och avståndet är viktigare än kompakt formfaktor.
- Välj **ToF** när kort avstånd, liten modul och I2C passar bra.
- Välj **PIR** när du vill upptäcka rörelse från människor, inte exakt avstånd.
- Välj **reed switch eller Hall-sensor** när du kan montera magnet och vill ha robust lägesdetektering.
- Välj **ljusbarriär** när passagen sker på en bestämd plats.

## Snabb överblick

- Avstånd, närvaro och objektupptäckt är olika problem.
- Ultraljud är billigt och pedagogiskt men känsligt för objektform, vinkel och eko.
- IR-reflektion är bra nära ytor men påverkas starkt av material och ljus.
- ToF är kompakt och ofta praktiskt via I2C, men har synfält och ytkänslighet.
- PIR är bra för mänsklig rörelse men inte för exakt avstånd eller stillasittande närvaro.
- Radar/mmWave kan upptäcka mer subtil närvaro men kräver mer konfiguration.
- Reed switch, hallgivare och mikrobrytare är ofta bäst när fysisk status kan mätas direkt.
- Hysteresis och tidslogik gör sensordata användbar i verkliga system.
- Dokumentera alltid mätområde, falska utslag och miljöförutsättningar.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Ofta 3,3 V eller 5 V via modul |
| Typiskt gränssnitt | Digital trigger/echo, I2C, UART eller analogt |
| Välj när | objekt, person eller avstånd ska upptäckas |
| Välj inte när | du behöver garanterad säkerhetsdetektion |
| Vanliga fel | falska ekon, PIR-fördröjning, reflekterande ytor, fel synfält |
| Alternativ att överväga | ultraljud, ToF, PIR, mmWave, brytare |

Använd referensrutan som en snabb kontroll innan du bygger projektet. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När sensorn ger digital närvaro, puls eller triggsignal, jämför med kapitel 5 och kapitel 8.
- När sensorn ger analog avstånds- eller närvarosignal, använd kapitel 6.
- När modulen kommunicerar via I2C, UART eller annan buss, börja med kapitel 9.
- När mätningen varierar med placering, objekt eller kablage, använd felsökningsmönstren i kapitel 35.

