# 19. Buzzers, ljudsignaler och enkla ljudutgångar

## Komponentöversikt
I de två föregående kapitlen använde vi ljus som återkoppling: först vanliga LED och RGB-LED, sedan adresserbara LED. Ljus är ofta den enklaste formen av statusvisning, men det kräver att någon tittar på projektet. Ljud fungerar annorlunda. Ett pip, en kort melodi eller en tydlig varningssignal kan dra uppmärksamhet även när användaren inte tittar på displayen, LED-strippen eller den seriella monitorn.

Buzzers och enkla ljudutgångar är därför användbara i många Arduino-projekt:

- larm och varningssignaler
- bekräftelse när en knapp trycks
- statusljud vid start, fel eller färdig mätning
- spel- och interaktionsprojekt
- timer- och påminnelsesystem
- sensorprojekt där ett tröskelvärde ska höras
- testutrustning där ljud visar att något händer

Samtidigt är ljudutgångar lättare att missförstå än de först verkar. En aktiv buzzer, en passiv buzzer, ett piezoelement, en liten högtalare och en förstärkt ljudmodul kan se snarlika ut på ett kopplingsbord men kräva olika kod och olika drivning. Vissa behöver bara HIGH/LOW. Andra behöver en fyrkantsvåg. En del kan drivas direkt från en mikrokontrollerpinne, andra bör drivas via transistor eller förstärkare.

Det här kapitlet hjälper dig välja rätt ljudlösning för rätt typ av Arduino-projekt. Fokus ligger inte på hi-fi-ljud, utan på robusta, begripliga och användbara ljudsignaler.

I praktiken används ljud för återkoppling, larm, knappbekräftelse och enkla statuslägen. De viktigaste valen är komponenttyp, drivning, timerpåverkan, ljudstyrka och om ljudet ska vara diskret eller tydligt varnande.

## Förutsättningar

Det här kapitlet bygger på flera tidigare kapitel:

- digital I/O från kapitel 5
- PWM och tidsstyrning från kapitel 7
- ström, jord och komponentgränser från kapitel 4
- aktuator-tänkandet från kapitel 17 och 18

En ljudutgång är en utenhet, inte en sensor. Den omvandlar elektrisk styrning till fysisk återkoppling. Därför behöver du tänka på samma frågor som för andra aktuatorer:

- Hur mycket ström behöver komponenten?
- Vilken spänning är den avsedd för?
- Räcker mikrokontrollerpinnen?
- Behöver du transistor, motstånd eller förstärkare?
- Är ljudet bara en enkel signal eller ska det bära information?

Det är också viktigt att skilja mellan ljud som **status** och ljud som **innehåll**. Den här boken använder ljud främst som status och återkoppling. När du vill spela upp tal, musik eller inspelat ljud behöver du normalt andra moduler, till exempel en ljudspelarmodul, DAC, I2S-förstärkare eller ett kraftigare kort.

## Grundtyper av enkla ljudutgångar

De vanligaste ljudkomponenterna i Arduino-lådor är små, billiga och ofta dåligt märkta. Börja därför med att identifiera vilken typ du faktiskt har.

| Typ | Typisk styrning | Vanlig användning | Kommentar |
|---|---|---|---|
| Aktiv buzzer | HIGH/LOW | Enkelt pip eller larm | Har inbyggd oscillator. |
| Passiv buzzer | Fyrkantsvåg, ofta `tone()` | Toner och enkla melodier | Kräver signal med frekvens. |
| Piezoelement | Fyrkantsvåg eller analog signal | Pip, klick, enklare toner | Låg ström men ofta svagt ljud. |
| Liten högtalare | Förstärkt ljudsignal | Ljud, toner, enklare uppspelning | Bör normalt inte drivas direkt från pinne. |
| Ljudmodul | Seriellt, knappar eller digital styrning | Uppspelade ljudfiler | Används när riktiga ljudklipp behövs. |

En vanlig källa till fel är att försöka använda `tone()` på en aktiv buzzer och sedan undra varför alla toner låter ungefär likadant. En aktiv buzzer skapar sin egen ton när den får matning. Den kan slås av och på, men du styr normalt inte tonhöjden.

