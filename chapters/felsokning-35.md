# 35. Felsökning med metod

## Felsökningsöversikt
Felsökning är den färdighet som gör skillnaden mellan ett roligt experiment och ett projekt som fastnar i timmar. När ett Arduino-projekt inte fungerar kan felet ligga i kod, koppling, spänningsnivå, bibliotek, timing, kommunikationsbuss, strömförsörjning, mekanik eller i själva antagandet om hur komponenten fungerar.

En erfaren programmerare är ofta van vid loggar, testfall och reproducerbara fel. I elektronikprojekt behövs samma tänkande, men med fler möjliga felkällor. En sketch kan vara korrekt, samtidigt som en jordledning saknas. En I2C-sensor kan vara rätt adresserad, men sakna pull-up. En motor kan styras med rätt PWM, men ändå få mikrokontrollern att starta om eftersom matningen dippar.

Det här kapitlet ger en metod för att felsöka Arduino-kompatibla system stegvis. Målet är inte att memorera alla fel, utan att bygga ett arbetssätt där du snabbt kan isolera vad som är sant, vad som är osäkert och vad som behöver mätas.

## Förutsättningar

Kapitlet bygger på tidigare delar av boken:

- Kapitel 4 gav elektriska grunder som spänning, ström, jord och nivåskiftning.
- Kapitel 5 till 9 visade digital I/O, analog mätning, timing, avbrott och kommunikationsbussar.
- Kapitel 10 till 16 jämförde kortfamiljer och deras skillnader.
- Kapitel 17 till 34 visade sensorer, aktuatorer, IC-kretsar och strömförsörjning.

I felsökning är en viktig regel att inte ändra för många saker samtidigt. Om du byter kort, bibliotek, koppling och kod i samma försök vet du inte vilken ändring som faktiskt påverkade felet. Gör en ändring, observera resultatet och dokumentera kort vad som hände.

## Felsökning som systematiskt arbetssätt

Ett Arduino-projekt kan ses som en kedja:

1. Strömförsörjning
2. Mikrokontrollerkort
3. Kopplingar
4. Sensorer, aktuatorer eller IC-kretsar
5. Bibliotek och drivrutin
6. Egen applikationskod
7. Kommunikation med dator, nätverk eller andra moduler
8. Mekanisk eller fysisk omgivning

När projektet inte fungerar vill du hitta den svagaste länken i kedjan. Börja därför med sådant som är lätt att bevisa.

En bra första felsökningsordning är:

1. Finns rätt matningsspänning?
2. Finns gemensam jord?
3. Är komponenten kopplad till rätt pinnar?
4. Är pinout läst från rätt kortvariant?
5. Kan kortet köra en enkel sketch?
6. Kan komponenten testas med ett minimalt exempel?
7. Kan bussen eller signalen observeras?
8. Är problemet återkommande eller intermittent?
9. Förändras felet med kabel, matning, belastning eller miljö?

Det här låter enkelt, men i praktiken hoppar många direkt till bibliotek, kod eller forumtrådar. Ofta är felet enklare: fel adress, fel GPIO-nummer, saknad jord, fel spänningsnivå, dålig kontakt i breadboard eller ett kort som startar om när lasten aktiveras.

## Skapa en minimal reproduktion

Inom programmering används ofta begreppet minimal reproduction: ett så litet exempel som möjligt som fortfarande visar felet. Samma princip är mycket värdefull i elektronik.

En minimal reproduktion ska helst ha:

- Ett mikrokontrollerkort.
- En komponent eller modul.
- Kortast möjliga koppling.
- Ett bibliotek eller ingen bibliotekskod alls.
- Tydliga seriella utskrifter.
- En enkel förväntan: exempelvis “sensorn hittas”, “LED blinkar” eller “värdet ändras”.

Om det stora projektet inte fungerar, koppla bort allt som inte behövs. Testa sensorn ensam. Testa displayen ensam. Testa motorn med separat testkod. När varje del fungerar separat kan du börja kombinera dem igen.

### Exempel: diagnostisk startsketch

Den här typen av sketch är enkel men användbar. Den visar att kortet kör kod, att seriell kommunikation fungerar och att `millis()` uppdateras.

