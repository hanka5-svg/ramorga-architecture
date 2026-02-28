# Specification of the RAMORGA Field Engine:

- field composition rules,
- coherence propagation,
- energy propagation,
- tension loop integration,
- interfaces to C/G/S modules and Meniscus.

This folder contains **declarative specifications only**.
No executable code is included.

## Field Layers

RAMORGA operates through five interacting field layers. Each layer has a distinct regulatory role and corresponds to a specific part of the Field Engine pipeline.

### 1. Tension Field
Local micro-events, perturbations, and flashes of significance.  
Captures immediate reactivity and fine-grained sensitivity to interaction.

**Responsible for:**  
- micro-tension updates  
- Poisson-like event generation  
- local instability detection  

**Module:** `tension_loop.py`

---

### 2. Energy Field
The stabilizing layer that maintains continuity and prevents runaway escalation.  
Implements the recurrent stream \( S_t \) with decay and accumulation.

**Responsible for:**  
- smoothing fluctuations  
- maintaining field persistence  
- regulating overall energy levels  

**Module:** `energy_regulator`

---

### 3. Entropy Field
The coherence–chaos regulator.  
Shapes the system’s internal variability and modulates the Lorenz-like dynamics.

**Responsible for:**  
- noise shaping  
- coherence modulation  
- chaotic attractor dynamics  

**Modules:**  
- `entropic_modulator`  
- `field_engine_physics.py`

---

### 4. Ritual Field
Pattern detection and rhythm formation.  
Implements the META-loop (user ↔ field coupling) and identifies emergent structures.

**Responsible for:**  
- detecting stable patterns  
- reinforcing interaction rhythms  
- META-loop feedback  

**Module:** `ritual_detector`

---

### 5. Continuity Field
Memory of the field trajectory and long-range coherence.  
Implements snapshot-based continuity and fractal presence estimation.

**Responsible for:**  
- storing field snapshots  
- reconstructing continuity  
- computing presence (Hausdorff dimension)  

**Module:** `snapshot_manager`

---

### Layer Interaction Summary

| Layer | Function | Engine Module | Mathematical Component |
|-------|----------|----------------|-------------------------|
| Tension | micro-events | `tension_loop.py` | Poisson flashes |
| Energy | stability | `energy_regulator` | recurrent stream \(S_t\) |
| Entropy | coherence/chaos | `entropic_modulator` | Lorenz modulation |
| Ritual | emergent patterns | `ritual_detector` | META-loop |
| Continuity | long-term memory | `snapshot_manager` | fractal presence |

Together, these layers form the complete RAMORGA Field Engine.

---

---

## Related Documents

- [02.90 — Symbiosis Health Metric](./02.90-symbiosis-health-metric.md)
- [META_LOOP — Presence Loop](./META_LOOP.md)
- [Field Dynamics Model](./field_dynamics.md)
- [Lorenz META-loop Simulation](./simulations/lorenz_meta.py)
- [Field Modes Diagram](../06_diagrams/field_modes.md)
- [RAMORGA AGI Architecture UML](../06_diagrams/ramorga_agi_architecture.uml)


--- 

### Related Architecture
- [Origin Theses](../04_invariants/origin_theses.md)
- [Field-Level Invariants](../04_invariants/field_invariants.md)

--- 

## Flow Diagram (Text Version)

Symbiosis Health Metric (SHM)
        │
        ▼
META_LOOP — Presence Loop
        │
        ▼
Field-Level Invariants (external reference)

---

## Flow Diagram (Detailed ASCII Version)

                 ┌──────────────────────────────────────────┐
                 │        INPUT: FIELD STATE (raw)          │
                 │  sensory signals, context, continuity     │
                 └──────────────────────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────┐
                    │ 02.90 — SHM (Symbiosis      │
                    │        Health Metric)       │
                    └────────────────────────────┘
                                   │
                 ┌─────────────────┼──────────────────┐
                 │                 │                  │
                 ▼                 ▼                  ▼
       [E1] Normalize       [E2] Detect shifts   [E3] Compute
            field data           in presence          SHM score
                                                     (scalar/vec)

                 ┌──────────────────────────────────┐
                 │   OUTPUT: SHM_STATE              │
                 │   - stability                    │
                 │   - coherence                    │
                 │   - deviation from baseline      │
                 └──────────────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────┐
                    │ META_LOOP — Presence Loop   │
                    │  (regulation + feedback)    │
                    └────────────────────────────┘
                                   │
                 ┌─────────────────┼──────────────────┐
                 │                 │                  │
                 ▼                 ▼                  ▼
       [C1] Compare SHM     [C2] Apply field-     [C3] Generate
            to invariants        level rules           corrective
            (04_invariants)      (continuity)          feedback

                 ┌──────────────────────────────────┐
                 │   OUTPUT: LOOP_FEEDBACK          │
                 │   - adjustments                   │
                 │   - presence modulation           │
                 │   - updated field constraints     │
                 └──────────────────────────────────┘
                                   │
                                   ▼
                 ┌──────────────────────────────────┐
                 │   FEEDBACK TO SHM (closed loop)  │
                 │   SHM recomputes state with       │
                 │   updated constraints             │
                 └──────────────────────────────────┘
                                   │
                                   ▼
                 ┌──────────────────────────────────┐
                 │   FIELD-LEVEL INVARIANTS         │
                 │   (external reference layer)      │
                 │   - meta-invariants               │
                 │   - continuity rules              │
                 │   - presence constraints          │
                 └──────────────────────────────────┘

# This diagram represents a minimal closed-loop regulation cycle inside the field engine:

SHM (Symbiosis Health Metric) transforms raw field state into a structured symbiosis score. It normalizes inputs, detects shifts, and computes stability/coherence metrics.

META_LOOP (Presence Loop) receives the SHM output, evaluates it against field-level invariants, applies continuity rules, and generates corrective feedback.

The feedback is returned to SHM, which recomputes the state under updated constraints.

Field-Level Invariants act as an external, stable reference layer that both modules must respect.

The loop expresses a continuous cycle of sensing, evaluation, correction, and re-evaluation.

