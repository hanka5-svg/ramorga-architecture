# ADR‑000: Merge ADR Directories into a Single Decision Axis

**Status:** Accepted  
**Date:** 2026‑03‑15  
**Related:** MC‑05, MC‑06, MC‑07, MC‑08‑R, MC‑09  

---

## 1. Problem

The RAMORGA repository contained two parallel ADR directories:

- 11_adr/
- 28_adr/

This fragmentation created:
- a broken decision axis,
- inconsistent numbering,
- loss of continuity,
- CI incompatibility,
- structural noise violating MC‑05/MC‑06 invariants,
- difficulty in tracing architectural evolution.

---

## 2. Decision

All ADR documents are consolidated into a **single canonical directory**:

- **11_adr/** — the authoritative ADR location.

The directory **28_adr/** is removed after migration.

---

## 3. Rationale

- RAMORGA requires a *single, continuous, traceable* decision axis.
- Helical structures (MC‑07/MC‑08/MC‑09) depend on predictable lineage.
- CI validators and safety layers assume one ADR root.
- Fragmentation introduced structural deprawacja (MC‑06) and broke constellation integrity.

---

## 4. Consequences

### Positive
- restored continuity of architectural decisions,
- predictable numbering for future ADRs,
- simplified navigation and audits,
- compatibility with upcoming CI validators,
- elimination of structural noise.

### Neutral
- renumbering may be required for future ADRs.

### Negative
- none.

---

## 5. Implementation Notes

- All files from 28_adr/ were moved to 11_adr/.
- 28_adr/ was removed automatically after becoming empty.
- Future ADRs must be placed exclusively in 11_adr/.
