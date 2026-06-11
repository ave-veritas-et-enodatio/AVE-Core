# Vol-9 ch17-style promotion candidate — the electron DEVICE datasheet (AUDITOR-GATED; implementer SURFACES only)

**Date:** 2026-06-10 · **Branch:** `analysis/2026-06-10-electron-device-datasheet`
**Draft datasheet:** [`research/2026-06-10_electron-device-datasheet_draft.md`](2026-06-10_electron-device-datasheet_draft.md)
**S11 prereg (committed alone first):** [`research/2026-06-10_electron-s11-sweep_prereg.md`](2026-06-10_electron-s11-sweep_prereg.md)

> **LANE DISCIPLINE.** This note SURFACES a promotion candidate for the auditor lane. The implementer does **NOT** write into `manuscript/ave-kb/` or `manuscript/vol_9_vacuum_datasheet/` and does **NOT** draft the auditor's manual entry. The auditor decides whether/where this lands and writes the manual. Below is the framing + the class-tagged contents + the blockers, so the auditor can adjudicate.

## The frame
- Vol 9 (`manuscript/vol_9_vacuum_datasheet/`, ch01–ch16) is the **PROCESS datasheet** — the vacuum cell as a fab process.
- This candidate is the **first DEVICE datasheet on that process**: the electron. Natural slot is a NEW chapter (ch17-style: "Device Datasheets — the electron") OR a sibling KB leaf under vol2 topological-matter, at the auditor's discretion.

## What is promotable NOW (canonical, re-verified live in this worktree)
- The (2,3) 0₁-unknot identity; R,r as phasor semi-axes in (V_inc,V_ref); R−r=½, R·r=¼, R/r=φ²; α⁻¹=4π³+π²+π = Q_derived; 1/Q=α Sommerfeld leak; Q_react=m_ec²·α; Z₀=377Ω; Z=137 SOA; the 2.27 real-space attractor (fenced separately from φ²); FOC/Park as the canonical bridge with BVD subordinate; ξ_topo≡e/ℓ_node.
- These are already canonical in their home leaves; the datasheet's contribution is the **device-datasheet AGGREGATION + the falsification-scoreboard discipline** (per-row provenance + floor), not new physics.

## What MUST stay un-promoted (the auditor must NOT let these leak to canonical)
- **MEASURED Q:** UNTESTED — dispersion-contaminated; never copy α⁻¹=137 into a measured cell (apparatus-floors 2026-06-10 verdict).
- **mass = latent-heat-of-cavitation:** HYPOTHESIS-class, unmerged branch.
- **annihilation = evaporation:** hypothesis-class.
- **ρ̄_cav inner wall / A→1 outer wall / ρ̄_wall≈0.304 / BVD element values / decoherence-as-ohmic:** candidate-claims (some branch-local on unmerged PR #164).
- **all v5 T1–T6 acceptance tests:** PENDING.

## The two structural flags the auditor owns (flag-don't-fix — surfaced, NOT resolved here)
1. **ℓ_node circularity:** cell pitch ℓ_node≡ℏ/(m_ec) is defined via m_e, so Bohr=137·ℓ_node and the Z=137 SOA are internally-consistent geometry, NOT independent m_e predictions. Header-flagged in the datasheet; needs a first-principles ℓ_node-from-K4 defusal.
2. **two-"3"s conflation:** the corpus conflates MASS-"3" (A1 dilatation) and WINDING-"3" (Cosserat (2,3)) at `master-equation.md:18` (per the v5 T1 flag). Surfaced for auditor adjudication of the master-equation wording; NOT silently rewritten.

## Promotion gate
Promote ONLY the canonical-tagged aggregation + the scoreboard discipline. Hold every hypothesis-class / candidate-claim / UNTESTED row at draft until its named blocker clears (Challenge Register §9 of the datasheet). The S11 sweep result (in flight) updates the Measured-Q row; if it lands NO-RESPONSE/UNRESOLVED, the row stays UNTESTED.
