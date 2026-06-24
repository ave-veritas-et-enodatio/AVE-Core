# Coupled A1+winding EIGENSOLVE — does a confined electron eigenmode (mass+charge) exist, and where does it sit in the V_yield/V_snap/m_e ladder

**Status:** **FROZEN PRE-REG.** Frozen pre-run; SHA-pin before the run.
**Date:** 2026-06-24
**Epic:** full-engine re-route — the **conservative existence** keystone (the clean step S3 left untested).
**Class:** CONSISTENCY (existence + ladder clarification). NOT the α-free chord (that is the bench). Q=137 stays EMPTY. mass=A1 (PR#260) UNTOUCHED.
**Branch base:** `analysis/engine-s3-cavity-pinning` (stacks on S3 #411 — reuses its coupled operator; rebase onto main when #411 merges).
**Why this, why now (Grant 2026-06-24):** "an engine that works, where we both understand how V_yield and V_snap actually relate to m_e." S3 falsified the winding+coupling as a *dynamical* pin; fork-b showed an A1-ONLY confined eigenmode EXISTS; **nobody has eigensolved the COUPLED A1+winding object.** This is the conservative existence question (an eigenvalue problem, NOT dynamical self-formation — so it does NOT refill the twice-falsified self-formation slot, A47 v11b), and reading the bound mode's operating point off it is how the voltage ladder becomes physical instead of asserted.

## §0 SCOPE-LOCK

- **Conservative EXISTENCE, not formation.** We eigensolve the (Hermitian) coupled generator and ask whether a confined stationary bound mode EXISTS. We do NOT seed a blob and evolve (that is Stage-2/S3, twice-falsified). Re-posing time-domain self-trap is BARRED (substitution-not-retraction).
- **Anti-rebuild (Rule 14):** reuse `coupled_cage_winding._assemble_H()` (the S3 coupled Hermitian H: native K4 A1-block + ω-block + `S(A)`-front-gated on-site coupling) and the fork-b confinement gate (`fork_b_saturation_tank`: core_frac, gapped/discrete, `Im(ω)` sign, ARM-B scramble control). fork-b did A1-ALONE; this extends it to the COUPLED object.
- **α-clean:** the chord-deciding reads route through the `_winding_host` guard (κ̃=6/5); no ALPHA/KAPPA_CHIRAL/Q_TANK on the verdict path. V_snap/V_yield enter only as the declared operating-point calibration (see §3), not on any chord-deciding read.

## §1 MAKE-OR-BREAK (pre-stated)

Eigensolve the coupled Hermitian generator `H` (A1 mass-block + ω winding-block + `S(A)`-front-gated coupling, on the native TETRA stencil, at the saturated operating point). **PASS (exists)** iff there is a bound eigenstate that simultaneously:
- **(a) CONFINED** — core-localized, `core_frac ≥ 0.50` (the fork-b GATE1 bar);
- **(b) GAPPED + DISCRETE** — separated from the continuum (a genuine bound state, not a band member);
- **(c) LOSSLESS** — `Im(ω) ≈ 0` (closed reactive cage; not a leaky/decaying mode);
- **(d) BOTH SECTORS PRESENT** — the eigenstate carries nonzero A1 mass-amplitude **AND** the (2,3) winding-charge (read off the winding-host quadrature-invariant). A confined mode that is A1-only, or whose winding has bled into the A1 scalar, does NOT count (genesis-24 guard);
- **(e) NON-TAUTOLOGICAL** — the ARM-B scramble control (destroy the saturation structure) must DE-CONFINE the mode (fork-b precedent ~94%), proving confinement is S-structure-decided, not a projector artifact.

**BREAK (does not exist):** no eigenstate satisfies (a)-(e) — i.e. the conservative coupling **de-stabilizes** the confined A1 mode that exists alone (fork-b). That would be a deeper negative (the coupled electron has no confined stationary state), reported honestly, retract-not-refill.

**INCONCLUSIVE** (Rule 11) if the eigensolve cannot resolve the mode (e.g. lattice resolution too coarse for the (2,3) winding) — report, do not rescue.

## §2 VALIDATE-ON-KNOWN

- **fork-b A1-only confined eigenmode** (`research/2026-06-20_fork-b-saturation-tank-confinement_result.md`, GATE1 PASS, core_frac=1.0, lossless, ARM-B de-confines ~94%): the coupled eigensolve MUST recover the fork-b A1 mode in the winding-OFF / decoupled limit (`winding_on=False` ⇒ Ω≡0). If it does not reproduce fork-b's confined A1 mode with coupling off, the instrument is broken (HALT).
- **S3 coupled operator** (`coupled_cage_winding._assemble_H()`): the SAME Hermitian generator S3 evolved — here we eigensolve it instead of time-stepping it. The eigensolve and the S3 dynamics must be consistent (the dispersing S3 blob = a superposition dominated by continuum/radiating modes, NOT the bound eigenstate; this eigensolve asks whether the bound eigenstate is in the spectrum at all).

## §3 THE V_yield / V_snap / m_e LADDER CLARIFICATION (the deliverable Grant asked for)

Read off the bound eigenmode and report, with the FORM-vs-CALIBRATION split explicit:

1. **Operating amplitude A\*** — the strain `A = V/V_yield` at which the mode actually binds (its core amplitude). This is a **FORM** result (dimensionless, substrate-set) — *where in the ladder the electron lives.* Report it; if it lands on a recognizable number (√α, ½, ¾=R_II, 1) apply the coincidence-magnet discipline (do NOT headline a suggestive value as a chord without the form-before-calibration test).
2. **Dimensionless eigenfrequency ω_bound** — the mode's gap/clock (FORM). Note whether it relates to the Compton/mass-gap structure.
3. **The honest ladder map:**
   - `V_snap ≡ m_e c²/e` — **DEFINITIONAL calibration** (the rest-mass-energy as a voltage; `constants.py:451`). This IS m_e in voltage units, not derived.
   - `V_yield ≡ √α·V_snap` — the onset of nonlinearity; the √α is the **imported echo** (`constants.py:460`).
   - **the eigenmode binds at A\*** — **FORM** (substrate-set).
   So "how V_yield and V_snap relate to m_e" = the dimensionful values ARE m_e (+α) by calibration; what the eigensolve adds is the **physical place of the electron in that ladder** (A\*, ω_bound) — the ladder becomes a picture you can read, not two asserted voltages.
4. **Two-camps reconciliation** — the corpus has carried two readings (Γ=−1 forms at V_yield [electron-identification.md:26] vs at V_snap [pair-production §4]). Resolve it with the actual A\*: does the bound mode live at the V_yield floor (onset) or near the V_snap cap (A→1)? Report which, as the empirical resolution (not assertion).
5. **Scale-free check** — sweep lattice size L (fork-b's scale proxy): if ω_bound diverges/floats with L (fork-b precedent), the dimensionful values are confirmed m_e-calibration (the FORM = the mode + A\*; the SCALE = the irreducible m_e). This is the EXPECTED outcome (do not over-frame a scale-free result as failure — it's the honest "m_e is the one input").

## §4 TRAPS + GUARDS

- **Self-formation refill** — this is an eigenvalue EXISTENCE problem, NOT a dynamical formation run; do not time-evolve a seed and call it existence (that's the twice-falsified slot). GUARD: report eigenpairs, not trajectories.
- **Tautological confinement** — a projector/seed could fake a bound mode. GUARD: the ARM-B scramble must de-confine (gate e).
- **Winding-bled-into-A1** — the "coupled" mode could be A1-only with the winding collapsed. GUARD: gate (d) requires nonzero winding-host quadrature-invariant in the eigenstate, separate from the A1 amplitude.
- **m_e-circularity / derivation over-claim** — do NOT claim the eigensolve "derives" m_e, V_snap, or V_yield (they are calibration inputs). GUARD: §3 form-vs-calibration split; the chord-decider stays the α-free dimensionless ratio (and that's the bench, not here).
- **Scale-free mis-read** — a scale-free ω_bound is the EXPECTED honest closure (m_e irreducible), NOT a failure. GUARD: §3.5 framing.
- **Resolution** — the (2,3) winding needs ≥~3-4 cells/turn; verify the eigenmode is Nyquist-resolved (fork-b auditor arithmetic), or run finer / report INCONCLUSIVE.

## §5 BUILDABILITY

**BUILDABLE-NOW.** Reuse `coupled_cage_winding._assemble_H()` (the coupled Hermitian H) + `fork_b_saturation_tank`'s confinement gate (core_frac/gapped/Im(ω)/ARM-B). Genuinely new = (i) eigensolve the COUPLED H (fork-b did A1-only); (ii) the both-sectors-present gate (d) on the eigenstate; (iii) the §3 ladder-clarification readout. Cheap (an eigenvalue problem, not a long PDE run).

## §6 REPRODUCE / GATE PLAN

1. **HALT GATE — winding-OFF recovers fork-b:** with `winding_on=False`, eigensolve recovers the fork-b confined A1 mode (core_frac≥0.50, lossless). FAIL → broken instrument, HALT.
2. **PRIMARY:** eigensolve the coupled H (winding ON); find the bound cluster; test gates (a)-(e). Verdict EXISTS / DOES-NOT-EXIST / INCONCLUSIVE.
3. **LADDER:** read A\*, ω_bound; produce the §3 form-vs-calibration map + the two-camps resolution.
4. **SCALE-FREE:** sweep L; report ω_bound(L) trend (expected: scale-free → m_e irreducible).
5. **OUTPUT:** result doc with the existence verdict, the bound eigenmode (core_frac, ω_bound, both-sectors), the ladder clarification, and the scale-free finding. Branch-only; NEVER self-merge.

## §7 CONSISTENCY-vs-EMERGENCE

CONSISTENCY-class. PASS = the electron exists as a confined coupled eigenmode (existence keystone, now for the full mass+charge object) + the ladder is made physical. It does NOT emit the α-free chord (the bench does) and does NOT derive m_e (the scale is the irreducible input, expected scale-free). A clean DOES-NOT-EXIST is a legitimate deeper negative.
