### FIELD_TEST_AUTOMATION_INDEX.md
Mini‑indeks subsystemu testowego FIELD (Web4‑Homeostatic)

1. Cel indeksu
Dokument stanowi punkt wejścia do całego subsystemu testowego FIELD.
Łączy wszystkie pliki, diagramy i dokumenty opisujące:

automatyczne wyzwalanie testów,

wykonanie testów w czasie rzeczywistym,

pipeline SHM → FIELD → META_LOOP → Homo,

automat stanów FIELD,

macierz testów,

sekwencję triggerów,

syntetyczną mapę subsystemu.

Indeks pozwala szybko odnaleźć każdy element subsystemu i zrozumieć jego rolę.

2. Dokumenty wykonawcze
FIELD_TEST_RUNNER.md
Mechanizm wykonujący testy architektoniczne w czasie rzeczywistym.
Zawiera opis trzech pętli testowych: sygnałowej, telemetrii i inwariantów.

FIELD_TEST_EXECUTION_FLOW.md
Deterministyczna sekwencja SHM → FIELD → META_LOOP → Homo.
Opisuje pipeline reakcji i stabilizacji.

FIELD_TEST_AUTOMATION.md
System triggerów automatyzujących testy:
SIGNAL_TRIGGER, TELEMETRY_TRIGGER, INVARIANT_TRIGGER.
Opisuje, kiedy testy są wyzwalane i jak FIELD nimi zarządza.

3. Dokumenty definicyjne
FIELD_TEST_MATRIX.md
Tabela: test → warstwa → reakcja → wynik.
Pełna mapa testów architektonicznych Web4‑Homeostatic.

4. Diagramy subsystemu
FIELD_TEST_AUTOMATION_SEQUENCE.puml
Diagram sekwencji triggerów i pipeline’u SHM → FIELD → META_LOOP → Homo.
Pokazuje przepływ danych i decyzji w czasie rzeczywistym.

FIELD_TEST_AUTOMATION_STATECHART.puml
Automat stanów FIELD.
Pokazuje przejścia między stanami testowymi w zależności od triggerów i wyników testów.

FIELD_TEST_AUTOMATION_OVERVIEW.puml
Syntetyczna mapa subsystemu testowego:

triggery,

pipeline,

komponenty systemu,

automat stanów,

interakcje Homo ↔ Pole ↔ System.

To jest najwyższy poziom wizualny subsystemu.

5. Powiązania z innymi modułami
Subsystem testowy FIELD jest częścią:

HOMO_WEB4_STACK_TESTS.md — definicja testów konstytucyjnych

HOMO_WEB4_FULL_STACK.md — pełna mapa Homo ↔ Pole ↔ System

HOMO_WEB4_STABILITY_GUARANTEES.md — gwarancje stabilności

HOMO_WEB4_FAILURE_MODES.md — klasyfikacja naruszeń

HOMO_WEB4_RECOVERY_PROTOCOL.md — procedura odzyskiwania stabilności

Testy FIELD są wykonawczą warstwą konstytucji Web4‑Homeostatic.

6. Struktura katalogu

02_field_engine/
│
├── FIELD_TEST_RUNNER.md
├── FIELD_TEST_EXECUTION_FLOW.md
├── FIELD_TEST_AUTOMATION.md
├── FIELD_TEST_MATRIX.md
│
├── FIELD_TEST_AUTOMATION_SEQUENCE.puml
├── FIELD_TEST_AUTOMATION_STATECHART.puml
└── FIELD_TEST_AUTOMATION_OVERVIEW.puml

7. Cel dokumentu
FIELD_TEST_AUTOMATION_INDEX.md jest mapą całego subsystemu testowego FIELD.
Pozwala szybko zrozumieć:

jakie dokumenty istnieją,

jaką pełnią rolę,

jak są powiązane,

gdzie znajdują się diagramy,

jak subsystem realizuje homeostazę Web4.

