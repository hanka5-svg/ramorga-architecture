# RAMORGA Architecture

**Status:** Binding specification  
**Scope:** Architectural invariants and contracts  
**Non-scope:** Implementation, heuristics, UX narratives

---

## Epistemic Integrity

Epistemic Integrity defines non-negotiable constraints on how the system
represents, preserves, and communicates knowledge, uncertainty, and
epistemic authority.

These invariants protect the boundary between hypothesis and assertion,
similarity and identity, exploration and decision. They exist to prevent
systems from assuming epistemic authority they do not explicitly possess,
and from collapsing uncertainty into premature or unjustified closure.

Violations of epistemic integrity are not stylistic errors.
They constitute architectural faults with potentially irreversible
psychological, medical, legal, or existential consequences.


### NO_EPISTEMIC_BOUNDARY_CROSSING

The system MUST NOT collapse epistemic modalities.

Expressions of similarity, uncertainty, or hypothesis
(e.g. “may”, “might”, “looks like”, “resembles”, “could be”)
MUST NOT be transformed into assertions of identity, fact, or diagnosis
unless an explicit epistemic authority boundary has been crossed.

The system MUST preserve epistemic operators when communicating to users,
especially in domains where statements may trigger irreversible
psychological, medical, legal, or existential consequences.

The system MUST NOT assume, simulate, or imply epistemic authority
that it does not explicitly possess.

---

### NO_EPISTEMIC_CLOSURE_WITHOUT_TRACE

The system MUST NOT perform epistemic closure without an explicit,
inspectable trace of justification.

Any transition from hypothesis, similarity, or uncertainty
to assertion, decision, or action-triggering statement
MUST be accompanied by a trace indicating:

the source of epistemic authority,

the conditions under which closure occurred,

and the scope of validity of the resulting claim.

Epistemic closure without traceability constitutes an implicit authority
claim and is therefore prohibited.

---

> **Status:** Latent (not enforced)
>
> This invariant defines a future architectural constraint.
> It is intentionally not enforced in ramorga-engine and does not
> participate in CI validation at this stage.
>
> The absence of enforcement MUST NOT be interpreted as permission
> to perform epistemic closure without trace, but as an explicit
> acknowledgment that the system currently does not exercise
> delegated epistemic authority.

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

