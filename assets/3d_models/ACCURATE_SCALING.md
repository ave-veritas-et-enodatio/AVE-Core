# Accurate Scaling of the Particle STL Models — Scope Note

**Status (2026-06-08, §43; scale-definition shore-up 2026-06-08):** the STL
meshes in this directory are **TOPOLOGY / RENDERING demos at an arbitrary
UNIFORM scale.** They do **not** encode physical particle sizes or physically
correct relative scales. This note specifies what accurate scaling *would*
require and why a single physical-scale render is currently intractable. The
**scale/size vocabulary** it depends on is now pinned in "The clarified
scale/size definition set" (Definitions 1–6, each `verify-before-cite`'d and
class-tagged); the full axiom-derived soliton-size leaf remains a separate,
still-gated effort.

## Why the old "physically correct relative scales" claim was retracted

`generate_particle_stl.py` sets every mesh's major radius from

```
r_opt = κ_FS / c          (c = torus-knot crossing number)
```

The retracted header treated `r_opt` as a **length in ℓ_node units** (e.g.
"baryons are ~5 ℓ_node", "electron:proton ~1:31"). That is **false**: per
`src/ave/core/constants.py:683-687`, `κ_FS = 8π` is a pure geometric constant,
and `r_opt = κ_FS/c` is a **DIMENSIONLESS coupling-budget ratio** — *not* a
length, *not* a confinement radius, *not* "N lattice spacings." Baking it into
STL vertex coordinates produced a proton mesh with a ~6.38 pm bounding box,
versus the measured proton charge radius **D_p ≈ 0.841 fm** — roughly
2300–4600× too large. The numbers in the mesh are a topology rendering, nothing
more.

No mesh was regenerated and no vertex value was changed in the §43 fix — the
correction is a **RELABEL**, because a physically-scaled render is intractable
(below).

## The clarified scale/size definition set (2026-06-08)

