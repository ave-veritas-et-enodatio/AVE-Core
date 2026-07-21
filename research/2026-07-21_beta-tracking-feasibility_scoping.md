# β tracking-ratio feasibility — scoping report (2026-07-21)

**Class: SCOPING (pre-lane). Implementer-lane output, NOT adversarially reviewed; prototype-grade numbers; all criteria herein DRAFT-NOT-FROZEN; mints no `clm-`; banks no verdict.** Engine byte-untouched (isolated worktree off `origin/main` @ `4c92971b`; scratch under `/private/tmp`). Committed post-hoc by the orchestrator as the citation basis for pending-rulings §1 items 10–12 (Grant, verbatim `[sic]`: *"approved the three words from my wue"*).

## 1. The question

Can the lattice engine measure the tracking ratio **β = v_cage-centroid / v_local-material** for a single breather cage under a deep-quasistatic compression carrier — promoting β in `ρ_eff/ρ_0 = 1 + β·φ` (frozen in the RVE prereg, scanned β∈{0,1,3} in the result) from a scanned parameter to a lattice-measured number? Context: the Fork-ρ DIRECTION was closed in-walk (relative-offset principle, `clm-hu1jjw`, PR #787: patterns on the node graph advect with material motion — no sub-graph spatial anchor exists to hold station against it); β pins the MAGNITUDE, including the sector-crossed piece (T2-trapped energy in the A1 carrier's inertia ledger).

## 2. The arithmetic (measured this session, srs-z3 bond model — the actual #775/#782 engine)

- `cP = 0.519`, `cS = 0.286` (cP/cS = 1.813, grade-lock confirmed), `ω_max = 5.568`, `dt = 0.0718` (cfl 0.2).
- Cost: L16 → 33k nodes @ 3 ms/step; L24 → 111k @ 12 ms; L32 → 262k @ 26 ms; L48 → ~885k @ ~90 ms; L100 → ~8M @ ~0.87 s/step. Reflection-free half-box window ≈ `(L/2)/cP` → 214/321/429 steps at L16/24/32.
- Cage resonance at `k·r_core = π` (λ_res ≈ 3.2–4.4 cells at r_core ≈ 1.6–2.2). Sub-resonant `k·r_core = 0.3` needs λ ≈ 33–46 cells.

| Protocol | Reach sub-resonant? | Box | #775 sponge gap? |
|---|---|---|---|
| A. Traveling carrier | fit ≥1 λ≈33–46 + cage + margin | L≳100–150 (hours–days/run) | **inherits fully** |
| B′. Oscillating uniform strain | k=0 exactly | L=24 (~10 min/run) | **evades** (no wave, no sponge) |
| E. Long-λ time-of-flight → ρ_acoustic | k·r_core~O(1), first-arrival | L~32–48 (tens of min) | mild |

Protocol B′ evades the #775 radiative-sponge-vs-wavelength gap cleanly. **That is not the binding constraint.**

## 3. The binding constraint: three structural absences (the deeper gap)

Prototyped the β_track measurement (seed a trapped compression texture in a fixed cage, apply a uniform Galilean material drift V, track the bond-strain PE-density centroid). Across `none/bulk_only/symmetric/rigid` at V = 0.05 and 0.02: PE-centroid velocity ≈ −0.0027 (none/rigid), −0.0071 (bulk_only) — **identical for both V**. A V-independent centroid drift is not advection; it is the seeded blob's own settling asymmetry, and dividing it by V manufactures a spurious β.

1. **No mass-energy equivalence.** Node mass uniform and fixed (velocity-Verlet `v += ½(F+F_new)·dt` with no mass factor ⇒ implicit m=1); trapped elastic energy carries zero inertia → `β_massload ≡ 0` analytically. (The RVE prereg already disclosed: "the cages are stiffness grades, they add NO inertia.")
2. **No advective pattern transport.** Under a uniform material shift `u → u + Δ`, bond strains `du = u_j − u_i` are invariant (`max|Δdu| = 5.6e-17`). The trapped pattern is anchored to the fixed reference nodes — a **formulation artifact** of the small-displacement / linearized-Lagrangian model, not physics. `β_track ≡ 0` structurally.
3. **The imposed grade IS the answer.** `cage_stiffness(...)` depends on `centers, r_cage, cage_w`, never on the field `u`. A fixed (Eulerian) grade forces β_track=0; a by-fiat co-moved grade forces β_track=1. Deriving β needs a *self-bound* (field-generated, co-moving) soliton — the self-lock capability infeasible on the lossless engine.

**Regime discipline:** the small-displacement lattice is a regime where the effect *cannot exist* — any lattice β null is an **ARTIFACT, not a falsification** of the relative-offset direction ruling. (This also supplies the candidate reconciliation for the June "does not advect / TRANSPORT-ABSENT" readings — they measured this same formulation anchor; adjudication routed to the #787 review, not resolved here.)

## 4. The sign flag (load-bearing for Fork ρ)

The ρ in `Z = √(Kρ)` is the **acoustic effective density**, which carries two competing terms: (i) the **structural** added-mass of a soft inclusion — for pressure-release cavities this trends **DOWN** (bubble-like); (ii) the **trapped-energy loading** — **UP** per `clm-hu1jjw`, magnitude open. A soft cage can make the composite acoustically lighter even while its trapped energy makes it heavier. The net sign is measurable (term i) + derivable-with-import (term ii), not walkable.

## 5. Ranked protocols

1. **Protocol E — ρ_acoustic-eff (FEASIBLE-WITH-COMPROMISE).** L~32–48 long-λ compression pulse time-of-flight, `ρ_eff = K_eff/c_eff²`; tens of minutes; reuses #782 K_eff. Measures the **structural** term only (the engine hosts no trapped-energy inertia). → **APPROVED to fold into the anisotropic vessel-state RVE prereg (pending-rulings item 10)** so r_Z is measured, not assumed.
2. **Protocol B′ — uniform-strain lock-in (feasible to run, epistemically empty for β).** Worth running only as a negative control to bank the anchor artifact explicitly.
3. **Protocol A — traveling carrier (INFEASIBLE).** Inherits #775 in full.

## 6. Draft criteria (DRAFT-NOT-FROZEN — for the eventual prereg author)

- Estimator: `β_track = (PE-density-centroid velocity)/(local material velocity)`; PE-centroid = `Σ_bond (½ du·Φ·du)·x_mid / Σ PE`; linear fit over a reflection-free window.
- Mandatory admissibility gates: (i) **V-independence check** — the centroid velocity must scale with drive amplitude, else artifact (the prototype FAILS this, as expected); (ii) boundary exclusion + window `t_end ≤ 0.9·(L/2−r_meas)/cP`; (iii) resonance control `k·r_core ≤ 0.3` or explicit non-resonant demonstration; (iv) grade-frame disclosure (Eulerian vs co-moving — it sets the answer); (v) cage-vs-none differential above the settling-noise floor.
- Guard: any β read where gate (i) fails ⇒ artifact, not a value.

## 7. Bottom line + routing (now Grant-ruled)

**INFEASIBLE-ON-LATTICE** for the mass-loading β and for a clean β_track — root cause one level deeper than #775's regime gap: no self-binding on the lossless engine → the cage is imposed, not field-generated. Routing per pending-rulings items 10–12 (Grant-approved 2026-07-21):

- **Item 10:** Protocol E → the anisotropic vessel-state RVE prereg (measure ρ_eff alongside K_eff).
- **Item 11:** β-proper → the continuum radial-solver lane, trapped-energy inertia as an explicit tagged **E=mc² IMPORT** scoped by `clm-hu1jjw`; charter drafted for Grant review before build. (Minimum engine change that would make advection representable at all: a finite-deformation / updated-Lagrangian reformulation — a major capability, not a near-term driver.)
- **Item 12:** `leg4_moving_cage` quarantine — see §8.

## 8. Addendum: the leg4 sweep verdict (2026-07-21, corpus-grep lane)

Two-method sweep (working-tree `grep -rFn` + `git grep -Fn origin/main`, identical hit sets): `carry_fraction`/`energy_centroid_displacement` are **LOAD-BEARING-NOWHERE** — every prose citation is descriptive/consistency-class; the #770 verdict banks (original and re-banked) rest on Legs 3/5/6; #775 (Legs W/K/C1/S) and #782 (its own Legs 0–5; `leg4_moving_cage` not imported) never touch them. **One latent clause flagged:** the #770 frozen prereg's Fork-C rule names Leg-4 **far-field** (`f_long`, NOT the artifact-flagged outputs) as co-decider — never exercised (Fork C unadjudicated; banked state = REOPENED on Legs 3/5/6). The quarantine is therefore **scoped to `carry_fraction`/`energy_centroid_displacement` only**; the far-field outputs are untouched and the latent Fork-C clause stays live as frozen.