En passiv buzzer har däremot ingen intern oscillator. Den låter när du matar den med en växlande signal. Därför kan du styra frekvensen och skapa olika toner.

## Aktiv buzzer

En aktiv buzzer är den enklaste ljudutgången. Den innehåller elektronik som skapar en ton när den får spänning. Du kan tänka på den som en liten modul som säger: “ge mig matning, så piper jag”.

En typisk koppling är:

- buzzer `+` till digital pinne eller matning via transistor
- buzzer `-` till GND
- gemensam jord med Arduino-kortet

För små aktiva buzzers med låg ström kan en digital pinne ofta räcka för experiment. Men du bör alltid kontrollera komponentens märkning eller datablad. Om den kräver mer ström än pinnen får leverera ska du använda transistor eller MOSFET.

Ett minimalt exempel:

```cpp
const int buzzerPin = 8;

void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  digitalWrite(buzzerPin, HIGH);
  delay(100);
  digitalWrite(buzzerPin, LOW);
  delay(900);
}
```

Det här fungerar som ett enkelt hjärtslag: ett kort pip varje sekund.

### När aktiv buzzer passar

Välj aktiv buzzer när:

- du bara behöver pip, larm eller bekräftelseljud
- ljudet ska vara enkelt och tydligt
- koden ska vara minimal
- tonhöjd inte är viktig
- du vill ha en robust statusindikator

Typiska exempel:

- felindikator
- knappbekräftelse
- färdig mätning
- enkel timer
- startljud
- varning vid låg batterinivå

### När aktiv buzzer inte passar

Välj något annat när:

- du vill spela flera toner
- du vill skapa melodier
- ljudet ska vara diskret eller mjukt
- du behöver ändra frekvens
- du behöver spela ljudfiler
- du behöver högre ljudkvalitet

En aktiv buzzer är bra på att vara tydlig, men dålig på att vara uttrycksfull.

## Passiv buzzer

En passiv buzzer behöver en växlande signal. Arduino-funktionen `tone()` är ofta den enklaste vägen. Den skapar en fyrkantsvåg på vald pinne med vald frekvens.

Exempel:

```cpp
const int buzzerPin = 8;

void setup() {
}

void loop() {
  tone(buzzerPin, 1000);
  delay(200);
  noTone(buzzerPin);
  delay(800);
}
```

Här skapas en ton på 1000 Hz i 200 millisekunder.

`tone()` är praktisk eftersom du slipper hantera pinnen manuellt. Du säger bara vilken frekvens du vill ha. Men funktionen använder timerresurser i mikrokontrollern, och på vissa kort kan det påverka andra funktioner som också använder timers.

### Tonhöjd och frekvens

Tonhöjd styrs av frekvens. Högre frekvens ger ljusare ton. Lägre frekvens ger mörkare ton.

Några ungefärliga exempel:

| Frekvens | Upplevelse | Möjlig användning |
|---|---|---|
| 250 Hz | Låg, dov | Fel eller varning |
| 500 Hz | Tydlig men mjukare | Statussignal |
| 1000 Hz | Klassisk pipton | Bekräftelse eller alarm |
| 2000 Hz | Skarp | Varning som ska märkas |
| 4000 Hz | Mycket skarp | Kort uppmärksamhetssignal |

I praktiken varierar upplevelsen med buzzer, kapsling, avstånd och miljö. En frekvens som är lagom på arbetsbordet kan vara irriterande i ett tyst rum eller för svag i en verkstad.

### När passiv buzzer passar

Välj passiv buzzer när:

- du vill styra tonhöjd
- du vill skapa olika ljudmönster
- du vill göra enkla melodier
- du vill särskilja flera händelser med olika toner
- du vill använda ljud som enkel kodad information

### När passiv buzzer inte passar

Välj något annat när:

- du bara behöver ett enkelt pip och vill minimera kod
- timerkonflikter är ett problem
- ljudet behöver vara starkt
- du behöver spela riktiga ljudfiler
- du behöver analog ljudkvalitet

En passiv buzzer är ofta bästa valet för experiment där ljudet ska bära lite mer information än bara “på” eller “av”.

## Piezoelement

Ett piezoelement är en tunn komponent som böjs mycket lite när spänningen ändras. Den rörelsen kan skapa ljud. Piezoelement används ofta i små buzzers, enkla larm, klickljud och billiga ljudindikatorer.

