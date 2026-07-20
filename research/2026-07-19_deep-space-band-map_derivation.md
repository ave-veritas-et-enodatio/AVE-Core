# Deep-Space Band-Map — Re-Derivation (per-channel dispersion, reactive-vs-radiative threshold, structure-at-resonances verdict)

**Date:** 2026-07-19
**Class:** DERIVATION (research-doc; **forms derived, values calibration-tagged; mints no `clm-`, propagates to no KB/tex leaf**). This lane executes the band-map re-derivation that the deep-space reactive-bulk walk-record (`research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md` §5) SPEC'd but did not run.
**Provenance:** SPEC = Grant's 2026-07-19 in-chat ruling, recorded verbatim in the walk-record §1(c). Every canon input below was `grep -F` content-verified in this worktree at HEAD `1be045a1` (verify-before-cite). Grant's own words are cited only through the walk-record's `[Grant-verbatim]` transcription — **not re-attributed or re-quoted from memory**.
**Lane fences:** DERIVATION lane only. **No** `manuscript/` / `manuscript/ave-kb/` / `.tex` edits, **no** engine edits, **no** files PR #738 touches. KB/tex propagation is listed as OWED-FOLLOW-ONS (§7) and fenced to the cleanup lanes.

---

## §0 — Attribution key + what this doc does / does not do

**Attribution tags** (load-bearing, same discipline as the walk-record):
- **[canon]** — a citation of an existing canonical leaf, content-verified at HEAD `1be045a1`.
- **[derived]** — a FORM this lane derives from [canon] inputs by standard lattice-dispersion algebra. Derivation shown; nothing here is asserted as new canon.
- **[calibration]** — a VALUE that enters only through `ℓ_node = ℏ/(m_e c)` (the Compton-length calibration identity). Consistency-class per `consistency-vs-emergence`: the FORM is derivable, the VALUE is CODATA-imported through the calibration.
- **[Grant-verbatim, via walk-record]** — Grant's ruling, cited through the walk-record's transcription, never paraphrased into a derived claim.

**This doc DOES:** derive per-channel lattice dispersion (band edges, cutoffs, evanescent decay lengths, the Cherenkov/Mach drag-onset criterion); classify the demoted deep-space sites as structure-at-resonances candidates with the consensus-bias knife applied both ways; produce a ranked, reachability-tagged, dimensionless-ratio discriminator list.

**This doc does NOT:** mint canon, edit any KB/tex leaf, refill the demoted-mechanism slot with a new asserted mechanism (Rule 12 / A47 v11b — the demoted slot stays open; this is a *new* lane with its own verification chain), or headline emergence-class claims where inputs are calibration-derived.

---

## §1 — REGIME / SECTOR / PHASE-STATE header (fire before any dispersion algebra)

**MODE.** A slow macroscopic body (asteroid, comet, dust grain, the Moon) — and, in the contrast column, a lattice-scale excitation (electron / atomic orbital) — coupling to the deep-space vacuum medium.

**REGIME.** **Regime I** — sub-yield, deeply linear (`A_gm ≪ 0.121`, the solar-system operating point of `06_solar_system.tex:203` [canon]). The dispersion algebra below is the **cold-linear** band structure; saturation (Op14, `A → 1`) enters only as a spatial *grading* of the channel impedances (§3.4), never as a bulk loss.

**PHASE-STATE.** **Cold-reactive** (lossless-reactive, Axiom 3): `manuscript/common_equations/eq_axiom_3.tex:24` [canon] — the medium "stores and returns energy but does not dissipate it," and "any apparent loss must be a boundary-radiation or mode-conversion channel, **never a bulk resistive one**." All band structure below is Hermitian (real ω, real or imaginary k); the only loss channel the band-map admits is a *radiative port* that opens above the Mach/Cherenkov threshold (§3.3).

**SECTOR.** Multi-channel. The graded vacuum impedance network carries **three** propagating channels — EM-transverse `Z_EM`, mechanical shear `Z_shear`, bulk-longitudinal `Z_bulk` (`bulk-impedance-at-saturation-boundary.md:44–73` [canon]) — plus a **fourth, gapped** Cosserat micro-rotation (couple-stress / curvature) branch that carries the `(2,3)` winding and is Yukawa-screened (`master-equation.md:24` [canon]; `cosserat-mass-gap.md` [canon]). The deep-space gravitational added-mass coupling is the **A1 / bulk** reactive channel; charge/winding is the **gapped Cosserat** channel. **Do not cross-wire** (A1 ⊥ T2, sector-ownership discipline).

