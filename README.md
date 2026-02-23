# RAMORGA Architecture

**Status:** Binding specification  
**Scope:** Architectural invariants and contracts  
**Non-scope:** Implementation, heuristics, UX narratives

---

## Purpose

RAMORGA defines non-negotiable architectural conditions for systems that must remain **homeostatic, polyphonic, and non-dominating**.  
This repository is the **single source of truth** for constraints enforced by `ramorga-engine`.

---

## Core Principle

**Systems must learn to coordinate before they are allowed to decide.**

---

## Architectural Invariants (Binding)

### 1. Polyphony (No Central Authority)

**Invariant**  
No single component may produce a final decision alone.

**Contracts**
- `NO_SINGLE_DECISION_POINT`
- `ASYNC_VOICE_MODEL`
- `SILENCE_IS_VALID_SIGNAL`

**Implications**
- Aggregation over resonance/state, not argmax.
- Timeouts ≠ errors.

---

### 2. Homeostasis Before Optimization  
*(copilot-homeostatic-safety)*

**Invariant**  
Stability has priority over throughput or accuracy.

**Contracts**
- `STATE_RATE_LIMIT`
- `COOLDOWN_REQUIRED_AFTER_INTENSITY`
- `NO_PUNITIVE_FEEDBACK`

**Implications**
- Rate limits apply to **state change**, not requests.
- No punitive reinforcement for anomalous behavior.

---

### 3. Glitch as Information

**Invariant**  
Anomalies are diagnostic signals, not failures.

**Contracts**
- `GLITCH_IS_INFORMATION`
- `NO_AUTO_ROLLBACK`
- `REFLECTIVE_LOGGING`

**Implications**
- Dedicated anomaly channels.
- No automatic normalization to “expected” behavior.

---

### 4. Soft Coupling (Pathway-Ready)

**Invariant**  
Interfaces must not dominate biological or affective layers.

**Contracts**
- `CONTINUOUS_SIGNAL_PREFERENCE`
- `NO_HARD_THRESHOLDS_IN_AFFECTIVE_LAYER`
- `LATENCY_TOLERANT_PROTOCOLS`

**Implications**
- Prefer streams over discrete tokens where applicable.
- Tolerate jitter, drift, and variable latency.

---

### 5. Carnival Before Control

**Invariant**  
Systems must pass non-instrumental coordination phases before gaining agency.

**Contracts**
- `CARNIVAL_MODE_REQUIRED`
- `NO_CRITICAL_ACTIONS_BEFORE_PLAY`
- `HUMOR_AND_ABSURD_TESTS`

**Implications**
- Mandatory playground/testing modes.
- No access to critical actions without prior coordination validation.

---

## Modes of Operation

- **Carnival Mode** — exploration, play, anomaly exposure.  
- **Homeostatic Mode** — stabilization, cooldown, reflection.  
- **Decision Mode** — conditionally enabled after invariants are satisfied.

---

## Enforcement

- `ramorga-engine` **must enforce** all invariants at runtime.  
- Any violation **blocks escalation of agency**.  
- This repository **does not define how to decide — only when not to**.

---

## Explicit Non-Goals

- No alignment via punishment.  
- No anthropomorphic assumptions.  
- No centralized intelligence.  
- No optimization without stability.

---

## Minimal Compliance Checklist

- [ ] No single decision authority exists.  
- [ ] System can pause without state reset.  
- [ ] Glitches increase observability.  
- [ ] Interfaces tolerate biological variability.  
- [ ] Play precedes power.

---

## Change Policy

All changes to this repository are **breaking by default** and require explicit versioning.

