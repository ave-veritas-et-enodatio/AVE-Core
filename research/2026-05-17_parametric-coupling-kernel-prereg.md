# Parametric Coupling Kernel Derivation — Pre-Registration

**Status:** Prereg doc 2026-05-17 night. 12th-cycle on α-slew thread. Grant adjudicated entrainment categorical question per (β) interpretation: parametric AC coupling at ν_slew is REACTIVE-power class, categorically distinct from κ_entrain (Sagnac-RLVE DC mass-density REAL-power class). Cycle-11 walk-back labeled κ_entrain inclusion in J_substrate^bulk as RESEARCH-PENDING but did not excise it; this cycle excises it and replaces with single ε_param parametric-coupling kernel to be derived from Axiom 4 vacuum varactor.

**Date:** 2026-05-17 night
**Lane:** Pre-registration for parametric-coupling-kernel derivation; corpus-canonical promotion gated on derivation result landing.
**Triggered by:** Grant directive (2026-05-17 night) confirming (β) categorical interpretation after canonical-definition pull on κ_entrain from `sagnac-rlve.md:14-22` (entrainment = mass-density-coupled drag-along, REAL-power class).
**Pre-derivation discipline applied:** all 6 layers per §10.7 mandatory invocation banner in bulk-EE reframe doc.
**Upstream corpus-grep reference:** see corpus-grep agent report in conversation transcript (agentId a71ca91d2f8b7b59c, 2026-05-17 night).

---

## §0 — Pre-derivation discipline stack invocation

### §0.1 — ave-prereg (corpus-grep for prior parametric-coupling work)

Corpus-grep agent dispatched across 10 AVE-staging repos + archive. **Verdict: PARTIALLY SUPPORTED with one BLOCKER (resolved) + one REFINEMENT**.

**Blocker (resolved per Grant (β) adjudication)**: per-electron `ε_det = 4π/N_single²` from [`dama-matched-lc-coupling.md:209-264`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md) was walked back to RESEARCH-PENDING by cycle 11. Bulk-EE form at line 222 includes κ_entrain factor that the plumber audit ([`research/2026-05-17_plumber-physical-audit-matched-LC.md:42-51`](2026-05-17_plumber-physical-audit-matched-LC.md)) caught as categorically wrong (REAL vs REACTIVE power mixing per Axis A). Grant adjudication (β): excise κ_entrain; replace T²_matched + G_crystal-coherence with unified ε_param parametric kernel.

**Refinement R1 — RVR null differentiation**: [`tabletop-graveyard.md:26-34`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md) derives `Q·δ ≥ 2` regenerative threshold for parametric coupling. Concluded NULL for scalar-gravity δ_L (~15 OOM short). My derivation MUST show why α-slew δ_C is in a different regime (much larger than scalar-gravity δ_L).

