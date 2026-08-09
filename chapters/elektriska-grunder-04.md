# 4. Elektriska grunder för programmerare

## Begrepp i praktiken
Det här kapitlet ger den elektriska grundmodell du behöver för resten av boken. Använd det när en koppling beter sig märkligt, när du ska blanda 5 V- och 3,3 V-delar, när en sensor kräver pull-up, eller när en motor, LED-list eller relä inte bör drivas direkt från en GPIO.

Kapitlet fokuserar på sådant som ofta avgör om ett Arduino-projekt fungerar stabilt:

- spänning, ström, resistans och effekt
- gemensam jord
- logiknivåer och nivåskiftning
- pull-up, pull-down och flytande ingångar
- avkopplingskondensatorer och enklare skydd
- multimetermätning som första felsökningssteg

Målet är inte att göra dig till analogelektronikkonstruktör. Målet är att du ska kunna läsa en moduls grundkrav, koppla säkrare och felsöka de vanligaste elektriska problemen mer metodiskt.

## Förutsättningar

Kapitlet förutsätter inte tidigare elektronikstudier. Det räcker att du är beredd att mäta, kontrollera datablad och tänka på fysiska gränser som spänning, ström, värme och gemensam jord.

## Elektronikens fyra vardagsstorheter

De fyra storheter du hela tiden möter är spänning, ström, resistans och effekt.

| Storhet | Enhet | Praktisk betydelse |
|---|---|---|
| Spänning | volt, V | Elektrisk potentialskillnad mellan två punkter |
| Ström | ampere, A | Hur mycket laddning som rör sig per tidsenhet |
| Resistans | ohm, Ω | Hur mycket en komponent begränsar ström |
| Effekt | watt, W | Hur snabbt elektrisk energi omvandlas till värme, ljus, rörelse eller annat |

En vanlig programmeraranalogi är att se spänning som tryck, ström som flöde och resistans som trängsel i ett rör. Analogin är inte perfekt, men den hjälper i början. En högre spänning kan driva mer ström genom samma motstånd. Ett större motstånd begränsar strömmen vid samma spänning.

Det viktiga i Arduino-sammanhang är att komponenter inte bara “tar vad de behöver” på ett magiskt sätt. En LED utan strömbegränsning kan försöka dra för mycket ström. En motor kan dra mycket mer ström vid start än när den redan snurrar. En sensor kan kräva 3,3 V även om den sitter på en modul som råkar likna en 5 V-modul. En GPIO-pinne kan tåla en logisk signal men inte driva en last.

## Spänning är alltid mellan två punkter

Spänning mäts mellan två punkter. När du säger att en pinne är 5 V menar du nästan alltid 5 V jämfört med jord, GND. GND är inte magiskt “noll” i universum, utan referenspunkten i din krets.

Det gör att en signal bara är begriplig om sändare och mottagare delar referens. Om en sensor skickar en digital signal till ett Arduino-kort men deras jordar inte är ihopkopplade, vet inte kortet vad sensorns HIGH och LOW betyder. Resultatet kan bli slumpmässigt beteende.

En grundregel är därför:

> Kretsar som utbyter elektriska signaler behöver normalt gemensam jord.

Det gäller även när de har separata matningar. Om du driver en LED-strip från en extern 5 V-strömförsörjning och styr den från ett Arduino-kort måste GND från LED-strömförsörjningen och GND från Arduino-kortet normalt kopplas ihop. Annars saknar datasignalen gemensam referens.

Det finns undantag, till exempel optokoppling eller galvanisk isolering, men de är medvetna konstruktioner. För vanliga Arduino-projekt ska du utgå från att gemensam jord behövs.

## Ström är det som ofta går fel

Många nybörjarfel handlar om spänning, men många förstörda komponenter handlar om ström. En mikrokontrollerpinne är inte en liten strömkälla för allt du vill styra. Den är i första hand en signalpinne.

En GPIO kan vanligtvis driva en liten LED via ett motstånd. Den ska inte driva motorer, reläspolar, solenoider, längre LED-strippar, högtalare eller annan last direkt. Sådana laster behöver en drivkrets, transistor, MOSFET, relämodul eller separat styrmodul. De behöver ofta också egen matning.