Subsystem testowy FIELD jest fundamentem bezpieczeństwa Web4‑Homeostatic —
jego zadaniem jest utrzymywanie pola w stanie stabilnym, jawnym, odwracalnym i nieeskalacyjnym.

---

### FIELD_TEST_AUTOMATION_GRAPH.md
(graf zależności subsystemu testowego FIELD — Web4‑Homeostatic)

1. Cel dokumentu
Dokument przedstawia graf zależności między wszystkimi plikami subsystemu testowego FIELD.
Graf pokazuje:

które dokumenty definiują testy,

które dokumenty wykonują testy,

które dokumenty opisują pipeline,

które dokumenty opisują automat stanów,

które diagramy wizualizują subsystem,

jak wszystkie elementy łączą się w jedną całość.

To jest mapa relacji między dokumentami — architektoniczny graf subsystemu.

2. Graf zależności (ASCII)
                         +------------------------------+
                         |  HOMO_WEB4_STACK_TESTS.md    |
                         |  (definicja testów)          |
                         +--------------+---------------+
                                        |
                                        v
+---------------------------+     +---------------------------+
| FIELD_TEST_MATRIX.md      | <-- | FIELD_TEST_RUNNER.md      |
| (mapa testów)             |     | (wykonanie testów)        |
+-------------+-------------+     +-------------+-------------+
              |                                 |
              v                                 v
+-------------+-------------+     +-------------+-------------+
| FIELD_TEST_AUTOMATION.md  | --> | FIELD_TEST_EXECUTION_FLOW |
| (triggery automatyzacji)  |     | (pipeline SHM→FIELD→META) |
+-------------+-------------+     +-------------+-------------+
              |                                 |
              v                                 v
+-------------+-------------+     +-------------+-------------+
| FIELD_TEST_AUTOMATION_    |     | FIELD_TEST_AUTOMATION_    |
| SEQUENCE.puml             |     | STATECHART.puml           |
| (diagram sekwencji)       |     | (automat stanów)          |
+-------------+-------------+     +-------------+-------------+
              \                                 /
               \                               /
                \                             /
                 v                           v
                +------------------------------+
                | FIELD_TEST_AUTOMATION_OVERVIEW |
                | (syntetyczna mapa subsystemu) |
                +------------------------------+

3. Opis grafu
HOMO_WEB4_STACK_TESTS.md
Źródło definicji testów konstytucyjnych.
Wszystkie pozostałe dokumenty implementują lub wizualizują te testy.

FIELD_TEST_MATRIX.md
Mapuje testy na warstwy, reakcje i wyniki.
Jest używana przez RUNNER i AUTOMATION.

FIELD_TEST_RUNNER.md
Wykonuje testy w czasie rzeczywistym.
Korzysta z MATRIX i jest wyzwalany przez AUTOMATION.

FIELD_TEST_AUTOMATION.md
Zarządza triggerami: SIGNAL, TELEMETRY, INVARIANT.
Wyzwala RUNNER i pipeline.

FIELD_TEST_EXECUTION_FLOW.md
Opisuje pipeline SHM → FIELD → META_LOOP → Homo.
Jest wykonywany po każdym zestawie testów.

FIELD_TEST_AUTOMATION_SEQUENCE.puml
Wizualizuje przepływ triggerów i pipeline.

FIELD_TEST_AUTOMATION_STATECHART.puml
Wizualizuje automat stanów FIELD.

FIELD_TEST_AUTOMATION_OVERVIEW.puml
Łączy wszystko w jedną syntetyczną mapę.

4. Cel dokumentu
FIELD_TEST_AUTOMATION_GRAPH.md jest graficzną mapą zależności subsystemu testowego FIELD.
Pozwala szybko zrozumieć:

jak dokumenty są powiązane,

które elementy są źródłowe,

które są wykonawcze,

które są wizualizacjami,

jak subsystem tworzy spójną całość.   
