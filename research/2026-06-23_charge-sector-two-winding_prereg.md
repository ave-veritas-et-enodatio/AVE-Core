# Charge-Sector Two-Winding Interaction — Pre-Registration

**Date:** 2026-06-23
**Lane:** LANE A PATH-(b) — charge-sector two-body interaction on the Cosserat (2,q) winding engine (chord-priority)
**Branch:** `analysis/charge-sector-two-winding`
**Status:** FROZEN pre-run. Refute-by-default.

Path-(a) (mass-sector on the scalar compression engine) returned a **WALL-engine
null** — the compression sector has no shear momentum to transduce a force.
Grant ruled pivot to the sector that genuinely carries the charge DOF.

---

## SUBSTRATE-FIRST SECTOR HEADER (mandatory, before any standard-physics word)

**WHICH SECTOR.** The Cosserat micro-rotation **(2,q) WINDING** sector — where
charge lives. Charge is **not** a tacked-on label here: it is the
through-linking / Beltrami helicity of the micro-rotation circulation,
`H_bel = ∫ ω·(∇×ω)`, on the T2 couple-stress grade. Anchor:
`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20`
(the two-"3"s disambiguation — A1 dilatation-MASS ⊥ T2 (2,3)-WINDING; "charge =
Beltrami helicity"). This sector **carries** the charge DOF; the scalar
compression engine (path-a) does **not**.

**ENGINE-CARRIES-THE-DOF CHECK (the substrate-native-check — done FIRST, not
assumed).** The verdict is recorded in §1 below. Summary: **YES** — the bare
Cosserat field engine `ave.topological.cosserat_field_3d.CosseratField3D`
genuinely carries (a) seeding TWO helical ω circulations at separated centers
with independently-chosen helicity SIGN (= charge sign), (b) evolving them under
a conservative **real force** `I_ω·ω̈ = −∂W/∂ω` (velocity-Verlet `step()`,
`use_impedance_boundary=False` = byte-identical `−∇W/mass`), and (c) reading the
inter-winding separation over time via `find_soliton_centroids`. This is a
genuine two-winding-dynamics engine — **NOT** a path-(a)-style capability wall.

**REGIME (declared before running, reasoned from the substrate).** The
charge–charge interaction is tested in the **cold–linear / sub-yield reactive**
regime: small-amplitude helical ω wavepackets (|ω| ≪ ω_yield = π) so the
saturation kernel S ≈ 1 and the medium responds as a **lossless reactive
elastic** medium (Ax-3-faithful). Rationale: a static Coulomb-like force between
two stable charges is a *reactive field-overlap* phenomenon, not a driven /
near-yield / ruptured one. (Near-yield / saturated regime is reserved for
pair-creation & annihilation — a DIFFERENT physics question, hosted by the
`UnifiedGenesisEngine`/`AnnihilationEngine` lineage, which we explicitly do NOT
use here because its dynamics are dominated by a per-cell snap state machine
that is "NOT a bulk force" — `unified_genesis_engine.py:52,447` — and would
confound the conservative charge-charge force with snap/drive/wall artifacts.)
A **saturated cross-check** at larger amplitude is pre-registered as a secondary
arm (§4 arm S) to bound regime-dependence, but the headline verdict is read in
the cold regime.

---

## 1. ENGINE-CARRIES-THE-DOF VERDICT (substrate-native-check, done before code)

**Verdict: the Cosserat engine CARRIES the two-winding charge DOF.** Evidence
(file:line, verified this session):

- **Charge DOF present.** `_beltrami_helicity(ω)` =
  `ω·(∇×ω)/(|ω||∇×ω|)` (`cosserat_field_3d.py:533`) is the local handedness; the
  `helicity` parameter of `initialize_gaussian_wavepacket_omega`
  (`:2133,2158-2160`) seeds a corkscrew ω field with nonzero Beltrami helicity —
  *the charge*; "the sign sets handedness (e⁻ vs e⁺)" (`:2158`).
- **Two windings seedable at separated centers.**
  `initialize_gaussian_wavepacket_omega(center=…, helicity=…)` takes an arbitrary
  `center` (`:2127`) and the ω field is additive — two calls (or one call +
  manual superposition) place two windings at `cA`, `cB`. The
  `AnnihilationEngine._two_object_build` (`test_annihilation_evaporation.py:53`)
  is an existing working precedent for two separated chiral windings with
  independent helicity signs.
- **Real conservative force between them.** Time-domain `step()`
  (`cosserat_field_3d.py:2022`) integrates `I_ω·ω̈ = −∂W/∂ω` by velocity-Verlet
  (`:2031-2032`); with `use_impedance_boundary=False` it is the bare `−∇W/mass`
  (`:2090-2092`). Two overlapping helical ω fields exert a genuine mutual torque
  through the shared energy functional `W` — this IS the medium pushing them.
- **Two-body readout present.** `find_soliton_centroids` was built precisely
  "to identify MULTIPLE soliton centroids … after pair creation, we expect TWO
  distinct centroids" (`:2241,2253`). Inter-centroid separation vs time → the
  sign of d(sep)/dt is the attract/repel verdict.

This is qualitatively different from path-(a): path-(a)'s compression engine
lacked the shear momentum DOF to transduce a force at all. Here the DOF is
carried end-to-end.

---

## 2. THE SUBSTRATE QUESTION (framed substrate-native, NOT "Coulomb scattering")

Two electron charge-windings — each a helical (corkscrew) Cosserat
micro-rotation ω circulation with the **same** Beltrami-helicity sign (=
like charge) — are placed near each other in the lattice. Their circulation
fields overlap through the medium. **Does the lattice push them apart?**

Then: does the substrate's charge–charge interaction **DIVERGE from textbook
1/r** in an AVE-distinct way (the chord-target)?

---

## 3. VALIDATE-ON-KNOWN — pre-registered expected SIGN (frozen BEFORE running)

**Known physics (the calibration anchor):** two like-handed (like-charge)
circulations are known to **REPEL**. This is the substrate-native validate-on-
known: like-charge → repulsion → **inter-centroid separation INCREASES** with
time (d(sep)/dt > 0), and the linear momentum imparted to each winding points
**away** from the other.

**Pre-registered PASS criterion (validate-on-known):**
- **PASS-VOK:** like-helicity pair (hA = hB = +1) → Δsep(t) > 0 monotonically
  over the recording window, AND the per-object linear-momentum component along
  the separation axis is **outward** (sign away from the partner), to within
  the symmetric-control tolerance below.
- **Opposite-helicity control (hA = +1, hB = −1):** the SIGN must FLIP — unlike
  charges → **attract** → Δsep(t) < 0. (Validate-on-known is only credible if
  the probe also reads the *opposite* sign on the known-opposite reference; the
  v6 m-even lesson, `test_annihilation_evaporation.py:6-8`.)
- **Achiral control (hA = hB = 0):** zero net Beltrami helicity → no charge →
  the inter-object force along the separation axis is **≈ 0** (below the
  symmetric-control tolerance). This is the null that proves the force we
  measure is *charge*-borne, not a generic wavepacket-overlap pressure.

**HALT condition (calibration broken):** if the achiral control shows a force
of the same magnitude as the charged pair, the probe is measuring overlap
pressure not charge — HALT and report, do not proceed to the chord assessment.

**Symmetric-standard note (consensus-bias guard).** SM does not *derive* the
sign of the Coulomb force from a deeper structure either — it posits the gauge
coupling. So a SIGN match here is a *consistency* win for AVE, scored on the
same standard SM is scored on; the AVE-distinct content (the *chord*) is sought
only in the DIVERGENCE from 1/r (§5), not in the sign itself.

---

## 4. METHOD (driver: `src/scripts/vol_1_foundations/charge_sector_two_winding.py`)

Engine: `CosseratField3D`, `use_saturation` per-arm, `use_impedance_boundary=False`
(conservative `−∇W/mass`), `damping_gamma=0` (energy-conserving VV — we want the
*force*, not a relaxed bound state). PML on (absorbing edge per Ax-1/Ax-3) with
explicit **PML-cell exclusion** on all centroid/peak extractions (A-Rule-10
corollary): only `pml_thickness ≤ {i,j,k} ≤ N−pml_thickness−1` interior cells
enter the centroid argmax/argpartition.

**Coordinate discipline (A46 / phase-space-coordinate-check).** The corpus claim
"charge = Beltrami helicity" is a **real-space** statement about the Cosserat ω
micro-rotation field (master-equation.md:20 explicitly: REAL-SPACE, NOT the
phase-space (V_inc,V_ref) Clifford-torus winding, NOT the A1 phasor). The
observable here — inter-centroid separation of the ω-density and the ω-field
linear momentum — is measured in the **same real-space lattice-Cartesian
coordinates** as the helicity that defines the charge. Coordinates match the
claim. (This is NOT a phase-space φ² claim, so the A46 phase-space-mismatch trap
does not apply; recorded explicitly per the check.)

**Density-peak vs centroid sampling (A-Rule-10).** ω wavepackets are
quasi-Gaussian blobs (not shells), so the energy-weighted centroid of each
connected `|ω|²` component IS the load-bearing position. `find_soliton_centroids`
already energy-weights (`:2272-2276`). For the per-object momentum we sum over
each object's half-mask (the `half_masks` partition), top-K excluded only if a
shell structure emerges.

**Reactance-pair tracking (Rule-10).** Record at EVERY step over the window:
per-object (a) centroid position, (b) C-state proxy `∫|ω|²` (the across /
field-amplitude state) and (c) L-state proxy `∫|ω̇|²` (the rate state), plus
total Hamiltonian `H = T + V` (energy-conservation guard — if H drifts > 5% the
force reading is integrator artifact, not physics).

**Arms (all pre-registered):**
- **Arm A (headline, cold):** like-helicity pair, small amplitude (peak |ω| ≈
  0.05, ≪ ω_yield = π), `use_saturation=True` but S≈1 so effectively linear.
  Sep(t), momentum sign, controls.
- **Arm B (opposite-helicity control):** as A with hB = −1.
- **Arm C (achiral null):** as A with hA = hB = 0.
- **Arm R (1/r form — the chord hunt):** like-helicity pair swept over initial
  separation d₀ ∈ {6, 8, 10, 12, 14} cells; measure the initial outward
  acceleration a(d₀) (second difference of sep at t=0⁺, before the wavepackets
  disperse). Fit log a vs log d₀ → exponent n (Coulomb-native n = −2 for
  *force*; if the engine reproduces 1/r² the slope is −2). Residual from the
  −2 power law at SHORT range is the chord candidate.
- **Arm S (saturated cross-check):** Arm R at peak |ω| ≈ 0.5·ω_yield to bound
  regime-dependence of the exponent. Secondary; does NOT set the headline.

**Scale (honest).** N = 48³ interior (matches the genesis-engine frozen scale),
pml_thickness = 4, window = enough steps for the centroids to move ≳ 1 cell but
before wavepacket dispersion dominates (auto-stop when either object's `∫|ω|²`
drops below 50% of its t=0 value — dispersion guard). Reduced-scale smoke
(N=24) validates the probe chain first.

---

## 5. CHORD ASSESSMENT — pre-registered DIVERGENCE targets

The AVE-distinct chord (if any) is a DEPARTURE of the charge–charge interaction
from the textbook point-charge 1/r potential / 1/r² force. Pre-registered
candidate divergences, in priority order:

1. **Short-range winding-overlap correction.** When the two ω circulations
   overlap (d₀ ≲ wavepacket σ), the force should depart from −2 power law —
   a finite-size / form-factor softening (or hardening) from the *extended*
   helicity distribution. PRE-REGISTERED chord signature: a(d₀) flattens or
   turns over at d₀ ≲ 2σ relative to the −2 extrapolation from large d₀.
2. **Chirality / handedness dependence.** Does the force MAGNITUDE (not just
   sign) differ for the (RH,RH) pair vs the (LH,LH) pair? In a *parity-symmetric*
   medium they must be identical; an AVE-distinct chord would be a
   handedness-dependent magnitude (a chiral-medium signature, the
   `κ_chiral·h_local` asymmetry of Op14, `cosserat_field_3d.py:605-606`).
   PRE-REGISTERED: |a_RR| vs |a_LL| compared; equality = parity-clean (consistent
   with SM); inequality = candidate chord (flag, do not rescue).
3. **(q·ℓ_node) correction.** A dispersion-style correction scaling with the
   winding "wavevector" q × ℓ_node (the same family as the
   `(q·ℓ_node)⁴` dispersion forward-prediction). Sought as a residual in the
   Arm-R exponent fit; LOW expected — a force-law correction at this order is
   only resolvable if the short-range arm is clean.

**Refute-by-default.** The DEFAULT expected outcome is **CONSISTENCY**: the
substrate reproduces the like-charge repulsion sign (validate-on-known PASS) and
a roughly 1/r² force with NO statistically resolvable AVE-distinct divergence at
this engine resolution — i.e., an *echo* of textbook electrostatics, not a
chord. A chord is claimed ONLY if a pre-registered divergence (1, 2, or 3) is
resolved above the energy-conservation / dispersion noise floor.

---

## 6. CLASSIFICATION (consistency-vs-emergence, fired)

- The **sign** of the force (like-charge repulsion): **CONSISTENCY** class — a
  match to known physics, scored on the symmetric standard (SM posits it too).
  NOT an emergence claim.
- The **force law exponent** (1/r²): **CONSISTENCY** class if it matches; the
  engine inputs (G, G_c, γ, ω_yield = π in natural units) are
  substrate-pinned O(1), not CODATA-substituted, so there is no SI-substitution
  emergence trap (A47 v17 family) — but a 1/r² recovery is still a *consistency*
  result (recovering known electrostatics), not an emergence headline.
- A resolved **short-range / chirality / (q·ℓ_node) divergence**: would be a
  **MANIFESTATION** of substrate structure (the winding is extended, not a point)
  — the chord-class result IF resolved. Tagged candidate-chord, flag-don't-fix.

No `ave.core.constants` CODATA value is load-bearing for the headline sign or
exponent (the engine runs in natural units G=γ=ρ=1, ω_yield=π). `ALPHA` enters
only via `KAPPA_CHIRAL_ELECTRON` in the *chirality-magnitude* arm (candidate
chord #2), where it is the calibration prefactor on the topological κ̃ — flagged
as calibration-input, not emergence.

---

## 7. ADJUDICATION TABLE (frozen — do not drop criteria post-hoc, Rule 11)

| Arm | Measurement | PASS / chord criterion | Outcome (filled post-run) |
|-----|-------------|------------------------|---------------------------|
| A (cold, like) | Δsep(t), p∥ sign | Δsep>0 & p∥ outward | — |
| B (opposite ctrl) | Δsep(t) sign | sign FLIPS to <0 | — |
| C (achiral null) | force ∥ sep | ≈0 (< tol) | — |
| R (1/r law) | exponent n | report n; chord if short-range residual > noise | — |
| S (saturated) | exponent n_sat | report; regime-dependence bound | — |

**Honest-closure commitment (Rule 11).** If validate-on-known FAILS (wrong sign,
or achiral null shows force) → clean negative, name the mechanism, close the
branch — no rescue debugging. If validate-on-known PASSES but no chord divergence
resolves → CONSISTENCY/ECHO result, recorded as such, NOT upgraded to a chord.
Criteria above are frozen; converting any — to ✅/❌ requires the as-written test.
