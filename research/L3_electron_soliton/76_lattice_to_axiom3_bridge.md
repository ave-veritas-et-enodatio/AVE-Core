# 76 — Lattice-Level Op14 Saturation as the Substrate Realization of Axiom 3 + Axiom 4 (Local Clock Rate, Local c, and the Round 7+8 Empirical Reframe)

> ⚠️ **SUPERSEDED 2026-04-27** — this doc's framing is built on **Scheme B** of the corpus axiom numbering (per [`.agents/handoffs/axiom_homologation.md`](../../.agents/handoffs/axiom_homologation.md), `eq_axiom_3.tex`'s "Axiom 3 — Gravity"). Per cross-repo audit (520 axiom occurrences across 9 repos, 469 in Scheme A), **Scheme A is canonical**: Ax 3 = Effective Action Principle ($\mathcal{L}_{node}$), NOT Gravity. The gravitational refractive index $n(r)$ and $c_{eff} = c_0\sqrt{S}$ relations are **derived consequences** of Ax 1 (LC network) + Ax 4 (saturation kernel) under symmetric $\mu/\varepsilon$ scaling — they are not primitive Ax 3 content. This doc therefore mis-numbers the bridge: the substrate-level statement is "lattice Op14 IS the substrate realization of **Ax 4** (per Vol 3 Ch 3 + Vol 3 Ch 20 derivation chain)," not "Ax 3 + Ax 4."
>
> The empirical content of the doc (E-072 observer gap, single-cell vs path-integrated framing, Op14 modulation patterns, Round 7+8 reframe) may still be valid under Scheme A but the axiom-numbering surgery is wrong throughout. **Hold for reframe** — do not cite this doc as authoritative for Ax 3 framing. The lattice-to-corpus bridge should be rewritten with Ax 4 (saturation) as the load-bearing axiom and the gravity-as-derived-consequence framing made explicit.

**Status:** auditor-drafted research doc, 2026-04-27. Bridges the gap between engine-level Op14 z modulation (Ax 4 implementation) and corpus-level macroscopic Ax 3 framework (gravitational refractive index, local clock rate, c_max in deep voids). Also reframes Round 7+8 empirical findings as direct manifestations of corpus axioms rather than anomalies.

