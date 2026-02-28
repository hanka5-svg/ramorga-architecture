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