Du kan tänka på en GPIO som ett logiskt beslut:

- “Sätt signalen HIGH.”
- “Sätt signalen LOW.”
- “Läs om signalen är HIGH eller LOW.”

Den är inte avsedd som en generell kraftutgång.

## Ohms lag som praktiskt verktyg

Ohms lag säger:

```text
U = R * I
```

Där:

- `U` är spänning i volt
- `R` är resistans i ohm
- `I` är ström i ampere

Samma formel kan skrivas om:

```text
I = U / R
R = U / I
```

I Arduino-projekt använder du ofta Ohms lag för att välja motstånd, uppskatta ström eller kontrollera om något är rimligt.

Exempel: Du har 5 V matning och vill låta ungefär 10 mA gå genom en LED. En röd LED kan ha ett spänningsfall på ungefär 2 V. Motståndet ska då ta resten:

```text
Spänning över motståndet = 5 V - 2 V = 3 V
R = 3 V / 0,010 A = 300 Ω
```

Ett vanligt närliggande standardvärde är 330 Ω. Det ger lite lägre ström och är oftast ett bra val.

För 3,3 V matning blir beräkningen:

```text
Spänning över motståndet = 3,3 V - 2 V = 1,3 V
R = 1,3 V / 0,010 A = 130 Ω
```

Ett vanligt val kan vara 150 Ω eller 220 Ω beroende på önskad ljusstyrka. För indikator-LED räcker ofta mindre ström än man tror.

## Effekt och varför komponenter blir varma

Effekt beskriver hur mycket energi som omvandlas per sekund. För resistiva delar kan du använda:

```text
P = U * I
```

eller:

```text
P = I * I * R
```

I små signalkopplingar är effekten ofta låg. Men så fort du arbetar med motorer, LED-strippar, regulatorer, reläer eller motstånd som tar upp mycket spänning kan effekt bli viktigt.

Exempel: Ett motstånd som har 5 V över sig och 100 mA genom sig förbrukar:

```text
P = 5 V * 0,1 A = 0,5 W
```

Ett vanligt litet 0,25 W-motstånd är då för litet. Det kan bli varmt eller skadas.

Samma sak gäller regulatorer. Om en linjär regulator tar in 9 V och ger ut 5 V vid 300 mA måste den göra sig av med skillnaden som värme:

```text
P = (9 V - 5 V) * 0,3 A = 1,2 W
```

Det kan vara mycket för ett litet utvecklingskort. Därför fungerar ett kort ibland bra via USB men blir instabilt eller varmt när det matas via en annan ingång och samtidigt driver moduler.

## 5 V, 3,3 V och logiknivåer

Klassiska Arduino UNO- och Nano-kort använder ofta 5 V-logik. Många modernare kort, till exempel ESP8266, ESP32 och RP2040-baserade kort, använder 3,3 V-logik. Det betyder att deras GPIO-signaler normalt förväntar sig ungefär 0 V för LOW och ungefär 3,3 V för HIGH.

Problemet uppstår när 5 V och 3,3 V blandas.

| Situation | Typisk risk | Vanlig lösning |
|---|---|---|
| 5 V-sensor till 5 V-kort | Ofta okej om båda är 5 V-kompatibla | Kontrollera datablad och modul |
| 3,3 V-sensor till 3,3 V-kort | Ofta okej | Kontrollera matning och pullups |
| 3,3 V-sensor till 5 V-kort | HIGH kanske läses rätt, men inte alltid | Kontrollera logiktrösklar |
| 5 V-signal till 3,3 V-kort | Risk att skada ingång | Använd nivåskiftning |
| I2C med 5 V-pullups till 3,3 V-kort | Risk för överspänning på SDA/SCL | Flytta pullups till 3,3 V eller använd nivåskiftare |

En särskilt viktig regel:

> Skicka inte 5 V-signaler direkt in i GPIO på ett kort som bara tål 3,3 V.

Vissa moduler har inbyggd nivåskiftning. Andra har det inte. Två breakout boards med samma sensorchip kan därför ha olika elektriska krav.

## Nivåskiftning