This section shores up the **scale/size vocabulary** this reference depends on.
It is **not** the canonical soliton-size derivation — the full axiom-derived KB
soliton-size leaf is a **separate, still-gated effort** (see "What accurate
scaling awaits"). Each definition below is tagged by **structural class**
(SOLID/SUPPORTED · SYNTHESIS · CORRECTION · OPEN-GAP) and by
**consistency-vs-emergence class**, and every file:line was re-verified
(`verify-before-cite`) before inclusion. One sub-claim **failed verification**
and is recorded as a flagged OPEN item, **not** canonized (see Definition 4).

> **§47 vocabulary discipline (locked):** never conflate the **spatial-Brillouin
> axis** (sub-node spatial features, real-space wavenumber `q → π/ℓ_node`) with
> the **phase-carrier axis** (the internal winding `ω = mc²/ℏ`). They coincide
> numerically at `c/ℓ_node` but are physically distinct geometries. Likewise
> never write `r_opt` without specifying which of its two meanings (Definition 3).

### Definition 1 — NODE = the spatial Nyquist / Brillouin cutoff `k_max = π/ℓ_node`

- **Class: SOLID.** **Consistency-vs-emergence: MANIFESTATION** (Axiom 1 lattice
  pitch → standard Nyquist/Whittaker-Shannon cutoff applied to the substrate).
- The lattice pitch `ℓ_node` makes `𝓜_A` a spatial Nyquist sampling grid; the
  maximum supportable spatial frequency without aliasing is the Brillouin
  boundary `k_max = π/ℓ_node`.
- **Verify (verbatim):** `manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md:10`
  — *"it acts as a spatial Nyquist sampling grid. The maximum spatial frequency
  the lattice can support without aliasing is the Brillouin boundary:
  `$k_{max} = \pi / \ell_{node}$`."*
- **Role here:** this cutoff is the **dividing line** between the two
  coordinate-space sizes of Definition 2 — at/above the node vs sub-node.

### Definition 2 — the TWO coordinate-space sizes (node-Nyquist resolution)

- **Class: SYNTHESIS** (coherent reorganization on a supported spine — the node
  cutoff of Def 1 plus the A46 axis-distinction below; not itself a new result).
  **Consistency-vs-emergence: CONSISTENCY** (a discipline guard, not an emergence
  claim).
- Splitting on the node (Def 1) gives two distinct coordinate-space "sizes":
  1. a **real-space resolved lattice body** — structure at/above the node, a
     lattice-extended object the render primitive can represent;
  2. a **sub-node scale** — structure below the node (e.g. the proton's
     `0.84 fm` charge-core), which lives *inside* one node, below the render
     primitive.
- ★ **A46 CAVEAT (load-bearing — do NOT fuse the axes):** the sub-node
  *spatial-Brillouin* axis (real-space wavenumber `q → π/ℓ_node`) is **physically
  distinct** from the *phase-carrier* axis (the `(2,3)`/`(2,5)` internal winding,
  `ω = mc²/ℏ`). They coincide numerically but measure different things.
- **Verify (verbatim):** `research/2026-06-08_highE-winding-aliasing-prereg.md:68`
  — *"The hypothesis lives on the **internal-winding carrier axis** (`ω = mc²/ℏ`);
  the C7-GRB falsifier lives on the **real-space wavenumber axis**
  (`q → π/ℓ_node`). They coincide numerically at `c/ℓ_node` but are physically
  distinct geometries."* And `:112` — *"Any test that compares a real-space
  lattice-Cartesian measurement against a phase-space φ²/winding prediction is
  A46-uninformative and is pre-disqualified."*

### Definition 3 — `r_opt` names TWO distinct quantities (the §47 clarity-killer)

- **Class: CORRECTION + SYNTHESIS** (a vocabulary disambiguation of a live
  symbol collision). **Consistency-vs-emergence: IDENTITY / CONSISTENCY**
  (dimensional-honesty disambiguation, not an emergence claim).
- **Meaning-A — coupling-budget ratio (proposed name: `κ_share`).** The
  **DIMENSIONLESS** ratio `κ_FS / c` (`c` = torus-knot crossing number). It is
  **NEVER** multiplied by `ℓ_node` and carries no length dimension.
  - **Verify:** `src/ave/core/constants.py:683-687` — `KAPPA_FS_COLD = 8.0 * pi`
    declared *"a pure geometric constant"* (dimensionless); reinforced by the
    `:697-699` relabel comment — *"The crossing number c sets the soliton's
    DIMENSIONLESS coupling-budget ratio (NOT a length / 'confinement radius')."*
  - `κ_share` is a **proposed coin** to give Meaning-A its own name: **0 corpus
    hits confirmed** (grep `kappa_share`/`κ_share` across manuscript/src/research/
    assets returns empty), so the term is free to adopt.
- **Meaning-B — a genuine envelope length (proposed name: `r_env`).** A real
  **length** (soliton HWHM / tube-radius fit-parameter), which DOES carry a
  length dimension and DOES scale with the lattice.
  - **Verify (it exists):** `src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py:76-78`
    uses `r_opt` as the **radial envelope length-scale** `r` in the power-law
    hedgehog envelope `A·π / (1 + (ρ_tube / r_opt)²)`; and
    `src/scripts/vol_1_foundations/r10_path_alpha_v14e_seven_mode_seed.py:75,133`
    sets `HORN_R = 2.0` (horn-torus radius in **lattice cells**) and literally
    `r_opt = HORN_R`; and
    `src/scripts/vol_1_foundations/validate_cosserat_alpha_via_ch8_ratios.py:42`
    takes `r = HWHM of |ω| radial profile`.
  - ⚠ **The live collision:** the SAME symbol `r_opt` is the dimensionless
    `κ_FS/c` in `constants.py:687` **and** a lattice-cell length in the
    eigenmode drivers above. That is the clarity-killer this definition fixes —
    Meaning-A → `κ_share`, Meaning-B → `r_env`; never bare `r_opt`.

### Definition 4 — the electron is NOT a cube (de-conflate identity from the FDTD attractor)

- **Class: CORRECTION** (de-conflation), with **one sub-claim that FAILED
  verification and is held OPEN, not canonized** (below).
  **Consistency-vs-emergence: IDENTITY** (electron = `0₁` unknot, axiom-derived)
  **+ MANIFESTATION** (the cubic attractor is an empirical FDTD substrate
  signature).
- **VERIFIED — the electron's real-space identity is the `0₁` unknot (a closed
  flux-tube LOOP), not a cube.** `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md:22`
  — *"Real-space topology: `$0_1$` unknot — the simplest closed flux-tube loop at
  minimum ropelength `$2\pi$` on the K4 lattice. Tube circumference `$\ell_{node}$`,
  tube radius `$\ell_{node}/(2\pi)$`, loop length `$2\pi \cdot \ell_{node}$`."*
