# Discussion follow-ups tracker

Running log of follow-up questions and explorations seeded by external discussions
(friend conversations, outside-review feedback, casual whiteboarding) that don't
yet belong in a numbered research arc or manuscript chapter.

**Entry conventions:**
- Date (ISO).
- Question verbatim (no paraphrase).
- Corpus grounding: what the manuscript / research corpus already says.
- Original territory: where the question opens new ground beyond corpus.
- Status: `open` / `researched` / `escalated-to-L3` / `escalated-to-manuscript` / `closed`.
- Canonical file pointers.

Flag-don't-fix posture: entries surface findings; Grant adjudicates whether any
escalate into formal pre-registration, derivation, or manuscript work.

---

## Entry 001 — 2026-05-16 — Cosmic spin grain ↔ Earth core/mantle differential rotation

**Question (verbatim, from friend discussion):**
> Does the spin of the universe imparting a grain on the lattice match what could
> be happening to earths core from mantle?

**Reading of the question.**
Two-part claim being tested:
1. Universal/cosmological spin at lattice genesis imparts a directional grain
   (preferred axis, chirality) onto the substrate.
2. That grain manifests at nested scales — specifically, as the observed
   differential rotation between Earth's solid inner core and the surrounding
   mantle (well-known geophysical phenomenon: inner core super-rotation
   ~0.1–1°/yr relative to mantle, with recent evidence of oscillation; e.g.
   Song & Richards 1996, Vidale et al. 2022).

### Corpus grounding (verified via cross-repo grep, 2026-05-16)

**Part 1 (cosmic spin → lattice grain) is CANONICAL in the corpus** — the
mechanism the friend is asking about already exists as the *freeze-in /
phase-transition-while-spinning* mechanism:

- [manuscript/ave-kb/common/trampoline-framework.md:89–99,123,131–136](../../manuscript/ave-kb/common/trampoline-framework.md) —
  canonical statement: during lattice formation from pre-geodesic plasma, the
  crystallizing region is rotating with angular velocity Ω_freeze. At
  crystallization, bond rest lengths lock at the rotating-frame equilibrium,
  and the direction of Ω_freeze becomes the direction of bond bowing →
  right-handed chirality. Cosmic spin is locked into the substrate as both bond
  over-bracing u₀ and the global chirality direction.

- [manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex:172–184,405–416,458–470](../../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex) —
  Vol 3 ch 04 canonical: "Ω_freeze is the rotation rate of the crystallizing
  region at the moment of lattice genesis… locked into the substrate as bond
  over-bracing u₀ and the global chirality direction, and survives forever as
  the cosmological initial condition." Names the multi-observable axis-alignment
  prediction (CMB axis-of-evil, Hubble anisotropy, galaxy spin, cosmic chirality).

- [manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:52](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex) —
  Axiom 1: K4 substrate governed by right-handed I4₁32 chiral space group; the
  two interpenetrating sublattices A and B carry opposite chirality. Lattice
  grain is built into the axioms.

- [research/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md:18–22,39–43](../L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md) —
  A-034 prereg (yesterday) formalizes a four-axis alignment test against
  Planck/Pantheon+/SDSS for the predicted cosmic preferred axis.

- [research/L3_electron_soliton/59_memristive_yield_crossing_derivation.md §5.4](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md) —
  "Lattice genesis as the primordial driven chirality event" — full mechanism
  with baryogenesis consequence.

**Part 2 (Earth core/mantle) is PARTIALLY in the corpus** — present, but framed
differently from the friend's nested-scale question:

- [manuscript/vol_3_macroscopic/chapters/13_geophysics.tex:20–23,122–127](../../manuscript/vol_3_macroscopic/chapters/13_geophysics.tex) —
  verbatim: *"Earth's spin imparts strain on the local lattice via the
  geodynamo, the strain accumulates against a 'Baryonic phase density
  [threshold]'…"* Framing is Earth-as-rotor in a Sagnac-VCA back-EMF picture,
  not as nested cosmic-grain.

- [manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md](../../manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md) —
  full Earth-as-rotor-in-Sagnac-boundary mechanism (KB-tier).

- [src/scripts/vol_3_macroscopic/simulate_geodynamo_vca.py](../../src/scripts/vol_3_macroscopic/simulate_geodynamo_vca.py) —
  engine code exists for the VCA framing.

