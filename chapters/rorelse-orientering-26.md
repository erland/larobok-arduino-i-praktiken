# 26. Rörelse, orientering och vibration

## Sensoröversikt
Rörelse är en av de sensorvärldar där Arduino-projekt snabbt blir intressanta. En sensor kan känna att ett objekt lutar, att en låda skakas, att en maskin vibrerar, att en robot ändrar riktning eller att en handkontroll vrids i luften. Samtidigt är rörelsesensorer lätta att misstolka, eftersom de ofta inte mäter det man först tror.

En accelerometer mäter inte “position”. Den mäter acceleration, inklusive tyngdkraftens acceleration. Ett gyroskop mäter inte absolut riktning. Det mäter rotationshastighet och driver över tid. En magnetometer pekar inte alltid på norr. Den påverkas av metall, kablar, motorer och magneter. En vibrationssensor kan säga att något skakade, men inte nödvändigtvis varför.

Det här kapitlet hjälper dig att välja mellan vanliga rörelse- och orienteringssensorer:

- accelerometrar
- gyroskop
- IMU-moduler
- magnetometrar
- tilt-sensorer
- vibrationssensorer
- enklare stötsensorer och brytarbaserade rörelsedetektorer

Kapitlet fungerar som praktiskt stöd när du behöver skilja mellan acceleration, rotation, orientering och vibration, välja mellan tilt-sensor, vibrationssensor, accelerometer, gyroskop, magnetometer och IMU, och skapa enkla trösklar, filtrering och hysteresis för rörelsedata. Målet är att du ska kunna avgöra när en enkel tilt- eller vibrationssensor räcker, när en accelerometer är rätt verktyg, när du behöver en IMU och när du bör undvika att göra orienteringsproblem svårare än de behöver vara.

## Förutsättningar

Det här kapitlet bygger på tidigare kapitel om analog läsning, digital I/O, tidsstyrning och I2C. Många moderna rörelsesensorer använder I2C, medan enklare tilt- och vibrationsmoduler ofta beter sig som digitala brytare eller analoga signaler.

Det viktigaste är att inte börja med kod. Börja med frågan:

- Vill du veta om något **lutar**?
- Vill du veta om något **rör sig**?
- Vill du veta hur snabbt något **roterar**?
- Vill du veta om något **vibrerar**?
- Vill du uppskatta en **orientering**?
- Vill du bara upptäcka en **händelse**, till exempel ett slag eller en skakning?

Många projekt behöver bara en robust händelsedetektering. Då kan en enkel vibrationssensor eller tilt-brytare vara bättre än en avancerad IMU. Andra projekt behöver däremot kontinuerliga mätvärden från flera axlar. Då är en digital accelerometer eller IMU mer lämplig.

## Grundbegrepp: axlar och rörelse

De flesta rörelsesensorer beskriver världen i tre axlar:

- **X-axel:** rörelse eller lutning i sidled enligt modulens märkning
- **Y-axel:** rörelse eller lutning i andra horisontella riktningen
- **Z-axel:** ofta uppåt/nedåt om modulen ligger plant

Det finns inget universellt krav på hur en modul monteras. Därför måste du alltid dokumentera din egen orientering:

- vilken sida av modulen som pekar framåt
- vilken sida som pekar uppåt
- vilken axel som används i koden
- vilket råvärde som motsvarar viloläge
- vilken tröskel som betyder rörelse, lutning eller vibration

En bra rörelselogik börjar med en liten kalibrering. Läs råvärden när systemet ligger stilla. Skriv ned vad sensorn visar. Vrid sedan modulen på ett kontrollerat sätt och se vilken axel som ändras.

## Viktiga valkriterier

När du väljer rörelsesensor bör du tänka på fler saker än bara “har den tre axlar?”.