För Arduino-projekt kan ett piezoelement ofta drivas med en digital signal, men ljudet kan bli svagt. Det kan också vara känsligt för montering. Samma piezoelement kan låta olika beroende på om det ligger löst på bordet, sitter i en kapsling eller är fasttejpat på en yta.

Piezoelement har också en intressant dubbelroll: de kan både skapa ljud och känna vibrationer. I den här delen använder vi dem som ljudutgångar. När de används som sensorer hör de hemma i kapitlet om rörelse, orientering och vibration.

### När piezoelement passar

Välj piezoelement när:

- du vill ha låg strömförbrukning
- ljudet får vara svagt eller lokalt
- komponenten ska vara tunn
- du vill skapa enkla klick eller toner
- du experimenterar med ljud och vibration

### När piezoelement inte passar

Välj något annat när:

- ljudet behöver höras på avstånd
- du behöver jämn ljudnivå
- du behöver bra bas eller fylligt ljud
- du vill spela ljudklipp

## Liten högtalare

En liten högtalare är inte samma sak som en buzzer. Den är byggd för att återge en varierande ljudsignal. Den har ofta låg impedans, till exempel 4 eller 8 ohm. En mikrokontrollerpinne är inte gjord för att driva en sådan last direkt.

Att koppla en liten högtalare direkt mellan en pinne och GND kan ge svagt ljud, distorsion och i värsta fall belasta pinnen mer än den tål. För seriösa experiment bör du använda ett drivsteg, en enkel förstärkarmodul eller en ljudmodul.

Välj liten högtalare när:

- du har en förstärkare eller ljudmodul
- du vill spela mer än enkla pip
- ljudkvalitet är viktigare än minimal koppling
- du använder kort eller moduler som har DAC, I2S eller ljudstöd

Välj buzzer när:

- du bara behöver statusljud
- kopplingen ska vara enkel
- ljudkvalitet inte är viktig
- koden ska vara liten

## LM386 och små högtalare

LM386 är en enkel ljudförstärkarkrets som ofta används i små Arduino- och elektronikexperiment när en liten högtalare ska höras tydligare än vad en mikrokontrollerpinne kan driva. Den finns både som lös krets och som färdig modul med potentiometer, kondensatorer och skruvterminaler.

Tänk på LM386 som ett enkelt förstärkarsteg, inte som en buzzer. En aktiv buzzer skapar sitt eget pip när den får spänning. En passiv buzzer eller piezo behöver en ton- eller PWM-liknande signal. En högtalare med LM386 behöver en ljudsignal som förstärks innan den går till högtalaren.

LM386 passar när:

- du vill driva en liten högtalare i ett enkelt test
- ljudet ska vara starkare än ett piezoelement eller en liten buzzer
- du använder en modul eller krets som redan ger en analog ljudsignal
- du accepterar begränsad ljudkvalitet

LM386 passar sämre när:

- du bara behöver ett kort statuspip
- du vill spela upp ljud med hög kvalitet
- du behöver mycket uteffekt
- brus, volym eller strömförbrukning är kritiskt

Var noga med matning, jordning och volym. En enkel förstärkare kan förstärka både önskat ljud och brus. För hög volym kan ge distorsion, störningar eller onödigt hög strömförbrukning. Håll ledningar korta, börja med låg volym och kontrollera modulens rekommenderade koppling innan du ansluter högtalaren.

## Direktdrivning eller drivsteg

Frågan “kan jag koppla den direkt till pinnen?” dyker upp ofta. Svaret är: ibland, men kontrollera alltid strömmen.

En digital pinne kan bara leverera begränsad ström. Exakta gränser beror på kort och mikrokontroller. Dessutom kan hela kortet ha en totalgräns för hur mycket ström alla pinnar tillsammans får leverera. Det är därför en bra vana att inte behandla GPIO-pinnar som strömkällor.

För små buzzers i prototyper kan direktdrivning vara okej. För starkare ljud, 5 V-buzzers, okända moduler eller flera ljudutgångar bör du använda transistor eller MOSFET.

En enkel NPN-transistorlösning kan beskrivas så här:

- buzzer `+` till extern eller kortets lämpliga matning
- buzzer `-` till transistorns kollektor
- transistorns emitter till GND
- Arduino-pinne via basmotstånd till transistorns bas
- gemensam jord mellan Arduino och matning

För induktiva komponenter behövs skyddsdiod. En vanlig piezo- eller liten elektronisk buzzer är normalt inte samma typ av induktiv last som ett relä eller en motor, men färdiga moduler kan innehålla mer elektronik än man ser. Vid osäkerhet: börja med datablad eller modulbeskrivning.

## Kodmönster: enkla pip

För en aktiv buzzer räcker digital styrning:

```cpp
const int buzzerPin = 8;

void beep(int durationMs) {
  digitalWrite(buzzerPin, HIGH);
  delay(durationMs);
  digitalWrite(buzzerPin, LOW);
}

void setup() {
  pinMode(buzzerPin, OUTPUT);
  beep(100);
}

void loop() {
}
```

Det är enkelt, men `delay()` blockerar programmet. Under pipet kan programmet inte läsa sensorer, uppdatera LED, hantera knappar eller kommunicera.

För ett startpip eller en enstaka testsketch är det acceptabelt. I ett större system bör du undvika blockering.

## Kodmönster: toner med passiv buzzer

För en passiv buzzer kan du skapa ett kort pip med `tone()`:

```cpp
const int buzzerPin = 8;

void setup() {
  tone(buzzerPin, 1000, 100);
}

void loop() {
}
```

Den tredje parametern anger varaktighet i millisekunder. På många Arduino-miljöer fortsätter programmet medan tonen spelas, men det är ändå bra att vara tydlig med tillståndet om du bygger mönster.

Ett enkelt felpip:

```cpp
const int buzzerPin = 8;

void errorBeep() {
  tone(buzzerPin, 300, 150);
  delay(200);
  tone(buzzerPin, 300, 150);
  delay(200);
  tone(buzzerPin, 300, 150);
  delay(200);
}

void setup() {
  errorBeep();
}

void loop() {
}
```

Det fungerar, men är fortfarande blockande på grund av `delay()`.

## Icke-blockerande ljudmönster

När ljud ska vara en del av ett större system behöver det kunna köras samtidigt som resten av programmet. Då bör du bygga ett litet tillståndsmaskinsmönster.

Målet är att programmet ska kunna säga “spela det här mönstret”, och sedan låta `loop()` fortsätta läsa sensorer och uppdatera andra utenheter.

Exempel med aktiv buzzer:

```cpp
const int buzzerPin = 8;

struct BeepStep {
  bool on;
  unsigned long durationMs;
};

const BeepStep okPattern[] = {
  {true, 80},
  {false, 120},
  {true, 80},
  {false, 0}
};

const BeepStep errorPattern[] = {
  {true, 250},
  {false, 150},
  {true, 250},
  {false, 150},
  {true, 250},
  {false, 0}
};

const BeepStep* currentPattern = nullptr;
int currentStep = 0;
unsigned long stepStartedAt = 0;
bool soundActive = false;

void startPattern(const BeepStep pattern[]) {
  currentPattern = pattern;
  currentStep = 0;
  stepStartedAt = millis();
  soundActive = true;
  digitalWrite(buzzerPin, currentPattern[currentStep].on ? HIGH : LOW);
}

void updateSound() {
  if (!soundActive || currentPattern == nullptr) {
    return;
  }

  unsigned long duration = currentPattern[currentStep].durationMs;

  if (duration == 0) {
    digitalWrite(buzzerPin, LOW);
    soundActive = false;
    currentPattern = nullptr;
    return;
  }

  if (millis() - stepStartedAt >= duration) {
    currentStep++;
    stepStartedAt = millis();

    if (currentPattern[currentStep].durationMs == 0) {
      digitalWrite(buzzerPin, LOW);
      soundActive = false;
      currentPattern = nullptr;
      return;
    }

    digitalWrite(buzzerPin, currentPattern[currentStep].on ? HIGH : LOW);
  }
}

void setup() {
  pinMode(buzzerPin, OUTPUT);
  startPattern(okPattern);
}

void loop() {
  updateSound();

  // Här kan resten av systemet läsa sensorer, hantera knappar
  // och uppdatera displayer utan att ljudmönstret blockerar.
}
```

