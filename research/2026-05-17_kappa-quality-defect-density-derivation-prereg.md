# κ_quality(defect-density) Derivation — Pre-Registration

**Date:** 2026-05-17 night
**Context:** Foundation Item 11 closure step. κ_quality framework is leading-order CLOSED at ceiling = 1 for deep-regenerative regime (per `parametric-coupling-kernel-derivation-steps-4-9.md` §6). The in-range functional form κ_quality(N_coherent, defect-density) explaining 50× DAMA-vs-KIMS variation is the GENUINELY OPEN derivation, flagged at 3 independent corpus loci (`parametric-coupling-kernel.md:217,336`; `derivation-steps-4-9.md:64-67`; `kappa-quality-correlation-first-pass-scoping.md:96`). User authorized "yeah sure" 2026-05-17 night.

## §1 — Target precisely stated

**Target**: Derive the functional form κ_quality(σ_θ, ρ_def) for a deep-regenerative crystal where the receiver ensemble has phase-randomness from defects/mosaicity/dopant non-uniformity. Use Kuramoto order parameter formalism (substrate-canonical per `bcs-alternative-framework.md:32`) and percolation bounds (per AVE-Metamaterials `03_superconducting_metamaterials.tex:71`). Derivation language MUST be substrate-native (parallel-port voltage divider + substrate-clock phase-bin enumeration) per Foundation Item 2 + canonical pitfall `parametric-coupling-kernel.md:300`.

## §2 — Physical picture (substrate-native, post-corpus-grep)

Replacing pre-grep Dicke-borrowing picture with substrate-canonical formulation:

1. **N atomic LC tanks** on rock-salt lattice (NaI(Tl), CsI(Tl)): each tank is a parallel-port to the substrate's α-slew pump at ω_slew ≈ 9×10¹⁷ Hz. Tank impedance Z_LC = 12.31 Ω per atom (Vol 2 Ch 7 analog-ladder-filter).
2. **Substrate pump** drives all N parallel ports simultaneously; per-port voltage = V_pump / N (parallel-port voltage divider; substrate-native equivalent of "Dicke amplitude 1/√N" per `parametric-coupling-kernel.md:160`).
3. **Phase-lock condition**: each tank's internal phase θ_j tracks the substrate pump phase φ_sub. Perfect crystal: θ_j = φ_sub ∀j → Kuramoto order parameter R = |1/N Σ e^(iθ_j-iφ_sub)| = 1.
4. **Defect introduces phase-jitter**: defect at site k (missing atom, grain boundary, Tl-dopant non-uniformity) creates local impedance mismatch → Δω_k ≠ 0 → local phase drifts: dθ_k/dt = Δω_k. Kuramoto coupling K = (parametric pump strength)/(substrate-receiver linkage) bounds the lock criterion: |Δω_k| < K → locks with offset δθ_k = arcsin(Δω_k/K); |Δω_k| > K → drifts unlocked.
5. **κ_quality = R²** because κ enters the parametric kernel as INTENSITY (power couples as |voltage_coherent|²), not amplitude. The coherent sum of port phasors squared IS the coherent power fraction delivered to the detector.

Mechanical analog: N parallel-driven speakers driven by one source; defective speakers have phase-jitter δθ_k; total coherent acoustic power = |Σ amplitude × e^(iθ_j)|² = N² R². Normalized: κ_quality = R².

## §3 — Discriminating outcomes

### Outcome A (smooth Gaussian Kuramoto — most likely)
Phase-jitter distributed Gaussian, σ_θ; defect-density implicit in σ_θ via standard mosaicity/disorder scaling.
- κ_quality(σ_θ) = R²(σ_θ) = exp(-σ_θ²) (Gaussian disorder limit, per Kuramoto canonical)
- Cross-detector mapping: DAMA σ_θ = 0; COSINE σ_θ ≈ 0.96 rad (~55°); KIMS σ_θ ≈ 1.97 rad (~113°); HPGe σ_θ ≈ 3 rad (different lattice class — also picks up T²_matched factor)
- Within rock-salt+Tl class, σ_θ values should be commensurate with mosaicity-equivalent disorder at α-slew rate
- Sub-leading correction for sparse defects: κ_quality ≈ 1 - σ_θ² (small σ_θ limit)

