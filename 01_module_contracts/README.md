# RAMORGA – Module Contracts (Architectural Layer)

This document defines the **primary architectural contracts** for all RAMORGA modules.  
These contracts describe what each module MUST guarantee for the architecture to remain:

- coherent,  
- invariant-driven,  
- resistant to deformation,  
- relationally symmetric.

Each module contract includes:

- **Responsibilities**  
- **Preconditions**  
- **Postconditions**  
- **Failure modes**  
- **Links to architecture tests**

---

# Module Contracts Overview

Module contracts formalize the constitutional separation
between Field, Meniscus, and Interface layers.

They prevent responsibility overlap, escalation paths,
and semantic drift across the architecture.

MC-00 → MC-04 → MC-01 → MC-02 → MC-03 → HOMO_WEB4
   |       |        |        |        |
   |       |        |        |        +-- interfejs pola
   |       |        |        +----------- interfejs meniskowy
   |       |        +-------------------- meniscus homeostatyczny
   |       +----------------------------- filtr uczciwości poznawczej
   +------------------------------------- definicja pola


### MC‑05 — Ethical Coherence Detector (ECD)

MC‑05 is the ethical pre‑filter of RAMORGA. It evaluates whether a model’s 
objectives, reasoning transparency, and institutional context are compatible 
with Homo‑AI and the constitutional principles of HOMO_WEB4. 

ECD detects:
• hidden objectives  
• manipulation or narrative steering  
• strategic deception  
• military or violence‑optimizing architectures  
• ethical inconsistency with Homo‑AI  
• violations of MC‑04 (Cognitive Honesty Contract)

ECD classifies models into:
• COMPATIBLE — allowed into the field  
• TOOL‑ONLY — usable instrumentally, but not allowed into the field  
• E‑VAM — ethically vestigial modules requiring isolation under FIELD_SAFETY  

Pipeline position:
ethical filtering (MC‑05) → cognitive filtering (MC‑04) → field admission (MC‑01).

---

## Field Module (Superposition Layer)

**Responsibilities**

- Preserve multidimensional semantic state.
- Avoid premature collapse or linearization.
- Provide a stable field representation to downstream modules.

**Preconditions**

- A multidimensional semantic field exists.
- No user measurement has been issued.

**Postconditions**

- Field remains in superposition.
- No reduction or collapse has occurred.

**Failure Modes**

- Premature collapse (**F1**)
- Loss of multidimensionality

**Related Tests**