Det här är mer kod än `delay()`, men det skalar bättre. Samma idé kan användas för LED-mönster, reläsekvenser och displayuppdateringar.

## Icke-blockerande toner

För passiv buzzer behöver varje steg även innehålla frekvens. Frekvensen 0 kan betyda paus.

```cpp
const int buzzerPin = 8;

struct ToneStep {
  int frequencyHz;
  unsigned long durationMs;
};

const ToneStep readyPattern[] = {
  {800, 80},
  {0, 80},
  {1200, 120},
  {0, 0}
};

const ToneStep warningPattern[] = {
  {400, 200},
  {0, 100},
  {400, 200},
  {0, 100},
  {400, 200},
  {0, 0}
};

const ToneStep* currentPattern = nullptr;
int currentStep = 0;
unsigned long stepStartedAt = 0;
bool tonePatternActive = false;

void applyToneStep(const ToneStep& step) {
  if (step.frequencyHz > 0) {
    tone(buzzerPin, step.frequencyHz);
  } else {
    noTone(buzzerPin);
  }
}

void startTonePattern(const ToneStep pattern[]) {
  currentPattern = pattern;
  currentStep = 0;
  stepStartedAt = millis();
  tonePatternActive = true;
  applyToneStep(currentPattern[currentStep]);
}

void updateTonePattern() {
  if (!tonePatternActive || currentPattern == nullptr) {
    return;
  }

  unsigned long duration = currentPattern[currentStep].durationMs;

  if (duration == 0) {
    noTone(buzzerPin);
    tonePatternActive = false;
    currentPattern = nullptr;
    return;
  }

  if (millis() - stepStartedAt >= duration) {
    currentStep++;
    stepStartedAt = millis();

    if (currentPattern[currentStep].durationMs == 0) {
      noTone(buzzerPin);
      tonePatternActive = false;
      currentPattern = nullptr;
      return;
    }

    applyToneStep(currentPattern[currentStep]);
  }
}

void setup() {
  startTonePattern(readyPattern);
}

void loop() {
  updateTonePattern();
}
```

Detta mönster gör det lätt att lägga till olika ljud för olika systemhändelser.

## Typiska ljudkoder i ett projekt

Ett bra ljudsystem ska vara enkelt att tolka. Det ska inte låta för att det går, utan ge kort och konsekvent återkoppling när visuell status inte räcker.

| Händelse | Ljudmönster | Praktisk kommentar |
|---|---|---|
| Start klar | två korta stigande pip | Bekräftar att systemet är redo. |
| Knapp bekräftad | ett mycket kort pip | Ska vara diskret och inte kännas som larm. |
| Fel | tre korta pip | Använd samma felmönster genom hela projektet. |
| Larm | upprepade pip med paus | Bör kombineras med visuell status och kunna stoppas. |
| Låg batterinivå | återkommande kort pip med lång paus | Ska inte tömma batteriet snabbare än nödvändigt. |
| Tyst läge | endast visuell status | Viktigt i miljöer där ljud stör eller kan misstolkas. |

Det viktiga är inte exakt vilka toner du väljer, utan att samma mönster betyder samma sak genom hela projektet. Undvik många nästan likadana signaler. Om användaren måste minnas sju olika pipmönster blir ljudsystemet snabbt störande i stället för hjälpsamt.

## Ljud kopplat till sensordata

En ljudutgång blir mer intressant när den kopplas till sensorer. Du kan till exempel låta frekvens, tempo eller mönster förändras med ett mätvärde.

Exempel:

- avståndssensor: snabbare pip när objektet kommer närmare
- temperatur: varningspip över tröskel
- ljussensor: tonhöjd följer ljusnivå
- strömsensor: ljud vid för hög belastning
- rörelsesensor: kort bekräftelse vid aktivitet
- timer: accelererande pip när tiden tar slut

Ett enkelt exempel med analog sensor och passiv buzzer:

```cpp
const int sensorPin = A0;
const int buzzerPin = 8;

void setup() {
}

void loop() {
  int raw = analogRead(sensorPin);

  int frequency = map(raw, 0, 1023, 200, 2000);

  tone(buzzerPin, frequency);
  delay(20);
}
```

