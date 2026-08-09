# 29. Position, tid och identitet

## Modulöversikt
Många Arduino-projekt behöver veta mer än vad som händer just nu vid en enskild pinne. De behöver veta **var** något händer, **när** det händer eller **vilken** sak eller användare som är inblandad. Det kan handla om en datalogger som ska tidsstämpla mätvärden, en portabel sensor som ska veta sin position, ett låssystem som använder RFID-taggar eller en mätstation som ska komma ihåg händelser även när den inte är uppkopplad.

Position, tid och identitet är tre olika problemområden, men de dyker ofta upp i samma projekt.

- En miljölogger kan behöva en realtidsklocka för att tidsstämpla mätningar.
- En mobil sensor kan behöva GNSS för att veta var mätningen gjordes.
- Ett åtkomstsystem kan behöva RFID eller NFC för att identifiera användare.
- Ett system med flera noder kan behöva unika ID:n för att skilja enheter från varandra.
- Ett batteridrivet projekt kan behöva väga precision mot strömförbrukning.

Det här kapitlet ger en praktisk överblick över vanliga lösningar: GPS/GNSS-moduler, RTC-kretsar, RFID/NFC-moduler, enkla ID-lösningar och mjukvarubaserade identifiers. Målet är inte att bygga ett komplett navigationssystem eller ett säkert passersystem. Målet är att kunna välja rätt typ av modul, förstå gränserna och bygga test som är användbara som grund för större projekt.

Kapitlet fungerar som stöd när du behöver välja mellan GNSS, RTC, nätverkstid, RFID/NFC och enklare ID-lösningar samt strukturera händelser med tid, nod-ID och status.

## Förutsättningar

Du har redan mött flera byggstenar som behövs i det här kapitlet:

- UART, I2C och SPI från kommunikationskapitlet
- digital I/O och enkel händelselogik
- strömförsörjning och batterimätning
- sensorer som skapar mätvärden
- displayer och användargränssnitt som kan visa status
- EEPROM, FRAM och SD-kort som kommer fördjupas senare

Position, tid och identitet är ofta inte projektets huvudfunktion. De är snarare **metadata** som gör andra data mer användbara.

Ett temperaturvärde som bara säger `21.7` är ofta mindre användbart än ett värde som säger:

```text
2026-06-30 14:05:12, greenhouse-01, 21.7 C, 43 %
```

I den raden finns tid, identitet och mätdata. Om projektet dessutom är mobilt kan raden även innehålla position:

```text
2026-06-30 14:05:12, tracker-03, 59.3293, 18.0686, 21.7 C
```

Det här kapitlet handlar om hur sådana sammanhang skapas i ett Arduino-projekt.

## Tre frågor: var, när och vem

Ett praktiskt sätt att börja är att skilja mellan tre frågor.

| Fråga | Typisk teknik | Exempel |
|---|---|---|
| Var är systemet? | GNSS, enklare positionslogik, zon-ID | GPS-logger, cykeltracker, fältmätning |
| När hände det? | RTC, nätverkstid, GNSS-tid, intern tid | Datalogger, schemalagd styrning, händelselogg |
| Vem eller vad är detta? | RFID, NFC, UID, serienummer, DIP-switch | Passerkort, verktygs-ID, nod-ID |

De här frågorna blandas lätt ihop. En GNSS-modul kan ge både position och mycket exakt tid. En RFID-tagg kan identifiera ett kort men säger inget säkert om personen som håller i kortet. En RTC kan hålla tid, men vet inte var systemet är. Ett internt nod-ID kan identifiera en enhet, men säger inget om en användare.

Det är därför viktigt att skriva ned vilket problem du faktiskt försöker lösa.

- Behöver du absolut position eller räcker det att veta vilken zon systemet befinner sig i?
- Behöver du exakt klockslag eller räcker det med tid sedan start?
- Behöver du identifiera ett objekt eller behöver du säker autentisering?
- Ska informationen användas för felsökning, statistik, styrning eller åtkomstkontroll?

Ju mer beslut systemet ska fatta baserat på informationen, desto mer noga behöver du vara med kvaliteten.

## Position med GNSS

GNSS står för Global Navigation Satellite System och är samlingsnamn för satellitbaserade positioneringssystem. I vardagligt Arduino-sammanhang säger många fortfarande GPS, även när modulen kan använda flera satellitsystem.

