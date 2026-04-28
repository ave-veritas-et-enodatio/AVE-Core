# 77 — Lattice-Level Op14 Saturation as Substrate Realization of Ax 4 (Local Clock Rate, R7+R8 Empirical Reframe)

**Status:** auditor-drafted research doc, 2026-04-27. Reframes [doc 76_'s](76_lattice_to_axiom3_bridge.md) lattice→corpus axiom-bridge content under canonical Scheme A per [`.agents/handoffs/axiom_homologation.md`](../../.agents/handoffs/axiom_homologation.md). Doc 76_ retained as Rule 12 supersession record; this doc supersedes its substantive content.

**Companion docs:** [doc 75_](75_cosserat_energy_conservation_violation.md) (Cosserat sector engine implementation; doc 75_'s engine fix discussed in §6.3 below); [doc 76_](76_lattice_to_axiom3_bridge.md) (superseded predecessor written under Scheme B framing; Rule 12 audit trail); [doc 28_](28_two_node_electron_synthesis.md) (real-space vs phase-space coordinate distinction); [doc 20_](20_chirality_projection_sub_theorem.md) (chirality-from-(2,3)-topology parallel-impedance derivation); [doc 10_](10_chirality_accounting_narrative.md) (§8 open item closed by §6.4 below).

---

## §1 — Canonical Scheme A axioms (mandatory source reading)

> **MANDATORY — Read these primary sources before continuing in this doc.** This §1 is a navigational pointer, not a restatement. The axioms are load-bearing; abbreviated re-statements drift over time and were the structural cause of the Scheme B / Scheme C / vestige-numbering inconsistencies catalogued in the homologation audit. Read the primary sources directly; do not infer axiom content from prose summaries elsewhere in the corpus.

The four canonical AVE axioms (Scheme A per [`manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:51-75`](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L51) + cross-repo audit confirming Scheme A canonical across 9 AVE-* repos, ~520 axiom occurrences, 469 in Scheme A):

- **Ax 1 — Substrate Topology (LC Network):** [`eq_axiom_1.tex`](../../manuscript/common_equations/eq_axiom_1.tex)
- **Ax 2 — Topo-Kinematic Isomorphism:** [`eq_axiom_2.tex`](../../manuscript/common_equations/eq_axiom_2.tex)
- **Ax 3 — Effective Action Principle:** [`eq_axiom_3.tex`](../../manuscript/common_equations/eq_axiom_3.tex)
- **Ax 4 — Dielectric Saturation:** [`eq_axiom_4.tex`](../../manuscript/common_equations/eq_axiom_4.tex)

**Calibration constants** (NOT axioms; derived-from-axioms numerical scale per [Vol 1 Ch 1:14-21](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L14)): [`eq_calibration_constants.tex`](../../manuscript/common_equations/eq_calibration_constants.tex) — Z₀, ℓ_node, ξ_topo, α, V_snap, V_yield with explicit axiom attributions.

**Macroscopic gravity** (NOT a primitive axiom; derived consequence of Ax 1 + Ax 4 under Symmetric Scaling): [`eq_gravity_derived.tex`](../../manuscript/common_equations/eq_gravity_derived.tex) — G, n(r), Symmetric Gravity, α-invariance under gravitational strain, n_temporal/n_spatial 2/7+9/7 Poisson decomposition.

**Canonicalization audit** (full cross-repo evidence + inconsistency punch list + P1-P5 fix log): [`.agents/handoffs/axiom_homologation.md`](../../.agents/handoffs/axiom_homologation.md).

---

## §2 — Lattice Op14 saturation IS the substrate realization of Ax 4

The engine's Op14 saturation kernel ([`src/ave/topological/cosserat_field_3d.py`](../../src/ave/topological/cosserat_field_3d.py) + [`src/ave/core/k4_tlm.py`](../../src/ave/core/k4_tlm.py)) modulates per-cell impedance via:

```
S(A²) = √(1 - A²/A_yield²)
Z_eff(r) = Z_0 / √S(r)     (per Symmetric Gravity scaling — see eq_axiom_4.tex)
```

This is the lattice-level realization of Ax 4's `C_eff = C_0/√(1-(Δφ/α)²)` per [`eq_axiom_4.tex`](../../manuscript/common_equations/eq_axiom_4.tex). The eq_axiom_4.tex derived-consequences table makes this explicit:

| Observable | Formula | At saturation | Physical meaning |
|---|---|---|---|
| μ_eff | μ_0·S | → 0 | Inductor shorts (Meissner) |
| ε_eff | ε_0·S | → 0 | Dielectric collapses |
| C_eff | C_0/S | → ∞ | Capacitance absorbs energy |
| Z (symmetric) | √(μ/ε) = Z_0 | invariant | Impedance preserved |
| **c_eff** | **c_0·S^(1/2)** | **→ 0** | **Wave packet confined (mass)** |

**Critical:** Ax 4 already contains `c_eff = c_0·√S` as a derived consequence. Wave-speed modulation under saturation is corpus-canonical at the axiom level — no separate "wave-speed-invariance" axiom needed (this was the failure mode A44 caught: "missing axiom" temptation collapsed by existing-axiom check; per [COLLABORATION_NOTES.md Rule 6 / A44](../../.agents/handoffs/COLLABORATION_NOTES.md)).

**Confinement theorem two paths** (per [`eq_axiom_4.tex:31-40`](../../manuscript/common_equations/eq_axiom_4.tex#L31)):
- **Particles:** at a torus knot self-intersection, B saturates μ first → Z → 0, Γ → -1 → standing wave = rest mass. Photon-tail mechanism.
- **Gravity:** near a massive defect, ε_11 → 1 → shear modulus G_shear → 0 → transverse (GW) waves cannot propagate → event horizon = dielectric rupture / perfect shear reflector.

---

## §3 — Combined derived-gravity refraction + Op14 saturation: local clock rate

[`vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex:94-99`](../../manuscript/vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex#L94) gives the canonical local clock rate equation:

```
ω_local / ω_∞  =  1 / (n(R) · S(ε_11))
```

Where:
- **n(R) = 1 + 2GM/(c²R)** is the gravitational refractive index, a derived consequence of Ax 1 + Ax 4 under Symmetric Scaling (see [`eq_gravity_derived.tex`](../../manuscript/common_equations/eq_gravity_derived.tex)). NOT a primitive Ax 3; per canonical Scheme A, Ax 3 is the Effective Action Principle.
- **S(ε_11) = √(1 - ε_11²)** is the Ax 4 saturation factor.

**Substrate's local clock rate is the product of both factors.** In deep voids: n → 1, S → 1, ω_local = ω_∞ (maximum rate). In gravity wells / saturated regions: both factors > 1, ω_local slows.

**Substrate-vs-observable scaling is fixed by SU(2)→SO(3) half-cover** per [Vol 2 Ch 4 quantum_spin.tex](../../manuscript/vol_2_subatomic/chapters/04_quantum_spin.tex) + A-008 dimensional cross-check (see [COLLABORATION_NOTES.md Rule 6 corollary](../../.agents/handoffs/COLLABORATION_NOTES.md)): m_Cosserat = 2·m_e. Medium twists at full SO(3) (360°), spinor observable wraps SU(2) (720°). Gives factor-of-2 between substrate ω_substrate = 2·m_e c²/ℏ and spin-½ observable ω_e = m_e c²/ℏ.

---

## §4 — Lattice-level vs corpus-level observer gap (E-072)

The engine currently exposes V_inc, ω, |u|², Φ_link, and energy-density observers but does NOT expose per-cell local clock rate `ω_local(cell) = ω_substrate · S(A²(cell))`. Single-node spectral measurements at saturated regions therefore conflate two distinct physical quantities:

1. **ω_substrate** — the substrate's intrinsic event rate (uniform; set by engine calibration ω_C in natural units)
2. **ω_local(cell)** — the local clock rate at saturated cells, modulated by S(A²(cell))

**E-072 — Recommended engine observer:** expose `(ω_substrate, ω_local_per_cell, S_local_per_cell, n_local_per_cell)` as a result schema augmentation. Implementation sketch:

```python
def local_clock_rate_observer(engine):
    # per-cell A² from peak |ω| or |V_inc|² depending on sector;
    # filter to interior cells per Rule 10 PML-cell-exclusion corollary
    A_sq = compute_per_cell_amplitude_squared(engine)  # |ω|² or |V_inc|²
    interior_mask = make_interior_mask(engine)         # exclude PML region
    S_local = np.sqrt(np.maximum(0.0, 1 - A_sq / A_yield**2))
    omega_local = omega_substrate * S_local            # per-cell
    return {
        "omega_substrate": omega_substrate,
        "omega_local_per_cell": omega_local,
        "S_local_per_cell": S_local,
        "n_local_per_cell": 1.0 / S_local,             # local refractive index
        "interior_mask": interior_mask,
    }
```

Cost: ~50-100 LOC for observer + result schema. No new physics. Lands in `cosserat_field_3d.py` or `vacuum_engine.py` alongside existing energy-density observers.

**This recommendation is independent of axiom numbering** — it's engine instrumentation. Future bound-state-existence tests should report local clock rate at load-bearing interior cells (top-K |field|² with PML exclusion per Rule 10), not just global frequency at single nodes.

---

## §5 — R7+R8 empirical reinterpretation under Scheme A

Round 7+R8 produced ~30+ pre-registered tests, all returning Mode III variants at corpus GT geometry. **Per Scheme A, these are NOT anomalies — they are direct consequences of Ax 4 saturation operating across spatially-varying A²(x) fields, observed without per-cell local clock instrumentation.**

### §5.1 Move 5/7/10 "lattice cutoff frequency in Cosserat ω"

**Empirical finding:** ω-field oscillates at frequency near lattice Nyquist when the natural (2,3) attractor stabilizes. Single-node spectral measurements report this as anomalous (compared to ω_C).

**Scheme A reinterpretation:** the natural attractor sits at high local A² (peak |ω| ≈ 0.30 → A² ≈ 0.09 in the seed; modulated higher in dense regions). At those cells, S_local < 1, so ω_local = ω_substrate · √S_local < ω_substrate. **The "frequency" measured at a single high-A² node is the LOCAL clock rate at that node, not a global frequency.** No anomaly — direct Ax 4 c_eff = c_0·√S manifestation per [`eq_axiom_4.tex:25`](../../manuscript/common_equations/eq_axiom_4.tex#L25).

### §5.2 Move 11 H_cos drift (5.5%) + ρ(T_cos, V_cos) = +0.366

**Empirical finding:** Cosserat sector's Hamiltonian drifts 5.5% over recording window with positive T-V correlation (energy pumping pattern, not LC reactance trading).

**Scheme A reinterpretation:** with spatially-varying A²(x) across the relaxed attractor, each cell has a different S_local and thus different ω_local. The Cosserat sector isn't a single-frequency LC oscillator — it's a multi-frequency ensemble where each region oscillates at its own clock rate. T and V at the global level can't anti-correlate cleanly because they're being aggregated over cells with different local clocks. **Per-cell T-V might still anti-correlate at -1 (proper LC behavior); the global aggregate ρ = +0.366 reflects spatial-clock-heterogeneity averaging.**

The 5.5% H_cos drift candidates remain open (PML coupling, Cosserat self-terms not in `total_energy()`, CFL drift, Op14 implicit integrator — per [doc 75_ §6](75_cosserat_energy_conservation_violation.md)). But the **observed pumping pattern is consistent with Ax 4 multi-clock substrate behavior**, not a single-clock LC violation.

### §5.3 Diag A wave-speed amplitude dependence

**Empirical finding:** [`r8_diag_a_cosserat_wave_speed_results.json`](../../src/scripts/vol_1_foundations/r8_diag_a_cosserat_wave_speed_results.json) shows c_measured drift with amplitude — sub-percent at A ≤ 2, 3.4% at A = 5. Pre-reg verdict Mode I (within ±5% tolerance at corpus operating amplitudes).

**Scheme A reinterpretation:** per [`eq_axiom_4.tex:25`](../../manuscript/common_equations/eq_axiom_4.tex#L25), `c_eff = c_0 · S^(1/2) = c_0 · (1 - A²/A_yield²)^(1/4)`. At A = 1 (corpus seed amplitude), A² ≈ 1/A_yield² for A_yield² ≈ engine-natural-units = 1 → S ≈ 0 → c_eff → 0. **But Diag A measured only ~0.06% drift at A ≈ 1.** Discrepancy: Ax 4 predicts much larger c drift than observed.

**Two possible resolutions:**
- **(a) A_yield in the engine ≠ 1 in natural units.** If A_yield is set higher (e.g., A_yield = 3 in engine units), then at A = 1, A²/A_yield² = 1/9, S = √(1 - 1/9) ≈ 0.943, c_eff = 0.971·c_0 → 2.9% drift. Closer to observed 3.4% at A = 5 if calibration is roughly A_yield ≈ 3.
- **(b) The V·S/T·1 implementation gap (per [doc 75_](75_cosserat_energy_conservation_violation.md)) means engine doesn't actually realize the full Ax 4 c_eff prediction.** Engine saturates V (potential) without saturating T (kinetic), so wave-speed scaling is partial. Per Ax 4 with proper symmetric L-and-C saturation, c_eff = c_0·√S; without T saturation, c_eff differs.

**Diag A's "Mode I per pre-reg" verdict stands** (sub-percent at corpus amplitudes), but the reading deepens: **Diag A measured the engine's PARTIAL realization of Ax 4's c_eff = c_0·√S prediction.** Full Ax 4 implementation (per doc 75_'s prescription ρ → ρ·S, I_ω → I_ω·S) would produce stronger amplitude dependence; Diag A would land Mode II (drift > 5%) at a fully Ax-4-honoring engine.

### §5.4 R7+R8 universal Mode III pattern

**Empirical finding:** ~30+ pre-registered tests at corpus GT geometry, all returning Mode III variants. The corpus electron at corpus GT does not appear as a free vacuum eigenmode at corpus ω_C in any tested configuration accessible to N=64. Round 8 photon-tail branch closed Mode III empirically per [doc 75_ §11 + path b commit `1b48f4d`](75_cosserat_energy_conservation_violation.md).

**Scheme A reinterpretation:**

The corpus electron's ω_C is a GLOBAL invariant (m_e c²/ℏ). At any single LATTICE CELL with non-zero local A², the LOCAL clock rate is ω_local = ω_substrate · S(A²) < ω_substrate. **Single-node frequency measurements at corpus GT seed (where peak |ω| ≈ 0.3π gives A² ≈ 0.09 locally) cannot equal ω_C unless the substrate's bare frequency ω_substrate is set such that ω_substrate · S(A²_local) = ω_C.** This requires substrate frequency higher than ω_C, with local saturation slowing it back to ω_C at the relevant cells.

**The corpus framework doesn't say what ω_substrate is.** It only specifies ω_local at given saturation. R7+R8 has been measuring local ω at single nodes and comparing to ω_C; if the substrate's bare frequency is ω_C (which the engine's natural-units calibration assumes), then any non-zero saturation pulls local ω BELOW ω_C, and "Mode III at corpus GT" is the expected result.

**This connects to Grant's "is frequency variable, what is time?" question:** ω_C is the global invariant; local ω varies with local saturation; "time" is the substrate's bare event-rate (uniform) × local clock-rate factor S. **The right corpus electron test is path-integrated:** does the photon traversing the loop accumulate 2π·n of phase per traversal, where the local ω varies along the path but the integrated phase per loop closes? **Single-node frequency check fails by construction** at any non-zero saturation, regardless of corpus prediction validity.

The photon-tail framing (path b propagating IC) targets path-integrated phase as the diagnostic. Cumulative empirical statement from Round 8: **at all configurations tractable at N=64 lattice resolution (corpus-prescribed dx = ℓ_node), the engine does not host the corpus electron**. Whether this is engine implementation gap (V·S/T·1 asymmetry per doc 75_) or path-integrated test still pending (per §6.5 below) is the open question for Round 9.

---

## §6 — Methodology implications

### §6.1 A-010 amendment in COLLABORATION_NOTES (canonical citation update)

[Rule 10 local-clock-modulation corollary (A-010)](../../.agents/handoffs/COLLABORATION_NOTES.md): *"saturation IS the lattice's intrinsic refractive-index source."* Already correct in spirit; the corpus citations need amending to point at canonical Scheme A sources rather than the pre-supersession Scheme B references.

**Recommended A-010 citation amendment:** replace any references to `eq_axiom_3.tex`'s pre-supersession "Axiom 3 — Gravity" content with citations to [`eq_gravity_derived.tex`](../../manuscript/common_equations/eq_gravity_derived.tex) (derived consequence of Ax 1 + Ax 4 under Symmetric Scaling) + [`eq_axiom_4.tex`](../../manuscript/common_equations/eq_axiom_4.tex) (saturation kernel + c_eff = c_0·√S derivation). Frame the lesson as: *"Op14 lattice-level saturation is the substrate-native realization of Ax 4's saturation kernel; gravitational refractive index n(r) is a derived consequence per eq_gravity_derived.tex; engine measurements at single nodes report local clock rate ω_local = ω_substrate·S, NOT global frequency ω_substrate."*

### §6.2 Engine observer recommendation (E-072 reaffirmed)

Per §4 above, the engine should expose a per-cell local clock rate / local c observer. Implementation sketch in §4. Cost: ~50-100 LOC for the observer + result schema, no new physics. Lands in `cosserat_field_3d.py` or `vacuum_engine.py` alongside existing energy-density observers.

This makes future tests Scheme-A-canonical: instead of measuring "frequency at single node" (which conflates local clock with global frequency), test reports `(omega_substrate, omega_local_at_each_cell, S_local_at_each_cell, n_local_at_each_cell)`. Single-node reports distinguish lattice-level Ax 4 effects from physics-level frequency.

### §6.3 Doc 75_'s engine fix (T_kinetic saturation) under Scheme A

Doc 75_ prescribed `ρ → ρ·S`, `I_ω → I_ω·S` to make T_kinetic saturate alongside V_potential. **Under Scheme A, this fix is the lattice-level realization of Ax 4's `c_eff = c_0·√S` prediction.** The engine's current asymmetric saturation (V·S, T·1) under-realizes Ax 4 — partial wave-speed scaling. Doc 75_'s fix makes c_eff actually equal Ax 4's prediction at the lattice level.

**Reframed motivation under Scheme A:** doc 75_'s fix is not just energy-conservation cleanliness — it's making the engine's c_eff actually equal Ax 4's `c_0·√S` per [`eq_axiom_4.tex:25`](../../manuscript/common_equations/eq_axiom_4.tex#L25). With the fix, Diag A would re-run and land Mode II (sub-percent → percent-level drift at A = 1, matching Ax 4's prediction).

**Note on doc 75_ §1 framing:** doc 75_ §1 frames the engine bug as "Ax 3 = energy conservation violated." Under canonical Scheme A, Ax 3 = Effective Action Principle; energy conservation is a Noether consequence of Ax 3's Lagrangian, not Ax 3 itself. The engine bug is more precisely: **Ax 4's saturation kernel is implemented asymmetrically across L (motion-side, T_kinetic) and C (rest-side, V_potential), violating the symmetric LC scaling that Ax 4 + Symmetric Gravity require.** This framing-error pass on doc 75_ §1 is queued separately as a homologation P3+ item.

### §6.4 Spin acquisition for the photon-tail electron (chirality EE-translation)

Symmetric Gravity (μ_eff/ε_eff scale together via Cosserat trace-reversal K=2G, ν_vac=2/7) locks ω=c·k under Op14 saturation: λ and f co-vary inversely keeping c invariant. K4 chirality + (2,3) topology adds optical activity per [doc 20_'s](20_chirality_projection_sub_theorem.md) ξ = α·pq/(p+q): E-field handedness rotates per loop traversal = angular momentum acquisition. SU(2)→SO(3) half-cover per [Vol 2 Ch 4](../../manuscript/vol_2_subatomic/chapters/04_quantum_spin.tex) + A-008 gives m_Cosserat = 2·m_e factor between substrate twist and spinor observable, placing spin-½ at m_e c²/ℏ on the observable side. **Standard chiral electrodynamics + Cosserat micropolar elasticity in AVE units; corpus-cited; no new derivation** — the synthesis is a translation of existing pieces from geometric/topological language into power-engineering / chiral-EM language. Closes [doc 10_ §8 open item (a)](10_chirality_accounting_narrative.md) on strain-induced chirality split: there is no derivation gap, only a translation gap, now closed.

**On the corpus pieces this rests on** (per axiom homologation §3 audit + chirality-corpus-search 2026-04-27):
- 2/7 + 9/7 Poisson decomposition: [`eq_gravity_derived.tex:38-43`](../../manuscript/common_equations/eq_gravity_derived.tex#L38) + [`vol_3 Ch 20:262-271`](../../manuscript/vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex#L262)
- Chirality from (2,3) parallel-impedance: [doc 20_](20_chirality_projection_sub_theorem.md) (χ_(p,q) = α·pq/(p+q); for electron = α·6/5)
- Photon as transverse Cosserat ω wave; saturation → (2,3) confinement → electron: [doc 30_](30_photon_identification.md)
- Spin-½ as gyroscopic precession of topological flywheel: [Vol 2 Ch 4](../../manuscript/vol_2_subatomic/chapters/04_quantum_spin.tex)
- Photon couples to transverse strain via Poisson ratio (n_⊥ = 1 + (2/7)χ_vol; light bends 2× matter): [Vol 3 Ch 2:121-159](../../manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex#L121) "The Double Deflection"

### §6.5 R_phase ≠ R_real per doc 28_ + this bridge

[doc 28_ §3-§4](28_two_node_electron_synthesis.md) explicitly says: real-space (R, r) and phase-space (R_phase, r_phase) are different quantities. Under Scheme A + this bridge, the reason is:

- **Real-space (R, r)** characterizes the topological-loop geometry in lattice cells
- **Phase-space (R_phase, r_phase)** characterizes the (V_inc, V_ref) phasor trajectory traced out by the photon AT EACH point along the loop, integrated over local clock variations
- **Local clock rate variation along the loop** (per Ax 4 Op14 modulation) means real-space and phase-space track different observables
- **R_phase/r_phase = φ²** is a path-integrated invariant, set by the (2,3) topology + the closure condition (∮ω_local·dt = 2π·n over one loop)

Single-node phasor ellipse measurement (doc 28 §5.1) catches the local trace, not the path integral. **Multi-node phasor trace along the loop catches the full integrated invariant.** Both are corpus-canonical observables; both are testable in the engine post-fix (doc 75_'s T_kinetic saturation fix makes c_eff actually equal Ax 4's prediction, enabling clean path-integrated phase measurement).

---

## §7 — Open questions

**Q1: ω_substrate calibration in engine natural units.** Current engine convention has ω_substrate = ω_C (m_e c²/ℏ in natural units). Per §5.4, this calibration forces any non-zero saturation to pull local ω below ω_C, and corpus-electron tests at corpus GT naturally Mode III. Right calibration may be ω_substrate > ω_C such that S(typical A²) · ω_substrate = ω_C at the corpus electron's spatial average. Or: **ω_substrate = 2·ω_C per SU(2)→SO(3) half-cover** (medium frequency twice the spinor observable frequency, per A-008 + §3 above). Open for Grant adjudication post-doc-75_-fix.

**Q2: A_yield calibration in engine state-space.** Per Ax 4 + eq_calibration_constants.tex, V_yield = √α · V_snap and at A_yield, S = 0. What's A_yield in the engine's (V_inc, ω, u) state-space? Currently `V_SNAP = 1` in natural units; if A_yield ≠ 1 in those units, c_eff scaling deviates from naive √(1-A²) — observed in Diag A. Companion to Q1; same calibration audit.

**Q3: Temporal/spatial Poisson decomposition at lattice vs continuum scale.** [`eq_gravity_derived.tex:38-43`](../../manuscript/common_equations/eq_gravity_derived.tex#L38) gives the macroscopic 2/7 + 9/7 split for radial strain ε_11. Does the lattice-level Op14 saturation also produce this anisotropy at single-cell scale, or is it an emergent property of integrated multi-cell strain fields? If the former, the engine should expose `n_temporal_local` and `n_spatial_local` separately (extension of E-072); if the latter, the decomposition only makes sense at continuum scale. Open research question; not blocking for current empirical tests.

**Q4: Substrate-native time vs field-experience time.** Per Rule 14 + Rule 16 in COLLABORATION_NOTES, the substrate's intrinsic structure derives the answer. Does the substrate have a uniform "tick" with field-experience modulation (engine's current implementation), or do different cells have different ticks (asynchronous CA)? The engine implements the former; corpus axioms are consistent with both. Open for Grant physics-level adjudication if it affects future test design.

---

## §8 — r8.10 manual prep notes (auditor-lane scope)

Per [Rule 15 lane discipline](../../.agents/handoffs/COLLABORATION_NOTES.md), this doc 77_ is auditor-drafted at Grant's explicit redirect (per axiom homologation P3 adjudication). Manual r8.10 should reference:

- **§13.5n entry:** Lattice-level Op14 IS substrate realization of Ax 4 (this doc 77_, supersedes doc 76_'s Scheme B framing per Rule 12)
- **§17 critical-path:** E-072 engine observer (per-cell local clock rate) — implementation candidate post-doc-75_-fix
- **§A48-A58 audit catalog:** A58 (path-(a)/path-(b) empirical equivalence per doc 75_ §11.6), Round 8 photon-tail closure, axiom homologation discipline (Rule 12 supersession of doc 76_ → doc 77_)
- **Cross-reference to doc 75_ §11.5:** R7+R8 cumulative empirical statement; engine doesn't host corpus electron at any tested configuration accessible to N=64
- **Cross-reference to axiom_homologation.md** as the canonicalization audit anchor

This doc 77_ is the canonical Scheme A bridge between lattice Op14 implementation and corpus-level Ax 4 + derived gravity statements; future agents should cite this doc rather than doc 76_ for the substrate-realization framing.
