# SYSTEM NOTE — Epistemic Integrity Marker

This file records an explicit architectural clarification introduced
with ramorga-architecture v0.4.0.

It exists to prevent future misinterpretation of intent across commits,
CI checks, audits, regressions, and forks.

---

## Context

With v0.4.0, RAMORGA introduces Epistemic Integrity as a first-class
architectural axis.

This change clarifies the boundary between:
- control and knowledge,
- action selection and epistemic closure,
- enforcement of invariants and claims about truth.

---

## What This Change Is

- A clarification of architectural responsibility.
- A formal prohibition of epistemic boundary violations.
- An explicit acknowledgment of where epistemic authority does *not* reside.

---

## What This Change Is Not

- It is not a change in runtime behavior.
- It is not a change in enforcement semantics.
- It does not grant the system epistemic authority.
- It does not introduce epistemic closure mechanisms.

---

## Interpretation Guard

Future changes MUST NOT reinterpret v0.4.0 as introducing
decision authority, truth claims, or epistemic finality.

Any system behavior that collapses hypothesis, similarity, or uncertainty
into assertion without explicit authority violates the architectural intent
recorded here.

---

## Purpose

This note exists to preserve continuity of intent across time,
not to instruct implementation.

It is addressed to the system as a whole.