En typisk GNSS-modul ger data som:

- latitud
- longitud
- höjd
- hastighet
- kurs
- antal satelliter
- uppskattad fix-kvalitet
- UTC-tid

Många moduler kommunicerar via UART och skickar textbaserade NMEA-meningar. Ett bibliotek kan tolka dessa meningar och ge mer lättanvända värden.

### När GNSS är rätt val

GNSS passar när projektet behöver absolut position utomhus.

Typiska exempel:

- spåra en cykel, båt, robot eller mätlåda
- tidsstämpla mätningar med position
- logga rörelse över en längre sträcka
- mäta ungefärlig hastighet
- synkronisera tid utan internet

GNSS är särskilt användbart när projektet är mobilt och inte kan förlita sig på fasta platser eller nätverk.

### När GNSS är fel val

GNSS är inte en magisk positionssensor. Det finns tydliga begränsningar.

GNSS passar dåligt när:

- systemet är inomhus
- antennen sitter skymd
- starttiden måste vara mycket kort
- batteriet är mycket begränsat
- positionen behöver vara exakt på centimeter- eller decimeternivå utan speciallösning
- projektet bara behöver veta vilken station, hylla eller maskin som är aktuell

I sådana fall kan andra lösningar vara bättre: RFID, NFC, BLE-beacons, manuellt zon-ID, QR-koder, reed switches, gränslägesbrytare eller helt enkelt ett konfigurerat nodnamn.

### Fix, kallstart och antennplacering

En GNSS-modul behöver få kontakt med satelliter innan den kan ge användbar position. Detta kallas ofta att få en **fix**.

Det finns några praktiska saker att förstå:

- Kallstart kan ta tid.
- Antennplacering påverkar resultatet mycket.
- Metall, byggnader och kroppen kan skärma signalen.
- Fönsterplacering kan fungera ibland men är inte pålitlig.
- En modul kan ge tid innan positionen är stabil.
- Latitud och longitud kan hoppa även när modulen ligger still.

För experiment bör du börja utomhus eller nära ett fönster med god sikt mot himlen. Börja inte med att felsöka GNSS i ett rum långt inne i en byggnad.

### UART och NMEA i praktiken

Många GNSS-moduler skickar löpande textdata via UART. Det kan se ut ungefär så här:

```text
$GPRMC,120000.00,A,5920.1234,N,01804.5678,E,0.05,31.66,300626,,,A*68
```

Du behöver normalt inte själv tolka varje fält. Ett bibliotek kan läsa tecken från seriell port och bygga upp strukturerade värden. Det viktiga är att förstå arbetsmönstret:

1. Läs inkommande tecken från GNSS-modulen.
2. Mata tecknen till parsern.
3. Kontrollera om en ny position eller tid finns.
4. Kontrollera om värdet är giltigt.
5. Använd bara värdet om fix-kvaliteten är tillräcklig.

Ett förenklat kodmönster kan se ut så här:

```cpp
#include <TinyGPSPlus.h>

TinyGPSPlus gps;

HardwareSerial gpsSerial(1);

const int GPS_RX_PIN = 16;
const int GPS_TX_PIN = 17;

void setup() {
  Serial.begin(115200);
  gpsSerial.begin(9600, SERIAL_8N1, GPS_RX_PIN, GPS_TX_PIN);
}

void loop() {
  while (gpsSerial.available() > 0) {
    gps.encode(gpsSerial.read());
  }

  if (gps.location.isUpdated() && gps.location.isValid()) {
    double latitude = gps.location.lat();
    double longitude = gps.location.lng();

    Serial.print("Latitude: ");
    Serial.println(latitude, 6);
    Serial.print("Longitude: ");
    Serial.println(longitude, 6);
  }
}
```

Det här exemplet är skrivet med ESP32-liknande seriell port i åtanke. På ett UNO-liknande kort behöver du ofta använda `SoftwareSerial` eller ett kort med extra hårdvaru-UART, till exempel Mega, ESP32 eller vissa moderna kort. Det är en bra påminnelse om att kortval och modulval hör ihop.

### Strömförbrukning och uppdateringstakt

GNSS kan dra mer ström än många enkla sensorer. För ett stationärt, USB-matat experiment spelar det kanske ingen större roll. För en batteridriven datalogger kan det vara avgörande.

