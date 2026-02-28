# RAMORGA Machine Schema

The Machine Schema defines the structural representation of all RAMORGA states, transitions, and modules in a unified schema.

---

## Schema Components

- **FieldState** — tension, energy, entropy, ritual, continuity signatures.
- **MeniscusState** — normalized and stabilized intermediate state.
- **PipelineState** — deterministic execution state.
- **Snapshot** — reversible state representation.
- **ErrorState** — invariant or interface violation.

---

## Schema Requirements

- All schemas must be explicit and versioned.
- All fields must have defined types and constraints.
- All transitions must preserve invariants.
- No schema may include implicit or hidden fields.

---

## Schema Transitions

- FieldState → MeniscusState  
- MeniscusState → PipelineState  
- PipelineState → Snapshot  
- Snapshot → FieldState  

All transitions must be deterministic and invariant-compliant.

---

## Related Documents

- [Versioning](../15_versioning/README.md)
- [Interfaces](../05_interfaces/README.md)
- [Invariants](../04_invariants/README.md)
- [Field Engine](../02_field_engine/README.md)
