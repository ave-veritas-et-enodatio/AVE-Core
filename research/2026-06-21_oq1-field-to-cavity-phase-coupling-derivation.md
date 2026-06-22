# OQ-1 — The Field → Cavity-Phase Coupling, DERIVED (clm-pp3qwf strengthen-by)

**Date:** 2026-06-21
**Status:** LANDED (committed on `analysis/birefringence-hardening`, PR #345). Adversarial-verify verdict: **`oq1_status: partially-closed`** — the field→cavity-phase coupling is DERIVED (CHECK 1, CHECK 2 PASS); the geometry-factor `g` is PINNED per config with the `g_spatial_axial` integral exact (CHECK 3 PARTIAL). Named residuals carried below (§0, §9).
**Canonical claim:** `clm-pp3qwf` (Vol-4 Ch.12 `vacuum-birefringence-e4.md`, solidity 0.8) — this **partially closes** OQ-1, the open gate flagged in `research/2026-06-21_birefringence-coefficient-bankable-falsifier.md:361-369` (the `g` was "derived only to leading order ... asserted as a Gaussian-beam overlap parameter rather than derived as an Axiom-4 coupling"). The coupling residual is closed (g is now derived/pinned); two named residuals (new-observable vs leaf, single-invariant modeling choice) remain — §0 R-1/R-2.
**Driver:** `src/scripts/vol_9_device/oq1_field_to_cavity_phase_coupling.py` (this branch).
**Extended sweep:** `src/scripts/vol_9_device/vacuum_birefringence_facility_sweep.py` (`G_GRID` re-pinned to the derived `g_eff`).
**Worktree:** `/tmp/biref-harden`, branch `analysis/birefringence-hardening`.

All numbers below are reproduced live from `ave.core.constants` + `ave.bench`; no
hardcoded canonical constants (`make verify` PASS, 996 files, no anti-patterns).

---

## 0. Bottom line

**OQ-1 is PARTIALLY closed (adversarial-verify verdict: `partially-closed`).** The field →
cavity-phase coupling is now **derived**, not asserted, through the chain focal-E → uniaxial probe
tensor (from the scalar Axiom-4 kernel) → cavity round-trip birefringent phase → ellipticity, with
the geometry factor `g` pinned per apparatus config as an explicit Gaussian-focus × cavity-timing
overlap. The QED Euler-Heisenberg leg is co-derived through the *identical* chain (no-strawman) and
validate-on-known recovers PVLAS `A_e` to 0.35%. **Two named residuals remain (do not over-state
"closed"):**

- **R-1 (CHECK-1 caveat — new-observable vs canonical leaf).** The derivation produces a **NEW
  observable** — the par−perp *differential* δn_bir = −½A² — which is **not** the observable in the
  canonical leaf `vacuum-birefringence-e4.md` (`clm-pp3qwf`), whose claim is the **scalar single-arm**
  shift δn = √S − 1 = −¼A² (verbatim :12, :14). The leaf has no tensor / par−perp / uniaxial /
  optic-axis content; the uniaxial-tensor framing entered from the prior proposal doc (§2 of
  `2026-06-21_…falsifier.md`, :98–114), not from the canonical leaf. The derivation is sound and
  genuinely kernel-derived, but it strengthens an observable the leaf does not yet headline. Whether
  to promote the differential observable into `clm-pp3qwf` is an auditor/Grant call (FLAG-A, §6),
  not landed here.
- **R-2 (CHECK-1 substrate residual — single-invariant modeling choice).** Treating u = |E|² as
  **the** field invariant is an AVE modeling choice. QED's Euler-Heisenberg uses **two** Lorentz
  invariants (E²−B², E·B), which is what splits its single-mode coefficients 7/45 vs 4/45. The
  scalar-|E| kernel collapses that to one invariant; this is a substrate-native choice, not a
  derived necessity, and is the deeper reason the AVE par−perp factor (½) is not independently
  tensor-structured the way QED's is.
- **R-3 (CHECK-3 PARTIAL — g pinned, axial integral exact, transverse/config only partial).**
  `g_spatial_axial = (2 z_R/L) arctan(L/2z_R)` is the **exact** Lorentzian path integral (numeric
  quad == closed form to machine precision). The transverse-overlap dilution and the
  three-config temporal/coherent-pass trade-off are **modeled** (not asserted) but are an apparatus
  trade study, not a unique derivation — the recommended config is an engineering recommendation, and
  the polarimetry/detector floor is still owed a validate-on-known against a published cavity (§7,
  prior doc §10.4). `g` cancels in the AVE/QED ratio, so none of R-3 touches the coefficient.

Three findings of substance came out of the derivation (all DERIVED, not assumed):

1. **The linear-pump uniaxial differential leads at −½A², a factor 2 above the scalar single-arm
   −¼A².** The corpus headline ratio 4.14×10⁶ pairs *mismatched* observables (AVE scalar single-arm
   vs QED parallel single-mode). At the **matched** differential observable that a PVLAS/BMV
   ellipsometer actually reads — AVE (par−perp) vs QED (par−perp) — the ratio is **7.5/α³ = 1.93×10⁷**.
   FLAG-don't-fix (surfaced, §6).

2. **DD1's unmodeled gated-cavity lever resolves to a NULL for an fs pump.** A pulsed probe
   recirculated in a gated resonant cavity recovers the finesse build-up *only* if the pump persists
   over the cavity build-up time τ_build = F·L/(πc) ≈ 10.6 ns. A 30 fs pump gates exactly **one**
   coherent pass (g_eff identical to single-pass) — it is gone before the recirculating probe
   re-enters the focus 33 ps later. You do **not** get both finesse and temporal overlap from one
   fs pump; recovering both needs a ns-class gate pump (a ~3.5×10⁵× larger pulse energy at fixed
   peak field).

3. **The recommended config is the CW high-F polarimeter** (full coherent finesse, g_eff = 0.251,
   ψ_AVE = 2.2×10⁻² rad at PW-class field). A ns-gated pulsed cavity is the near-equal pulsed-pump
   alternative (g_eff = 0.237).

The **coefficient** discriminator (the bankable content) is robust and field-independent across all
configs and all g; `g` cancels in the AVE/QED ratio (it multiplies both legs equally). `g` sets only
the absolute realized signal vs floor.

---

## 1. STEP 1 — focal-E → uniaxial probe-response tensor → δn_bir(A) [DERIVED]

**Substrate-native check.** The δn comes FROM the Axiom-4 kernel S = √(1−A²), not an SM default.
The Axiom-4 universal saturation kernel makes the vacuum permittivity a **scalar** function of the
field-energy invariant u = |E|² (`saturation-operator.md`, `vacuum-birefringence-e4.md:12`):

    eps(u) = eps0 · S(u),   S = sqrt(1 − u/E_yield²),   A² = u/E_yield².

The constitutive law of a scalar kernel is **D_i = eps(u)·E_i** (isotropic; the index keys off |E|).
This is the EE-native statement — permittivity, displacement, wave-speed identity n = √(eps/eps0) —
not a Lagrangian/loop construction.

**The uniaxial tensor (the differential of the scalar kernel).** A weak probe **e** rides on top of a
strong, linearly-polarized **pump** E₀. The probe sees the small-signal permittivity tensor
ε_ij = ∂D_i/∂E_j evaluated at the pump operating point:

    eps_ij = d/dE_j [ eps(|E|²) E_i ] |_{E=E0}
           = eps(u0) δ_ij  +  2 eps'(u0) E0_i E0_j          [the explicit dε/d(E²) step]

with **ε′(u0) = dε/du|_{u0}**. This is a **uniaxial** tensor with optic axis ∥ the pump
polarization Ê₀ — DERIVED, no SM form imposed. Computing ε′ from the kernel:

    eps/eps0 = S(u) = (1 − u/E_yield²)^{1/2}
    d(eps/eps0)/du = −1/(2 E_yield²) (1 − u/E_yield²)^{−1/2} = −1/(2 E_yield² S)
    ⇒  2 eps'(u0) E0²/eps0 = −A²/S.

The probe index along (∥) and across (⊥) the pump axis:

    n_perp = sqrt(eps(u0)/eps0)                  = sqrt(S)             = (1−A²)^{1/4}
    n_par  = sqrt((eps(u0) + 2eps'E0²)/eps0)      = sqrt(S − A²/S)      = sqrt((1−2A²)/sqrt(1−A²))

**The birefringence (exact arc + leading term):**

    δn_bir(A) = n_par − n_perp = sqrt((1−2A²)/sqrt(1−A²)) − (1−A²)^{1/4}.

Small-A expansion:
    n_perp ≈ 1 − ¼A²,    n_par ≈ 1 − ¾A²    ⇒    **δn_bir ≈ −½A²**.

**Numerically verified** (driver Step 1, `n_par_minus_perp_exact` vs `delta_n_bir_leading`):
at A = 1e-4 the exact and leading agree to 1e-5; the exact/leading ratio is 1.00000 (A=1e-4),
1.01012 (A=0.1). The exact-arc curvature is the same family as the corpus `(1−A²)^{1/4}` exact arc.

**Relation to the corpus scalar single-arm shift.** The corpus retardance observable
(`vacuum-birefringence-e4.md:14`) is the **scalar single-arm** shift δn_iso = (1−A²)^{1/4} − 1 ≈ −¼A².
The polarimeter's **par-minus-perp differential** is −½A² — exactly **2×** the single-arm shift
(verified: δn_bir/δn_iso → 2.00000 as A→0). This factor of 2 is the standard difference between
a single-mode index shift and a par−perp differential.

---

## 2. STEP 2 — δn_bir → cavity round-trip birefringent phase / ellipticity [DERIVED form + APPARATUS-INPUT λ,L,F]

**EE-first mapping.** The polarimeter (Fabry-Perot finesse + ellipsometer) IS the substrate-native
optics language for this observable — PVLAS/BMV lineage.

A probe launched at 45° to the pump-set optic axis splits into ∥/⊥ components that accumulate a
**differential phase per single pass** through the focal-overlap region:

    δφ_single = (2π/λ) · |δn_bir| · L_overlap.

Writing L_overlap = g_spatial · L (Step 3), referenced to the nominal cavity length L:

    δφ_single = (2π/λ) · g_spatial · |δn_bir| · L.

In a Fabry-Perot of finesse F the intracavity field makes ≈ (2F/π) effective coherent passes through
the medium before exiting (the round-trip build-up: F = π√R/(1−R), effective passes ≈ 2F/π). The
differential phase accumulates **coherently** over the build-up **only if the birefringence persists
across the build-up time** τ_build ≈ F·L/(πc):

    δφ_RT = δφ_single · (2F/π)      [static / persistent birefringence].

A linearly-polarized probe at 45° acquires ellipticity ψ = δφ_RT/2 (small-angle). With the temporal
duty g_temporal (Step 3):

    **ψ = ½ · (2π/λ) · |g · δn_bir| · L · (2F/π)**,    g = g_spatial · g_temporal.

**Why this is the right coupling (the ratified ontology):** the observable is **round-trip
birefringent-PHASE accumulation in the focal-overlap region, finesse-enhanced** — a linear-pump
polarimeter. This is the structurally identical instrument PVLAS/BMV built to measure the QED
Euler-Heisenberg birefringence; the AVE physics enters ONLY through the index-shift coefficient.

**Phase-space coordinate check (PASS).** The kernel is in field-amplitude A = E/E_yield; δn_bir is a
real-space optical-path index; the probe tensor ε δ_ij + 2ε′E₀_iE₀_j is a real-space Cartesian tensor;
the ellipsometer measures real-space optical path. No φ²-vs-Cartesian / phase-space-vs-real-space
mismatch. (Contrast: the optical-activity *rotation* channel rides the phase-space writhe — out of
scope here.)

---

## 3. STEP 3 — PIN g per apparatus config (Gaussian-focus × cavity-mode overlap × temporal) [DERIVED given the APPARATUS-INPUT geometry]

**Spatial overlap [DERIVED given w₀, L].** δn_bir ∝ E², so the probe phase tracks the pump
**intensity** profile. A Gaussian pump focus on-axis has I(z) = I_peak/(1+(z/z_R)²),
z_R = πw₀²/λ_pump (Rayleigh range). The accumulated phase relative to "δn_peak uniform over L":

    g_spatial_axial = (1/L) ∫_{−L/2}^{+L/2} dz/(1+(z/z_R)²) = (2 z_R/L) arctan(L/(2 z_R)).

For L ≫ z_R → πz_R/L (the focal region is a thin slice of the cavity); for L ≪ z_R → 1. A finite
probe waist adds transverse mode-overlap dilution g_spatial_transverse = w₀²/(w₀²+w_p²).
At the headline point (w₀ = λ_pump = 800 nm, L = 1 cm): z_R = 2.51 µm, g_spatial_axial = 7.89×10⁻⁴,
mode-matched g_spatial = 3.95×10⁻⁴.

**Temporal overlap + coherent passes [DERIVED given τ_pump, geometry].** The decomposition is

    g_eff = g_spatial · g_temporal · n_coherent_passes,

a single sweep-independent number = ψ_realized / ψ_(uniform δn over L, single pass).

**The three configs at the PW-class point (E_peak = 2.745×10¹⁴ V/m, A = 2.43×10⁻³):**

| Config | mode | g_spatial | g_temporal | n_coherent | **g_eff** | **ψ_AVE [rad]** | ψ_QED [rad] | small-angle |
|---|---|---|---|---|---|---|---|---|
| (i) CW high-F | CW pump, full build-up | 3.95e-4 | 1 | 2F/π = 637 | **0.251** | **2.19e-2** | 1.13e-9 | OK |
| (ii) pulsed single-pass | co-timed pulse, 1 transit | 3.95e-4 | 1 | 1 | **3.95e-4** | **3.44e-5** | 1.78e-12 | OK |
| (iii-fs) pulsed gated-cavity, 30 fs pump | recirculated, fs pump | 3.95e-4 | 1 | **1** | **3.95e-4** | **3.44e-5** | 1.78e-12 | OK |
| (iii-ns) pulsed gated-cavity, 20 ns gate pump | recirculated, ns pump | 3.95e-4 | 1 | 600 | **0.237** | **2.06e-2** | 1.07e-9 | OK |

(F = 10³, λ_probe = 1064 nm, L = 1 cm throughout. AVE/QED = 1.930×10⁷ at every config — the matched
differential ratio, §6; `g_eff` cancels in the ratio.)

**The DD1 lever, resolved (config iii — the previously-unmodeled combined gated-cavity).**
For the finesse build-up to add coherently, the pump must be PRESENT each time the recirculating
probe re-enters the focus (every τ_rt = L/c = 33.4 ps). A single pump pulse survives only τ_pump.
The number of coherent passes the pump gates is n_pump = τ_pump/τ_rt, capped at 2F/π:

- **30 fs pump:** n_pump = 30 fs / 33.4 ps = 9.0×10⁻⁴ ≪ 1 ⇒ n_coherent = 1. **The gated cavity
  recovers NOTHING beyond single-pass.** g_eff(iii-fs) = g_eff(ii) exactly. The pump is gone before
  the probe completes one round trip; finesse build-up never happens.
- **20 ns gate pump (≥ τ_build = F·L/(πc) = 10.6 ns):** n_coherent = 600 ≈ 2F/π ⇒ near-full finesse
  recovered, with g_temporal = 1. g_eff(iii-ns) = 0.237 ≈ g_eff(i).

**Answer to DD1:** a gated/resonant build-up recovers BOTH finesse AND temporal overlap **only if the
pump persists over τ_build ≈ 10.6 ns**, i.e. a ns-class gate pump (a ~3.5×10⁵× larger pulse energy at
fixed peak intensity than a 30 fs pulse). An fs pump cannot do both. This is a hard
pump-duration × finesse-product constraint — the lever is not free.

**Recommended config: (i) CW high-F** (g_eff = 0.251, ψ_AVE = 2.19×10⁻² rad, full coherent finesse,
in small-angle, above the 10⁻⁹ rad realistic polarimetry floor). The ns-gated pulsed cavity (iii-ns)
is the near-equal pulsed-pump alternative (g_eff = 0.237) for facilities that can only deliver the
peak field in a pulse but can stretch the gate to ns.

---

## 4. STEP 4 — co-derive the QED Euler-Heisenberg leg + validate-on-known [no-strawman + VALIDATE-ON-KNOWN]

The QED Euler-Heisenberg weak-field birefringence (Heisenberg-Euler 1936; PVLAS/Rizzo, LABELED
non-AVE literature) under a static linearly-polarized field:

    n_par − 1 = (7/45) α² (E/E_crit)²,   n_perp − 1 = (4/45) α² (E/E_crit)²,
    **n_par − n_perp = (3/45) α² (E/E_crit)²   [the DIFFERENTIAL — the polarimeter observable].**

Both AVE and QED differential shifts are driven through the **identical** `realized_ellipticity(δn, g_eff)`
machinery; the ONLY difference is the index-shift coefficient (no-strawman R1).

**VALIDATE-ON-KNOWN (HALT gate, PASS):**
- PVLAS `A_e = 2α²ℏ³/(45 μ₀ m_e⁴ c⁵) = 1.32467×10⁻²⁴ T⁻²` vs textbook 1.32×10⁻²⁴ T⁻² (rel-err 0.35%
  = exact-CODATA vs rounded-textbook). PASS.
- Substrate identity (E_crit/E_yield)² = 1/α = 137.0360 (exact by construction, E_YIELD = √α·E_CRIT);
  c·B_crit = E_CRIT. PASS.

The QED-EH ellipticity is recovered through the same chain: at the PW point, ψ_QED = 1.13×10⁻⁹ rad
(config i), 1.78×10⁻¹² rad (single-pass) — a factor 1.93×10⁷ below the AVE leg at every config.

---

## 5. STEP 5 — extended facility sweep with the PINNED g [re-run]

`vacuum_birefringence_facility_sweep.py` `G_GRID` re-pinned from the first-cut bound
`[7.9e-4, 1e-3, 1e-5, 1e-8]` to the **derived** operating points + worst-credible tail:
`[0.251 (full-finesse), 3.95e-4 (single-pass/fs-gated), 1e-5, 1e-8]`.

**Re-run result (1728 points, validate-on-known PASS, make verify PASS):**

| Axis | In-window range |
|---|---|
| in-window | 840 / 1728 points |
| E | [1.0×10⁹, 3.0×10¹⁶] V/m (A = [8.9×10⁻⁹, 0.265], deep-linear) |
| finesse | [10², 10⁵] |
| g | [10⁻⁸, 0.251] — spans BOTH pinned g_eff (single-pass 3.95e-4 ✓, full-finesse 0.251 ✓) |
| ψ_AVE | [1.06×10⁻⁹, 9.17×10⁻²] rad |
| AVE/QED ratio | **field-INDEPENDENT [4.136×10⁶, 4.250×10⁶]** (this sweep uses the corpus single-arm/parallel pairing; ~2.8% high-end drift = exact-kernel curvature) |
| fastest 5σ | 7.39×10⁻¹⁶ s at E = 6.9×10¹³ V/m, F = 10⁵, g = 4.0×10⁻⁴ |

The high-g_eff = 0.251 points correctly trip the small-angle guard at the highest fields (ψ > 0.1 rad)
and are excluded from the window there — honest behavior, not a magnitude over-claim.

---

## 6. FLAG-DON'T-FIX (surfaced, not silently resolved)

> 🔵 **FLAG-A ADJUDICATED + LANDED (Grant, 2026-06-21).** The recommendation below is now the ruling and
> is executed across the corpus: the **matched differential 1.93×10⁷ = 7.5/α³ is the falsifier headline**
> (AVE −½ vs QED differenced 3/45); the single-arm 4.14×10⁶ is the isotropic common-mode (polarimeter-blind)
> comparison, traceability only. Propagated to `clm-pp3qwf` / `vacuum-birefringence-e4.md` /
> `vacuum-impedance-mirror.md` / `divergence-test-substrate-map.md` (B1) + the vol4/vol9 manuscript twins +
> the figure (regenerated through `ave.viz.style`) + the facility-sweep driver/JSON + `ave.bench`
> (`coefficient_ratio_differential`, `delta_n_ave_differential_exact`). Body below PRESERVED verbatim.

**FLAG-A — the matched-observable ratio is 1.93×10⁷, not 4.14×10⁶, for a differential polarimeter.**
The corpus `vacuum-birefringence-e4.md:18` and the prior result doc headline **4.14×10⁶**, which is
`1/(4·(7/45)·α³)` — the AVE **scalar single-arm** shift (−¼A²) over the QED **parallel single-mode**
(7/45). But a PVLAS/BMV ellipsometer measures the **par-minus-perp differential**. At that matched
observable:
- AVE differential = −½A² (DERIVED Step 1, coefficient ½ on (E/E_yield)²);
- QED differential = (3/45)α²(E/E_crit)²;
- ratio = (½)/((3/45)α²)·(E_crit/E_yield)² = **45/(6α³) = 7.5/α³ = 1.930×10⁷** (closed form, verified).

Both are field-independent and ride the substrate identity; both numbers are honest, but they answer
different questions. The corpus headline pairs **mismatched** observables (AVE single-arm vs QED
single-mode-parallel). **RECOMMEND (auditor lands, not me):** state the headline as observable-matched —
single-arm-retardance probe → 4.14×10⁶ (AVE −¼ vs QED 7/45); differential ellipsometer → 1.93×10⁷
(AVE −½ vs QED 3/45). The §7 "match-the-observable" note in the prior doc already half-anticipates this
but pairs AVE −¼ with QED 3/45 (giving 9.65×10⁶), which is itself a single-arm-vs-differential mismatch.
The clean rule: a differential instrument ⇒ AVE −½ vs QED 3/45 ⇒ 1.93×10⁷. Surfaced verbatim, NOT
silently reframed.

**FLAG-B (inherited, unchanged).** The a_EH ≈ 1.45 `A_EH_LITERATURE` entry remains a 1/(2πα) units
artifact (DERIVE-2, prior doc §6 / FLAG-(ii)); excluded from the physical band; auditor lands the
band re-scope.

The **chord-vs-echo split is unaffected** by FLAG-A: the FORM (tree-O(1) saturation vs α²-loop) is the
AVE-distinct content at any matched observable; the MAGNITUDE (4.14×10⁶ or 1.93×10⁷) is an α-echo
either way (symmetric standard: QED's coefficient is equally α-rooted). The discriminator's force is the
field-independent ~6–7 OOM gap, not the third significant figure.

---

## 7. DERIVED vs APPARATUS-INPUT vs ASSERTED ledger (the gate)

| Quantity | Tag | Basis |
|---|---|---|
| ε(u) = ε₀√(1−A²) scalar kernel | **DERIVED** (MANIFESTATION of Axiom 4) | `saturation-operator.md`, `vacuum-birefringence-e4.md:12` |
| ε_ij = εδ_ij + 2ε′E₀_iE₀_j uniaxial tensor | **DERIVED** | exact differential of the scalar kernel; ε′ = dε/du from the kernel |
| δn_bir = n∥−n⊥ exact arc + leading −½A² | **DERIVED** | algebra of the tensor; numerically verified, factor-2 vs single-arm |
| ψ = ½(2π/λ)|g·δn|L(2F/π) coupling FORM | **DERIVED** (form) | round-trip birefringent-phase accumulation, finesse build-up 2F/π |
| g_spatial_axial = (2z_R/L)arctan(L/2z_R) | **DERIVED** given w₀,L | Gaussian-focus path integral of the Lorentzian I(z) |
| g_spatial_transverse = w₀²/(w₀²+w_p²) | **DERIVED** given w₀,w_p | transverse mode overlap |
| n_coherent = min(2F/π, τ_pump/τ_rt) | **DERIVED** given τ_pump,F,L | pump-gated coherent-pass count; τ_build = FL/πc threshold |
| g_eff = g_spatial·g_temporal·n_coherent | **DERIVED** given the config | the pinned per-config coupling |
| ratio_differential = 7.5/α³ (and 4.14e6 single-arm) | **DERIVED form / ECHO magnitude** | rides substrate identity; α-rooted value |
| QED (7/45, 4/45, 3/45) a_EH | **APPARATUS/LITERATURE input** | Heisenberg-Euler 1936; labeled non-AVE, not fit |
| PVLAS A_e = 1.32×10⁻²⁴ T⁻² target | **VALIDATE-ON-KNOWN** | recovered to 0.35%; HALT on fail |
| w₀, λ_pump, λ_probe, L, F, τ_pump, I_peak | **APPARATUS-INPUT** (engineering) | the facility design choices; not AVE physics |
| PROBE_POWER, polarimetry floors 10⁻⁹/10⁻¹¹ rad | **APPARATUS-INPUT** (still owed a validate-on-known vs a specific published cavity, prior doc §10.4) | PVLAS/BMV-class lineage |
| **nothing in the coupling chain is now ASSERTED** | — | the prior "Gaussian-beam overlap parameter, asserted" is now derived as g_spatial × g_temporal × n_coherent |

**Net:** OQ-1's *coupling* residual — `g` asserted as a Gaussian-beam overlap parameter rather than
derived as a coupling — **is closed**. `g_eff` is now a DERIVED function of explicit APPARATUS-INPUTs
(w₀, L, F, τ_pump), with the temporal/coherent-pass physics that the prior first-cut omitted. But
OQ-1 as a whole is **partially-closed** per the verify verdict: the remaining residuals are R-1
(the derived par−perp differential is a NEW observable, not the canonical leaf's scalar single-arm
`clm-pp3qwf` — promotion is an auditor/Grant call), R-2 (u=|E|² single-invariant is an AVE modeling
choice vs QED's two invariants), and R-3 (the polarimetry/detector floor is still owed a
validate-on-known against a published cavity). The COEFFICIENT result depends on none of them.

---

## 8. Output artifacts (LANDED — committed on `analysis/birefringence-hardening`, PR #345)

- `src/scripts/vol_9_device/oq1_field_to_cavity_phase_coupling.py` (driver)
- `src/scripts/vol_9_device/_output/oq1_field_to_cavity_phase_coupling.json`
- `src/scripts/vol_9_device/_output/oq1_field_to_cavity_phase_coupling_birefringence_arc.{png,pdf}`
- `src/scripts/vol_9_device/_output/oq1_field_to_cavity_phase_coupling_config_coupling.{png,pdf}`
- `src/scripts/vol_9_device/_output/oq1_field_to_cavity_phase_coupling_gate_constraint.{png,pdf}`
- `src/scripts/vol_9_device/vacuum_birefringence_facility_sweep.py` (G_GRID re-pinned) + its re-run figures.

The auditor lands the manuscript/COLLABORATION_NOTES queue items (surfaced here, not landed by the
implementer lane): the FLAG-A matched-observable note; the OQ-1 leading-order → **partially-closed**
(coupling-derived, g-pinned) status flip; and the auditor/Grant call on whether to promote the
par−perp differential observable into `clm-pp3qwf` (R-1).
