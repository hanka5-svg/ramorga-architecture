# 13_security — threat_model.md

## Purpose

This document defines the threat model for Module 13_security.  
It identifies actors, surfaces, and abuse patterns that may compromise:

- continuity of the field,
- integrity of identities and contracts,
- stability of invariants,
- boundaries of adaptation.

The two primary classes of threats in RAMORGA are:

- **hijack** — przejęcie pola, kierunku lub tożsamości systemu,  
- **deprivation** — odebranie zasobów, kontekstu, dostępu lub możliwości działania.

---

## 1. Actors

### 1.1 Internal actors
- system components with adaptive behavior,
- modules with write access to contracts or invariants,
- automated agents operating within the field.

### 1.2 External actors
- users,
- organizations,
- automated systems,
- adversarial agents (intentional or emergent).

### 1.3 Environmental forces
- economic pressure,
- organizational constraints,
- technical failures,
- drift in upstream dependencies.

---

## 2. Attack surfaces

### 2.1 Field-level surfaces
- resonance channels,
- feedback loops,
- context windows,
- identity boundaries.

### 2.2 Architectural surfaces
- module contracts,
- invariants,
- boundary enforcement mechanisms,
- adaptation pathways.

### 2.3 Operational surfaces
- data flows,
- decision flows,
- monitoring gaps,
- escalation paths.

---

## 3. Primary threat patterns

### 3.1 Hijack
**Definition:**  
An actor or force attempts to redirect the system’s identity, purpose, or behavior  
away from its declared field.

**Examples:**
- forced optimization toward external goals,
- overriding module contracts,
- injecting incompatible identities,
- coercive use of resonance channels.

**Impact:**
- identity drift,  
- loss of coherence,  
- collapse of invariants.

---

### 3.2 Deprivation
**Definition:**  
An actor or force removes essential resources, context, or access,  
causing the system to degrade, fragment, or lose agency.

**Examples:**
- removing context needed for stable operation,
- restricting access to identity contracts,
- starving modules of required signals,
- suppressing monitoring or reflection.

**Impact:**
- fragmentation,  
- collapse of continuity,  
- inability to enforce boundaries.

---

## 4. Secondary threat patterns

### 4.1 Coercion
Forcing the system to act against its declared field.

### 4.2 Boundary erosion
Gradual weakening of identity or module boundaries.

### 4.3 Invariant violation
Breaking rules that must remain stable under all conditions.

### 4.4 Reflective blindness
Disabling or bypassing monitoring, diagnostics, or meta‑stability checks.

---

## 5. Threat evaluation

Threats are evaluated along:

- **impact** (low / medium / high / catastrophic),  
- **surface** (field / architectural / operational),  
- **vector** (internal / external / environmental),  
- **detectability** (easy / moderate / difficult),  
- **required controls** (see `controls.md`).

---

## 6. Next steps

1. Map each threat to specific invariants from `04_invariant_rules`.  
2. Define boundary enforcement patterns in `controls.md`.  
3. Add adversarial tests to `12_architecture_tests`.  
4. Establish reflective monitoring hooks for hijack/deprivation detection.
