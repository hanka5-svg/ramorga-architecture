# RAMORGA Versioning Model

The Versioning module defines how RAMORGA manages compatibility, evolution, and controlled change across all components.

---

## Versioning Rules

- All interfaces must be versioned.
- All invariants must specify version applicability.
- Breaking changes require major version increments.
- Minor versions may introduce backward-compatible extensions.
- Patch versions may fix defects without altering behavior.

---

## Versioned Components

- FieldState schema  
- MeniscusState schema  
- PipelineState schema  
- Snapshot format  
- Interfaces and invariants  

---

## Compatibility Requirements

- New versions must preserve backward compatibility unless explicitly marked.
- Snapshot restoration must support at least one previous major version.
- Pipeline execution must remain deterministic across versions.

---

## Deprecation Policy

- Deprecated fields must remain functional for one major version.
- Removal requires explicit ADR approval.

---

## Related Documents

- [ADR](../11_adr/README.md)
- [Interfaces](../05_interfaces/README.md)
- [Invariants](../04_invariants/README.md)