```cpp
const unsigned long printIntervalMs = 1000;
unsigned long lastPrintMs = 0;

void setup() {
  Serial.begin(115200);

  while (!Serial && millis() < 3000) {
    // Wait briefly for boards with native USB.
  }

  pinMode(LED_BUILTIN, OUTPUT);

  Serial.println();
  Serial.println("Diagnostic sketch started");
}

void loop() {
  const unsigned long now = millis();

  digitalWrite(LED_BUILTIN, (now / 500) % 2 == 0 ? HIGH : LOW);

  if (now - lastPrintMs >= printIntervalMs) {
    lastPrintMs = now;

    Serial.print("Uptime ms: ");
    Serial.println(now);
  }
}
```

Om den här sketchen inte laddas upp eller inte ger någon utskrift är problemet troligen inte din sensor. Då ska du först felsöka kort, USB-kabel, port, board package, bootloader, seriell hastighet eller utvecklingsmiljö.

## Seriell loggning utan att störa systemet

`Serial.print()` är ofta det första felsökningsverktyget. Det är också ett verktyg som kan förändra tidsbeteendet i programmet. För mycket seriell utskrift kan göra en loop långsam, påverka timing, fylla buffertar eller maskera fel.

Använd seriell loggning med några regler:

- Logga vid viktiga tillståndsbyten, inte varje varv i `loop()`.
- Skriv ut råvärden och tolkade värden tillsammans.
- Lägg till tidsstämplar med `millis()` när timing är relevant.
- Gör loggningen lätt att stänga av.
- Undvik långa utskrifter i interrupt handlers.
- Undvik att använda `delay()` bara för att hinna läsa loggen.

### Exempel: enkel loggmakro

På små Arduino-kort kan avancerade loggsystem vara överdrivna. En enkel flagga räcker långt.

```cpp
const bool debugEnabled = true;

void debugPrint(const char *message) {
  if (debugEnabled) {
    Serial.println(message);
  }
}

void debugValue(const char *label, int value) {
  if (debugEnabled) {
    Serial.print(label);
    Serial.print(": ");
    Serial.println(value);
  }
}
```

Det här är inte ett komplett loggramverk, men det gör att du kan markera vad som är felsökningsutskrifter. I större projekt kan du senare byta ut funktionen mot något mer strukturerat.

### Logga tillstånd, inte bara värden

När ett projekt har flera tillstånd är det ofta mer värdefullt att logga övergångar än att skriva ut allt hela tiden.

```cpp
enum class SystemState {
  Starting,
  WaitingForSensor,
  Running,
  Error
};

SystemState currentState = SystemState::Starting;

void setState(SystemState nextState) {
  if (nextState == currentState) {
    return;
  }

  Serial.print("State change: ");
  Serial.print(static_cast<int>(currentState));
  Serial.print(" -> ");
  Serial.println(static_cast<int>(nextState));

  currentState = nextState;
}
```

I en färdig bokkod skulle du gärna skriva ut läsbara namn i stället för siffror, men principen är viktigare: logga när systemet byter läge. Det gör det lättare att förstå var programmet fastnar.

## Multimetern som första mätinstrument

En multimeter är ofta viktigare än ett avancerat oscilloskop. Den kan snabbt svara på frågor som:

- Finns 5 V eller 3,3 V där du tror?
- Är jord gemensam mellan kort och modul?
- Är batteriet urladdat?
- Är en kabel av?
- Är en knapp normalt öppen eller normalt sluten?
- Finns spänning över lasten när den ska vara aktiv?
- Har du vänt polaritet på en LED eller diod?

### Kontrollera matning

Börja med att mäta mellan VCC och GND på modulen, inte bara på Arduino-kortet. Det är vanligt att matningen finns vid kortet men inte framme vid breadboardens rätta rad.

Mät:

- Mellan kortets GND och kortets 5 V eller 3,3 V.
- Mellan modulens GND och modulens VCC.
- Mellan kortets GND och modulens GND.
- Spänningen när lasten är aktiv, inte bara i vila.

Det sista är viktigt. Ett projekt kan se korrekt ut i vila men falla ihop när en LED-strip, motor, relä eller radiosändare aktiveras.

### Kontrollera kontinuitet

Kontinuitetsläget på multimetern piper när två punkter är elektriskt ihopkopplade. Det är användbart för att kontrollera:

- Att en jumper faktiskt leder.
- Att två breadboard-rader verkligen hänger ihop.
- Att en knapp ansluter när den trycks.
- Att en lödning inte är kall eller bruten.
- Att du inte av misstag har kortslutit två intilliggande rader.