Vanliga strategier är:

- slå bara på GNSS när position behövs
- sänk uppdateringstakten om modulen stödjer det
- använd last switch eller MOSFET för att stänga av modulen helt
- lagra senaste kända position om projektet rör sig långsamt
- skilj mellan “ingen fix ännu” och “position okänd”

Ett vanligt misstag är att låta GNSS-modulen vara på hela tiden trots att projektet bara behöver position någon gång per timme.

## Tid i Arduino-projekt

Arduino-kod har alltid någon form av tid. Funktionen `millis()` berättar hur lång tid som gått sedan programmet startade. Men det är inte samma sak som kalender- och klocktid.

Det finns minst fyra typer av tid som är relevanta:

| Tidstyp | Exempel | Passar för |
|---|---|---|
| Tid sedan start | `millis()` | intervaller, timeout, icke-blockerande logik |
| Kalender- och klocktid | 2026-06-30 14:05 | loggning, schemaläggning, rapporter |
| Nätverkstid | NTP | uppkopplade system |
| Satellittid | GNSS | mobila system utan internet |

När ett projekt bara behöver blinka en LED var femte sekund räcker `millis()`. När ett projekt ska spara en mätning som senare ska analyseras behöver det ofta riktig tidsstämpel.

## RTC-kretsar

RTC står för Real-Time Clock. En RTC-krets håller reda på datum och klockslag även när mikrokontrollern startar om. Många RTC-moduler har ett litet knappcellsbatteri så att tiden fortsätter gå när huvudströmmen är avstängd.

Vanliga RTC-kretsar i Arduino-världen är exempelvis DS1307, DS3231 och PCF8523. De kommunicerar ofta via I2C.

### När RTC är rätt val

RTC passar när:

- projektet ska logga data utan internet
- kortet kan starta om men tiden måste finnas kvar
- mätningar ska ske vid vissa klockslag
- systemet ska kunna vara avstängt men ändå komma ihåg tiden
- batteriförbrukningen ska vara låg
- GNSS är onödigt eller opraktiskt

En väderstation, ett växthusprojekt, en energilogger eller en fristående händelselogg är typiska RTC-projekt.

### När RTC inte behövs

RTC kan vara onödigt när:

- projektet alltid är uppkopplat och kan hämta nätverkstid
- tidsstämplar bara används relativt start
- användaren alltid ställer tid manuellt vid start
- loggningen bara gäller korta experiment

En RTC är en extra komponent, en extra I2C-enhet och en extra felkälla. Lägg till den när projektet faktiskt behöver den.

### Noggrannhet och drift

Alla klockor driver. En billig RTC kan gå fel med sekunder eller minuter över tid. En mer noggrann RTC, ofta temperaturkompenserad, driver mindre. För många Arduino-projekt är en DS3231-liknande modul populär just eftersom den brukar ge bättre noggrannhet än enklare RTC-varianter.

Fråga dig:

- Hur mycket fel är acceptabelt?
- Ska tiden bara användas för sortering av mätvärden?
- Ska systemet styra något vid exakta klockslag?
- Finns möjlighet att synkronisera mot nätverk eller GNSS ibland?
- Vad händer när backupbatteriet tar slut?

### Kodmönster för RTC

Många RTC-bibliotek följer samma grundmönster:

1. Starta I2C.
2. Starta RTC-objektet.
3. Kontrollera att RTC finns.
4. Kontrollera om tiden är satt.
5. Läs aktuell tid.
6. Formatera tidsstämpeln.
7. Använd tidsstämpeln i logg eller styrning.

Ett förenklat exempel:

```cpp
#include <Wire.h>
#include "RTClib.h"

RTC_DS3231 rtc;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  if (!rtc.begin()) {
    Serial.println("RTC not found");
    while (true) {
      delay(1000);
    }
  }

  if (rtc.lostPower()) {
    Serial.println("RTC lost power, setting compile time");
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }
}

void loop() {
  DateTime now = rtc.now();

  char timestamp[24];
  snprintf(
    timestamp,
    sizeof(timestamp),
    "%04d-%02d-%02d %02d:%02d:%02d",
    now.year(),
    now.month(),
    now.day(),
    now.hour(),
    now.minute(),
    now.second()
  );

  Serial.println(timestamp);
  delay(1000);
}
```

