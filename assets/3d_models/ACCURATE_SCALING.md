# Accurate Scaling of the Particle STL Models — Scope Note

**Status (2026-06-08, §43):** the STL meshes in this directory are
**TOPOLOGY / RENDERING demos at an arbitrary UNIFORM scale.** They do **not**
encode physical particle sizes or physically correct relative scales. This note
specifies what accurate scaling *would* require and why a single physical-scale
render is currently intractable.

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

## The five distinct length scales (and one non-length)

A faithful "physical scale" render would have to reconcile quantities that live
at wildly different magnitudes — and one of them is not a length at all:

| # | Scale | Electron (c=3) | Proton (c=5) | Notes |
|---|-------|----------------|--------------|-------|
| 1 | Saturation-boundary body | (size-definition pending) | (size-definition pending) | The saturated-core extent of the soliton; **awaits the canonical soliton-size definition**. |
| 2 | Charge radius `D_p` | ~0 (point-like in scattering) | **0.841 fm** = 4λ_p | Proton: Pohl 2010 muonic-H; see `manuscript/ave-kb/.../proton-identification.md`. |
| 3 | Compton wavelength `ℏ/mc` | **386 fm** (= ℓ_node) | **0.210 fm** (= λ_p) | Reduced Compton; electron's *equals* the lattice spacing. |
| 4 | Lattice spacing `ℓ_node` | **386.16 fm** | 386.16 fm | `ℏ/(m_e c)`; the same for every particle. |
| 5 | `r_opt = κ_FS/c` | 8.317 (= κ_FS/3) | 4.990 (= κ_FS/5) | **DIMENSIONLESS coupling-budget ratio — NOT a length.** What the STLs currently use as their uniform mesh scale. |

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

Faithful relative scaling **awaits the canonical soliton-size definition** —
i.e. a single, axiom-derived, dimensionally-honest "size" observable for a
saturated topological soliton (the **pending 2026-06-08 soliton-size
determination**). Open sub-question, explicitly **flagged not resolved**: which
of scales #1–#4 (saturation-boundary body, charge radius, Compton wavelength,
or lattice spacing) is the physically-correct render diameter — and whether the
impedance-taper radial width (`entanglement_thread.impedance_taper_profile`)
should track it.

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