Kontrollera kontinuitet när projektet är strömlöst. Kontinuitetsmätning på ett aktivt system kan ge vilseledande resultat och riskera instrument eller krets.

## Felsökning av digital I/O

Digital I/O är ofta enkelt, men vanliga fel är fortfarande mycket vanliga.

Typiska symtom:

- En ingång växlar slumpmässigt.
- En knapp fungerar tvärtom.
- En LED lyser svagt när den borde vara släckt.
- Ett relä klickar inte.
- En signal fungerar på UNO men inte på ESP32 eller Pico.

### Flytande ingångar

En digital ingång som inte är kopplad till en definierad nivå kan läsa både HIGH och LOW. Lösningen är pull-up eller pull-down.

Testa med en sketch som skriver ut ändringar, inte varje läsning.

```cpp
const int inputPin = 2;
int lastState = HIGH;

void setup() {
  Serial.begin(115200);
  pinMode(inputPin, INPUT_PULLUP);
  Serial.println("Button test with INPUT_PULLUP");
}

void loop() {
  const int state = digitalRead(inputPin);

  if (state != lastState) {
    lastState = state;

    Serial.print("Input changed to: ");
    Serial.println(state == LOW ? "PRESSED" : "RELEASED");
  }
}
```

Med `INPUT_PULLUP` blir knappen vanligtvis aktiv låg: den läser LOW när knappen trycks och kopplar pinnen till GND. Det är inte ett fel, men det måste synas i kodens namn och logik.

### Fel GPIO-nummer

På vissa kort, särskilt NodeMCU och andra ESP-baserade kort, kan silkscreen-namn som `D1` och faktiska GPIO-nummer skilja sig. På andra kort är det tydligare. Felsök därför alltid pinout mot rätt kortvariant.

En enkel pin-test kan hjälpa:

```cpp
const int testPin = LED_BUILTIN;

void setup() {
  pinMode(testPin, OUTPUT);
}

void loop() {
  digitalWrite(testPin, HIGH);
  delay(300);
  digitalWrite(testPin, LOW);
  delay(300);
}
```

Om du testar extern LED, flytta bara en sak åt gången: först pinnen i koden, sedan kabeln, sedan LED-orientering och resistor.

## Felsökning av analog mätning

Analoga problem är ofta mer subtila än digitala. De kan vara “nästan rätt”, brusiga eller beroende av hur du rör vid kablarna.

Typiska symtom:

- Värdet hoppar kraftigt.
- Värdet når aldrig 0 eller max.
- Värdet ändras när USB-kabeln eller datorn byts.
- Värdet är olika på olika kort.
- Sensorn verkar fungera men ger orimliga enheter.

### Läs råvärdet först

Innan du kalibrerar eller filtrerar ska du titta på råvärdet.

```cpp
const int analogPin = A0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  const int raw = analogRead(analogPin);

  Serial.print("raw=");
  Serial.println(raw);

  delay(200);
}
```

Om råvärdet är stabilt kan felet ligga i omräkning, kalibrering eller antagandet om referensspänning. Om råvärdet är instabilt ska du felsöka koppling, jord, impedans, brus, kabeldragning och eventuell filtrering.

### Kontrollera mätområdet

Ett vanligt fel är att anta att ADC:n mäter 0 till 5 V på alla kort. Många moderna kort använder 3,3 V-logik, och vissa analoga ingångar tål inte 5 V. Mät alltid sensorns utspänning och jämför med kortets tillåtna ingångsområde.

Om du använder spänningsdelare, räkna och mät. En spänningsdelare som är rätt på papper kan bli fel om motståndsvärden blandas ihop.

## Felsökning av PWM, motorer och laster

När en last inte beter sig rätt är problemet ofta ström eller drivning, inte själva PWM-koden.

Typiska symtom:

- Mikrokontrollern startar om när motorn startar.
- Servot rycker eller brummar.
- LED-strippen flimrar.
- Reläet klickar men lasten fungerar inte.
- MOSFET:en blir varm.
- USB-porten kopplar bort.

### Separera styrsignal och lastström

Mikrokontrollern ska styra. Den ska sällan driva lasten direkt. Kontrollera:

- Har lasten separat matning när det behövs?
- Har Arduino-kortet och lastens matning gemensam jord?
- Finns skyddsdiod över induktiv last?
- Är MOSFET:en logic-level vid den styrspänning du använder?
- Är servots eller motorns strömbehov rimligt för matningen?
- Finns avkopplingskondensator nära lasten?

