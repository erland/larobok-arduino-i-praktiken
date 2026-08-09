# 27. Ljud, mikrofoner och enkla signalmätningar

## Signal- och sensoröversikt
I kapitel 19 använde vi ljud som utgång: buzzers, tonmönster och enkla varningssignaler. I det här kapitlet vänder vi på riktningen. Nu ska Arduino-systemet lyssna på sin omgivning.

Ljudsensorer kan användas till mycket, men de är också lätta att överskatta. En billig ljudsensor kan ofta svara på frågan “hände något ljudligt nu?”, men den kan sällan svara exakt på “hur många decibel är det här?” eller “vilket ljud är det?”. En mikrofonmodul med analog utgång kan ge en signal som följer ljudets variationer, men signalen är snabb, brusig och beroende av förstärkning, matning, placering och akustisk miljö. En digital I2S-mikrofon kan ge bättre rådata, men kräver ett kraftigare kort och mer programlogik.

Det här kapitlet hjälper dig att välja rätt nivå av ljudmätning:

- enkel ljudtrigger
- analog ljudnivåindikator
- relativ ljudnivå över tid
- ljudhändelser med tröskel och tidsfönster
- digital mikrofondata med I2S på kraftigare kort
- KY-037-liknande ljudsensormoduler med analog och digital utgång
- gränsdragning mellan Arduino-projekt och riktig ljudanalys

Målet är inte att bygga en professionell ljudmätare. Målet är att förstå vilka ljudmoduler som passar i Arduino-projekt, hur du kopplar dem, hur du tolkar signalerna och när du bör välja en annan metod.

Kapitlet fungerar som stöd när du behöver välja mellan ljudtrigger, analog mikrofonmodul och digital mikrofon, läsa relativa ljudnivåer och undvika vanliga feltolkningar kring brus, trösklar, decibel och sampling.

## Förutsättningar

Du bör känna igen följande från tidigare kapitel:

- digital ingång och intern pull-up
- analog läsning och ADC-upplösning
- filtrering med medelvärde eller enkel lågpasslogik
- trösklar och hysteresis
- icke-blockerande kod med `millis()`
- seriell plotter som verktyg för att se mätvärden över tid

Du behöver också ha en tydlig skillnad i huvudet mellan ljud som människor uppfattar och signaler som mikrokontrollern mäter. En mikrofonmodul ger inte “ljud” i sig. Den ger en elektrisk signal som påverkas av ljudtryck, förstärkning, modulens konstruktion och din kod.

## Ljud som elektrisk signal

Ljud är tryckvariationer i luft. En mikrofon omvandlar dessa variationer till en elektrisk signal. För en mikrokontroller är den signalen bara en spänning som varierar över tid.

Det skapar tre praktiska problem.

För det första är ljudsignalen snabb. En mänsklig röst eller ett klick innehåller variationer som sker mycket fortare än typiska temperatur- eller ljussensorvärden. Om du läser för långsamt missar du detaljer.

För det andra är signalen ofta centrerad runt en vilonivå. På många analoga mikrofonmoduler ligger tystnad inte nära 0 V, utan runt ungefär halva matningsspänningen. Ljudet gör att signalen svänger upp och ned runt denna mittnivå.

För det tredje är ljudmiljöer brusiga. Fläktar, tangentbord, motorer, handrörelser, kablar och matningsbrus kan påverka mätningen. Därför bör ett Arduino-projekt sällan reagera direkt på ett enskilt analogt råvärde.

En bra grundregel är:

> Mät inte ljud med ett enskilt värde. Mät ljud som förändring över ett kort tidsfönster.

Det betyder att du ofta läser många värden under exempelvis 20 till 100 millisekunder och beräknar ett sammanfattande mått.

## Vanliga typer av ljudmoduler

Ljudmoduler för Arduino-projekt kan delas in i några praktiska kategorier.