| Fråga | Varför den spelar roll |
|---|---|
| Behöver du bara en händelse eller kontinuerliga värden? | En tilt-brytare räcker för händelser, men inte för mätning. |
| Behöver du lutning, rotation eller vibration? | Olika sensorer mäter olika fysiska fenomen. |
| Behöver du absolut riktning? | Då kan magnetometer eller extern referens behövas. |
| Hur snabb är rörelsen? | Uppdateringshastighet och filtrering påverkar resultatet. |
| Är miljön brusig eller mekaniskt stökig? | Motorer och vibrationer kan ge falska utslag. |
| Finns metall, motorer eller magneter nära? | Magnetometrar kan bli opålitliga. |
| Ska systemet batteridrivas? | Välj sensor och uppdateringsfrekvens efter strömbudget. |
| Ska sensorn sitta på rörlig mekanik? | Kabeldragning, dragavlastning och montering påverkar mätningen. |

Som tumregel: välj den enklaste sensor som svarar på rätt fråga.

## Tilt-sensorer: när bara lutning räcker

En tilt-sensor är ofta en enkel brytare som ändrar läge när den lutar. Äldre varianter kan innehålla en liten kula eller mekanisk kontakt. Andra moduler kan vara halvledarbaserade men används på samma sätt: de ger en enkel digital signal.

Tilt-sensorer passar när du bara behöver veta om något har ändrat läge ungefärligt:

- en låda har vält
- ett lock är öppet eller stängt
- ett objekt har passerat en enkel lutningsgräns
- en installation har flyttats från sitt normala läge

De passar sämre när du behöver exakt vinkel, snabb respons eller stabil mätning i en miljö med vibrationer. En mekanisk tilt-sensor kan studsa på samma sätt som en knapp. Därför bör den ofta debouncas.

## Exempel: läsa en tilt-sensor som brytare

### Det här används i exemplet

- Arduino-kompatibelt kort
- tilt-sensormodul med digital utgång
- LED med seriemotstånd eller inbyggd LED på kortet
- kopplingskablar

### Koppling

- Sensorns VCC till rätt matningsspänning enligt modulen
- Sensorns GND till gemensam jord
- Sensorns digitala utgång till pinne 2
- LED till pinne 13 eller använd kortets inbyggda LED om den finns

Kontrollera om modulen har egen pull-up eller pull-down. Om du använder en ren brytare utan modul kan du använda intern pull-up och koppla brytaren mot GND.

### Kod

```cpp
const int tiltPin = 2;
const int ledPin = LED_BUILTIN;

const unsigned long debounceMs = 40;

bool stableTilted = false;
bool lastRawState = false;
unsigned long lastChangeTime = 0;

void setup() {
  pinMode(tiltPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  bool rawTilted = digitalRead(tiltPin) == LOW;

  if (rawTilted != lastRawState) {
    lastRawState = rawTilted;
    lastChangeTime = millis();
  }

  if (millis() - lastChangeTime >= debounceMs) {
    if (stableTilted != rawTilted) {
      stableTilted = rawTilted;
      Serial.println(stableTilted ? "Tilted" : "Normal");
    }
  }

  digitalWrite(ledPin, stableTilted ? HIGH : LOW);
}
```

### Förväntat resultat

När sensorn lutar tillräckligt ändras LED-status och ett meddelande skrivs i seriell monitor. Om sensorn skakar bör debouncingen minska antalet falska växlingar.

## Vibrationssensorer och stötdetektering

Vibrationssensorer används när du vill upptäcka skakning, slag, mekanisk aktivitet eller vibrationer. De kan vara enkla brytarliknande sensorer, piezoelement, fjädermoduler eller mer avancerade accelerometerbaserade lösningar.

En enkel vibrationssensor svarar ofta på frågan: “Hände något?” Den ger inte en exakt vibrationsanalys. Den kan ändå vara mycket användbar för:

- larm vid slag eller skakning
- enkel maskinövervakning
- aktivitetsdetektering
- interaktiva installationer
- väckning av batteridrivet system

Vibrationssensorer kräver ofta tidslogik. Ett enstaka utslag kan vara brus, medan flera utslag inom en kort period kan vara verklig aktivitet. Du kan därför räkna pulser under ett tidsfönster.

## Exempel: enkel vibrationsdetektor

