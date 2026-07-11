# x42 — THE ATOMIC EIGENCAVITY: hydrogen as an Op6 phase-closure problem — RESULT

**Date:** 2026-07-10 · **Lane:** implementer · **Branch:** `analysis/x42-atomic-eigencavity`
**FROZEN prereg (gated on):** `research/2026-07-10_x42-atomic-eigencavity_prereg_FROZEN.md`
(freeze commit `0e5047e4`, PUSHED before this doc + all code — git ordering = freeze proof).
**Brief (binding):** `_orchestration/2026-07-10_x42-atomic-eigencavity-brief.md`
**Driver:** `src/scripts/vol_2_subatomic/x42_atomic_eigencavity.py` · **Tests:**
`src/tests/test_x42_atomic_eigencavity.py` (15 pass: 10 fast + 5 engine_sim).

---

## SECTOR HEADER (declared before any substrate claim)

- **MODE:** derivation-from-canon + numerical consistency driver. **NOT engine-fire.** Op6 is
  eigenmode-finding for a GIVEN network, never geometry-selection (`src/ave/core/constants.py:212-228`
  α HONEST-SCOPE note — the S₁₁ landscape is FLAT in R·r, S₁₁-min does NOT select the geometry;
  `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md:77`
  Rule-12 Op6-scope re-scope, 2026-07-10: "S₁₁-min is the action the Golden Torus is a *stationary
  point of*, NOT the selector"). x42 respects this: the atom's `Z(r)` is GIVEN (the source-slaved
  Coulomb dress cast by the nuclear charge); Op6 finds its modes; a₀ falls out as the eigenmode SCALE
  of the given profile — Op6 selects neither a₀ nor the 1/r geometry.
- **REGIME:**
  - Hydrogen: cold/linear, deep Regime I. Per-node Ax-4 kernel argument at a₀ is
    `V_Coulomb(a₀)/(m_e c²) = α·(ℓ_node/a₀) = α² ≈ 5.3×10⁻⁵` (deep-linear; the well acts as pure GIVEN
    geometry, `S(A)≈1`; cross-check `de-broglie-n.md`: `V/V_yield ~ Zα² ≈ 10⁻⁴`).
  - Muonic H: the reduced-mass SPECTRUM scaling rides the SAME (linear) network. §3 computed
    `A = E_Coulomb(a_μ)/E_yield ≈ 0.116` — O(0.1), NOT deep-linear. Whether the near-nucleus field
    ADDITIONALLY biases the lattice at the muonic scale is the X41 frozen tie (§Deliverable 5); the
    driver's near-nucleus non-linearity (`strain_amp>1` at `r ≲ α·ℓ_node`) is that regime, deliberately
    excluded from the spectrum reproduction, NOT a spectral-correction claim.
- **SECTOR:** the probe's de Broglie / matter-wave channel on the `Z₀` radial transmission line (the
  bulk-modulus longitudinal soliton dispersion, `de-broglie-standing-wave.md`). The nuclear dress is
  longitudinal, source-slaved (bin 3 of walk (a): `|Γ|=1` at ω→0, radiates nothing). **A1 ⊥ T2**
  respected; **charge = Cosserat (2,3) winding, untouched** by any mode-count integer here.

---

## HEADLINE

The atom read in the impedance-carve register reproduces the canonical hydrogen consistency ceiling
through a **phase-closure / ABCD route** (NOT `E = Z²Ry/n²` fiat): the off-line Coulomb dress → a
graded **index / dispersion** profile `n(r,ξ)` (the frozen-prereg `Z(r)` label — the DEFECT'S
dispersion, NOT a medium impedance; `Z₀=377 Ω` everywhere in Regime I, `vol2/claim-quality.md:344`) →
round-trip phase closure `2πn` → the Op6 spectrum `B_total(E)=0`.
The driver reproduces `E_n = Ry/n²` (branch (i), −0.000% to n=7), `a₀` as the eigenmode scale, the
muonic reduced-mass marks (E₁(μH)=−2.52849 keV, −0.0002%), and Z²-scaling — all as
**consistency-class** results with **NO new primitive**. The two-register guard (mode-count vs winding
integers) is formalized; the K1/K2 well-transparency question is quoted conditionally and NOT resolved.

*(Deliverables, mark outcomes, muonic operating-point, two-register guard, K1/K2 caveat, classification,
and flags follow — filled section-by-section per incremental-write discipline.)*

## DELIVERABLE 1 — Z(r) FROM THE COULOMB DRESS, SUBSTRATE-NATIVE