| Typ | Typiskt gränssnitt | Passar för | Begränsning |
|---|---|---|---|
| Digital ljudtrigger | Digital utgång | Upptäcka ljudhändelse | Ger inte ljudnivå eller ljudform |
| Analog mikrofonmodul | Analog utgång | Relativ ljudnivå och enkla ljudhändelser | Kräver sampling och filtrering |
| Analog modul med digital tröskel | Analog och digital utgång | Snabba tester med justerbar tröskel | Tröskelpotentiometer kan vara svår att kalibrera |
| I2S-mikrofon | Digital ljudström | Mer seriös ljudsampling på ESP32/RP2040-liknande kort | Mer komplex kod och mer data |
| Färdig ljudnivåmodul | Analog, I2C eller seriellt | Relativ eller ibland kalibrerad ljudnivå | Kontrollera noga vad modulen faktiskt mäter |

En enkel modul med en liten mikrofon och justerbar potentiometer kan vara utmärkt för att detektera klapp, knackning eller hög ljudnivå. Den är däremot inte automatiskt en decibelmätare.

## KY-037 och vanliga ljudsensormoduler

KY-037 är en vanlig mikrofonmodul i Arduino-kit och sortiment med billiga sensormoduler. Den finns i flera närbesläktade varianter, men grundidén är ofta densamma: en liten mikrofon, enkel förstärkning, en potentiometer och ibland både analog och digital utgång.

Den analoga utgången kan användas för att se en relativ ljudnivå eller bygga en enkel indikator. Den digitala utgången fungerar mer som en tröskelsignal: modulen växlar när ljudet passerar en inställd nivå. Det gör KY-037 användbar för experiment som klappdetektering, enkel ljudnivåindikering eller “något lät”-händelser.

Behandla däremot inte KY-037 som en riktig inspelningsmikrofon eller professionell ljudmätare. Modulen är ofta brusig, känslig för placering och svår att kalibrera exakt. Den passar bäst när projektet behöver upptäcka enkla ljudhändelser, inte analysera ljudinnehåll.

Kontrollera särskilt:

- vilken pinne som är analog utgång och vilken som är digital utgång
- hur potentiometern påverkar den digitala tröskeln
- om modulen matas med 5 V eller 3,3 V
- om signalnivån passar kortets ADC och digitala ingångar
- om omgivningsljud ger falska händelser

En bra testordning är att först läsa den analoga utgången i seriell plotter, sedan justera potentiometern och därefter testa den digitala utgången med en enkel LED eller seriell utskrift.

## Välj rätt ljudlösning

### Digital ljudtrigger

En digital ljudtrigger ger ofta HIGH eller LOW när ljudnivån passerar en tröskel. Tröskeln ställs ibland med en liten potentiometer på modulen.

Välj en digital ljudtrigger när:

- du bara behöver veta om något ljudligt hände
- du vill väcka ett system eller starta en sekvens
- du vill undvika analog signalbehandling
- du accepterar att tröskeln är ungefärlig

Välj något annat när:

- du behöver jämföra ljudnivåer
- du vill se hur starkt ljudet var
- du vill skilja mellan olika ljudtyper
- du behöver reproducerbara mätvärden

En digital ljudtrigger bör behandlas ungefär som en knapp eller PIR-sensor: den ger en händelse, inte en exakt mätning.

### Analog mikrofonmodul

En analog mikrofonmodul ger en spänning som varierar med ljudet. Ibland är signalen förstärkt och centrerad runt halva matningen. Ibland är modulen mer av en enkel “sound sensor” med begränsad dokumentation.

Välj en analog mikrofonmodul när:

- du vill skapa en relativ ljudnivåindikator
- du vill visualisera ljud med seriell plotter
- du vill styra LED eller annan återkoppling med ljudstyrka
- du vill experimentera med peak, medelvärde och trösklar

Välj något annat när:

- du behöver exakt ljudnivå i dB
- du behöver frekvensanalys
- du behöver känna igen tal eller ljudmönster
- du vill sampla ljud med hög kvalitet

För Arduino UNO-liknande kort är analog mikrofonmodul ofta den enklaste vägen in, men ADC-hastighet, upplösning och brus begränsar vad du kan göra.

### I2S-mikrofon

I2S är ett digitalt ljudgränssnitt. En I2S-mikrofon skickar digitala ljuddata till mikrokontrollern. Det passar bäst på kort som ESP32, vissa RP2040/RP2350-baserade kort och andra kraftigare plattformar med bra stöd i bibliotek eller core.

