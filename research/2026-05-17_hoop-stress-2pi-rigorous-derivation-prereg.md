# Cross-Volume Hoop Stress 2π Substrate Motif — Rigorous Derivation Pre-Registration

**Status:** PREREG + INITIAL DERIVATION 2026-05-17 night (Tier-3 #10 to cycle-12 thread). First-session goal: prereg with full 6-skill discipline stack + Steps 1-2 of derivation chain (continuum-mechanics setup + K4-substrate lift) + identification of scale-universality / discreteness-correction structure. Multi-session work continues across sessions.
**Date:** 2026-05-17 night
**Lane:** Theoretical derivation pre-registration + initial derivation

## §0 — Pre-derivation discipline stack invocation (full skills ahead per Grant directive)

### §0.1 — ave-prereg (corpus-grep for prior Hoop Stress work)

Existing corpus has:
- **mond-hoop-stress.md §4.5** ([Vol 1 Ch 4](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md)): derivation of MOND $a_0 = c H_\infty/(2\pi)$ via Unruh-Hawking Hoop Stress; explicit statement of Hoop Stress geometric projection $T = F_r / (2\pi)$ in continuum-mechanics formulation (line 23)
- **mond-hoop-stress.md §4.5 cross-volume motif** (line 43-71, NEW 2026-05-17 evening): naming of the recurring pattern across 4 scales (cosmic MOND, substrate v_substrate, derived DAMA quantum E_slew, substrate-velocity refined to LSR-scope only)
- **dm-mechanism-unification.md §5.2** ([Vol 3 Ch 5](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md)): catalogued the Hoop Stress 2π sub-family as one of the two DM-mechanism operator classes
- **closure-roadmap.md §0.5 NEW 2026-05-17 evening entry** (line 98 in current version): identifies the Hoop Stress 2π substrate motif as "proposed canonical synthesis" with "rigorous derivation chain showing why 2π Hoop projection applies at both cosmic + substrate scales from common substrate principles" as open work.

**Prior derivation status**:
- Continuum-mechanics derivation of $T = F_r/(2\pi)$ EXISTS in classical mechanics (textbook physics)
- AVE-specific application at cosmic scale (MOND) is DERIVED via Unruh-Hawking + Hoop Stress in mond-hoop-stress.md §4.5
- AVE-specific application at substrate scale (v_substrate, ν_slew) is INDEPENDENTLY DERIVED via Schwinger anomalous-moment substrate-rate, NOT via direct Hoop Stress lift
- **The unified substrate-level derivation showing 2π is universal is OPEN** — this is what Tier-3 #10 tackles

### §0.2 — ave-canonical-leaf-pull (canonical leaves required)

- [`Vol 1 Ch 1 Axiom 1 (K4 Cosserat substrate)`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-axioms-and-lattice/index.md) — substrate topology foundation
- [`mond-hoop-stress.md` §4.5](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md) — continuum-mechanics derivation + cross-volume motif
- [`vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) — substrate-scale instance derivation
- [`vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md) §5.2 — sub-family catalogue
- [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) — cycle-12 canonical leaf using α-slew at substrate scale (where Hoop Stress 2π is embedded)

### §0.3 — ave-analytical-tool-selection (which toolkit-index tools apply)

Per [`ave-analytical-toolkit-index.md`](../manuscript/ave-kb/common/ave-analytical-toolkit-index.md):

- **§6 Mode analysis** — Z₀ derivation (discrete LC ladder), Op11+Op12 (discrete Yee-lattice curl/div on K4 graph), Op13 D'Alembertian — substrate-native PDE machinery
- **§8 Network analysis** — Topological Kinematics 6-row table, ξ_topo translation — mechanical ↔ EE translation
- **§1 Coupling analysis** — Op17 power transmission, Theorem 3.1' Z_radiation = Z₀/(4π) (spinor cycle), Sagnac-RLVE κ_entrain (drag-along)

**Why these are relevant**: the Hoop Stress 2π factor lives in the geometry of closed topological loops in the K4 substrate. §6 Mode analysis provides the substrate-native PDE tools to derive loop tension from substrate stress-strain. §8 Network analysis provides cross-domain translation (continuum-mechanics ↔ substrate-EE). §1 Coupling provides comparison with other geometric factors (4π spinor-cycle, etc.).

### §0.4 — ave-power-category-check (5-axis classification of Hoop Stress 2π projection)

The Hoop Stress 2π projection is:
- **Axis A (Real vs Reactive)**: GEOMETRIC — neither real nor reactive power; pure geometric projection factor relating external drift to internal tension
- **Axis B (Propagating vs Bound)**: BOUND-MODE PROPERTY — characterizes the equilibrium response of bound topological loops to external isotropic drift
- **Axis C (On-shell vs Off-shell)**: SUBSTRATE-NATIVE — the 2π is intrinsic to the substrate's topological structure
- **Axis D (Internal vs External)**: INTERNAL — applies to the substrate's intrinsic loop topology
- **Axis E (Substrate-mode vs Atomic-physics)**: SUBSTRATE-MODE — purely geometric; no atomic-Z dependence

**Categorical distinction from related factors**:
- 4π (spinor cycle): per Theorem 3.1' — applies to spinor-period averaging (electron internal phase loops in 4π radians, not 2π); DIFFERENT factor from Hoop Stress 2π
- π (half-cycle): would apply if loop covered only half the angular space; NOT the Hoop Stress case
- 4π (3D solid angle): per Sagnac-RLVE — solid-angle integration for full sphere; DIFFERENT geometry

### §0.5 — ave-discrimination-check (alternative interpretations)

| Alternative | Predicted geometric factor | Distinguishes via |
|---|---|---|
| **Hoop Stress 2π (universal)** | 2π for all closed-loop substrate projections | Cross-scale empirical pattern (cosmic + atomic) |
| **2π only valid at cosmic scale (continuum limit)** | 2π for cosmic; discreteness corrections for atomic | Atomic-scale observables should show O(ℓ_node/R_loop)² corrections |
| **Different factors at different scales (empirical coincidence)** | 2π_cosmic ≠ 2π_atomic numerically | Cross-scale check: any DERIVED 2π for substrate scale must match cosmic; if separate derivations give different 2π values, motif is coincidence |
| **2π is approximate; exact factor is something else** | Could be 2π × (1 + small correction); approximation works | Higher-precision measurements should reveal correction |

**Self-application discipline (cycle-12 reviewer pattern)**: this prereg's claims (2π is universal substrate property) are NEW derivation claims. Applying ave-discrimination-check Step 1.5:

| Claim | Free-parameter content | How constrained |
|---|---|---|
| 2π is universal across cosmic + substrate scales | Zero — geometric factor | Derived from K4 closed-loop topology |
| Scale-invariance OR discreteness corrections explain why 2π is exact at extremes | Some — scale-invariance assumption needs justification | Multi-session derivation work |
| Additional Hoop Stress instances at intermediate scales | Some — predicted but not yet observed | Falsifiable via future tests |

### §0.6 — ave-canonical-source (constants from constants.py)

Will use canonical:
- $\ell_{node} = \hbar/(m_e c) \approx 3.86 \times 10^{-13}$ m (Compton wavelength scale per `constants.py:180`)
- $H_\infty$ canonical cosmological asymptotic Hubble (per `constants.py`)
- $\alpha$ CODATA fine structure constant
- $m_e$, $c$ canonical
- No new constants required for this derivation

## §1 — Derivation target (precise)

**Derive**: that the 2π geometric factor appearing in:
- $a_0 = c H_\infty / (2\pi)$ (cosmic MOND scale)
- $\nu_{slew} = \alpha \omega_{Compton} / (2\pi)$ (substrate refresh rate)
- $v_{substrate} = \alpha c / (2\pi)$ (substrate-equilibrium velocity, LSR-class)

is the UNIVERSAL Hoop Stress geometric projection factor for closed topological loops in the K4 Cosserat substrate, with the form:

$$\text{[equilibrium observable]} = \frac{c \times \epsilon}{2\pi}$$

where $\epsilon$ is the scale-specific small parameter ($H_\infty$ cosmic, $\alpha$ substrate) and $c$ is the substrate-native propagation velocity.

**Specifically derive**:
1. Continuum-mechanics Hoop Stress for closed circular loop: $T = F_r / (2\pi)$
2. K4-substrate lift: discrete-lattice loop version recovers continuum 2π in scale-invariant or continuum limits
3. Scale-invariance argument: WHY 2π is exact at cosmic + substrate extremes (NOT at intermediate atomic/molecular scales)
4. Predictive content: additional scales where 2π should apply OR where discreteness corrections should be observable

## §2 — Physical picture (mechanical, no equations)

1. **K4 substrate has closed topological loops at multiple scales**: electron unknot at substrate scale (single closed loop in K4 graph), cosmic horizon at cosmic scale (de Sitter horizon as closed 3-sphere), proton/neutron at nuclear scale (torus knot loops). All are "closed topological structures" in the K4 substrate at different scales.

2. **External substrate drift exists at each scale**: cosmological expansion $c H_\infty$ at cosmic scale, α-slew refresh $\alpha \omega_{Compton}$ at substrate scale, possibly other drifts at intermediate scales. The drift is an isotropic radial pressure on closed loops.

3. **Hoop Stress geometric projection**: any closed loop subjected to isotropic radial pressure develops internal tension by the classical Hoop Stress formula. For continuous loops, the factor is exactly $1/(2\pi)$ from integration around the loop's $2\pi$ angular extent.

4. **Scale-universality requires**: either (a) the loop is large enough that K4 lattice discreteness is irrelevant (cosmic horizon: R ≫ ℓ_node, so discretization corrections vanish) OR (b) the loop topology is scale-invariant under conformal transformations (electron unknot: simplest closed loop with conformal symmetry — discreteness factors out).

5. **Intermediate scales should show discreteness corrections**: if a closed loop exists at scale R ~ a few × ℓ_node, the 2π factor would be modified by O((ℓ_node/R)²) corrections. Atomic and molecular orbital loops fall in this regime. Predictive content: Hoop Stress observables at atomic/molecular scales should NOT be exactly $c \times \epsilon / (2\pi)$.

## §3 — Pre-registered derivation chain

### Step 1 — Continuum-mechanics Hoop Stress derivation (textbook physics, repeated here for self-containment)

Closed circular loop of radius $R$ in 2D. External isotropic radial force per unit length $f_r$ (positive outward). Loop tension $T$ uniform around loop by symmetry.

Force balance on infinitesimal arc element $ds = R\, d\theta$:
- Tension at angle $\theta$ tangent to loop; tension at $\theta + d\theta$ tangent but rotated by $d\theta$
- Net radial component of internal tension forces: $2T \sin(d\theta/2) \approx T\, d\theta$ (inward, for small $d\theta$)
- External radial force on element: $f_r \cdot ds = f_r \cdot R\, d\theta$ (outward)

**Equilibrium**: $T\, d\theta = f_r \cdot R\, d\theta \Rightarrow T = f_r \cdot R$

**Total external radial force on full loop**: $F_r = \int f_r\, dl = f_r \cdot 2\pi R$

Solving for $T$ in terms of $F_r$:

$$\boxed{T = \frac{F_r}{2\pi}}$$

The $2\pi$ comes from integrating the external force over the full angular extent of the closed loop.

### Step 2 — K4-substrate lift: discrete-lattice loop version

K4 Cosserat lattice has discrete nodes spaced by $\ell_{node}$. A closed loop in the K4 graph traverses $N$ nodes with $N$ discrete steps of angular displacement $2\pi/N$.

For discrete loop with $N$ nodes:
- Internal tension per node: $T_n$ (uniform by symmetry for symmetric loop)
- Net radial force per node from tension: $2 T_n \sin(\pi/N) \approx (2\pi/N) T_n$ for $N \gg 1$
- External radial force per node: $F_r / N$ (total external $F_r$ distributed across $N$ nodes)

**Equilibrium**: $(2\pi/N) T_n = F_r / N \Rightarrow T_n = F_r / (2\pi)$

**Same result as continuum: $T = F_r / (2\pi)$** in the $N \gg 1$ limit.

For finite $N$ (small loops at scale R ~ N × ℓ_node), the exact formula:
$$T_n = \frac{F_r}{2 N \sin(\pi/N)} = \frac{F_r}{2\pi} \times \frac{1}{1 - \pi^2/(6 N^2) + O(N^{-4})}$$

**Discreteness correction**: factor $1 / (1 - \pi^2/(6N^2))$ deviates from unity by $\sim \pi^2/(6N^2) \approx 1.6 / N^2$.

For cosmic loop (R = R_H/ℓ_node ~ 10⁶⁰, N huge): correction ~ 10⁻¹²⁰ — totally negligible.
For substrate-scale electron unknot (R ~ ℓ_node, N = 1?): naive correction would be O(1), suggesting 2π factor is NOT exact at electron scale.

### Step 3 — Scale-invariance argument: WHY 2π is exact at substrate scale

The naive discreteness correction analysis predicts O(1) corrections at electron unknot scale. But empirically the prediction $\nu_{slew} = \alpha \omega_{Compton}/(2\pi)$ matches at the precision required by experiments. So either:
(a) The electron unknot has special topology that makes 2π factor exact even at N ~ few
(b) Other unknown corrections cancel the discreteness factor
(c) The "loop" at electron scale isn't actually a single K4 lattice cycle — it's a more elaborate structure where 2π factor emerges from different mechanism

**Conjecture (to be derived rigorously)**: the electron unknot is a "scale-invariant minimal-link" topology in K4 where conformal symmetry forces the geometric factor to be exactly 2π regardless of discrete-lattice realization. The Faddeev-Skyrme framework provides the scale-invariance: minimal solutions to the unknot Hamiltonian are conformally invariant on $S^3$, so the substrate-scale "loop" inherits the same 2π geometric factor as a continuum circle.

**Status**: this is conjecture, not derivation. Multi-session theoretical work required to either (a) rigorously derive scale-invariance, (b) compute discreteness corrections, or (c) find the alternative geometric mechanism.

### Steps 4-N — Future-session work

- Step 4: Faddeev-Skyrme scale-invariance for electron unknot — verify or refute that conformal symmetry produces exact 2π at substrate scale
- Step 5: Cosmic horizon geometry — verify that 3-sphere de Sitter horizon also produces exact 2π via spherical Hoop Stress
- Step 6: Intermediate-scale check — search for observables where loops at scale R ~ few × ℓ_node should show measurable discreteness corrections (atomic / molecular)
- Step 7: Predictive content — additional Hoop Stress instances at scales where 2π should apply OR fail
- Step 8: Connection to Theorem 3.1' 4π spinor factor — explicit distinction (Hoop Stress 2π is loop-integration; spinor 4π is internal-phase integration; both apply simultaneously at electron scale)

## §4 — Pre-registered outcomes

### Outcome A — 2π is universal (most likely if Conjecture above holds)

Scale-invariance argument validates. 2π is exact at cosmic + substrate scales via conformal symmetry of electron unknot + large-N limit at cosmic scale. Cross-volume motif STRENGTHENED — single derivation chain produces all scales.

**Probability assessment (before derivation)**: MEDIUM-HIGH (~40-55%). The empirical pattern is consistent; scale-invariance is plausible via Faddeev-Skyrme; needs derivation.

### Outcome B — 2π is exact at cosmic, approximate at substrate (discreteness corrections present but unmeasurable)

Cosmic-scale 2π is exact (large-N limit). Substrate-scale 2π has discreteness corrections of order $1.6/N^2$ where N is the effective lattice size of the electron unknot. If N is large enough (say ~100), corrections are at percent level — possibly within current measurement uncertainty (9% LSR gap could absorb percent-level corrections without empirical fingerprint).

**Probability assessment**: MEDIUM (~30-40%). Plausible but doesn't fundamentally falsify the motif.

### Outcome C — Different factors at different scales (motif is empirical coincidence)

Rigorous derivation reveals cosmic-scale uses different geometry than substrate-scale; 2π happens to appear in both via independent derivations. Cross-volume motif WEAKENED to "common factor coincidence."

**Probability assessment**: LOW (~10-15%). Would walk back the cross-volume synthesis.

### Outcome D — Hoop Stress factor is NOT 2π (rigorous derivation gives different number)

Rigorous derivation produces a factor that's close to but not exactly 2π (e.g., 6.28 not 6.2832). All scale-instances should be re-derived with corrected factor.

**Probability assessment**: VERY LOW (~5%). Would be a substantial finding requiring all 3 scale-instances to be re-derived.

## §5 — Falsifier specification

The 2π Hoop Stress motif is FALSIFIED at substrate scale if:

1. **High-precision substrate-velocity measurement reveals exact LSR-class velocity ≠ αc/(2π) × (1 + small)**: any non-2π geometric factor (e.g., 2π × Catalan-number correction) would manifest as systematic deviation from αc/(2π) prediction at <1% precision.

2. **Hoop Stress prediction fails at intermediate scale**: if Hoop Stress 2π is universal AND we identify an observable at intermediate scale (atomic / molecular) where it should apply, finding the predicted observable doesn't match would falsify universality.

3. **Faddeev-Skyrme analysis shows electron unknot has NOT conformally-symmetric topology**: would walk back the scale-invariance argument; require alternative derivation OR Outcome B.

## §6 — Canonization plan (gated on outcomes)

### If Outcome A or B closes (multi-session)

**Artifacts**:
1. NEW canonical KB leaf at `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/hoop-stress-2pi-substrate-motif.md` — rigorous derivation with K4 substrate topology + continuum-mechanics + scale-invariance argument
2. Toolkit-index entry for "Hoop Stress 2π substrate projection" under §6 Mode analysis or §8 Network analysis
3. Updates to mond-hoop-stress.md §4.5 cross-volume motif: scope from "proposed canonical synthesis" → "CANONICAL with rigorous derivation"
4. dm-mechanism-unification.md §5.2 update with rigorous-derivation reference
5. closure-roadmap §0.5 new entry closing Tier-3 #10 open work

### If Outcome C closes

**Walk-back artifacts**:
1. Remove "Hoop Stress 2π substrate motif" cross-volume synthesis from mond-hoop-stress.md §4.5
2. Update dm-mechanism-unification.md §5.2: limbs (i) + (iii) cross-volume sub-family RESCOPED to empirical coincidence (numerical 2π match across scales is coincidence)
3. closure-roadmap §0.5 new entry documenting walk-back

### If Outcome D closes

**Substantial walk-back across corpus**:
1. Re-derive cosmic, substrate, DAMA quantum at corrected factor
2. Update foreword DAMA bullet, matrix C14 row, all relevant leaves with corrected formulas
3. Multi-week corpus surgery work

## §7 — Difficulty estimate

- Step 1 + Step 2 (this session): COMPLETE — textbook continuum-mechanics + discrete-lattice derivation
- Step 3 (this session): CONJECTURE stated; rigorous derivation pending
- Steps 4-8: 3-5 sessions per ave-prereg discipline estimate, depending on Faddeev-Skyrme complexity + intermediate-scale observable identification

## §8 — What this session lands (Steps 1-3 + scaling insight)

**Closed at this session**:
1. **Continuum-mechanics derivation**: $T = F_r / (2\pi)$ from circular-loop equilibrium (textbook physics, repeated here for self-containment + AVE-substrate context)
2. **Discrete-lattice version**: same result $T = F_r / (2\pi)$ in $N \gg 1$ limit; explicit discreteness correction formula $1 / (1 - \pi^2/(6N^2))$ for finite N
3. **Scale-universality structure identified**:
   - Cosmic scale: N huge (R_H/ℓ_node ~ 10⁶⁰); discreteness corrections vanish; 2π EXACT
   - Substrate scale (electron unknot): N small (~1); naive discreteness correction O(1); CONJECTURE that conformal symmetry of Faddeev-Skyrme minimal soliton restores 2π exactness; needs rigorous derivation
   - Intermediate scale (atomic R ~ a_0 = ℓ_node/α ~ 137 ℓ_node, N ~ 137): discreteness correction $\sim 1.6/137^2 \approx 0.0085\%$ — too small to falsify but should be present if Hoop Stress applies at atomic scale
4. **Predictive content**: atomic-scale or molecular-scale observables where Hoop Stress 2π should apply with predicted discreteness correction at $0.01\%$-$1\%$ level. NOT yet identified specific observables; future work.

**Open for next sessions**:
- Step 4 Faddeev-Skyrme scale-invariance derivation
- Step 5 cosmic-horizon 3-sphere Hoop Stress derivation
- Step 6 intermediate-scale observable identification
- Step 7 predictive content + falsifier specifications
- Step 8 Theorem 3.1' 4π spinor factor distinction

## §9 — Outcome tracking

**Currently tracking Outcome A or B** (likely either is consistent with empirical pattern). Need Faddeev-Skyrme analysis (Step 4) to distinguish A vs B. Outcome C or D would require subsequent walk-back.

## §10 — Cross-references

**Upstream**:
- Cycle-12 thread context (parametric coupling kernel canonical leaf)
- closure-roadmap §0.5 NEW 2026-05-17 evening "Cross-volume Hoop Stress 2π substrate motif" open-work entry
- Tier-2 #5 GC test (substrate-velocity scope narrowing — informs which scales are Hoop Stress 2π valid)

**Canonical leaves cited**:
- [mond-hoop-stress.md §4.5](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md) — existing derivation + cross-volume motif
- [dm-mechanism-unification.md §5.2](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md) — Hoop Stress 2π sub-family catalogue
- [dama-alpha-slew-derivation.md](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) — substrate-scale instance derivation

**Faddeev-Skyrme context**:
- [src/ave/topological/faddeev_skyrme.py](../src/ave/topological/faddeev_skyrme.py) — engine for I_scalar computation; relevant for Step 4 Faddeev-Skyrme scale-invariance work

**Downstream (gated on outcomes)**:
- NEW canonical leaf `hoop-stress-2pi-substrate-motif.md` (gated on Outcome A or B closing)
- Updates to mond-hoop-stress.md §4.5 cross-volume motif scope
- closure-roadmap §0.5 entries (outcome-dependent)

---

**Prereg + Steps 1-3 landed 2026-05-17 night per Tier-3 #10 first-session work. Multi-session continuation: Faddeev-Skyrme scale-invariance derivation (Step 4); cosmic-horizon 3-sphere Hoop Stress (Step 5); intermediate-scale observable identification (Step 6). Full 6-skill discipline stack invoked per Grant directive "full skills ahead." Outcome A or B currently tracking; need Step 4-5 work to distinguish.**