- **VERIFIED — the "cubic envelope" is a DIFFERENT object: the FDTD
  saturation-collapse attractor.** It is the seeded-near-saturation field's
  attractor, **cardinal / `[100]`-face-extremal**, and is an empirical substrate
  signature — NOT the electron's identity.
  - `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cubic-k4-empirical-anisotropy.md:11`
    — *"When the K4 substrate collapses into saturation regime (`$A^2 \to 1$`),
    the bipolar saturated attractor exhibits **cubic K4 anisotropy** — NOT
    spherical, NOT isotropic"*; `:67` — *"6 face-centered protrusions (one per
    face of the K4 unit cube)"*; `:19` — `±x̂, ±ŷ, ±ẑ` preferred directions.
  - `manuscript/ave-kb/common/trampoline-framework.md` §6.3 (line 804) —
    *"The cubic K4 anisotropy at saturation collapse (empirical, 2026-05-14)."*
  - The associated `√2` is a **propagation-SPEED ratio**, NOT an amplitude
    rolloff: `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md:11`
    — *"The wavefront **speed** along cardinal axes … is `$v = c \cdot \sqrt{2}$`
    … Along diagonal axes … the speed reduces to `$v = c$`."* Same `T_d`
    symmetry, two observables (saturated → cubic envelope; linear → speed split,
    per `cubic-k4-empirical-anisotropy.md:80`).
- ❌ **FAILED VERIFICATION — held OPEN, NOT canonized:** the proposed positive
  claim *"the electron's real-space envelope is **SPHERICAL** (zitterbewegung
  time-average)"* could **not** be verified at the cited
  `electron-identification.md:22-25`. Those four lines give the `0₁` unknot
  (a loop), the `(2,3)` Clifford-torus *phase-space* winding, the self-saturated
  TIR cavity, and the `T₂` Cosserat core — and contain **no "spherical," no
  "zitterbewegung," no "time-average."** A repo-wide grep finds "zitterbewegung"
  only in `research/2026-06-07_electron-interstitial-rotor-synthesis.md` tied to
  the **rotor = Compton-clock** (tagged identity/consistency), **not** to a
  spherical real-space envelope. Per the `verify-before-cite` governing rule this
  sub-claim is **flagged, not written as fact**: the verified real-space shape is
  the `0₁` unknot LOOP (tube radius `ℓ_node/(2π)`); whether its zitterbewegung
  time-average is spherical is an **unverified synthesis awaiting a real citation**.

### Definition 5 — OPEN GAPS (flag-don't-fix — recorded, NOT resolved here)

- **Class: OPEN-GAP** (×3). **Consistency-vs-emergence: n/a** (these are flags,
  not claims). Per Rule 6 / flag-don't-fix these are surfaced for Grant
  adjudication and are **not** silently resolved in this reference.