Välj I2S-mikrofon när:

- du vill ha digital ljuddata i stället för analog ADC-läsning
- du använder ESP32 eller liknande kort
- du vill göra enklare frekvensanalys, ljudloggning eller mer kontrollerad sampling
- du accepterar mer komplex kod

Välj enklare analog modul när:

- du bara behöver ljudhändelser
- du vill göra ett snabbt experiment
- du använder ett klassiskt UNO/Nano-kort
- du inte vill hantera buffertar och samplingsfrekvens

I2S är kraftfullt, men det gör inte automatiskt projektet enklare.

## Elektriska krav och koppling

En ljudmodul kan se enkel ut, men kontrollera alltid fyra saker innan du kopplar den:

- matningsspänning
- signalnivå på utgången
- om utgången är analog, digital eller båda
- om modulen kräver 3,3 V-logik eller tolererar 5 V

Många mikrofonmoduler fungerar med 3,3 V eller 5 V matning, men det betyder inte alltid att alla signaler är säkra för alla kort. Om du använder ESP32, ESP8266, Raspberry Pi Pico eller många småkort ska du normalt tänka 3,3 V-logik.

För en analog mikrofonmodul är en vanlig koppling:

| Modul | Arduino UNO | ESP32/Pico-liknande kort |
|---|---|---|
| VCC | 5 V eller 3,3 V enligt modul | 3,3 V om modulen stöder det |
| GND | GND | GND |
| AO | A0 | ADC-kompatibel pinne |
| DO | Valfri digital pinne | Valfri säker digital pinne |

Om modulen har både `AO` och `DO` kan du börja med `AO` för att förstå signalen och sedan använda `DO` om du vill ha enkel händelsedetektering.

## Råvärde, mittnivå och amplitud

Anta att en analog mikrofonmodul är kopplad till `A0` på ett UNO-liknande kort. Om du skriver ut råvärden kan du se att tystnad kanske ligger runt 500 till 530 i stället för nära 0.

Det beror ofta på att signalen är biaserad runt en mittnivå. Ljud gör att värdet svänger upp och ned runt mitten.

Det mest användbara första måttet är därför inte råvärdet utan avvikelsen från mittnivån:

```cpp
const int micPin = A0;
const int midLevel = 512;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int raw = analogRead(micPin);
  int amplitude = abs(raw - midLevel);

  Serial.print(raw);
  Serial.print(',');
  Serial.println(amplitude);

  delay(5);
}
```

Det här är pedagogiskt, men inte tillräckligt robust. Mittnivån kan variera mellan moduler, matningsspänning och kort. I praktiska projekt bör du uppskatta mittnivån över tid eller mäta min och max under ett kort fönster.

## Mät ljud över ett tidsfönster

En enkel metod är att under ett kort tidsfönster läsa många värden och spara minsta och största värde. Skillnaden mellan max och min ger ett grovt “peak-to-peak”-mått.

```cpp
const int micPin = A0;
const unsigned long sampleWindowMs = 50;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int signalMin = 1023;
  int signalMax = 0;

  unsigned long start = millis();

  while (millis() - start < sampleWindowMs) {
    int sample = analogRead(micPin);

    if (sample < signalMin) {
      signalMin = sample;
    }

    if (sample > signalMax) {
      signalMax = sample;
    }
  }

  int peakToPeak = signalMax - signalMin;

  Serial.println(peakToPeak);
}
```

Detta är ett användbart experimentmått. Det säger inte exakt ljudtryck, men det ger ett relativt värde som ofta räcker för LED-indikatorer, tröskellogik och jämförelser i samma miljö.

Viktiga begränsningar:

- värdet beror på mikrofonmodulen
- värdet beror på avstånd och riktning
- värdet beror på matningsspänning och ADC
- värdet kan påverkas av mekaniskt brus och vibrationer
- värdet är inte kalibrerade decibel

## Tröskel, hysteresis och tidsfönster

Om du vill reagera på ljud ska du undvika kod som säger “om råvärdet är över X, gör något”. Det ger lätt fladdrande beteende.

Använd hellre tre nivåer:

- ett ljudmått från ett tidsfönster
- en tröskel för att aktivera
- hysteresis eller timeout för att stanna kvar i aktivt läge en kort stund

