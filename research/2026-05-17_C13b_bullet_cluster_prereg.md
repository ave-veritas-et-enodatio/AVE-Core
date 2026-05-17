# C13b Bullet-Cluster Offset Derivation — Pre-Registration

**Status:** PREREG ONLY (no derivation performed). Surfaces 1 load-bearing physics-judgment call + 2 adjacent corpus-coherence flags. Per `ave-prereg` skill discipline.

**Date:** 2026-05-17
**Author:** agent + corpus-grep audit (agentId: a4c3924a8285b5960)
**Matrix row:** C13b-BULLET
**Closure-roadmap item:** §0.5 open scope-correction "Bullet-cluster offset distance derivation (C13b row)" pending

## Derivation target

Derive the AVE prediction for the spatial offset between baryonic matter (Chandra X-ray gas peak) and lensing peak (HST gravitational lensing) in the Bullet Cluster system 1E 0657-558, targeting match with empirical ~150 kpc projected (~25 arcsec at z = 0.30, ~1.14 Gpc distance), with collision time ~150 Myr post-pericenter at relative velocity ~4700 km/s.

## Corpus state

**Verdict: GREEN-FIELD with load-bearing physics tension.**

Per comprehensive cross-repo grep:
- **C13b row "qualitative-only" classification CONFIRMED MATCH** to actual corpus state. No leaf, chapter, or script derives the offset distance.
- **`simulate_bullet_cluster_fdtd.py` is mislabeled** — does NOT compute FDTD, TT-shockwave, Gordon metric, or offset distance. Computes pure kinematic-prescription + static MOND-saturation-halo superposition (~Vol 3 Ch 5 framing). Same anti-pattern class as the retired `vlbi_impedance_parallax.py`.
- **Two different corpus framings coexist** for bullet cluster mechanism: Vol 1 Ch 4 (TT-shockwave) vs Vol 3 Ch 5 (η_eff halo superposition). Already flagged as part of C13c META.
- **Empirical anchor numerics** (150 kpc, 25 arcsec, 4700 km/s, 150 Myr, z=0.30) **NOT in corpus** — would need to land first.

## Load-bearing physics tension

The Step 1.5 plumber-arithmetic ("150 kpc / 150 Myr ≈ 1000 km/s implied TT-shockwave propagation speed") **CONTRADICTS** the corpus's canonical $v_T = c$ result — confirmed unanimously across three loci:

- [`photon-propagation-baseline.md:16`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md): "$T_2$ (transverse photon): $c = \sqrt{G/\rho}$"
- [`k4-port-irrep-decomposition.md:109`](manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md): same
- [`de-broglie-standing-wave.md:236-240`](manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md): "$\boxed{c_S \equiv c}$"

If the substrate transverse wave speed is $c$, then a TT shockwave from a 150-Myr-old cluster collision would have propagated **46 Mpc** (not 150 kpc), contradicting the "still propagating in the cluster" observation by ~300×. So either:

- **(α) Propagating sub-luminal**: corpus needs a κ-coupling or Gordon-metric-drag mechanism that reduces effective $v_T$ at cluster scale by factor ~300 (no precedent in corpus)
- **(β) Standing-mode reframing**: lensing isn't tracking a *propagating shockwave* but a *coherent standing TT-mode* at the collision site that decays slowly via Q-factor + damping. Parallel to DAMA refresh-rate reframing (which similarly recast "propagating wave" → "coherent substrate-mode detection"). Picture: bell STILL RINGING from the strike, lensing tracks the standing acoustic mode that decays over ~150 Myr.
- **(γ) Wrong framing entirely**: bullet cluster offset is geometric (linear superposition of static halo-strain fields per Vol 3 Ch 5), not shockwave-derived. The Vol 1 Ch 4 TT-shockwave story is itself wrong; the right framing is Vol 3 Ch 5's η_eff halo superposition that the driver actually implements.

**This is the Q1 of the bullet cluster derivation — analogous to DAMA's Q1+Q2.** Needs Grant's physics-judgment call before solo derivation can proceed.

## Cross-repo precedents that may inform reframing

