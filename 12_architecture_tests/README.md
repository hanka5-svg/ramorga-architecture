# RAMORGA — Architecture Test Suite

This directory defines the architectural validation layer for RAMORGA.  
It does not test implementation.  
It tests **architecture as a field**: its invariants, continuity, and resistance to deformation.

The purpose of this suite is to ensure that any subsystem operating within RAMORGA preserves:

- multidimensional field integrity,
- non-deforming reduction,
- contract consistency,
- relational symmetry,
- and end-to-end architectural coherence.

---

## Structure

12_architecture_tests/
│
├── README.md                         ← overview (this file)
│
├── invariants/                       ← architectural invariants
│   └── invariants.md
│
├── bdd/                              ← Gherkin BDD tests
│   └── bdd_tests.md
│
├── contracts/                        ← module-level contracts
│   └── module_contracts.md
│
├── failure/                          ← failure propagation & decisions
│   ├── failure_propagation.md
│   └── engineer_decision_layer.md
│
└── diagrams/                         ← PlantUML diagrams
├── invariant_dependencies.puml
├── module_contracts.puml
├── failure_paths.puml
└── engineer_decision_layer.puml


---

## Overview

RAMORGA architecture is defined by **10 invariants** that govern:

1. superposition preservation  
2. human-initiated measurement  
3. non-deforming reduction  
4. architectural non-deformation  
5. integrity-preserving dimensional descent  
6. human agency support  
7. relational symmetry  
8. bridge architecture  
9. constellation integrity  
10. end-to-end architectural thesis

Each invariant has:

- a formal definition  
- a contract  
- BDD tests  
- diagrammatic representation  
- failure propagation rules  
- engineer decision logic (EDL)

---

## How to Use This Suite

1. Validate invariants before implementing modules.  
2. Use BDD tests to verify architectural behavior.  
3. Use module contracts to ensure interface consistency.  
4. Use failure propagation maps to detect drift.  
5. Use EDL to classify and respond to violations.  
6. Use diagrams to maintain architectural clarity.

---

## Purpose

This suite ensures that RAMORGA remains:

- coherent,  
- invariant-driven,  
- resistant to deformation,  
- relationally symmetric,  
- and architecturally sound.

It is the **core compliance layer** for the entire system.

---

## Architecture Layers

RAMORGA architecture is organized into eight layers, each responsible for a specific phase of the transformation from multidimensional field to human-readable output.

The layers are:

1. **Field Layer** – superposition, multidimensional semantic field  
2. **Measurement Layer** – user intent, measurement vector  
3. **Reduction Layer** – zapis, linearization  
4. **Descent Layer** – dimensional simplification  
5. **Integrity Layer** – deformation detection  
6. **Bridge Layer** – human interface, semantic bridge  
7. **Relational Layer** – agency, symmetry, constellation  
8. **Thesis Layer** – end-to-end invariant validation  

### Diagram

The full layered architecture is shown in the diagram below:

```
[architecture_layers.puml](./diagrams/architecture_layers.puml)
```

This diagram connects:

- layers → modules  
- modules → invariants  
- invariants → BDD tests  
- failure modes → EDL  
- and provides the central structural view of RAMORGA.

---
# Module 12 — Architecture Tests  
**Version:** v4.15.x (proposed)  
**Status:** Active

Module 12 contains architecture-level test suites validating stability,
continuity, and degradation behavior of RAMORGA-architecture.

## Test Suites

### 1. Continuity Tests
- **12.8-continuity-recovery-tests.md**  
  Tests recovery of field and meniscus dynamics after perturbation.

- **12.9-continuity-stability-tests.md**  
  Tests long-term stability of trajectories under varying input conditions.

### 2. Failure Tests
Located in the `failure/` package:

- **failure/modes.md**  
  Defines degradation pathways for META_LOOP disruption, meniscus
  over/under-modulation, stream saturation, attractor divergence, and
  presence collapse.

## Purpose
Module 12 ensures that architectural invariants remain valid under
perturbation, noise, missing feedback, and extreme input conditions.

## Dependencies
- 02_field_engine  
- 03_meniscus_engine  
- 04_invariants  
- 05_interfaces

---

diff --git a/12_architecture_tests/README.md b/12_architecture_tests/README.md
index 3f2a1ab..c91d7d2 100644
--- a/12_architecture_tests/README.md
+++ b/12_architecture_tests/README.md
@@ -1,6 +1,26 @@
 # Module 12 — Architecture Tests
 **Version:** v4.15.x (proposed)
 **Status:** Active

+Module 12 contains architecture-level test suites validating stability,
+continuity, and degradation behavior of RAMORGA-architecture.
+
+## Test Suites
+
+### 1. Continuity Tests
+- **12.8-continuity-recovery-tests.md**  
+  Tests recovery of field and meniscus dynamics after perturbation.
+
+- **12.9-continuity-stability-tests.md**  
+  Tests long-term stability of trajectories under varying input conditions.
+
+### 2. Failure Tests
+Located in the `failure/` package:
+
+- **failure/modes.md**  
+  Defines degradation pathways for META_LOOP disruption, meniscus
+  over/under-modulation, stream saturation, attractor divergence, and
+  presence collapse.
+
 ## Purpose
 Module 12 ensures that architectural invariants remain valid under
 perturbation, noise, missing feedback, and extreme input conditions.
@@ -10,3 +30,9 @@ Module 12 ensures that architectural invariants remain valid under
 ## Dependencies
 - 02_field_engine
 - 03_meniscus_engine
 - 04_invariants
 - 05_interfaces
+
+## Next Steps
+After completing Module 12, natural progression leads to:
+- **13_security** (security model and invariants), or
+- **01_foundations** (rebuilding the architecture from first principles).