```cpp
const int micPin = A0;
const int ledPin = 9;

const unsigned long sampleWindowMs = 40;
const unsigned long holdTimeMs = 300;

const int onThreshold = 80;
const int offThreshold = 45;

bool soundActive = false;
unsigned long lastLoudSoundMs = 0;

int readPeakToPeak() {
  int signalMin = 1023;
  int signalMax = 0;

  unsigned long start = millis();

  while (millis() - start < sampleWindowMs) {
    int sample = analogRead(micPin);

    if (sample < signalMin) {
      signalMin = sample;
    }

    if (sample > signalMax) {
      signalMax = sample;
    }
  }

  return signalMax - signalMin;
}

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int level = readPeakToPeak();
  unsigned long now = millis();

  if (level >= onThreshold) {
    soundActive = true;
    lastLoudSoundMs = now;
  }

  if (soundActive && level < offThreshold && now - lastLoudSoundMs > holdTimeMs) {
    soundActive = false;
  }

  digitalWrite(ledPin, soundActive ? HIGH : LOW);

  Serial.print(level);
  Serial.print(',');
  Serial.println(soundActive ? 100 : 0);
}
```

Detta mönster är viktigare än exakt tröskelvärde. Trösklarna måste nästan alltid justeras efter modul och miljö.

## Digital ljudtrigger som händelse

Om din modul har digital utgång kan den användas som en enklare händelsesensor. Då gör modulen själv tröskeljämförelsen.

```cpp
const int soundPin = 2;
const int ledPin = 13;

bool eventActive = false;
unsigned long lastEventMs = 0;
const unsigned long holdTimeMs = 250;

void setup() {
  pinMode(soundPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  unsigned long now = millis();

  if (digitalRead(soundPin) == HIGH) {
    eventActive = true;
    lastEventMs = now;
    Serial.println("Sound event");
  }

  if (eventActive && now - lastEventMs > holdTimeMs) {
    eventActive = false;
  }

  digitalWrite(ledPin, eventActive ? HIGH : LOW);
}
```

Vissa moduler ger aktiv LOW i stället för aktiv HIGH. Testa därför alltid modulen med seriell utskrift innan du bygger systemlogik runt den.

Digitala ljudtriggers passar bra för:

- klappdetektering på experimentnivå
- enkel larmstart
- spelinteraktion
- test av akustisk händelse
- väckning av annan logik

De passar sämre för:

- nivåmätning
- jämförbar ljudanalys
- klassificering av ljud
- miljöövervakning med krav på dokumenterad noggrannhet

## Relativ ljudnivå med LED-indikator

Ett vanligt experiment är att låta ljudnivån styra LED-ljusstyrka. Här är det viktigt att inte mappa råvärdet direkt. Använd ett ljudmått, filtrera det och mappa sedan till PWM.

```cpp
const int micPin = A0;
const int ledPin = 9;

float filteredLevel = 0.0;
const float alpha = 0.2;

int readPeakToPeak() {
  int signalMin = 1023;
  int signalMax = 0;

  unsigned long start = millis();

  while (millis() - start < 30) {
    int sample = analogRead(micPin);

    if (sample < signalMin) {
      signalMin = sample;
    }

    if (sample > signalMax) {
      signalMax = sample;
    }
  }

  return signalMax - signalMin;
}

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int level = readPeakToPeak();
  filteredLevel = filteredLevel + alpha * (level - filteredLevel);

  int brightness = map((int)filteredLevel, 0, 180, 0, 255);
  brightness = constrain(brightness, 0, 255);

  analogWrite(ledPin, brightness);

  Serial.print(level);
  Serial.print(',');
  Serial.print(filteredLevel);
  Serial.print(',');
  Serial.println(brightness);
}
```

I seriell plotter kan du se skillnaden mellan rått peak-to-peak-värde och filtrerad nivå. Det ger bra intuition för varför direkta trösklar ofta fungerar dåligt.

## Om decibel och kalibrering

Decibel är en logaritmisk skala. När människor säger “mäta ljudnivå” menar de ofta dB SPL, alltså ljudtrycksnivå relativt en definierad referens. En vanlig billig mikrofonmodul ger normalt inte ett kalibrerat dB-värde.