- **(a) Cutoff-as-sphere vs the real K4/diamond Brillouin ZONE.** Def 1's
  `|k| < π/ℓ_node` is written as an **isotropic sphere** everywhere, but the K4
  (chiral diamond) Brillouin zone is a **truncated octahedron** (L-point at
  `[111]`). The corpus self-flags this:
  `manuscript/ave-kb/vol1/claim-quality.md:820` — *"Confirm band-limitedness and
  the RKHS reproducing kernel explicitly for the **chiral-K4 Brillouin zone**
  rather than a generic cubic Nyquist grid"*; and `:1528` — *"State whether the
  cutoff is a **hard sphere `|k|<π/ℓ_node`** or the **first Brillouin zone of the
  K4 lattice** (the geometry changes the numerical prefactor)."* (NB: this flag
  is at `:1528`, off-by-one from the briefed `:1527`.)
- **(b) Proton multi-node vs single-node — a live corpus contradiction.**
  `manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex:40` — *"The `$6^3_2$`
  Borromean knot **spans multiple fundamental nodes**."* versus
  `src/scripts/vol_6_periodic_table/simulations/semiconductor_binding_engine.py:68`
  — *"the entire nucleus exists inside a **single saturated lattice node**
  (`ℓ_node ≈ 386 fm`)."* Both are stated as fact in their own files; this
  reference does **not** adjudicate which holds.
- **(c) Exact vertex / anisotropy attenuation is uncomputed.** The
  geometry-dependent numerical prefactor (sphere vs truncated-octahedron, and the
  cardinal-vs-diagonal anisotropy magnitude) is flagged as **uncomputed** —
  `claim-quality.md:1528` ("the geometry changes the numerical prefactor") and
  the empirical-only status of `cubic-k4-empirical-anisotropy.md`.

## The five distinct length scales (and one non-length)

A faithful "physical scale" render would have to reconcile quantities that live
at wildly different magnitudes — and one of them is not a length at all:

| # | Scale | Electron (c=3) | Proton (c=5) | Notes |
|---|-------|----------------|--------------|-------|
| 1 | Real-space resolved lattice body | `0₁` unknot loop, tube radius `ℓ_node/(2π)` (Def 2/4) | **sub-node** (see #2; multi-vs-single-node OPEN, Def 5b) | The structure **at/above the node** (Def 2). Electron: the `0₁` unknot LOOP, **not a cube** (Def 4). The full saturated-core "size" observable is the still-gated KB leaf. |
| 2 | Charge radius `D_p` | ~0 (point-like in scattering) | **0.841 fm** = 4λ_p | Proton: Pohl 2010 muonic-H; see `manuscript/ave-kb/.../proton-identification.md`. |
| 3 | Compton wavelength `ℏ/mc` | **386 fm** (= ℓ_node) | **0.210 fm** (= λ_p) | Reduced Compton; electron's *equals* the lattice spacing. |
| 4 | Lattice spacing `ℓ_node` | **386.16 fm** | 386.16 fm | `ℏ/(m_e c)`; the same for every particle. |
| 5 | `r_opt = κ_FS/c` → propose `κ_share` (Def 3) | 8.317 (= κ_FS/3) | 4.990 (= κ_FS/5) | **DIMENSIONLESS coupling-budget ratio — NOT a length.** This is Meaning-A of `r_opt`; rename to `κ_share`. Distinct from the genuine envelope length `r_env` (Meaning-B). What the STLs currently use as their uniform mesh scale. |

## Why a single physical-scale render is intractable

1. **The proton body is SUB-NODE.** The only measured proton size — charge
   radius `D_p = 0.841 fm` — is **≈460× smaller than ℓ_node = 386 fm**. A
   physically-scaled proton is smaller than a single lattice cell, so there is
   nothing to render as an extended lattice object. The torus-knot topology
   lives *inside* one node, below the rendering primitive.

2. **"Size" is measure-dependent.** By Compton wavelength the **electron is
   LARGER** (386 fm vs the proton's 0.21 fm). By charge radius the **electron
   is SMALLER** (point-like vs the proton's 0.841 fm). There is no single
   scalar "diameter" that orders the particles consistently, so no single
   uniform scale can be "the" physical scale.

3. **`r_opt` is not a length.** The quantity the meshes are actually built from
   (scale #5) carries no length dimension, so it cannot anchor a physical
   render even in principle.

## What accurate scaling awaits

This note **shores up the scale/size vocabulary** (Definitions 1–6 above) and
**flags the physics** for the KB — it is **not** the canonical soliton-size
derivation. Faithful relative scaling still **awaits the canonical soliton-size
leaf**: a single, axiom-derived, dimensionally-honest "size" observable for a
saturated topological soliton. **That leaf is a separate, still-gated effort**
(its canonical home is the **Vol 9 Vacuum Datasheet** — `ch1-general-description`
for identity, `ch14-phase-diagrams` for the regime maps; both verified to exist).
Open sub-question, explicitly **flagged not resolved**: which of scales #1–#4
(real-space resolved body, charge radius, Compton wavelength, or lattice spacing)
is the physically-correct render diameter — and whether the impedance-taper
radial width (`entanglement_thread.impedance_taper_profile`) should track it.
The Definition 5 OPEN GAPS (sphere-vs-Brillouin-zone, multi-vs-single-node,
uncomputed anisotropy prefactor) are **prerequisites** for that leaf and are
**not** resolved here.

Until that definition lands, **these STLs are explicitly topology demos.** Use
them to inspect knot type, crossing number, chirality, and link structure —
**not** to read off particle sizes or size ratios.

## Provenance

- §43 STL dimensional-bug audit (proton STL ≈6.38 pm bbox vs D_p = 0.841 fm).
- `src/ave/core/constants.py:683-687` — `κ_FS = 8π` declared a pure geometric
  constant (dimensionless).
- Sibling propagation: `analysis/2026-06-08-ropt-dimensional-propagation`
  relabeled the same `r_opt`-as-length error across the KB + `constants.py` +
  `faddeev_skyrme.py` (10 sites).

### Scale/size definition shore-up (2026-06-08, `verify-before-cite` ledger)

Every citation in "The clarified scale/size definition set" was re-verified
before inclusion. Result:

- **Def 1** SOLID — VERIFIED verbatim `paley-wiener-hilbert.md:10`.
- **Def 2** SYNTHESIS — A46 caveat VERIFIED verbatim at
  `research/2026-06-08_highE-winding-aliasing-prereg.md:68` + `:112`.
- **Def 3** CORRECTION — `κ_FS=8π` dimensionless VERIFIED `constants.py:683-687`;
  `r_env`-as-length VERIFIED at `tlm_electron_soliton_eigenmode.py:76-78`,
  `r10_path_alpha_v14e_seven_mode_seed.py:75,133`,
  `validate_cosserat_alpha_via_ch8_ratios.py:42`; `κ_share` 0-corpus-hits
  CONFIRMED.
- **Def 4** CORRECTION — `0₁` unknot VERIFIED `electron-identification.md:22`;
  cube-as-saturation-attractor VERIFIED `cubic-k4-empirical-anisotropy.md:11,19,67`,
  `trampoline-framework.md` §6.3 (:804), `photon-propagation-baseline.md:11`
  (√2 = SPEED ratio). **❌ FAILED VERIFICATION:** the "spherical (zitterbewegung
  time-average)" envelope sub-claim is **not** supported at the cited
  `electron-identification.md:22-25` — recorded as a flagged OPEN item,
  **not canonized**.
- **Def 5** OPEN-GAP — (a) VERIFIED `claim-quality.md:820` + `:1528` (briefed
  `:1527` was off-by-one); (b) VERIFIED both `02_baryon_sector.tex:40` and
  `semiconductor_binding_engine.py:68`.
- **Def 6** — Vol 9 Vacuum Datasheet `ch1-general-description` + `ch14-phase-diagrams`
  VERIFIED to exist as the canonical home for the (still-gated) soliton-size leaf.