```cpp
const int vibrationPin = 3;
const int ledPin = LED_BUILTIN;

const unsigned long windowMs = 1000;
const int triggerCount = 3;

unsigned long windowStart = 0;
int eventsInWindow = 0;
bool alarmActive = false;

void setup() {
  pinMode(vibrationPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  windowStart = millis();
}

void loop() {
  static bool lastState = HIGH;
  bool state = digitalRead(vibrationPin);

  if (lastState == HIGH && state == LOW) {
    eventsInWindow++;
  }
  lastState = state;

  if (millis() - windowStart >= windowMs) {
    alarmActive = eventsInWindow >= triggerCount;

    Serial.print("Vibration events: ");
    Serial.print(eventsInWindow);
    Serial.print(" alarm: ");
    Serial.println(alarmActive ? "yes" : "no");

    eventsInWindow = 0;
    windowStart = millis();
  }

  digitalWrite(ledPin, alarmActive ? HIGH : LOW);
}
```

Det här är inte en exakt mätning av vibrationsnivå. Det är en enkel händelselogik. För många praktiska projekt är det precis rätt nivå.

## Accelerometrar: lutning, rörelse och tyngdkraft

En accelerometer mäter acceleration längs en eller flera axlar. Det viktiga är att den också känner av tyngdkraften. När en 3-axlig accelerometer ligger stilla på ett bord visar den ungefär 1 g på den axel som pekar uppåt eller nedåt och nära 0 g på de andra axlarna, beroende på modulens orientering.

Det gör accelerometrar användbara för lutning. Om modulen vrids ändras hur tyngdkraften fördelas mellan axlarna. Det betyder däremot inte att accelerometern ger stabil position. Om du integrerar acceleration för att få hastighet och position växer mätfel snabbt.

Accelerometrar passar för:

- lutningsdetektering
- skakdetektering
- fall- eller stötdetektering
- aktivitetsmätning
- enklare geststyrning
- vibrationsindikering på låg till medelhög nivå

De passar sämre för:

- exakt position över tid
- långsiktig navigering utan andra referenser
- miljöer med mycket mekaniskt brus utan filtrering
- högprecision utan kalibrering och mekanisk kontroll

## Accelerometer som lutningssensor

För att använda en accelerometer som lutningssensor behöver du ofta inte räkna ut exakta vinklar. Det räcker att observera axelvärden och skapa trösklar.

Exempel:

- Om X är nära 1 g lutar modulen åt ett håll.
- Om X är nära -1 g lutar den åt motsatt håll.
- Om Z är nära 1 g ligger modulen plant.
- Om summan av förändringar är stor på kort tid har modulen skakats.

För en robust produkt bör du kalibrera mot den faktiska monteringen. För experiment räcker det ofta att skriva ut råvärden och välja trösklar efter observation.

## Gyroskop: rotationshastighet och drift

Ett gyroskop mäter rotationshastighet, ofta i grader per sekund. Det är användbart när du vill veta hur snabbt något vrids. Men gyroskop har en viktig begränsning: de driver över tid. Små offsetfel integreras och blir större vinkelavvikelser.

Gyroskop passar för:

- snabb rotationsdetektering
- stabilisering
- kortvarig vinkeluppskattning
- gestdetektering
- robotik där snabb förändring är viktig

De passar sämre som ensam sensor för:

- absolut orientering under lång tid
- kompassriktning
- stabil vinkel utan korrigering
- projekt där kalibrering inte är möjlig

I praktiken kombineras gyroskop ofta med accelerometer. Accelerometern ger långsam lutningsreferens via tyngdkraften, medan gyroskopet ger snabb rotationsinformation. Det är grundidén bakom många IMU-lösningar.

## IMU: flera rörelsesensorer i samma modul

IMU betyder inertial measurement unit. I Arduino-sammanhang menar man ofta en modul som kombinerar accelerometer och gyroskop. Ibland ingår även magnetometer.

Vanliga benämningar:

- **6-DOF:** tre accelerometeraxlar och tre gyroskopaxlar
- **9-DOF:** accelerometer, gyroskop och magnetometer
- **DOF:** degrees of freedom, alltså frihetsgrader eller mätaxlar

En IMU är rätt val när du behöver mer än en enkel tröskel:

- orientering i ett interaktivt objekt
- robotlutning eller balans
- geststyrning
- rörelselogger
- data för sensorfusion
- stabilare rörelseinformation än en enskild sensor ger

Men en IMU är också lätt att överanvända. Om du bara vill veta om ett lock är öppet, använd en brytare. Om du bara vill veta om något vibrerar, börja med en enkel vibrationssensor eller accelerometer. Välj IMU när du faktiskt behöver kombinationen.

## Magnetometer och kompassproblem

En magnetometer mäter magnetfält. Den kan användas som elektronisk kompass, men den är känslig för omgivningen. I ett Arduino-projekt finns ofta metall, kablar, strömförande ledare, motorer, högtalare, magneter och batterier i närheten. Allt detta kan påverka mätningen.

Magnetometrar passar när:

- du behöver ungefärlig kompassriktning
- sensorn kan placeras bort från störkällor
- du kan kalibrera systemet
- miljön är relativt stabil

De passar sämre när:

- kortet sitter nära motorer eller stora strömmar
- konstruktionen innehåller rörliga magneter
- absolut riktning är säkerhetskritisk
- användaren inte kan kalibrera efter montering

Om ett projekt bara behöver veta lutning eller rörelse ska du inte lägga till magnetometer i onödan. Den gör systemet mer känsligt för monterings- och miljöproblem.

## Filtrering: från råvärde till användbar status

Rörelsedata är ofta brusig. Det gäller särskilt när sensorn sitter på något som vibrerar, när kablar rör sig eller när koden reagerar på varje liten förändring. Därför bör du skilja mellan råvärde, filtrerat värde och systemstatus.

En enkel kedja kan se ut så här:

1. Läs råvärden från sensor.
2. Subtrahera viloläge eller offset.
3. Beräkna ett enklare mått, till exempel total förändring.
4. Filtrera med glidande medelvärde eller lågpassfilter.
5. Använd tröskel och hysteresis.
6. Uppdatera status först när förändringen varit stabil en viss tid.

För händelser som skakning kan du i stället räkna antal toppar under ett tidsfönster. För lutning kan du kräva att värdet ligger över tröskeln i exempelvis 100 millisekunder innan status ändras.

## En enkel rörelseindikator med analog accelerometer

Vissa accelerometer-moduler har analoga utgångar för X, Y och Z. Då kan du läsa dem med `analogRead`. Moderna digitala IMU-moduler är vanligare, men analogt exempel är pedagogiskt eftersom det visar principen utan bibliotek.

```cpp
const int xPin = A0;
const int yPin = A1;
const int zPin = A2;

const int ledPin = LED_BUILTIN;
const int motionThreshold = 60;

int xBase = 0;
int yBase = 0;
int zBase = 0;

int readAverage(int pin) {
  long sum = 0;

  for (int i = 0; i < 20; i++) {
    sum += analogRead(pin);
    delay(2);
  }

  return sum / 20;
}

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);

  delay(500);
  xBase = readAverage(xPin);
  yBase = readAverage(yPin);
  zBase = readAverage(zPin);

  Serial.println("Calibration complete");
}

void loop() {
  int x = readAverage(xPin);
  int y = readAverage(yPin);
  int z = readAverage(zPin);

  int movement =
    abs(x - xBase) +
    abs(y - yBase) +
    abs(z - zBase);

  bool moving = movement > motionThreshold;

  digitalWrite(ledPin, moving ? HIGH : LOW);

  Serial.print("x=");
  Serial.print(x);
  Serial.print(" y=");
  Serial.print(y);
  Serial.print(" z=");
  Serial.print(z);
  Serial.print(" movement=");
  Serial.println(movement);

  delay(50);
}
```

Det här exemplet kalibrerar viloläget vid start. Om sensorn flyttas till ett nytt normalläge bör du kalibrera om. I ett riktigt system kan du lägga till en knapp för ny kalibrering.

## Digitala IMU-moduler via I2C

Många vanliga IMU-moduler ansluts med I2C. Då får du inte bara ett analogt värde utan registerbaserad sensordata via ett bibliotek. Kodens exakta form beror på sensor och bibliotek, men arbetsflödet är ofta samma:

- inkludera bibliotek
- starta I2C
- initiera sensorn
- kontrollera att sensorn hittades
- välj mätområde och uppdateringshastighet
- läs accelerometer och eventuellt gyroskop
- översätt värden till status eller loggning

Ett generellt kodmönster kan beskrivas så här:

```cpp
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  Wire.begin();

  // Initiera sensorn med valt bibliotek.
  // Kontrollera alltid returvärde eller status.
}

void loop() {
  // Läs accelerometerdata.
  // Läs gyroskopdata om det behövs.
  // Filtrera eller tolka värdena.
  // Uppdatera systemstatus.

  delay(20);
}
```

Det viktiga är inte vilket bibliotek du använder i första testet. Det viktiga är att du dokumenterar sensor, biblioteksversion, I2C-adress, mätområde och hur modulen är monterad.

## Referensmönster: lutnings- och skakindikator

### Vad mönstret visar

Mönstret visar hur en rörelsesensor kan användas för två olika systemstatusar:

- **Tilted:** objektet lutar från sitt normalläge.
- **Shaken:** objektet har utsatts för snabb rörelse eller vibration.

Mönstret kan användas med analog accelerometer, digital accelerometer eller IMU. Använd det bibliotek som passar din modul. Det centrala är logiken, inte den exakta sensormodellen.

### Det här används i exemplet

- Arduino-kompatibelt kort
- accelerometer- eller IMU-modul
- LED eller RGB-LED för status
- kopplingskablar
- eventuell breadboard
- seriell monitor

### Koppling

För I2C-modul:

- VCC till rätt spänning enligt modulen
- GND till gemensam jord
- SDA till kortets SDA
- SCL till kortets SCL

Kontrollera om modulen är 3,3 V, 5 V-tolerant eller har nivåskiftning. Om kortet är 5 V och modulen bara tål 3,3 V på I2C behöver du nivåskiftning eller ett 3,3 V-kort.

För analog modul:

- VCC till rätt spänning
- GND till gemensam jord
- X, Y och Z till analoga ingångar

### Arbetsgång

1. Lägg sensorn i sitt normalläge.
2. Läs råvärden i seriell monitor.
3. Spara normalläget som baslinje.
4. Luta sensorn långsamt och notera vilka axlar som ändras.
5. Skaka sensorn kort och notera hur värdena förändras.
6. Välj en tröskel för lutning och en annan för skakning.
7. Lägg till hysteresis eller tidsfönster så att statusen blir stabil.
8. Dokumentera trösklar och montering.

### Förväntat resultat

När modulen lutar från sitt normalläge ska systemet visa lutning. När modulen skakas snabbt ska systemet visa skakning under en kort tid och sedan återgå. Seriell monitor ska göra det möjligt att se varför statusen ändras.

## Vanliga användningar av samma rörelsemönster

Lutnings- och skakmönstret kan återanvändas i många projekt utan att koden behöver bli mycket mer avancerad. Det viktiga är att baslinje, trösklar och tidslogik anpassas till monteringen.

| Användning | Vad mönstret behöver avgöra |
|---|---|
| Låda har vält | orienteringen avviker från normalläget under en viss tid |
| Dörr eller lock har ändrat läge | lutningen eller en axel passerar en stabil gräns |
| Enhet skakas | korta rörelsetoppar passerar en skaktröskel |
| Motor eller fläkt vibrerar ovanligt | vibrationsnivån skiljer sig från normal drift |
| Sensor ska bara vara aktiv vid rörelse | rörelse används som väckning eller aktiveringsvillkor |

Samma sensorvärde kan alltså bli flera olika systembeslut. Börja med råvärden och en enkel status, och lägg först därefter till mer avancerad filtrering.

## Valguide