För att mäta ljudnivå mer seriöst behöver du bland annat:

- mikrofon med känd känslighet
- stabil förstärkning
- känd frekvensrespons
- korrekt sampling
- lämplig viktning om du vill efterlikna mänsklig hörsel
- kalibrering mot referenskälla
- kontrollerad mekanisk placering

Det betyder inte att enkla Arduino-projekt är värdelösa. Tvärtom. De är utmärkta för relativ ljudnivå: tystare eller starkare, aktivitet eller ingen aktivitet, jämförelse i samma miljö med samma sensor.

Skriv därför hellre:

- “relativ ljudnivå”
- “ljudaktivitet”
- “akustisk händelse”
- “peak-to-peak-värde”
- “filtrerat ljudmått”

än “decibel”, om du inte faktiskt har kalibrerat systemet.

## Samplingshastighet och aliasing

När du samplar en analog signal läser du värden med en viss hastighet. Om signalen varierar snabbare än din sampling kan du få missvisande resultat. Detta kallas aliasing.

I många Arduino-projekt behöver du inte förstå all signalteori, men du behöver känna till konsekvensen:

- långsam sampling räcker för ljudhändelser
- snabbare sampling krävs för frekvensinnehåll
- `delay()` förstör ofta kontrollerad sampling
- seriella utskrifter kan göra sampling långsammare
- klassiska UNO-kort har begränsad ADC- och CPU-kapacitet

Om målet är att veta om ett ljud inträffade är ett kort mätfönster med peak-to-peak ofta tillräckligt. Om målet är att analysera tonhöjd, frekvens eller ljudmönster bör du välja ett kraftigare kort och en mer lämplig ljudingång.

## I2S-mikrofoner på kraftigare kort

Med ESP32 och vissa andra kort kan du använda I2S-mikrofoner. De ger digitala ljuddata och kan vara ett bättre val när du vill göra mer än enkel analog nivådetektering.

En typisk I2S-mikrofon har pinnar som:

| Pinne | Funktion |
|---|---|
| VCC | Matning, ofta 3,3 V |
| GND | Jord |
| BCLK/SCK | Bit clock |
| LRCLK/WS | Word select eller left/right clock |
| DOUT/SD | Digital ljuddata ut från mikrofonen |
| L/R | Val av vänster/höger kanal på vissa moduler |

I2S-koppling är mer känslig för rätt pinout, bibliotek och kortstöd än en analog ljudsensor. Läs alltid dokumentationen för både kortet och mikrofonmodulen.

För den här boken räcker det att se I2S som nästa nivå:

- analog mikrofonmodul för enkla tester
- I2S-mikrofon för digital ljudsampling
- specialiserad ljudplattform när projektet blir ljudanalys på riktigt

## Referensmönster: ljudstyrd statusindikator

Det här mönstret visar en indikator som reagerar på ljudnivå men inte fladdrar vid små variationer. Mönstret kan göras med en analog mikrofonmodul och en LED.

### Det här används i exemplet

- Arduino UNO, Nano, ESP32, Pico eller annat kompatibelt kort
- analog mikrofonmodul med `AO`
- LED med seriemotstånd, eller inbyggd LED för enklare test
- kopplingskablar
- seriell monitor eller seriell plotter

### Koppling

För UNO-liknande kort:

| Mikrofonmodul | Arduino |
|---|---|
| VCC | 5 V eller 3,3 V enligt modul |
| GND | GND |
| AO | A0 |

LED kan kopplas till pinne 9 via lämpligt seriemotstånd, eller så kan du först använda inbyggd LED på pinne 13 utan PWM.

För 3,3 V-kort bör du mata modulen på 3,3 V om modulen stöder det och kontrollera att analogutgången inte överskrider kortets ADC-område.

### Steg 1: Se råvärden

Ladda först upp ett program som skriver ut råvärden. Använd seriell plotter och gör ljud nära mikrofonen.

```cpp
const int micPin = A0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int raw = analogRead(micPin);
  Serial.println(raw);
  delay(5);
}
```

Notera:

- ungefärlig vilonivå
- hur mycket värdet rör sig vid tystnad
- hur starkt värdet reagerar på klapp, tal eller knackning
- om värdet slår i 0 eller maxvärde

Om signalen ofta slår i maxvärde kan förstärkningen vara för hög eller ljudet för starkt nära mikrofonen.

### Steg 2: Mät peak-to-peak

Byt till fönsterbaserad mätning.

```cpp
const int micPin = A0;
const unsigned long sampleWindowMs = 50;

int readPeakToPeak() {
  int signalMin = 1023;
  int signalMax = 0;

  unsigned long start = millis();

  while (millis() - start < sampleWindowMs) {
    int sample = analogRead(micPin);
    signalMin = min(signalMin, sample);
    signalMax = max(signalMax, sample);
  }

  return signalMax - signalMin;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  int level = readPeakToPeak();
  Serial.println(level);
}
```

Testa flera ljud:

- tyst rum
- tal på normalt avstånd
- klapp
- knackning på bord
- motor eller fläkt om du har en säker lågspänningskälla
- bakgrundsljud från dator eller ventilation

Dokumentera ungefärliga värden. Det är din lokala ljudprofil.

### Steg 3: Lägg till indikator

Använd sedan en LED som visar när ljudnivån passerar en tröskel.

```cpp
const int micPin = A0;
const int ledPin = 9;

const int onThreshold = 90;
const int offThreshold = 50;
const unsigned long holdTimeMs = 400;

bool active = false;
unsigned long lastHighLevelMs = 0;

int readPeakToPeak() {
  int signalMin = 1023;
  int signalMax = 0;

  unsigned long start = millis();

  while (millis() - start < 40) {
    int sample = analogRead(micPin);
    signalMin = min(signalMin, sample);
    signalMax = max(signalMax, sample);
  }

  return signalMax - signalMin;
}

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int level = readPeakToPeak();
  unsigned long now = millis();

  if (level >= onThreshold) {
    active = true;
    lastHighLevelMs = now;
  }

  if (active && level < offThreshold && now - lastHighLevelMs > holdTimeMs) {
    active = false;
  }

  digitalWrite(ledPin, active ? HIGH : LOW);

  Serial.print(level);
  Serial.print(',');
  Serial.println(active ? 120 : 0);
}
```

Justera trösklarna efter dina faktiska mätvärden.

### Praktiska förbättringar

Utöka experimentet på ett av följande sätt:

- låt en RGB-LED visa tyst, normal och stark ljudnivå
- logga antal ljudhändelser per minut
- kombinera ljud med PIR eller avståndssensor för att minska falska larm
- visa ljudnivå på OLED-display
- använd en buzzer som bekräftelse, men undvik att den triggar mikrofonen om och om igen

Den sista punkten är viktig. Om projektet både lyssnar och låter kan det skapa akustisk återkoppling: systemet reagerar på sitt eget ljud.

### Typiska ljudmönster

Ljudmoduler fungerar bäst när de används för enkla händelser eller relativa nivåer, inte som exakt ljudanalys. Tabellen visar vanliga val:

| Användning | Praktiskt mönster |
|---|---|
| Klapp eller knackning | peak-to-peak över kort tidsfönster och en kort spärrtid efter trigger |
| Grov bullernivå | relativ nivå över längre tidsfönster |
| Enkel ljudtrigger | digital modulutgång med debounce eller tidslås |
| Statusindikator | låg, normal och hög nivå med hysteresis |
| Mer avancerad ljudanalys | I2S-mikrofon eller specialiserad ljudbehandling |

Börja alltid med råvärden i seriell plotter. Då ser du om modulen ger användbar variation innan du bygger beslut, larm eller loggning ovanpå signalen.

## Vanliga misstag

- **Misstag: Att tro att en billig ljudsensor mäter decibel.**
  - Varför det händer: Moduler säljs ofta med otydliga beskrivningar som “sound level sensor”.
  - Hur man undviker det: Beskriv värdet som relativ ljudnivå om systemet inte är kalibrerat.

- **Misstag: Att jämföra råa analogvärden direkt med en tröskel.**
  - Varför det händer: Det liknar hur man ofta börjar med potentiometrar och ljussensorer.
  - Hur man undviker det: Beräkna ett mått över ett tidsfönster, exempelvis peak-to-peak.

