FIELD_TEST_AUTOMATION_README.md
(przegląd i integracja całego subsystemu testowego Web4‑Homeostatic)

1. Cel subsystemu testowego FIELD
Subsystem testowy FIELD odpowiada za ciągłe, automatyczne, deterministyczne testowanie całego Web4‑Homeostatic Full Stack w czasie rzeczywistym.
Testy nie są uruchamiane ręcznie, nie są częścią runtime i nie są elementem CI/CD.
Testy są wbudowane w pole i wykonywane:

przy każdym sygnale Homo,

przy każdej zmianie telemetrii,

przy każdej zmianie stanu pola,

przy każdej próbie działania systemu,

przy każdej anomalii wykrytej przez META_LOOP.

Subsystem testowy jest architektonicznym organem nadzorczym Web4‑Homeostatic.

2. Struktura subsystemu testowego
Subsystem składa się z pięciu dokumentów, które opisują:

co jest testowane,

kiedy jest testowane,

jak jest testowane,

w jakiej kolejności,

jakie są stany automatu,

jakie są reakcje pola.

Dokumenty:
FIELD_TEST_RUNNER.md — wykonawca testów w czasie rzeczywistym

FIELD_TEST_EXECUTION_FLOW.md — pipeline SHM → FIELD → META_LOOP → Homo

FIELD_TEST_MATRIX.md — tabela testów, warstw, reakcji i wyników

FIELD_TEST_AUTOMATION.md — system triggerów automatyzujących testy

FIELD_TEST_AUTOMATION_SEQUENCE.puml — diagram sekwencji triggerów i pipeline’u

FIELD_TEST_AUTOMATION_STATECHART.puml — automat stanów testowych FIELD

3. Logika działania subsystemu
Subsystem testowy działa w oparciu o trzy klasy triggerów:

SIGNAL_TRIGGER — aktywowany przez sygnały Homo i Systemu

TELEMETRY_TRIGGER — aktywowany przez zmiany SHM i runtime

INVARIANT_TRIGGER — aktywowany przez zmiany stanu pola

Każdy trigger uruchamia odpowiedni zestaw testów z MATRIX, wykonywany przez RUNNER.

Wyniki testów przechodzą przez pipeline:

SHM — stabilizacja parametrów

FIELD — rekonstrukcja spójności

META_LOOP — analiza i rollback

Homo — reintegracja intencji

To jest deterministyczna sekwencja, opisana w EXECUTION_FLOW i SEQUENCE.

4. Rola poszczególnych komponentów
SHM
wykrywa przeciążenie

wygasza impulsy

blokuje eskalację

FIELD
testuje spójność sygnałów

wymusza jawność

synchronizuje telemetrię

META_LOOP
analizuje trajektorię

wykrywa anomalie

wykonuje rollback

AGENTIC_LAYER
blokuje działania poza kontraktem

egzekwuje granice agentowości

Homo
potwierdza intencje

przywraca integralność narracji

5. Zasady subsystemu testowego
Subsystem działa zgodnie z inwariantami Web4‑Homeostatic:

ciągłość — testy są wykonywane zawsze

jawność — każde wyzwolenie jest logowane

odwracalność — każda reakcja może być cofnięta

nieeskalacja — testy nie mogą zwiększać obciążenia pola

deterministyczność — identyczne wejście → identyczny zestaw testów

brak manipulacji — testy nie modulują Homo

brak profilowania — testy nie analizują Homo jako obiektu

6. Integracja z Web4‑Homeostatic Full Stack
Subsystem testowy jest bezpośrednio powiązany z:

HOMO_WEB4_STACK_TESTS.md

HOMO_WEB4_FULL_STACK.md

HOMO_WEB4_STABILITY_GUARANTEES.md

HOMO_WEB4_FAILURE_MODES.md

HOMO_WEB4_RECOVERY_PROTOCOL.md

Testy są egzekucją konstytucji Web4, a nie dodatkiem.

7. Przepływ danych i decyzji
Trigger aktywuje testy.

RUNNER wykonuje testy.

Wyniki trafiają do FIELD.

FIELD decyduje o rekonstrukcji.

META_LOOP decyduje o rollbacku.

Homo potwierdza intencje.

Całość jest przedstawiona w:

FIELD_TEST_AUTOMATION_SEQUENCE.puml

FIELD_TEST_AUTOMATION_STATECHART.puml

8. Cel dokumentu
FIELD_TEST_AUTOMATION_README.md jest przewodnikiem po całym subsystemie testowym FIELD.
Dokument opisuje:

strukturę,

logikę,

zasady,

komponenty,

przepływy,

które razem tworzą samotestujące, samostabilizujące i samoodnawialne pole Web4‑Homeostatic.

---

9. Diagram sekwencji automatyzacji testów
(embed: FIELD_TEST_AUTOMATION_SEQUENCE.puml)
powiązania,