| Behov | Rekommenderad lösning | Kommentar |
|---|---|---|
| Upptäcka om något vält | Tilt-sensor eller accelerometer | Tilt-sensor är enklast, accelerometer ger mer information. |
| Upptäcka slag eller skakning | Vibrationssensor eller accelerometer | Vibrationssensor räcker för enkel händelse. |
| Mäta lutning i flera riktningar | 3-axlig accelerometer | Kräver montering och kalibrering. |
| Mäta snabb rotation | Gyroskop eller IMU | Tänk på drift över tid. |
| Uppskatta orientering | IMU, eventuellt med sensorfusion | Kräver mer kod och kalibrering. |
| Kompassriktning | Magnetometer eller 9-DOF IMU | Känslig för magnetiska störningar. |
| Maskinvibration på enkel nivå | Accelerometer eller vibrationssensor | För avancerad vibrationsanalys krävs mer än enkel Arduino-logik. |
| Batteridriven rörelsedetektering | Sensor med interrupt eller låg strömförbrukning | Låt sensorn väcka mikrokontrollern om möjligt. |

## Vanliga misstag

- **Misstag: Att tro att accelerometer betyder position.**
  - **Varför det händer:** Acceleration kan matematiskt integreras till hastighet och position, men små mätfel växer snabbt.
  - **Hur man undviker det:** Använd accelerometer för lutning, rörelse och händelser, inte för långsiktig positionsmätning utan externa referenser.

- **Misstag: Att använda gyroskop som absolut vinkelgivare.**
  - **Varför det händer:** Gyroskopets rotationshastighet känns som om den borde kunna summeras till vinkel.
  - **Hur man undviker det:** Räkna med drift och kombinera med accelerometer eller annan referens om vinkeln ska vara stabil över tid.

- **Misstag: Att montera sensorn utan att dokumentera axlarna.**
  - **Varför det händer:** Modulen fungerar i test, men riktningar blir otydliga när den byggs in.
  - **Hur man undviker det:** Rita eller skriv in X, Y, Z, framåt, uppåt och normalt råvärde i projektets sensorprofil.

- **Misstag: Att reagera direkt på varje råvärde.**
  - **Varför det händer:** Rörelsesensorer ger mycket data och små variationer.
  - **Hur man undviker det:** Använd filtrering, hysteresis och tidslogik innan du ändrar systemstatus.

- **Misstag: Att välja IMU när en brytare räcker.**
  - **Varför det händer:** IMU-moduler är billiga och verkar mer professionella.
  - **Hur man undviker det:** Börja med kravet. Om frågan bara är öppet/stängt, lutat/inte lutat eller skakat/inte skakat kan en enklare sensor vara bättre.

- **Misstag: Att lita på magnetometer nära motorer.**
  - **Varför det händer:** Kompassvärden ser rimliga ut på bordet men ändras när projektet monteras.
  - **Hur man undviker det:** Testa magnetometern i slutlig miljö och placera den bort från strömmar, motorer och magneter.

## Snabb överblick

- Tilt-sensorer och vibrationssensorer är ofta bästa valet när du bara behöver en enkel händelse.
- Accelerometrar mäter acceleration inklusive tyngdkraft och kan därför användas för lutning.
- Gyroskop mäter rotationshastighet men driver över tid om de används ensamma för vinkel.
- IMU-moduler kombinerar flera sensorer och passar när projektet behöver mer avancerad rörelseinformation.
- Magnetometrar kan ge kompassriktning men är känsliga för metall, motorer och magnetfält.
- Rörelsedata behöver ofta filtrering, hysteresis och tidslogik.
- Spara sensoraxlar, montering, vilovärden, trösklar och felkällor medan mönstret fungerar.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Ofta 3,3 V-logik |
| Typiskt gränssnitt | I2C, SPI, analogt eller digital trigger |
| Välj när | lutning, vibration, acceleration eller orientering behövs |
| Välj inte när | mekanisk brytare ger enklare och robustare svar |
| Vanliga fel | brus, drift, fel axelriktning, saknad kalibrering |
| Alternativ att överväga | tilt-switch, encoder, IMU, vibrationssensor |

Använd referensrutan som en snabb kontroll innan du bygger projektet. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat


- Använd kapitel 8 när rörelsedata ska trigga händelser snabbt, väcka systemet eller kombineras med watchdog.
- Använd kapitel 9 när IMU- eller accelerometermodulen kommunicerar via I2C/SPI och ger bussproblem.
- Använd kapitel 35 när projektet reagerar fel på rörelse trots att sensorn verkar fungera i enkel testkod.