Det här är medvetet enkelt. Det visar principen: ett mätvärde översätts till en tonhöjd. I ett riktigt projekt bör du lägga till filtrering, trösklar och kanske bara spela ljud när värdet är relevant.

För många system är det bättre att inte låta hela tiden. Använd trösklar:

```cpp
const int sensorPin = A0;
const int buzzerPin = 8;
const int threshold = 700;

void setup() {
}

void loop() {
  int raw = analogRead(sensorPin);

  if (raw > threshold) {
    tone(buzzerPin, 1200);
  } else {
    noTone(buzzerPin);
  }

  delay(20);
}
```

Även här är nästa steg att ta bort `delay()` om programmet ska göra mer samtidigt.

## Volym och upplevd ljudstyrka

Många små buzzers saknar enkel volymkontroll. En aktiv buzzer låter ungefär som den låter vid sin märkspänning. En passiv buzzer kan ibland upplevas starkare eller svagare beroende på frekvens, eftersom komponenten har resonansområden där den låter mer.

Du kan påverka ljudet genom:

- matningsspänning, inom komponentens tillåtna område
- fysisk montering
- kapsling
- hål eller öppning framför buzzer
- avstånd till användaren
- val av frekvens
- mönstrets längd och repetition
- drivsteg

För diskreta användargränssnitt är ett kort pip ofta bättre än ett långt. Ett system som piper för ofta kommer användaren vilja stänga av.

En bra designregel är:

> Ljud ska användas när användaren behöver reagera, inte varje gång programmet lyckas göra något internt.

## Elektriska hänsyn

För buzzers och ljudutgångar gäller samma grundprinciper som för andra utenheter.

Kontrollera alltid:

- märkspänning
- strömförbrukning
- polaritet
- om komponenten är aktiv eller passiv
- om den kan drivas direkt från pinne
- om den behöver transistor, MOSFET eller förstärkare
- om kortet använder 3,3 V eller 5 V-logik
- om extern matning kräver gemensam jord

En 5 V aktiv buzzer kan ibland låta svagt eller inte alls från ett 3,3 V-kort. Det betyder inte att koden är fel. Det kan vara ett nivå- eller matningsproblem. Lösningen kan vara en 3,3 V-kompatibel buzzer, ett drivsteg eller annan komponent.

Om du använder extern matning till buzzern och styr via transistor måste Arduino-kortet och den externa matningen normalt dela jord. Utan gemensam jord har styrsignalen ingen gemensam referens.

## Timerkonflikter och kortskillnader

`tone()` är bekväm, men den är inte magisk. Den använder hårdvaru- eller mjukvaruresurser beroende på plattform. På vissa kort kan den påverka PWM på vissa pinnar eller krocka med bibliotek som använder timers. På andra kort fungerar den annorlunda eller har andra begränsningar.

Det här är särskilt viktigt när du kombinerar ljud med:

- servon
- PWM-baserad motorstyrning
- adresserbara LED
- IR-sändning
- tidskritiska bibliotek
- sleep-lägen
- trådlös kommunikation

Om ett ljudexempel fungerar ensamt men slutar fungera när du lägger till ett annat bibliotek bör du misstänka resurskonflikt. Testa då:

- annan pinne
- annan buzzerstrategi
- kortare ljud
- annan biblioteksversion
- plattformsspecifik dokumentation
- separat ljudmodul

I ett referensvänligt projekt bör du dokumentera när ljudfunktionen använder `tone()` och när den bara använder digital HIGH/LOW.

## När du bör välja vad

| Behov | Rekommenderad lösning | Skäl |
|---|---|---|
| Enkelt pip | Aktiv buzzer | Minimal kod och enkel styrning. |
| Olika toner | Passiv buzzer | Frekvensen kan styras. |
| Mycket låg ström | Piezoelement | Kan vara strömsnålt och tunt. |
| Starkare ljud | Buzzer med drivsteg | Skyddar mikrokontrollerpinnen. |
| Ljudfiler | Ljudspelarmodul | En Arduino-pinne räcker inte för inspelat ljud. |
| Bättre ljudkvalitet | Förstärkare och högtalare | Kräver riktig ljudkedja. |
| Diskret UI-feedback | Kort buzzerpip | Snabb och lätt att tolka. |
| Avancerat ljud | ESP32/RP2040 med ljudbibliotek eller modul | Mer beräkningskraft och bättre gränssnitt. |

