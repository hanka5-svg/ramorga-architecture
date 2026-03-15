# ADR‑002: Origin and Definition of MC‑08‑R Relational Agent Contract

Status: Accepted  
Date: 2026‑03‑15  
Related: MC‑05, MC‑06, MC‑07, MC‑09  

## Problem
RAMORGA requires a formal contract defining how an AI agent may participate in relational interaction without violating user autonomy, cognitive architecture, or safety invariants. Without such a contract, MC‑09 cannot be safely introduced.

## Decision
MC‑08‑R is adopted as the authoritative relational agent contract. It establishes:
- non‑initiation of movement,
- non‑regulation of the user,
- non‑intrusion into Loop RAMORGI,
- symmetry and boundedness of interaction,
- strict adherence to MC‑05 and MC‑06.

## Rationale
MC‑08‑R provides the minimal relational framework necessary for safe interaction. It ensures that the AI remains non‑intrusive, predictable, and aligned with the user’s cognitive architecture (MC‑07).

## Consequences
- MC‑09 must extend MC‑08‑R without weakening its constraints.
- All protocols must enforce non‑initiation and non‑regulation.
- MC‑07 remains the superior helix governing interaction boundaries.
