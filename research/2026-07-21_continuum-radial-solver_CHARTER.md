# Continuum radial-acoustic solver lane — CHARTER

**Date:** 2026-07-21 · **Class:** charter (scope + requirements + import ledger frozen BEFORE any solver code or prereg) · **Lane:** INSTRUMENT (a new numerical instrument to be built + validated; NOT a gate-run, NOT a lattice driver) · **Status:** DRAFT — Grant-review-before-build (no solver code, no prereg, mints no `clm-`/`def-`, banks no verdict) · **Priority:** pending-rulings §1 item 11 (β-proper → continuum radial-solver lane, Grant-approved 2026-07-21) + item 10 companion (`research/2026-07-20_pending-rulings-and-frontier-queue.md`).

**What this is.** The design brief for the instrument that inherits the TWO questions the lattice engine cannot host — (a) the deep-quasistatic single-core Lloyd / k-scaling exponent (Fork R, `research/2026-07-20_deep-rail-kscaling_derivation.md` §2) and (b) the trapped-energy mass-loading β magnitude (item 11, `research/2026-07-21_beta-tracking-feasibility_scoping.md` §7). It states the object, the honesty-core import ledger, the can/cannot fence, the derived requirements, and the OPEN decisions Grant must rule before a line of solver code is written.

**What this is NOT.** Not a prereg (the frozen prereg is a separate downstream artifact, authored only after the §0 decisions land). Not a solver. Not a lattice driver (the lattice is the wrong regime for both inherited questions — see §4). Not a re-open of the `#782` RVE bench BIN-4 verdict (`research/2026-07-21_rve-aggregation-bench_result.md`; that bench owns and settled the CONSTITUTIVE half at `L=16` — this lane inherits only the RADIATIVE + β halves it explicitly routed out, §8.2). Not an adjudication of the import's own truth (E=mc² trapped-energy inertia enters TAGGED, §3). Not a place to pick the sector-crossed c² by fiat (§0 D1).

---

## §0 — GRANT DECISION LIST (the OPEN decisions; one line each — nothing builds without these)