Det praktiska valet är ofta enklare än tabellen antyder: börja med aktiv buzzer om du bara behöver larm. Välj passiv buzzer om ljudet ska bära flera betydelser.

## Referensmönster: ljudsignaler för systemstatus

Det här referensmönstret visar ett litet ljudsystem som kan återanvändas i senare projekt. Det har tre signaler:

- start klar
- varning
- fel

Mönstret kan köras med en passiv buzzer på en digital pinne. Om din buzzer kräver mer ström använder du transistor eller en färdig drivmodul.

### Det här används i exemplet

- Arduino-kompatibelt kort
- passiv buzzer eller piezoelement
- kopplingskablar
- eventuellt motstånd eller drivsteg beroende på komponent
- valfri knapp eller sensor för att trigga olika ljud

### Koppling

För en liten passiv buzzer i ett enkelt test:

- buzzer `+` till digital pinne 8
- buzzer `-` till GND

Om din modul har märkning som `S`, `+` och `-`:

- `S` till digital pinne 8
- `+` till 5 V eller 3,3 V enligt modulens krav
- `-` till GND

Kontrollera alltid modulens märkning. Vissa moduler har inbyggd transistor, andra är bara en komponent på ett litet kretskort.

### Kod

```cpp
const int buzzerPin = 8;
const int buttonPin = 2;

struct ToneStep {
  int frequencyHz;
  unsigned long durationMs;
};

const ToneStep readyPattern[] = {
  {800, 80},
  {0, 80},
  {1200, 120},
  {0, 0}
};

const ToneStep warningPattern[] = {
  {700, 150},
  {0, 120},
  {700, 150},
  {0, 120},
  {700, 150},
  {0, 0}
};

const ToneStep errorPattern[] = {
  {300, 300},
  {0, 150},
  {300, 300},
  {0, 150},
  {300, 300},
  {0, 0}
};

const ToneStep* currentPattern = nullptr;
int currentStep = 0;
unsigned long stepStartedAt = 0;
bool patternActive = false;

bool lastButtonState = HIGH;
int pressCount = 0;

void applyStep(const ToneStep& step) {
  if (step.frequencyHz > 0) {
    tone(buzzerPin, step.frequencyHz);
  } else {
    noTone(buzzerPin);
  }
}

void startPattern(const ToneStep pattern[]) {
  currentPattern = pattern;
  currentStep = 0;
  stepStartedAt = millis();
  patternActive = true;
  applyStep(currentPattern[currentStep]);
}

void updatePattern() {
  if (!patternActive || currentPattern == nullptr) {
    return;
  }

  unsigned long duration = currentPattern[currentStep].durationMs;

  if (duration == 0) {
    noTone(buzzerPin);
    patternActive = false;
    currentPattern = nullptr;
    return;
  }

  if (millis() - stepStartedAt >= duration) {
    currentStep++;
    stepStartedAt = millis();

    if (currentPattern[currentStep].durationMs == 0) {
      noTone(buzzerPin);
      patternActive = false;
      currentPattern = nullptr;
      return;
    }

    applyStep(currentPattern[currentStep]);
  }
}

void handleButton() {
  bool buttonState = digitalRead(buttonPin);

  if (lastButtonState == HIGH && buttonState == LOW) {
    pressCount++;

    if (pressCount % 3 == 1) {
      startPattern(readyPattern);
    } else if (pressCount % 3 == 2) {
      startPattern(warningPattern);
    } else {
      startPattern(errorPattern);
    }
  }

  lastButtonState = buttonState;
}

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  startPattern(readyPattern);
}

void loop() {
  handleButton();
  updatePattern();
}
```

### Förväntat resultat

När systemet startar hörs en kort “redo”-signal. Varje gång du trycker på knappen växlar programmet mellan redo-, varnings- och felsignal. Eftersom ljudmönstret är icke-blockerande kan du senare lägga till sensorläsning, LED-status eller displayuppdatering i samma `loop()`.

### Variationer

Du kan bygga vidare genom att:

- byta knapp mot en analog sensor och trigga varning vid tröskelvärde
- lägga till LED-status som följer samma händelse
- skapa ett diskret nattläge med kortare toner
- göra felmönstret långsammare men lägre i frekvens
- lägga till seriell loggning när ljudmönster startar
- skapa en global inställning för ljud av/på

