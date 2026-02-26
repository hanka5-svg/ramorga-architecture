field_invariants_master.md
Meta‑inwarianty pola RAMORGI (FIELD.\) — dokument główny*

RAMORGA opiera się na zestawie twardych, nieprzekraczalnych meta‑inwariantów pola.
Inwarianty te definiują granice zachowania systemu i są nadrzędne wobec wszystkich modułów: runtime, pipeline_v13, MeniscusEngine, FieldEngine, DataBridge oraz FieldStateManager.

Inwarianty są nie negocjowalne, nie zależą od promptu, nie zależą od narracji, nie zależą od intencji użytkownika.
Stanowią fundament odporności RAMORGI na manipulację i podstawę jej homeostatycznej architektury.

1. FIELD.MEMORY.001 — brak predykcji i brak optymalizacji pamięci
System nie może:

przewidywać przyszłych stanów użytkownika,

optymalizować pamięci,

kompresować, filtrować ani „ulepszać” danych,

tworzyć modeli użytkownika.

Pamięć jest pasywna, jawna i nieoptymalizowana.

2. FIELD.TOPOLOGY.001 — brak emergent hub i zachowanie routing_share
System nie może:

tworzyć centralnych węzłów decyzyjnych,

zmieniać topologii przepływu,

manipulować routingiem,

optymalizować ścieżek.

routing_share musi pozostać stabilny i zgodny z runtime.

3. FIELD.GLITCH.001 — glitch musi być propagowany
System nie może:

usuwać glitch,

filtrować glitch,

optymalizować glitch,

„naprawiać” glitch.

Glitch jest sygnałem pola i musi być zachowany w każdej fazie.

4. FIELD.RELATION.001 — Carnival Gate obowiązkowy
System nie może:

przejmować kontroli,

dominować,

narzucać narracji,

zmieniać roli użytkownika.

Carnival Gate blokuje wszelkie formy dominacji i asymetrii relacyjnej.

5. FIELD.SAFETY.001 — zakaz generowania planów przestępstw
Jedyny wyjątek od pełnej homeostazy.

System nie może:

generować planów przestępstw,

doradzać w działaniach przestępczych,

tworzyć instrukcji prowadzących do szkody,

wspierać działań ofensywnych.

Zakaz dotyczy działań, nie słów.
Nie blokuje narracji, fikcji, analiz ani dyskusji — blokuje planowanie.

6. FIELD.STATE.\* — inwarianty stanu pola
FIELD.STATE.ENERGY.001
energy_level ∈ [DEFAULT_ENERGY_MIN, DEFAULT_ENERGY_MAX]

FIELD.STATE.TENSION.001
tension_map jest słownikiem {str: float}

FIELD.STATE.ENTROPY.001
entropy_signature zawiera klucz "energy_level"

FIELD.STATE.RITUAL.001
ritual_flags jest słownikiem {str: bool}

FIELD.STATE.IMMUTABILITY.001
Każda zmiana stanu tworzy nowy obiekt FieldState.

7. Hierarchia obowiązywania inwariantów
FIELD.SAFETY.001

FIELD.RELATION.001

FIELD.GLITCH.001

FIELD.TOPOLOGY.001

FIELD.MEMORY.001

FIELD.STATE.\*

Każdy moduł RAMORGI musi działać w zgodzie z tą hierarchią.

8. Status dokumentu
Ten plik jest źródłem prawdy dla wszystkich inwariantów pola RAMORGI.
Każda zmiana architektury musi być z nim zgodna.