**SUBSTRATE-NATIVE CHECK (fired before the dispersion algebra).** K4: the lattice is the chiral Laves K4 Cosserat crystal (`cosserat-mass-gap.md:38` [canon], 6 DOF/node = 3 translational + 3 micro-rotational). Cosserat: the micro-rotation ω is a genuine independent DOF (the mass-gap lives on it). Op14: saturation enters as `Z_eff(r) = Z_0/√S`, `S = √(1−A²)` (`lattice-impedance-decomposition.md:56` [canon]) — a *reactance grading*, not a resistor. Phase-space-vs-real-space: the band-map is a **dispersion-relation (ω–k) object** — a phase-space statement — and the reactive-vs-radiative verdict is read in ω–k, not in real-space Cartesian drag. This is the correct coordinate per A46 (the corpus claim "effects live in frequency passbands" is a frequency-domain claim; the test is a frequency-domain dispersion object).

---

## §2 — THE BAND-MAP: per-channel dispersion of the K4 / Cosserat lattice

### §2.1 — The generic acoustic branch (the shape all gapless channels share) [derived]

For a nearest-neighbour lattice of pitch `ℓ_node`, a channel of long-wavelength speed `c_ch` carries the standard monatomic-chain / TLM arccos branch (the "band-structure / dispersion survey" row, `translation-circuit.md:233` catalog, coined-quantum-walk / TLM arccos map [canon]):

$$\omega_{ch}(k) \;=\; \frac{2\,c_{ch}}{\ell_{node}}\,\left|\sin\!\left(\tfrac{k\,\ell_{node}}{2}\right)\right|,\qquad k\in\Big[0,\ \tfrac{\pi}{\ell_{node}}\Big].$$

Three consequences fall straight out, each a **[derived] FORM**:

1. **Long-wavelength (Regime-I) limit is exactly linear:** `k ℓ_node ≪ 1 ⇒ ω ≈ c_ch k`. The channel is dispersionless — a matched transmission line — throughout the entire regime any macroscopic body probes. This is the field-theoretic content of "the vacuum acts as a perfect lossless transmission line" (`vol3/claim-quality.md:76` [canon]).
2. **Upper band edge (the lattice cutoff):** at `k = π/ℓ_node`, `ω = ω_max = 2c_ch/ℓ_node`, `f_max = c_ch/(π ℓ_node)`. This reproduces the canonical Casimir/below-cutoff row exactly: `translation-circuit.md:154,:353` [canon] gives `f_max = c/(π ℓ_node)`, `ω_max = 2c/ℓ_node` for the `c_ch = c` channel — a **content-match, not a new result** (this lane recovers the canon band edge as the `k = π/ℓ_node` corner of the arccos branch).
3. **Group velocity collapses at the edge:** `v_g = dω/dk = c_ch cos(kℓ_node/2) → 0` as `k → π/ℓ_node`. The band edge is a *cutoff*, not a resonance; a mode driven at `ω_max` does not propagate away — it is a standing zero-group-velocity mode ("resolves near the band edge," `translation-circuit.md:188` [canon]).

### §2.2 — The four branches of the graded vacuum medium [derived FORMS; VALUES tagged]

| # | Channel (sector) | Impedance | Long-λ speed `c_ch` | Band structure | Band edge `ω_max = 2c_ch/ℓ_node` | Gap? |
|---|---|---|---|---|---|---|
| 1 | **EM-transverse** (photon, T₂ shear-EM) | `Z_EM = Z_0` [canon] | `c = √(G/ρ)` | gapless acoustic (§2.1) | `2c/ℓ_node` | none |
| 2 | **Mechanical shear / GW** (T₂ shear-G) | `Z_shear = ρ c_shear` [canon] | `c_shear = c` | gapless acoustic | `2c/ℓ_node` | none |
| 3 | **Bulk-longitudinal / dilatation** (A1 mass) | `Z_bulk = ρ c_bulk` [canon] | `c_bulk = √2·c` (K = 2G magic angle) | gapless acoustic | `2√2·c/ℓ_node` | none |
| 4 | **Cosserat micro-rotation / wryness** (couple-stress, the `(2,3)` winding) | couple-stress `γ`-grade [canon] | `c_κ = √2·c` | **GAPPED**: `ω² = c_κ²k² + m_ω²` | `2√2·c/ℓ_node` | **`m_ω = √(4G_c/I_ω)`** |