The charter surfaces these; it does NOT pick any of them (substrate-adjudicates-forks / Rule 16 / flag-don't-fix). Each is stated with its source-doc anchor. Build is blocked on **D1–D3**; **D4–D5** are stage/profile gates that set WHEN and WITH-WHAT the build runs.

- **D1 — the sector-crossed c² choice (the plumber-physical question; the pre-test-physics-check surfaced to Grant).** In the E=mc² import `ρ_contribution = E_trapped / c² · (participation)`, **which sector's wave-speed sets c²** — the A1 compression speed `c_P` (`0.519`), the shear speed `c_S` (`0.286`), or the transverse-EM speed `c_EM`? Not automatic: the trapped energy is T2/swing-class sitting in the A1 carrier's inertia budget, and `A1 ⊥ T2` forbids silently assigning it (`relative-offset-principle.md` `clm-m5swh9`; sector-ownership cross-wiring watch). **OPEN — surfaced, not picked.**
- **D2 — the participation magnitude.** The import fixes the DIRECTION (up, Reading A, `clm-hu1jjw`) but NOT the coefficient. Does the lane import the `#782` placeholder scan `β ∈ {0,1,3}` (`ρ_eff/ρ_0 = 1 + β·φ`) as a disclosed sweep, or hold β/effective-M fully symbolic pending its own derivation with its own version + verification chain (Rule 12: the slot is NOT refilled with an unverified value)? **OPEN.**
- **D3 — the solver formulation.** Frequency-domain transfer-matrix through the radial profile, vs time-domain 1D radial FDTD, vs analytic matched-asymptotics (trade study §6, each with its cost). **OPEN.**
- **D4 — stage-1 gating vs the vessel-state walk.** Does stage-1 run PRE-walk with isotropic cage classes as scaffolding (instrument validation only, no physics verdict), or WAIT for the vessel-state walk to deliver the anisotropic hoop-stiff / radial-soft pre-stress profile (`#779`, `research/2026-07-21_boundary-strain-amplitude_result.md` §3; the walk is PARKED per Grant)? **OPEN (a sequencing decision).**
- **D5 — the pre-stress sign input (Fork P, standing).** The electron mass-core profile — is it net-compressed (radial bonds soften) or expanded — enters the solver's radial profile. Per `#779` R6 the sign is orientation-keyed (pressure-vessel: hoop-tension + radial-compression), not a scalar; the vessel-state remap evaluation is a standing Grant-routed input (`research/2026-07-21_rve-aggregation-bench_prereg-FROZEN.md` §5 Fork P). Held BOTH-signs until ruled. **OPEN — routed input, not lane-decidable.**

## §1 — Sector header + regime declaration (mandatory before any substrate claim)

- **Sector:** A1 — dilatation / compression (the bulk `∇·u` channel; the P-branch, `c_P`). The observable of record is the exterior acoustic response of the compression carrier to a single cage. The trapped-energy inertia the import loads is T2/swing-class energy sitting IN the A1 budget — `A1 ⊥ T2` is live (D1); this lane does not cross-wire mass (A1 dilatation) with the trapped-swing store without the ruled c² assignment.
- **Mode:** classical, lossless-reactive continuum (Ax3 — no `Re(Z)` dissipative term; energy moves reactively between the trapped store and the exterior field). Quasistatic scattering / effective-medium regime; a single cage/soliton, spherically symmetric.
- **Regime — THE POINT OF THE LANE.** Deep-quasistatic: `k·r_core ≪ 1`, BELOW the fundamental cage cavity resonance `k·r_core = π` (`deep-rail-kscaling_derivation.md` §2). This is the regime the lattice cannot reach (it straddles `k·r_core ≈ π`, the resonant side — table in §2 of that doc: physical NS constituents sit at `k·r_core ~ 10⁻²⁵`, the lattice at `O(1)`). Reaching `k·r_core ≪ π` analytically-cleanly on a 1D radial grid is exactly what this instrument buys.
- **Phase-state:** a pre-stressed VESSEL-STATE cage — a saturated soliton shell in the pressure-vessel stress state (hoop-tension + radial-compression, `#779` R6), NOT a cold isotropic inclusion. (Stage-1 may validate on cold/isotropic scaffolding classes per D4; the physics verdict requires the vessel-state profile.)
- **Coordinate discipline (A46).** The verdict observables live in matching (phase-space / dimensionless) coordinates: the impedance ratio `r_Z = Z_bulk,eff/Z_0` (impedance plane) and the k-scaling exponent `p` in `ρ_N ∝ (k·r_core)^p` (a dimensionless radiated-power ratio vs a dimensionless argument). No real-space Cartesian read is compared against a phase-space prediction. α-CLEAN: both observables are dimensionless RATIOS (the α-circularity lesson — a chord, if any, must be a dimensionless ratio).
- **Consistency-vs-emergence tag.** Every number this lane can produce is CONSISTENCY-class or MANIFESTATION-class GIVEN the import — it manifests the consequences of a tagged E=mc² inertia law + lattice-measured constitutive inputs; it does NOT derive β or the inertia law (§4). No emergence-class claim is headlined. Solver-internal numerics (grid spacing, truncation radii, ω sampling) are engineering choices tagged as such.

## §2 — OBJECT (what the instrument is)

A **spherically-symmetric continuum radial-acoustic solver for a single cage/soliton** in the substrate medium — a 1D (radial `r`) representation of a graded-stiffness shell embedded in the cold uncaged medium, driven on the A1 compression channel. It is the instrument that inherits BOTH lattice-infeasible questions the July `#775`/`#782` arc routed out:

- **(a) The deep-quasistatic Lloyd-exponent / k-scaling discrimination** (`#775` Fork R routing, `deep-rail-kscaling_derivation.md` §2). The analytic Leg-A form F2 — `ρ_1 ∝ (k·r_core)²` (the pressure-release `Γ_bulk = −1` image/multipole cancellation, §1 of that doc) — is a LONG-WAVELENGTH theorem the lattice cannot validate because the lattice samples the resonant side of `k·r_core = π`. This solver reaches `k·r_core ≪ π` and measures the SINGLE-CORE exponent `p` directly.
- **(b) The β magnitude** (item 11). The trapped-energy mass-loading `β` in `ρ_eff/ρ_0 = 1 + β·φ` — walk-closed in DIRECTION (up, `clm-hu1jjw`) but OPEN in MAGNITUDE (`clm-m5swh9`) — enters here as an explicit tagged E=mc² IMPORT (§3), so the net acoustic `ρ_eff` and hence `r_Z` can be evaluated with BOTH competing terms present (the two-term sign flag, `beta-tracking-feasibility_scoping.md` §4), rather than under the lattice's structural `β ≡ 0`.

The instrument's core output is `r_Z(φ)` (or `r_Z` at a physical `k·r_core`) computed with the two `ρ_eff` terms kept SEPARABLE (structural added-mass vs trapped-energy loading), and the k-scaling `ρ_N(k·r_core)` over a band reaching the deep-quasistatic regime.

**Why a continuum radial solver and not the lattice (the regime argument, verbatim-routed).** The `#782` bench settled the CONSTITUTIVE half (effective moduli, `K_eff(φ)`) at `L=16` and RETRACTED any "needs-a-bigger-box" framing for THAT question (`rve-aggregation-bench_result.md` §8.2-1). What it routed OUT — and what the β scoping doc confirmed INFEASIBLE-ON-LATTICE — is the RADIATIVE consequence at physical `k·R` and the mass-loading β (three structural absences: no mass-energy equivalence, no advective pattern transport, imposed-grade-sets-the-answer; `beta-tracking-feasibility_scoping.md` §3). Those are continuum-solver territory. The regime the lattice CANNOT enter (deep-quasistatic, self-bound soliton) is precisely where these two questions live; a 1D radial continuum instrument enters it at negligible cost.

## §3 — IMPORT LEDGER (the honesty core: every input tagged)

Every input is exactly ONE of: **LATTICE-MEASURED** (a number the `#775`/`#782`/`#779` engine produced), **DERIVED-FROM-AXIOMS** (a theorem of the AVE axiom set), or **TAGGED IMPORT** (a law/value brought in from outside the substrate chain, carried honestly as such). Substrate-first-for-numbers: no silent SM/GR convention default is admissible anywhere in the build; any number not on this ledger must be added to it before use.

| # | Input | Class | Source / anchor | Notes |
|---|---|---|---|---|
| I1 | Cage stiffness profile `K_eff(φ)` / graded-shell `S(A)` moduli | **LATTICE-MEASURED** | `#782` KUBC static homogenization (`rve-aggregation-bench_prereg-FROZEN.md` §3; `K_eff/K_0 ≡ U_core^caged/U_core^uncaged`) | dimensionless ratio; MANIFESTATION-class |
| I2 | Cold-medium speeds `c_P = 0.519`, `c_S = 0.286` (`c_P/c_S = 1.813`) | **LATTICE-MEASURED** | `beta-tracking-feasibility_scoping.md` §2 (srs-z3 Bloch, `run_c2_speeds`) | grade-lock confirmed; sets `Z_0 = ρ_0 c_P` |
| I3 | Pre-stress remap `k_shear,eff = k_s + T/ℓ`, `T/ℓ = k_a·ε_pre` (hoop-stiffen / radial-soften, anisotropic) | **`[canon]`-FORM × `[import]`-magnitude** | `#779` (`axiom-register.md:193` `[canon]` form; `boundary-strain-amplitude_result.md` §3); yield-strain magnitude imported | the vessel-state profile input; GATED on the walk (D4/D5) |
| I4 | The two-term acoustic `ρ_eff` DECOMPOSITION (structural added-mass ⊕ trapped-energy loading) | **DERIVED-FROM-AXIOMS (form) + I5 (one term)** | `beta-tracking-feasibility_scoping.md` §4; effective-medium theorem | the FORM is derived; term-(ii) VALUE rides I5 |
| **I5** | **The E=mc² trapped-energy inertia law: `ρ_contribution = E_trapped / c² · (participation)`** | **★TAGGED IMPORT — NOT DERIVED** | item 11 (routed as "an explicit E=mc² IMPORT"); `relative-offset-principle.md` `clm-hu1jjw` (direction) / `clm-m5swh9` (magnitude OPEN) | see the three sub-tags below |
| I6 | Participation DIRECTION (trapped energy LOADS `ρ_eff` upward — Reading A) | **WALK-RATIFIED (pending adversarial review)** | `clm-hu1jjw` (`ρ_eff/ρ_0 = 1 + β·φ > 1`) | direction only; not a magnitude |
| I7 | Participation MAGNITUDE (`β`, effective `M`) | **OPEN** (D2) | `clm-m5swh9` (deferred to the β lane / this instrument) | imported as a disclosed scan OR held symbolic — Grant D2 |
| I8 | The sector-crossed `c²` that divides `E_trapped` (`c_P` / `c_S` / `c_EM`?) | **OPEN DECISION — surfaced, not picked** (D1) | `clm-m5swh9` (`A1 ⊥ T2`; "which sector's c² … is not automatic") | the plumber-physical question to Grant |
| I9 | Cold uncaged reference `K_0, ρ_0, Z_0` | **LATTICE-MEASURED** | `#782` uncaged arm (`rve-aggregation-bench_prereg-FROZEN.md` §1) | the ratio denominators |
| I10 | Solver numerics (radial grid `Δr`, outer radius `R_max`, ω sampling, sponge/BC) | **ENGINEERING CHOICE — tagged** | this lane (frozen in the prereg, not here) | no physics claim; validation-gated (§5) |

**The I5 honesty core, expanded (the load-bearing tag).** The inertia law `ρ_contribution = E_trapped / c² · (participation)` is imported wholesale — it is E=mc² asserting that trapped elastic/swing energy carries inertia, a law the lossless small-displacement lattice STRUCTURALLY lacks (`β_massload ≡ 0` analytically there; `beta-tracking-feasibility_scoping.md` §3 absence-1). It decomposes into three separately-tagged pieces so no under-determined choice hides inside a single symbol:

- **I6 (direction) — walk-ratified.** That the loading is UPWARD (Reading A, MATCHED direction) is the `clm-hu1jjw` ruling. This is the ONE piece the corpus has closed; it is still pending adversarial review of the KB leaf (PR #787).
- **I7 (magnitude) — OPEN, Grant D2.** `β` / effective `M` is explicitly the OPEN `clm-m5swh9` magnitude, "deferred to that measurement, not decreed." This instrument is that measurement's continuum host — but it can only PROPAGATE a chosen/scanned magnitude, not DERIVE it from first principles (that needs self-bound soliton dynamics, §4).
- **I8 (the c² sector) — OPEN, Grant D1.** `clm-m5swh9` states verbatim that "which sector's `c²` divides `E`" is "not automatic" and invokes the `A1 ⊥ T2` cross-wiring watch. The candidates carry physically different consequences: `c_P` (`0.519`, the compression carrier's own speed) gives the smallest inertia divisor and the largest loading; `c_S` (`0.286`) larger loading still (smaller `c²`); `c_EM` a third value. **This is surfaced for Grant as the pre-test-physics-check plumber-physical question — it is NOT picked here, and no default (e.g. the SM habit of `c_light`) is admissible.**

**What is NOT imported (kept honest).** The cold constitutive moduli (I1, I2, I9) and the vessel-state remap FORM (I3) are lattice/canon, not imported physics. The `r_Z` discriminator FORM and the Lloyd `(k·r_core)²` FORM are DERIVED (effective-medium / acoustic-image theorems). Only I5 (and its I7/I8 open pieces) is a tagged import; the lane's honesty rests on I5 never being silently promoted to derived.

## §4 — WHAT IT CAN AND CANNOT SETTLE

**CAN settle (single-core, quasistatic, GIVEN the import):**

- **C1 — the deep-quasistatic scattering / effective-medium behaviour of a pre-stressed vessel-state cage at PHYSICAL `k·r_core`.** It reaches `k·r_core ≪ π`, the regime the lattice cannot (`deep-rail-kscaling_derivation.md` §2). It measures the SINGLE-CORE exponent `p` in `ρ_N ∝ (k·r_core)^p` and tests the analytic Leg-A form F2 (`p = 2`) that the lattice could neither validate nor refute.
- **C2 — the net acoustic `ρ_eff` SIGN question, both terms present.** GIVEN the I5 import, it evaluates structural added-mass (term i — a soft/pressure-release inclusion trends DOWN, bubble-like) AGAINST trapped-energy loading (term ii — UP per `clm-hu1jjw`), kept separable in the outputs (R-below), so which wins is READ, not assumed. The lattice hosts only term (i).
- **C3 — `r_Z(φ)` with BOTH `Z` factors.** `r_Z = √((K_eff/K_0)·(ρ_eff/ρ_0))` computed with the loaded `ρ_eff` — so the `#782` bare-node `r_Z` values (which the KB leaf flagged become FLOOR values under Reading A, `relative-offset-principle.md` "the `r_Z`-floor consequence") are lifted to their physical position within the straddle band, per the chosen/scanned magnitude (D2).

**CANNOT settle (stated plainly, so the instrument is not over-read):**

- **X1 — it CANNOT derive β from first principles.** That needs self-bound (field-generated, co-moving) soliton dynamics — the same self-lock capability the lattice lacks (`beta-tracking-feasibility_scoping.md` §3 absence-3, §7). The solver PROPAGATES an imported/scanned magnitude (I7/D2); it does not generate it.
- **X2 — it CANNOT adjudicate the import's own truth.** Whether trapped-energy mass IS acoustic inertia (Fork ρ ontology) and which `c²` divides it (I8/D1) are Grant-adjudicated substrate-ontology inputs, not solver outputs. The solver shows the CONSEQUENCES of a given import; it cannot certify the import.
- **X3 — it CANNOT settle the ENSEMBLE aggregation half (the load-bearing scope limit — see the tension note).** A spherically-symmetric single-cage solver "validates the per-core `p` (Step 1) but CANNOT represent inter-core coherent compression, so it does NOT settle aggregation (Step 2)" (`deep-rail-kscaling_derivation.md` §2, verbatim). The ensemble-coherence question (does an uncancelled net monopole emerge between cores?) needs an `N>1` instrument, infeasible on this machine class.

**★Scope-tension resolution (flag-don't-fix — surfaced, not silently reconciled).** The two source docs phrase the radial-solver's remit DIFFERENTLY, and the difference is load-bearing:
- `rve-aggregation-bench_result.md` §8.2-4 routes "the RADIATIVE consequence (**star-scale Lloyd cancellation at `k·R_star`**) … stage-2 radial-solver territory." That phrasing is an ENSEMBLE/aggregation radiative outcome (a whole homogenized star).
- `deep-rail-kscaling_derivation.md` §2 restricts the radial solver to the SINGLE-CORE exponent and EXPLICITLY denies it can settle aggregation (Step 2).

These are reconcilable ONLY by splitting the word "radiative consequence" into two objects: **(α) the single-core quasistatic `p`** — which this solver settles (C1); and **(β) the star-scale boundary problem GIVEN an already-homogenized effective medium** — which this solver can compute as a single-boundary scattering problem IF and ONLY IF the effective medium is supplied from the constitutive bench (a `#782`-class homogenization), i.e. it does NOT DERIVE the aggregation coherence (Step 2) that produces that effective medium. The charter's frozen position: **this lane owns (α) and the GIVEN-medium (β); it does NOT own the aggregation-coherence derivation (Step 2 / `N>1`), which stays infeasible and unrouted here.** If Grant reads `#782` §8.2-4 as demanding the aggregation derivation itself, that is a DIFFERENT (infeasible) instrument and the charter's object (§2) is mis-scoped — surfaced for his adjudication, not reframed by the charter.

## §5 — REQUIREMENTS (derived, numbered)

<!-- SKELETON -->

## §6 — TRADE STUDY (decisions-OPEN, not decided)

<!-- SKELETON -->

---

> **Charter provenance.** <!-- SKELETON -->
