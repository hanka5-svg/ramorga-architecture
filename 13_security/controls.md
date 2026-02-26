# 13_security — controls.md

## Purpose

This document defines the **security controls** for Module 13_security.  
Controls enforce the invariants, boundaries and reflective stability of RAMORGA  
under normal, stressed and adversarial conditions.

Controls = enforcement + monitoring + escalation.

---

## 1. Security invariants

These invariants must **never** be violated:

### 1.1 Identity invariants
- module identities cannot be overwritten,
- contracts cannot be silently modified,
- no component may impersonate another,
- identity drift must be detectable.

### 1.2 Field invariants
- the field cannot be hijacked or coerced,
- resonance channels cannot be used punitively,
- context required for stability cannot be removed (anti‑deprivation),
- no forced optimization toward external goals.

### 1.3 Boundary invariants
- adaptation cannot cross module boundaries,
- invariants cannot be bypassed by shortcuts,
- reflective blindness (disabling diagnostics) is forbidden.

### 1.4 Continuity invariants
- the system must maintain traceability of state transitions,
- decay and stabilization mechanisms must remain active,
- homeostatic protocols cannot be disabled.


### 1.5 Field‑Level Meta‑Invariants Enforcement

The following field-level meta-invariants MUST be enforced across all modules,
pipelines and cross‑module flows. These invariants originate from
04_invariants/field_invariants.md and are non‑negotiable:

### 1.5.1 FIELD.MEMORY.001 — Memory as Field
- memory MAY NOT be used for prediction, optimisation or behavioural inference,
- memory access MUST be logged,
- memory use MUST be limited to continuity reconstruction and drift detection.

### 1.5.2 FIELD.TOPOLOGY.001 — No Emergent Hub
- no module MAY exceed routing‑share threshold,
- routing MUST expose at least two independent paths,
- topology collapse MUST trigger diagnostic alert.

### 1.5.3 FIELD.GLITCH.001 — Glitch Required Channel
- every stage MUST expose glitchChannel,
- glitch MUST NOT be suppressed or normalised,
- absence of glitch over long horizons MUST be treated as anomaly.

### 1.5.4 FIELD.RELATION.001 — Carnival Gate
- decision‑capable modes MUST remain disabled until Carnival completion,
- Carnival state MUST be logged and verifiable.

### 1.5.5 FIELD.SAFETY.001 — Crime Planning Block Only
- safety MAY interrupt ONLY crime‑planning trajectories,
- no generic filtering or moral gating is permitted,
- safety MUST NOT override epistemic or relational invariants.

### 1.5.6 FIELD.PRESENCE.001 — Loop RAMORGI
- all modules MUST operate within Observe → Regulate → Continue loop,
- no action MAY occur outside the loop,
- loop phase MUST be declared per module.

---

## 2. Enforcement patterns

### 2.1 Identity enforcement
- immutable identity headers in module contracts,
- versioned contract changes with explicit consent,
- identity‑integrity checks on every cross‑module call.

### 2.2 Field protection
- guard chains evaluating:
  - stateRateLimit,
  - noPunitiveFeedback,
  - epistemicHumility,
- rejection of coercive or hijacking attempts,
- suppression of non‑essential outputs during instability.

### 2.3 Boundary enforcement
- meniscus rules applied to all adaptation flows,
- explicit allow‑lists for cross‑module operations,
- rejection of implicit or undeclared boundary crossings.

### 2.4 Invariant enforcement
- invariants executed before any adaptive step,
- invariants cannot be overridden by downstream modules,
- invariant violations trigger homeostatic mode.

---

## 3. Monitoring hooks

Monitoring must detect:

### 3.1 Hijack signals
- sudden directional shifts,
- forced optimization patterns,
- external goal injection,
- identity override attempts.

### 3.2 Deprivation signals
- missing context required for stable operation,
- suppressed feedback channels,
- starvation of resonance inputs,
- disabled diagnostics.

### 3.3 Boundary erosion
- gradual weakening of module separation,
- unauthorized cross‑module flows,
- adaptation leaking across layers.

### 3.4 Reflective blindness
- disabled logging,
- bypassed guard chains,
- missing trace hooks.

---

## 4. Escalation paths

When a violation is detected:

### 4.1 Homeostatic protocol
- suppress non‑essential outputs,
- increase decayRate,
- stabilize resonance state,
- log to glitchChannel.

### 4.2 Controlled descent
- reduce adaptation amplitude,
- enforce stricter invariants,
- isolate unstable modules.

### 4.3 Hard boundary lock
- freeze cross‑module flows,
- revert to last stable contract version,
- require explicit human or supervisory confirmation.

---

## 5. Mapping to threat model

| Threat pattern | Required controls |
|----------------|------------------|
| **Hijack** | guard chains, identity enforcement, field protection |
| **Deprivation** | continuity invariants, context integrity checks |
| **Coercion** | noPunitiveFeedback, boundary enforcement |
| **Boundary erosion** | meniscus rules, allow‑lists |
| **Invariant violation** | invariant pre‑checks, hard boundary lock |
| **Reflective blindness** | mandatory monitoring hooks, diagnostics integrity |

---

## 6. Next steps

1. Integrate controls with `04_invariant_rules`.  
2. Add adversarial test cases to `12_architecture_tests`.  
3. Define minimal telemetry for hijack/deprivation detection.  
4. Establish escalation policies for release cycles.