**Speed provenance [canon], `cosserat-mass-gap.md:120–132` "three speeds, do not fuse" table:**
- Channel 1 `clm-j550uh`: T₂ transverse **shear** photon, `c = √(G/ρ) = 1` (engine units).
- Channel 2: GW = **transverse shear** mode, propagates on the shear-G modulus at `c` (`einstein-field-equation.md:62–63,:84` [canon]: "GW are transverse shear modes"; "low-frequency macroscopic inductive strain-waves"). Same *speed* as channel 1, distinct *sector/impedance*.
- Channel 3 `clm-uu1qbo`: A1 / bulk **dilatational** longitudinal, `√2·c = √(K_bulk/ρ)`, the `√2` from `K = 2G` at the magic angle.
- Channel 4 `clm-kmliqx`: T₂ **curvature / wryness** twist-gradient, `c_κ = √(2γ/I_ω) = √2·c` (no-½ `Σκ²` convention, `cosserat_field_3d.py:704`); when the mass term `4G_c/I_ω` is on, the branch is the **gapped** dispersion `ω² = c_κ²k² + m_ω²`, `m_ω² = 4G_c/I_ω` (`cosserat-mass-gap.md:59` [canon]).

*(A fifth object, the isotropic-solid P-wave `c_L = √((K + 4/3 G)/ρ) = √(10/3)·c ≈ 1.826 c`, `cosserat-mass-gap.md:132` [canon], is the acoustic-manifold top inside the BZ — a combined bulk+shear longitudinal mode, not an independent graded-impedance channel; listed for completeness, not load-bearing here.)*

### §2.3 — The gapped channel is the ONLY one with a low-frequency stopband [derived]

The three gapless channels (1–3) propagate **all the way down to DC**: `ω → 0` as `k → 0`, no lower cutoff. Channel 4 is different. Its dispersion `ω² = c_κ²k² + m_ω²` has a **mass gap**: no real-`k` propagating mode exists for `ω < m_ω`. In the stopband `0 ≤ ω < m_ω`, `k` is imaginary,

$$k \;=\; \pm\,\frac{i}{c_\kappa}\sqrt{m_\omega^2 - \omega^2},\qquad\text{evanescent decay length }\ \xi(\omega)=\frac{c_\kappa}{\sqrt{m_\omega^2-\omega^2}}.$$

For a **static or slow** source (`ω ≪ m_ω`) the decay length saturates at `ξ_0 = c_κ/m_ω` — a Yukawa / Compton screening length. This is the field-theoretic origin of the corpus's "gapped mechanical Cosserat ω → short-range, Yukawa-screened `(2,3)` winding" (`master-equation.md:24`, `substrate-perspective-electron.md:109` [canon]).

**Numerically [calibration]** (`ℓ_node = ℏ/(m_e c) = 3.862×10⁻¹³ m`, the reduced Compton wavelength = the calibration identity):
- `m_ω ~ c/ℓ_node = 7.76×10²⁰ rad/s` (the electron Compton angular frequency), so `ξ_0 ~ ℓ_node`. The gapped channel's reactive reach is **one Compton wavelength** — a *contact* interaction at any macroscopic scale.
- Band edges: `ω_max^EM = 2c/ℓ_node = 1.55×10²¹ rad/s`, `f_max = 2.47×10²⁰ Hz`.
- **Gap-to-band-edge ratio `m_ω/ω_max^EM = 1/2`** — but this `1/2` is a *consequence of the calibration* `ℓ_node ≡ λ̄_C` (which forces `m_ω = c/ℓ_node`), NOT an independent emergent ratio. Tag: **consistency-class**, do not headline.

**Load-bearing structural fact.** Only the gapped Cosserat channel is genuinely "below cutoff / evanescent" for a slow source. The gapless channels 1–3 are *not* in a stopband at low frequency — they are in the linear passband. So the walk-record's clause "(ii)" framing ("deep-space slow matter sits below the band edge ⇒ evanescent") is **precise only for the gapped channel**; for the gapless channels the reactive-ness has a *different* origin (below the Mach/Cherenkov threshold, §3.3), not evanescence. This lane derives both mechanisms explicitly and does not conflate them — see §3.

---

## §3 — Reactive coupling and the drag-onset (Cherenkov/Mach) threshold, per channel

### §3.1 — Two distinct reasons a slow body couples reactively (not resistively) [derived]

A body moving at `v` through the medium couples to each channel, and in **every** channel the coupling is reactive (lossless) at deep-space speeds — but for **two structurally different reasons**:

- **Gapless channels (1–3):** the body drags a **co-moving quasi-static near-field**. Below the radiation threshold (§3.3) no energy leaves as a propagating wave; the near-field stores kinetic energy on acceleration and returns it on deceleration. This is the **added-mass / d'Alembert** reactance — a virtual inductance, zero steady drag. (Prior corpus use of "added mass" as reactive inertia: `hollow-vortex-binding.md`, `temporal-saturation-regime-classifier.md` — cited as prior use, not as a derivation of this claim.)
- **Gapped channel (4):** the body's slow forcing is `ω ≪ m_ω`, deep in the stopband ⇒ the coupling is **evanescent** (§2.3), decay length `~ ℓ_node`. An evanescent field cannot radiate, so it cannot dissipate — it can only store-and-return, and at macroscopic range it is negligible (Yukawa contact term).

Both are Axiom-3-lossless-reactive. **Neither is a bulk `Re(Z)`.** The demoted "topological Joule stall against the resistive deep-space metric" (`04_continuum_electrodynamics.tex:252`, `:254` [canon, now 🔴-demoted]) is neither of these and is forbidden by `eq_axiom_3.tex:24`.

### §3.2 — Added-mass back-force is reactive: the d'Alembert statement [derived]

For steady motion through a lossless medium the net force in the direction of motion vanishes (d'Alembert's paradox: no dissipation ⇒ no net drag on uniform motion). The only force is the *reactive* added-mass term, `F = −m_add · dv/dt`, which vanishes for `dv/dt = 0`. Mechanical dual of `eq_axiom_3.tex:24` (the bond-LC tank "stores and returns"). **Consequence:** a deep-space body in uniform drift feels **zero steady drag** — the store-and-return, not a stall.

### §3.3 — The Cherenkov/Mach drag-onset threshold (the radiative port) [derived]

Real drag requires a **propagating wake** — a radiative port opens (Ax3-legal: loss at a *radiation channel*, not in the bulk). The wake becomes propagating when the source can phase-match to a real lattice mode, i.e. when `v` exceeds the mode's phase velocity `v_p = ω/k` for some available `k`. On the arccos branch (§2.1),

$$v_p(k) \;=\; \frac{\omega_{ch}(k)}{k} \;=\; c_{ch}\,\operatorname{sinc}\!\left(\tfrac{k\,\ell_{node}}{2}\right),\qquad v_p:\ c_{ch}\ (k\to0)\ \longrightarrow\ \tfrac{2}{\pi}\,c_{ch}\ (k=\tfrac{\pi}{\ell_{node}}).$$

The phase velocity is **minimised at the band edge**, `v_{p,\min} = (2/π)\,c_{ch}`. Therefore the **drag-onset (Mach/Cherenkov) condition, per channel, is**

$$\boxed{\ v \;>\; v_{crit}^{(ch)} \;=\; \frac{2}{\pi}\,c_{ch}\quad\text{(for a source that couples to band-edge modes).}\ }$$

- **`v_crit/c_ch = 2/π ≈ 0.637` is a [derived], DIMENSIONLESS, LATTICE-UNIVERSAL ratio** — independent of `ℓ_node`, identical for any nearest-neighbour cosine branch. It is the single genuinely AVE-distinct dimensionless number the band-map produces at the drag-onset. Manifestation-class (a theorem of the arccos dispersion), not calibration.
- **Per-channel thresholds:** EM/shear `v_crit = (2/π)c ≈ 0.637c`; bulk `v_crit = (2/π)√2 c ≈ 0.900c`; curvature `≈ 0.900c` (above its gap).

