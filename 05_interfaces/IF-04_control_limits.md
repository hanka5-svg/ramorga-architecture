Interface ID: IF-04
Protected Invariants: INV-04, INV-05

Interface statement:
Interfaces must not enable escalation,
reward shaping, or adaptive control loops.

Constraints:
- No reinforcement signals
- No preference scoring
- No adaptive feedback channels

Purpose:
Prevent escalation and training surface leakage.
