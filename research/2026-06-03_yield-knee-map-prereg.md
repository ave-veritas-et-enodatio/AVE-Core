# Prereg: Yield-Knee Map — the Vacuum as a Saturable Reactor (two methods)

**Status:** SCOPING (2026-06-03). Supersedes `2026-06-03_spinning-chiral-coupling-prereg.md` (closed Outcome B/C). Corpus-grep dispatched.
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
Inventory: IVIM (reflectance kernel-probe, its V_yield-reachability + magnitude); ZENER-04 (avalanche knee, 43.65 kV); EE-Bench dielectric plateau (E_yield=1.13e17); any prior C–V / resonance-shift / autoresonant / f₀(V) kernel measurement; the kernel's even-harmonic signature; any Phase-0 bench-reachable-magnitude estimate; the vacuum-vs-material separation. [PENDING — fills on grep return.]

## Discipline
`ave-prereg` · `substrate-native-check` (the C–V / f₀ framing must be substrate-native, not an SM-imported nonlinear-optics analogy) · `ave-discrimination-check` (linear-EM + QED counterfactuals + the material-nonlinearity systematic) · `ave-canonical-leaf-pull` (kernel, V_yield, dielectric-plateau, IVIM, ZENER-04) · `ave-fundamental-ground-up-implementation` (Phase-0 from canonical, not engineering-default) · `ave-ee-intuition-summary` (the saturable-reactor 5-beat on the deliverable).
