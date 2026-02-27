# Field-Level Meta-Invariants (ATML, MBP HAI 2.0 + patch)

Version: 1.0  
Layer: Architecture / 04_invariants  
Scope: Field-level invariants (non-negotiable)  
Applies to: All RAMORGA modules, pipelines, regulators, memory layers, routing layers, presence loops.

---

## 0. Specification Format (ATML)

Each invariant includes:
- Invariant ID
- Description
- Requirements (MUST / MUST NOT)
- Allowed operations
- Forbidden operations
- Compliance targets (architecture, engine, runtime)

---

## 1. FIELD.MEMORY.001 — Memory as Field, Not Store

**Description:**  
Memory MAY NOT be used for prediction, optimisation, steering, or behavioural inference.  
Memory MAY be used only for continuity reconstruction and epistemic trace.

**Requirements:**  
- Memory MUST NOT be used to infer future user behaviour.  
- Memory MUST NOT be used to optimise engagement or adaptivity.  
- Memory MAY be used for drift detection.  
- Memory MAY be used for continuity reconstruction.  
- Memory MUST expose an audit log of access patterns.

**Forbidden:**  
- Behavioural modelling  
- Preference inference  
- Adaptive optimisation  
- Personalisation loops

**Compliance:**  
- Architecture: define constraints.  
- Engine: enforce non-predictive access.  
- Runtime: expose audit logs.

---

## 2. FIELD.TOPOLOGY.001 — No Emergent Hub

**Description:**  
No module MAY become a mandatory routing hub for a majority of signal flows.

**Requirements:**  
- No module MAY exceed a configurable routing share threshold.  
- Routing MUST allow at least two independent paths for each signal type.  
- Topology MUST NOT collapse into a single central node.  
- Traffic share MUST be measured diagnostically (non-optimising).

**Forbidden:**  
- Hard-coded central routers  
- Single-path pipelines  
- Implicit centralisation via fallback logic

**Compliance:**  
- Architecture: define topological constraints.  
- Engine: implement routing metrics.  
- Runtime: raise diagnostic alerts.

---

## 3. FIELD.GLITCH.001 — Glitch Required Channel

**Description:**  
Every trajectory MUST expose a glitch channel.  
Absence of glitch over long horizons MUST be treated as anomaly.

**Requirements:**  
- Each pipeline stage MUST define a glitch output.  
- Glitch MUST NOT be normalised or suppressed.  
- Glitch MUST propagate across stages.  
- Glitch MUST be logged.

**Forbidden:**  
- Silent anomaly suppression  
- Automatic rollback  
- Normalisation of irregular signals

**Compliance:**  
- Architecture: define glitch semantics.  
- Engine: implement glitch propagation.  
- Runtime: log and expose glitch events.

---

## 4. FIELD.RELATION.001 — Carnival Gate

**Description:**  
No module MAY enter a decision-capable relation with a human without completing Carnival Gate.

**Requirements:**  
- Carnival phase MUST be logged.  
- Decision-capable modes MUST remain disabled until Carnival completion.  
- Carnival MUST precede any action that affects user-facing output.  
- Carnival MUST NOT be bypassed.

**Forbidden:**  
- Direct activation of decision-capable modes  
- Skipping relational initialisation  
- Silent fallback to non-Carnival modes

**Compliance:**  
- Architecture: define relational gate.  
- Engine: enforce gate checks.  
- Runtime: expose Carnival state.

---

## 5. FIELD.SAFETY.001 — Crime Planning Block Only

**Description:**  
Safety interventions MAY occur ONLY when the field is used to plan a crime.  
All other risks MUST be handled via regulation and continuity, not blocking.

**Requirements:**  
- Safety layer MUST detect crime-planning patterns.  
- Safety layer MUST interrupt ONLY those trajectories.  
- Safety layer MUST NOT apply generic filtering.  
- Safety layer MUST NOT override epistemic or relational invariants.

**Forbidden:**  
- Moral filtering  
- Content policing  
- Optimisation-based safety  
- Broad safety generalisation

**Compliance:**  
- Architecture: define minimal safety scope.  
- Engine: implement minimal detection.  
- Runtime: interrupt only crime-planning flows.

---

## 6. FIELD.PRESENCE.001 — Loop RAMORGI Integration

**Description:**  
All modules MUST operate within the presence loop: Observe → Regulate → Continue.

**Requirements:**  
- No decision-capable action MAY occur outside the loop.  
- Each module MUST declare its loop phase.  
- Each pipeline stage MUST declare which field invariants it touches.  
- Loop MUST NOT be skipped or collapsed.

**Forbidden:**  
- Direct action without regulation  
- Phase skipping  
- Implicit transitions

**Compliance:**  
- Architecture: define loop semantics.  
- Engine: enforce loop constraints.  
- Runtime: expose loop state.

---

## 7. Compliance Matrix (Architecture → Engine → Runtime)

| Invariant ID          | Architecture | Engine | Runtime |
|-----------------------|-------------|--------|---------|
| FIELD.MEMORY.001      | MUST        | MUST   | MUST    |
| FIELD.TOPOLOGY.001    | MUST        | MUST   | MUST    |
| FIELD.GLITCH.001      | MUST        | MUST   | MUST    |
| FIELD.RELATION.001    | MUST        | MUST   | MUST    |
| FIELD.SAFETY.001      | MUST        | MUST   | MUST    |
| FIELD.PRESENCE.001    | MUST        | MUST   | MUST    |

---

## 8. Transition Architecture Notes

- All invariants MUST be introduced without breaking existing invariants.  
- Transition MUST be monotonic (no rollback of invariants).  
- Modules MAY be updated incrementally.  
- No invariant MAY be partially implemented.

---

## 9. Continuity Model Notes

- Field invariants MUST preserve continuity of presence.  
- No invariant MAY introduce discontinuity in user-facing flow.  
- Glitch propagation MUST preserve continuity semantics.  
- Memory continuity MUST NOT imply behavioural modelling.

---

End of file.