Nivåskiftning (level shifting) betyder att du anpassar signalspänningen mellan två logiknivåer. Det kan göras på flera sätt.

| Metod | Passar för | Kommentar |
|---|---|---|
| Spänningsdelare | Enkel envägssignal från 5 V till 3,3 V | Långsam men ofta okej för enkla digitala ingångar |
| MOSFET-baserad nivåskiftare | I2C och tvåvägssignaler | Vanlig färdig modul |
| Dedikerad level shifter-IC | Snabbare eller mer kontrollerade signaler | Bättre för SPI och mer krävande signaler |
| Transistorlösning | Enkla styrsignaler | Kräver rätt dimensionering |
| Optokopplare | Isolering mellan kretsar | Långsammare och mer specialiserat |

För I2C är MOSFET-baserade nivåskiftarmoduler vanliga eftersom SDA och SCL är tvåvägssignaler med pull-up. För SPI är dedikerade nivåskiftare ofta bättre, eftersom signalerna kan vara snabbare och har tydligare riktning.

En färdig I2C logic level converter är ett vanligt praktiskt val när ett 5 V-kort ska kommunicera med en 3,3 V-I2C-modul. Då kopplas lågspänningssidan till 3,3 V, högspänningssidan till 5 V och GND delas mellan sidorna. Den löser inte alla nivåproblem, men den är ofta rätt startpunkt för I2C-sensorer, OLED-displayer och andra breakoutkort med SDA/SCL.

En vanlig fälla är att använda en långsam eller olämplig nivåskiftarmodul bara för att den “fungerade” i ett annat experiment. Nivåskiftning måste passa signaltyp, hastighet och riktning.

## Ingångar får inte flyta

En digital ingång som inte är kopplad till en definierad nivå kan flyta. Det betyder att den kan läsa HIGH eller LOW beroende på brus, beröring, närliggande signaler eller slumpmässiga elektriska förhållanden.

Det klassiska exemplet är en knapp. Om du kopplar ena sidan av knappen till 5 V och den andra till en ingång, men inte ger ingången någon nivå när knappen inte är tryckt, kommer ingången att flyta i viloläget.

Lösningen är pull-up eller pull-down.

## Pull-up och pull-down

Ett pull-up-motstånd kopplar en signal svagt till HIGH när inget annat aktivt driver den. Ett pull-down-motstånd kopplar signalen svagt till LOW.

| Koppling | Viloläge | Aktivt läge | Typisk användning |
|---|---|---|---|
| Pull-up | HIGH | Knapp drar till LOW | Arduino-knappar med `INPUT_PULLUP` |
| Pull-down | LOW | Knapp drar till HIGH | Vanligt i många digitala kretsar |
| Extern pull-up | HIGH | Enhet drar till LOW | I2C, open drain, vissa sensorer |

Arduino har ofta interna pull-up-motstånd som kan aktiveras med:

```cpp
pinMode(buttonPin, INPUT_PULLUP);
```

Då kopplas knappen ofta mellan pinnen och GND. När knappen inte är tryckt läser pinnen HIGH. När knappen trycks läser pinnen LOW.

Detta känns bakvänt första gången, men är robust och vanligt.

```cpp
const int buttonPin = 2;

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  bool pressed = digitalRead(buttonPin) == LOW;

  if (pressed) {
    Serial.println("Pressed");
  } else {
    Serial.println("Released");
  }

  delay(100);
}
```

I senare kapitel kommer vi att förbättra knapphanteringen med debouncing och icke-blockerande kod. Här är poängen att ingången alltid har en definierad nivå.

## Open drain och varför vissa signaler behöver pull-up

Vissa kretsar driver inte aktivt signalen både HIGH och LOW. De kan i stället bara dra signalen låg. När ingen enhet drar ner signalen gör ett pull-up-motstånd att signalen blir HIGH. Detta kallas ofta open drain eller open collector, beroende på teknik.

I2C bygger på den principen. Flera enheter delar samma SDA- och SCL-ledningar och kan dra dem låga. Pull-up-motstånd gör att linjerna går tillbaka till HIGH.

Det är därför I2C-problem ofta handlar om pullups:

- Pullups saknas.
- Pullups finns men till fel spänning.
- Pullups är för svaga för bussens kapacitans och hastighet.
- Flera moduler har egna pullups så den totala resistansen blir för låg.
- Kablarna är för långa eller brusiga.

Du behöver inte kunna dimensionera alla I2C-bussar från grunden ännu, men du ska känna igen mönstret: I2C är inte bara två godtyckliga digitala signaler. Det är en buss med elektriska regler.

## Kondensatorer som praktisk stabilitet

En kondensator kan lagra en liten mängd laddning. I Arduino-projekt används kondensatorer ofta för avkoppling, filtrering och stabilisering.

Avkoppling (decoupling) betyder att en kondensator placeras nära en komponent för att jämna ut snabba strömvariationer. Många IC-kretsar behöver en liten kondensator nära matningspinnarna, ofta exempelvis 100 nF. Moduler har ibland redan detta, men inte alltid tillräckligt för hela kopplingen.

Större kondensatorer kan hjälpa när laster ändras snabbt. En LED-strip, servo eller radiosändare kan dra strömtoppar som får matningsspänningen att dippa. Då kan mikrokontrollern starta om eller sensorer ge konstiga värden.

Kondensatorer löser inte allt. Om matningen är för svag, ledningarna för tunna eller lasten för stor behöver du rätt strömförsörjning och bättre kopplingslayout. Men en välplacerad kondensator kan göra skillnaden mellan ett instabilt experiment och ett stabilt.

## Dioder och skydd mot induktiva laster

Induktiva laster, till exempel reläspolar, solenoider och motorer, kan skapa spänningsspikar när strömmen bryts. Energin i magnetfältet måste ta vägen någonstans. Utan skydd kan spiken störa eller skada styrkretsen.

En vanlig lösning är en skyddsdiod, ofta kallad flyback-diod, parallellt med spolen. Dioden leder när spänningen försöker gå åt fel håll och ger strömmen en säker väg att klinga av.

Färdiga relämoduler och motordrivare har ofta skyddskomponenter, men du ska inte anta det utan att kontrollera modulen. Om du bygger med lös transistor, MOSFET eller reläspole behöver skyddet vara en del av konstruktionen.

## Spänningsdelare

En spänningsdelare består av två motstånd och används för att skapa en lägre spänning från en högre. Den vanligaste Arduino-användningen är att mäta en spänning som är högre än ADC-ingången tål, eller att sänka en enkel digital signal från 5 V till ungefär 3,3 V.

Grundkopplingen är:

```text
Vin --- R1 ---+--- R2 --- GND
              +
             Vout
```

Formeln är:

```text
Vout = Vin * R2 / (R1 + R2)
```

Exempel: Du vill sänka 5 V till ungefär 3,3 V.

Välj R1 = 10 kΩ och R2 = 20 kΩ:

```text
Vout = 5 V * 20000 / (10000 + 20000)
Vout är ungefär 3,33 V
```

Det fungerar för långsamma signaler eller enkla mätningar. Det är inte alltid rätt lösning för snabba bussar, långa kablar eller signaler där mottagaren påverkar delaren. En ADC-ingång har också krav på källimpedans, särskilt vid snabb sampling.

Som tumregel är spänningsdelare bra för:

- enkel batterimätning
- enkel skalning av DC-spänning
- långsam envägslogik från 5 V till 3,3 V

De är sämre för:

- tvåvägssignaler
- I2C
- snabb SPI
- laster
- signaler där noggrannhet är viktig utan kalibrering

## Motstånd skyddar inte mot allt

Det är lätt att börja se motstånd som allmänna skydd. Ett seriemotstånd kan begränsa ström och skydda i vissa situationer, men det gör inte en felaktig koppling automatiskt säker.

Ett motstånd kan hjälpa vid:

- LED-strömbegränsning
- enkel ingångsbegränsning
- pull-up och pull-down
- spänningsdelning
- begränsning av ström vid vissa fel

Ett motstånd ersätter inte:

- rätt matningsspänning
- nivåskiftning när signalriktningen är tvåvägs eller snabb
- drivkrets för motor eller relä
- säkring vid högre strömmar
- isolering där säkerhet kräver det
- korrekt dimensionerad regulator

