# Changelog Extensions — Rules for Recording Architectural Evolution

This document extends the changelog module with additional rules for documenting system evolution.

## Recording Requirements
- All architectural changes must reference affected invariants.
- Cross-layer changes must include dependency impact notes.
- Breaking changes must include migration instructions.
- Each entry must specify whether the change affects runtime, contracts, or documentation.

## Structure
- Version identifier.
- Summary of change.
- Impacted modules.
- Migration or compatibility notes.
- Reference to related ADRs.

## Purpose
Ensure transparent, deterministic documentation of RAMORGA evolution.