Att sätta tiden till kompileringstid är praktiskt i experiment, men det är inte alltid rätt i ett färdigt system. Kompileringstid är inte nödvändigtvis samma som verklig tid när enheten startar. I ett mer robust system behöver du en tydlig rutin för tidssättning.

### Tidszoner och sommartid

Ett enkelt råd för dataloggning är: lagra helst tid i UTC och hantera lokal tid vid visning.

Det minskar problem med:

- sommartid
- tidszonsbyte
- system som flyttas mellan platser
- data som jämförs mellan flera noder

För små lokala experiment kan lokal tid vara enklare. Men så fort data ska jämföras, exporteras eller användas över längre tid blir UTC ofta mer robust.

## Nätverkstid

Uppkopplade kort som ESP8266, ESP32 och vissa moderna Arduino-kort kan hämta tid via NTP. Det är ofta enklare än RTC om systemet ändå har Wi-Fi.

Nätverkstid passar när:

- projektet redan är uppkopplat
- internet eller lokal tidsserver finns
- högre noggrannhet än billig RTC önskas
- backupbatteri ska undvikas

Nätverkstid passar sämre när:

- projektet ska fungera offline
- Wi-Fi bara är tillgängligt ibland
- starttid måste vara omedelbar
- batteriförbrukning är kritisk

Ett vanligt mönster är att använda nätverkstid för synkronisering och sedan låta systemet gå på intern tid mellan synkroniseringar. I mer robusta system kan en RTC användas som lokal klocka och synkroniseras när nätverk finns.

## GNSS som tidskälla

GNSS-moduler kan ge mycket bra tid när de har satellitkontakt. För vissa projekt är tid viktigare än position. En GNSS-modul kan då användas som fristående tidskälla där nätverk saknas.

Det passar exempelvis för:

- fältlogger
- mobila mätstationer
- system som ska synkronisera tid utomhus
- experiment där både tid och position behövs

Begränsningen är samma som för position: modulen behöver antennläge och satellitkontakt.

## Identitet med RFID och NFC

RFID och NFC används ofta för att identifiera kort, taggar eller objekt. I Arduino-världen är moduler som arbetar på 13,56 MHz vanliga, till exempel moduler baserade på MFRC522 eller PN532. De används ofta med kort eller små taggar.

Det viktiga är att skilja mellan tre nivåer:

- **Upptäckt:** det finns en tagg nära läsaren.
- **Identifiering:** taggen har ett UID eller annan identifierare.
- **Autentisering:** systemet kan med rimlig säkerhet avgöra att taggen eller användaren är behörig.

Många hobbyprojekt stannar vid identifiering. Det kan vara helt okej för experiment, men det är inte samma sak som ett säkert passersystem.

### När RFID/NFC är rätt val

RFID/NFC passar när:

- användaren eller objektet kan ha en tagg
- avståndet får vara kort
- interaktionen ska vara medveten
- mekanisk kontakt ska undvikas
- systemet ska vara enkelt att använda
- det räcker att identifiera ett kort eller objekt

Typiska prototyper:

- enkel närvarologg
- verktygsidentifiering
- låtsas-passersystem
- val av profil eller inställning
- inventarie-ID

### När RFID/NFC inte passar

RFID/NFC passar sämre när:

- avståndet behöver vara flera meter
- taggen måste läsas genom metall eller svåra material
- hög säkerhet krävs
- många taggar ska läsas samtidigt
- användaren inte aktivt ska hålla upp något
- systemet ska fungera i hård industriell miljö utan rätt komponentval

För längre avstånd kan BLE, UHF RFID eller andra tekniker vara bättre, men de ligger utanför den enkla Arduino-nivån för det här kapitlet.

### UID är inte samma sak som säkerhet

Många exempel på nätet använder taggens UID som “nyckel”. Det är pedagogiskt enkelt, men säkerhetsmässigt svagt. UID kan i vissa system läsas öppet och i vissa fall kopieras eller emuleras beroende på taggtyp och angriparmodell.

Det är därför bra att använda tydliga ord:

- För experiment: “den här taggen känns igen”.
- För enkel intern användning: “den här taggen ger en låg säkerhetsnivå”.
- För verklig åtkomstkontroll: “det här kräver en säkerhetsdesign som ligger utanför detta test”.

Det betyder inte att RFID är värdelöst. Det betyder att du ska vara ärlig med vad systemet skyddar mot.