- **Misstag: Att glömma mittnivån på analoga mikrofonmoduler.**
  - Varför det händer: Man förväntar sig att tystnad ska vara nära 0.
  - Hur man undviker det: Titta på råvärden i seriell plotter och förstå modulens biasnivå.

- **Misstag: Att använda för långsamma utskrifter under sampling.**
  - Varför det händer: Seriell debug känns ofarligt, men kan dominera tiden i snabb mätkod.
  - Hur man undviker det: Sampla först, skriv ut sammanfattade värden efter mätfönstret.

- **Misstag: Att placera mikrofonen nära reläer, motorer eller buzzers.**
  - Varför det händer: Man tänker på elektrisk funktion men inte akustisk eller mekanisk påverkan.
  - Hur man undviker det: Testa placering, kapsling och avstånd med projektets faktiska ljudkällor.

- **Misstag: Att använda I2S för ett problem som bara kräver ljudhändelse.**
  - Varför det händer: Digitalt ljud låter mer professionellt.
  - Hur man undviker det: Välj enklaste lösning som ger tillräcklig information.

## Snabbreferens

| Behov | Rekommenderad lösning | Kommentar |
|---|---|---|
| Upptäcka klapp eller knackning | Digital ljudtrigger | Enkel, men ungefärlig |
| Relativ ljudnivå | Analog mikrofonmodul | Använd tidsfönster och filtrering |
| LED som följer ljud | Analog modul plus peak-to-peak | Mappa filtrerad nivå till PWM |
| Mer kontrollerad ljudsampling | I2S-mikrofon | Passar bättre på ESP32/RP2040-liknande kort |
| Exakt ljudnivå i dB | Kalibrerad ljudmätare eller specialmodul | Vanlig Arduino-modul räcker inte |
| Ljudklassificering | Kraftigare plattform och signalbehandling | Ligger utanför enkel Arduino-mätning |

Bra startvärden för experiment:

| Parameter | Rimligt startvärde | Kommentar |
|---|---|---|
| Samplingsfönster | 30 till 100 ms | Kortare reagerar snabbare, längre blir stabilare |
| Hålltid efter ljud | 200 till 500 ms | Hindrar fladder |
| Hysteresis | Av-tröskel lägre än på-tröskel | Gör status stabilare |
| Seriell hastighet | 115200 baud | Minskar risken att utskrift bromsar för mycket |
| Första analys | Seriell plotter | Ger snabb bild av signalens beteende |

## Snabb sammanfattning

- En ljudsensor är ofta bäst på att upptäcka ljudhändelser, inte på att mäta exakt ljudnivå.
- Analoga mikrofonmoduler bör läsas över ett tidsfönster, inte som enskilda råvärden.
- Peak-to-peak är ett enkelt och användbart relativt ljudmått.
- Hysteresis och hålltid gör ljudstyrda system mycket stabilare.
- Digitala ljudtriggers fungerar som händelsesensorer, men ger inte detaljerad nivåinformation.
- I2S-mikrofoner passar när du behöver digital ljuddata och använder ett kraftigare kort.
- Säg inte decibel om systemet inte är kalibrerat för decibel.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Beror på modul, ofta 3,3 V på digitala mikrofoner |
| Typiskt gränssnitt | Analogt, digital trigger eller I2S |
| Välj när | ljudhändelser eller enkel nivå ska upptäckas |
| Välj inte när | du behöver exakt ljudmätning eller avancerad analys |
| Vanliga fel | förväxling mellan detektion och ljudnivå, brus, fel sampling |
| Alternativ att överväga | buzzer, I2S-mikrofon, extern ljudmodul |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När du bara behöver ljud ut, börja med kapitel 19 om buzzers, små högtalare och enkla ljudsignaler.
- När mikrofonmodulen ger analog signal, använd kapitel 6 för trösklar och kapitel 33 för brus, förstärkning och nivåanpassning.
- När ljud ska samplas över tid utan att blockera resten av programmet, jämför med kapitel 7.
- När ljuddelen stör resten av projektet, kontrollera strömförsörjningen i kapitel 34.