Ett bra felsökningsgrepp är att först ersätta lasten med en LED och resistor. Om styrsignalen fungerar med LED men inte med motor är koden troligen inte huvudproblemet.

## Felsökning av I2C

I2C är populärt eftersom det kräver få ledningar, men det är också en vanlig källa till felsökning. Bussen är känslig för adresser, pullups, kabeldragning och nivåer.

Typiska symtom:

- I2C-scanner hittar ingen enhet.
- Scannern hittar en adress men biblioteket fungerar inte.
- Det fungerar med en sensor men inte med två.
- Det fungerar på kort kabel men inte i kapsling.
- Värdena blir `nan`, noll eller fasta maxvärden.

### I2C-scanner

En I2C-scanner är ett standardverktyg. Den bevisar inte att sensorn fungerar fullt ut, men den visar om en enhet svarar på bussen.

```cpp
#include <Wire.h>

void setup() {
  Serial.begin(115200);

  while (!Serial && millis() < 3000) {
    // Wait briefly for native USB boards.
  }

  Wire.begin();

  Serial.println("I2C scanner started");
}

void loop() {
  byte foundCount = 0;

  for (byte address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    const byte error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("Found I2C device at 0x");

      if (address < 16) {
        Serial.print("0");
      }

      Serial.println(address, HEX);
      foundCount++;
    }
  }

  if (foundCount == 0) {
    Serial.println("No I2C devices found");
  }

  Serial.println("Scan complete");
  delay(3000);
}
```

Om scannern inte hittar något, kontrollera i denna ordning:

1. VCC och GND på modulen.
2. SDA och SCL på rätt pinnar för kortet.
3. Gemensam jord.
4. Rätt spänningsnivå.
5. Pull-up-motstånd.
6. Kabelns längd och kvalitet.
7. Om modulen har alternativ adress som styrs med lödbygel.
8. Om enheten behöver särskild startsekvens eller wake-up.

Om scannern hittar enheten men biblioteket inte fungerar kan felet vara fel sensormodell, fel adress i koden, fel bibliotek, gammal biblioteksversion eller en modul som bara är kompatibel på ytan.

### Flera I2C-enheter

När två I2C-enheter inte fungerar tillsammans är adresskrock en vanlig orsak. Två enheter med samma fasta adress kan inte normalt sitta på samma I2C-buss utan multiplexer eller adressändring.

Andra möjliga orsaker:

- För många pullups parallellt.
- För lång buss.
- Blandning av 5 V och 3,3 V utan nivåskiftning.
- En defekt modul som håller SDA eller SCL låg.
- Olika bibliotek som konfigurerar bussen på oväntade sätt.

Ett praktiskt test är att ansluta en enhet i taget och köra scannern efter varje ändring.

## Felsökning av SPI

SPI är ofta snabbare än I2C men kräver fler ledningar. Det finns ingen standardiserad adressökning på samma sätt som I2C-scanner, så felsökningen blir mer kopplings- och signalspecifik.

Typiska symtom:

- Displayen visar ingenting.
- SD-kortet initieras inte.
- En enhet fungerar ensam men inte med en annan SPI-enhet.
- Data blir korrupt.
- Fel enhet reagerar.

Kontrollera:

- MOSI, MISO, SCK och CS mot rätt pinout.
- Att varje SPI-enhet har egen chip select.
- Att inaktiva CS-pinnar hålls i rätt läge.
- Att SPI-läge och hastighet passar komponenten.
- Att nivåskiftning används vid behov.
- Att kablarna är korta, särskilt vid hög hastighet.

En bra metod är att börja med bibliotekets enklaste exempel och sänka SPI-hastigheten om biblioteket tillåter det. Om det börjar fungera vid lägre hastighet är problemet ofta kabeldragning, signalintegritet, breadboard eller nivåskiftning.

## Felsökning av UART och seriella moduler

UART används ofta för GPS, Bluetooth-moduler, vissa sensorer, seriella displayer och kommunikation mellan kort.

Typiska symtom:

- Bara konstiga tecken visas.
- Ingen data kommer.
- Data kommer ibland men tappas.
- Uppladdning till kortet störs.
- Modulen svarar inte på kommandon.

Kontrollera:

- TX ska normalt gå till RX och RX till TX.
- Baud rate måste stämma.
- GND måste vara gemensam.
- Spänningsnivån måste vara kompatibel.
- Vissa kort delar UART med USB-seriell kommunikation.
- Vissa moduler behöver `\r\n` efter kommandon.
- Vissa moduler startar i olika lägen beroende på boot-pinnar.

En enkel metod är att först läsa rå inkommande data och skriva ut bytevärden, inte bara tolka dem som text. Då ser du om data faktiskt kommer.

## När logikanalysatorn är rätt verktyg

En logikanalysator visar digitala signaler över tid. Den är mycket användbar för I2C, SPI, UART, PWM, pulser och vissa timingproblem. Den visar däremot normalt inte analog kvalitet som brus, långsam flank eller spänningsnivåns exakta form.

Använd logikanalysator när:

- Du vill se om en buss faktiskt skickar data.
- Du vill kontrollera om rätt adress används på I2C.
- Du vill se om UART har rätt baud rate.
- Du vill se om en interrupt-signal kommer.
- Du vill mäta pulslängd eller period.
- Du misstänker att två enheter pratar samtidigt.

En billig logikanalysator kan vara tillräcklig för många Arduino-projekt, men kontrollera alltid dess tillåtna ingångsspänning. Många är gjorda för 3,3 V/5 V digital logik, men det ska inte antas utan kontroll.

## När oscilloskopet är rätt verktyg

Ett oscilloskop visar spänning över tid. Det är rätt verktyg när signalens form spelar roll.

Använd oscilloskop när:

- Du vill se spänningsdippar vid motorstart.
- Du misstänker brus på matningen.
- Du vill se flankhastighet, ringing eller översläng.
- En analog sensor ger instabila värden.
- PWM-signalen behöver verifieras elektriskt.
- En I2C- eller SPI-buss ser digitalt korrekt ut men ändå fungerar opålitligt.

För många Arduino-projekt räcker multimeter och logikanalysator långt, men oscilloskop blir värdefullt när problemet är elektriskt snarare än logiskt.

## Bibliotek, versioner och exempel

Bibliotek är en stor styrka i Arduino-ekosystemet, men de kan också skapa felsökningsproblem.

Vanliga bibliotekskällor till fel:

- Fel bibliotek med liknande namn.
- Biblioteket stöder inte exakt sensorvariant.
- Exemplet är skrivet för annan kortfamilj.
- Standardpinnar i exemplet stämmer inte med ditt kort.
- Biblioteket antar annan I2C-adress.
- Biblioteksversionen har ändrats sedan en guide skrevs.
- Två bibliotek använder samma timer, interrupt eller resurs.

När ett bibliotek inte fungerar, gör så här:

1. Kör bibliotekets enklaste exempel utan egen kod.
2. Kontrollera att rätt modellnamn används.
3. Skriv ut vilken adress, pinne eller buss som används.
4. Kontrollera öppna issues eller dokumentation om kortfamiljen är modern eller ovanlig.
5. Testa en äldre eller nyare version om problemet verkar versionsspecifikt.
6. Läs initieringskoden för att se vilka antaganden biblioteket gör.

Det är särskilt viktigt på ESP32, ESP8266, Pico/RP2040 och andra kort där Arduino-API:t finns, men hårdvaran skiljer sig från klassisk UNO.

## Felsökning av strömförsörjning och omstarter

Om ett projekt startar om slumpmässigt är strömförsörjningen en huvudmisstänkt.

Typiska symtom:

- Seriell monitor visar startmeddelandet flera gånger.
- ESP-kort skriver boot-meddelanden oväntat.
- Displayen blinkar till och slocknar.
- Sensorvärden blir fel när motor eller Wi-Fi startar.
- Projektet fungerar via USB men inte på batteri.
- Projektet fungerar på labbbänk men inte i kapsling.

Kontrollera:

- Strömkällans maxström.
- Spänningsregulatorns kapacitet och värme.
- Kabellängd och kabelarea.
- Spänningsfall över breadboard, jumperkablar och kontakter.
- Kondensatorer nära kort och last.
- Separat matning för motorer, servon och LED-strippar.
- Gemensam jord mellan styrkort och extern matning.

En bra testmetod är att logga uppstarten tydligt.

```cpp
void setup() {
  Serial.begin(115200);
  delay(500);

  Serial.println();
  Serial.println("Boot marker: system started");
}

void loop() {
  static unsigned long lastPrintMs = 0;
  const unsigned long now = millis();

  if (now - lastPrintMs >= 1000) {
    lastPrintMs = now;

    Serial.print("Alive at ");
    Serial.print(now);
    Serial.println(" ms");
  }
}
```

