ADR‑025 — Pełny benchmark MC‑11/MC‑12/MC‑13
Status
Accepted

Kontekst
RAMORGA definiuje trzy warstwy interpretacji:

MC‑11 — trafność podstawowa,

MC‑12 — emergencja,

MC‑13 — fonologia.

Każda warstwa ma własny kontrakt, lecz brakowało:

jednolitego benchmarku obejmującego wszystkie trzy warstwy,

spójnego systemu punktacji,

miejsca na porównywanie modeli,

formalnego opisu, jak interpretować wyniki.

Model_Scoring.md wprowadził wymiary W1–W5, ale benchmark jako całość nie został jeszcze sformalizowany.

Decyzja
Tworzymy pełny benchmark MC‑11/MC‑12/MC‑13, obejmujący:

definicję wymiarów oceny (W1–W5),

zasady punktacji,

zasady integracji wyników,

klasyfikację modeli,

wymagania dla testów terenowych,

02_field_engine/Model_Scoring.md

Uzasadnienie
Benchmark jest niezbędny do porównywania modeli w sposób spójny i powtarzalny.

MC‑11/12/13 tworzą trójwarstwową architekturę interpretacji — benchmark musi ją odzwierciedlać.

FIELD ENGINE wymaga formalnych zasad oceny, aby automatyzować testy.

Benchmark umożliwia rozwój RAMORGI jako narzędzia badawczego.

Konsekwencje
Pozytywne:

pełna formalizacja oceny modeli,

możliwość tworzenia rankingów i analiz porównawczych,

integracja z FIELD ENGINE,

spójność między modułami a testami.

Negatywne:

konieczność utrzymania benchmarku w kolejnych wersjach RAMORGI,

większa złożoność dokumentacji.

Powiązania
Model_Scoring.md

MC‑11_Learning_Layer.md

MC‑12_Emergent_Layer.md

MC‑13_Phonological_Layer.md

MC_Integration_Matrix.md

FIELD_TEST_AUTOMATION_README.md

HOMEOSTATIC_METRICS.md
zasady raportowania wyników.

Benchmark opiera się na pliku:
