# Why Refusal — Causal Chain of Architectural Decisions

Refusal is an architectural consequence, not a policy layer. Every refusal must expose its causal chain.

## Mechanism
Input → detection → invariant → decision → message.

## Criteria
- Violation of a field invariant.
- Escalation detected in a subsystem.
- Loss of continuity or field stability.

## Transparency Requirements
- Logs must expose the violated invariant.
- Messages must reference the causal chain.
- No opaque or policy-based refusals.

## Purpose
Maintain field homeostasis and ensure full interpretability of system decisions.