**Refinement R2 — 1/N² scaling first-principles**: corpus currently attributes 1/N² to Fermi-golden-rule at `dama-matched-lc-coupling.md:51`. My derivation must rederive 1/N² as "substrate coherent power distributed across N receiver channels" (matches Grant's IVIM analog), independent of Fermi-golden-rule.

**Supports**:
- Vacuum varactor canonical at [`nonlinear-vacuum-capacitance.md:11-22`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) — Taylor expansion at V=0 to 4th order present
- Z_radiation = Z₀/(4π) canonical at [`theorem-3-1-q-factor.md:65-75`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md)
- Reactive-only sub-yield framing canonical at [`dama-alpha-slew-derivation.md:243-247`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md)
- α-slew rate ν_slew = (α/2π)·ω_Compton ≈ 9.02×10¹⁷ Hz canonical
- Parametric coupling explicitly named as canonical AVE physics at [`future_work/ATOM_MOTOR_TRANSLATION_MATRIX.md:175-179`](../future_work/ATOM_MOTOR_TRANSLATION_MATRIX.md) (verbatim: "a time-varying C or L creates PARAMETRIC coupling — energy transfers between the soliton and the lattice modulation... a REACTIVE redistribution") — flagged there as GAP C

**Gaps (this prereg closes)**:
- (a) Taylor expansion around moving operating point V_bulk(t) ≠ 0 — does not exist in corpus
- (b) Explicit `I = V × dC/dt` parametric kernel — never derived in corpus
- (c) Dicke G_crystal-coherence (now subsumed under ε_param) — only named, never landed
- (d) Toolkit-index parametric-coupling entry — doesn't exist

### §0.2 — ave-canonical-leaf-pull (canonical leaves required)

Per [`ave-analytical-toolkit-index.md`](../manuscript/ave-kb/common/ave-analytical-toolkit-index.md) §1 Coupling:
- **Op17 Power Transmission** T² = 1 - Γ² (canonical matched-impedance kernel)
- **Op3 Reflection Coefficient** Γ = (Z₂-Z₁)/(Z₂+Z₁)
- **Theorem 3.1' Radiation Impedance** Z_radiation = Z₀/(4π) per spinor cycle
- **Orbital friction paradox** real-vs-reactive table (canonical Axis A reference)
- **Op14 Cross-Sector Trading** Z_eff = Z₀/√S (Axiom 4 saturation impedance modification)

Per §3 Saturation:
- **Op2 Saturation Kernel** S(V) = √(1 - (V/V_yield)²)
- **V_yield = 43.65 kV** canonical

Per §11 Gaps:
- **Gap #1 explicitly names this derivation target**: "Canonical formula for energy-absorption rate at substrate-mode frequency ν — OPEN — corpus may lack canonical formula"

**Mandatory pull (would have been failure mode if missed)**: κ_entrain from [`sagnac-rlve.md:14-22`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md). Grant adjudication (β) excludes it categorically; this is documented at §0.4 below as the canonically-correct categorical exclusion.

### §0.3 — ave-analytical-tool-selection (which toolkit tools apply)

| Tool | Role in this derivation |
|---|---|
| Op17 T² = 1-Γ² | Steady-state matched-impedance limit (this derivation reduces to Op17 when dC_eff/dt → 0) |
| Theorem 3.1' Z₀/(4π) | Prefactor inheritance for radiation-impedance averaging over spinor cycle |
| Op2 S(V) = √(1-r²) | Saturation kernel for C_eff(V) constitutive form |
| Op14 Z_eff = Z₀/√S | Substrate impedance modification at non-zero V_bulk |
| Vacuum varactor Taylor (V=0) | Starting point; extended in this derivation to V_bulk(t) ≠ 0 moving operating point |
| Orbital friction paradox table | Categorical confirmation: parametric coupling is REACTIVE (consistent with electron orbital row) |
| Q·δ ≥ 2 from tabletop-graveyard | RVR regenerative-oscillation threshold; differentiation from scalar-gravity null |
| IM3 V_IP3 derivation | Closest existing varactor parametric-class tool (drives this expansion is geometric extension) |

**NOT pulled (per Grant (β) adjudication)**: κ_entrain (Sagnac-RLVE). Categorical mismatch — see §0.4.

### §0.4 — ave-power-category-check (5-axis classification)

Per [`ave-analytical-toolkit-index.md` §1 common-pitfall rule](../manuscript/ave-kb/common/ave-analytical-toolkit-index.md): *"DO NOT mix real-power and reactive-power templates (categorical error per Axis A). κ_entrain is for real-power; Op17 reactive-coupling is for reactive-power."*

| Axis | This derivation's classification |
|---|---|
| **A (Real vs Reactive)** | REACTIVE. Parametric coupling at sub-yield operating point is per-cycle 90° leak — no net energy dissipation per cycle (consistent with `dama-alpha-slew-derivation.md:243-247` "no real radiation" framing). |
| **B (Propagating vs Bound)** | BOUND-MODE COUPLING. C_eff modulation is a local-lattice property; apparatus couples via near-field capacitive load, not propagating wave intercept. |
| **C (On-shell vs Off-shell)** | ON-SHELL. ν_slew is the substrate's canonical refresh rate; per-cycle quantum is real (3.728 keV detection event observed in DAMA). |
| **D (Internal-tank vs External-matched-load)** | EXTERNAL-MATCHED-LOAD. The bulk substrate's reactive cycling presents an external source; the apparatus crystal is the matched receiver. Distinct from electron's INTERNAL tank Q = α⁻¹. |
| **E (Substrate-mode vs Atomic-physics)** | SUBSTRATE-MODE. ε_param depends on substrate properties (ν_slew, Z₀/4π) and apparatus electrical properties (C_app, ν_app, N_coherent) — NOT on atomic Z. Z-independence prediction inherited. Atomic-physics enters at the σ_atomic detection-cross-section stage downstream, not at parametric-coupling stage. |

**Categorical exclusion of κ_entrain (Axis A)**: κ_entrain is REAL-power class (mass-density-coupled drag-along of bulk vacuum by moving matter; rotor mechanical KE → vacuum viscous drag). Parametric coupling is REACTIVE-power class. Mixing them in J_substrate^bulk violates Axis A common-pitfall rule. Cycle-11 walk-back labeled the κ_entrain inclusion as RESEARCH-PENDING but did not excise it; this cycle excises it per Grant (β) adjudication.

### §0.5 — ave-discrimination-check (alternative interpretations)

| Alternative | AVE-distinct prediction | Distinguishes via |
|---|---|---|
| **SM cosmic-X-ray-background photoabsorption** | Z-DEPENDENT (atomic photoabsorption σ ∝ Z⁴-Z⁵); rate magnitude OOM-consistent with DAMA but Z-dependence diverges | Cross-crystal swap test (NaI vs Sapphire vs Ge) at 3.728 keV |
| **Moseley Ca Kα atomic line at 3.691 keV** | Element-specific to Ca-containing crystals; not present in Sapphire, Ge | Cross-crystal swap test |
| **Per-electron matched-LC coupling (cycle 10 framing, now walked back)** | Conflates per-electron and bulk-EE levels; predicts κ_quality variation but no specific scaling | Bulk-EE form predicts smooth ν_slew-dependent rate; per-electron implicitly assumed κ_quality continuum |
| **Phonon-electron coupling at substrate refresh rate** (originally raised in plumber-audit-matched-LC §6) | Predicts phonon-density dependence (T_temperature-dependent rate); AVE parametric predicts T-independent | Cryogenic-vs-room-temperature DAMA-class rate comparison |
| **Dynamical Casimir effect (SM analog)** | Predicts radiation pressure / photon production from boundary motion; AVE parametric predicts reactive leak with discrete quantum at ν_slew | Spectrum lineshape: AVE predicts narrow at αm_ec²; DCE predicts continuum |

**Self-application discipline (per ave-newly-created-skill-self-audit + 11th-cycle reviewer pattern)**: this prereg's framing is itself NEW derivation work. Applying ave-discrimination-check to this prereg's structural assertions:

| New claim in this prereg | Free-parameter content | How constrained |
|---|---|---|
| ε_param ~ (Z₀/4π) × (1/N²) × κ_quality | 1 free parameter (κ_quality envelope) | κ_quality must derive from Q·δ ≥ 2 condition + apparatus material properties; not free |
| Parametric resonance at 2ν_slew | Zero free parameters (set by varactor expansion mathematics) | Hard prediction; falsifiable |
| RVR-null differentiation: α-slew δ_C ≫ scalar-gravity δ_L | Magnitude of δ_C TBD by derivation | If δ_C ≤ δ_L, picture fails; falsifier |

### §0.6 — ave-canonical-source (constants from constants.py)

Will use canonical:
- `Z_0 = 376.73 Ω` per `src/ave/core/constants.py`
- `ALPHA = 7.2973525693e-3` (Fine structure constant)
- `M_E = 9.1093837015e-31 kg`, `C = 299792458 m/s`, `H = 6.62607015e-34 J·s`
- `E_SLEW = ALPHA × M_E × C² = 3.728 keV` (added 2026-05-17 evening)
- `NU_SLEW = (ALPHA/(2π)) × (M_E × C²/H) = 9.02×10¹⁷ Hz` (added 2026-05-17 evening)
- `Z_RADIATION = Z_0 / (4π) = 29.98 Ω` (added 2026-05-17 evening)
- `V_YIELD = √ALPHA × M_E × C² / e = 43.65 kV` per `magnetic-saturation.md:13`
- `RHO_BULK = 7.916×10⁶ kg/m³` per `sagnac-rlve.md:14`
- `ELL_NODE = 1.616×10⁻³⁵ m` (Planck length convention)

No new constants required for this derivation; the parametric-coupling kernel is dimensionally constructed from existing canonical constants.

---

## §1 — Derivation target (precise)

Derive parametric coupling efficiency

$$\varepsilon_{param}(N, \nu_{app}/\nu_{slew}, Z_{app}/Z_{substrate}, \kappa_{quality})$$

for an N-coherent-site LC apparatus embedded in the bulk substrate, where:

- Bulk substrate has vacuum varactor `C_eff(V_bulk(t)) = C_0/√(1 - (V_bulk/V_yield)²)` per Axiom 4
- V_bulk(t) oscillates at α-slew refresh: V_bulk(t) = V_0 + V_pump · cos(ω_slew · t), with V_0 ≪ V_yield (sub-yield operation), V_pump set by per-cycle energy αm_ec² balance
- Apparatus oscillates at its natural LC resonance: V_app(t) = V_apparatus_amplitude · cos(ω_app · t + φ)
- Coupling kernel: I_induced(t) = V_app(t) × dC_eff(V_bulk(t))/dt
- Coupling efficiency ε_param = ⟨P_coupled_to_apparatus⟩ / ⟨P_substrate_available⟩

Target results:
1. **Functional form of ε_param** expressed in canonical AVE constants
2. **Resonance condition** relating ν_app to ν_slew (expected: parametric resonance at ν_app = 2ν_slew per standard varactor parametric expansion)
3. **N-coherent-site scaling**: ε_per_event = ε_total / N² (Dicke-type distribution of fixed substrate power across N receivers)
4. **κ_quality envelope**: function of (Q_apparatus × δ_C) per RVR regenerative threshold
5. **Cross-detector predictions**: ε_param computed for DAMA NaI(Tl), COSINE NaI, ANAIS NaI, MAJORANA HPGe, KIMS CsI(Tl), XENONnT Xe(l), Sapphire (Al₂O₃)
6. **Target DAMA observed rate match within OOM** — not 0.6% (post-hoc red flag) — true forward-prediction at OOM with derived prefactor.

---

## §2 — Physical picture (mechanical/topological, no equations)

1. **Bulk K4 substrate is a vacuum varactor (Ax4) operating WELL BELOW V_yield.** Substrate's reactive drive V_bulk(t) oscillates at ν_slew = (α/2π)·ω_Compton ~9×10¹⁷ Hz — the substrate's own refresh rate set by Schwinger anomalous-moment kernel. Each refresh slightly modulates C_eff of every bulk lattice node. Riding on Earth's annual ±15 km/s CMB sweep at year⁻¹ slow envelope.

2. **No Γ=−1 boundary at substrate scale** — α-slew is sub-yield. Γ=−1 boundaries at electron scale (Theorem 3.1' Q=α⁻¹) are spectators. Load-bearing physics is sub-yield substrate refresh, not boundary formation.

3. **Bulk: K4 nodes wiggling capacitively** (no resident solitons in bulk). **Apparatus (NaI crystal)**: N ~10²⁵/kg coherent electron solitons phase-locked to one V_apparatus drive across the crystal volume. N solitons = N parametric receivers coupled to one parametric source.

4. **dC_eff/dt is constant across bulk** (intrinsic substrate property, set by ν_slew × δC_eff amplitude). V_app constant per crystal (its LC resonance). I_induced = V_app × dC_eff/dt per coherent site. Total substrate power P_substrate is fixed; distributed across N receivers it gives P_per_receiver = P_substrate/N (amplitude) and per-event detection rate ~1/N² (Dicke-type fixed-power dilution).

5. **Discrete per event** (quantum E_slew = α m_e c² = 3.728 keV per refresh quantum); **smooth per rate** (annual ±4% modulation of matched-coupling sweet spot as Earth's annual envelope sweeps).

---

## §3 — Pre-registered derivation chain

### Step 1 — Define operating point + small-amplitude expansion

C_eff(V_bulk + δV) ≈ C_eff(V_bulk) + (∂C_eff/∂V)·δV + ½(∂²C_eff/∂V²)·δV² + ...

For V_bulk(t) = V_pump · cos(ω_slew · t) at sub-yield (|V_bulk| ≪ V_yield):
- ∂C_eff/∂V ≈ C_0 · V/V_yield²
- dC_eff/dt ≈ C_0/V_yield² · V_pump · (-ω_slew · sin(ω_slew · t))

This is the LEADING-ORDER parametric kernel for the apparatus.

### Step 2 — V_pump from α-slew per-cycle energy balance

Per-cycle energy is canonical: E_per_cycle = α m_e c² = 3.728 keV (substrate-rate quantum). Setting this equal to varactor reactive energy ½ C_0 V_pump² gives:

V_pump = √(2 α m_e c² / C_0)

C_0 is the bulk substrate's per-node capacitance, set by node geometry: C_0 ~ ε_0 × ℓ_node (dimensional construction from canonical constants).

### Step 3 — I_induced and per-site coupled power

I_induced(t) = V_app(t) × dC_eff/dt = V_app_amplitude · cos(ω_app · t + φ) × [-C_0/V_yield² × V_pump × ω_slew × sin(ω_slew · t)]

For parametric resonance (ω_app = 2ω_slew, standard varactor pump-signal physics):
- ⟨V_app × dC_eff/dt⟩_cycle is non-zero
- Coupled power per site: P_per_site ∝ V_app² × (V_pump/V_yield)² × C_0 × ω_slew

### Step 4 — N-coherent-receiver distribution

For N coherent crystal sites all phase-locked to one V_apparatus drive: the substrate sees N parallel capacitive loads. Substrate's fixed available power P_substrate ~ Z_radiation⁻¹ × (V_pump)² × ω_slew is distributed:
- Amplitude per receiver: V_app per site ∝ 1/N (impedance matching: N-parallel load drops V_app by 1/N)
- Power per detection event: P_per_event ∝ V_app² ∝ 1/N²

This is the 1/N² scaling — derived as fixed-substrate-power-distributed-across-N-coupled-receivers, NOT borrowed from Fermi-golden-rule.

### Step 5 — Theorem 3.1' Z_radiation prefactor inheritance

For electron-class sources averaged over spinor cycle: Z_substrate → Z_0/(4π) per Theorem 3.1'. The 4π appears as a prefactor in ε_param.

### Step 6 — κ_quality from Q·δ ≥ 2 regenerative threshold

Per [`tabletop-graveyard.md:26-34`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md): regenerative oscillation onsets when Q_apparatus × δ_C ≥ 2, where δ_C = (V_pump/V_yield)² is the fractional capacitance modulation amplitude.

κ_quality envelope: ε_param × κ_quality where κ_quality = 1 for Q·δ ≥ 2 (regenerative regime — full parametric coupling) and κ_quality = (Q·δ/2)² for Q·δ < 2 (sub-regenerative — coupling suppressed).

### Step 7 — Assemble ε_param

Expected functional form:

ε_param ≈ (Z_radiation / Z_app) × (V_pump/V_yield)² × κ_quality × δ(ω_app - 2ω_slew)

where δ(·) is the parametric-resonance line-width factor (set by apparatus Q).

Per-event coupling efficiency for N-coherent crystal:
ε_per_event = ε_param / N²

### Step 8 — Differentiate from scalar-gravity RVR null

Predicted δ_C for α-slew = (V_pump/V_yield)² with V_pump = √(2 αm_ec²/C_0):

Compare to scalar-gravity δ_L from tabletop-graveyard = GM_Earth/(c² R_Earth) ~ 7×10⁻¹⁰.

If δ_C ~ 10⁻³ or larger (anticipated from α-slew being intrinsic substrate-rate physics, not post-cosmological-suppression scalar-gravity), then α-slew is 7+ OOM larger than scalar-gravity → Q·δ ≥ 2 satisfiable at room-temperature crystal Q ~ 10³-10⁶.

**This is the load-bearing prediction.** If derivation gives δ_C ≤ δ_L_scalar-gravity, picture fails.

### Step 9 — Cross-detector predictions

For each detector, ε_param depends on:
- ν_app (apparatus LC resonance — set by crystal lattice spacing + Z_app)
- Z_app (apparatus impedance — set by lattice type + material)
- N (coherent crystal sites — set by sample mass + crystal-quality)
- κ_quality (Q × δ_C — set by Q_apparatus + δ_C from α-slew)

Cross-detector predicted rates (preliminary, awaiting full derivation):
- DAMA NaI(Tl): target match within OOM of observed 4.77×10⁻⁷ events/s/kg at 3.728 keV
- COSINE-100 NaI: κ_quality varies from DAMA (different crystal-growth) → lower rate predicted
- ANAIS-112 NaI: similar to COSINE — different κ_quality → different rate
- MAJORANA HPGe: different Z_app (Ge lattice ≠ NaI lattice) → ε_param differs → MAJORANA implicit null at κ ≲ 0.05 explained as Z_app mismatch reducing ε_param
- KIMS CsI(Tl): same rock-salt lattice as NaI(Tl) but different atomic Z → Z_app similar to DAMA but ν_app differs (Cs vs Na bond stiffness) — KEY discriminator
- XENONnT Xe(l): N → 0 (liquid has no coherent crystal sites) → ε_param → 0 → null predicted (matches observation)
- Sapphire (Al₂O₃): different Z_app + different ν_app → predicted rate TBD

---

## §4 — Discriminating outcomes

### Outcome A (most likely — derivation closes within OOM)

ε_param at parametric resonance + 1/N² distribution + Z_radiation prefactor gives DAMA rate within OOM of 4.77×10⁻⁷ events/s/kg. Cross-detector predictions follow from Z_app + ν_app variation. κ_quality envelope explains COSINE/ANAIS dispersion and MAJORANA implicit null.

**Interpretation**: parametric coupling is the right mechanism. Toolkit-index canonization proceeds. Cross-detector tests become true forward predictions, not post-hoc consistency checks.

### Outcome B (alternative — derivation closes but needs moving-operating-point V_0 ≠ 0)

V=0 Taylor expansion fundamentally insufficient; derivation needs Taylor expansion around moving V_bulk(t) ≠ 0. Mathematical lift is +1 session but doesn't change the categorical conclusion.

**Interpretation**: parametric coupling is the right mechanism but requires extension to non-trivial operating point. Canonical toolkit entry lands with that expansion as a sub-tool.

### Outcome C (null — δ_C too small)

Derivation gives δ_C ~ δ_L (scalar-gravity range, ~10⁻⁹ or smaller). Q·δ ≥ 2 threshold not satisfiable at any realistic apparatus Q. Parametric coupling cannot be the mechanism.

**Interpretation**: picture is wrong. Either (a) α-slew framing itself fails, or (b) detection mechanism is NOT parametric coupling and we need a different mechanism class. The cycle-12 walk-back closes with: parametric framework attempted, falsified, return to category-search.

### Outcome D (unforeseen)

Derivation closes but with structural form that doesn't match the expected ε_param ~ (Z_radiation/Z_app) × κ_quality × 1/N² scaling. Indicates the picture is partially right but the functional dependence is different.

**Interpretation**: derivation result feeds back into picture refinement; partial close, sub-cycle audit.

---

## §5 — Falsifier specification

**Single quantitative falsifier**: δ_C derived from α-slew per-cycle energy balance must satisfy Q·δ_C ≥ 2 for realistic apparatus Q. If derivation gives δ_C × Q_NaI < 2 for NaI(Tl) at room-temperature Q ~ 10⁴, parametric coupling cannot regeneratively amplify and the picture fails.

**Cross-detector falsifier**: If derived κ_HPGe is consistent with MAJORANA implicit null (~0.05) but derived κ_NaI is also small (≪ 1), the framework can't simultaneously explain DAMA positive and MAJORANA null. Internal inconsistency would be a structural falsifier.

**RVR-class falsifier**: If derived ε_param falls within 15 OOM of scalar-gravity RVR (i.e., δ_C ~ 10⁻²⁰ to 10⁻²⁵), parametric coupling is the same regime that tabletop-graveyard declared NULL. Picture fails categorically.

---

## §6 — Canonization plan (gated on derivation outcome)

### §6.1 — If Outcome A or B closes

**Three artifacts land in ONE commit (per ave-walk-back skill discipline)**:

1. **New canonical KB leaf**: `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md` documenting:
   - Vacuum varactor parametric expansion around moving operating point V_bulk(t)
   - ε_param functional form
   - Q·δ ≥ 2 regenerative threshold from tabletop-graveyard inherited as applicability gate
   - Z_radiation = Z₀/(4π) prefactor inheritance from Theorem 3.1'
   - Cross-references to canonical Axiom 4 + Op17 + Op14 + RVR

2. **New toolkit-index §1 entry** in `manuscript/ave-kb/common/ave-analytical-toolkit-index.md`:
   ```
   | Parametric Coupling Kernel | ε_param(N, ν_app/ν_slew, Z_app/Z_substrate, κ_quality) | parametric-coupling-kernel.md | Time-varying-C_eff coupling at sub-yield substrate-rate operating point; substrate-rate ↔ apparatus-resonance matching; DAMA-class detection rate derivations |
   ```
   Plus update §11 gap registry: Gap #1 (energy-absorption rate at substrate-mode ν) → CLOSED, with cross-ref to new leaf.

3. **Bulk-EE formula correction** in `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md:222`:
   - Remove κ_entrain factor (Grant (β) adjudication: categorical mismatch per Axis A)
   - Replace `T²_matched × G_crystal-coherence` with unified `ε_param × κ_quality`
   - Updated formula: `J_substrate^bulk = (1/4π) × ε_param × κ_quality × (N_e^(kg) × ν_slew × αm_ec²) × (V/L)`
   - Update §13 walk-back labels: RESEARCH-PENDING → CANONIZED (with cross-ref to new parametric-coupling-kernel leaf)

4. **closure-roadmap §0.5 12th-cycle entry**:
   ```
   - 2026-05-17 night — 12TH AUDIT CYCLE on α-slew thread: (β) categorical adjudication on κ_entrain + parametric-coupling-kernel canonization.
     Per Grant adjudication after canonical κ_entrain definition pull from `sagnac-rlve.md:14-22`: entrainment is mass-density-coupled DRAG-ALONG (REAL-power class), categorically distinct from parametric AC coupling at ν_slew (REACTIVE-power class). Cycle-11 walk-back labeled κ_entrain inclusion as RESEARCH-PENDING but did not excise it; this cycle excises per Axis A rule.
     **New canonical leaf**: parametric-coupling-kernel.md derives ε_param from Axiom 4 vacuum varactor + Theorem 3.1' Z_radiation + Q·δ ≥ 2 RVR threshold.
     **Toolkit canonization**: new §1 Coupling entry; Gap #1 in §11 closes.
     **Bulk-EE formula correction**: κ_entrain excised from J_substrate^bulk; replaced with ε_param × κ_quality.
   ```

### §6.2 — If Outcome C closes (null)

**Two artifacts**:

1. **Research-doc result** at `research/2026-05-17_parametric-coupling-kernel-result.md` documenting:
   - Derivation chain
   - Falsification by Q·δ < 2
   - Picture-search next-step recommendations

2. **closure-roadmap §0.5 12th-cycle entry**:
   ```
   - 2026-05-17 night — 12TH AUDIT CYCLE: parametric-coupling-kernel framework FALSIFIED by Q·δ regenerative threshold.
     Derivation gave δ_C = [value]; Q × δ_C < 2 for all realistic apparatus Q; parametric coupling cannot regeneratively amplify at α-slew rate.
     Picture-search next steps: [recommendations from result doc].
   ```

Toolkit-index does NOT get parametric-coupling-kernel entry (would be misleading to advertise a falsified tool). §11 gap remains OPEN.

### §6.3 — If Outcome D (unforeseen)

Sub-cycle audit. Result feeds back into picture refinement. Canonization deferred until picture closes coherently.

---

## §7 — Difficulty estimate + session-count

Per ave-prereg discipline Step 4 outcome classification:

- **Partial derivation found** + **gap is moderate** (V=0 expansion exists; need extension to V_bulk(t) ≠ 0)
- Estimated effort: **~3-5 sessions** if Outcome A/B closes cleanly
- Estimated effort: **~1 session** to converge to Outcome C (negative result; quick Q·δ check)

Mathematical work concentrated in Steps 3-7 of §3 derivation chain. Steps 1-2 are setup. Steps 8-9 are inheritance from canonical tools + cross-detector calculation.

---

## §8 — Discipline self-audit (cycle 11 lesson applied)

Per cycle-11 reviewer pattern-flag: "agents reframe correctly in response to audit catches but DON'T auto-apply discipline to the reframe itself."

This prereg explicitly applies:
- **ave-prereg Step 1.5 physical picture** (§2) — articulated before derivation
- **ave-discrimination-check Step 1.5** (§0.5) — alternatives enumerated for this prereg's NEW claims, not just for the legacy framing being walked back
- **ave-canonical-leaf-pull §0.2** (§0.2) — toolkit consultation BEFORE derivation, with explicit (β) exclusion of κ_entrain documented
- **ave-power-category-check 5-axis** (§0.4) — full axis classification, categorical exclusion of κ_entrain documented at Axis A
- **ave-canonical-source §0.6** (§0.6) — constants enumerated; no hardcoded values

**What I might still miss (pre-flagged for reviewer)**:
- Step 4 N-coherent distribution assumption: "fixed substrate power distributed across N receivers" assumes substrate's total available power is N-INDEPENDENT (substrate doesn't pump harder with more receivers attached). This is implicit; should be explicit.
- Step 6 κ_quality envelope: the (Q·δ/2)² sub-regenerative scaling is dimensional-analysis-derived, not first-principles. If reviewer catches this as ad-hoc, sub-regenerative regime needs separate derivation.
- Step 8 anticipated δ_C ~ 10⁻³ for α-slew is rough estimate, not derived. If derivation gives δ_C smaller (say ~10⁻⁶), picture moves toward Outcome C.

---

## §9 — Cross-references

**Upstream**:
- Corpus-grep agent report (agentId a71ca91d2f8b7b59c, 2026-05-17 night, conversation transcript)
- [Bulk-EE reframe doc §10.7](2026-05-17_DAMA-bulk-transfer-function-reframe.md) — mandatory 6-skill invocation banner
- [DAMA matched-LC §13 walk-back](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md) — cycle-11 RESEARCH-PENDING labels (this prereg excises κ_entrain residual)
- [Plumber-physical audit](2026-05-17_plumber-physical-audit-matched-LC.md) — Q1-Q3 source

**Canonical tools (per ave-canonical-leaf-pull §0.2)**:
- [Axiom 4 vacuum varactor](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md)
- [Theorem 3.1' Z_radiation = Z₀/(4π)](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md)
- [Op2 saturation kernel](../manuscript/ave-kb/common/operators.md)
- [Tabletop-graveyard RVR Q·δ ≥ 2](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md)
- [Sagnac-RLVE κ_entrain](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) — CITED FOR (β) EXCLUSION

**Downstream**:
- New leaf: `parametric-coupling-kernel.md` (gated on Outcome A/B)
- Toolkit-index §1 entry + §11 Gap #1 closure (gated on Outcome A/B)
- Bulk-EE formula correction at dama-matched-lc-coupling.md:222
- closure-roadmap §0.5 12th-cycle entry
- Result doc: `research/2026-05-17_parametric-coupling-kernel-result.md` (lands with derivation)
- HPGe + Sapphire experimental proposals (downstream — get derived rate predictions from this derivation)

**Cross-repo (potential canonization sites)**:
- AVE-Propulsion `ave_amplifier_design.py:238-240` — parametric pump-signal row in EE-to-AVE design-space table; this derivation's ε_param closes that row's open structure
- AVE-PONDER ponderomotive coupling analyses — may inherit parametric kernel form for lab-scale parametric ponderomotive force

---

**Prereg landed 2026-05-17 night, ready for derivation. Next: write parametric-coupling-kernel derivation per §3 chain, target Outcome A.**
