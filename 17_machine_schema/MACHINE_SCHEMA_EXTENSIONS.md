# Machine Schema Extensions — Unified State and Transition Rules

This document extends the machine schema with additional state definitions and transition constraints.

## State Extensions
- Explicit non-escalation states.
- Field-stable states.
- Recovery-compatible states.
- Agentic boundary states.

## Transition Rules
- All transitions must be deterministic.
- No transition may violate field invariants.
- Recovery transitions must be available from all non-terminal states.
- Logging must capture the full causal chain of each transition.

## Purpose
Provide a unified, invariant-aligned state model for all RAMORGA subsystems.