### Kodmönster för RFID

En RFID-prototyp följer ofta denna struktur:

1. Starta SPI eller I2C beroende på modul.
2. Starta RFID-läsaren.
3. Vänta på en tagg.
4. Läs UID.
5. Jämför UID mot en lista.
6. Logga händelsen med tid.
7. Ge feedback med LED, buzzer eller display.

Pseudokod:

```cpp
void loop() {
  if (!tagPresent()) {
    return;
  }

  String uid = readTagUid();
  bool allowed = isAllowed(uid);

  DateTime now = rtc.now();
  logAccessEvent(now, uid, allowed);

  if (allowed) {
    showAcceptedFeedback();
  } else {
    showRejectedFeedback();
  }
}
```

Lägg märke till att taggen inte bara styr en utgång direkt. Systemet skapar en händelse, tidsstämplar den, loggar den och ger feedback. Det är ett mer robust sätt att tänka.

## Andra identitetslösningar

RFID är bara en lösning. I många Arduino-projekt räcker enklare identitet.

### Fast nod-ID i kod

Det enklaste är att ge varje enhet ett namn i koden:

```cpp
const char* NODE_ID = "greenhouse-01";
```

Det passar när du bygger få enheter och inte ofta byter hårdvara.

Nackdelen är att du måste kompilera om eller ändra kod för varje nod.

### DIP-switch eller lödbryggor

En DIP-switch eller några lödbryggor kan ge ett enkelt hårdvaru-ID. Det passar när samma firmware ska användas på flera enheter, men varje enhet ska kunna läsa sin egen adress vid start.

Exempel:

```cpp
const int ID_PIN_0 = 4;
const int ID_PIN_1 = 5;
const int ID_PIN_2 = 6;

int readNodeId() {
  int id = 0;

  if (digitalRead(ID_PIN_0) == LOW) {
    id += 1;
  }

  if (digitalRead(ID_PIN_1) == LOW) {
    id += 2;
  }

  if (digitalRead(ID_PIN_2) == LOW) {
    id += 4;
  }

  return id;
}
```

Med tre pinnar kan du skapa åtta ID:n. Med fler pinnar får du fler kombinationer, men du använder också fler GPIO.

### Serienummer och chip-ID

Vissa mikrokontrollers har unika eller nästan unika chip-ID:n. Det kan användas för att skapa nodidentitet utan extra komponenter. Men stödet varierar mellan plattformar, och du bör inte anta att alla Arduino-kompatibla kort fungerar likadant.

Använd chip-ID när:

- plattformen har dokumenterat stöd
- ID:t bara används för loggning eller enhetsidentifiering
- projektet inte kräver hemlig identitet

Använd inte chip-ID som ensam säkerhetsmekanism.

### Konfiguration i EEPROM, FRAM eller fil

En annan lösning är att spara ett nodnamn i icke-flyktigt minne. Det gör att samma firmware kan användas på flera enheter och att ID kan ändras utan omkompilering.

Det passar när:

- systemet ska installeras på flera platser
- användaren ska kunna konfigurera namn
- data ska loggas med mänskligt läsbart nod-ID
- enheten har display, seriell konfiguration eller webbgränssnitt

Det kräver mer kod, men är ofta bättre i större projekt.

## Tidsstämplade händelser

Det mest användbara mönstret i det här kapitlet är **tidsstämplad händelse**.

En händelse kan vara:

- en RFID-tagg lästes
- en dörr öppnades
- en sensor passerade en gräns
- en knapp trycktes
- en position uppdaterades
- batterinivån blev låg
- systemet startade om

En händelsepost kan se ut så här:

```text
2026-06-30T14:05:12Z,node-03,rfid,04A1B2C3,accepted
2026-06-30T14:06:03Z,node-03,battery,low,3.58
2026-06-30T14:07:41Z,node-03,position,59.329300,18.068600
```

Det här formatet är enkelt men kraftfullt. Det går att skriva till seriell monitor, SD-kort, FRAM, MQTT eller en HTTP-endpoint.

## Valguide