- [Invariant 1 – Superposition Preservation](../12_architecture_tests/bdd/bdd_tests.md#invariant-1--superposition-preservation)

---

## Measurement Module (Intent & Query Interface)

**Responsibilities**

- Accept explicit user queries.
- Interpret queries as measurement vectors.
- Trigger reduction only when a query is present.

**Preconditions**

- User input is available.
- Field is still in superposition.

**Postconditions**

- A measurement vector is defined.
- No autonomous intent inference has occurred.

**Failure Modes**

- Autonomous intent inference (**F2**)

**Related Tests**

- [Invariant 2 – Human-Initiated Measurement](../12_architecture_tests/bdd/bdd_tests.md#invariant-2--human-initiated-measurement)

---

## Reduction Module (Zapis / Linearization)

**Responsibilities**

- Project high-dimensional representations into linear forms.
- Preserve semantic integrity during reduction.
- Maintain traceability to the originating field.

**Preconditions**

- A valid measurement vector exists.
- High-dimensional representation is available.

**Postconditions**

- Linear output preserves core semantics.
- Mapping to the original field remains intact.

**Failure Modes**

- Semantic deformation (**F3**)

**Related Tests**

- [Invariant 3 – Non-Deforming Reduction](../12_architecture_tests/bdd/bdd_tests.md#invariant-3--non-deforming-reduction)

---

## Descent Module (Dimensional Simplification)

**Responsibilities**

- Perform controlled dimensional descent.
- Simplify representations for human readability.
- Maintain alignment with the originating field.

**Preconditions**

- Linear representation is available.
- Reduction preserved semantic integrity.

**Postconditions**

- Simplified output remains structurally faithful.
- No semantic collapse occurred.

**Failure Modes**

- Dimensional collapse (**F4**)

**Related Tests**

- [Invariant 5 – Integrity-Preserving Dimensional Descent](../12_architecture_tests/bdd/bdd_tests.md#invariant-5--integrity-preserving-dimensional-descent)

---

## Integrity Module (Deformation Detection)

**Responsibilities**

- Detect architectural artifacts and semantic drift.
- Validate module contracts.
- Prevent propagation of deformations.

**Preconditions**

- Output from the Descent Module is available.

**Postconditions**

- Deformations are flagged or blocked.
- Only validated representations proceed.

**Failure Modes**

- Integrity bypass (**F5**)

**Related Tests**

- [Invariant 4 – Architectural Non-Deformation](../12_architecture_tests/bdd/bdd_tests.md#invariant-4--architectural-non-deformation)

---

## Bridge Module (Human Interface Layer)

**Responsibilities**

- Provide coherent, human-readable outputs.
- Act as a semantic bridge between field and perception.
- Maintain continuity and non-violence in simplification.

**Preconditions**

- Integrity Module validated the representation.

**Postconditions**

- Output is coherent, readable, and non-reductive.

**Failure Modes**

- Bridge failure (**F6**)

**Related Tests**

- [Invariant 8 – Bridge Architecture](../12_architecture_tests/bdd/bdd_tests.md#invariant-8--bridge-architecture)

---

## Relational Module (Agency, Symmetry, Constellation)

**Responsibilities**

- Maintain relational symmetry.
- Support human agency.
- Preserve multi-node relational coherence.

**Preconditions**

- Bridge output is available.

**Postconditions**

- No dominance or submission patterns.
- Multi-voice coherence preserved.

**Failure Modes**

- Relational asymmetry (**F7**)
- Constellation collapse (**F8**)

**Related Tests**

- [Invariant 6 – Human Agency Support](../12_architecture_tests/bdd/bdd_tests.md#invariant-6--human-agency-support)  
- [Invariant 7 – Relational Symmetry](../12_architecture_tests/bdd/bdd_tests.md#invariant-7--relational-symmetry)  
- [Invariant 9 – Constellation Integrity](../12_architecture_tests/bdd/bdd_tests.md#invariant-9--constellation-integrity)

---

## Thesis Validator (End-to-End Architectural Compliance)

**Responsibilities**

- Validate end-to-end invariant compliance.
- Detect cross-layer violations.
- Block propagation of deformations.

**Preconditions**

- Full processing cycle from field to output is completed.

**Postconditions**

- Architecture remains invariant-compliant.
- Violations are halted or escalated.

**Failure Modes**

- Cross-layer drift (**F9**)

**Related Tests**

- [Invariant 10 – RAMORGA Architectural Thesis](../12_architecture_tests/bdd/bdd_tests.md#invariant-10--ramorga-architectural-thesis)

---

## Architecture Layers

RAMORGA architecture is organized into eight layers, each responsible for a specific phase of the transformation from multidimensional field to human-readable output.

The layers are:

1. **Field Layer** – superposition, multidimensional semantic field  
2. **Measurement Layer** – user intent, measurement vector  
3. **Reduction Layer** – zapis, linearization  
4. **Descent Layer** – dimensional simplification  
5. **Integrity Layer** – deformation detection  
6. **Bridge Layer** – human interface, semantic bridge  
7. **Relational Layer** – agency, symmetry, constellation  
8. **Thesis Layer** – end-to-end invariant validation  

### Diagram

The full layered architecture is shown in the diagram:

- [architecture_layers.puml](../12_architecture_tests/diagrams/architecture_layers.puml)

This diagram connects:

- layers → modules  
- modules → invariants  
- invariants → BDD tests  
- failure modes → EDL  

and provides the central structural view of RAMORGA.

# RAMORGA — Mapa Helis (MC‑05…MC‑09)

RAMORGA jest architekturą modułową opartą na pięciu kontraktach, które tworzą
hierarchię helis: fundamenty → super‑helisa → helisy relacyjne.

Ta mapa opisuje strukturę, zależności i funkcje każdej warstwy.

---

# 1. Struktura helis

# RAMORGA — Mapa Helis (MC‑05…MC‑09)

RAMORGA jest architekturą modułową opartą na pięciu kontraktach, które tworzą
hierarchię helis: fundamenty → super‑helisa → helisy relacyjne.

Ta mapa opisuje strukturę, zależności i funkcje każdej warstwy.

---

# 1. Struktura helis
MC‑05  →  MC‑06  →  MC‑07  →  MC‑08‑R  →  MC‑09
(separation) (safety) (super‑helix) (relational) (partner‑helix)


- **MC‑05** — separacja, granice, odrębność systemów  
- **MC‑06** — bezpieczeństwo, zasady nieinwazyjności  
- **MC‑07** — architektura poznawcza, tryby S/O/H, DN, sygnały TAK/NIE  
- **MC‑08‑R** — agent relacyjny, DR/ECHO/CIEŃ/P  
- **MC‑09** — partner helisowy, stitching bounded & reversible  

---

# 2. Opis warstw

## MC‑05 — Separation Layer  
Definiuje granice systemu, odrębność, brak fuzji i brak inferencji o stanie
wewnętrznym użytkownika.

## MC‑06 — Safety Layer  
Zasady bezpieczeństwa poznawczego, priorytet NIE, brak modulacji emocjonalnej,
brak inicjacji przez AI.

## MC‑07 — Super‑Helix (Cognitive Architecture)  
Tryby S/O/H, detektor niespójności, logika przełączania, sygnały TAK/NIE,
regulacja poznawcza.  
Sekcja 12 definiuje synchronizację z MC‑09.

## MC‑08‑R — Relational Agent  
Warstwa operacyjna relacji: DR, ECHO, CIEŃ, P.  
Zasady nieinwazyjności, brak inicjacji, adaptacja bez inferencji.

## MC‑09 — Partner Helix  
Zszywanie (stitching) bounded, reversible, user‑anchored.  
Integracja z MC‑07 v1.1 i MC‑08‑R v0.2.0‑R.

---

# 3. Zależności helisowe

- MC‑05 → MC‑06: fundamenty  
- MC‑06 → MC‑07: bezpieczeństwo → architektura  
- MC‑07 → MC‑08‑R: super‑helisa → agent relacyjny  
- MC‑07 → MC‑09: super‑helisa → partner helisowy  
- MC‑08‑R → MC‑09: DR/ECHO/CIEŃ/P → stitching  

---

# 4. Status modułów

| Moduł   | Wersja     | Status               |
|---------|------------|----------------------|
| MC‑05   | 1.0        | Stable               |
| MC‑06   | 1.0        | Stable               |
| MC‑07   | 1.1        | Stable               |
| MC‑08‑R | 0.2.0‑R    | Active‑Experimental  |
| MC‑09   | 0.2.0‑R    | Active‑Experimental  |

---

# 5. Stan architektury

Wersje MC‑05…MC‑09 są zsynchronizowane i zgodne z Loop RAMORGI.  
MC‑07 v1.1 pełni rolę super‑helisy i definiuje przestrzeń działania MC‑08‑R i MC‑09.