- **AVE-Fusion** [`vol_fusion/chapters/03_metric_catalyzed_fusion.tex:12`](../../../AVE-Fusion/manuscript/vol_fusion/chapters/03_metric_catalyzed_fusion.tex): invokes "a macroscopic, constructive acoustic-metric interference wave (a 3D standing Tensor Shockwave)" for fusion. **Standing-wave Tensor Shockwave** is the bell-still-ringing picture — directly relevant to interpretation (β).
- **AVE-Propulsion** [`vol_propulsion/chapters/04_superluminal_transit.tex:32-36`](../../../AVE-Propulsion/manuscript/vol_propulsion/chapters/04_superluminal_transit.tex): describes "Vacuum Impedance Boom" / Cherenkov-Unruh shock with explicit substrate-shockwave physics (Nyquist piling, lattice relaxation time $\tau = \ell_{node}/c$). Provides a corpus-precedent for substrate-shockwave physics that doesn't exist in AVE-Core.

## Three discriminator-bearing physics-judgment options for Grant (analogous to DAMA Q1+Q2)

**(α) Propagating sub-luminal TT shockwave**
- Requires deriving a $v_T$ reduction mechanism (κ-coupling at cluster scale? Gordon-metric drag in dense ICM medium?)
- Predicts lensing peak STILL PROPAGATING outward 150 Myr after collision
- Implication for COSINE-style cross-cluster comparison: different cluster ages → different offsets scaling with age
- Cleanest mechanism if substrate shows dispersive behavior at galactic-cluster scales

**(β) Standing TT-mode at collision site** (DAMA-template reframe)
- Recasts "propagating shockwave" → "coherent excited substrate mode that decays over ~150 Myr"
- Requires deriving Q-factor + damping timescale of cluster-scale TT mode
- Predicts lensing peak STATIONARY at original collision site (not propagating)
- AVE-Fusion precedent: "3D standing Tensor Shockwave" already in sibling corpus
- Most parallel to DAMA refresh-rate framing
- Plumber: struck bell still ringing, lensing = standing acoustic mode amplitude

**(γ) Wrong framing entirely — Vol 3 Ch 5 wins**
- Bullet cluster offset is geometric η_eff halo superposition (per Vol 3 Ch 5 and the existing `simulate_bullet_cluster_fdtd.py` driver)
- The Vol 1 Ch 4 TT-shockwave-on-Gordon-metric story is wrong / superseded
- Predicts offset frozen at "cluster centers passed through each other" geometry
- Closest to standard WIMP picture — minimal AVE-distinctive prediction
- C13c META gap would resolve toward "η_eff is the load-bearing operator; TT shockwave framing in Vol 1 Ch 4 is stale"

## Available structural ingredients (post-Grant adjudication)

| Ingredient | File:line | Available? |
|---|---|---|
| Gordon optical metric $g^{AVE}_{\mu\nu}$ | [`gordon-optical-metric.md:12-14`](manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md) | ✓ |
| Transverse refractive index $n = 1 - h_\perp$ | [`transverse-refractive-index.md:10-19`](manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/transverse-refractive-index.md) | ✓ |
| $h_\perp \propto 1/r$ static falloff | [`boundary-trapping-test.md:11`](manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/boundary-trapping-test.md) | ✓ static only |
| Einstein deflection $\delta = 4GM/bc^2$ (Gordon) | [`einstein-lensing-deflection.md:13`](manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/einstein-lensing-deflection.md) | ✓ static only |
| $\rho_{bulk} \approx 7.92 \times 10^6$ kg/m³ | [`lc-electrodynamics.md:29`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md) | ✓ |
| $v_T = \sqrt{G/\rho} = c$ | 3 loci (see above) | ✓ but constrains derivation |
| **TT-shockwave source term** (cluster collision → $h_\perp$) | None | ✗ MISSING |
| **TT-shockwave propagation equation** | None | ✗ MISSING |
| **TT-shockwave dispersion/attenuation at cluster scale** | None | ✗ MISSING |
| **Dynamic Gordon-metric strain → lensing offset** | None | ✗ MISSING |