- [manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/cross-scale-isomorphism-table.md:15,26–28](../../manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/cross-scale-isomorphism-table.md) —
  cross-scale isomorphism table lists co-rotation across scales (BH frame-drag
  ↔ nuclear shell ↔ motor rotor ↔ plasma; Park-transform decomposition) but at
  table-level only.

**NOT in the corpus (confirmed by grep across all 10 sibling repos + archive):**
- The phrase / framing of inner-core / mantle *differential* rotation.
- Cosmic-grain → planetary-rotation-axis alignment statistics.
- Angular-momentum cascade from cosmic → galactic → stellar → planetary → core
  scales as a single nested-grain phenomenon.

### Original territory the question opens

Three sub-questions the friend's framing surfaces that are not yet anywhere
in the corpus:

**(a) Is inner-core super-rotation a nested re-expression of Ω_freeze?**
Observation: Earth's inner core super-rotates relative to the mantle at
~0.1–1°/yr (variable, with recent evidence of oscillation period ~6–7 yr and
longer-term ~70 yr; Vidale et al. 2022; Yang & Song 2023). If the cosmic
grain biases angular-momentum partitioning across nested rotating bodies, the
inner-core/mantle differential could be a leak of the cosmic preferred axis
through the planetary scale. Predicts: the differential rotation vector should
have a non-zero alignment statistic with Ω_freeze (the A-034 predicted axis,
l≈174°, b≈−5°). Currently free-parameter in geophysics (no first-principles
prediction for the super-rotation rate or its axis).

**(b) Should planetary rotation axes statistically align with Ω_freeze?**
If lattice grain biases angular-momentum accretion during planetary formation,
solar system bodies' rotation axes should show non-random alignment with the
cosmic preferred axis. Testable from existing planetary-rotation catalogs
(JPL ephemeris, NAIF SPICE). Note: exoplanet spin axes mostly unmeasured;
solar system N=~10 is small but checkable.

**(c) Is "easy axis for angular-momentum cascade" a substrate-mechanical
prediction?** If the K4 lattice has a preferred chirality direction (Ω_freeze),
does it act as an *easy axis* for angular-momentum transmission — making
co-axial-with-Ω_freeze rotation lower-impedance than off-axis? This would be
a substrate-mechanical claim derivable from the K4 Cosserat anisotropy tensor,
not a cosmological one. Could in principle be checked against the K4 stiffness
tensor structure directly.

### Tension / risk

The Vol 3 ch 13 Earth-spin framing is **Sagnac-VCA back-EMF** — Earth
*generates* strain in the local lattice via its rotation. The friend's
framing is the *inverse*: cosmic grain biases Earth's rotational structure.
These need not conflict (both could be true at different scales), but the
nested-grain claim (cosmic → planetary → core) is a *stronger* claim than
the local-Sagnac claim, and would need its own derivation chain rather than
inheriting from ch 13.

Possible coherence: cosmic grain sets the *axis*; Sagnac-VCA back-EMF sets
the *local strain dynamics*. The two are decoupled-in-principle but
geometrically related at the planetary scale.

### Status
`open` — flagged for Grant adjudication. Not yet escalated.

### Suggested escalation paths (Grant's call)
- **If Grant adjudicates (a) is the load-bearing question** → could become an
  L3 prereg following the A-034 template, testing inner-core super-rotation
  axis alignment against the A-034 predicted preferred axis.
- **If Grant adjudicates (b) is the load-bearing question** → planetary
  rotation axis catalog test, lower-cost than (a), N-small but cheap.
- **If Grant adjudicates (c) is the load-bearing question** → derivation
  from K4 anisotropy tensor, manuscript-side work in Vol 1 or Vol 3 ch 04
  follow-up; does not need empirical test in the same way.

### Canonical pointers
- Cosmic spin → lattice grain (canonical): trampoline-framework.md;
  vol_3 ch 04; vol_1 ch 01 Axiom 1.
- Earth's spin → local lattice strain (canonical, different framing):
  vol_3 ch 13; geodynamo-vca-back-emf.md.
- A-034 cosmic-axis empirical prereg (canonical, in flight): 2026-05-15 prereg
  under research/L3_electron_soliton/.

---

## Entry 002 — 2026-05-16 — Orbital dynamics as macroscopic grain/chirality projection

**Question (verbatim, from friend discussion):**
> Is orbital dynamics as macroscopic "grain/chirality" projection?