## Vanliga misstag

- **Misstag: Att använda fel typ av buzzer.**
  - Varför det händer: Aktiva och passiva buzzers kan se nästan likadana ut.
  - Hur man undviker det: Testa först med HIGH/LOW. Om den piper med konstant matning är den aktiv. Om den kräver frekvens är den passiv.

- **Misstag: Att koppla en högtalare direkt till en GPIO-pinne.**
  - Varför det händer: Högtalare och buzzers blandas ofta ihop.
  - Hur man undviker det: Använd buzzer för enkla pip och förstärkare eller ljudmodul för högtalare.

- **Misstag: Att låta ljudkod blockera hela programmet.**
  - Varför det händer: `delay()` är det enklaste sättet att skapa pipsekvenser.
  - Hur man undviker det: Använd `millis()` och tillståndsmaskin när ljudet ska ingå i ett större system.

- **Misstag: Att välja för skarpa eller för långa ljud.**
  - Varför det händer: På arbetsbordet känns det bra att ljudet hörs tydligt.
  - Hur man undviker det: Testa i den miljö där projektet ska användas och gör ljudet kortare än du först tror.

- **Misstag: Att glömma gemensam jord vid extern matning.**
  - Varför det händer: Buzzern får egen matning men styrsignalen saknar referens.
  - Hur man undviker det: Koppla GND från Arduino och extern matning tillsammans när styrningen kräver gemensam referens.

- **Misstag: Att anta att `tone()` fungerar likadant på alla kort.**
  - Varför det händer: Arduino-API:t döljer många plattformsskillnader.
  - Hur man undviker det: Testa ljudfunktionen på målplattformen och dokumentera eventuella timerkonflikter.

## Felsök ljudsignalen

Använd punkterna när ljudet är tyst, svagt, felaktigt eller stör annan kod.

- Kontrollera först om komponenten är aktiv buzzer, passiv buzzer, piezoelement eller liten högtalare.
- En aktiv buzzer kan ofta testas med enkel HIGH/LOW-styrning.
- En passiv buzzer eller piezo kräver normalt en ton eller fyrkantsvåg, till exempel med `tone()`.
- En liten högtalare bör normalt inte drivas direkt från en GPIO-pinne.
- Kontrollera polaritet och modulmärkning innan du felsöker koden.
- Om annan kod beter sig konstigt samtidigt som ljudet spelas: kontrollera timerkonflikter och blockerande väntan.
## Snabb sammanfattning

- En aktiv buzzer piper när den får matning och styrs ofta med HIGH/LOW.
- En passiv buzzer kräver en växlande signal och passar för olika toner.
- `tone()` är ett enkelt sätt att skapa fyrkantsvågstoner, men kan använda timerresurser.
- Små buzzers kan ibland drivas direkt från en pinne, men starkare ljudutgångar bör ha drivsteg.
- En liten högtalare är inte samma sak som en buzzer och bör normalt använda förstärkare.
- Ljudmönster bör vara korta, konsekventa och lätta att tolka.
- Icke-blockerande ljudkod gör att systemet kan läsa sensorer och uppdatera andra utenheter samtidigt.
- Gemensam jord, rätt spänning och rätt komponenttyp är vanligare felkällor än själva koden.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Beror på buzzer-modul |
| Typiskt gränssnitt | Digital I/O eller PWM/tone |
| Välj när | du behöver enkel ljudåterkoppling |
| Välj inte när | du behöver ljudkvalitet, musik eller inspelning |
| Vanliga fel | aktiv/passiv förväxlas, för hög ström, blockerande melodikod |
| Alternativ att överväga | LED-feedback, display, I2S-ljud på kraftigare kort |

Använd referensrutan som en snabb kontroll innan du bygger projektet. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat


- Använd kapitel 7 när ljudet kräver tonhöjd, timing eller icke-blockerande signaler.
- Använd kapitel 21 när ljudmodulen drar mer ström än en GPIO-pinne klarar eller behöver transistor/MOSFET.
- Använd kapitel 34 när ljudet stör andra delar av projektet eller när matningen faller vid högre volym.