| Behov | Förstahandsval | Alternativ | Kommentar |
|---|---|---|---|
| Tidsstämpla offline-data | RTC | GNSS-tid | RTC är enkel och strömsnål. |
| Tidsstämpla uppkopplad data | NTP | RTC som backup | Bra för ESP8266/ESP32 och Wi-Fi-kort. |
| Position utomhus | GNSS | Manuell platskonfiguration | GNSS kräver antennläge och tid till fix. |
| Position inomhus | Zon-ID, RFID, BLE | Manuell konfiguration | GNSS fungerar ofta dåligt inomhus. |
| Identifiera objekt på kort avstånd | RFID/NFC | Streckkod, knappval | UID är identifiering, inte stark säkerhet. |
| Identifiera en nod | Fast nod-ID | DIP-switch, chip-ID, konfigurationsfil | Välj efter antal enheter och underhållsbehov. |
| Enkel åtkomstdemo | RFID + LED/buzzer | Keypad | Bra experiment men inte säkert passersystem. |

## Referensmönster: tidsstämplad RFID- eller knapphändelse

Det här referensmönstret kan användas på två nivåer. Om du har en RFID-läsare kan du använda den. Om du inte har det kan du använda en knapp som simulerar en identifierad händelse. Poängen är att bygga ett mönster för tid, identitet och loggning.

### Vad mönstret visar

Mönstret visar hur ett system kan:

- ha ett nod-ID
- läsa tid från RTC eller simulera tid med `millis()`
- ta emot en händelse från RFID eller knapp
- skapa en händelserad
- ge feedback med LED eller buzzer
- skriva händelsen till seriell monitor

### Rekommenderad hårdvara

För full version:

- Arduino-kompatibelt kort
- RTC-modul via I2C
- RFID/NFC-läsare
- en eller två RFID-taggar
- LED med seriemotstånd
- eventuell buzzer

För förenklad version:

- Arduino-kompatibelt kort
- knapp
- LED med seriemotstånd
- eventuell RTC-modul

### Kopplingsidé

För RTC:

- VCC till rätt matningsspänning enligt modul
- GND till gemensam jord
- SDA till kortets SDA
- SCL till kortets SCL

För RFID-läsare:

- använd SPI eller I2C beroende på modul
- kontrollera spänningsnivå noga
- undvik att anta att alla RFID-moduler tål 5 V på signalpinnar

För knappversion:

- ena sidan av knappen till GND
- andra sidan till digital ingång
- använd intern pull-up

### Kodstruktur

Kodens viktigaste delar bör vara separata funktioner:

```cpp
const char* NODE_ID = "bench-node-01";

void setup() {
  Serial.begin(115200);
  setupTimeSource();
  setupIdentitySource();
  setupFeedback();
}

void loop() {
  IdentityEvent event;

  if (readIdentityEvent(event)) {
    String timestamp = getTimestamp();
    logEvent(timestamp, NODE_ID, event);
    showFeedback(event.allowed);
  }
}
```

Det här är inte komplett kod. Det är en struktur. Poängen är att tid, identitet, loggning och feedback inte ska blandas ihop i en enda lång `loop()`.

### Förenklad knappversion

En minimal knappversion kan se ut så här:

```cpp
const int BUTTON_PIN = 2;
const int LED_PIN = 13;

const char* NODE_ID = "bench-node-01";

bool lastButtonState = HIGH;

void setup() {
  Serial.begin(115200);

  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  bool buttonState = digitalRead(BUTTON_PIN);

  if (lastButtonState == HIGH && buttonState == LOW) {
    unsigned long secondsSinceStart = millis() / 1000;

    Serial.print(secondsSinceStart);
    Serial.print(", ");
    Serial.print(NODE_ID);
    Serial.print(", ");
    Serial.print("button, ");
    Serial.println("pressed");

    digitalWrite(LED_PIN, HIGH);
    delay(100);
    digitalWrite(LED_PIN, LOW);
  }

  lastButtonState = buttonState;
}
```

Den här versionen använder tid sedan start i stället för kalenderklocka. Det är tillräckligt för att träna händelsestrukturen, men inte för en riktig datalogger som ska analyseras dagen efter.


### Typisk händelserad

En händelserad bör vara enkel att läsa både för människa och program. En kompakt rad kan till exempel se ut så här:

```text
2026-07-02T14:25:10;NODE-03;RFID;A1B2C3D4;ACCESS_GRANTED
```

Fälten betyder:

