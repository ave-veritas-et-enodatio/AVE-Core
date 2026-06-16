# K4/srs Zone-Edge Nyquist — Empirical Settle of the Two-k_max Corpus Contradiction (PREREG, FROZEN)

**Date:** 2026-06-16
**Status:** FROZEN (bins + discriminator below are locked before the full-range sweep is run/recorded).
**Class (consistency-vs-emergence):** **CONSISTENCY-class** — this settles an internal-corpus
consistency question (which of two corpus-quoted `k_max` values the actual chiral K4/srs lattice
exhibits at the Brillouin zone edge). No CODATA fit, no emergence claim. `ℓ_node` and `c` are imported
from `src/ave/core/constants.py`; the verdict is a dimensionless lattice-geometry ratio
(`k_band-top · ℓ_node`).

---

## §0 The contradiction being settled

The corpus carries TWO different values, both labeled "K4 Nyquist limit / `k_max`", ~5.4× apart,
presented as interchangeable:

- **0.577 / ℓ_node** (= 1/√3) — [`boundary-observables-m-q-j.md:87`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md):
  > "The K4 Nyquist limit $k_{\max} = 0.577 / \ell_{\text{node}}$ does NOT apply to interior structure…"

  This 0.577 originates as the 3D-TLM **network-velocity** factor 1/√3
  (`chiral_lattice_dynamics.py:48` `ANALYTIC_NETWORK_FACTOR`).

- **π / ℓ_node** (≈ 3.14159) — [`paley-wiener-hilbert.md:10`](../manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md):
  > "The maximum spatial frequency the lattice can support without aliasing is the Brillouin boundary: $k_{max} = \pi / \ell_{node}$."

  Also [`ave-analytical-toolkit-index.md:179`](../manuscript/ave-kb/common/ave-analytical-toolkit-index.md):
  > "K4 discrete vs continuum Maxwell — discrete dispersion has Nyquist cutoff at k_max = π/ℓ_node".

  And the analytic closed form `spectral_gap.lattice_dispersion` / `brillouin_zone_edge`
  (`src/ave/axioms/spectral_gap.py:66,102`): `ω(k)=(2c/ℓ)|sin(kℓ/2)|`, edge at `k=π/ℓ`.

These are physically DIFFERENT bounds: a **measured-K4-propagating-mode velocity factor** vs an
**idealized-cubic Brillouin/Nyquist zone edge**. The corpus presents them as the same `k_max`. This
prereg settles, EMPIRICALLY, which (if either) the actual chiral K4/srs lattice exhibits where its
band tops out.

**Downstream consumer:** the verdict feeds Grant's adjudication on which `k_max` binds the
`clm-sjjvhf` interior-Nyquist-exemption argument (`claims.jsonl:239` —
"Interior Eigenmodes of a Bounded Soliton Are Not Lattice-Nyquist-Constrained"; the claim text quotes
the **0.577/ℓ_node** value as the bound that interior modes are exempt from).

**This is NOT a re-litigation of the CLOSED Nyquist-binding route** (`2026-06-11_nyquist-binding-route_CLOSED.md`).
That closure was a narrative/arithmetic demolition of "electron-at-the-cutoff → mass = sampling-rate readout",
anchored to the corpus-quoted `π/ℓ_node` value WITHOUT ever sweeping the extractor to the edge. This is the
empirical-driver (Rule 10) measurement of where the actual band tops out — a distinct, never-run test.

---

## §1 substrate-native-check walk (done before any code)

- **Dynamics:** discrete K4/srs-TLM **scatter + connect** (`chiral_lattice.scalar_tlm_step`,
  the closed orthogonal one-step operator `M = Connect · blockdiag(S)`). NOT Lagrangian, NOT
  gradient-descent, NOT continuum-Helmholtz, NOT energy-basin. **The driver reuses the existing
  `measure_dispersion` loop verbatim — no new solver, no rebuild.**
- **Sector:** scalar/capacitive V-sector (one scalar per port) — the same mode `measure_dispersion`
  already probes at small k. ω(k) is a real-space/spectral observable.
- **Coords (A46):** the test measures ω(k) in real-space lattice wavevector coordinates; the corpus
  `k_max` claims are ALSO real-space lattice wavevector bounds (rad/ℓ_node). **Coordinate match holds**
  — this is NOT a phase-space φ² vs lattice-Cartesian mismatch. Both sides are lattice wavevectors.
- **CP10:** runs CLOSED (no PML, no bulk force) — the scatter+connect loop conserves energy exactly.
  The PML-cell-exclusion corollary does not apply (no PML in this extractor).
- **Saturation:** OFF (linear, A ≪ 1). No Op14 local-clock modulation. The cold-lattice band is the
  object of measurement.

---

## §2 Units (load-bearing — the conversion is the trap)

`measure_dispersion` parameterizes `k = 2π·m / net.box`, where `net.box` is in **Cartesian a_cell
length** and `m` is the commensurate-mode integer. The returned phase velocity is `ω/k` in
(Cartesian-length / step).

The conversion to **rad/ℓ_node** units (the corpus units):

> One NN bond = one ℓ_node by construction (`build_srs_net` default `a_cell = 2√2`, so the srs NN bond
> length `c_link = mean_bond_length(net) = 1` a_cell-length, declared ≡ ℓ_node). Therefore
> **`k_in_ℓnode_units = k[rad/a_cell] × c_link[a_cell/bond]`** — multiplying by the NN-bond length
> converts rad/a_cell to rad/(NN-bond) = rad/ℓ_node.

