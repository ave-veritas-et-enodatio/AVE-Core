[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.15 Falsification Tests

Chapter 15 of the Vol 9 datasheet documents the substrate-physics falsification programme. Every load-bearing substrate-physics claim in this datasheet is tied to at least one bench-falsifiable or observational kill-switch. Vol 9 is a synthesis chapter — no falsification entry originates here; each is routed to its canonical leaf in the cross-volume falsification index.

## Canonical cross-volume home

The canonical cross-volume falsification catalog lives at:

> → Primary: [Appendix: Unified Index of Experimental Falsifications](../../common/appendix-experiments.md) — INVARIANT-S3 cross-volume canonical home (clm-t5ybqw)

> → Primary: [Divergence-test substrate map](../../common/divergence-test-substrate-map.md) — operational tracking layer (33 rows: A1-HOPF, A2-SAGNAC, B7-PONDER-05, C15-CLEAVE-01, C17-PROTOCOL-11-SAGNAC-WIND, …)

## Forward-Prediction Test Register (chord-vs-echo)

The bench/null-result programme below tests the substrate's *internal* consistency. The **forward-prediction register** is the orthogonal axis: which predictions are AVE-distinct *chords* that experiment can actually discriminate against SM/GR/ΛCDM, and which are *echoes* (a match built in by construction). The classification axis is the FORM-deriving / VALUE-importing frame ([`form-deriving-value-importing.md`](../../common/form-deriving-value-importing.md); the chord/echo definitions `def-ch0rd1` / `def-ech0v1` at [`vocabulary-register.md`](../../common/vocabulary-register.md)). Because *every dimensionful magnitude is an echo by construction*, an AVE-distinct discriminating prediction lives only in (1) **FORM-EXISTENCE** divergences (a structure the SM vacuum lacks) and (2) **FORCED DIMENSIONLESS RATIOS** that do not dissolve into α, G, or m_e.

Three test classes:

- **BANKABLE** — a forced dimensionless ratio that gives an SM-divergent, observable number at an existing or near-term instrument. The discriminator is the *number*, not its provenance.
- **FORM-EXISTENCE-FALSIFIER** — a structural feature (saturation / longitudinal scalar / native birefringence) the SM vacuum lacks; the test probes the *existence* of the structure. The magnitude itself is an echo, so the falsifier lives in the *coefficient ratio*, not the field-law.
- **CONSISTENCY-ECHO** — a forced ratio whose root is the ν_vac = 2/7 ← K=2G family (itself GR-imported), or a dimensionful value that rides α/G/m_e. A match is corroborative but tests an imported value's consequence, not an independently-forced AVE number. Reported peer-mapped-honestly, never headlined as emergence.

| Prediction | Class | SM / GR counterfactual | Discriminator observable | Data status | Canonical source |
|---|---|---|---|---|---|
| **Iron-Kα disk-edge** r_in = 7GM/c² (= 3.5 r_s) | BANKABLE (forced ratio, ν_vac=2/7) | GR ISCO at 6GM/c² | inner-accretion-disk edge via X-ray Fe-Kα reflection / kHz QPOs (matter observable, NOT the GR-standard photon ring) | untested; surviving discriminator per 2026-05-16 scope audit | [`divergence-test-substrate-map.md`:143,145](../../common/divergence-test-substrate-map.md) (C1-BH-RING row :452); [`ave-merger-ringdown-eigenvalue.md`](../../vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md) |
| **g\* = 7³/4 = 85.75** effective DOF cutoff | BANKABLE (forced ratio, ν_vac=2/7) | SM g\*,SM = 106.75 at EW scale (24 more fermionic DOF) | Ω_GW +7.6% (LISA/DECIGO); EW expansion −10.4% (CMB-S4); EW latent heat −20% (FCC-ee/CEPC) | untested; awaits LISA / CMB Stage-4 / FCC-ee | [`divergence-test-substrate-map.md`:245,247](../../common/divergence-test-substrate-map.md) (C12-G-STAR row :470); [`g-star-derivation.md`:14-16](../../vol2/nuclear-field/ch10-open-problems/g-star-derivation.md) |
| **Vacuum birefringence COEFFICIENT** ~10⁷× QED (matched differential) | FORM-EXISTENCE-FALSIFIER (saturation; echo-magnitude) | QED differenced Euler–Heisenberg 3/45, α²-loop-suppressed coefficient (both E²-leading) | the matched par−perp differential ratio δn_AVE/δn_QED = 7.5/α³ ≈ 1.93×10⁷ at any field (AVE −½A² vs QED 3/45; single-arm 1/(4 a_EH α³) ≈ 4.14×10⁶ = traceability); a QED-sized coefficient falsifies AVE | not resolved at current high-intensity-laser / PVLAS bounds | [`divergence-test-substrate-map.md`:448,67](../../common/divergence-test-substrate-map.md) (B1-VAC-BIREFRINGE); [`epistemology-kill-switches.md`](../../vol4/falsification/ch11-experimental-bench/epistemology-kill-switches.md) (clm-pp3qwf) |
| **sin²θ_W = 2/9** | CONSISTENCY-ECHO (forced ratio, 2/7-family-adjacent) | SM: a fit input (running, ~0.231 at M_Z) | weak mixing angle; AVE forces the dimensionless 2/9 | consistent at tree level; not a forward discriminator | [`form-deriving-value-importing.md`:105](../../common/form-deriving-value-importing.md); [`full-derivation-chain.md`](../../common/full-derivation-chain.md) |
| **PPN /7 couplings** (1/7, 2/7, 9/7) | CONSISTENCY-ECHO (ν_vac=2/7 ← K=2G, GR-imported) | GR PPN with γ=β=1 | light/matter deflection ratios; Mach-Zehnder n_s=9/7 vs n_t=2/7 split | C11-MACH-ZEHNDER live-fire 249.64 rad (sim); ν_vac triangulation with C1+C12 | [`divergence-test-substrate-map.md`:469](../../common/divergence-test-substrate-map.md) (C11); [`form-deriving-value-importing.md`:105,113](../../common/form-deriving-value-importing.md) |
| **Mass sector** (m_p −0.002%, lepton ladder) | CONSISTENCY-ECHO (dimensionful, rides m_e/ℓ_node) | SM: Yukawa fits | particle masses as ℓ_node geometric ratios | closed ECHO-final (near-saturation chord-residual closed-negative, PR #311) | [`form-deriving-value-importing.md`:74-77](../../common/form-deriving-value-importing.md) |

> **The single independent operating-point test** that would convert the {α, G} story from echo to chord is 𝒥_cosmic (CMB axis-of-evil → Ω̂_freeze; the three-route u₀\* commitment in §three-route below). **Pass = chord, fail = echo.** All other forced-ratio discriminators above are largely ν_vac = 2/7-rooted, and ν_vac = 2/7 ← K=2G is GR-imported — so they test the *consequences* of an imported value. The cleanest AVE-distinct chords are the FORM-EXISTENCE rows (birefringence) plus any forced ratio whose root is not the 2/7 family.

### Detection-principle scope (lossless-reactive ⇒ wave-structure, never calorimetric loss)

Per Axiom 3 the substrate is lossless-reactive, so every AVE-distinct vacuum modification is a change in the substrate's *reactance* / wave-structure and **never** appears as net absorptive or calorimetric attenuation of the probe. This reactive signature manifests across **three** lossless observable families, and the register above draws from all three:

1. **Phase / polarization** — birefringence ellipticity (δn_bir ≈ −½ A², read as accumulated retardance ψ), optical-activity polarization-plane rotation, and the (q·ℓ_node)⁴ dispersion anisotropy. These *dominate for a uniform, weak probe* because the observables ARE phase differences.
2. **Amplitude / timing reflection at impedance discontinuities** — the Γ(V) vacuum-impedance mirror, the Γ→−1 shear/bulk gravitational-wave echo, the achromatic-lens matched condition (Γ=0), and the C(E) capacitance plateau. A lossless medium still reflects *amplitude* at an impedance step; reflection is reactive, not dissipative.
3. **Spectral frequency-conversion under nonlinear drive** — third-order intermodulation (IM3), plus the mass-spectrum / pair-yield / thrust facility-class falsifiers. Energy moves between frequencies, not into heat.

The discriminating axis across all three is impedance **symmetry** (Γ=0 matched vs Γ≠0 mismatched), which is *orthogonal to dissipation*. **Caution:** losslessness scopes OUT absorptive / heating channels — it does **not** imply phase-only detection. Second-harmonic generation, four-wave mixing, and parametric amplification are all lossless amplitude / spectral effects, so the absence of calorimetric loss is consistent with a strong amplitude or spectral signature, not only a phase one. (Consistent with the birefringence leaf [`vacuum-birefringence-e4.md`](../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md): the birefringence *readout* is a polarization-phase difference because the *observable* is a phase difference — one of the three families, not the whole detection principle.)

## Per-test canonical leaves cited in the chapter

### Bench-scale kill-switches

- **PONDER-05** DC-biased quartz, 27.4% $\varepsilon_{eff}$ collapse at ~30 kV — ⚠ **consistency-class material varactor analog of the kernel SHAPE, NOT a vacuum-kernel kill-switch** (2026-06-04 per-node-conflation correction): $V_{DC}/V_{yield}$ is a **per-node** ratio, and at 30 kV across real quartz the vacuum per-node $A_0 = 10^{-7}$–$10^{-10}$ → vacuum collapse ~0. The 27.4% is the quartz material's own voltage-coefficient; the vacuum-kernel falsifier is facility-class ($\sim 8\times10^{16}$ V/m). Cascade to Ax4 DECOUPLED (a null quartz effect falsifies quartz dielectric data, not the vacuum kernel). Per `vol4/claim-quality.md:51`.
  - [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) — substrate-physics derivation (the §13/§14 amplitude-shape edifice anchors on $a = 0.687$ as the operating point — see borderline-flag note in the 2026-06-04 corrections result doc)
  - [`vol4/falsification/ch11-experimental-bench-falsification/open-source-hardware.md`](../../vol4/falsification/ch11-experimental-bench-falsification/open-source-hardware.md) — open-source PCBA build guide
  - Divergence-test row B7-PONDER-05 (reclassified consistency-class)
- **HOPF-01** chiral antenna $S_{11}$ torus-knot shift ($\Delta f/f = \alpha\cdot pq/(p+q)$):
  - [`vol4/falsification/ch11-experimental-bench-falsification/open-source-hardware.md`](../../vol4/falsification/ch11-experimental-bench-falsification/open-source-hardware.md) (clm-wzezvt)
  - [`vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md`](../../vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md) — HOPF-02 mitigation of pilot-board mutual-coupling confound
  - Divergence-test row A1-HOPF
- **Sagnac-RLVE** rotational lattice mutual-inductance ($\Psi_{W/Al} = 7.15$) — **RETIRED forward "kill-switch" → corroborative-null (2026-06-03 audit)**; surviving piece is the paired W-vs-Al $\Psi$ self-consistency scaling check (Earth-as-rotor $+7\times10^{-4}$ bias excluded by RLG geodesy; `AVE-PONDER/research/2026-06-03_sagnac-rlve-fog-question-verdict.md`):
  - [`vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md`](../../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) (exp-rth12t status pending; strengthens clm-qx9bb8; scope-correction header 2026-06-03)
  - Divergence-test row A2-SAGNAC
- **CLEAVE-01** femto-Coulomb electrometer ($\xi_{topo}$ kill-switch):
  - [`vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md`](../../vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) (clm-ydksh6, exp-742kv5 status pending)

### Right-handed neutrino joint kill-switch

- [`vol4/falsification/ch11-experimental-bench-falsification/epistemology-of-falsification.md`](../../vol4/falsification/ch11-experimental-bench-falsification/epistemology-of-falsification.md) (clm-gw2wgc, clm-om0rtq, clm-pp3qwf)
- [`vol4/falsification/ch11-experimental-bench/epistemology-kill-switches.md`](../../vol4/falsification/ch11-experimental-bench/epistemology-kill-switches.md) (mirror)
- [`vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md`](../../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md) (clm-gw2wgc)
- [`vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm — joint constraint via $\gamma_c$)

### Null-result tests

- **Quasar α-variation (SYM-class null):** [`vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) (clm-3zz0f6)
- **Schwinger pair production at $E_S$:** [`vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md`](../../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) (clm-ezai5b); [`vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md`](../../vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md) (clm-lj4ok5)
- **Vacuum birefringence COEFFICIENT discriminator** (~~$E^4$ vs $E^2$ slope~~ retracted false-falsifier; both $E^2$-leading, ratio $\sim 10^6\times$ QED — Rule-12 correction 2026-06-04): [`vol4/falsification/ch11-experimental-bench/epistemology-kill-switches.md`](../../vol4/falsification/ch11-experimental-bench/epistemology-kill-switches.md) (clm-pp3qwf)
- **Static-Sagnac galactic-wind anisotropy (corroborative null):** [`vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md`](../../vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md); [`vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md); divergence-test row C17-PROTOCOL-11-SAGNAC-WIND
- **GRB photon dispersion (Trans-Planckian discriminator):** [`vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md`](../../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md) (clm-gw2wgc)
- **Cosmic chirality 8-channel axis:** [`common/omega-freeze-cosmic-grain-cascade.md`](../../common/omega-freeze-cosmic-grain-cascade.md) (clm-dsb560, clm-a7cbqq, clm-pe8lpx, clm-fndptx)

### Three-route $u_0^*$ falsifiability

- [`common/omega-freeze-cosmic-grain-cascade.md`](../../common/omega-freeze-cosmic-grain-cascade.md) §1 (clm-dsb560)
- `src/ave/core/constants.py` header preamble lines 18–24 (three-route framework commitment)
- Vol 9 Ch.12 cosmological characteristics §three-routes

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/15_falsification_tests.tex` — chapter populated 2026-05-28 (Wave 3 of Vol 9 buildout). Synthesis chapter; no substrate-physics derivation originates here. All canonical-leaf cross-references resolve to the per-test sources listed above.

## Evidence-framing discipline

Per `ave-evidence-framing-discipline`: no entry in this chapter is framed as "validated" or "confirmed". Status uses the bench-discipline vocabulary:

- "Not yet observed" — predicted observable not detected at any current bound
- "Current bounds consistent with prediction" — existing data within substrate-predicted range (typically null where substrate predicts null)
- "Pending bench measurement" — apparatus in fabrication or paper-stage; first measurement not yet performed
- "Predicted at $E_S$; terrestrial $E$ inaccessible" — substrate positive prediction applies at unreachable regime; current observation is the predicted null

---