**Reading of the question.**
Whether orbital mechanics at every scale (planetary orbits, moons, solar
system coplanarity, ecliptic, prograde/retrograde preference, stellar binary
orientations, galactic disk axes, spiral-arm chirality) is a *projection* of
the cosmic lattice grain — i.e., whether the orientation, handedness, and
alignment statistics of orbital structures across all scales are the same
preferred-axis information that the A-034 prereg is testing in CMB / Hubble
flow / LSS-spin.

### Corpus grounding (verified via cross-repo grep, 2026-05-16)

**Orbital mechanics IS in the corpus** — substantial coverage, but framing is
substrate-mechanical impedance/LC-tank, NOT chiral-grain projection:

- [manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex](../../manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex) —
  canonical Vol 3 Ch 14, "Macroscopic Orbital Mechanics." Line 36 verbatim:
  *"Gravity is the macroscopic 1/r acoustic tension of the dielectric vacuum
  displaced by massive nodes. The mathematics are identical to nuclear binding
  impedance, scaled by the gravitational compliance constant G instead of the
  nuclear stringency K_mutual."* Mercury perihelion derived as mechanical 1/r³
  impedance-gradient drag (lines 60–77), exact GR result without curved
  spacetime. Flyby anomaly derived as Sagnac acoustic shear at Earth's
  rigid–compliant LC boundary (lines 86–105), ΔV ≈ 13.4 mm/s, claimed to
  falsify Lense-Thirring. Saturn rings: Cassini gaps as standing-wave
  cancellation zones.

- [manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex](../../manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex) —
  BH ringdown ω_R M_g = 18/49, validated 10–18% against GW150914 / GW170104 /
  GW151226. Kerr ringdown uses *prograde saturation-boundary shift*.

- [manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md](../../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) —
  lines 6–23: stable circular orbits are *"the macroscopic mechanical
  equivalent of a Lossless LC Tank Circuit operating purely in the reactive
  power domain"* — θ=90° between F_g and v_orb gives P_real = 0. Lines 27–32
  Power Domain Classification table maps: stable orbit / inspiral (GW) /
  electron orbital / photon propagation all to phase-angle regimes. This is
  the corpus's existing scale-bridge for orbits ↔ electron-shell isomorphism.

- [manuscript/backmatter/01_appendices.tex:221](../../manuscript/backmatter/01_appendices.tex) —
  AQUAL Galactic Dynamics §; MOND-scale a₀ = cH/2π ≈ 1.07×10⁻¹⁰ m/s² from
  Axiom 4 saturation. See also
  [manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/derived-mond-acceleration-scale.md](../../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/derived-mond-acceleration-scale.md).

- Cosmic-grain mechanism (canonical, from Entry 001):
  [trampoline-framework.md:99,131](../../manuscript/ave-kb/common/trampoline-framework.md),
  [vol_3 ch 04](../../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex),
  [A-034 prereg](../L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md).

**One observational hint already in corpus (not derived):**
[A-034 prereg lines 136–138](../L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md)
notes that the CMB axis-of-evil (l=174°, b=−5°) is anomalously aligned with
the **ecliptic plane** — standard cosmology has no explanation. A-034 treats
this as background context, not as a derived AVE prediction.

**NOT in the corpus (confirmed by grep, all 10 sibling repos):**
- Explicit claim that orbital plane orientations, ecliptic, solar-system
  prograde preference, galactic disk axes are projections of the K4 cosmic
  grain.
- Extension of the [cross-scale isomorphism table](../../manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/cross-scale-isomorphism-table.md)
  "Co-rotation" row (currently: BH frame-drag ↔ electron shell ↔ nuclear shell
  ↔ protein ↔ antenna ↔ tokamak ↔ motor) to planetary or galactic columns.
- Any axial / chiral structure in the Vol 3 Ch 14 gravity treatment (currently
  pure scalar 1/r acoustic tension; no preferred-axis term in the gravity
  Lagrangian).

### Original territory the question opens

**(a) Orbital-plane orientation statistics as a direct test of Ω_freeze axis.**
The A-034 prereg already pre-registers alignment tests in CMB / Hubble flow /
LSS spin / E-B polarization / matter asymmetry against the predicted preferred
axis. The friend's framing adds a sixth target: orbital-plane orientations at
all available scales. Concrete observables:
- Solar system: ecliptic normal vs A-034 axis (single data point but already
  known to be anomalously aligned with CMB axis-of-evil — corpus notes this).
- Solar-system prograde fraction (8/8 planets prograde; Venus/Uranus spin
  retrograde — does the spin/orbit decomposition track the cosmic axis?).