The two corpus values, restated in these units:
- `0.577/ℓ_node` is dimensionally a **velocity** (it is 1/√3 = `c(k→0)/c_link`, the low-k phase-velocity
  factor), but the corpus quotes it as a `k_max`. If the band genuinely topped out at `k ≈ 0.577 rad/ℓ_node`
  the group velocity would vanish there.
- `π/ℓ_node ≈ 3.14159` is a genuine wavevector — the canonical 1-bond Brillouin edge.

---

## §3 The discriminator (FROZEN)

Sweep `measure_dispersion` across the FULL commensurate-`m` range to the axis Nyquist
(`m = 1 … m_nyq`, where `m_nyq = (#distinct planes along axis)/2`) on the chiral srs net (both
enantiomorphs) and the diamond control. For each `m` record `ω(k)` and `k·ℓ_node`. The **band-top**
`k_max` is the `k` at which the band saturates: **`ω(k)` is maximal and the discrete group velocity
`dω/dk → 0`**.

**Discriminator:** where does the measured `ω(k)` band top out, in rad/ℓ_node units?

---

## §4 Bins (FROZEN — exactly one fires)

- **K4-CUTS-AT-~0.577/ℓ_node** — the band tops out (dω/dk→0) at `k_band-top ≈ 0.577 ± 0.10 rad/ℓ_node`.
  This would make `boundary-observables-m-q-j.md:87` the empirically-correct `k_max` and
  `paley-wiener-hilbert.md:10` (π/ℓ_node) the mislabel.

- **K4-CUTS-AT-~π/ℓ_node** — the band tops out at `k_band-top ≈ π ± 0.30 rad/ℓ_node` (i.e. the measured
  axis-projected band-top is at, or within geometric O(1) of, the canonical 1-bond Brillouin edge π;
  fires if the measured band-top is in `[π−0.3, π+0.3]` OR is the geometry-rescaled image of π —
  see the geometry caveat in §5 — and is decisively far from 0.577). This would make
  `paley-wiener-hilbert.md:10` the empirically-correct order and 0.577 the mislabel.

- **NEITHER (report measured value)** — the band tops out at a `k_band-top` that matches neither
  0.577 (within ±0.10) nor π (within ±0.30, including the geometry-rescaled image). Report the
  measured value, its L-stability, and the srs-vs-cubic geometry dependence as the finding.

**Adjudication note (frozen, anti-rescue):** "0.577 is actually the low-k *velocity* not a k_max" is a
LEGITIMATE finding, not a bin-drop. If the band-top is decisively NOT at 0.577 AND 0.577 reappears as
the measured low-k phase-velocity factor `c(k→0)/c_link`, that is recorded as the mechanism explaining
the contradiction (velocity mislabeled as wavevector) — it does NOT convert a NEITHER/π verdict into a
0.577 verdict. The bins are about where the BAND TOPS OUT (dω/dk→0), not about where 0.577 shows up.

---

## §5 Caveats committed in advance (flag-don't-fix)

1. **srs ≠ simple cubic.** The analytic `π/ℓ_node` is the simple-cubic 1-bond Brillouin edge. The srs
   net is degree-3 chiral Laves; its axis-2 plane spacing is `ℓ/√2` (denser than one bond along that
   ray), so the **axis-projected** Nyquist `k = π/(plane spacing)` can be a geometry-dependent O(1)
   multiple of `π/ℓ_node`. The π-bin explicitly admits this geometry-rescaled image; the verdict
   paragraph will state the raw measured number AND the geometric relationship, not collapse them.

2. **Commensurate-m + FFT resolution.** The band-top `m` can shift by ±1 bin near `m_nyq` due to FFT
   frequency resolution at finite `n_steps`. The driver uses large `n_steps` and reports the band-top
   across L ∈ {6,8,10} to show L-(in)stability; a ±1-bin wobble at the very top is recorded, not hidden.

3. **Single propagating scalar band.** This measures the scalar V-sector acoustic band. A degree-3 net
   may carry optical/folded branches; the FFT-peak extractor reads the dominant (lowest) band. If a
   higher branch dominates at high m it will show as a discontinuity in ω(k) and is reported as-is.

4. **If `measure_dispersion` structurally cannot reach the edge** (e.g. the cosine-Bloch seed projects
   to zero at high m, or the FFT peak collapses), that STRUCTURAL limitation is the finding, reported
   in place of a forced number — per the task's explicit instruction.

---

## §6 Driver + outputs (committed)

- **Driver:** `src/scripts/vol_1_foundations/k4_zone_edge_nyquist_sweep.py` — sweeps
  `cld.measure_dispersion` over `m = 1…m_nyq` on srs-R, srs-L, diamond; converts k to rad/ℓ_node via
  `× c_link`; finds the band-top (max ω, group-velocity sign change); compares to 0.577 and π; emits a
  figure + the JSON sidecar.
- **Result doc:** `research/2026-06-16_k4-zone-edge-nyquist-settle_result.md`.
- **JSON sidecar:** `research/2026-06-16_k4-zone-edge-nyquist-settle_result.json`.
- **Canonical constants** imported from `src/ave/core/constants.py` (ℓ_node, c) — never hard-coded.
