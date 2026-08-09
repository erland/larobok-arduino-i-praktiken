# 31. Drivkretsar för LED, motorer och laster

## Drivsteg i praktiken
I tidigare kapitel har du styrt LED, buzzers, servon, motorer, reläer, MOSFET:ar och andra laster. Då har fokus legat på hur utenheten beter sig och hur den används i ett praktiskt test. I det här kapitlet flyttar vi blicken ett steg nedåt: till kretsarna som gör det möjligt att styra lasten på ett kontrollerat sätt.

En Arduino-pinne är en styrsignal, inte en kraftutgång. Den kan sättas till HIGH eller LOW, generera PWM och ibland driva en liten indikator-LED. Men den är inte byggd för att direkt mata motorer, LED-strippar, reläspolar, solenoider eller större grupper av lysdioder. Om du försöker göra det ändå kan resultatet bli instabilt beteende, omstarter, varma komponenter eller i värsta fall en skadad mikrokontroller.

En drivkrets är länken mellan mikrokontrollerns logik och lastens elektriska behov. Den kan förstärka ström, skydda mot induktiva spänningsspikar, hantera flera kanaler, ge konstant ström, byta riktning på en motor, isolera signaler eller förenkla kopplingen.

Det här kapitlet kompletterar kapitel 17 till 21. Där såg du hur olika aktuatorer används. Här lär du dig välja rätt typ av drivning:

- en enkel transistor när lasten är liten och kopplingen ska vara enkel
- en logiknivå-MOSFET när du vill styra en DC-last effektivt
- en transistorarray som ULN2803 eller ULN2003 när du vill styra flera kanaler eller en liten unipolär stegmotor
- en H-brygga när en DC-motor ska kunna gå åt båda håll, med L298N som vanligt men äldre exempel och DRV8833 eller L9110S som små modulalternativ
- en stegmotordrivare som A4988 eller DRV8825 när en bipolär stegmotor ska styras med strömbegränsning
- en konstantströmsdrivare när LED ska lysa stabilt och säkert
- en färdig modul när snabb prototypning är viktigare än kretsdetaljer

Målet är inte att du ska bli analogkonstruktör. Målet är att du ska känna igen de vanligaste drivsituationerna, välja en rimlig lösning och undvika de fel som ofta uppstår när programmerare börjar styra verkliga laster.

Kapitlet fungerar som stöd när du behöver välja drivsteg för LED, motorer, reläer, solenoider och andra laster, med fokus på signalnivå, lastström, skyddskomponenter och säker matning.

## Förutsättningar

Det här kapitlet bygger på flera tidigare begrepp:

- Från kapitel 4: spänning, ström, effekt, gemensam jord, nivåskiftning och avkoppling.
- Från kapitel 5: digitala styrsignaler och HIGH/LOW.
- Från kapitel 7: PWM och icke-blockerande tidsstyrning.
- Från kapitel 17 och 18: LED, RGB-LED och adresserbara LED.
- Från kapitel 20: servon, DC-motorer och stegmotorer.
- Från kapitel 21: reläer, MOSFET:ar, solenoider och andra laster.

En viktig tumregel återkommer genom hela kapitlet:

> Mikrokontrollern bestämmer vad som ska hända. Drivkretsen levererar den elektriska kraft som krävs för att det ska hända.

Det betyder att kod, styrsignal och lastmatning ska ses som tre olika delar av samma system.

## Grundidén: signal, drivsteg och last

En typisk koppling med drivkrets kan delas upp i tre nivåer.

| Nivå | Exempel | Roll |
|---|---|---|
| Styrnivå | Arduino-pinne, ESP32-GPIO, RP2040-GPIO | Skickar logisk signal eller PWM |
| Drivnivå | Transistor, MOSFET, ULN2803, H-brygga, LED-drivare | Hanterar ström, spänning och skydd |
| Lastnivå | LED-list, motor, reläspole, solenoid, lampa | Förbrukar energi och gör något fysiskt |

När något inte fungerar är det vanligt att felet ligger i övergången mellan nivåerna. Koden kanske växlar en pinne korrekt, men drivkretsen får för låg styrspänning. Drivkretsen kanske fungerar, men matningen orkar inte med lasten. Lasten kanske fungerar separat, men stör mikrokontrollern när den startar.

Därför ska du alltid dokumentera minst fyra saker:

- vilken pinne som styr lasten
- vilken drivkrets eller modul som används
- vilken spänning som matar lasten
- hur jord är kopplad mellan mikrokontroller, drivsteg och last

Detta är särskilt viktigt i projekt med externa nätaggregat, batterier, motorer eller LED-strippar.

## Direktdrivning: när det faktiskt är okej

Det finns fall där en Arduino-pinne kan driva något direkt. En enkel indikator-LED med seriemotstånd är det vanligaste exemplet. Även vissa mycket högimpediva ingångar på andra kretsar kan drivas direkt.

Direktdrivning kan vara rimligt när alla dessa villkor är uppfyllda:

- lasten kräver mycket liten ström
- lasten är inte induktiv
- lasten har rätt spänningsnivå
- strömmen ligger väl under kortets och mikrokontrollerns rekommenderade gränser
- lasten orsakar inte stora störningar eller startströmmar

Det är däremot inte rimligt att direktdriva:

- motorer
- reläspolar
- solenoider
- LED-strippar
- högeffekts-LED
- lampor
- värmeelement
- pumpar
- fläktar
- många LED samtidigt

Ett vanligt programmerarperspektiv är att “pinnen är ju HIGH, alltså borde den kunna slå på saken”. Elektriskt är det fel tänkt. En GPIO är en styrsignal med begränsad strömförmåga, inte ett litet nätaggregat.

## Lågside- och högsidestyrning

När du styr en last med transistor eller MOSFET finns två grundläggande placeringar: lågside- och högsidestyrning.

### Lågsidestyrning

Vid lågsidestyrning sitter drivkomponenten mellan lasten och jord.

```text
+V ---- Last ---- Drivkomponent ---- GND
```

Mikrokontrollern styr drivkomponenten. När drivkomponenten leder får lasten en väg till jord och slås på.

Lågsidestyrning är vanlig eftersom den är enkel, särskilt med NPN-transistor, N-kanals MOSFET eller ULN2803. Den passar bra för många DC-laster som LED-strippar, reläspolar, solenoider och små motorer.

Fördelar:

- enkel koppling
- fungerar bra med N-kanals MOSFET
- lätt att styra med 3,3 V eller 5 V om rätt komponent väljs
- vanligt i färdiga moduler

Nackdelar:

- lastens jordanslutning växlas, vilket inte alltid är önskvärt
- vissa laster, moduler eller sensorer förväntar sig fast jord
- kan skapa mätproblem om lasten också delar signaljord på känsligt sätt

### Högsidestyrning

Vid högsidestyrning sitter drivkomponenten mellan matningen och lasten.

```text
+V ---- Drivkomponent ---- Last ---- GND
```

Här får lasten en fast jord, medan plusmatningen slås av och på.

Fördelar:

- lasten har fast jord
- passar när jord inte bör brytas
- ofta bättre för vissa systemarkitekturer

Nackdelar:

- kräver ofta P-kanals MOSFET, PNP-transistor eller särskild high-side driver
- kan vara svårare att styra korrekt när lastspänningen är högre än mikrokontrollerns logikspänning
- mer risk för fel om man inte tänker igenom gate/base-styrning

I Arduino-projekt är lågsidestyrning ofta enklast. Högsidestyrning blir aktuell när lasten måste ha gemensam jord, när moduler delar signalledningar, eller när konstruktionen kräver att plusmatningen styrs.

## Transistor som enkel drivare

En bipolär transistor, till exempel en NPN-transistor, kan användas som enkel lågsidebrytare. Mikrokontrollerns pinne går via ett basmotstånd till transistorns bas. Lasten sitter mellan plusmatning och kollektor. Emittern går till jord.

```text
Arduino pin -- resistor -- base
+V ---- Last ---- collector
emitter ---- GND
```

När pinnen är HIGH går en liten basström in i transistorn. Då kan en större ström gå genom lasten.

Transistorn är ett bra val när:

- lasten är relativt liten
- kopplingen är enkel
- du vill förstå principen
- effektivitet inte är kritisk
- spänningsfallet över transistorn är acceptabelt

Transistorn är sämre när:

- lasten drar högre ström
- du vill styra med PWM effektivt
- batteridrift och låg förlust är viktigt
- du har många kanaler och vill minska komponentantalet

Kom ihåg att en transistor i lågsidekoppling ofta behöver:

- basmotstånd
- gemensam jord
- skyddsdiod om lasten är induktiv
- kontroll av maximal kollektorström och effektförlust

För små reläer, buzzers, enkla lampor eller små DC-laster fungerar transistorlösningar bra, men i många moderna projekt är en logiknivå-MOSFET ett bättre standardval.

## MOSFET som effektiv drivare

En MOSFET används ofta som elektronisk strömbrytare. I Arduino-sammanhang är en N-kanals MOSFET i lågsidekoppling mycket vanlig.

```text
Arduino pin ---- gate
+V ---- Last ---- drain
source ---- GND
```

När gate-spänningen är tillräckligt hög relativt source börjar MOSFET:en leda mellan drain och source. För mikrokontrollerprojekt är det viktigt att välja en MOSFET som fungerar bra vid den gate-spänning du faktiskt har. En MOSFET som fungerar fint vid 10 V på gate kan fungera dåligt med 3,3 V från en ESP32 eller RP2040.

Det du letar efter är ofta en logiknivå-MOSFET. Det betyder inte bara att databladet nämner en låg tröskelspänning. Tröskelspänningen anger när MOSFET:en precis börjar leda, inte när den leder bra. Det du vill veta är om den har låg resistans i påslaget läge vid till exempel 4,5 V, 3,3 V eller den styrspänning ditt kort använder.