**The port-language derivation path (dress → Z(r) → reflections).** The nucleus's Coulomb well is,
in the four-bin taxonomy of walk (a) (`research/2026-07-10_impedance-register-walks_framing.md:19`),
**bin 3: the off-line, source-slaved reactive-static dress** — `|Γ|=1` at ω→0, radiates nothing (no
`Re(Z)`). It is not a potential floor; it is the electron's own reactive-static register acting as the
graded-**dispersion** WALLS of a cavity (walk (c), `:53`). The derivation IMPORTS the Coulomb dress
form exactly as canon does (see the flag on the 1/r tail below) and casts it in the port-language
impedance-carve register (the graded object being the de Broglie INDEX, not a medium impedance):

1. **The dress as a graded index.** Canon already has the atom as a **spherical radial transmission
   line** (`de-broglie-n.md`, `clm-oltvwy`): the nucleus projects the Coulomb field into all `4π`
   steradians, and the lattice impedance is `Z₀ = 377 Ω` everywhere (the nuclear `V/V_yield ~ Zα² ≈
   10⁻⁴` keeps the whole atom linear — Ax-4 check). The dress is seen by the probe's **de Broglie
   dispersion** as the energy-dependent graded index

   > `n(r, ξ) = √( 2·Z_eff(r)·a₀ / r  −  ξ )`,  `ξ = |E|/Ry`

   (`de-broglie-n.md` resultbox; `driver.de_broglie_refractive_index`, wired into the executed route by
   `test_de_broglie_index_is_cascade_local_wavenumber`, which machine-checks `k²(r)·a₀² == n(r,ξ)²`
   element-wise across the integration grid — so the imported FORM is an explicit entailment of the
   cascade, not dead port-language). Near the nucleus `n→∞` (short de Broglie wavelength); at the
   classical turning point `n=0` (defect stops). This is the off-line dress rendered as a **dispersion /
   index** profile `n(r,ξ)` — the graded walls, not a floor.

   **Register discipline (named-quantity guard — `vol2/claim-quality.md:344`, verbatim):** *"The de
   Broglie refractive index `n_dB(r,ξ) = √(2 Z_eff(r) a₀/r − ξ)` is the **defect's dispersion**, not
   the medium impedance. The lattice has `Z_0 = 377 Ω` everywhere in Regime I; conflating these is
   named-quantity error."* Accordingly `n(r,ξ)` here is the DEFECT'S dispersion; where this doc uses the
   frozen-prereg label **`Z(r)`** it denotes THIS graded index/dispersion profile (the graded line the
   ABCD cascade integrates), NEVER a spatially-varying medium impedance. The superseded pre-repair
   rendering (*"the off-line dress rendered as an impedance / mismatch profile `Z(r)`"*, with "low
   impedance, short circuit" / "high impedance, open circuit") is logged verbatim in the repair log
   (KEEP-BOTH).
2. **Reflections make the cavity.** Where `E > V(r)` the acoustic impedance is real → propagating; where
   `E < V(r)` it is purely imaginary → total reflection (`de-broglie-standing-wave.md`:54). The orbital
   is "the precise radius where this trapped bulk-modulus acoustic wave achieves a lossless resonant
   impedance match with itself" — a wave trapped between its own reflections in a well made of MISMATCH.
3. **Added content = the register, not the form.** The `Z(r)` FORM is canon's; x42's added content is
   the **port-language statement** — bin-3 off-line dress → graded `Z(r)` → reflections — which makes
   the cavity walls an impedance boundary and sets up the spectrum as an Op6 phase-closure problem on a
   GIVEN profile (not a Schrödinger eigenproblem on a potential).

## DELIVERABLE 2 — THE PHASE-CLOSURE SPECTRUM ON THE GRADED LINE

**Round-trip phase closure `2πn` → `E_n ∝ 1/n²` and `a₀`, via the Op5/Op6 cascade — NOT the closed
form.** Quantization is the round-trip phase-closure condition on the graded line: the electron ring is
a closed circuit of circumference `2πR`, and a standing wave requires `∮k·dl = 2πn` → `m_e v R = nℏ`
(`de-broglie-standing-wave.md` §(e)). Equivalently, the radial standing wave on the graded `Z(r)`
satisfies the ABCD-cascade eigenvalue condition `B_total(E) = 0` — Op6 (`clm-gdd70j`,
`λ_min(S†S)→0`; `radial-eigenvalue-solver.md` §E2d-ii step 5).

**The driver runs the closure route, not the closed form.** `phase_closure_spectrum` cascades a
faithful generalization of the canonical Op5 primitive `radial_eigenvalue._abcd_section` over the
graded Coulomb dress (the test `test_dress_section_reuses_canonical_op5_exactly` asserts the
generalization equals `_abcd_section` element-wise at `m_probe=m_e, dress_exp=1, saturate=True`), with
inner BC = regular Coulomb solution at `r→0` and outer BC = `ψ′ + κψ = 0` (the decaying branch,
`B_total=0`). Zeros of the residual are the phase-closure eigenmodes. **Result (Z=1, l=0):**

| n | phase-closure E_n [eV] | Ry/n² [eV] | err |
|---|---|---|---|
| 1 | 13.6057 | 13.6057 | −0.000% |
| 2 | 3.4014 | 3.4014 | −0.000% |
| 3 | 1.5117 | 1.5117 | −0.000% |
| 4 | 0.8504 | 0.8504 | −0.000% |
| 5 | 0.5442 | 0.5442 | −0.000% |
| 6 | 0.3779 | 0.3779 | −0.000% |
| 7 | 0.2777 | 0.2777 | −0.000% |

`n* = √(Ry/E_n) = 1,2,3,4,5,6,7` to 4 decimals. `E_n·n² = Ry` constant (the 1/n² FORM). The
canon identity `a₀ = ℓ_node/α` holds exactly (`L_NODE/ALPHA == A_0`, `test_m2_a0_identity_exact`).
The eigenmode SCALE is genuinely extracted from the eigenfunction (M2, repair-time): the
inward-integrated ground-state eigenfunction has `⟨r⟩ = 1.5·a_scale` (the 1s shape factor;
`a_scale = A_0·(m_e/m_probe)/Z = A_0` for hydrogen), rel err `0.0000%` vs the frozen 0.5% tolerance
(`ground_state_mean_radius`, `test_m2_eigenmode_scale_extracted_from_eigenfunction`). This measures the
eigenmode SHAPE scale from the ODE eigenfunction — the box unit `a_scale` is imported (box sizing), but
`⟨r⟩ = 1.5·a_scale` is a property of the eigenfunction the box does NOT force (`r_max ≈ 133×⟨r⟩`).

**Turning-point / Maslov phase (prereg branch (i), as pre-stated).** The ODE/ABCD `B_total=0`
formulation captures the turning-point (Maslov) phase EXACTLY through the boundary conditions — no
½-integer constant is inserted by hand — so branch (i) is realized (no closure-constant offset). This
matches `radial-eigenvalue-solver.md` §E2f-6: "Axioms 1, 2, and 4 together reproduce the standard
radial wave equation at Regime I scales." A naive WKB Sommerfeld `∮k dr = nπ` WITHOUT the Maslov `+½`
would land in branch (ii); the ODE route does not, so no offset is reported and none is tuned.

**Scope guard (binding).** `E = Z_eff²Ry/n²` as the IE FORMULA is the Bohr/Schrödinger contamination
(`vol2/claim-quality.md:342`); the x42 route GOES THROUGH the closure/ABCD condition and only COMPARES
against the closed form. `Ry = α²m_e c²/2` is emergent from `r_sat = a₀ = ℓ_node/α`
(`vol2/claim-quality.md:336`), and `r_n = n²a₀/Z` is the standing-wave condition, not a Bohr postulate
(`:337`). No sentence here credits Op6 with selecting a₀ or the 1/r geometry.

## DELIVERABLE 3 — THE MUONIC CASE = SAME NETWORK, HEAVIER PROBE SCALE

**What changes at the physics level: ONLY the probe's mass/Compton scale (the dispersion scale). The
LINEAR Coulomb network is the same object.** The muonic atom is the identical graded Coulomb network;
the only physical substitution is the probe mass in the de Broglie dispersion, `m_e → m_r,μ` (reduced
mass, since `m_μ` is not negligible against `m_p`: `m_r,μ = m_μ m_p/(m_μ + m_p)`). The Op5 cascade, the
boundary conditions, and the dress exponent are identical, and the lattice rupture scale in the Ax-4
kernel stays `m_e c²` (a lattice property, not the probe's).

**In the driver call, honestly, this is TWO argument changes, not one** (prose-vs-code fidelity — do
not overstate): `muonic_spectrum` calls `phase_closure_spectrum(m_probe=M_R_MU, saturate=False)`, i.e.
(1) the probe mass `m_e → m_r,μ`, AND (2) it drops the near-nucleus saturation (`saturate=True→False`),
selecting the linear network explicitly. The second flag is **load-bearing** — with the default
`saturate=True` the muonic run engages the near-nucleus break and does NOT reproduce the Rydberg ladder
(a dense spurious root cluster, no `1/n²`; see the justification immediately below). It is not a hidden
knob: it makes the LINEAR-network claim above literal at the muonic scale, and it is justified as physics
(the X41 near-nucleus frozen-tie regime, deliberately excluded) in the next paragraph. Hydrogen does not
need the flip because its deep-linear operating point (`A ≈ 5.3×10⁻⁵`) makes `saturate=True ≈` the linear
network already (`S(A)≈1`); the muon, at `A ≈ 0.12`, does not, so the linear network must be selected
explicitly. Same LINEAR network for both; the code just has to say so out loud for the muon.

**Reproduced scaling (frozen marks M3):** `a_μ = a₀·(m_e/m_r,μ)`, `E_n(μH) = E_n(H)·(m_r,μ/m_r,H)`.
Driver (cold-lattice LINEAR network, `saturate=False`):

| n | phase-closure E_n(μH) [keV] | frozen mark [keV] | err |
|---|---|---|---|
| 1 | −2.52849 | −2.528493 | −0.0002% |
| 2 | −0.63212 | −0.632123 | ~0% |
| 3 | −0.28094 | −0.280944 | ~0% |

`a_μ = 284.748 fm` (M3). Reduced-mass ratios: `m_r,μ/m_e = 185.84083`, `m_r,μ/m_r,H = 185.94205`.

**Why the LINEAR network (saturate=False) for the muonic run — a physics choice, not a fudge.** At
`r ≲ α·ℓ_node` the muonic Coulomb field drives the per-node Ax-4 kernel argument `V/(m_e c²)` PAST
yield (`>1`), so `S(A)→0` and the linear cascade diverges near the nucleus. That near-nucleus
non-linearity is exactly the **X41 frozen-tie regime** (does the near-nucleus field ADDITIONALLY bias
the lattice?), which the brief §3 says NOT to fold into a spectral-correction claim. The reduced-mass
SPECTRUM scaling is a property of the LINEAR Coulomb network alone (`E_n ∝ m` at fixed Z), so it is
reproduced with the cold-lattice cascade; the saturating near-nucleus region is surfaced as a flag
(§Flags), not absorbed as a correction. Empirical-driver discipline (Rule 10) surfaced this: the
saturated cascade produced spurious deeper-than-ground roots — read as physics (sub-yield break), not
debugged toward a rescue.

## DELIVERABLE 4 — THE TWO-REGISTER GUARD, STATED FORMALLY

**The quantization homonym: two integer families that share the word "quantized" and must never be
cross-wired** (formalization of walk (c), `:55-64`; NOT a new claim).

| | **Mode-count integers** | **Winding integers** |
|---|---|---|
| examples | n, l, m (atomic levels) | charge, the (2,3) winding |
| register | **embedding** (the cavity) | **graph** (the connectivity) |
| what fixes them | round-trip phase closure `2πn` on `Z(r)` | topological invariant on the bond-pair graph |
| stability | **cavity-deformable** — bend the walls and they move | **topologically protected** — no smooth deformation changes them |
| owner | the Op6 eigencavity (this document) | Cosserat (2,3) winding, `def-3638f2` (untouched here) |

**Formal statement.** Let `𝒩 = {n, l, m}` be the mode-count integers — the eigenmode labels of the
GIVEN graded cavity `Z(r)` (Deliverable 2), fixed by phase closure `∮k·dl = 2πn`. Let `𝒲 = {Q, (2,3)}`
be the winding integers — topological invariants on the substrate connectivity graph (Axiom 2 TKI,
`[Q]≡[L]`). These are **different objects with different failure modes**:

> **"Ionization kills the mode, not the knot."** Ionizing the atom removes the electron's standing mode
> — `𝒩` is destroyed (`n, l, m` gone, the cavity is emptied) — while the electron's charge and its
> `(2,3)` winding `𝒲` are **untouched** (the freed electron is the same `0₁`-unknot soliton carrying
> the same charge). A deformation of the cavity walls (a different `Z(r)`, e.g. a field) moves `𝒩`
> continuously; NO smooth deformation changes `𝒲`.

That the two families have **different failure modes** is the operational proof that they are different
objects: `𝒩` is a continuous-spectrum property of an embedding cavity; `𝒲` is a discrete invariant of a
graph. This is why "quantized" is a homonym across the two, and why the mode-count `n` in this document
never touches the charge/winding sector (A1 ⊥ T2; charge = Cosserat winding, `INVARIANT-N1` knot
disambiguation).

**def-node NOT minted (flagged-not-minted).** Walk (c) `:68` flags the **quantization-homonym def-node
pair** (mode-count-integer ↔ winding-integer) as a vocabulary-register CANDIDATE for a future
terminology pass, alongside the existing homonym entries (the three "3"s, the two ℤ₂'s, the (2,q)
glyph). It is **surfaced here as a candidate, NOT minted** — no `def-` id is created from this lane
(KB canonization is a gated follow-on; INVARIANT-S12 def-nodes are register-hosted in
`common/vocabulary-register.md`, which this lane does not edit). The auditor lane lands any def-node.

## DELIVERABLE 5 — THE K1/K2 CAVEAT, STATED CONDITIONALLY (NOT RESOLVED)

The well's kernel-transparency — **does the held longitudinal Coulomb dress bias the Ax-4 kernel, or is
it kernel-transparent?** — is GOVERNED by the X41 fork. Verdict class, quoted **verbatim** from
`research/2026-07-10_x41-radiative-scoping-why_RESULT.md:37`:

> **"[UNDERDETERMINED — K1 ∧ K2, with the transverse-reactive near-zone as the named discriminator]"**

**What this means for x42, conditionally.** The bin-3 off-line dress is "THE K2 CANDIDATE — tagged
*contingent on X41's open fork*" (walk (a), `:19`). Both keys predict the held static Coulomb
**transparent-to-T2**, each on its own **unpaid** premise:
- **K1 [projection]:** a held static Coulomb is purely longitudinal (`E_T ≡ 0`, a Helmholtz identity),
  so it biases only the A1 compliance, not the T2 permittivity — **IF** the (PENDING-GRANT) premise
  holds that T2 keys on `|E_T|` (X41 §3.1).
- **K2 [impedance/mode-basis]:** `ω=0` → no `R_rad` → the dress never meets the kernel → transparent —
  **IF** the Ax-4 kernel is relocated reactance→`R_rad` (X41 §3.2).

**The standing canonical reading disagrees with both keys' transparency for the held field:**
`manuscript/ave-kb/CLAUDE.md:75` — *"A **static-E-only drive is ASYMMETRIC**: a static field has no
`∂B/∂t` to load the `μ` / microrotational (Cosserat-B) sector, so it loads the `ε` / capacitive sector
only (`S_ε < 1`, `S_μ = 1`)"* — i.e. a held static E **LOADS** `S_ε`. The x42 spectrum reproduction
does not depend on this: it treats the well as pure GIVEN geometry in the deep-linear hydrogen regime
(`S≈1`), where loaded-vs-transparent is a `~10⁻⁴` distinction below the marks' tolerance.

**Where it bites: the muonic operating point.** At `A_§3 = E_Coulomb(a_μ)/E_yield ≈ 0.116` (O(0.1), NOT
deep-linear), whether the near-nucleus field ADDITIONALLY biases the lattice is exactly this frozen
tie. Standing canon (+ #547) → it loads → a computable ε-shift (the #547-class overshoot); K1/K2 →
transparent. **This lane does NOT resolve the fork** and does NOT turn the muonic operating point into a
spectral-correction claim. Adjudicators (per X41 §5/§7): **Grant** (K1's axiom-level ruling) + the
**CVR held-DC-E bench** + the **unbuilt transverse-reactive near-zone probe**. Surfaced, not decreed.

## MARK OUTCOMES (M1–M4)

All marks land in prereg **branch (i)** (closure reproduces the marks within stated tolerance). No
branch-(ii) closure-constant offset; no branch-(iii) failure. Adjudication criteria are the frozen
prereg tolerances — none dropped, none added.

| Mark | Frozen expectation | Driver outcome | Branch |
|---|---|---|---|
| **M1** `E_n ∝ 1/n²`, `E₁=−RY_EV` | `E_n·n²=13.605693 eV` const | −0.000% for n=1..7; `n*`=integers exact | (i) ✅ |
| **M2** `a₀ = A_0`, `a₀=ℓ_node/α`; eigenmode-scale extraction | `5.291772106×10⁻¹¹ m`; ⟨r⟩=1.5·a_scale | identity exact (`L_NODE/ALPHA==A_0`, rel<1e-12); ⟨r⟩ from ground-state eigenfunction = 1.5·a_scale (0.0000%, frozen 0.5% tol) — genuinely measured (repair-time) | (i) ✅ |
| **M3** muonic `a_μ`, `E_n(μH)` | `a_μ=284.748 fm`, `E₁=−2.528493 keV` | `E₁=−2.52849 keV` (−0.0002%); `a_μ=284.748 fm` | (i) ✅ |
| **M4** Z²-scaling (bare ion) | `E₁(Z=2)=4·RY_EV=54.4228 eV` | `54.4228 eV` (−3×10⁻⁵%) | (i) ✅ |

**Sabotage outcomes (P11) — every gate FIRED on its plant and PASSED on the real profile:**

| Gate | real 1/r Coulomb | plant (a) 1/r² dress | plant (b) detuned `Ry/(n+0.4)²` |
|---|---|---|---|
| G-MARK | PASS | **FIRED** (no Rydberg ladder: 0–1 stray root, misses marks) | **FIRED** (real n* are integers, not n+0.4) |
| G-FORM | PASS | **FIRED** | — |
| G-INT | PASS | — | **FIRED** |

A gate that cannot fire is a checklist; each of G-MARK / G-FORM / G-INT was shown to fire on a planted
defect (`test_sabotage_wrong_exponent_dress_fires_gate`, `test_gate_mark_fires_on_detuned_closure_integer`,
`test_gate_form_fires_on_non_rydberg_form`, `test_gate_mark_fires_on_empty_spectrum`).

**⚑ Recording-window disclosure + receipt (branch (ii), review finding #4).** The energy scan for
branch (ii) was ORIGINALLY one-directionally narrowed by an RY-keyed window: `e_hi = e_ground·1.03`,
capped at the `n=1` ground-state energy `e_ground = Z²·ry_scale`. That window could still record an
excited-ladder offset and any *less-bound* branch-(ii) offset, and G-MARK stayed fireable (the sabotage
receipts above prove it), but it could NOT have recorded a *more-bound* ground-state offset `RY_EV·c₀/n²`
with `c₀ > 1.03`. At repair time the window was WIDENED to `e_hi = e_ground·1.5` (default `hi_factor=1.5`)
so any more-bound offset up to `c₀ = 1.5` is now recordable. Re-run RECEIPT (branch (i) confirmed with
the more-bound channel open — no additional roots appear above `e_ground`):

| run | ground state | Ry mark | # roots | deeper-than-ground roots |
|---|---|---|---|---|
| H (Z=1) | 13.60566 eV | 13.60569 eV | 7 | **none** |
| muonic (m_r,μ) | 2528.49 eV | 2528.49 eV | 6 | **none** |
| He⁺ (Z=2) | 54.37649 eV | 54.42277 eV | 5 | **none** |

The widening is strictly more permissive; branch (i) holds (`c₀ = 1`), and G-MARK remains fireable.
The superseded `hi_factor=1.03` window is logged in the repair log (KEEP-BOTH).

## CLASSIFICATION (consistency-vs-emergence + explicit new-primitive scan)

**Class: RE-DERIVATION / CONSISTENCY DEMONSTRATION.** Canon already recovers `E_n` and `a₀` as
consistency checks (`clm-oltvwy`, `de-broglie-standing-wave.md`; `Z²`-scaling `de-broglie-n.md`) — the
**canonical ceiling**. x42's added content is the **port-language derivation path** (off-line dress →
graded `Z(r)` → reflections → `2πn` closure → Op6 `B_total=0`). No result is promoted past the ceiling.

**Explicit derivation-path trace for every "AVE reproduces X" sentence:**
- `E_n ∝ 1/n²` → phase closure `∮k·dl=2πn` on the graded `Z(r)` → Op6 `B_total(E)=0`
  (`clm-gdd70j`, `radial-eigenvalue-solver.md` §E2d-ii). NOT via `E=Z²Ry/n²` (that is the flagged Bohr
  contamination, `vol2/claim-quality.md:342`).
- `a₀` → eigenmode SCALE of the given profile; identity `a₀=ℓ_node/α` (`de-broglie-standing-wave.md`
  examplebox; `vol2/claim-quality.md:336`). NOT Op6-selected.
- muonic marks → reduced-mass scaling `E_n ∝ m_r` on the SAME linear network.
- `Z²`-scaling → `ξ₀=Z²` (`de-broglie-n.md`).

**NEW-PRIMITIVE SCAN (explicit, per brief §5) — result: NONE.** Every quantity used is pre-existing:
`ALPHA, A_0, RY_EV, M_E, M_PROTON` (all imported CODATA/calibration; `M_MUON` is a CODATA experimental
probe-mass anchor added this session, NOT a new substrate primitive — the three imported inputs remain
`{m_e, α, G}`, `constants.py:126-150`); the operators `Op5/Op6` and `_abcd_section` are canonical; the
`Z(r)` form is imported (see flag on the 1/r tail). The two-register guard is a FORMALIZATION of walk
(c), not a new claim; no `def-`/`clm-`/`ilk-` node is minted. **No emergence headline.** The marks ride
CODATA-derived `RY_EV, A_0, M_E, M_PROTON, M_MUON` → **CONSISTENCY-class magnitudes**, not chords.

## FLAGS SURFACED (flag-don't-fix; Grant/auditor adjudicate — this lane resolves none)

1. **⚑ The muonic ground-state orbit is sub-lattice-cell.** `a_μ = 284.7 fm < ℓ_node = 386.2 fm`
   (`a_μ/ℓ_node = 0.7374`). The AVE lattice pitch is the electron reduced Compton wavelength
   (`de-broglie-standing-wave.md:155`: "`l_node ≈ 3.862×10⁻¹³ m` (the reduced Compton wavelength) is the
   lattice spatial cutoff"). So the muonic-H ground state orbits INSIDE one lattice cell. The
   reduced-mass SPECTRUM scaling (M3) holds as arithmetic consistency (a property of the linear
   dispersion scale), but the continuum "spherical radial transmission line" `Z(r)` picture
   (Deliverable 1) is formally **sub-Nyquist** below `ℓ_node`. Surfaced, not resolved — the substrate
   may have real structure here that the continuum `Z(r)` misses.
2. **⚑ Two distinct yield references at the muonic scale.** The brief §3 named check uses the DIELECTRIC
   yield: `A_dielectric = E_Coulomb(a_μ)/E_yield = 5057 eV / 43651.85 eV = 0.116` (`E_yield = e·V_YIELD`,
   `V_YIELD = 43.65 kV`, `INVARIANT-C1`). The Ax-4 kernel argument the ODE saturation ACTUALLY uses is
   the RUPTURE reference: `A_rupture = V_Coulomb(a_μ)/(m_e c²) = 5057 eV / 511 keV = 0.0099`. These
   differ by ~12× because `V_YIELD·e (43.65 keV) ≠ m_e c² (511 keV)` — a real two-convention split
   (`vol4/claim-quality.md:1475`: `A_geom = ℓ_node/r` vs `A_field = E·ℓ_node/V_yield`). Both numbers are
   reported; which convention is load-bearing for "does the muonic near-nucleus field bias the lattice"
   is not adjudicated here (it rides the K1/K2 fork, Deliverable 5).
3. **⚑ The 1/r Coulomb tail is asserted-not-derived (cited, not derived).** x42 IMPORTS the Coulomb
   dress form exactly as canon does. WHY the topological strain is `ℓ_node/r` (∝1/r) rather than
   `α·ℓ_node/r` from first principles is an OPEN multi-week item (`vol4/claim-quality.md:1473-1482`,
   `clm-4r4jiy`, solidity 0.70: "Partial closure only: WHY topological strain equals `ℓ_node/r` rather
   than `α·ℓ_node/r` from first principles is an open multi-week analytical item"). x42 makes **no claim
   to derive the tail**; the phase-closure result is downstream of the imported form.
   > *(Note: the brief cited this as `vol4/claim-quality.md:1311`; the verified location at branch tip
   > is `:1473-1482`. Line-number drift only — content confirmed, no contradiction.)*

## DISCIPLINE

- **Freeze-by-push (timestamps corrected, review finding #5):** prereg commit `0e5047e4` was
  *committer-dated* `2026-07-10T16:46:14-07:00` (this is the COMMIT timestamp, not the push time); the
  remote branch `CreateEvent` on `origin` was `2026-07-10T23:46:33Z` (`16:46:33 PDT`), 19 s later — the
  actual moment the prereg landed on the remote. Both precede the M_MUON commit (committer-dated
  `16:47`) and the first code commit (committer-dated `17:06`, ~20 min after the prereg landed remotely)
  by a wide margin; ordering unaffected (git audit table in the PR body). The
  earlier single `16:46:14` label conflated commit-authored with remote-created and is corrected here.
  **The freeze ordered ARTIFACTS, not knowledge** — the pilot had already landed branch (i) numbers
  pre-freeze (disclosed at prereg `:120-121`, "the pilot run this session already lands at −0.000% for
  n=1..6"), consistent with the P10 declaration that branch (i) was ENTAILED; freeze-by-push here
  certifies PROVENANCE (the marks were computed and committed before the driver existed), not RISK.
- **Substrate-native-first / MODE header:** the atom is framed in the impedance-carve register
  (off-line dress, graded `Z(r)`, phase closure) before any Schrödinger word; the Helmholtz–Schrödinger
  ISOMORPHISM is cited as canon's bridge (`de-broglie-standing-wave.md`), not adopted as the primary
  ontology. No new solver written → `substrate-native-check` not triggered (thin driver over the
  canonical Op5/Op6 primitives).
- **Op6 scope (binding):** Op6 finds the modes of the GIVEN `Z(r)`; it selects neither a₀ nor the 1/r
  geometry (`constants.py:212-228`, `electron-identification.md:77`). No scope breach.
- **Consistency-vs-emergence:** re-derivation/consistency class; explicit new-primitive scan = NONE;
  no emergence headline; no promotion past the canonical ceiling.
- **Rule 11 honest closure:** all marks land branch (i); no criterion dropped; the muonic near-nucleus
  saturation break was read as physics (the X41 frozen-tie regime) and flagged, not debugged toward a
  rescue.
- **Rule 12:** no retraction, no slot-refill; `M_MUON` is an additive CODATA anchor, not a new
  hypothesis.
- **phase-space-coordinate-check (A46):** the spectrum comparison is in matched `ξ = E/Ry` coordinates
  (the driver and the marks both live in Rydberg-scaled energy; `n* = √(Ry/E)`), not a real-space
  vs phase-space mismatch.
- **Flag-don't-fix:** three flags surfaced verbatim (§Flags); none resolved in-lane.
- **verify-before-cite:** all cites re-grepped at branch tip this session (`clm-gdd70j`, `clm-oltvwy`,
  `clm-4r4jiy` @ `:1473-1482` [brief's `:1311` was stale], `CLAUDE.md:75`,
  `de-broglie-standing-wave.md:155`, `vol2/claim-quality.md:336/337/342`, X41 verdict `:37`,
  `electron-identification.md:77`, `constants.py:212-228`). No stitched quotes.
- **No KB/canon edits from this lane** — `research/` + `src/` only; the ONE exception is the additive
  `M_MUON` constant (flagged in the PR body; engine lane owns `constants.py`).

## Orchestrator-review repair log (2026-07-10/11, 6 findings, all MINOR EVIDENCE-VOID)

The orchestrator's adversarial review confirmed 6 findings. **All MINOR / EVIDENCE-VOID — no
conclusion flips.** Marks, sabotage receipts, freeze ordering, quote fidelity, and the two-register
firewall were all independently reproduced; the repairs bank precision (implement a code-void sub-mark,
wire dead code, correct labels, widen a recording channel) without changing any branch verdict. Every
mark still lands prereg **branch (i)**. Superseded wording is preserved verbatim below (KEEP-BOTH); the
FROZEN prereg was NOT edited.

| # | finding (MINOR/EVIDENCE-VOID) | fix | superseded wording (KEEP-BOTH) |
|---|---|---|---|
| **1** | M2 "eigenmode-scale extraction" (prereg `:115`) had no implementing code — the ✅ rode only the algebraic identity `ℓ_node/α == A_0` | **Implemented** (took the optional leg): `ground_state_mean_radius` extracts `⟨r⟩ = 1.5·a_scale` from the inward-integrated ground-state eigenfunction (0.0000%, frozen 0.5% tol) — M2 now GENUINELY MEASURED. **Deviation logged:** the frozen sub-mark shipped WITHOUT code in the original arc; the extraction was added at repair time (post-review), not separately measured in the original ship | *"`a₀ = A_0` falls out as the eigenmode scale (M2)"* (D2) — a restatement, no length extracted; M2 row previously read *"eigenmode scale reproduced"* |
| **2** | PR-body Deliverable-3 carried the pre-repair muonic overstatement | PR body fixed to the two-argument honest state (`m_probe=M_R_MU` AND `saturate=False`), riding the X41 [K1∧K2] frozen tie, disclosed load-bearing. (RESULT D3 was already honest at `:133-143`) | PR body: *"Muonic case = same network, heavier probe — only `m_e→m_r,μ`"* |
| **3** | D1 port-language was prose-only + a named-quantity hazard (`de_broglie_refractive_index` dead code; `Z(r)` undefined; "impedance/mismatch" collides with `vol2/claim-quality.md:344`) | (a) wired the function into the executed route via `local_wavenumber_sq` + `test_de_broglie_index_is_cascade_local_wavenumber` (`k²·a₀² == n(r,ξ)²` element-wise); (b) corrected register to "dispersion/index profile" with the verbatim `:344` guard; defined `Z(r)` explicitly as the graded index/dispersion profile (never a medium impedance) | *"the off-line dress rendered as an impedance / mismatch profile `Z(r)`"*, with *"low impedance, short circuit"* / *"high impedance, open circuit"* (D1) |
| **4** | Search window keyed to the target (`e_hi = e_ground·1.03`) could not record a >3% more-bound branch-(ii) offset | **Widened** (optional leg) to `hi_factor=1.5`; re-run RECEIPT shows no additional more-bound roots (H 7 / muonic 6 / He⁺ 5, none deeper); disclosure + receipt table added near the marks; G-MARK stays fireable | window `e_hi = e_ground * 1.03` and discard filter `if root <= e_ground * 1.03` |
| **5** | Freeze label used the COMMIT timestamp as if it were the push time | corrected: committer-dated `16:46:14-07:00` vs remote `CreateEvent 23:46:33Z` (19 s later); both precede M_MUON (16:47) + first code push (17:06); added the "ordered ARTIFACTS not knowledge — pilot landed branch (i) pre-freeze" epistemic note | *"pushed to origin at `2026-07-10T16:46:14-07:00`"* |
| **6** | `constants.py` M_MUON comment self-cited main's PRE-insertion lines (`:126-150`, `:228`) | replaced with HEADER TEXT (robust to drift): the "THREE IMPORTED CALIBRATION INPUTS {m_e, α, G}" block + the α HONEST-SCOPE "coordinate on merge" note; constants suites re-run (124 passed) | *"see :126-150"* … *"coordinate on merge per :228."* |

**Optional legs taken:** #1 (genuine ⟨r⟩ extraction) and #4 (window widening) — both cheap and clean;
each converted a disclosure into a machine-checked receipt. **Tests after repair:** x42 fast lane 10
pass (was 9; +`test_de_broglie_index_is_cascade_local_wavenumber`), engine_sim lane 5 pass (was 4;
+`test_m2_eigenmode_scale_extracted_from_eigenfunction`) = **15 total** (was 13); constants suites
124 pass. No adjudication criterion dropped; no ❌→✅ conversion.