## Breadboard, kablar och kontaktproblem

Många Arduino-projekt byggs på breadboard. Det är praktiskt men inte perfekt. Breadboards har kontaktresistans, glapp, kapacitans mellan rader, begränsad strömtålighet och varierande kvalitet.

Vanliga breadboard-problem är:

- komponentben sitter inte ordentligt
- kablar är avbrutna eller dåligt pressade
- plus- och minus-skenor är delade på mitten utan att det syns tydligt
- långa kablar plockar upp brus
- höga strömmar går genom banor som inte är avsedda för det
- en modul sitter en rad fel

När ett experiment beter sig konstigt ska du inte bara granska koden. Dra försiktigt i kablarna, mät kontinuitet, kontrollera att skenorna verkligen är sammanhängande och kontrollera att GND är gemensam.

## Mät med multimeter innan du gissar

En multimeter är ett av de viktigaste verktygen i boken. Du behöver inte använda den avancerat för att få stor nytta.

Börja med dessa kontroller:

- Mät matningsspänningen mellan VCC och GND.
- Mät att GND på olika delar verkligen är ihopkopplade.
- Kontrollera att en GPIO inte får högre spänning än den tål.
- Kontrollera att en knapp faktiskt ändrar signalnivå.
- Kontrollera kontinuitet i kablar.
- Mät spänning före och efter regulator eller nivåskiftare.

Ett bra arbetssätt är att alltid mäta matning och jord innan du laddar upp mer kod. Många “programmeringsfel” i Arduino-projekt är egentligen fel matning, fel GND eller fel pinout.

## Säkerhetsgräns: undvik nätspänning

Den här boken fokuserar på lågspänningsprojekt. Nätspänning, alltså 230 V AC i svensk miljö, är farligt och ska inte hanteras på breadboard eller med improviserade kopplingar. Färdiga relämoduler gör inte nätspänning automatiskt säker.

När ett projekt behöver styra nätansluten utrustning bör du använda färdiga, kapslade och godkända produkter eller låta behörig kompetens hantera installationen. I bokens experiment håller vi oss till säkra lågspänningslaster.

En praktisk tumregel:

> Bygg, testa och lär med lågspänning. Behandla nätspänning som ett separat säkerhetsområde, inte som ännu en Arduino-pin.


## Riskkontroll före koppling

Använd den här kontrollen när du är osäker på om en enkel koppling är trygg att prova.

- Kontrollera vilken spänning kortet använder för logik: 5 V, 3,3 V eller något annat.
- Kontrollera att en LED alltid har seriemotstånd.
- Kontrollera att en knapp eller sensorutgång inte lämnar en ingång flytande.
- Kontrollera att alla delar som delar signal också delar jord.
- Kontrollera att ingen pinne får högre spänning än kortet tål.
- Koppla inte in motorer, reläer, solenoider eller andra laster direkt på en GPIO-pinne.

Om någon punkt känns oklar är det bättre att mäta först, förenkla kopplingen och gå vidare i små steg.

## Referensmönster: minsta säkra koppling med LED, knapp och analog signal

Det här referensmönstret samlar tre grundkopplingar som återkommer i nästan alla Arduino-projekt: en LED med seriemotstånd, en knapp med definierad ingång och en enkel analog signal via spänningsdelare eller potentiometer. Poängen är att kontrollera spänning, ström, jord och signalnivå innan projektet växer.

Mönstret visar också en viktig gräns: en GPIO kan driva en liten indikator, men den ska inte användas som strömkälla för laster som motorer, reläer, solenoider eller LED-strips.

### Del A: LED med seriemotstånd

Det här används i exemplet:

- ett Arduino-kompatibelt kort
- en LED
- ett motstånd, till exempel 330 Ω för 5 V eller 220–330 Ω för 3,3 V som försiktig start
- breadboard och kopplingskablar
- multimeter

Koppling:

1. Koppla en GPIO till motståndet.
2. Koppla motståndet till LED:ens anod.
3. Koppla LED:ens katod till GND.
4. Kontrollera LED:ens riktning innan du matar kretsen.