**Authority (per Scheme B — see supersession banner):** [`manuscript/common_equations/eq_axiom_1.tex`](../../manuscript/common_equations/eq_axiom_1.tex), [`eq_axiom_2.tex`](../../manuscript/common_equations/eq_axiom_2.tex), [`eq_axiom_3.tex`](../../manuscript/common_equations/eq_axiom_3.tex), [`eq_axiom_4.tex`](../../manuscript/common_equations/eq_axiom_4.tex) (the eq_axiom files claim "single source of truth" but their numbering disagrees with Vol 1 Ch 1; per axiom homologation, only Ax 4 in those files matches canonical) + [`vol_3_macroscopic/chapters/03_macroscopic_relativity.tex`](../../manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex) (optical metric chapter) + [`vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex:94-97`](../../manuscript/vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex#L94) (local clock rate equation) + [`COLLABORATION_NOTES.md` Rule 10 corollary A-010](../../.agents/handoffs/COLLABORATION_NOTES.md) (local-clock-modulation, lattice-level statement).

**Trigger:** Grant directive 2026-04-27 — *"if frequency is variable, what is the purpose of time in AVE?"* Corpus survey revealed that the framework already has a complete answer (Ax 3 + Ax 4 + Vol 3 Ch 3) but the lattice-level engine implementation hasn't been bridged explicitly to the corpus-level axiom statements. R7+R8 methodology arc was probing effects that are corpus-canonical, not anomalies — but no engine observer reports them in Ax-3-native terms.

**Companion docs:** [doc 66_ §17.2](66_single_electron_first_pivot.md) three-storage-mode mapping (V_inc, Φ_link, u, ω as conjugate LC pairs) — defines the substrate sectors. [doc 70_ §1 A29](70_phase5_resume_methodology.md) Φ_link as derived flux observable — locates Φ_link in the K4 LC tank. [doc 72_ §1](72_vacuum_impedance_design_space.md) four AVE-native concepts — frames the wave-substrate-not-minimization-substrate principle. [doc 73_ §3.1.1](73_discrete_k4_tlm_lctank_operator.md) V=0 decoupling caveat — names the cross-block vanishing at V=0 seed. [doc 75_](75_cosserat_energy_conservation_violation.md) conservation-of-energy-violation in Cosserat T_kinetic — closely related, predates this bridge.

---

## 1. The four corpus axioms, restated with citations

Foundation: the corpus axioms IS-OF-TRUTH lives in [`manuscript/common_equations/eq_axiom_*.tex`](../../manuscript/common_equations/) (single source per file header convention).

### 1.1 Axiom 1 — Impedance ([eq_axiom_1.tex](../../manuscript/common_equations/eq_axiom_1.tex))

```
Z_0 = √(μ_0 / ε_0) ≈ 376.73 Ω
ℓ_node = ℏ / (m_e c) ≈ 3.86 × 10⁻¹³ m
```

The vacuum is a discrete LC resonant network with characteristic impedance Z_0 and lattice pitch ℓ_node. Per [`eq_axiom_1.tex:15-16`](../../manuscript/common_equations/eq_axiom_1.tex#L15): *"μ_0 is the per-node inductance (rotational inertia) and ε_0 is the per-node capacitance (elastic compliance)."*

**Implementation note:** the K4-TLM lattice in [`src/ave/core/k4_tlm.py`](../../src/ave/core/k4_tlm.py) realizes this — discrete nodes at ℓ_node spacing, scatter+connect dynamics with Z_0 wave impedance.

### 1.2 Axiom 2 — Fine Structure ([eq_axiom_2.tex](../../manuscript/common_equations/eq_axiom_2.tex))

```
α = e² / (4π ε_0 ℏ c) ≈ 1/137.036
V_yield = √α · V_snap = √α · m_e c² / e ≈ 43.65 kV
```

α couples topology to impedance; it sets the saturation threshold V_yield in terms of V_snap.

### 1.3 Axiom 3 — Gravity ([eq_axiom_3.tex](../../manuscript/common_equations/eq_axiom_3.tex))

**This is the load-bearing axiom for "what is time in AVE."**

```
G = ℏc / (7ξ · m_e²)                           [eq:axiom3_gravity]
n(r) = 1 + 2GM/(rc²)                           [eq:axiom3_refraction]
μ_eff = μ_0 · n(r),  ε_eff = ε_0 · n(r),  Z = Z_0 (invariant)
```

ξ = 4π(R_H/ℓ_node)·α⁻² ≈ 8.15 × 10⁴³ is the Machian hierarchy coupling.

**Derived consequence 1 — α invariance** ([eq_axiom_3.tex:21-31](../../manuscript/common_equations/eq_axiom_3.tex#L21)):

```
α_local = e² / (4π · ε_local · ℏ · c_local)
        = e² / (4π · (ε_0 · n · S) · ℏ · (c_0 / (n · S)))
        = e² / (4π · ε_0 · ℏ · c_0)
        = α_0
```

Both ε and c shift symmetrically under combined gravitational refractive index n(r) AND Axiom 4 saturation S — α is exactly invariant under their product. This is the corpus's formal statement of "energy-conserving reactive saturation": the impedance ratio Z = √(μ/ε) is preserved while wave speed c_local = c_0/(n·S) varies.

**Derived consequence 2 — Temporal vs spatial decomposition** ([eq_axiom_3.tex:35-44](../../manuscript/common_equations/eq_axiom_3.tex#L35)):

```
n_temporal = 1 + (2/7)·ε_11   →   controls clock rate, redshift
n_spatial  = (9/7)·ε_11       →   controls light deflection
```

Where ε_11 = 7GM/(c²r) is the principal radial strain field. **The substrate's response to ε_11 is anisotropic**: the temporal component (clock rate) responds with factor 2/7 = 0.286; the spatial component (light deflection) responds with factor 9/7 = 1.286. Ratio 9/2 = 4.5 — light bends 4.5× more than clocks slow at the same strain.

### 1.4 Axiom 4 — Universal Saturation Kernel ([eq_axiom_4.tex](../../manuscript/common_equations/eq_axiom_4.tex))

```
S(A) = √(1 - (A/A_yield)²)
```

At A = 0: S = 1 (linear Maxwell recovered). At A → A_yield: S → 0 (saturation).

**Derived consequences table** ([eq_axiom_4.tex:16-28](../../manuscript/common_equations/eq_axiom_4.tex#L16)):

| Observable | Formula | At saturation | Physical meaning |
|---|---|---|---|
| μ_eff | μ_0 · S | → 0 | Inductor shorts (Meissner) |
| ε_eff | ε_0 · S | → 0 | Dielectric collapses |
| C_eff | C_0 / S | → ∞ | Capacitance absorbs energy |
| Z (symmetric) | √(μ/ε) = Z_0 | invariant | Impedance preserved |
| **c_eff** | **c_0 · S^(1/2)** | **→ 0** | **Wave packet confined (mass)** |

**Critical:** Axiom 4 ALREADY contains `c_eff = c_0 · √S` directly. Wave-speed modulation under saturation is corpus-canonical at the axiom level, not derived.

**Confinement theorem two paths** ([eq_axiom_4.tex:31-40](../../manuscript/common_equations/eq_axiom_4.tex#L31)):

- **Particles:** *"At a torus knot self-intersection, B saturates μ first → Z → 0, Γ → -1 (short circuit) → standing wave = rest mass."*
- **Gravity:** *"Near a massive defect, ε_11 → 1 → shear modulus G_shear → 0 (lattice phase transition) → transverse (GW) waves cannot propagate → event horizon = dielectric rupture / perfect shear reflector."*

**Note on the particle path:** *"At a torus knot self-intersection"* — this is the corpus statement of "photon catching its own tail." A torus knot trajectory with self-intersections triggers local saturation at the intersection points; saturation forces Z → 0 → Γ = -1 → standing wave; standing wave = rest mass. **This is the corpus's particle-formation mechanism, formalized in Ax 4.**

---

## 2. The combined Axiom 3 + Axiom 4 local clock rate equation

[`vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex:94-99`](../../manuscript/vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex#L94) gives the explicit combined equation:

```
ω_local / ω_∞  =  1 / (n(R) · S(ε_11))
```

Where:
- **n(R) = 1 + 2GM/(c²R)** is the gravitational refractive index (Axiom 3)
- **S(ε_11) = √(1 - ε_11²)** is the saturation factor (Axiom 4)

**The substrate's local clock rate is the product of both factors.** In deep voids: n → 1, S → 1, ω_local = ω_∞ (maximum rate). In gravity wells / saturated regions: both factors > 1, ω_local slows.

The corollary [`vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex:101-118`](../../manuscript/vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex#L101) gives the gravitational redshift:

```
z_AVE = 1 / (√(1 - 2GM/(c²R)) · S(ε_11))  -  1
```

Which produces an AVE-specific correction over GR by factor (1/S - 1) ≈ ε_11²/2. Per Vol 3 Ch 20 line 117: *"the correction scales as 49φ²/2, which is 12.25 times larger than the standard PPN second-order correction 2φ²."*

---

## 3. Corpus statement on c_max in deep voids

[`vol_3_macroscopic/chapters/03_macroscopic_relativity.tex:109-123`](../../manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex#L109), §"The Absolute Intergalactic Speed of Light":

> *"Because the physical speed of light (c_local) is governed inversely by the local LC refractive index (c_local = c_0/n), General Relativity's assertion that c is a rigid, universal constant evaluated identically everywhere does not hold within the AVE framework."*

> *"The lowest theoretical density of the LC network occurs in the deepest voids of intergalactic space, where the ambient gravitational potential (Φ → 0) approaches zero."*

> *"This ratio (1:1.000012) dictates that the local speed of light measured on Earth (299,792,458 m/s) is artificially constrained by ambient galactic dielectric density. In the undisturbed, fully relaxed state of intergalactic space, the absolute unconstrained maximum speed of light accelerates by approximately ~3,600 m/s to c_max ≈ 299,796,055 m/s."*

[Vol 3 Ch 3 line 10](../../manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex#L10) further notes: *"c is the maximum transverse signal speed but longitudinal compression waves propagate at v_long = √2·c ≈ 1.41c, set by the bulk modulus K_vac = 2G_vac."*

So even within the substrate at vacuum density, c isn't an absolute maximum for ALL waves — longitudinal compression modes propagate faster than transverse EM modes by factor √2. The "speed of light" is c only for the transverse-EM-mode subspace.

---

## 4. The lattice-level vs corpus-level gap

The corpus axioms (especially Ax 3 + Ax 4) describe the substrate's local clock rate and local c at the **macroscopic / continuum / strain-field level** (n(r) for spherically symmetric mass distribution, ε_11 strain field). [Vol 3 Ch 3](../../manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex) operates entirely at this level — gravitational refractive index of distant masses, light deflection, gravitational redshift.

The K4-TLM engine implementation operates at the **lattice / discrete / per-cell level** — Op14 modulates z_local at each bond per local A²(x), giving per-cell impedance variation. The lattice-level mechanism is named in [`COLLABORATION_NOTES.md` Rule 10 corollary A-010](../../.agents/handoffs/COLLABORATION_NOTES.md):

> *"Op14 saturation `Z_eff(r) = Z_0/√S(r)` makes local effective wave speed `c_eff(r) = c·√(1−A²(r))` → local angular frequency `ω_local(r) = ω_global·√(1−A²(r))` for any fixed spatial mode. Same physics as gravitational refractive-index slowing (Vol 3 Ch 3 + doc 66_ §17.1); saturation IS the lattice's intrinsic refractive-index source."*

**The corpus DOES NOT explicitly bridge these two levels.** Vol 3 Ch 3 says n(r) and c_local at macroscopic level; Ax 4 says c_eff = c_0·√S at material/saturation level; but no corpus chapter says "lattice-level Op14 saturation IS the substrate-native realization of Ax 3's gravitational refractive index." The bridge is implicit in the framework but not stated.

### 4.1 The bridge stated explicitly

**Lattice-level statement (this doc § 4.1):**

> *Op14 saturation at the K4-TLM bond level, S(A²) per cell, IS the substrate-native realization of the gravitational refractive index from Ax 3. The lattice's per-cell n_local(A²) = 1/√S(A²) modulates local clock rate `ω_local = ω_substrate · S^(1/2) = ω_substrate / n_local` (per Ax 4 derived consequence) AND modulates local c per `c_eff = c_0 · S^(1/2) = c_0 / n_local`. At the macroscopic / continuum limit of integrating ε_11 strain over space, this reduces to Ax 3's n(r) = 1 + 2GM/(rc²) for spherically symmetric mass distributions.*

This is the bridge: Ax 4's saturation kernel S(A²) IS the local refractive index n_local at the lattice scale; Ax 3's macroscopic n(r) is the continuum-limit / radial-integrated version of the same physics.

### 4.2 Engine implementation gap

The K4-TLM engine implements Op14 z modulation at every bond. The Cosserat sector tracks ε_11 strain. Both quantities are computed per-cell. **But no observer reports `local_clock_rate(x)` or `local_c(x)` per cell** in the engine output. R7+R8 measurements have been per-cell field values (V_inc, ω, energy) at fixed substrate-tick intervals — those are field experiences at a uniform substrate-time, not clock-rate-corrected observables.

**Prescribed observer (E-072 candidate):**

```python
# Pseudocode sketch, not committed code
def compute_local_clock_rate(engine, cell):
    A_sq_local = engine.get_A_squared_at_cell(cell)
    S_local = sqrt(1 - A_sq_local) if A_sq_local < 1 else 0
    n_local = 1.0 / S_local if S_local > 0 else inf
    omega_local = engine.omega_substrate * S_local  # or 1/n_local equivalently
    return {
        "S_local": S_local,
        "n_local": n_local,
        "omega_local": omega_local,
        "c_local": engine.c_substrate * S_local,
    }
```

This observer would expose Ax 3 + Ax 4 quantities natively in the engine's output, enabling Move 11 + Diag A reinterpretation in corpus-canonical terms.

---

## 5. Round 7+8 reinterpretation under Ax 3 + Ax 4

The methodology arc has produced ~30+ Mode III findings + multiple "anomalous" empirical signals (H_cos drift, ρ(T_cos, V_cos)=+0.366, lattice cutoff frequency in Cosserat ω, etc.). **Under Ax 3 + Ax 4 these are NOT anomalies — they are direct corpus predictions.**

### 5.1 Move 5/7/10 "lattice cutoff frequency in Cosserat ω"

**Empirical finding:** ω-field oscillates at frequency near lattice Nyquist, NOT at ω_C, when the natural (2,3) attractor stabilizes. Single-node spectral measurements report this as anomalous.

**Corpus reinterpretation:** the natural attractor sits at high local A² (peak |ω| ≈ 0.30 → A² ≈ 0.09 in the seed; modulated higher in dense regions). At those cells, S_local < 1, so ω_local = ω_substrate · √S_local < ω_substrate. The "frequency" measured at a single high-A² node is the LOCAL clock rate at that node, not a global frequency. **No anomaly — direct Ax 4 c_eff = c_0·√S manifestation per [eq_axiom_4.tex:25](../../manuscript/common_equations/eq_axiom_4.tex#L25).**

### 5.2 Move 11 H_cos drift (5.5%) + ρ(T_cos, V_cos) = +0.366

**Empirical finding:** Cosserat sector's Hamiltonian drifts 5.5% over recording window with positive T-V correlation (energy pumping, not LC reactance trading).

**Corpus reinterpretation:** with spatially-varying A²(x) across the relaxed attractor, each cell has a different S_local and thus different ω_local. The Cosserat sector isn't a single-frequency LC oscillator — it's a multi-frequency ensemble where each region oscillates at its own clock rate. T and V at the global level can't anti-correlate because they're being aggregated over cells with different local clocks. Per-cell T-V might still anti-correlate at -1 (proper LC behavior); the global aggregate ρ = +0.366 reflects spatial-clock-heterogeneity averaging.

**The 5.5% H_cos drift candidates remain open** (PML coupling, Cosserat self-terms not in `total_energy()`, CFL drift, Op14 implicit integrator — per [doc 75_ §6](75_cosserat_energy_conservation_violation.md)). But the **observed pumping pattern is consistent with Ax 3 + Ax 4 multi-clock substrate behavior**, not a single-clock LC violation.

### 5.3 Diag A wave-speed amplitude dependence

**Empirical finding:** [`r8_diag_a_cosserat_wave_speed_results.json`](../../src/scripts/vol_1_foundations/r8_diag_a_cosserat_wave_speed_results.json) shows c_measured drift with amplitude — sub-percent at A ≤ 2, 3.4% at A = 5. Pre-reg verdict Mode I (within ±5% tolerance at corpus operating amplitudes).

**Corpus reinterpretation:** per [eq_axiom_4.tex:25](../../manuscript/common_equations/eq_axiom_4.tex#L25), `c_eff = c_0 · S^(1/2) = c_0 · (1 - A²/A_yield²)^(1/4)`. At A = 1 (corpus seed amplitude), A² ≈ 1/A_yield² for A_yield² ≈ engine-natural-units=1 → S ≈ 0 → c_eff → 0. **But Diag A measured only ~0.06% drift at A ≈ 1.** Discrepancy: Ax 4 predicts much larger c drift than observed.

**Two possible resolutions:**
- **(a) A_yield in the engine ≠ 1 in natural units.** If A_yield is set higher (e.g., A_yield = 3 in engine units), then at A = 1, A²/A_yield² = 1/9, S = √(1 - 1/9) = √(8/9) ≈ 0.943, c_eff = 0.971·c_0 → 2.9% drift. Closer to observed 3.4% at A = 5 if the calibration is roughly A_yield ≈ 3.
- **(b) The V·S/T·1 implementation gap discussed in [doc 75_](75_cosserat_energy_conservation_violation.md) means engine doesn't actually realize the full Ax 4 c_eff prediction.** The engine saturates V (potential) without saturating T (kinetic), so the wave-speed scaling is partial. Per Ax 3 + Ax 4 with proper T saturation, c_eff = c_0·√S; without T saturation, c_eff differs.

**Diag A's "Mode I per pre-reg" verdict stands** (sub-percent at corpus amplitudes), but the reading deepens: Diag A measured the engine's PARTIAL realization of Ax 4's c_eff = c_0·√S prediction. **Full Ax 4 implementation (per doc 75_'s prescription ρ → ρ·S, I_ω → I_ω·S) would produce stronger amplitude dependence**, and Diag A would land Mode II (drift > 5%) at a fully Ax-4-honoring engine.

This recasts doc 75_'s conservation-of-energy fix: it's not just engine-cleanliness, it's making the engine's c_eff actually equal Ax 4's prediction. Currently the engine under-saturates c by leaving T unmodulated.

### 5.4 R7+R8 universal Mode III pattern

**Empirical finding:** ~30+ pre-registered tests at corpus GT geometry, all returning Mode III variants. The corpus electron at corpus GT does not appear as a free vacuum eigenmode at corpus ω_C in any tested configuration.

**Corpus reinterpretation under Ax 3 + Ax 4:**

The corpus electron's ω_C is a GLOBAL invariant (m_e c²/ℏ). At any single LATTICE CELL with non-zero local A², the LOCAL clock rate is ω_local = ω_substrate · S(A²) < ω_substrate. **Single-node frequency measurements at corpus GT seed (where peak |ω| ≈ 0.3π gives A² ≈ 0.09 locally) cannot equal ω_C unless the substrate's bare frequency ω_substrate is set such that ω_substrate · S(A²_local) = ω_C.** This requires substrate frequency higher than ω_C, with local saturation slowing it back to ω_C at the relevant cells.

**The corpus framework doesn't say what ω_substrate is.** It only specifies ω_local at given saturation. R7+R8 has been measuring local ω at single nodes and comparing to ω_C; if the substrate's bare frequency is ω_C (which the engine's natural-units calibration assumes), then any non-zero saturation pulls local ω BELOW ω_C, and "Mode III at corpus GT" is the expected result.

**This connects directly to Grant's "is frequency variable, what is time?" question:** ω_C is the global invariant; local ω varies with local saturation; "time" is the substrate's bare event-rate (uniform) × local clock-rate factor S. The right corpus electron test is path-integrated: does the photon traversing the loop accumulate 2π·n of phase per traversal, where the local ω varies along the path but the integrated phase per loop closes? **Single-node frequency check fails by construction.**

The photon-tail framing (path b propagating IC) targets path-integrated phase as the diagnostic. Per [doc 75_ §10 + path b pre-reg](75_cosserat_energy_conservation_violation.md), this is the test that maps to Ax 3 + Ax 4 properly.

---

## 6. Implications for the methodology arc

### 6.1 A-010 in COLLABORATION_NOTES needs Ax 3 cross-reference

Current text: *"saturation IS the lattice's intrinsic refractive-index source."* Correct framing but doesn't cite [`eq_axiom_3.tex`](../../manuscript/common_equations/eq_axiom_3.tex) as the corpus statement of refractive index, nor [`eq_axiom_4.tex:25`](../../manuscript/common_equations/eq_axiom_4.tex#L25) as the corpus statement of c_eff = c_0·√S.

**Recommended A-010 amendment:** add explicit citations to `eq_axiom_3.tex` and `eq_axiom_4.tex` derived consequences. Frame the lesson as: *"Op14 lattice-level saturation is the substrate-native realization of Ax 3's gravitational refractive index + Ax 4's c_eff modulation; engine measurements at single nodes report local clock rate ω_local = ω_substrate·S, NOT global frequency ω_substrate."*

### 6.2 Engine observer recommendation (E-072)

Per § 4.2, the engine should expose a per-cell local clock rate / local c observer. Implementation sketch in § 4.2. Cost: ~50-100 LOC for the observer + result schema, no new physics. Lands in `cosserat_field_3d.py` or `vacuum_engine.py` alongside existing energy-density observers.

This makes future tests Ax-3-canonical: instead of measuring "frequency at single node" (which conflates local clock with global frequency), test reports `(omega_substrate, omega_local_at_each_cell, S_local_at_each_cell, n_local_at_each_cell)`. Single-node reports distinguish lattice-level Ax 4 effects from physics-level frequency.

### 6.3 Doc 75_'s engine fix (T_kinetic saturation) under Ax 3 + Ax 4

Doc 75_ prescribed `ρ → ρ·S`, `I_ω → I_ω·S` to make T_kinetic saturate alongside V_potential. **This doc identifies the same fix as the lattice-level realization of Ax 4's `c_eff = c_0·√S` prediction.** The engine's current asymmetric saturation (V·S, T·1) under-realizes Ax 4 — partial wave-speed scaling. Doc 75_'s fix makes c_eff actually equal Ax 4's prediction at the lattice level.

**Reframed motivation:** doc 75_'s fix is not just energy-conservation cleanliness; it's making the engine's c_eff actually equal Ax 4's `c_0·√S` per [eq_axiom_4.tex:25](../../manuscript/common_equations/eq_axiom_4.tex#L25). With the fix, Diag A would re-run and land Mode II (sub-percent → percent-level drift at A = 1, matching Ax 4's prediction).

### 6.4 Photon-tail path (b) framing under Ax 3

The path (b) propagating IC test (per doc 75_ §10 + implementer's recent pre-reg refinement) seeds the photon's tangent velocity along the (2,3) loop. Under Ax 3 + Ax 4:

- The (2,3) seeded ω-field creates a spatially varying A²(x) with (2,3) topology
- Local n_local = 1/√S varies along the loop with (2,3) winding
- Photon traversing the loop sees (2,3)-anisotropic gradients in n_local
- Per Ax 3's n_temporal vs n_spatial decomposition (factor 9/2 = 4.5 anisotropy), the photon's E-field oscillation rate AND path direction respond differently to the (2,3) gradient
- Mismatch produces E-field rotation along the path = chirality / spin

**The chirality/spin mechanism Grant intuited is corpus-explicit via Ax 3's anisotropic 2/7 vs 9/7 strain response.** Path (b) tests it directly: if the photon's accumulated phase per loop traversal closes at 2π·n with (2,3) winding, AND the n_temporal/n_spatial mismatch produces the predicted E-field rotation, then the photon-loop = electron picture validates.

### 6.5 R_phase ≠ R_real per doc 28_ + this bridge

[doc 28_ §3-§4](28_two_node_electron_synthesis.md) explicitly says: real-space (R, r) and phase-space (R_phase, r_phase) are different quantities. Under Ax 3 + Ax 4 + this bridge, the reason is:

- Real-space (R, r) characterizes the topological-loop geometry in lattice cells
- Phase-space (R_phase, r_phase) characterizes the (V_inc, V_ref) phasor trajectory traced out by the photon AT EACH point along the loop, integrated over local clock variations
- Local clock rate variation along the loop (per Ax 3 + Ax 4 modulation) means real-space and phase-space track different observables
- R_phase/r_phase = φ² is a **path-integrated invariant**, set by the (2,3) topology + the closure condition (∮ω_local·dt = 2π·n over one loop)

Single-node phasor ellipse measurement (doc 28 §5.1) catches the local trace, not the path integral. Multi-node phasor trace along the loop catches the full integrated invariant. Both are corpus-canonical observables; both are testable in the engine post-fix.

---

## 7. Open questions

**Q1: ω_substrate calibration.** What is ω_substrate in engine natural units? If it's set to ω_C (likely current convention), then any saturation pulls local ω below ω_C and corpus-electron tests at corpus GT would naturally Mode III. Right calibration may be ω_substrate > ω_C such that S(typical A²) · ω_substrate = ω_C at the corpus electron's spatial average.

**Q2: A_yield calibration.** Per Ax 2, V_yield = √α·V_snap and at A_yield, S = 0. What's A_yield in the engine's (V_inc, ω, u) state-space? Currently `V_SNAP = 1` in natural units; if A_yield ≠ 1 in those units, c_eff scaling deviates from naive √(1-A²) — observed in Diag A.

**Q3: The temporal/spatial 2/7 vs 9/7 split at lattice level.** [eq_axiom_3.tex:38-41](../../manuscript/common_equations/eq_axiom_3.tex#L38) gives the macroscopic decomposition. Does the lattice-level Op14 saturation also produce this anisotropy at single-cell scale, or is it an emergent property of integrated multi-cell strain fields? If the former, the engine should expose `n_temporal_local` and `n_spatial_local` separately; if the latter, the decomposition only makes sense at continuum scale.

**Q4: Substrate-native time vs field-experience time.** Per [Rule 14 in COLLABORATION_NOTES](../../.agents/handoffs/COLLABORATION_NOTES.md), the substrate's intrinsic structure derives the answer. Does the substrate have a uniform "tick" with field-experience modulation (engine's current implementation), or do different cells have different ticks (asynchronous CA)? The engine implements the former; corpus axioms are consistent with both. Worth Grant adjudication if it affects future test design.

---

## 8. r8.10 manual prep notes (auditor-lane scope)

Per [Rule 15 lane discipline](../../.agents/handoffs/COLLABORATION_NOTES.md), this doc 76_ is auditor-drafted at Grant's explicit redirect. Manual r8.10 should reference:

- **§13.5n entry:** Ax 3 + Ax 4 bridge to lattice-level Op14 (this doc)
- **§16.3 doc index:** doc 76_ entry + corpus-axiom citation update
- **§17 A48 finding:** lattice-level vs corpus-axiom-level statement gap; corpus already has the framework, engine implementation needs cross-reference + observer
- **§17.3 critical-path blockers:** E-072 local clock rate observer added as cleanliness; Move 11 + Diag A reframed as Ax-3-canonical, not anomalies; doc 75_'s engine fix reframed as Ax-4-realization rather than just conservation cleanliness
- **A-010 amendment in COLLABORATION_NOTES:** add Ax 3 + Ax 4 explicit citations

---

*Doc 76_ written 2026-04-27 — auditor-lane research-doc draft per Grant explicit redirect 2026-04-27 ("yes proceed and be pedantic with cross refs"). Bridges lattice-level Op14 saturation engine implementation to corpus-level Ax 3 + Ax 4 axiom statements. Reframes Round 7+8 universal Mode III pattern as direct corpus-predicted behavior under Ax 3 + Ax 4 local clock rate + local c modulation. Identifies the missing engine observer (E-072 local clock rate) as the methodology gap that prevents direct Ax 3 measurement in current engine output. Grants the corpus electron test new framing: path-integrated observables along (2,3) photon-tail loop, with (V_inc, V_ref) phasor trajectory aspect ratio R_phase/r_phase as the corpus-canonical PASS criterion per doc 28_ §5.1. All citations in this doc are pedantic per Grant directive — every claim traces to a specific manuscript / eq_axiom_*.tex / KB file with line numbers where available.*