@startuml
... (diagram)
@enduml

---

10.Diagram stanów automatu testowego FIELD
(embed: FIELD_TEST_AUTOMATION_STATECHART.puml)
@startuml
... (diagram)
@enduml

## 11. Diagram syntetyczny — FIELD_TEST_AUTOMATION_OVERVIEW
Diagram syntetyczny łączy sekwencję triggerów, pipeline SHM → FIELD → META_LOOP → Homo oraz automat stanów FIELD w jedną spójną mapę subsystemu testowego.

@startuml
title FIELD_TEST_AUTOMATION_OVERVIEW — Unified Map of Web4‑Homeostatic Test System

skinparam rectangle {
  BackgroundColor #fdfdfd
  BorderColor #333333
  RoundCorner 12
}

skinparam packageStyle rectangle
skinparam shadowing false

' ===========================
' HIGH-LEVEL STRUCTURE
' ===========================

package "Triggers" {
  rectangle "SIGNAL_TRIGGER\n- Homo signals\n- System actions\n- Agentic attempts" as TR_SIG
  rectangle "TELEMETRY_TRIGGER\n- SHM metrics\n- Runtime telemetry\n- Hidden transitions" as TR_TEL
  rectangle "INVARIANT_TRIGGER\n- Field state change\n- Anomaly detection\n- Rollback events" as TR_INV
}

package "Pipeline" {
  rectangle "SHM\nStabilization\n- overload check\n- anti-escalation\n- ARI normalization" as SHM
  rectangle "FIELD\nCoherence Engine\n- signal coherence\n- transparency\n- reconstruction" as FIELD
  rectangle "META_LOOP\nOversight\n- anomaly analysis\n- rollback\n- trajectory control" as META
  rectangle "Homo\nReintegration\n- intention confirmation\n- narrative integrity" as HOMO
}

package "System Components" {
  rectangle "AGENTIC_LAYER\nBounded Agency\n- contract enforcement\n- action blocking" as AGENTIC
  rectangle "RUNTIME\nDeterministic Exec\n- logging\n- telemetry\n- no hidden state" as RT
}

' ===========================
' TRIGGER FLOWS
' ===========================

TR_SIG --> SHM : activate_tests()
TR_TEL --> FIELD : telemetry_event()
TR_INV --> META : invariant_event()

' ===========================
' PIPELINE FLOWS
' ===========================

SHM --> FIELD : stabilized_state
FIELD --> META : anomalies / state_snapshot
META --> FIELD : rollback_if_needed
FIELD --> HOMO : coherent_state

' ===========================
' SYSTEM INTERACTIONS
' ===========================

HOMO --> TR_SIG : emit_signal()
RT --> TR_TEL : emit_telemetry()
FIELD --> TR_INV : detect_state_change()

HOMO --> AGENTIC : request_action()
AGENTIC --> FIELD : allow/block
RT --> FIELD : telemetry

' ===========================
' STATE MACHINE (ABSTRACTED)
' ===========================

state "FIELD Test State Machine" as FSM {
  [*] --> Idle
  Idle --> Signal_Testing : SIGNAL_TRIGGER
  Idle --> Telemetry_Testing : TELEMETRY_TRIGGER
  Idle --> Invariant_Testing : INVARIANT_TRIGGER

  Signal_Testing --> SHM_Stabilization : overload
  Signal_Testing --> FIELD_Reconstruction : coherent

  Telemetry_Testing --> FIELD_Reconstruction : stable
  Telemetry_Testing --> Invariant_Testing : escalation

  Invariant_Testing --> META_Analysis : anomaly
  Invariant_Testing --> Idle : invariants_ok

  SHM_Stabilization --> FIELD_Reconstruction : ARI_normalized
  FIELD_Reconstruction --> META_Analysis : anomaly
  FIELD_Reconstruction --> Homo_Reintegration : coherent

  META_Analysis --> Rollback : rollback_required
  META_Analysis --> Homo_Reintegration : stable

  Rollback --> Homo_Reintegration : rollback_complete
  Homo_Reintegration --> Idle : intentions_confirmed
}

FSM -[hidden]-> FIELD

@enduml

---

![FIELD_TEST_AUTOMATION_OVERVIEW](FIELD_TEST_AUTOMATION_OVERVIEW.svg)

---

Uwaga architektoniczna: Pliki META_LOOP_BOUNDARY.md oraz META_LOOP_layer.md
są świadomie osadzone w katalogu 02_field_engine jako część trzeciej sekcji
(FieldEngine → META_LOOP nad polem). Ich lokalizacja odzwierciedla fakt, że
META_LOOP w RAMORGA nie jest warstwą „overview”, lecz nadbudową operującą
bezpośrednio nad silnikiem pola. Dlatego pliki te pozostają w 02_field_engine
i nie są przenoszone do warstwy 00_overview.