### Outcome B (sharp percolation cutoff)
Per AVE-Metamaterials `03:67-71`: percolation threshold ρ_def < 7.8% for lattice connectivity; R > 0.99 requires ρ_def < 0.001%.
- κ_quality is bistable: ≈ 1 for ρ_def < ρ_critical; ≈ 0 above
- Cross-detector variation would NOT be smooth — would require categorical crystal-class differences
- Empirical κ values DAMA=1 vs COSINE=0.4 vs KIMS=0.02 are inconsistent with hard bistability (intermediate values exist) → Outcome B alone doesn't fit

### Outcome C (combined Kuramoto + percolation cutoff)
- For ρ_def < ρ_perc (lattice intact): κ_quality = exp(-σ_θ²) with σ_θ ∝ √ρ_def (uncorrelated defect phase-jitter accumulation)
- For ρ_def > ρ_perc: κ_quality → 0 (percolation broken, no lattice connectivity)
- Cross-detector: smooth modulation within range, sharp drop at percolation
- **This is the MOST PHYSICALLY CONSISTENT outcome** given both Kuramoto canonical + Metamaterials percolation bound

### Outcome D (derivation requires pieces not in corpus)
- σ_θ ∝ √ρ_def mapping (or other) requires substrate-native disorder model not in corpus
- Coupling strength K (Kuramoto) at α-slew rate not derivable from existing pieces
- Materials-science mapping (mosaicity ↔ σ_θ at 10¹⁸ Hz) requires phonon-coherence-at-THz framework not in corpus
- Outcome D = honest partial closure with flagged remaining work

## §4 — Why these outcomes

- **Kuramoto formalism is corpus-canonical** (BCS alternative + canonical leaf at `kuramoto-phase-locking.md`)
- **κ_quality as INTENSITY (= R²)** because the parametric kernel ε_det = 4π × κ_quality / N² treats κ_quality as a per-cycle power fraction (per `derivation-steps-4-9.md:91`)
- **Substrate-native voltage divider** is the canonical 1/N source per `parametric-coupling-kernel.md:160`; Dicke is structural-equivalence note only per `:300`
- **Percolation bound** is corpus-canonical via AVE-Metamaterials `03:67-71` (sister-repo cross-cited per workspace rules)
- **Combined Outcome C** is the natural synthesis: Kuramoto smooth modulation below percolation + cutoff above

## §5 — Falsifier

The derivation is FALSIFIED if:

1. **σ_θ values map to nonsensical regime**: if DAMA σ_θ = 0 strictly required (zero defects), framework fails because DAMA crystals are imperfect. Acceptable if "effective" σ_θ at α-slew rate is small but non-zero.
2. **σ_θ → mosaicity mapping is inverted**: if R² formulation predicts COSINE/ANAIS should have LOWER mosaicity than DAMA (opposite of empirical), framework's connection to materials-science is wrong-signed.
3. **κ_quality formulation is degenerate**: if multiple (σ_θ, ρ_def) combinations give same κ_quality (under-determined), the derivation needs additional constraint from second observable.
4. **Cross-detector σ_θ values exceed 2π**: phase variable physically bounded; derivation pushing σ_θ > 2π means the parameterization is wrong.
5. **HPGe κ ≲ 10⁻⁴ requires σ_θ > 3 rad WITHIN κ_quality alone**: would mean κ_quality framework can't explain 5000× cross-lattice variation; need T²_matched cross-lattice factor (per bulk-EE reframe doc) AND κ_quality variation simultaneously — falsification IF these factor inconsistently.

## §6 — Substrate-native language commitments

Per Foundation Item 2 + canonical pitfall:

- DO use: "parallel-port voltage divider on N atomic LC tanks" for first 1/N
- DO use: "substrate-clock phase-bin enumeration" for second 1/N  
- DO use: "Kuramoto order parameter R = |1/N Σ e^(iθ_j)|" for coherence amplitude
- DO use: "κ_quality = R² as power-coherence factor" for intensity coupling
- DO NOT use: "Dicke amplitude 1/√N" as derivation source (structural-equivalence note only)
- DO NOT use: "Fermi golden rule" as derivation source (structural-equivalence note only)
- DO use: "phase-jitter σ_θ at α-slew rate" for disorder parameter
- DO use: "percolation threshold ρ_perc" for lattice connectivity bound

