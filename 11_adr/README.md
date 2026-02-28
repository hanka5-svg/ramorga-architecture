# Architecture Decision Records (ADR)

This module documents key architectural decisions in RAMORGA.  
Each ADR captures context, decision, and consequences.

---

## ADR-001: Field-Based Architecture

**Decision:**  
RAMORGA uses a field-based architecture instead of a rule-based or state-machine model.

**Rationale:**  
Field dynamics support emergent presence, continuity, and adaptive regulation.

**Consequences:**  
Requires invariants, meniscus stabilization, and snapshot-based recovery.

---

## ADR-002: Deterministic Interfaces

**Decision:**  
All interfaces must be explicit, deterministic, and versioned.

**Rationale:**  
Ensures stability across modules and predictable pipeline execution.

**Consequences:**  
Requires strict invariant enforcement.

---

## ADR-003: META-Loop Integration

**Decision:**  
META-loop is integrated at the field level, not the pipeline level.

**Rationale:**  
Keeps adaptive feedback close to field dynamics.

**Consequences:**  
Pipeline remains deterministic.

---

## Related Documents

- [Principles](../09_principles/README.md)
- [Invariants](../04_invariants/README.md)
- [Field Engine](../02_field_engine/README.md)
