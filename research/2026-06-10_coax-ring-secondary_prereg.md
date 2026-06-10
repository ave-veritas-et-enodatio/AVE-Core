# PREREG (FROZEN) — Coax-ring secondary route to α: the cavitation floor + the saturation wall as a coaxial cavity

**Date:** 2026-06-10
**Branch:** `analysis/2026-06-10-coax-ring-secondary` (worktree off `analysis/2026-06-10-sonic-horizon-closure`; inherits the cavitation + sonic-horizon engines and the formed-pocket machinery). Not pushed/merged.
**Lane:** implementer. **This prereg is committed ALONE, before any run artifact** (process gate).
**Licensed entry:** the §5 gate of the 2026-06-04 α-¼ closure ([`research/2026-06-04_alpha-quarter-adversarial-rechallenge.md`](2026-06-04_alpha-quarter-adversarial-rechallenge.md) §5): "Over-determination would be evidence *only* if a route made a **discriminating secondary prediction** the others don't, **and the substrate confirmed THAT**." This run names that discriminating secondary BEFORE deriving, and frames the work as a **SECOND ROUTE to already-derived quantities** (the (2,3) selection at [`torus-knot-uniqueness.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md); the ch8 α chain at [`ch8-alpha-golden-torus.md`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md)) — convergence, NOT gap-fill.

**Grant directive (verbatim, the discriminating secondary, recorded BEFORE deriving):**
> "can we link it to collimated flux tube diameter? or local saturation? might be how L and C change together in scale but not relative magnitude?"

**Skills fired:** `substrate-native-check` (CP phase-space-vs-real-space + CP9 dynamical + CP10 boundary-not-bulk, walked below §2.4), `ave-prereg` (this doc; Step-3.5 dimensional subsection §6), `ave-apparatus-floor-attribution` (governs every engine number; Arm-3 §5.3 + the A_cap clip in Arm-1/2), `ave-canonical-source` (numeric checks import `ave.core.constants` only), `ave-driver-script-honesty` (forward, no target in any loop), `ave-conserved-vs-pumped` (the (2,3) winding / circulation is energize+lock; the slosh is the C↔L exchange, never a pump), `ave-representation-capability-check` (the slosh observable must read the RIGHT DOF pair: bulk-V "u" ↔ Cosserat-ω; the real-space radius ratio is NEVER the phase-space (2,3) winding nor the phasor φ²), `verify-before-cite` (every file:line grep-confirmed this session; unpushed content cited by branch+commit), `ave-live-fire-derivation-provenance` (forward bins; any step chosen to land on a target = FITTED, said so), `consistency-vs-emergence` (every arm class-tagged).

---

## §0 — THE COAX-RING HYPOTHESIS (the thing under test, stated forward)

**Plumber-physical statement.** The electron's flux-tube wall is a **coaxial cavity**. Its two walls are the two α-FREE reflecting (`Γ→−1`) loci that the inherited engines already exhibit:

- **inner conductor radius `a` = the cavitation locus** — the `c_bulk² = 0` root of the candidate Propulsion EOS `c_eff²(ρ̄) = c₀²(1 + ρ̄/(1−ρ̄²))`, at `ρ̄ = ρ̄_cav = (1−√5)/2 = −1/φ ≈ −0.618` (**CANDIDATE-CLAIM**: AVE-Propulsion `vol_propulsion/chapters/04_superluminal_transit.tex:86,89`; zero KB / `constants.py` hits — kept candidate throughout). At this locus the bulk impedance `Z_bulk = ρ·c_bulk → 0`, so `Γ_bulk = (Z−Z₀)/(Z+Z₀) → −1`: a pressure-release sonic horizon (`research/2026-06-10_sonic-horizon-closure_result.md` §7, verdict LOCK — horizon FORMS cleanly).
- **outer conductor radius `b` = the rupture / full-saturation locus `A → 1`** — where the Axiom-4 saturation kernel `S(A) = √(1 − (A/A_yield)²) → 0` (equivalently `S(ρ̄) = √(1−ρ̄²) → 0`, the EM/dielectric specialization). This is the `Γ=−1` saturation wall the mass breather generates by over-saturating the medium (`crystal_graft_v2_result.md` §4: "the asymptote to −1 is the rupture boundary A→1"). It is the **regime boundary `R_III = 1.0` (Saturated → Rupture)** in `constants.py:425`. **α-FREE by construction.**

**The coax claim.** Between these two `Γ=−1` mirrors a trapped mode rings. Its characteristic impedance has the coaxial form `Z ∝ ln(b/a)` (or the K4-TLM substrate-native equivalent, derived in Arm 1, not imported blind). As scale changes, `L` and `C` both change (so `ω = 1/√(LC)` shifts) **but `Z = √(L/C) ∝ ln(b/a)` stays fixed** — Grant's "how L and C change together in scale but not relative magnitude." The scale-free ratio `b/a` (a **real-space** radius ratio) would be a SECOND route to the electron's already-derived geometry / α.

**The circularity trap (binding, per the licensed-entry constraints).** The outer BC MUST be α-FREE: the rupture locus `A→1` / full saturation. We **explicitly REJECT** `√(2α)` onset and `√α·V_SNAP` yield as outer BCs — they smuggle α into the ratio that is supposed to predict α. A dead-input test (Arm 1 §2.3, Arm 2) shows the derived ratio does NOT secretly depend on any α-laden input.

**The coordinate firewall (binding).** `R, r` of the Golden Torus (`R_GOLDEN_TORUS = φ/2`, `R_GOLDEN_TORUS_MINOR = (φ−1)/2`; ratio `φ² ≈ 2.618`) are **PHASOR semi-axes** (`ch8-alpha-golden-torus.md` §"Substrate derivation"; `28_two_node_electron_synthesis.md` §4). The **real-space envelope ratio `≈ 2.27`** is a DIFFERENT canonical quantity — the **TLM real-space `R_real/r_real ≈ 2.27` attractor**, convergent across N=48, 96, canonical at [`research/_archive/L3_electron_soliton/28_two_node_electron_synthesis.md`](../research/_archive/L3_electron_soliton/28_two_node_electron_synthesis.md) §5.3 + §4.2 ("Real-space `R_real/r_real ≈ 2.27` is a DIFFERENT QUANTITY from phase-space `R_phase/r_phase = φ²`"). **All real-space radius ratios in this work (`b/a`, `R/r`) compare to the real-space canon `≈ 2.27`, NEVER to `φ²`.**

---

## §1 — WHAT THE CORPUS ALREADY HAS (corpus-grep, ave-prereg)

- **α already derived** (ch8): `α⁻¹_ideal = Λ_vol + Λ_surf + Λ_line = 4π³ + π² + π ≈ 137.0363038` (`ALPHA_COLD_INV`, `constants.py:204`), Class-B substrate-mechanism manifestation via the Golden-Torus `(R·r = ¼)` geometry. The ¼-selection is **CHALLENGE-CLOSED Class B** (2026-06-04). This work does NOT reopen ¼-selection; it tests a *different* (real-space coax) construction.
- **(2,3) already derived** (`torus-knot-uniqueness.md`): smallest non-trivial coprime torus knot, forced. This work does NOT re-derive (2,3); it uses the *validated* (2,3) carrier (graft-v2) as the Arm-3 measurement substrate.
- **The FBD radial balance already attempted** (`analysis/2026-06-10-electron-manufacturing-flow`, `research/2026-06-10_electron-manufacturing-process-flow.md` §4 + `src/scripts/vol_1_foundations/electron_mfg_rr_balance.py`): the forward `ln(R/r) = G(ρ̄_wall) − G(ρ̄_cav)`, `G(ρ̄) = −¼ln(1−ρ̄) + (5/4)ln(1+ρ̄) + ½/(1+ρ̄)`, returned **UNDERDETERMINED** — one constraint short, because the outer BC `ρ̄_wall` was free. **This work's new input (Arm 2): fix the outer BC at the α-free A→1 locus** (Grant's "local saturation"), supplied where the mfg-flow doc left it open.
- **The two engines inherited** (this branch): `CavitationFlow2D` / `SonicHorizonFlow2D` (the `c²=0` sonic horizon = inner mirror) and — to be grafted in for Arm 3 — `CrystalGraftV2` (the validated own-ω-field carrier, `analysis/2026-06-09-crystal-graft-v2`; SMOKE-3 reads back a planted (2,3) at rel (0.80, 0.59)).

**Fenced material — DO NOT re-run** (closed-negative, absorbs α): mirror-vs-ring `(½)²` bookkeeping; real-space face counting; phasor↔real-space area bijection. None of the three arms touches these.

---

## §2 — THE THREE ARMS + FROZEN BINS

### Arm 1 — the forward coax derivation (paper-math + numeric check)
Derive the trapped-mode radial profile `ρ̄(r)` from the canonical kernel (the EOS + the v=c₀ scale-free closure of the radial balance — NOT assumed). Locate `a` (the `c²=0` root) and `b` (the `A→1` rupture locus) ON THAT profile. Derive the coax / slosh form `Z ∝ ln(b/a)` substrate-natively (the K4-TLM line; not the textbook coax form imported blind). State forward what `b/a` and the implied `Z`/slosh fraction ARE; compare to the canonical α chain AND the 2.27 real-space envelope. Dead-input test (§2.3).

**Frozen bins:**
- **RATIO-DERIVED** — `b/a` emerges α-FREE from the two floors; the implied `Z`/slosh fraction is stated forward and compared to the canonical α chain. (Sub-record: whether the derived ratio is FINITE-and-meaningful or DIVERGENT/apparatus-clip-limited — reported honestly, not as a separate bin.)
- **α-LADEN** — circularity found; name the α-bearing input that leaked into `b/a`.
- **UNDERDETERMINED** — `b/a` not fixed by the two floors alone (a third input needed).

### Arm 2 — the FBD re-closure with the A→1 outer BC
Re-run the mfg-flow radial balance (`electron_mfg_rr_balance.py`, the `G(ρ̄)` integral) with the outer BC fixed at the **A→1 locus** (U5's named input — Grant's "local saturation"). Compare `R/r` to the **real-space envelope canon `≈ 2.27`** (`28_..._synthesis.md` §5.3) — NOT φ². Report residual + bin.

**Frozen bins:**
- **CLOSES** — `R/r` with outer BC = A→1 matches the real-space canon `≈ 2.27` within stated tol (tol frozen here: **±10%**, i.e. `R/r ∈ [2.04, 2.50]`).
- **DIFFERENT** — `R/r` is well-defined but ≠ 2.27 (state the value; includes the divergent case).
- **STILL-UNDERDETERMINED** — the A→1 BC does not by itself fix `R/r` (a velocity-profile law still free).

### Arm 3 — the scale-invariance smoke (the genuinely discriminating in-engine test)
In `CrystalGraftV2` (own-ω-field, the validated carrier), plant the validated (2,3) configuration (the SMOKE-3 known-seed, `seed_omega_known_2_3`) at ≥3 scales — vary minor radius above the r≥3-cell extractor floor (**r = 4, 6, 8** at matched N margins). Per cycle measure: **(i)** the `u↔ω` (bulk-V `E_V` ↔ Cosserat-ω `E_ω`) energy-exchange fraction (the slosh — defined cleanly from the existing `stencil_energy()` ledger, instrument floor calibrated on a known case first); **(ii)** the mode frequency `ω`.

**Prediction under the coax reading:** the exchange fraction is **INVARIANT** (ratio-set, `Z=√(L/C)` fixed) while `ω` scales with size (`ω ∝ 1/√(LC)`, product-set, expected `∝ 1/r` in lattice units). The torus-knot-only reading predicts NO constraint on the fraction.

**Frozen bins:**
- **SCALE-FREE** — the `u↔ω` exchange fraction is invariant across ≥3 scale settings (within the ledger floor, §5.3) WHILE `ω` shifts as LC predicts (monotone `↓` with size).
- **SCALE-DEPENDENT** — the exchange fraction tracks scale (varies beyond the ledger floor).
- **UNRESOLVED** — the exchange-fraction read does not clear its own instrument floor / the extractor cannot resolve (2,3) at the tested scales.

**Apparatus gates (Arm 3, ave-apparatus-floor-attribution):** the extractor floor (known-null + known-positive + free-drift at EACH scale; the de-novo poloidal-r≈1.1 floor is avoided by construction at r=4,6,8); the ledger floor (the ±6.5%-class free-evolution `H_total` drift, measured for THIS config); a grid-resolution sweep on ONE scale point.

---

### §2.4 — substrate-native-check walk (CP applied to the physics, before code)
- **CP phase-space-vs-real-space:** `b/a` and `R/r` are **REAL-SPACE radius ratios** → compared to the 2.27 real-space canon, never to the φ² phasor ratio. The (2,3) winding is **phase-space** (read by `extract_2_3_omega` in the ω Clifford torus). The Arm-3 slosh is a REAL-energy ledger (`E_V`, `E_ω`). The three coordinate systems are kept disjoint throughout (representation-capability-check).
- **CP9 (dynamical-not-heuristic):** the ω field is dynamically evolved (its own wave eq `∂²_tω = c_ω²∇²ω − ω_0²ω + f_ω`); `E_V`/`E_ω` come from `stencil_energy()` (the discrete conserved ledger), not a closed-form formula.
- **CP10 (boundary-not-bulk):** the `Γ=−1` wall is a frozen-window BC (`freeze_wall_window()`), Op17-bounded — never a bulk force (the genesis-24 detonation was exactly the bulk-force leak; the buckle is `H_couple`, bilinear/conservative).
- **CP8 (hosting):** Arm 3 PLANTS the validated known (2,3) and measures a PROPERTY (the slosh) of that given config — it is NOT an emergence test, so the "seed-the-precursor" discipline does not apply; the known-seed IS the calibrated measurement substrate (apparatus known-positive).
- **conserved-vs-pumped:** the (2,3) winding / circulation is a conserved topological invariant — energize+LOCK, never pumped. The slosh is the `E_V↔E_ω` exchange at fixed |invariant|; it is NOT an accumulation channel.

---

## §6 — STEP-3.5 DIMENSIONAL ANALYSIS (canonical primitives only)

All canonical values verbatim from `src/ave/core/constants.py` (cited file:line); no round-number estimates.

**Primitives:**
- `PHI = (1+√5)/2 = 1.6180339887` (`constants.py:199`) ⇒ `ρ̄_cav = −1/φ = −0.6180339887` (the EOS `c²=0` root; DERIVED in-script, not asserted).
- `R_III = 1.0` (`constants.py:425`, "Saturated → Rupture") ⇒ the A→1 outer BC: `ρ̄_wall → +1` (full-compression saturation `S(ρ̄)=√(1−ρ̄²)→0`). **α-free.**
- `R_GOLDEN_TORUS / R_GOLDEN_TORUS_MINOR = (φ/2)/((φ−1)/2) = φ² = 2.6180339887` (`constants.py:200–201`) — **PHASE-space** comparison-DISTINCT (NOT the target).
- real-space canon `R_real/r_real ≈ 2.27` (`28_..._synthesis.md` §5.3) — the Arm-2 comparison target.
- `ALPHA_COLD_INV = 4π³+π²+π = 137.0363038` (`constants.py:204`) — the Arm-1 α-chain comparison target.

**Dimensionless combinations evaluated at canonical primitives:**
- The radial-balance antiderivative `G(ρ̄) = −¼ln(1−ρ̄) + (5/4)ln(1+ρ̄) + ½/(1+ρ̄)`. Evaluated:
  - `G(ρ̄_cav = −0.618034) = −0.0143`
  - `G(+1/φ = 0.618034) = 1.1511` ⇒ `R/r = e^{1.1654} = 3.21`
  - `G(+1/φ² = 0.381966) = 0.8865` ⇒ `R/r = e^{0.9008} = 2.46`
  - `G(+0.5) = 1.0135` ⇒ `R/r = e^{1.0278} = 2.79`
  - **`G(ρ̄_wall → +1)` DIVERGES** (the `−¼ln(1−ρ̄)` term → +∞), so **`ln(R/r) → +∞`, `R/r → ∞`**. The medium stiffens to `c²→∞` at full compression; the v=c₀ rigid lock cannot reach the A→1 wall at finite radius.
- **Pre-registered Arm-1/Arm-2 magnitude expectation:** with the literal α-free A→1 outer BC (`ρ̄_wall → 1`), `R/r = b/a` **DIVERGES**. Regularized at a clip `A_cap` it is large and **grows with `A_cap`** (`A_cap=0.99 ⇒ R/r ≈ 9.7`; `A_cap=0.999 ⇒` larger) — i.e. it **tracks the regularization knob** (apparatus, per ave-apparatus-floor-attribution). Forward expectation therefore: **Arm 2 = DIFFERENT** (divergent / clip-tracking, NOT 2.27); the value `R/r = 2.27` would require `ρ̄_wall ≈ 0.30` (a NON-canonical wall) ⇒ that would be a FIT, not the A→1 derivation. **This is the honest pre-registered expectation; the run will confirm or refute it (Rule 11 — not debugged toward 2.27).**
- **Arm-3 magnitude expectation:** `ω` is the slosh oscillation rate. In lattice units the LC tank's `ω = 1/√(LC)` with `L, C ∝ size` ⇒ `ω ∝ 1/r` (monotone `↓` with minor radius r=4→6→8, ratio ≈ 4:6:8 inverse ≈ 1 : 0.67 : 0.50). The exchange fraction `f_exch = ΔE_ω/(E_V+E_ω)` is dimensionless and (coax prediction) **scale-invariant** within the ledger floor.

**Sanity-check vs empirical anchor:** the mfg-flow §4.2 already ran this `G` integral live and confirmed `R/r(1/φ²)=2.46`, `R/r(0.5)=2.79`, and the φ²-forcing wall `ρ̄_wall≈0.440` — my G-evaluations above reproduce those, so the antiderivative is the same validated one. The divergence at `ρ̄_wall→1` is consistent with the mfg-flow §3.2 figure ("R/r as a continuous curve vs ρ̄_wall", crossing φ² only at the non-canonical 0.440 and rising without bound toward the wall).

---

## §7 — SYNTHESIS MAP (frozen; how the bins combine, Step 5)

- **Arm-3 SCALE-FREE ∧ Arm-1 RATIO-DERIVED** → the slosh lane EARNS its §5 license (the phasor-native quantization derivation may then be *designed* — NOT run here; next-step note only).
- **Arm-3 SCALE-DEPENDENT** → the coax reading DIES honestly (the scale-free `Z=√(L/C)` invariant Grant's secondary requires is absent).
- **Mixed** → localize (state which arm carries the negative and why).

The α-chain and the 2.27 envelope are **comparison targets imported COMPARISON-ONLY**; neither enters any forward loop. Any step chosen to land on a target is FITTED and will be said so (ave-live-fire-derivation-provenance).