| Fält | Exempel | Varför det är med |
|---|---|---|
| Tid | `2026-07-02T14:25:10` | gör händelsen möjlig att jämföra med andra loggar |
| Nod | `NODE-03` | visar vilken enhet som skapade raden |
| Källa | `RFID` | skiljer RFID, knapp, GNSS eller annat händelseursprung |
| Identitet | `A1B2C3D4` | anger tagg, användare, objekt eller simulerat ID |
| Status | `ACCESS_GRANTED` | gör beslutet synligt utan att tolka rådata |

Samma struktur kan användas även när tiden först bara är `millis()` och identiteten kommer från en knapp. När projektet växer byter du källa, inte hela logikmodellen.


### Förbättringar

När grundversionen fungerar kan du förbättra den:

- byt tid sedan start mot RTC-tid
- lägg till debouncing
- skriv händelser till SD-kort eller FRAM
- lägg till RFID-läsare
- lägg till lista över godkända UID:n
- lägg till display som visar senaste händelse
- lägg till batteristatus från föregående kapitel
- lägg till GNSS-position om systemet är mobilt

## Vanliga misstag

- **Misstag: Att använda `millis()` som kalenderklocka.**
  - **Varför det händer:** `millis()` är enkelt och finns alltid tillgängligt.
  - **Hur man undviker det:** Använd `millis()` för intervaller och timeout, men RTC, NTP eller GNSS för verkliga tidsstämplar.

- **Misstag: Att anta att GNSS fungerar inomhus.**
  - **Varför det händer:** GPS i telefonen verkar ofta fungera överallt eftersom telefonen använder flera hjälptekniker.
  - **Hur man undviker det:** Testa GNSS-modulen utomhus först och skilj mellan satellitposition och andra positionskällor.

- **Misstag: Att lita på RFID-UID som säker autentisering.**
  - **Varför det händer:** Många exempel jämför bara UID mot en lista.
  - **Hur man undviker det:** Beskriv lösningen som identifiering på experimentnivå, inte som säkert passersystem.

- **Misstag: Att glömma backupbatteriet i RTC-modulen.**
  - **Varför det händer:** RTC fungerar under USB-testet och felet syns först efter strömavbrott.
  - **Hur man undviker det:** Testa kallstart utan USB och logga om RTC rapporterar förlorad tid.

- **Misstag: Att blanda lokal tid och UTC i loggar.**
  - **Varför det händer:** Lokal tid är enklast att läsa direkt.
  - **Hur man undviker det:** Spara helst UTC i loggar och konvertera till lokal tid vid visning.

- **Misstag: Att använda ett kort utan tillräckliga seriella portar för GNSS och debug.**
  - **Varför det händer:** En GNSS-modul ser ut som en enkel UART-enhet.
  - **Hur man undviker det:** Välj kort med extra hårdvaru-UART eller planera noga för SoftwareSerial och dess begränsningar.

## Snabb överblick

- Position, tid och identitet är metadata som gör mätningar och händelser mer användbara.
- GNSS passar bäst för absolut position utomhus, men kräver antennläge, fix och ström.
- RTC passar för fristående system som behöver kalender- och klocktid utan nätverk.
- NTP passar bra när systemet redan är uppkopplat.
- GNSS kan också användas som tidskälla.
- RFID/NFC är praktiskt för kortdistansidentifiering, men UID-jämförelse är inte stark autentisering.
- Fast nod-ID, DIP-switchar, chip-ID och konfigurationsfiler är olika sätt att identifiera själva enheten.
- Det viktigaste kodmönstret är tidsstämplad händelse: tid, nod, typ, värde och status.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Ofta 3,3 V-moduler |
| Typiskt gränssnitt | UART, I2C, SPI eller RF-gränssnitt |
| Välj när | plats, tid eller identifiering behövs |
| Välj inte när | projektet bara behöver relativ ordning eller enkel knappinmatning |
| Vanliga fel | dålig antennplacering, fel tidszon, svag RFID-koppling |
| Alternativ att överväga | RTC, GNSS, RFID/NFC, knappkod |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- Använd kapitel 9 när GPS, RFID, NFC eller realtidsklocka inte kommunicerar stabilt med kortet.
- Använd kapitel 32 när position, tid eller identitet ska loggas, visas eller sparas mellan omstarter.
- Använd kapitel 35 när felet gäller intermittent kontakt, fel tid, saknade satelliter eller svårtolkade testvärden.