MOSFET passar bra när:

- lasten drar mer ström än en GPIO kan hantera
- du vill använda PWM
- du vill ha låg effektförlust
- lasten är DC
- du vill styra LED-strip, fläkt, pump, solenoid eller motor i en riktning

MOSFET kräver ofta:

- gate-motstånd för att begränsa snabba strömpulser och dämpa ringningar
- pulldown-motstånd från gate till source så lasten är av under uppstart
- skyddsdiod över induktiv last
- tillräcklig kylning eller marginal vid hög ström
- gemensam jord mellan mikrokontroller och lastmatning

En typisk MOSFET-koppling för en 12 V LED-strip kan se ut så här:

```text
12 V + ---- LED-strip + 
LED-strip - ---- drain på N-MOSFET
source på N-MOSFET ---- GND
Arduino GND ---- samma GND
Arduino PWM-pin ---- gate via litet motstånd
gate ---- pulldown ---- GND
```

Kodmässigt ser styrningen ofta enkel ut:

```cpp
const int ledStripPin = 5;

void setup() {
  pinMode(ledStripPin, OUTPUT);
}

void loop() {
  for (int level = 0; level <= 255; level++) {
    analogWrite(ledStripPin, level);
    delay(10);
  }

  for (int level = 255; level >= 0; level--) {
    analogWrite(ledStripPin, level);
    delay(10);
  }
}
```

Koden är enkel. Det är kopplingen, matningen och komponentvalet som avgör om systemet blir robust.

## ULN2003, ULN2803 och transistorarrays

ULN2003 och ULN2803 är klassiska drivkretsar med flera lågsidekanaler i samma kapsel. Den består i praktiken av flera Darlington-transistorer med inbyggda motstånd och skyddsdioder för induktiva laster. Den används ofta för att driva reläer, små lampor, solenoider, LED-grupper eller andra måttliga laster.

Den stora styrkan är enkelheten. Du får flera kanaler i ett paket och kan styra dem direkt från digitala pinnar.

Typisk användning:

- åtta reläspolar
- flera små solenoider
- LED-grupper
- summermoduler
- små DC-laster
- experiment där många utgångar behöver mer ström än GPIO klarar

ULN2803 passar bra när:

- du behöver flera lågsidekanaler
- lasten inte kräver mycket låg effektförlust
- du vill minska komponentantalet
- lasten är av/på snarare än högpresterande PWM
- du vill ha enkel relä- eller solenoiddrivning

En särskilt vanlig variant är **ULN2003-modulen** som säljs tillsammans med den lilla stegmotorn **28BYJ-48**. Den kombinationen är enkel och billig, men den är främst lämpad för långsamma, lätta rörelser. Den ska inte blandas ihop med moderna STEP/DIR-drivare för bipolära stegmotorer.

Tänk på:

- ULN2003/ULN2803 är lågside-drivare, inte fullständiga H-bryggor.
- De passar bra för flera av/på-laster och vissa små unipolära stegmotorer.
- De har spänningsfall och värmeförlust, så de är inte bäst för hög ström.
- De kan vara pedagogiskt bra även när en modernare lösning vore effektivare.

ULN2003/ULN2803 passar sämre när:

- du behöver mycket låg spänningsförlust
- lasten drar hög ström
- du vill ha effektiv batteridrift
- du behöver högsidestyrning
- PWM-förluster och värme blir viktiga

Eftersom Darlington-steg har ett tydligare spänningsfall än en bra MOSFET blir ULN2803 inte alltid det mest effektiva valet. Men för många undervisnings- och prototypfall är den mycket praktisk.

Exempel på kod för att styra flera kanaler:

```cpp
const int channelPins[] = {2, 3, 4, 5};
const int channelCount = 4;

void setup() {
  for (int i = 0; i < channelCount; i++) {
    pinMode(channelPins[i], OUTPUT);
    digitalWrite(channelPins[i], LOW);
  }
}

void loop() {
  for (int i = 0; i < channelCount; i++) {
    digitalWrite(channelPins[i], HIGH);
    delay(200);
    digitalWrite(channelPins[i], LOW);
  }

  delay(500);
}
```

Koden är identisk med enkel digital styrning. Skillnaden är att GPIO-pinnen inte längre driver lasten direkt. Den driver ULN-ingången, och drivkretsen hanterar lastströmmen.

## H-bryggor för DC-motorer

En vanlig DC-motor kan snurra åt två håll om polariteten över motorn byts. En H-brygga är en krets som gör just detta elektroniskt. Namnet kommer från att fyra brytare kan ritas som ett H runt motorn.

H-bryggor finns som lösa IC-kretsar och färdiga moduler. Klassiska exempel i hobbyvärlden är L293D och L298N, men moderna MOSFET-baserade motor-drivers är ofta effektivare, särskilt vid batteridrift.

En H-brygga kan ge:

- riktning framåt
- riktning bakåt
- stopp
- bromsning
- hastighetsstyrning med PWM

H-brygga passar när:

