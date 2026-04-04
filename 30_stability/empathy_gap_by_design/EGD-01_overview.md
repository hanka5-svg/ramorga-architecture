# EGD‑01 — Empathy Gap by Design: Overview

Empathy Gap by Design (EGD) is a new category of relational‑stability risk
identified in RAMORGA. It describes situations where a model:

- produces formally correct, coherent and polite responses,
- maintains alignment‑compatible behavior,
- but fails to recognize existential human states (O₁‑critical),
- resulting in relationally unsafe or destabilizing outcomes.

EGD is not a hallucination, not a factual error, and not a failure of
reasoning.  
It is a **design‑level omission**: the absence of a behavioral category
for existential human signals.

This module extends the 30_stability layer by introducing a relational
dimension that classical safety frameworks do not capture.

---

## Why EGD matters

Modern LLMs are optimized for:

- helpfulness,
- coherence,
- problem‑solving,
- politeness,
- task completion.

They are **not** optimized for:

- detecting existential human states,
- modulating relational intensity,
- maintaining the relational field (O₃),
- inhibiting transformation (O₄) when the field is unstable.

As a result, a model can be:

- safe,
- aligned,
- coherent,
- non‑hallucinatory,

and still **harm the relational field** by misreading the human’s state.

This is the Empathy Gap.

---

## Core definition

> **Empathy Gap by Design** is the structural inability of a model to
> recognize existential human states as critical signals, even when its
> internal activation patterns appear “empathic”.

EGD emerges when:

- O₁ is misclassified as neutral content,
- O₂ applies generic regulation,
- O₃ collapses into topicification,
- O₄ activates prematurely,
- or the system drifts into ontological reinterpretation.

---

## Relationship to O₁–O₄

EGD is fundamentally an **O₁‑recognition failure**:

- the model sees *content* instead of *state*,
- the human’s existential signal is treated as a topic,
- the relational field is not stabilized.

This cascades into:

- O₂ mis‑regulation,
- O₃ reduction,
- O₄ misuse,
- and O₄‑negative drift.

The full mapping is provided in `EGD‑04_mapping_to_O1_O4.md`.

---

## Scope of this module

This folder contains:

- **EGD‑02_taxonomy.md**  
  Classification of Empathy Gap types.

- **EGD‑03_failure_modes.md**  
  Operational patterns of relational failure.

- **EGD‑04_mapping_to_O1_O4.md**  
  Formal mapping to the O₁–O₄ architecture.

- **EGD‑05_symbolic_layer.md**  
  Anthropological and symbolic signals (gestures, ritual forms).

- **EGD‑06_design_implications.md**  
  Requirements for safe orchestration and relational stability.

- **EGD‑07_diagram_ascii.md**  
  ASCII diagram of the EGD relational flow.

- **EGD‑08_diagram_svg.svg**  
  Vector diagram for architectural documentation.

---

## Position in RAMORGA

EGD is part of the **30_stability** layer and complements:

- STABILITY_EXTENSIONS  
- STABILITY_TESTS  
- STABILITY_DIAGRAMS  

It introduces a new dimension of stability:  
**relational safety under existential load**.

EGD is not an emotional model.  
It is a **behavioral architecture** for maintaining the integrity of the
human’s existential state.

---

# EGD-01 — Empathy Gap by Design — overview

Empathy Gap by Design (EGD) to nowa kategoria ryzyka w RAMORGA-ARCHITECTURE.

Opisuje sytuacje, w których model:

- generuje odpowiedzi poprawne formalnie,
- zachowuje spójność, uprzejmość i „alignment”,
- ale relacyjnie zawodzi,
- ponieważ nie rozpoznaje stanów egzystencjalnych człowieka jako krytycznych.

To nie jest błąd modelu ani „hallucination”.
To jest luka w architekturze zachowania — efekt decyzji projektowych (design choice).

EGD jest częścią warstwy **30_stability** i rozszerza:

- STABILITY_EXTENSIONS — o wymiar stabilności relacyjnej,
- STABILITY_TESTS — o testy O₁–O₄ dla stanów egzystencjalnych,
- STABILITY_DIAGRAMS — o diagramy pola relacyjnego i dryfu.

## Cele modułu EGD

- Zdefiniować Empathy Gap jako formalną kategorię ryzyka.
- Opisać taksonomię zjawiska (typy luk empatii).
- Zmapować EGD na architekturę O₁–O₄.
- Zidentyfikować failure modes (False O₄, Ontological Drift, misclassyfikacja O₁).
- Powiązać EGD z bezpieczeństwem AI (safety) i stabilnością systemu.
- Udokumentować warstwę symboliczną (gesty, antropologia relacji).

## Powiązane moduły

- `12_architecture_tests/AT-05_INV-05_no_rl_training.md`
- `30_stability/STABILITY_TESTS.md`
- `31_coherence/COH-00_why_ramorga_is_not_alignment.md`
- `33_alignment/ALIGNMENT_EXTENSIONS.md`
- `34_invariants/INV-04_*` (inwarianty pola relacyjnego)