## Adjacent corpus-coherence flag surfaced by audit

**$G_{vac}$ discrepancy across corpus** (NOT load-bearing for bullet cluster directly, but flagged):
- [`lc-electrodynamics.md:35`](manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md): $G_{vac} = m_e c^2 / \ell_{node}^2 \approx 5.48 \times 10^{24}$ Pa
- [`derived-numerology.md:52,56`](manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/derived-numerology.md): $G_{vac} = \rho_{bulk} \cdot c^2 \approx 7.11 \times 10^{23}$ Pa; explicitly says lc-electrodynamics value is wrong (cross-checked via $v_T = \sqrt{G/\rho} = c$)
- Factor 7.7 discrepancy; not corrected in lc-electrodynamics leaf
- This is a separate corpus-coherence cleanup item; should be queued

## Driver-script mislabel flag

`simulate_bullet_cluster_fdtd.py` does not compute FDTD, TT-shockwave, or Gordon metric. Same anti-pattern as the retired `vlbi_impedance_parallax.py`. Driver name is misleading; the script implements Vol 3 Ch 5's η_eff halo superposition (interpretation γ above), not Vol 1 Ch 4's TT-shockwave (Step 1.5 picture).

If Grant adjudicates interpretation (γ), the driver is already correct (just needs honest rename + scope note). If (α) or (β), the driver needs to be rewritten or supplemented with a TT-shockwave / standing-mode implementation.

Also: 3 sibling animation scripts (`animate_2d_bullet_cluster.py`, `animate_bullet_timelapse.py`, `extract_bullet_stills.py`) all use the same η_eff halo pattern. Same Class C overclaim cleanup we did for the other scripts likely applies here too — but the bullet-cluster ones may need waiting until the operator-choice adjudication.

## Discriminating outcomes (post-adjudication)

- **Outcome A — Grant picks (α) propagating sub-luminal**: 2-3 sessions to derive κ-coupling-reduced $v_T$ + propagation eq + offset prediction. Cross-validation: cluster-age-vs-offset scaling across multiple merging-cluster systems.
- **Outcome B — Grant picks (β) standing TT mode** (DAMA-parallel): 2-3 sessions to derive Q-factor + damping + standing-mode amplitude + offset extraction. Cross-validation: lensing peak amplitude should decay over time (~150 Myr) for systems of different ages. AVE-Fusion sibling-corpus precedent.
- **Outcome C — Grant picks (γ) wrong framing**: ~30 min to retire Vol 1 Ch 4 TT-shockwave framing as stale; promote Vol 3 Ch 5 η_eff halo as canonical; update C13b matrix row + C13c META; clarify driver scope-correction. Closest to existing driver behavior; least AVE-distinctive but cleanest scope.
- **Falsifier**: if all three interpretations produce predictions that conflict with the bullet-cluster geometry (e.g., offset wrong sign, wrong scaling with collision time, wrong magnitude beyond fit-class), the underlying TT-shockwave / η_eff framings for DM-class observables need fundamental revision.

## Lane attribution

Prereg landed in research/ branch `analysis/divergence-test-substrate-map`. Honest-flag-the-gap status; no derivation attempted. Awaits Grant's physics-judgment call on (α)/(β)/(γ) before any solo derivation session.

## Plumber question for Grant (analogous to DAMA refresh-rate session)

In your physical intuition for the K4 substrate at galactic-cluster scale:

- Is the bullet-cluster lensing peak **PROPAGATING** outward from the collision site (interpretation α: substrate behaves dispersively at cluster scale, reducing effective $v_T$)?
- Is it **STANDING** at the collision site, with amplitude slowly decaying (interpretation β: cluster collision excited a long-lived coherent TT mode; lensing tracks the standing mode amplitude; ~150 Myr is the natural Q-factor decay time)?
- Or is the TT-shockwave story wrong and the offset is just **GEOMETRIC** superposition of static η_eff halos rigidly co-moving with cluster centers (interpretation γ: Vol 3 Ch 5 wins, Vol 1 Ch 4 stale)?

Each leads to a clean 2-3 session derivation path. None requires multi-month work.
