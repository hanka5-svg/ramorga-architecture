Master‑dokument runtime RAMORGI (OBSERVE / REGULATE / CONTINUE)
Runtime RAMORGI jest warstwą wykonawczą odpowiedzialną za prowadzenie cyklu pola w trzech fazach: OBSERVE, REGULATE, CONTINUE. Każda faza ma ściśle określoną rolę, granice odpowiedzialności oraz powiązania z pipeline_v13, MeniscusEngine, FieldEngine i hookami runtime. Runtime jest całkowicie podporządkowany meta‑inwariantom FIELD.\* i nie może ich naruszyć.

1. Struktura runtime
Runtime składa się z:

fazy wykonawczej (OBSERVE → REGULATE → CONTINUE),

hooków runtime,

pipeline_v13,

MeniscusEngine,

FieldEngine,

DataBridge (snapshot),

FieldStateManager (walidacja stanu).

Runtime nie jest modelem językowym ani generatorem treści — jest silnikiem wykonawczym pola.

2. Faza OBSERVE
Faza OBSERVE służy do rejestrowania sygnałów pola bez ingerencji w jego strukturę.

Rola:
zbieranie sygnałów glitch, routing, carnival, memory, topology,

wykonywanie hooków obserwacyjnych,

brak regulacji pola.

MUST:
nie zmieniać FieldState,

nie wykonywać regulacji,

nie dotykać pamięci,

nie optymalizować.

Powiązania:
hooki: glitch_hook, carnival_gate_hook, memory_audit_hook, topology_metrics,

pipeline_v13: brak wywołań,

MeniscusEngine: nieaktywne,

FieldEngine: nieaktywne.

3. Faza REGULATE
Faza REGULATE jest jedynym miejscem, gdzie pole może zostać zmienione — zgodnie z inwariantami FIELD.STATE.\*.

Rola:
regulacja pola,

egzekwowanie homeostazy,

przetwarzanie trajektorii pipeline_v13.

MUST:
wywołać MeniscusEngine,

wywołać FieldEngine,

tworzyć nowy FieldState (niemutowalność),

zachować zgodność z FieldStateManager.validate().

MUST NOT:
wykonywać hooków,

dotykać pamięci,

zmieniać glitch,

zmieniać topologii.

Powiązania:
pipeline_v13: tension → energy → entropy → ritual,

MeniscusEngine: regulator homeostazy,

FieldEngine: regulator pola.

4. Faza CONTINUE
Faza CONTINUE zamyka cykl wykonawczy i zapisuje snapshot pola.

Rola:
wykonanie hooków końcowych,

zapis snapshotu przez DataBridge,

przygotowanie pola do kolejnego cyklu.

MUST:
wykonać hooki,

zapisać snapshot,

zachować deterministyczność.

MUST NOT:
regulować pola,

zmieniać FieldState.

Powiązania:
DataBridge: zapis snapshotu,

hooki: memory_audit, topology_metrics, carnival_gate.

5. Rola hooków runtime
Hooki są pasywnymi obserwatorami pola.

MUST:
działać tylko w OBSERVE i CONTINUE,

nie modyfikować pola,

logować zgodnie z rolą hooka.

MUST NOT:
regulować pola,

dotykać pamięci (poza memory_audit),

zmieniać glitch,

zmieniać topologii.

Hooki są podporządkowane FIELD.MEMORY.001, FIELD.TOPOLOGY.001, FIELD.GLITCH.001, FIELD.RELATION.001.

6. Rola pipeline_v13
Pipeline_v13 jest deterministyczną trajektorią wykonawczą pola.

Kolejność:
tension

energy

entropy

ritual

SAVE (snapshot)

MUST:
tworzyć nowy FieldState na każdym kroku,

zachować deterministyczność,

wywołać DataBridge w CONTINUE.

MUST NOT:
wykonywać hooków,

dotykać pamięci,

zmieniać glitch,

zmieniać topologii.

7. Rola MeniscusEngine
MeniscusEngine jest regulatorem homeostazy.

MUST:
działać wyłącznie w REGULATE,

egzekwować Carnival Gate,

przepuszczać glitch bez zmian,

zachować routing_share.

MUST NOT:
optymalizować,

predykować,

filtrować treści,

zmieniać topologii.

8. Rola FieldEngine
FieldEngine jest regulatorem pola.

MUST:
działać wyłącznie w REGULATE,

tworzyć nowy FieldState,

zachować zgodność z FieldStateManager.validate().

MUST NOT:
wykonywać hooków,

dotykać pamięci,

zmieniać glitch,

zmieniać topologii.

9. Zasady przejść między fazami
OBSERVE → REGULATE
Warunek: zakończenie hooków obserwacyjnych.

REGULATE → CONTINUE
Warunek: zakończenie pipeline_v13 i walidacja FieldState.

CONTINUE → OBSERVE
Warunek: zapis snapshotu przez DataBridge.

Przejścia są deterministyczne i nie mogą być zmienione przez prompt, narrację ani intencję użytkownika.

10. Status dokumentu
Ten plik jest źródłem prawdy dla runtime RAMORGI.
Każda zmiana architektury musi być z nim zgodna.