Exempelkod:

```cpp
const int ledPin = 9;

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

Kontrollera detta:

- Mät spänningen över LED:en när den lyser.
- Mät spänningen över motståndet.
- Kontrollera att summan ungefär motsvarar matningsspänningen.
- Beräkna strömmen genom motståndet med Ohms lag.
- Byt hellre till större motstånd om du är osäker på LED:ens strömgräns.

### Del B: Knapp med intern pull-up

Det här används i exemplet:

- samma Arduino-kompatibla kort
- en tryckknapp
- breadboard och kopplingskablar

Koppla knappen mellan digital ingång och GND. I koden används intern pull-up, vilket gör att viloläget är HIGH och tryckt knapp blir LOW.

Exempelkod:

```cpp
const int buttonPin = 2;
const int ledPin = 9;

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  bool pressed = digitalRead(buttonPin) == LOW;

  digitalWrite(ledPin, pressed ? HIGH : LOW);

  Serial.print("button=");
  Serial.println(pressed ? "pressed" : "released");

  delay(100);
}
```

Kontrollera detta:

- Mät spänningen på knappens ingång när knappen inte är tryckt.
- Mät spänningen när knappen är tryckt.
- Jämför mätningen med vad seriella monitorn visar.
- Kom ihåg att aktiv LOW är normalt när en knapp kopplas mot GND med intern pull-up.

### Del C: Spänningsdelare eller potentiometer som analog signal

Det här används i exemplet:

- två motstånd, till exempel 10 kΩ och 20 kΩ, eller en potentiometer
- en känd matningsspänning, till exempel 5 V från ett 5 V-kort eller 3,3 V från ett 3,3 V-kort
- multimeter
- eventuellt en analog ingång

En enkel spänningsdelare kan kopplas så här:

```text
5 V --- 10 kΩ ---+--- 20 kΩ --- GND
                 |
               A0 eller mätpunkt