Om “Boot marker” visas igen utan att du laddat upp ny kod eller tryckt reset har kortet startat om. Då bör du felsöka matning, watchdog, brownout, resetpinne och eventuell kod som orsakar omstart.

## Intermittenta fel

Intermittenta fel är de svåraste eftersom de inte alltid går att framkalla. De beror ofta på kontaktproblem, temperatur, vibration, strömspikar, brus, minnesproblem eller timing.

Arbeta så här:

- Försök hitta ett sätt att reproducera felet.
- Logga tidpunkt, tillstånd och senaste händelse.
- Rör försiktigt vid kablar och kontakter för att se om felet påverkas.
- Testa annan strömkälla.
- Testa kortare kablar.
- Testa en komponent i taget.
- Minska klockhastighet eller busshastighet om det gäller kommunikation.
- Låt projektet köra längre med periodiska hälsomeddelanden.

Ett enkelt heartbeat-meddelande kan visa att programmet fortfarande lever även när huvudfunktionen inte fungerar.

```cpp
void printHeartbeat() {
  static unsigned long lastHeartbeatMs = 0;
  const unsigned long now = millis();

  if (now - lastHeartbeatMs >= 5000) {
    lastHeartbeatMs = now;

    Serial.print("Heartbeat, uptime=");
    Serial.println(now);
  }
}
```

Anropa `printHeartbeat()` från `loop()`. Om heartbeat fortsätter men sensordata stannar är felet troligen i sensorn, bussen eller biblioteket. Om heartbeat också stannar kan programmet blockera, krascha eller starta om.

## Diagnostiska testsketcher som verktygslåda

Det är klokt att ha en mapp med små testsketcher som du återanvänder mellan projekt.

Bra testsketcher att ha:

- Blink för valfri pinne.
- Seriell startdiagnostik.
- Knapp med `INPUT_PULLUP`.
- Analog råvärdesläsning.
- PWM-test.
- Servo sweep med extern matningspåminnelse.
- I2C-scanner.
- Enkel SPI-display- eller SD-initiering.
- UART echo eller rå byte-logg.
- Batteri-/spänningsmätning.
- Watchdog- eller omstartsmarkör.
- Minimal Wi-Fi-anslutning för ESP-kort.

### Typiska minimisketcher för felsökning

| Problem | Minimisketch |
|---|---|
| Kortet verkar inte köra | Diagnostisk startsketch med seriell utskrift och heartbeat |
| I2C-modul saknas | I2C-scanner med tydlig adressutskrift |
| Analogt värde verkar fel | Råvärdesläsare med min, max och medelvärde |
| Knapp beter sig slumpmässigt | Pullup- eller ingångstest med stabil händelselogg |
| PWM beter sig olika på kort | Enkel PWM-test med känd pinne och fast frekvensnivå |
| Matningen verkar svag | Spänningslogg eller batterimonitor utan övriga laster |

Spara gärna korta kommentarer i varje testsketch om vilken koppling den förutsätter. En testsketch utan sparad pinout blir snabbt svår att återanvända.

## Felsökningsmönster: I2C-problem metodiskt

Det här felsökningsmönstret visar en metodisk ordning för I2C-problem. Använd en valfri I2C-sensor eller I2C-display, exempelvis BME280, BMP280, OLED-display eller I/O-expander.

### Steg 1: Kontrollera antaganden

Kontrollera:

- Kortmodell.
- Logiknivå.
- Vilka pinnar som är SDA och SCL.
- Modulens matningsspänning.
- Förväntad I2C-adress.
- Vilket bibliotek du tänker använda.

### Steg 2: Mät matningen

Mät VCC och GND på modulen medan den är inkopplad. Kontrollera också att kortets GND och modulens GND verkligen är gemensamma.

### Steg 3: Kör I2C-scanner

Ladda upp I2C-scannern från tidigare i kapitlet. Notera om adressen hittas.

- Om ingen adress hittas: felsök koppling, matning, SDA/SCL och pullups.
- Om fel adress hittas: kontrollera modulvariant och adressbyglar.
- Om rätt adress hittas: gå vidare till bibliotekets enklaste exempel.

### Steg 4: Kör biblioteksexempel

