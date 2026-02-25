# 13_security — integrity & protection layer

## Module intent

Module 13 defines the security layer for the RAMORGA architecture.

Security here is not reduced to “access control” or “compliance”.  
It is the protection of:

- continuity of the field,
- integrity of identities,
- stability of invariants,
- and non‑abusive use of adaptive systems (including AI).

This module describes how the system **stays itself** under pressure:
technical, organizational, economic, and cognitive.

---

## Scope

This module covers:

- threat modelling at the level of:
  - field (environment, ecosystem),
  - actors (humans, agents, institutions),
  - flows (data, decisions, feedback),
- security invariants (what must never be broken),
- protective patterns (how we enforce those invariants),
- monitoring & reflection (how we notice drift and abuse).

It does **not** define low‑level crypto, IAM configs or vendor‑specific setups.  
Instead, it defines the **security contract** that any implementation must respect.

---

## Relations to other modules

- **00_overview** — defines the field and its boundaries; 13_security protects them.
- **01_module_contracts** — defines identities and contracts; 13_security guards their integrity.
- **02_field_engine** — manages resonance; 13_security prevents hostile or coercive use of the field.
- **03_meniscus_engine** — manages boundaries; 13_security defines what cannot cross.
- **04_invariant_rules** — defines invariants; 13_security enforces them under adversarial conditions.
- **12_architecture_tests** — provides tests; 13_security adds adversarial and abuse‑oriented scenarios.

---

## Core security questions

This module is driven by questions like:

- Who can change what, for whom, and under which conditions?
- What must remain visible, and what must never be exposed?
- Which parts of the system are allowed to adapt, and which must stay invariant?
- How do we detect when the system is being:
  - hijacked,
  - coerced,
  - deprived,
  - or used against its declared field?

---

## Threat model

See: [`threat_model.md`](./threat_model.md)

This document describes:

- actors and their capabilities,
- attack surfaces (technical, organizational, cognitive),
- typical abuse patterns (e.g. hijack, deprivation, forced optimization),
- and how they manifest in this architecture.

---

## Controls & invariants

See: [`controls.md`](./controls.md)

This document defines:

- security invariants (what must never be violated),
- control patterns (how we enforce them),
- monitoring hooks (what we observe),
- and escalation paths (what happens when something breaks).

---

## Next steps

1. Draft the initial threat model for RAMORGA (field‑level first, then technical).
2. Extract security‑relevant invariants from `04_invariant_rules`.
3. Define a minimal set of controls that:
   - protect the field,
   - protect identities,
   - prevent hijack and deprivation,
   - and keep adaptive components within declared boundaries.
4. Add security‑focused tests to `12_architecture_tests`.

Module 13 is not a checklist.  
It is the **protective skin** of the architecture.