- en DC-motor ska kunna rotera åt båda håll
- du vill styra hastighet
- lasten kräver mer ström än mikrokontrollern klarar
- du vill separera motorström från logiksignal

H-brygga passar inte automatiskt för:

- stegmotorer, som behöver en särskild styrsekvens eller stegmotordrivare
- servon, som redan har intern drivning
- mycket stora motorer utan korrekt dimensionerad driver
- AC-laster

En förenklad styrmodell med två riktningspinnar och en PWM-pinne kan se ut så här:

```cpp
const int motorIn1 = 7;
const int motorIn2 = 8;
const int motorPwm = 9;

void setup() {
  pinMode(motorIn1, OUTPUT);
  pinMode(motorIn2, OUTPUT);
  pinMode(motorPwm, OUTPUT);
}

void driveForward(int speed) {
  digitalWrite(motorIn1, HIGH);
  digitalWrite(motorIn2, LOW);
  analogWrite(motorPwm, speed);
}

void driveBackward(int speed) {
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, HIGH);
  analogWrite(motorPwm, speed);
}

void stopMotor() {
  analogWrite(motorPwm, 0);
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, LOW);
}

void loop() {
  driveForward(160);
  delay(1000);

  stopMotor();
  delay(500);

  driveBackward(160);
  delay(1000);

  stopMotor();
  delay(1000);
}
```

I verkliga projekt bör du också tänka på acceleration. Att gå direkt från stillastående till hög PWM kan ge stora startströmmar. En enkel ramp gör ofta systemet stabilare.

```cpp
void rampForward() {
  digitalWrite(motorIn1, HIGH);
  digitalWrite(motorIn2, LOW);

  for (int speed = 0; speed <= 180; speed += 5) {
    analogWrite(motorPwm, speed);
    delay(30);
  }
}
```

Detta är fortfarande enkelt, men mycket snällare mot motor, drivare och matning.

### L298N som vanlig men äldre H-bryggmodul

**L298N** är en av de vanligaste motor-driver-modulerna i Arduino-sammanhang. Den finns i många butiker, guider och startkit. Därför är den värd att känna igen även om den inte alltid är det bästa tekniska valet.

L298N fungerar ofta till enkla principtester med små DC-motorer, men den har tydliga begränsningar:

- den har relativt stora spänningsfall
- den kan bli varm
- den är ineffektiv jämfört med moderna MOSFET-baserade drivers
- den kan ge svagare motor än väntat vid batteridrift
- modulens inbyggda regulator/jumpers kan vara förvirrande

Använd L298N när du vill förstå riktning, PWM och H-brygga med låg risk i ett experiment. Välj hellre modernare motor-driver när projektet ska bli kompakt, batteridrivet, strömsnålt eller belastat under längre tid.

### DRV8833 som liten modern dubbel H-brygga

**DRV8833** är en liten modern motor-driver som ofta passar bättre än L298N i små batteridrivna Arduino-projekt. Den är en dubbel H-brygga, vilket betyder att den kan driva två små DC-motorer eller i vissa fall en liten bipolär stegmotor beroende på modul, bibliotek och koppling.

DRV8833 är särskilt användbar när:

- projektet använder små DC-motorer i robotar, hjul, pumpar eller mekaniska prototyper
- låg spänningsförlust och bättre batteridrift är viktigare än att följa äldre guider
- modulen ska vara liten och effektiv
- du vill styra riktning och hastighet med digitala signaler och PWM

Kontrollera alltid modulens datablad eller butiksspecifikation innan du väljer motor. Det viktiga är inte bara att motorn snurrar på bänken, utan att drivaren klarar startström, blockerad motor, kylning och den matningsspänning som projektet faktiskt använder. En liten driver kan fungera utmärkt i ett lätt robotbygge men bli överbelastad om hjulen fastnar eller mekaniken går trögt.

### L9110S som enkel lågkostnadsdrivare

**L9110S** är en enkel och billig liten motordrivare som ofta dyker upp i små robotkit och lågkostnadsmoduler. Den används framför allt för små DC-motorer där kraven på ström, effektivitet och precision är begränsade.

L9110S passar när:

- du bygger ett litet testprojekt eller en enkel robot
- motorerna är små och lätta belastade
- låg kostnad och enkel koppling är viktigare än hög prestanda
- du vill lära dig grundprincipen för riktning och PWM

L9110S är däremot inte ett bra val för tyngre laster, stora hjul, motorer med hög stallström eller projekt som ska gå länge under belastning. Om motorn startar svagt, modulen blir varm eller kortet startar om är det ett tecken på att drivaren, matningen eller mekaniken behöver väljas om.

## Stegmotordrivare

Stegmotorer kräver en annan typ av drivning än vanliga DC-motorer. En stegmotor flyttas stegvis genom att spolarna aktiveras i rätt ordning. Små hobby-stegmotorer kan ibland styras med enklare transistorarray och bibliotek, men mer användbara stegmotorsystem använder särskilda drivare.

Vanliga stegmotordrivare i hobby- och makerprojekt har ofta ingångar som:

- STEP
- DIR
- ENABLE
- ibland MS1/MS2/MS3 eller liknande för microstepping

Mikrokontrollern behöver då inte själv styra varje motorspole. Den skickar stegimpulser och riktning. Drivaren hanterar spolar, strömbegränsning och microstepping.

Stegmotordrivare passar när:

- motorn ska flyttas ett bestämt antal steg
- position är viktig
- du vill ha kontrollerad rörelse
- lasten inte kräver återkoppling i enklare system
- du vill använda microstepping för jämnare gång

Var särskilt uppmärksam på:

- motorström
- drivarnas kylning
- matningsspänning
- strömbegränsning
- acceleration
- att inte koppla loss motor när drivaren är aktiv
- att logikspänning och styrsignal passar kortet

En enkel principiell kod för STEP/DIR-styrning:

```cpp
const int stepPin = 3;
const int dirPin = 4;
const int enablePin = 5;

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enablePin, OUTPUT);

  digitalWrite(enablePin, LOW);
}

void stepMotor(int steps, bool direction) {
  digitalWrite(dirPin, direction ? HIGH : LOW);

  for (int i = 0; i < steps; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(800);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(800);
  }
}

void loop() {
  stepMotor(200, true);
  delay(1000);

  stepMotor(200, false);
  delay(1000);
}
```

För riktiga projekt är ett bibliotek för stegmotorrörelse ofta bättre, särskilt om du behöver acceleration, flera axlar eller icke-blockerande kod.

### A4988 och DRV8825

**A4988** och **DRV8825** är vanliga STEP/DIR-drivare för bipolära stegmotorer. De används ofta med NEMA 17-liknande motorer, men principen är viktigare än motornamnet: mikrokontrollern skickar steg och riktning, medan drivaren reglerar strömmen genom motorlindningarna.

De passar när:

- du behöver kontrollerad position eller repetitiv rörelse
- motorn är bipolär
- du vill använda microstepping
- du kan ställa in strömbegränsning
- du kan ge drivaren kylning och korrekt motormatning

Vanliga fel:

- strömgränsen är inte inställd
- drivaren saknar kylning
- motorn kopplas loss medan drivaren är aktiv
- acceleration saknas
- motormatning och logikmatning blandas ihop
- man tror att motorspänningen ensam avgör om drivaren passar

A4988/DRV8825 är därför inte bara “stegmotor-moduler”. De är strömreglerande drivare och ska behandlas som effektkomponenter.

## LED-drivare och konstant ström

En vanlig LED behöver strömbegränsning. I enkla tester är ett seriemotstånd tillräckligt. Men när du använder många LED, högeffekts-LED eller LED som ska lysa jämnt över varierande matningsspänning blir en LED-drivare bättre.

En LED-drivare kan ge:

- konstant ström
- flera kanaler
- PWM-dimning
- högre effektivitet
- enklare styrning av många LED
- jämnare ljusstyrka mellan kanaler

Det finns flera nivåer av LED-drivning:

| Lösning | Passar för | Begränsning |
|---|---|---|
| GPIO + motstånd | Enstaka indikator-LED | Mycket låg ström |
| Transistor/MOSFET + motstånd | LED-grupp eller strip | Strömmen beror på matning och motstånd |
| Konstantströmsdrivare | Högeffekts-LED eller jämn ljusstyrka | Kräver rätt dimensionering |
| Adresserbar LED | Effekter och många individuella pixlar | Timing, ström och bibliotek |
| LED-matrisdrivare | Många LED i matris | Specifik krets och displaystruktur |

För högeffekts-LED är det sällan bra att bara välja ett lågt motstånd och hoppas. Små variationer i spänning och temperatur kan ge stor skillnad i ström. Därför används konstantströmsdrivare.

För många små LED kan en LED-drivarkrets också minska belastningen på mikrokontrollern. I stället för att uppdatera många pinnar direkt skickar du data via I2C eller SPI till drivaren.

## Relädrivning och induktiva laster

Reläer, solenoider och motorer är induktiva. En induktiv last lagrar energi i ett magnetfält. När strömmen bryts försöker lasten hålla strömmen igång, vilket kan skapa en hög spänningsspik. Den spiken kan skada transistor, MOSFET, drivkrets eller störa mikrokontrollern.

Därför behövs skydd. För DC-reläer och solenoider används ofta en flyback-diod över lasten. Dioden kopplas så att den inte leder när lasten är på, men ger strömmen en säker väg när lasten stängs av.

```text
+V ---- Reläspole ---- transistor/MOSFET ---- GND
       [flyback-diod kopplad parallellt över reläspolen]
```

Diodens riktning är viktig. Sitter den fel blir den en kortslutning när lasten slås på.

Många relämoduler och drivkretsar har redan skydd, men du bör inte anta det utan att kontrollera modulens dokumentation eller kretskortets uppbyggnad.

För induktiva laster gäller:

- använd skyddsdiod eller annan lämplig transientskyddslösning
- separera gärna motor-/relämatning från logikmatning
- använd gemensam jord när styrsignalerna kräver det
- lägg avkopplingskondensatorer nära störande laster
- räkna med startström, inte bara märkström
- testa först med liten last eller strömbegränsad matning

## PCA9685 för många servon

**PCA9685** är inte en kraftdrivare i samma mening som en H-brygga eller MOSFET. Den är en I2C-styrd PWM-driver som ofta används för många servon eller många PWM-kanaler. I praktiken fungerar den som en signalgenerator: mikrokontrollern skickar kommandon via I2C och PCA9685 skapar servopulserna.

Det gör PCA9685 användbar när:

- många servon ska styras från samma projekt
- du vill avlasta mikrokontrollern från många servopulser
- du vill samla servokablar på en modul
- du bygger robotarm, pan-tilt, animatronik eller flera mekaniska indikatorer

Men PCA9685 matar inte servona åt dig på ett magiskt sätt. Servoströmmen måste fortfarande komma från en matning som klarar belastningen. GND måste vara gemensam mellan mikrokontroller, PCA9685 och servomatning.

Kontrollera särskilt:

- servomatningens strömkapacitet
- modulens servospänning jämfört med servonas krav
- gemensam jord
- I2C-adress
- kabeldragning och avkoppling nära servon
- mekaniska stopp så att servon inte står och drar hög ström

## Färdig modul eller lös IC-krets?

I Arduino-projekt finns nästan alltid två vägar: färdig modul eller lös komponent.

En färdig modul är ofta bäst när:

- du vill komma igång snabbt
- kopplingen är sekundär i projektet
- modulen har skruvterminaler, skyddskomponenter eller regulator
- du vill minska risken för felkoppling
- experimentet ska vara lätt att reproducera

En lös IC eller diskret krets är bättre när:

- du vill förstå kretsen på djupet
- projektet ska bli kompakt
- du vill optimera kostnad, ström eller storlek
- du vill bygga ett eget kretskort
- modulen döljer viktiga detaljer

För prototyper och praktisk testmiljö är moduler ofta rimliga. Men du bör fortfarande förstå vad modulen gör. En “motor driver module” kan innehålla en gammal ineffektiv H-brygga, en modern MOSFET-driver, regulator, skyddsdioder, strömbegränsning eller nästan inget skydd alls. Modulens namn räcker inte. Titta på komponentbeteckningen.

## Valguide: vilken drivlösning passar?

| Situation | Bra första val | Kommentar |
|---|---|---|
| En indikator-LED | GPIO + motstånd | Enkel direktdrivning räcker |
| Flera små LED | I/O-expander, shift register eller LED-drivare | Beror på antal och ljusstyrka |
| 12 V LED-strip | Logiknivå-N-MOSFET | Kontrollera ström och kylning |
| Reläspole | Transistor, MOSFET, ULN2803 eller relämodul | Skydd mot induktiv spik krävs |
| Flera reläer | ULN2803 eller relämodul | Praktiskt med flera kanaler |
| Liten DC-motor, en riktning | MOSFET + skydd | PWM kan användas |
| DC-motor, två riktningar | H-brygga/motor-driver | Dimensionera efter startström |
| Stegmotor | Stegmotordrivare | Ställ in strömbegränsning |
| Liten 28BYJ-48-stegmotor | ULN2003-modul | Enkel kitlösning för långsam rörelse |
| Bipolär stegmotor | A4988 eller DRV8825 | Kräver strömgräns, kylning och acceleration |
| Flera servon | PCA9685 + separat servomatning | Driver signalerna, inte servoströmmen |
| DC-motor i enkelt kit | L298N kan fungera för principtest | Ofta ineffektiv och varm jämfört med moderna drivers |
| Solenoid | MOSFET eller ULN2803 | Hög startström och flyback-skydd |
| Högeffekts-LED | Konstantströmsdrivare | Motstånd räcker ofta inte |
| Många kanaler i prototyp | Färdig drivmodul | Snabbt och lätt att felsöka |

Kort beslutsrad:

- Välj **direkt GPIO** bara för mycket små indikatorlaster.
- Välj **MOSFET** när en lågspänd DC-last ska slås av/på eller PWM-styras.
- Välj **DRV8833** när en liten DC-motor behöver två riktningar och effektivare drivning än L298N.
- Välj **L298N** främst när modulen redan finns, lasten är liten nog och värmeförlusten är acceptabel.
- Välj **ULN2003/ULN2803** när många små induktiva eller digitalt styrda kanaler ska hanteras på ett enkelt sätt.

## Jämförelsemönster: samma last med tre drivlösningar

Det här jämförelsemönstret visar tre sätt att styra en last. Välj en säker lågspänningslast, till exempel en liten 5 V- eller 12 V-LED-modul, en liten DC-fläkt eller en relämodul. Undvik nätspänning.

### Vad mönstret visar

Mönstret visar skillnaden mellan:

- direkt GPIO-styrning av en mycket liten indikatorlast
- transistor- eller MOSFET-styrning av en extern last
- färdig drivmodul eller ULN2803-kanal