Kör bibliotekets enklaste exempel utan att blanda in egen projektkod. Ändra bara adress och pinnar om det behövs.

### Steg 5: Integrera i egen kod

När exemplet fungerar, flytta in minsta möjliga kod i ditt eget projekt. Lägg till loggning runt initiering och läsning.

### Steg 6: Sammanfatta vad som faktiskt ändrades

Skriv en kort rapport:

- Vad var förväntat?
- Vad hände först?
- Vilka mätningar gjordes?
- Vilken ändring löste problemet?
- Hur kan samma fel upptäckas snabbare nästa gång?

Syftet är att bygga erfarenhet som går att återanvända, inte bara lösa dagens fel.

## Vanliga misstag

- **Misstag: Att börja med att ändra koden när felet är elektriskt.**
  - Varför det händer: Programmerare är vana vid att kod är den primära felkällan.
  - Hur man undviker det: Mät matning, jord och signalvägar innan du ändrar större delar av koden.

- **Misstag: Att ändra flera saker samtidigt.**
  - Varför det händer: Det känns effektivt att byta bibliotek, koppling och kort i samma försök.
  - Hur man undviker det: Gör en ändring åt gången och skriv ner resultatet.

- **Misstag: Att lita på färgen på jumperkablar.**
  - Varför det händer: Röd brukar betyda plus och svart brukar betyda jord, men kablar är bara kablar.
  - Hur man undviker det: Följ faktisk koppling och mät vid osäkerhet.

- **Misstag: Att använda fel pinout för kortvarianten.**
  - Varför det händer: Många Arduino-kompatibla kort har liknande namn men olika pinnummer och specialpinnar.
  - Hur man undviker det: Kontrollera pinout för exakt kortmodell, särskilt för ESP8266, ESP32, Pico och småkort.

- **Misstag: Att ignorera strömspikar.**
  - Varför det händer: Projektet fungerar i vila och ser därför korrekt ut.
  - Hur man undviker det: Mät eller observera beteendet när motorer, servon, radio eller LED-strippar aktiveras.

- **Misstag: Att felsöka ett stort system utan minimal testsketch.**
  - Varför det händer: Det känns som ett steg bakåt att koppla bort funktioner.
  - Hur man undviker det: Isolera komponenten och bevisa att den fungerar ensam innan du felsöker integrationen.

## Riskkontroll när något beter sig fel

När ett projekt beter sig oväntat bör du först avgöra om felet kan skada komponenter.

- Bryt matningen om något blir varmt, luktar, låter onormalt eller får kablar att mjukna.
- Koppla bort motorer, reläer, LED-strippar och andra större laster innan du felsöker logik.
- Gå tillbaka till USB-matning eller strömbegränsad matning om det är möjligt.
- Testa en modul i taget innan hela systemet körs igen.
- Mät spänning vid kortet, inte bara vid adaptern.
- Kontrollera polaritet och jord innan du laddar upp ny kod.
- Dokumentera vilket test som var säkert och vilket som gav fel.

Felsökning handlar inte bara om att hitta felet. Den ska också minska risken medan du letar.

## Felsökningschecklista

- Börja med matning, jord, pinout och minimal sketch innan du misstänker avancerade kodfel.
- Ändra en sak i taget och kontrollera effekten innan du går vidare.
- Använd seriell loggning för tillstånd och felvägar, men undvik så mycket utskrift att timing påverkas.
- Använd multimeter först för spänning, jord och kontinuitet.
- Använd I2C-scanner, rå analog läsning och enkla pin-tester som återanvändbara diagnostiska verktyg.
- Använd logikanalysator när problemet handlar om digitala protokoll eller timing.
- Använd oscilloskop när problemet handlar om signalform, brus eller spänningsdippar.
- Vid omstarter, ryckiga motorer eller störda sensorer: börja med strömförsörjning och gemensam jord.
- Vid en modul som inte reagerar: börja med pinout, minimal sketch och bibliotekets enklaste exempel.
- Vid analoga mätfel: börja med råvärden, mätområde, referensspänning och brus.
- Vid intermittent fel: försök först göra felet reproducerbart.

## Relaterat

- När felet verkar bero på ström, jord eller omstarter, börja med kapitel 34.
- När felet gäller I2C, SPI, UART eller 1-Wire, använd kapitel 9 som första kontrollpunkt.
- När felet bara uppstår när flera delar kopplas ihop, jämför med integrationsordningen i kapitel 37.
