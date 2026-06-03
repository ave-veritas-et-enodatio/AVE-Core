# Prereg: Yield-Knee Map — the Vacuum as a Saturable Reactor (two methods)

**Status:** SCOPING (2026-06-03) — corpus-grep done; **REFRAMED to a tree-level V²-coefficient SIGN test** (the literal knee at V_yield is bench-unreachable; resume from Q-G42). Supersedes `2026-06-03_spinning-chiral-coupling-prereg.md` (closed Outcome B/C).
**Lane:** experimental-protocol revamp — direct characterization of the saturation kernel.
**Origin (Grant 2026-06-03):** characterize the vacuum as a saturable reactor and map its yield knee using standard nonlinear-component characterization (C-V / B-H / DMA). Two methods on the table; a Phase-0 magnitude estimate picks which one reaches a measurable shift.

## Target (precise)
Directly map the AVE saturation kernel ε_eff(V) = ε₀√(1−(V/V_yield)²) — the "yield-knee map" — and discriminate:
- **AVE:** ε_eff softens with a **knee at V_yield**, shape √(1−(V/V_yield)²).
- **QED (Euler–Heisenberg):** a weak smooth polynomial ε(E) correction (∝E²), ~12 OOM weaker, **NO finite-field knee**.
- **Linear EM:** ε independent of field amplitude — **NO shift at all**.
Zeroth-order discriminator is binary (does the vacuum's reactance move with field amplitude?); then the shape (knee vs smooth polynomial).

## Physical picture (EE-native)
The vacuum bond-LC is a **saturable reactor**: drive the local field toward V_yield and ε_eff (∝ C) softens. Same nonlinearity as a varactor (C–V), a saturating core (B–H), a stiffening spring (DMA) — **the component is novel (the vacuum), the method is standard**. The AVE-distinct fingerprint is the **knee at V_yield** (a discrete saturation onset at a specific field), vs QED's smooth polynomial and linear-EM's flat.

## Two methods (both build the knee map; Phase-0 picks)
- **Method A — C–V (DC-bias + small-signal probe; varactor analog).** Strong static field V_DC (geometric concentration toward V_yield) sets the operating point; a small AC test signal reads the vacuum's incremental ε; sweep V_DC → the vacuum C–V, knee at V_yield. Sibling of **IVIM** (IVIM reads *reflectance* at the bias; this reads *small-signal C*).
- **Method B — Autoresonant (AC-drive + PLL; B–H loop-tracer analog).** Put the saturable vacuum in a high-Q resonator; AC-drive amplitude toward V_yield; PLL/autoresonance rides f₀(amplitude) as ε_eff softens. The f₀(V) walk + even-harmonic generation = the kernel; **the resonator Q amplifies a tiny ε change into a measurable f₀ shift** (the main reason to prefer AC).

## Phase-0 magnitude gate (THE decision — do FIRST, derive to canonical source)
From canonical constants (V_yield; E_yield = 1.13×10¹⁷ V/m; the kernel; achievable field-concentration factor G_geom; resonator Q), estimate:
- **Method B:** bulk Δf₀/f₀ at the max reachable local field (where a sub-volume reaches V_yield, diluted by the unsaturated bulk) × Q. Above the noise floor AND the apparatus-material-nonlinearity background?
- **Method A:** small-signal ΔC/C at V_DC near reachable max. Measurable?
Pick the method — or kill both — on this estimate. This is the gate the α + IVIM work taught us to run BEFORE building.

## Discriminating outcomes
- **A (LIVE):** reactance shift vs field amplitude following the √(1−(V/V_yield)²) **knee at V_yield**, separable from apparatus-material nonlinearity → AVE-distinct kernel measurement.
- **B (QED-degenerate):** only a smooth polynomial shift consistent with EH at reachable fields → not AVE-distinct.
- **C (NULL / unreachable):** no measurable shift (field can't reach V_yield in a measurable bulk fraction) → kernel real but bench-unreachable; falls back to IVIM-class reflectance.

## Falsifier / hard systematics
- **Vacuum-vs-apparatus-material (the load-bearing one):** real dielectrics/cavities ALSO soften at high field (electrostriction/Kerr/material-saturation) → they shift f₀/C too. AVE separator = the **knee at a specific V_yield** (discrete onset) vs the material's smooth background; a PLL resolving knee-vs-smooth IS the discrimination. If inseparable → null.
- **V_yield reachability:** E_yield ~10¹⁷ V/m, reached only locally via geometric concentration. If the saturated sub-volume is too small a fraction of the resonator, the bulk shift is unmeasurable (Outcome C).

## Corpus-grep (DISPATCHED 2026-06-03)
Inventory: IVIM; ZENER-04; EE-Bench dielectric plateau; prior C–V / autoresonant / f₀(V) work; even-harmonic; Phase-0 magnitude; vacuum-vs-material separation.

**RESULT (2026-06-03): the corpus already ran most of this Phase-0 (Q-G42), and it REFRAMES the experiment — the literal knee at V_yield is NOT bench-reachable; the reachable AVE-distinct observable is the TREE-LEVEL V² softening coefficient (its SIGN).**

**Reachability (load-bearing — CONTRADICTS the literal knee):** V_yield = 43.65 kV is **per-node** (across ℓ_node = 3.86×10⁻¹³ m), not per-apparatus. A 30 kV / 1 mm cap → E/E_yield ≈ 2.7×10⁻¹⁰ (Regime I). Even β=10³ tip × Q=10⁴ → A ≈ 3.8×10⁻³ (Regime II onset, NOT the knee). The bench reaches the small-A tree-level kernel, not the knee. **`AVE-QED/docs/analysis/2026-05-13_Q-G42_v_yield_apparatus_scaling_prereg.md` IS this Phase-0** — resume from it, don't restart.

**The reframe (Q-G42's recoverable discriminator — and it's *cleaner* than the knee):**
- **AVE:** δε/ε₀ = −A²/2 — the vacuum dielectric **softens** (negative V² coefficient).
- **QED (Euler–Heisenberg):** +α²(E/E_S)² — a tiny **positive** shift, 8.3×10¹² weaker.
- **The SIGN alone discriminates** (AVE softens, QED stiffens) — a robust two-sided binary needing neither the knee nor a magnitude match. Plus the even-**2ω** harmonic (canonical, `parametric-coupling-kernel.md:70-78`).

**Reuse, don't reinvent:** the per-node C–V table (`nonlinear-vacuum-capacitance.md:32`: C_eff/C0 = 1.155/2.294/7.089 at V/V_yield = 0.5/0.9/0.99); PONDER-05's Method-A C–V (27.4% ε-collapse at V_DC/V_yield=0.687, piezo-mediated, `07_universal_saturation_kernel.tex:107`); δC/C = ¼(V/V_yield)² ≈ 4.57% @ 2ω; the 8.3×10¹² ratio (IVIM, verified); the β/G_geom catalog (β∈{30,10³,10⁵}, G_ferro~3000).

**Green-field remaining:** (i) the autoresonant Q-amplified Δf₀/f₀ small-signal number (Ch 15 treats PLL only as a rupture-driver); (ii) the even-2f measurement proposal (corpus emphasizes odd-IM3); (iii) the vacuum-softening-vs-dielectric-electrostriction separation.

**Verdict: SURVIVES — reframed from "knee map" → "tree-level V²-coefficient SIGN test" (does the vacuum soften [AVE] or stiffen [QED] under field).** Both methods (C–V / autoresonant) stay; observable is the V²-coefficient sign + magnitude at small A. **Open decision (Q-G42 §4 Q1–Q3, Grant's call): detection architecture** — precision capacitance bridge (ΔC/C ~10⁻⁹) / cryo-lock-in (10⁻¹²) / resonant-Q autoresonant (10⁻¹⁵).

## Discipline
`ave-prereg` · `substrate-native-check` (the C–V / f₀ framing must be substrate-native, not an SM-imported nonlinear-optics analogy) · `ave-discrimination-check` (linear-EM + QED counterfactuals + the material-nonlinearity systematic) · `ave-canonical-leaf-pull` (kernel, V_yield, dielectric-plateau, IVIM, ZENER-04) · `ave-fundamental-ground-up-implementation` (Phase-0 from canonical, not engineering-default) · `ave-ee-intuition-summary` (the saturable-reactor 5-beat on the deliverable).