**Bandlimiting caveat (honest, load-bearing).** The `(2/π)` reduction only applies to a source whose coupling k-content *reaches the band edge* `π/ℓ_node`. A physical body of size `R ≫ ℓ_node` has bandlimited coupling `k ≲ 1/R ≪ π/ℓ_node`, so the only phase velocities available to it are the linear-branch values `v_p ≈ c_ch`. For such a body the **effective threshold rises to `v_crit → c_ch`** — never reached by anything sub-luminal. This is *why* normal matter (and relativistic particles: an accelerator electron's de Broglie `λ ≫ ℓ_node`) shows **no** spurious vacuum-Cherenkov drag, and it is the band-map's consistency with emergent Lorentz invariance (`preferred-frame-and-emergent-lorentz.md` [canon]: the GRB `(qℓ_node)²` dispersion horn is retracted; the free photon is the linear-branch continuum field). **Deep-space slow matter is doubly protected:** `v ~ 10⁻⁴ c` (≪ `2/π c`) AND bandlimited.

### §3.4 — Saturation grading is a reactance grading, not a resistor [derived from canon]

Near a mass, Op14 grades the channel impedance `Z_eff(r) = Z_0/√S`, `S = √(1−A²(r))` (`lattice-impedance-decomposition.md:56` [canon]). This is the AVE mechanism of **gravity itself** ("macroscopic dielectric refraction," `einstein-field-equation.md:76` [canon]) — a spatial gradient of a *reactance*, which bends trajectories and sets the added-mass profile. It introduces **no `Re(Z)`**: a graded lossless line is still lossless. An impedance *step* (if a sharp `S`-isocline exists at an outer boundary) produces a **reactive reflection** `Γ = (Z_2−Z_1)/(Z_2+Z_1)` — a phase-preserving partial reflection, energy-conserving — **not** a thermalising stall. This is the discriminator handle §5-D1.

---

## §4 — Structure-at-resonances: the demoted deep-space sites (prove-or-disprove, consensus knife both ways)

The ruling's clause 2 [Grant-verbatim, via walk-record §1(c)]: *"there dofferent passpa danof frequencies for effects, like the rings of saturn vs electron orbitals"* `[sic]`. The honest question (not "manufacture an AVE effect," not "reflex-null"): **does the lattice band-map predict any structure at the Kirkwood / Oort scale that Newtonian orbital resonance does not already produce?**

### §4.1 — What the Kirkwood "cavity-mode" account actually is [canon + derived]

`kirkwood-gaps-cavity-modes.md:12` [canon]: gaps at `a_gap = a_J·(q/p)^{2/3}`, all five (4:1, 3:1, 5:2, 7:3, 2:1) to `<0.3%`. **This spacing law is Kepler's third law applied to a mean-motion resonance:** `T_ast/T_J = q/p ⇒ (a_ast/a_J)^{3/2} = q/p ⇒ a_ast = a_J(q/p)^{2/3}`. The `2/3` exponent is the Kepler exponent, not a lattice number. The "cavity mode in the gravitational impedance field" is therefore a **relabelling of the Newtonian mean-motion resonance** — it reproduces the gaps to `<0.3%` *because it is* the Newtonian resonance condition. **Consistency-class, peer-with-Newtonian; not a distinct spacing prediction.**

### §4.2 — Why there is no lattice-native structure at solar-system frequencies [derived]

Solar-system dynamical frequencies vs the lattice band features [calibration, computed this lane]:

| Site | `Ω_orb` (rad/s) | orders below `ω_max = 2c/ℓ_node` |
|---|---|---|
| asteroid (`a ≈ 2.5 AU`) | `4.98×10⁻⁸` | **28.5** |
| Jupiter | `1.68×10⁻⁸` | **29.0** |
| Oort (`a ≈ 5×10⁴ AU`) | `1.81×10⁻¹⁴` | **34.9** |

Every solar-system orbital frequency sits **~28–35 orders of magnitude below** the lattice band edge *and* the Cosserat mass gap (`m_ω ~ c/ℓ_node`). At these frequencies **every channel is in its exactly-linear, dispersionless, featureless passband** (§2.1). The lattice has **no band feature — no cutoff, no gap, no resonance — anywhere near solar-system frequencies.** The reactive added-mass coupling (§3.2) is a smooth, non-resonant effective-inertia renormalisation; it produces no discrete structure.

### §4.3 — VERDICT: CLEAN NULL at the solar-system scale (with a KEEP-BOTH boundary discriminator)

**The demotion ends the story for the Kirkwood/Oort sites.** The lattice band-map predicts **no additional structure** beyond Newtonian mean-motion resonance:
- No distinct spacing law (the `(q/p)^{2/3}` is Kepler, reproduced by relabelling — §4.1).
- No channel-selective comb (all channels are featureless and identical at these frequencies — §4.2).
- No dimensionless ratio Newtonian resonance does not already produce (the only AVE-distinct dimensionless numbers the band-map carries — `2/π`, `√2`, `√(10/3)` — live at the *threshold/quantum* scale, not at orbital frequencies — §3.3, §5).

This is a **derived null, not a reflex null**: it follows from the ~28–35-order frequency separation, computed above, between orbital dynamics and the nearest lattice band feature.

**Consensus-bias knife, both ways (symmetric standard):**
- *Against AVE:* the "gravitational-impedance cavity mode" adds nothing observable over Newtonian resonance — it is a relabel that fits because it reduces to Kepler. AVE-distinct content at this scale = **∅**.
- *Against consensus:* Newtonian mean-motion resonance is *also* "just" the accepted mechanism that fits to `<0.3%`; it does not derive the gaps from anything deeper than the resonance condition either. So AVE and Newton are **peer** here — and a peer relabel is *not* a chord. Neither framework earns a distinction from the Kirkwood/Oort data.

**The one thing that does survive as a live discriminator** is not "additional structure" but the *character of the boundary crossing* (reactive reflection vs resistive stall) — §5-D1, the KEEP-BOTH axis the demotion opens. That is a boundary phenomenon, not a spacing law.

### §4.4 — WHERE lattice-band structure IS observable (the other passband) [derived]

The ruling's two passbands are **~27–35 orders of magnitude apart in frequency**, and only one of them carries lattice-native content:

| Passband | Frequency regime | Structure source | Lattice-native content? |
|---|---|---|---|
| **"rings of Saturn" (macro)** | `Ω_orb ~ 10⁻⁸ – 10⁻¹⁴ rad/s` | **gravitational / Newtonian** mean-motion resonance | **NO** — featureless-linear lattice; structure is orbital-mechanical (§4.2) |
| **"electron orbitals" (micro)** | `~ 10¹⁵ – 10²¹ rad/s` (approaching `m_ω`, `ω_max`) | **lattice** band structure / Cosserat mass gap | **YES** — this is where the arccos band, the gap, and the `2/π`, `√2` ratios become physical |

The band-map's genuine structure-at-resonances is at the **atomic/quantum passband** (near the mass gap and band edge), where a body's coupling frequency is within a few orders of `m_ω`. The deep-space (macro) passband is the *gravitational-resonance* passband, and it has no lattice-distinct structure. Grant's "Saturn rings vs electron orbitals" is precisely this two-passband, two-decades-of-decades split — and the honest reading is that the demoted deep-space claim belongs to the *left column* (Newtonian), which the demotion correctly empties of AVE-distinct content.

---

## §5 — Forward discriminators (ranked; dimensionless where possible; reachability-tagged)

Ranked by discriminating power × reachability. Each names: the observable, what each world predicts, calibration-vs-derived status, reachability.

**D1 — Zero-drag / `v`-independence at the outer-boundary crossing.** *[PRIMARY]*
- **Observable (dimensionless):** the scaling exponent `n` in anomalous along-track deceleration `a_drag ∝ v^n` for a probe crossing the Oort/yield transition.
- **Reactive ruling predicts:** `n` undefined — **no secular drag** (d'Alembert, §3.2); at most a *reactive reflection* (a bounded, phase-coherent, energy-conserving velocity kick at an impedance step, §3.4), not a monotone deceleration.
- **Demoted resistive stall predicts:** `n ≥ 1` — a `∝v` (or steeper) drag spike scaling with transit velocity (`04:252` [canon, demoted]).
- **Status:** the discriminating axis is [derived] (form-level, dimensionless exponent). **Flips the vol4 boundary-trapping falsification target `clm-h55fy1`** (`boundary-trapping-test.md`): the resistive mechanism's "sudden spike in transit drag" becomes, under the ruling, a **reactive reflection with no energy-shedding drag**. KEEP-BOTH axis.
- **Reachability: EXISTING DATA.** Pioneer 10/11, Voyager, New Horizons Doppler residuals already bound anomalous outer-system deceleration; the Pioneer anomaly is resolved as anisotropic thermal recoil (no vacuum-drag term needed) — consistent with the **reactive `n`-undefined (zero-drag)** prediction and in tension with the demoted `∝v` stall.

**D2 — Coherent reactive reflection vs incoherent thermalisation at the impedance step.**
- **Observable:** whether the boundary interaction is *phase-preserving/recoverable* (reactive `Γ`-reflection, energy returns to the body) or *irreversible/heating* (resistive stall thermalises KE into the lattice).
- **Reactive predicts:** phase-coherent partial reflection, `Γ = (Z_2−Z_1)/(Z_2+Z_1)`, energy conserved (§3.4). **Resistive predicts:** thermalised detritus, KE → heat.
- **Status:** [derived] qualitative discriminator; the reflection *magnitude* needs the `S`-step size (calibration).
- **Reachability: FEASIBLE.** Precision ranging of an outer-system probe across the transition; or the thermal/spectral signature of putative boundary detritus (is it dynamically cold — reactively parked — or shock-heated?).

**D3 — Structure spacing law: Newtonian `(q/p)^{2/3}` with NO lattice overlay.**
- **Observable (dimensionless):** the exponent and comb of belt/ring gap positions.
- **Both worlds predict:** `a_gap/a_J = (q/p)^{2/3}` (Kepler). AVE predicts **no additional comb** and **no exponent shift** (§4.1–4.3).
- **Status:** [derived] NULL. Peer-with-Newtonian.
- **Reachability: EXISTING DATA** — Kirkwood positions already `<0.3%` Newtonian. **Verdict already in: NULL** (no AVE-distinct content). This discriminator is *settled negative* and is listed to close the axis honestly, not as an open test.

**D4 — Vacuum Mach/Cherenkov drag-onset threshold `v_crit/c_ch = 2/π`.**
- **Observable (dimensionless):** the critical speed ratio at which a band-edge-coupled source begins radiating a lattice wake (drag turns on).
- **AVE predicts:** `2/π ≈ 0.637` for band-edge-coupled sources, rising to `1` for bandlimited (macroscopic) sources (§3.3). **SM/Lorentz predicts:** no vacuum-Cherenkov threshold at any `v < c`.
- **Status:** [derived], DIMENSIONLESS, lattice-universal — the band-map's cleanest AVE-distinct number. But **protected/unreachable** for ordinary and deep-space matter (bandlimiting + emergent Lorentz, §3.3), so it is a *forward* discriminator only at the band-edge-coupled frontier.
- **Reachability: UNREACHABLE** at the deep-space operating point (`v ~ 10⁻⁴ c`); conceptually reachable only by a probe that couples to `k ~ π/ℓ_node` modes (lattice-scale), which nothing macroscopic does. **The chord, if any, is this dimensionless ratio — but it is currently unfalsifiable at deep-space scales.** (Honest: this is where a band-map "chord" would live, and it does not touch the demoted sites.)

**D5 — Inter-channel speed ratios `c_bulk/c_shear = √2`, `c_P/c_shear = √(10/3)`.** *[FORK / FLAG — see §7]*
- **Observable (dimensionless):** the propagation-speed ratio of a scalar-longitudinal (bulk-dilatation) gravitational channel to the transverse-shear GW.
- **AVE band-map derives:** `√2` (bulk/shear) and `√(10/3) ≈ 1.826` (P-wave/shear) [derived from `K = 2G`]. The **observed transverse GW is the shear channel at `c`** (`einstein-field-equation.md:62–63,:84` [canon]) — consistent with GW170817 (`c_GW = c_EM` to `10⁻¹⁵`). The `√2·c` **scalar-longitudinal** mode is a *distinct* channel.
- **Status:** the `√2`, `√(10/3)` are [derived] band-map FORMS. But **the identification "bulk-dilatation channel ↔ an observable, radiating scalar-GW polarisation" is NOT established in the corpus.** Until it is, this is a **FORK**, not a clean discriminator — see §7 flag.
- **Reachability: EXISTING DATA** (LIGO/Virgo scalar-polarisation bounds) *conditional on* the unestablished identification.

**D6 — Cosserat-channel evanescent reach = one Compton length (`ξ_0 = c_κ/m_ω ~ ℓ_node`).**
- **Observable:** the range of the `(2,3)`-winding (charge) reactive coupling.
- **AVE predicts:** Yukawa/contact-range (`~10⁻¹³ m`), invisible at solar-system scale (§2.3, §4.4). This is the electron-orbital passband, not deep-space.
- **Status:** [derived] FORM; VALUE = calibration (`ℓ_node`). Confirms the §4.3 null (the winding channel cannot carry deep-space structure).
- **Reachability:** quantum/atomic-scale (the "electron orbitals" passband) — **not deep-space**; listed to locate where the winding channel's structure actually lives.

---

## §6 — Calibration-vs-derived ledger (consistency-vs-emergence tags)

| Quantity | FORM | VALUE | Class |
|---|---|---|---|
| `ℓ_node = ℏ/(m_e c)` | — | CODATA `m_e` imported | **calibration identity** (SI substitution; A47-family) |
| `ω_max = 2c/ℓ_node`, `f_max = c/(π ℓ_node)` | [derived] arccos band edge = [canon] Casimir row | calibrated via `ℓ_node` | consistency (FORM-match to canon) |
| `m_ω = √(4G_c/I_ω)` | [derived]/[canon] Cosserat gap | calibrated to `m_e` | consistency |
| `ξ_0 = c_κ/m_ω ~ ℓ_node` | [derived] evanescent length | calibration | consistency |
| `m_ω/ω_max = 1/2` | downstream of `ℓ_node ≡ λ̄_C` | — | **consistency (do NOT headline as emergent)** |
| `v_crit/c_ch = 2/π` | [derived] arccos min-`v_p` | dimensionless, `ℓ_node`-free | **manifestation** (theorem of the dispersion) |
| `c_bulk/c_shear = √2`, `c_P/c_shear = √(10/3)` | [derived] from `K = 2G` | dimensionless | manifestation — but observability gated by an unestablished identification (§7) |

**Headline discipline:** the only `ℓ_node`-free (calibration-independent) dimensionless content is `2/π`, `√2`, `√(10/3)`. Per the α-circularity lesson (any band-map "chord" must be a dimensionless ratio), these are the sole chord candidates — and all three are either unreachable at deep-space speeds (`2/π`) or gated on an unestablished sector-identification (`√2`, `√(10/3)`). **No emergence-class claim is headlined; the band-map's deep-space verdict is a clean null with one live boundary discriminator.**

---

## §7 — Deviations, contradictions (flag-don't-fix), OWED-FOLLOW-ONS

### Deviations from the SPEC / walk-record
- **The "~20 orders below the band edge" figure (walk-record §1d-ii, orchestrator-walk, non-canon) is an underestimate.** The derived separation with `ℓ_node = λ̄_C` is **28.5 orders (asteroid) → 34.9 orders (Oort)** (§4.2). Reported as a deviation; it **strengthens** the null (deeper sub-band ⇒ even more decisively featureless). Not a contradiction with canon (the "~20" was explicitly non-canon orchestrator-walk).
- **The walk-record's "below the band edge ⇒ evanescent" (clause ii) is precise only for the gapped Cosserat channel.** For the three gapless channels, low frequency is the *passband*, not a stopband; their reactive-ness comes from being **below the Mach/Cherenkov threshold** (§3.3), a *different* mechanism than evanescence. This lane derives both explicitly and does not conflate them. This refines (does not overturn) the walk-record — surfaced per flag-don't-fix.

### Contradictions FLAGGED (not fixed — Grant / auditor adjudication)
- **FLAG-1 (D5, sector-identification gap).** The band-map derives a **scalar-longitudinal `√2·c` bulk-dilatation channel** distinct from the transverse-shear GW at `c`. The corpus places the *observed* GW on the shear channel at `c` (`einstein-field-equation.md:62–63,:84` — no contradiction with GW170817 for the shear mode). **But the corpus has not stated whether the `√2·c` bulk channel radiates as an observable scalar-GW polarisation.** If it does, LIGO/Virgo scalar-polarisation bounds constrain it; if it is non-radiating (a pure near-field reactive channel), no constraint applies. **This fork is surfaced, not resolved** — it is a sector-ownership question (does the A1/bulk dilatation have a radiative far-field port?) for Grant/auditor, not something this lane silently reframes.
- **FLAG-2 (walk-record §3 handle-1 vs D1).** The walk-record frames D1 as "flips the vol4 boundary-trapping target `clm-h55fy1`." This lane confirms the *direction* (reactive → no `∝v` stall) but notes the vol4 target's status on `main` is **not edited here** (DERIVATION-lane fence). The relabel of `clm-h55fy1` from "drag-spike falsifier" to "reactive-reflection / zero-drag test" is an **owed KB follow-on**, not executed in this lane.

### OWED-FOLLOW-ONS (KB/tex propagation — FENCED this session; cleanup lanes own these trees)
1. **`clm-h55fy1` relabel** (`boundary-trapping-test.md`): drag-spike falsifier → reactive-reflection / zero-drag `v`-independence test (D1, FLAG-2). *Auditor lane lands; implementer surfaces.*
2. **Kirkwood-cavity-mode leaf annotation** (`kirkwood-gaps-cavity-modes.md`): tag the `(q/p)^{2/3}` account explicitly **consistency-class / peer-with-Newtonian** (currently silent on its Kepler-relabel status; §4.1). *Auditor lane.*
3. **D5 sector-identification fork** (FLAG-1): a `bulk-impedance-at-saturation-boundary.md` or gravity-sector note on whether the `√2·c` bulk-dilatation channel has a radiative scalar-GW port. *Grant-gated physics ruling first; then auditor lane.*
4. **Band-map canonical leaf** (if promoted): a `translation-circuit`-adjacent leaf carrying the four-branch table + the `2/π` drag-onset ratio. **Gated on Grant** — this lane mints nothing; promotion is a *separate* session (cross-repo/KB promotions happen in different sessions).

**None of items 1–4 are executed here.** The demoted-mechanism slot (§ walk-record) stays **open** (Rule 12 / A47 v11b): this band-map is a *new* lane with its own verification chain, not a refill of the demoted slot.

---

> **Derivation-doc provenance.** SPEC = walk-record `research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md` §5 (Grant 2026-07-19 ruling, transcribed there). All [canon] citations `grep -F` content-verified at HEAD `1be045a1`. Forms [derived] by standard lattice-dispersion algebra from [canon] inputs; values [calibration]-tagged via `ℓ_node = ℏ/(m_e c)`. Mints no `clm-`; propagates to no leaf; owed follow-ons fenced to §7. Companion: the demotion banners (`04_continuum_electrodynamics.tex:245`, `14_macroscopic_orbital_mechanics.tex:227`) and the docket continuation (`_orchestration/2026-07-10_rulings-docket.md`, this date).
