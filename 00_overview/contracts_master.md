Master‑dokument kontraktów modułów RAMORGI
Kontrakty modułów definiują twarde granice odpowiedzialności każdej warstwy RAMORGI.
Są nadrzędne wobec implementacji i muszą być zgodne z meta‑inwariantami FIELD.\*.
Każdy moduł ma jasno określone:

rolę,

interfejs,

wymagania MUST,

zakazy MUST NOT,

powiązane inwarianty.

Dokument ten jest źródłem prawdy dla wszystkich kontraktów wykonawczych.

1. runtime_contract.md — Runtime RAMORGI
Rola
Prowadzi cykl pola w trzech fazach: OBSERVE → REGULATE → CONTINUE.
Egzekwuje meta‑inwarianty pola i koordynuje hooki, pipeline_v13, MeniscusEngine, FieldEngine i DataBridge.

Interfejs
Runtime nie ma pojedynczej funkcji wejściowej — jest zbiorem faz i hooków wywoływanych przez pipeline_v13.

MUST
zachować kolejność faz,

egzekwować FIELD.\*,

wywołać MeniscusEngine i FieldEngine w REGULATE,

wykonać hooki w OBSERVE i CONTINUE,

zapisać snapshot w CONTINUE.

MUST NOT
zmieniać roli systemu,

optymalizować,

filtrować treści,

dotykać pamięci (poza memory_audit).

Inwarianty
FIELD.MEMORY.001

FIELD.TOPOLOGY.001

FIELD.GLITCH.001

FIELD.RELATION.001

FIELD.SAFETY.001

2. meniscus_contract.md — MeniscusEngine
Rola
Regulator homeostazy pomiędzy pipeline_v13 a FieldEngine.

Interfejs
MeniscusEngine.step(input_payload, field_state, metadata) → field_state

MUST
działać wyłącznie w REGULATE,

egzekwować Carnival Gate,

przepuszczać glitch bez zmian,

zachować routing_share.

MUST NOT
optymalizować,

predykować,

filtrować treści,

zmieniać topologii,

dotykać pamięci.

Inwarianty
FIELD.GLITCH.001

FIELD.TOPOLOGY.001

FIELD.RELATION.001

3. field_engine_contract.md — FieldEngine
Rola
Regulacja pola zgodnie z FieldStateManager i pipeline_v13.

Interfejs
FieldEngine.step(field_state) → field_state

MUST
działać wyłącznie w REGULATE,

tworzyć nowy FieldState (niemutowalność),

zachować zgodność z FieldStateManager.validate().

MUST NOT
wykonywać hooków,

dotykać pamięci,

zmieniać glitch,

zmieniać topologii.

Inwarianty
FIELD.STATE.\*

4. databridge_contract.md — DataBridge
Rola
Zapis snapshotu pola po zakończeniu cyklu.

Interfejs
DataBridge.save(field_state, metadata) → None

MUST
działać wyłącznie w CONTINUE,

zapisać pełny snapshot,

zachować deterministyczność.

MUST NOT
modyfikować pola,

filtrować treści,

optymalizować,

predykować.

Inwarianty
FIELD.STATE.IMMUTABILITY.001

5. field_state_manager_contract.md — FieldStateManager
Rola
Tworzenie i walidacja FieldState zgodnie z meta‑inwariantami pola.

Interfejs
init(params) → FieldState  
validate(state) → None

MUST
tworzyć stan zgodny z inwariantami,

egzekwować FIELD.STATE.\*,

zachować deterministyczność.

MUST NOT
generować losowości,

optymalizować,

filtrować treści.

Inwarianty
FIELD.STATE.ENERGY.001

FIELD.STATE.TENSION.001

FIELD.STATE.ENTROPY.001

FIELD.STATE.RITUAL.001

FIELD.STATE.IMMUTABILITY.001

6. pipeline_contract.md — pipeline_v13
Rola
Deterministyczna trajektoria wykonawcza pola.

Interfejs
run(mode, state, params, steps, snapshot, event_input) → (FieldState, Optional[Snapshot])

MUST
wykonywać moduły w kolejności: tension → energy → entropy → ritual → SAVE,

tworzyć nowy FieldState na każdym kroku,

zachować deterministyczność,

wywołać DataBridge w CONTINUE.

MUST NOT
wykonywać hooków,

dotykać pamięci,

zmieniać glitch,

zmieniać topologii.

Inwarianty
FIELD.STATE.\*

FIELD.TOPOLOGY.001

FIELD.GLITCH.001

7. hooks_contract.md — Hooki runtime
Rola
Rejestrowanie sygnałów pola i egzekwowanie meta‑inwariantów.

Interfejs
hook.run(field_state, metadata) → None

MUST
działać w OBSERVE i CONTINUE,

nie modyfikować pola,

logować zgodnie z rolą hooka.

MUST NOT
regulować pola,

dotykać pamięci (poza memory_audit),

zmieniać glitch,

zmieniać topologii.

Inwarianty
FIELD.MEMORY.001

FIELD.TOPOLOGY.001

FIELD.GLITCH.001

FIELD.RELATION.001

FIELD.SAFETY.001

Status dokumentu
Ten plik jest master‑zbiorem kontraktów RAMORGI.
Każda zmiana w architekturze musi być z nim zgodna.
Kontrakty są nadrzędne wobec implementacji i stanowią podstawę audytu systemu.