- Binary star orbital plane statistics (Gaia DR3 has ~10⁵ resolved binaries).
- Galactic disk axes (SDSS galaxy spin axes — A-034 already references these
  as "weak ~1–2σ preferred direction; contested").
- LIGO/Virgo binary inspiral orbital-plane orientations (~100 events; small
  but rapidly growing).
This would not be a new derivation; it's an extension of the A-034
multi-observable axis-alignment program to a new observable channel.

**(b) Extension of cross-scale isomorphism table to solar-system + galactic
scales.** The cross-scale table currently has columns BH-QNM / electron /
nuclear / protein / antenna / tokamak / BLDC motor. The "Co-rotation" row is
empty for any astrophysical scale beyond BH. Filling in solar-system and
galactic columns would force a derivation of which substrate observables map
to orbit-period, orbital-plane normal, semi-major axis, eccentricity. This is
table-completion work that is structurally implied but not done.

**(c) Does gravity-as-impedance-tension inherit a chiral preferred axis?**
Vol 3 Ch 14 currently treats gravity as pure scalar 1/r acoustic tension —
no axial / chiral / preferred-direction term in the gravitational Lagrangian.
But if the K4 substrate carries a frozen Ω_freeze axis with I4₁32 chirality
(Axiom 1), then the dielectric-vacuum response that produces gravity at
macroscopic scale should inherit at least a *small* anisotropic correction.
This is a derivation question, not an empirical one: extract the leading-order
anisotropy in the gravitational compliance constant G from the K4 stiffness
tensor along vs perpendicular to Ω_freeze. Predicts a tiny ΔG/G anisotropy
that could be tested via orbit-precession residuals (planetary ephemerides
are sensitive at the 10⁻¹¹ level via JPL DE).

### Tension / risk

The Vol 3 Ch 14 framing makes gravity scalar (1/r acoustic tension) and the
[orbital-friction-paradox.md](../../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md)
makes stable orbits lossless LC tanks (reactive power, θ=90°). Both are
chirality-blind. To bring grain-projection into orbital mechanics one of
three things has to happen:
1. Add an anisotropic correction to G in Ch 14 (the (c) derivation).
2. Add a chiral coupling term to the LC tank in the orbital-friction-paradox
   leaf (would predict slight orbit-handedness preference at sub-leading order).
3. Argue the alignment is purely *inherited from initial conditions* (cosmic
   grain biases planetary-formation angular momentum, not the orbital dynamics
   themselves) — in which case orbital mechanics stays chirality-blind but the
   *statistics* of orbital planes still track Ω_freeze.

Option (3) is the cleanest theoretically — orbital dynamics stays as Vol 3
Ch 14 has it, and the grain projection lives entirely in initial conditions.
It also nests directly with Entry 001 (inner-core/mantle differential as
cosmic-grain initial-condition leak).

### Status
`open` — flagged for Grant adjudication. Strongly nests with Entry 001;
together (Entry 001 + Entry 002) would form an "Ω_freeze cascade through
nested rotators" research program if escalated.

### Suggested escalation paths (Grant's call)
- **If (a) is load-bearing** → extend A-034 prereg to a sixth observable
  channel (orbital-plane alignment). Lowest cost; uses existing methodology.
- **If (b) is load-bearing** → manuscript-side work to complete the
  cross-scale isomorphism table with solar-system + galactic columns. Forces
  clarification of the substrate-mechanical mapping.
- **If (c) is load-bearing** → derivation of leading-order G anisotropy from
  K4 stiffness tensor in the Ω_freeze direction; high-precision empirical
  test via JPL planetary ephemerides at 10⁻¹¹ level. Highest scientific
  return but most expensive derivation.
- **If Entry 001 + 002 are unified** → bundled "Ω_freeze cascade through
  nested rotators" prereg covering inner-core/mantle, planetary spin axes,
  orbital planes, galactic disks, all as one multi-observable test of a
  single mechanism.

### Canonical pointers
- Orbital mechanics framing (canonical, scalar/chirality-blind):
  vol_3 ch 14, ch 15; vol_4 ch 1 orbital-friction-paradox.md.
- MOND-scale derivation from Axiom 4 saturation: backmatter app §AQUAL.
- Cross-scale isomorphism table (incomplete — no astrophysical columns):
  vol_2 app F.
- Cosmic-grain mechanism (canonical, from Entry 001): trampoline-framework.md;
  vol_3 ch 04; A-034 prereg.
- A-034 ecliptic-alignment observational hint (background, not derived):
  research/L3_electron_soliton/2026-05-15_A-034 lines 136–138.