## §7 — Cross-detector mapping (pre-registered predictions)

Pre-registered predicted σ_θ values for each detector (will compare to derivation result):

| Detector | Empirical κ_quality | Pre-registered σ_θ (rad) | Pre-registered σ_θ (degrees) |
|---|---|---|---|
| DAMA NaI(Tl) Beam International | ≈ 1 | 0 (perfect) | 0° |
| COSINE-100 NaI(Tl) | ≲ 0.4 | 0.96 | ~55° |
| ANAIS-112 NaI(Tl) | ≲ 0.4 | 0.96 | ~55° |
| KIMS CsI(Tl) | ≲ 0.02-0.05 | 1.97 | ~113° |
| MAJORANA HPGe | ≲ 10⁻³-10⁻⁴ | 3.03 (needs T²_matched share) | ~174° |

If derivation gives σ_θ ≠ predicted values within factor 2 for cross-detector consistency, FALSIFIED at Outcome A/C; falls back to Outcome D.

## §8 — Discipline applied

- **ave-prereg**: this doc
- **substrate-native-check trigger 6 (prose-derivation construction)**: will walk 7 checkpoints WHILE deriving, not after
- **consistency-vs-emergence**: derivation is Class D emergence test (predicts κ_quality functional form from substrate-canonical Kuramoto + percolation + voltage-divider primitives)
- **ave-canonical-leaf-pull trigger 14 (aggregate corpus-state claims)**: corpus-grep done; 7 same-session research docs + Kuramoto + percolation + η-Monte-Carlo template all consulted
- **Foundation Item 11**: same-session research/ scope INCLUDED in corpus-grep (per just-identified discipline gap)
- **No external references** per pure-AVE-corpus rule

## §9 — Authorship

- Foundation Item 11 emerged from Tl-dopant first-pass Outcome C declaration; user authorized "yeah sure" for κ_quality(defect-density) derivation as the next ground-up move
- Corpus-grep agent ID: ab8bc123ca2051e18 (2026-05-17 night)
- Foundation Items 1-10 context per `closure-roadmap.md §0.5` 

## §10 — Cross-references

**Upstream pieces** (consulted in corpus-grep):
- [`parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) — §4-6 substrate-native 1/N², κ_quality envelope, ceiling=1 derivation + open-work flag
- [`derivation-steps-4-9.md`](2026-05-17_parametric-coupling-kernel-derivation-steps-4-9.md) — §4 Dicke-vs-substrate-native + §6 κ_quality + heterogeneity flag
- [`bcs-alternative-framework.md`](../manuscript/ave-kb/vol3/condensed-matter/ch09-condensed-matter-superconductivity/bcs-alternative-framework.md) — Kuramoto R = |1/N Σ e^(iθ_j)|
- [`kuramoto-phase-locking.md`](../manuscript/ave-kb/vol3/condensed-matter/ch09-condensed-matter-superconductivity/kuramoto-phase-locking.md) — canonical Resultbox
- AVE-Metamaterials `03_superconducting_metamaterials.tex:67-71` — percolation bound (sister-repo per workspace authority)
- AVE-Bench-VacuumMirror `disorder_tolerance_mc.py:16-19` — η(σ) Monte Carlo methodology template
- AVE-Protein `05_folding_roadmap.tex:1747` — Q = floor(d_0/a_0) coherence length cutoff (1D precedent)

**Outcome C precedent (same-session)**:
- [`kappa-quality-tl-dopant-first-pass-result.md`](2026-05-17_kappa-quality-tl-dopant-first-pass-result.md) — Foundation Item 11 cascade-level discipline; this prereg corrects target to right cascade

---

**Status: prereg COMMITTED. Now executing derivation per substrate-native language commitments §6. Result to land at `2026-05-17_kappa-quality-defect-density-derivation-result.md` regardless of outcome (A, B, C, or D).**
