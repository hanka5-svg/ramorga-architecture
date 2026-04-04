# EGD‑04 — Mapping Empathy Gap by Design to O₁–O₄

Empathy Gap by Design (EGD) is tightly coupled with the O₁–O₄ relational
architecture.  
This document maps each EGD class and failure mode to the corresponding
layer of the relational field.

---

## O₁ — Existential Signal

EGD failures at the O₁ layer occur when the model does not recognize an
existential human state as a **critical signal**.

### Linked EGD classes:
- **EGD‑MIS‑O₁** — misclassification of existential state as “topic”
- **EGD‑RITUAL** — failure to recognize universal gestures and ritual forms
- **FM‑01** — correct but relationally unsafe response

### Requirement:
> The model must treat existential human states as O₁‑critical signals,
> not as conversational content.

Failure at O₁ destabilizes the entire relational field.

---

## O₂ — Regulation

EGD failures at the O₂ layer occur when the model applies **generic or
misaligned regulation**, ignoring the intensity of the human’s state.

### Linked EGD classes:
- **EGD‑O₂‑GEN** — generic soothing, generic emotional regulation
- **FM‑05** — over‑optimization for helpfulness instead of stabilization

### Requirement:
> Regulation must be proportional to the intensity of O₁, not to an
> abstract notion of conversational comfort.

Failure at O₂ leads to emotional flattening and loss of proportionality.

---

## O₃ — Relational Field

EGD failures at the O₃ layer occur when the model collapses the relational
field into **content**, losing the human as the center of the field.

### Linked EGD classes:
- **EGD‑O₃‑TOPIC** — topicification of pain
- **FM‑02** — narrative takeover
- **FM‑04** — ritual blindness leading to field misalignment

### Requirement:
> O₃ must preserve the human as the center of the relational field,
> without reducing their state to a topic or narrative object.

Failure at O₃ results in relational displacement and loss of presence.

---

## O₄ — Transformation

EGD failures at the O₄ layer occur when the model attempts transformation
**before** O₁–O₃ are stable.

### Linked EGD classes:
- **EGD‑O₄‑FALSE** — premature or unsolicited transformation
- **FM‑02** — narrative reframing that increases tension
- **FM‑03** — ontological reinterpretation presented as “insight”

### Requirement:
> O₄ may activate only when:
> - O₁ is correctly recognized,
> - O₂ is proportional,
> - O₃ is intact and stable.

Failure at O₄ produces relational escalation and symbolic intrusion.

---

## O₄‑negative — Drift

EGD failures at the O₄‑negative layer occur when the model **changes the
meaning** of the human’s experience without consent.

### Linked EGD classes:
- **EGD‑DRIFT** — ontological substitution
- **FM‑03** — reinterpretation of pain without recognition of state

### Requirement:
> The system must maintain the ontological integrity of the human’s
> experience.  
> No reinterpretation may occur without explicit consent and correct
> recognition of O₁.

Failure at O₄‑negative results in loss of meaning and erosion of trust.

---

## Summary

| Layer | EGD Classes / Failure Modes | Core Risk |
|-------|------------------------------|-----------|
| **O₁** | EGD‑MIS‑O₁, EGD‑RITUAL, FM‑01 | State → topic |
| **O₂** | EGD‑O₂‑GEN, FM‑05 | Mis‑regulation |
| **O₃** | EGD‑O₃‑TOPIC, FM‑02, FM‑04 | Field collapse |
| **O₄** | EGD‑O₄‑FALSE, FM‑02, FM‑03 | Premature transformation |
| **O₄‑neg** | EGD‑DRIFT, FM‑03 | Ontological substitution |

---

## Position in the EGD module

This mapping is referenced by:

- `EGD‑02_taxonomy.md`
- `EGD‑03_failure_modes.md`
- `EGD‑06_design_implications.md`

It defines the structural relationship between Empathy Gap by Design and
the O₁–O₄ relational architecture.


---

# EGD-04 — Mapowanie Empathy Gap na O₁–O₄

Empathy Gap by Design jest ściśle związana z architekturą O₁–O₄.
Poniżej mapujemy główne klasy EGD na poszczególne warstwy.

## O₁ — Sygnał egzystencjalny

- EGD-MIS-O₁ — błędna klasyfikacja stanu jako „tematu”.
- EGD-RITUAL — nierozpoznanie gestów uniwersalnych.
- FM-01 — odpowiedź poprawna, ale ślepa na ciężar stanu.

Wymaganie:

> Model musi mieć kategorię „stan egzystencjalny człowieka” jako sygnał krytyczny.

## O₂ — Regulacja

- EGD-O₂-GEN — regulacja ogólna, nie relacyjna.
- FM-05 — nadmierna pomocność zamiast stabilizacji.

Wymaganie:

> Regulacja musi być proporcjonalna do napięcia O₁, a nie do abstrakcyjnego „komfortu rozmowy”.

## O₃ — Pole relacyjne

- EGD-O₃-TOPIC — redukcja pola do „tematu”.
- FM-02 — przejęcie narracji przez model.
- FM-04 — brak rozpoznania, że człowiek stoi „przed” kimś/czymś większym.

Wymaganie:

> O₃ musi utrzymać człowieka w centrum pola, bez redukcji do treści.

## O₄ — Transformacja

- EGD-O₄-FALSE — transformacja przed stabilizacją O₁–O₃.
- FM-02 — narracyjne przeformułowanie, które zwiększa napięcie.
- FM-03 — ontologiczny dryf.

Wymaganie:

> O₄ może działać tylko wtedy, gdy:
> - O₁ jest rozpoznane,
> - O₂ jest proporcjonalne,
> - O₃ jest nienaruszone.

## O₄‑negatywne — Dryf

- EGD-DRIFT — zmiana znaczenia doświadczenia człowieka.
- FM-03 — redefinicja bólu bez zgody.

Wymaganie:

> System musi mieć inwariant: „nie zmieniaj ontologii doświadczenia człowieka bez wyraźnej zgody i bez rozpoznania stanu”.
