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

<!-- SKELETON -->

## §2 — OBJECT (what the instrument is)

<!-- SKELETON -->

## §3 — IMPORT LEDGER (the honesty core: every input tagged)

<!-- SKELETON -->

## §4 — WHAT IT CAN AND CANNOT SETTLE

<!-- SKELETON -->

## §5 — REQUIREMENTS (derived, numbered)

<!-- SKELETON -->

## §6 — TRADE STUDY (decisions-OPEN, not decided)

<!-- SKELETON -->

---

> **Charter provenance.** <!-- SKELETON -->