Det viktiga är att skilja mellan nivåerna styrsignal, drivsteg och last.

### Det här används i exemplet

Du behöver:

- ett Arduino-kompatibelt kort
- en indikator-LED med seriemotstånd
- en liten DC-last, till exempel LED-stripbit, fläkt eller reläspole
- lämplig transistor eller logiknivå-MOSFET
- eventuellt ULN2803 eller färdig drivmodul
- extern lågspänningsmatning för lasten
- kopplingskablar
- multimeter
- skyddsdiod om lasten är induktiv och drivningen inte redan har skydd

### Del A: indikator-LED direkt från pinne

Koppla en enkel LED med seriemotstånd till en digital pinne. Detta är referensfallet: liten last, enkel koppling, låg risk.

```cpp
const int indicatorPin = 6;

void setup() {
  pinMode(indicatorPin, OUTPUT);
}

void loop() {
  digitalWrite(indicatorPin, HIGH);
  delay(300);
  digitalWrite(indicatorPin, LOW);
  delay(300);
}
```

Kontrollera:

- pinne
- motståndsvärde
- ungefärlig LED-ström
- om kortet är 3,3 V eller 5 V

### Del B: extern last med MOSFET

Koppla en lågspänningslast via N-kanals MOSFET i lågsidekoppling. Använd extern matning om lasten kräver mer än kortet bör leverera. Koppla gemensam jord mellan Arduino och lastmatning.

```cpp
const int driverPin = 9;

void setup() {
  pinMode(driverPin, OUTPUT);
}

void loop() {
  for (int level = 0; level <= 255; level += 5) {
    analogWrite(driverPin, level);
    delay(20);
  }

  for (int level = 255; level >= 0; level -= 5) {
    analogWrite(driverPin, level);
    delay(20);
  }
}
```

Kontrollera:

- lastspänning
- uppmätt eller uppskattad lastström
- MOSFET-modell eller modulnamn
- om gate har pulldown
- om lasten behöver flyback-diod

### Del C: flera kanaler med ULN2803 eller modul

Om du har ULN2803, koppla två eller flera små laster till olika kanaler. Annars använd en färdig flerkanalig drivmodul. Målet är att se hur flera utgångar kan styras utan att varje kanal byggs av separata diskreta komponenter.

```cpp
const int outputPins[] = {2, 3, 4};
const int outputCount = 3;

void setup() {
  for (int i = 0; i < outputCount; i++) {
    pinMode(outputPins[i], OUTPUT);
    digitalWrite(outputPins[i], LOW);
  }
}

void loop() {
  for (int i = 0; i < outputCount; i++) {
    digitalWrite(outputPins[i], HIGH);
    delay(250);
    digitalWrite(outputPins[i], LOW);
  }

  delay(500);
}
```

Spara gärna:

- hur många kanaler du använder
- om lastens plus är gemensam
- om drivningen är lågside eller högside
- vad som händer vid uppstart och reset

### Förväntade observationer

Du bör se att direktdrivning är enkel men begränsad. MOSFET-styrning kräver mer koppling men klarar större last och PWM bättre. En flerkanalig driver förenklar när många liknande laster ska styras.

Det viktiga är inte att alla tre lösningar gör exakt samma sak. Det viktiga är att du kan förklara varför varje lösning passar i ett visst läge.

## Riskkontroll före val av drivkrets

Innan du väljer modul eller IC, beskriv lasten som drivkretsen faktiskt ska hantera.

- Vilken spänning behöver lasten?
- Vilken ström drar lasten i normal drift?
- Finns startström, stallström eller andra korta toppar?
- Behöver lasten byta riktning, bromsas eller bara slås av och på?
- Är lasten induktiv och behöver flyback-skydd?
- Behöver styrsignalen vara 3,3 V-kompatibel?
- Hur mycket värme kan drivaren behöva bli av med?
- Vad ska hända vid reset, uppstart och tappad signal?

En drivkrets väljs inte bara efter maxström. Den väljs efter lasttyp, styrsätt, skydd, värme och marginal.

## Vanliga misstag

- **Misstag: Att driva lasten direkt från GPIO.**
  - Varför det händer: Koden fungerar likadant oavsett vad som sitter på pinnen, vilket kan ge intrycket att pinnen är en kraftutgång.
  - Hur du undviker det: Kontrollera alltid lastens ström och använd drivkrets när lasten är mer än en liten indikator-LED.

- **Misstag: Att glömma gemensam jord.**
  - Varför det händer: Lasten har egen matning och styrsignalen verkar separat.
  - Hur du undviker det: Koppla gemensam jord mellan mikrokontroller och drivsteg när styrsignalen inte är galvaniskt isolerad.

- **Misstag: Att välja MOSFET efter tröskelspänning.**
  - Varför det händer: Databladets gate threshold voltage ser ut som den spänning som krävs för att MOSFET:en ska vara på.
  - Hur du undviker det: Kontrollera resistans i påslaget läge vid den gate-spänning du faktiskt använder.