```

Exempelkod för analog mätning:

```cpp
const int analogPin = A0;
const float referenceVoltage = 5.0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int raw = analogRead(analogPin);
  float voltage = raw * referenceVoltage / 1023.0;

  Serial.print("raw=");
  Serial.print(raw);
  Serial.print(" voltage=");
  Serial.println(voltage, 3);

  delay(500);
}
```

Kontrollera detta:

- Beräkna förväntad `Vout`.
- Mät `Vout` med multimeter.
- Läs `Vout` med analog ingång.
- Jämför beräkning, multimeter och ADC-värde.
- Justera `referenceVoltage` och ADC-upplösning om kortet inte använder 5 V och 10-bitars ADC.
- Koppla aldrig en spänning till en analog ingång om den kan överstiga vad kortet tål.

Skillnader mellan beräknat värde, multimetervärde och Arduino-värde beror ofta på motståndstoleranser, referensspänning, ADC-upplösning, brus och hur stabil matningen är.

## Valguide: vad behöver kopplingen?

När du kopplar en ny sensor, modul eller krets kan du använda denna checklista.

| Fråga | Varför den spelar roll |
|---|---|
| Vilken matningsspänning krävs? | Fel matning kan ge felvärden eller skada komponenten |
| Vilken logiknivå använder signalerna? | 5 V-signal kan skada 3,3 V-GPIO |
| Hur mycket ström drar modulen? | Kortets regulator eller USB kan vara otillräcklig |
| Behövs gemensam jord? | Signaler behöver referens mellan sändare och mottagare |
| Behövs pull-up eller pull-down? | Ingångar och bussar måste ha definierade nivåer |
| Behövs extern drivning? | GPIO-pinnar är signaler, inte kraftutgångar |
| Behövs skydd mot induktiv last? | Reläer, solenoider och motorer kan skapa spänningsspikar |
| Behövs nivåskiftning? | Blandade 5 V- och 3,3 V-system kräver kontroll |
| Behövs avkopplingskondensator? | Snabba strömvariationer kan ge omstarter och brus |
| Är kopplingen säker att bygga på breadboard? | Höga strömmar och nätspänning hör inte hemma där |

## Vanliga misstag

- **Misstag: Att koppla en 5 V-signal direkt till ett 3,3 V-kort.**
  - Varför det händer: Moduler ser ofta likadana ut oavsett logiknivå.
  - Hur man undviker det: Kontrollera GPIO-tolerans och använd nivåskiftning när det behövs.

- **Misstag: Att glömma gemensam jord mellan separat matade delar.**
  - Varför det händer: Det är lätt att tänka på signalen men glömma referensen.
  - Hur man undviker det: Koppla ihop GND när kretsar ska utbyta vanliga elektriska signaler, om du inte använder avsiktlig isolering.

- **Misstag: Att driva motor, relä eller LED-strip direkt från en GPIO.**
  - Varför det händer: En digital utgång känns som en styrbar strömkälla.
  - Hur man undviker det: Använd transistor, MOSFET, relämodul eller drivkrets och separat matning vid behov.

- **Misstag: Att lämna digitala ingångar flytande.**
  - Varför det händer: En knapp eller brytare verkar bara behöva öppna och stänga en signal.
  - Hur man undviker det: Använd intern pull-up, extern pull-up eller extern pull-down.

- **Misstag: Att lita på färgen på kablar i stället för att mäta.**
  - Varför det händer: Röd brukar betyda plus och svart brukar betyda GND.
  - Hur man undviker det: Mät spänning och kontinuitet, särskilt i återanvända eller billiga kabelsatser.

- **Misstag: Att anta att två moduler med samma sensorchip har samma elektriska egenskaper.**
  - Varför det händer: Sensorchipet är detsamma, men breakout-kortet kan skilja sig.
  - Hur man undviker det: Kontrollera om modulen har regulator, pullups, nivåskiftning och rätt pinout.

- **Misstag: Att felsöka kod innan matningen är kontrollerad.**
  - Varför det händer: Programmerare börjar naturligt i koden.
  - Hur man undviker det: Mät VCC, GND och signalnivåer först när beteendet verkar oförklarligt.

## Begreppsförklaring: logiknivå och gemensam jord

Två begrepp återkommer genom resten av boken:

- **Logiknivå** är den spänning som ett kort tolkar som digitalt låg eller hög signal. Ett klassiskt 5 V-kort och ett modernt 3,3 V-kort kan därför vara inkompatibla även om koden ser likadan ut.
- **Gemensam jord**, ofta kallat **common ground**, betyder att två delar av en krets delar samma referensnivå för spänning. Utan gemensam jord kan en styrsignal från ett kort bli meningslös för en extern modul.

När två moduler kommunicerar med vanliga digitala signaler behöver du normalt kontrollera tre saker: samma jord, kompatibla logiknivåer och rimlig strömförsörjning.

## Snabb sammanfattning

- Spänning mäts mellan två punkter, oftast jämfört med GND.
- Kretsar som utbyter vanliga elektriska signaler behöver normalt gemensam jord.
- GPIO-pinnar är i första hand signalpinnar, inte kraftutgångar.
- Ohms lag hjälper dig att välja motstånd och uppskatta ström.
- Effekt blir viktig när strömmen ökar eller när regulatorer och motstånd blir varma.
- 5 V- och 3,3 V-system får inte blandas utan kontroll av logiknivåer.
- Nivåskiftning behövs när signalnivåer inte passar mottagaren.
- I2C-nivåomvandlare är ofta rätt skydd när 5 V- och 3,3 V-I2C-moduler ska dela buss.
- Digitala ingångar behöver definierad nivå genom pull-up eller pull-down.
- Kondensatorer kan stabilisera matning och minska problem från snabba strömvariationer.
- Motorer, reläer och solenoider kräver drivning och ofta skydd mot induktiva spikar.
- Mät matning, jord och signalnivåer innan du lägger för mycket tid på kodfelsökning.
- Håll bokens experiment på säker lågspänning.

## Relaterat

- När teorin blir en faktisk digital signal, gå vidare till kapitel 5.
- När spänning, ström och mätning behöver kvantifieras, använd kapitel 28.
- När 5 V- och 3,3 V-delar ska kopplas ihop, jämför med kapitel 9 och kapitel 33.
