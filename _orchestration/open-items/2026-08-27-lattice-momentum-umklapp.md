---
id: lattice-momentum-umklapp
title: "Momentum conservation is not among Axiom 3's stated Noether legs, and Umklapp is untreated -- with exact thresholds"
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-27
source: manuscript/common_equations/eq_axiom_3.tex
anchor: "Energy conservation follows as a Noether consequence of time-translation invariance"
---

Surfaced by the `L2-preferred-frame` lane; thresholds independently recomputed by
the `two-knob-gravity-repair` lane. Distinct from
`2026-08-27-preferred-frame-boost-channel` (that one is boost/anisotropy; this one
is discrete translation and momentum closure), but they share a root and the
same PPN family.

**The axiom text names its Noether legs and spatial translation is not one.**
`eq_axiom_3.tex`:27, verbatim: *"Energy conservation follows as a Noether
consequence of time-translation invariance. The written action's exact internal
symmetry is the residual (time-independent) gauge family A → A + ∇λ(x); its
Noether content is the pointwise conservation of the Gauss function
∇·(ε₀∂_tA)."* **Time translation and residual gauge.** On a lattice, spatial
translation symmetry is precisely the one that is only **discrete** — so the
conserved bookkeeping quantity is **crystal momentum modulo a reciprocal-lattice
vector**, and Umklapp is a reactive three-wave phase-matching condition (*not* a
drag; the dissipative wording fails the Ax3-lossless test).

**L2 reports** that the only assertion of momentum conservation it located is a
docstring at `src/ave/topological/vacuum_engine.py`:1477, and that the one place
momentum closure was load-bearing — the dark wake — is DEMOTED 2026-08-11 and
self-flags at `dark-wake-bemf-foc-synthesis.md`:122 as *"an explicit open gap,
not a framework claim."*

**`α₃` is the PPN parameter that is nonzero exactly for theories with a
preferred frame AND non-conserved momentum. It is bounded at `|α₃| < 4e-20`**
(externally retrieved, tentative-standing) — among the tightest numbers in
physics. Canon has the first condition by its own axiom text (`:27`, above) and
cannot presently rule out the second.

**Two searches find Umklapp named only inside a gap list.** Two independent
methods over the worktree at `a3f4fef7` (`grep -ril` and `rg -il`, `.git`
excluded): `umklapp` → **1 file** (`temporal-saturation-regime-classifier.md`),
where the hits sit inside a gap list; `crystal momentum` → **0 files**. Blind
spot: single-line regex on two spellings, AVE-Core only — a treatment worded
without either token, or one in a sibling repo, would not be caught.

**The thresholds are exact, because `ℓ_node` is definitional.** From
`constants.py`:293 (`ℓ_node ≡ ħ/(m_e c)`) with CODATA:

| carrier at the zone edge `q = π/ℓ_node` | energy |
|---|---|
| photon | `E = π·m_e c² = 1.605351 MeV` (the π is definitional, not a coincidence) |
| electron | kinetic `1.173718 MeV` |
| **proton** | kinetic **`1.37335 keV`** |

**Two consequences the corpus does not carry.**
(a) **For light:** canon's escape is weak-C (`preferred-frame-and-emergent-lorentz.md`:102,
*"the free photon is the continuum EM field … no zone-edge (qℓ_node)² dispersion"*),
gate `wejkhvnfb` **OPEN**. If weak-C fails, photons above ~1.6 MeV are Bloch modes
and vacuum Umklapp/Bragg opens — which **MeV gamma-ray astronomy excludes far more
directly than the birefringence horn**, and LHAASO's 13 TeV photon from GRB221009A
sits `2.5e7` zone edges out.
(b) **For matter:** the leaf's weak-C RESCOPE says the zone-edge group-velocity
bending *"governs matter carriers (which ARE lattice-locked)"*. **If that is the
centre-of-mass wave rather than the soliton's internal mode, every cosmic ray
above ~1.4 keV has momentum defined only modulo a reciprocal-lattice vector.**
Canon does not disambiguate the two readings.

**Ruling sought.** Which reading of the weak-C RESCOPE is intended — internal
mode or centre-of-mass wave? That single word decides whether (b) is a
housekeeping note or the sharpest substrate-native preferred-frame test
available, and it is currently unasked.