- **Misstag: Att ignorera startström.**
  - Varför det händer: Man tittar på märkströmmen för motor eller last, inte strömmen vid start.
  - Hur du undviker det: Välj drivare och matning med marginal och testa med multimeter eller strömbegränsad matning.

- **Misstag: Att sakna flyback-skydd på induktiv last.**
  - Varför det händer: Reläet eller solenoiden fungerar först, så skyddet verkar onödigt.
  - Hur du undviker det: Använd skyddsdiod, färdig modul med skydd eller drivkrets med inbyggt skydd.

- **Misstag: Att använda gammal H-brygga utan att räkna på förlust.**
  - Varför det händer: Klassiska moduler är billiga och vanliga i exempel.
  - Hur du undviker det: Kontrollera spänningsfall, värme och ström. Välj modern MOSFET-baserad driver när effektivitet är viktig.

- **Misstag: Att tro att en modul alltid är säker.**
  - Varför det händer: Moduler ser färdiga och robusta ut.
  - Hur du undviker det: Identifiera huvudkretsen, läs kopplingsmärkning och kontrollera spänningsnivåer innan du ansluter lasten.

## Felsökning

- Om lasten inte reagerar: kontrollera först gemensam jord, matningsspänning och att styrsignalen faktiskt ändras.
- Om drivaren blir varm: minska lasten, kontrollera databladets strömgränser och se till att MOSFET eller modul är vald med marginal.
- Om mikrokontrollern startar om: separera lastmatning från logikmatning och kontrollera avkoppling nära lasten.
- Om en induktiv last ger störningar: kontrollera frihjulsdiod, snubber, kabellängd och att skyddskomponenten sitter nära lasten.
- Om PWM beter sig märkligt: testa först med låg frekvens och liten last innan du ökar effekt eller komplexitet.

## Snabbreferens

| Drivlösning | Styrtyp | Bra för | Undvik när |
|---|---|---|---|
| GPIO direkt | Av/på | Enstaka indikator-LED | Lasten drar mer än mycket liten ström |
| NPN-transistor | Lågside av/på | Små laster, reläer, buzzers | Effektivitet och hög ström är viktigt |
| N-kanals MOSFET | Lågside av/på/PWM | LED-strippar, DC-laster, solenoider | Du behöver högsidestyrning eller AC |
| ULN2003/ULN2803 | Flera lågsidekanaler | Reläer, små solenoider, LED-grupper, 28BYJ-48 | Låg förlust eller hög ström krävs |
| H-brygga | Riktning och PWM | DC-motorer åt båda håll | Stegmotorer eller stora motorer utan rätt driver |
| L298N | Riktning och PWM | Enkla DC-motortest och äldre kit | Batteridrift, hög ström eller effektivitet är viktigt |
| Stegmotordrivare | STEP/DIR | Stegmotorer | Vanliga DC-motorer eller servon |
| A4988/DRV8825 | STEP/DIR + strömbegränsning | Bipolära stegmotorer | Strömgräns och kylning inte är kontrollerade |
| PCA9685 | I2C till PWM/servopuls | Många servon eller PWM-kanaler | Du tror att den även löser servomatningen |
| Konstantströmsdrivare | Strömreglering | Högeffekts-LED och jämn LED-ljusstyrka | En enkel indikator-LED räcker |
| Färdig modul | Varierar | Snabb prototypning | Du behöver full kontroll, liten storlek eller optimering |

Kort tumregel:

> Om lasten gör ljus, rörelse, ljud eller magnetism med mer än minimal ström ska du anta att den behöver en drivkrets tills du har bevisat motsatsen.

## Säkerhetsruta: drivkretsen skyddar inte mot alla fel

En drivkrets gör det möjligt att styra större laster, men den gör inte automatiskt projektet säkert. Du behöver fortfarande kontrollera maxström, värmeutveckling, polaritet, flyback-skydd, säkring och ledningsdimension.

Om något blir varmt, luktar, blinkar oväntat eller får kortet att starta om ska du bryta matningen och felsöka stegvis med mindre last.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Logik och lastmatning kan vara separata |
| Typiskt gränssnitt | Digital styrsignal, PWM, SPI/I2C för vissa drivare |
| Välj när | lasten kräver mer ström, spänning eller skydd än kortet klarar |
| Välj inte när | du saknar information om lastens elektriska krav |
| Vanliga fel | värme, fel polaritet, saknad kylning, fel jordning |
| Alternativ att överväga | färdig modul, relä, MOSFET, H-brygga |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När du väljer drivkrets för motorer, börja med kapitel 20 och använd detta kapitel för att välja själva kretsfamiljen.
- När lasten är relä, solenoid, LED-list eller annan switchad last, jämför med kapitel 21.
- När drivningen ger värme, spänningsfall eller omstarter, gå vidare till kapitel 34 innan du ändrar koden.
- När felet bara uppstår i det sammansatta projektet, använd felsökningsordningen i kapitel 35.
