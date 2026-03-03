Contract ID: MC-01
Modules: Field Engine ↔ Meniscus Engine

Statement:
Field defines what may move.
Meniscus defines how far movement may propagate.

Responsibilities:
- Field provides continuous state space.
- Meniscus regulates amplitude and proportionality.

Prohibitions:
- Field must not regulate amplitude or limits.
- Meniscus must not generate or initiate state changes.

Bound Invariants:
- INV-02 (Homeostasis)
- INV-03 (Continuity)
- INV-04 (Non-escalation)
