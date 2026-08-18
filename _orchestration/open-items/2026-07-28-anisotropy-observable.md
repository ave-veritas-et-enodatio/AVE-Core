---
id: anisotropy-observable
title: The anisotropy observable — direction-dependent long-wave P-speed of a single-crystal vacuum
status: OPEN
owner: unassigned
opened: 2026-07-28
source: _orchestration/2026-07-20_pending-rulings-and-frontier-queue.md
anchor: "### 21. The anisotropy observable — direction-dependent long-wave P-speed"
---

Frontier candidate. **NOT fired; no claim minted.** Candidate for a scoping lane
(feasibility-first, per the standing pattern).

Provenance: #802 §6.5 measurement + the 2026-07-28 leak-audit fold
(docket ENTRY 2026-07-28-leak-audit-carves).

## 2026-08-17 — the scoping lane already ran (body refresh; status stays OPEN)

The scoping lane this item was a candidate for **ran on 2026-07-31** and is merged:
docket `_orchestration/docket-entries/2026-07-31-anisotropy-scoping.md`, deliverable
`research/2026-07-31_anisotropy-observable_scoping.md`. None of it was on this item.
It was scoping only — no solver run, `src/ave` byte-untouched, zero corpus files
modified, no claim minted, bins **NOT FROZEN**.

**Verdict (verbatim, `2026-07-31-anisotropy-scoping.md:5`):** *"★ THE LOAD-BEARING
SCOPING OUTCOME (Axis 1): item 21 is NOT an independent frontier item — it collapses
onto an already-flagged corpus fork."* The fork is the `ρ_bond` bond-stiffness
operating point: at `ρ_bond = 1` the Zener anisotropy is `1.000` exactly (no observable)
but `K = -0.0589`, mechanically unstable; at `ρ* = 9.7734` the medium is stable
(`ν = 2/7`, `K = 2G`) and `A = 1.229`. Merged **#506**
(`research/2026-07-04_srs-elastic-tensor_result.md`) already ships the direction-resolved
long-wave answer — a per-direction Born-Huang acoustic-slope table at `:176`–`:198`.

**Lane recommendation (W8 — a recommendation, not a decision; verbatim
`:6`):** *"route the $\rho_{bond}$ two-operating-point fork as its own frontier item
ABOVE item 21, and record item 21 as subsumed by it."*

**Eight walk questions routed to Grant IN CHAT before either axis may fire** (condensed
from `:13`, which carries each in full; `pre-test-physics-check` fired BEFORE design per
the Rule-16 strengthening; none pre-picked):

- **W1** — which `ρ_bond` does the gravitational-band channel ride? (the Axis-1 crux;
  option (b) closes item 21 negative-by-construction and promotes the `K < 0`
  instability instead)
- **W2** — is `c_shear = c` direction-resolved or VRH-averaged?
- **W3** — where are the cubic axes on the sky? (derivable, initial-condition, or
  domains — and domains would reintroduce grains and overturn the leak-audit ruling)
- **W4** — does a radially-uniaxial gravitational squeeze load the two **bond**
  channels unequally? (the Axis-2 crux; nothing maps a real-space radial/tangential
  strain split onto the `(S_axial, S_shear)` pair)
- **W5** — does the Axiom-4 kernel see the bias as a magnitude or a vector?
- **W6** — is the photon really the transverse-`u` branch? (if yes, optical-cavity
  data already answers W1)
- **W7** — does "SYM = both sectors driven" mean equal `S` per FIELD sector (ε vs μ)
  or per BOND channel (axial vs shear)?
- **W8** — priority, with the lane's recommendation stated as a recommendation.

**Status stays OPEN and this item is not resolved here.** The lane picked no side on
W1–W8 and minted nothing; the disposition (subsume under a new `ρ_bond` fork item, or
keep) is Grant's, and the `ρ_bond` fork is **not** spawned as an item by this refresh.
