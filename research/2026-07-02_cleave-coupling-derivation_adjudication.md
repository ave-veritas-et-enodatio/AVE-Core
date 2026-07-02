# Cleave-01 coupling — first-principles derivation adjudication (receipts)

**Date:** 2026-07-02
**Lane:** implementer (adjudication receipts — NO simulation in this doc)
**Branch:** `analysis/cleave-coupling-chern-adjudication` (off main `f556dcdc`)
**Disciplines fired:** `verify-before-cite`, `ave-canonical-source`, `substrate-native-check`,
`consistency-vs-emergence`
**Class:** adjudication / consistency-class. The surviving mechanism is a **CANDIDATE**, not a
derivation — do not inflate solidity.

> **What this doc is.** The receipts for a five-agent adversarial pass (ground → three
> derivation angles → cross-examination) on the question: *does mechanically displacing a
> Cleave-01 capacitor plate pump topological charge, and if so at what magnitude?* It records
> the verdict (**UNDECIDABLE-AT-PAPER**), the single load-bearing unadjudicated assumption
> (sliding-vs-locked substrate reading), and Grant's ruling that the engine — not fiat —
> adjudicates it. The frozen pre-reg and driver that execute the ruling are separate files
> (`2026-07-02_cleave-registry-pump-chern_prereg.md`, `.../cleave_registry_pump_chern.py`).

---

## (a) The question + the prior ASSERTED finding

The Cleave-01 bench (`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md`)
tests Axiom-2 (`[Q] ≡ [L]`) by pulling a capacitor gap apart and reading a topological-charge
step. The bench's formula (`project-cleave-01.md:32-35`, verified verbatim this turn):

> "The induced topological charge is **analytically derived** as: `Q = ξ_topo · x = (4.149×10⁻⁷ C/m) × 10⁻⁶ m = 0.415 pC`"

and the requirements floor (`cleave-01-requirements-boundary-conditions.md:27`, verified):

> "`CLV-REQ-FLOOR` | The derived floor `dQ/dx = ξ_topo = e/ℓ_node = 414.9 fC/µm` … (zero free params)"

**Prior status = ASSERTED, not derived.** The coupling `Q = ξ_topo·x` is a *unit-bridge*
substitution — the `def-tk1xfm` electromechanical dictionary (`Q = ξx`,
`common/vocabulary-register.md:348-364`) whose own ceiling reads "identity-by-translation, **NOT**
emerges-from / NOT a derivation" (`:357`, verified). The bench doc *already concedes* this at the
`ξ_topo` level (`project-cleave-01.md:62`, verified): "The gap-protection is on 𝒬 (the **integer**
linking charge), NOT on ξ_topo (the **unit-bridge**) … ξ_topo is not itself a Chern number /
topological invariant." So the word "analytically derived" at `:32` over-states what the corpus
supports: a units substitution, not a mechanism. This adjudication asks whether a real substrate
*mechanism* backs that substitution — and if so, at what slope.

---

## (b) Grounding — canonical anchors (re-verified this turn, worktree HEAD `f556dcdc`)

Every anchor below was re-grepped/Read in this worktree (verify-before-cite; line numbers drift).

- **The 4₁ screw / bulk g₀.** `research/2026-06-23_chiral-vector-tlm-phase1_result.md:23` —
  "the bulk forward-propagating polarization-rotation rate **converges** … to the **4₁ screw
  pitch** (∓2.21589 rad / lattice-z-unit, srs-R / srs-L), **L-independent to machine precision**
  … with an **exact enantiomorph sign-flip**." GATE-1 (`:23`): "signed, equal-magnitude loop
  holonomy **±0.256776 rad**, EXACT diamond null." Bare pitch (`:65`):
  `(π/2)/(t_z·a_cell) = +2.22144`, matched to 0.25%. **This ±0.256776 rad OA-loop holonomy /
  bulk g₀ = 2.21589 rad per lattice-z-unit is the KNOWN ANCHOR the dual-reading run must
  reproduce.**
- **The screw operator (code).** `src/ave/core/chiral_lattice_dynamics.py:203` `find_screw_operator`
  — "a proper 4-fold rotation R about z and fractional translation t with a quarter/three-quarter
  z-pitch that maps the srs motif (mod 1) to itself — i.e. the 4_1 (right) / 4_3 (left) screw
  operator" (t_z = 1/4 or 3/4). `screw_orbit_helix` (`:222`) generates the open helix with
  `a_cell = 2√2` (verified). **Translation→rotation: advancing t_z·a_cell along z rotates the
  frame π/2.**
- **Constants.** `src/ave/core/constants.py:282` `L_NODE = HBAR/(M_E·C_0) ≈ 3.8616e-13 m`;
  `:328` `XI_TOPO = e_charge/L_NODE ≈ 4.149e-7 C/m` (verified). Do NOT hard-code these.
- **Charge = boundary linking.** `manuscript/ave-kb/common/boundary-observables-m-q-j.md:20` —
  `Q = Link(∂Ω, F_substrate) ∈ ℤ`, a "1D line/loop." The linking readout is
  `ave.topological.charge_quantization.compute_Q_link` (`src/ave/topological/charge_quantization.py:257`,
  verified — the rigorous replacement for the connected-component proxy at
  `boundary_invariants.py:146-151`).
- **ξ_topo is a unit-bridge, not a Chern number.** `research/2026-06-03_topological-charge-occupation-robustness.md:20`
  — ξ_topo is a "frozen-metric **UNIT-BRIDGE** (C/m), NOT itself a Chern number." No-hair
  (`:60`): through a Γ=−1 surface only 𝓜, 𝓠, 𝓙 are externally measurable.
- **Sliding-vs-locked fork.** `research/2026-06-03_ivim-RA-adjudication.md:108` — "canonical
  engine = SLIDING/Eulerian → a mechanical strain couples to the kernel only via the piezo
  E-field it generates." (Scope caveat — see §f.)
- **OA k→0 continuum-extraction OPEN.** `research/2026-06-23_chiral-vector-tlm-phase1_result.md:142`
  (§9) — "The k→0 continuum gyration is unsettled … the degree-3 srs band has **no isolated
  transverse photon band** … not cleanly extracted here." The literal lattice g₀ over-shoots the
  cosmic OA bound by ~40 OOM; the corpus forbids quoting its magnitude as a forward prediction
  (`manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/field-free-optical-activity.md`,
  clm-fofwr1).

---

## (c) The three angles, condensed (with the judge's REGRADES preserved)

Three independent derivation agents attacked the coupling. All three agree on more than their
verdict labels advertise: **all three conclude the bench's exact `e/ℓ_node = 414.9 fC/µm` is
NOT form-forced**, and all three route any surviving coupling through the same object — the 4₁
screw as an adiabatic Thouless/spectral-flow pump whose magnitude rides an **uncomputed Chern
number C**.

### Angle A — chiral registry-winding construction. Verdict: CONSTRUCTIBLE-WITH-GAPS.

Construction: an adiabatic **Thouless-class registry pump** (not a friction grip). Define registry
phase `θᵢ = g₀·xᵢ` between each plate's readout boundary and the substrate screw field; treat θ as
an adiabatic pump parameter of the saturated (Γ=−1-bounded) band. Per full 2π of relative registry
the pump transfers `C·e` through the readout loop `∂Ω` (C = Chern number of the occupied band over
the `(k_z, θ)` torus). Facing plates carry **opposite screw-normal signs** → `Q ∝ g₀(x₁−x₂)`;
rigid translation cancels exactly (G1). Slope (A's period = full cell `a_cell`):
`C·e/a_cell = C·ξ_topo/(2√2) = C × 146.7 fC/µm`.

- Gaps blocking DERIVED status: (1) **C uncomputed** — corpus states ξ_topo is a unit-bridge "NOT
  itself a Chern number"; C=0 is live. (2) **k→0 survival** — the lattice g₀ over-shoots the OA
  bound by 40 OOM; if continuum extraction washes g₀ out, the same wash-out plausibly kills the
  slope (new cross-link to the OA OPEN, §f). (3) **Peierls-Nabarro tension** — the electron's
  matched-impedance Γ→0 slipstream (`app-b-paradoxes/peierls-nabarro-paradox.md:12`) means matter
  translates with no substrate phase grip; must be shown reconcilable, not asserted.

### Angle B — boundary-linking / Thouless treatment. Verdict: NULL (as stated).

Precise linking calculus: `Q = Link(γ, F)`, `dLink/dt` nonzero only when flux crosses the loop.
For a rigid loop through uniform F, `∮ dl × F = 0` identically; gap change pumps only if flux is
anchored to the plate's matter — but a neutral plate is a Γ=−1 no-hair assembly presenting only
`(M,0,J)` → zero net linkable flux. The canonical **SLIDING/Eulerian** engine drags no substrate
texture. → `Q̇ = 0`. The "structural srs flux texture" rescue is corpus-ABSENT and independently
killed (axial sweep → zero crossings; transverse → area-scaling, contradicting the area-free bench
formula; net-flux-per-cell → uniform B-background, contradicting emergent-Lorentz). Under Angle B
the CLEAVE floor `dQ/dx = e/ℓ_node` is the TKI unit-bridge wearing a Thouless costume.

### Angle C — adversarial null proof: Q ≡ 0. Verdict: NULL-LIKELY-WITH-GAPS.

Two independent kills of the *static* law `Q = ξ_topo·x`: (Leg 1) the I4₁32 screw symmetry makes
`Q(x)` **periodic** in x with period `p = t_z·a_cell = (√2/2)ℓ_node` — a periodic function has
zero mean slope; the only symmetry-legal escape is integer pumping per period, quantum `e/p =
√2·ξ_topo = 586.8 fC/µm` (C's period = quarter-pitch `p`). (Leg 2) no-hair reads `Link = 0` at
every static x. Survivor = adiabatic pump through **GAP-1 (sliding-lattice spectral flow) × GAP-3
(one-sided gap-change annulus)**. That survivor **still contradicts** the bench value: `586.8·C
fC/µm`, screw-axis orientation dependence, per-period quantization.

### The A-vs-C period fork (load-bearing, real)

A and C disagree on the pump period: **full cell `a_cell = 2√2·ℓ_node`** (A → C×146.7 fC/µm) vs
**quarter-pitch `p = t_z·a_cell = √2/2·ℓ_node`** (C → C×586.8 fC/µm). Both are a √2-family away
from the bench's 414.9. The computed pump quantum settles which period is physical (pre-reg §c).

### Gate matrix — the judge's default-skeptical regrades (⚠ = regrade, PRESERVED)

| Gate | Angle A | Angle B | Angle C |
|---|---|---|---|
| G1 relativity | PASS | PASS | PASS (all sound: uniform-motion loop integral vanishes identically) |
| G2 no standing Q | PASS | PASS | PASS |
| G3 Regime-I | PASS | PASS | PASS |
| G4 sector-legality | ⚠ **OPEN** (was PASS-conditional) | ⚠ **OPEN** (was FAIL) | ⚠ **OPEN** (correctly) |
| G5 no-hair | PASS+pred | PASS (executioner) | PASS |
| G6 area-scaling | PASS (loop wins) | ⚠ **OPEN** (was FAIL) — loop-wins-at-value-0 | PASS |
| G7 magnitude | ⚠ **FAIL** (146.7 ≠ 414.9) | 0 | ⚠ **FAIL** (586.8 ≠ 414.9) |
| G8 fingerprints | PASS | PASS | PASS |

**Regrade reasons (judge, preserved verbatim in substance):**
- **A-G4: PASS-conditional → OPEN.** A grades G4 PASS "only if the Chern computation is done"; the
  computation is NOT done (A's own Gap-1). A conditional-on-uncomputed is OPEN, not PASS.
- **A-G7: FAIL** (146.7 ≠ the bench value it was built to derive) — the CONSTRUCTIBLE tier
  over-weights this.
- **B-G4: FAIL → OPEN.** The even-in-ω fixed point (`photon-ee-mapping.md:86`) kills the
  *parametric V²→ω* route, but the screw-pump route is a *linking* claim, not a V²-drive; B
  conflates the two transducers.
- **B-G4→ / B-G6: OPEN, not FAIL.** B's null is contingent on the sliding reading (see §d); under
  the locked reading the linking channel is not structurally dead, so FAIL over-states.
- **C-G4: OPEN (correctly)** — the def-tk1xfm ceiling. Note: cite the underlying identity, not the
  `status:proposed` def-node.

---

## (d) Cross-examination verdict: UNDECIDABLE-AT-PAPER + the decider

**VERDICT: UNDECIDABLE-AT-PAPER.** Neither NULL-DERIVED nor CONSTRUCTIBLE is honestly available
on paper. The A=CONSTRUCTIBLE vs B/C=NULL split is narrower than the labels: C's own GAP-1×GAP-3
*is* A's construction, and C grades it "the coupling survives only as …" — i.e. C concedes A's
mechanism as the sole survivor. The genuine disagreement is one node.

**The single load-bearing unadjudicated assumption = the sliding(Eulerian)-vs-locked(Lagrangian)
substrate reading.** Whether the 4₁ screw is a *linkable ground-state texture* (nonzero-C pump)
or *pure transport holonomy* (C=0, null) reduces to whether the substrate is read:
- **SLIDING/Eulerian** — matter drags no substrate texture → B/C null (C=0), or
- **LOCKED/Lagrangian** — finite-strain, matter co-moves → a mechanical linking channel exists.

`research/2026-06-03_ivim-RA-adjudication.md:108` (verified): "the mechanical channel exists
*only* in the LOCKED (finite-strain Lagrangian) reading … canonical engine = SLIDING/Eulerian."
**Every angle's verdict is downstream of this one fork, and none of them named it as the decider**
— A buried it in Gap-3 (Peierls-Nabarro), B cited it as settled-for-null, C did not reach it.

**Minimal computation that decides it:** sweep the readout boundary loop `∂Ω` adiabatically
through the srs chiral ground state and compute the Chern number of the occupied band over the
`(k_z, θ)` registry torus — does `Link(∂Ω, F_substrate)` accumulate a nonzero integer per registry
period, or exactly zero? Existing hooks: `find_screw_operator`/`screw_orbit_helix`
(`chiral_lattice_dynamics.py:203,222`), `compute_Q_link` (`charge_quantization.py:257`).
**C=0 → NULL-DERIVED; C≠0 → slope = C·e/(period)**, period fork settled by the same computation.

### Bench consequences (from the judge, carried forward)

- **The exact 414.9 fC/µm is NOT form-forced.** Expect `C × {146.7 or 586.8}` fC/µm if the pump
  exists. Per `cleave-01-requirements-boundary-conditions.md:19` the slope is a **demoted
  consistency corner** — a slope deviation books as "A-with-flag (F3)," NOT a chord kill. The
  datasheet already protects this.
- **The kill-test is unaffected.** The binding discriminator is the gap-independent integer floor
  surviving a ≥4× gap-sweep (`project-cleave-01.md:38`) — independent of C's *value* as long as
  **C≠0**. Only **C=0** kills the chord.

---

## (e) Grant's ruling (2026-07-02): option (b) — engine adjudicates, not fiat

Grant ruled **option (b)**: **run BOTH substrate readings.** Whichever setup reproduces the known
anchor — the OA loop holonomy **±0.256776 rad** / bulk **g₀ = 2.21589 rad per lattice-z-unit**
(`research/2026-06-23_chiral-vector-tlm-phase1_result.md:23,65`) — earns the canon slot. **Doc-109
(sliding-vs-locked) is adjudicated by the engine, not by fiat.**

Consequences pre-committed by the ruling (frozen in the pre-reg
`2026-07-02_cleave-registry-pump-chern_prereg.md`):
- The Chern machinery must first reproduce a **known quantized pump** (Rice-Mele / Thouless toy,
  C=±1) in the same run before any srs verdict counts (validate-on-known gate).
- Frozen outcome bins: `[C_slide=0 ∧ C_lock=0 → NULL-DERIVED]` / `[C≠0 in exactly one reading →
  canon-candidate IFF it also reproduces the OA anchor]` / `[C≠0 both → anchor cross-check
  adjudicates; period fork settles from the pump quantum]` / `[INCONCLUSIVE: toy-gate fail or
  non-convergence]`.
- **C must flip sign between srs-R and srs-L** (enantiomorph-odd; same-sign = red flag).
- No post-hoc bin edits.

---

## (f) Two corpus flags (flag-don't-fix — surfaced, not resolved)

### FLAG 1 — the `2√2` rad/m conversion ambiguity (OPEN, not a confirmed bug)

Angle A alleged a `×2√2` slip at `research/2026-06-23_chiral-vector-tlm-phase1_result.md:105`:
the doc converts `2.21589 rad/lattice-z-unit` by dividing by `a_cell_physical = 2√2·L_NODE ≈
1.092e-12 m` → `±2.0e12 rad/m`. A claims the coordinate unit is the BOND length (= ℓ_node;
`a_cell = 2√2` in code units ⇒ bond = 1), so the correct conversion would be `~5.75e12 rad/m`.

**Judge regrade (preserved): this is a genuine unit AMBIGUITY, not a confirmed bug.** Re-verified
`:105` this turn — it is internally consistent (per-lattice-z-unit rate ÷ physical cell length).
A over-stated it as "verified bug." **Status: OPEN.** It does NOT touch the 40-OOM
over-shoot conclusion either way. It is now **coupled to the Cleave slope** (the same z-unit ↔
physical-length convention sets both the OA rad/m and the pump `C·e/period`), so the pre-reg's
dimensional evaluation (§d) resolves it as a by-product — or documents it as still-open if a
one-hour check does not settle it.

### FLAG 2 — the OA k→0 continuum-extraction OPEN, now coupled to the Cleave slope

`research/2026-06-23_chiral-vector-tlm-phase1_result.md:142` (§9): the physically-relevant k→0
continuum gyration "is unsettled." Angle A's valid cross-link: **the Cleave slope magnitude is
coupled to this OPEN.** If continuum extraction washes g₀ out (the lattice value is ~40 OOM over
the cosmic bound), the same wash-out plausibly kills the lattice-scale pump slope. Worth adding to
the Cleave datasheet open-items (fallout scope item 8).

### Scope note on doc-109 (flag-don't-fix — do NOT silently reconcile)

`ivim-RA-adjudication.md:108-117` records a **"CORRECTED 2026-06-03 (Rule 12): RULED OUT, not
gated"** for the *piezo-transducer / IVIM E-field* channel — "the fork was reframed (doc 109 §13
boundary-envelope, impedance-only) AND closed at v14 Mode I." **That closure is scoped to the
piezo E-field channel** ("a mechanical strain couples to the kernel only via the piezo E-field it
generates = the dead field channel"). The Cleave **registry-pump** mechanism is a *different*
channel — screw-registry spectral flow / boundary linking, not a piezo E-field. Grant's (b) ruling
**reopens the sliding-vs-locked question specifically for the registry-pump reading**, to be
settled by the engine (which anchor-reproducing setup wins). This is NOT a contradiction to
silently fix: the piezo-channel closure and the registry-pump reopening are about different
transducers. Surfaced here so the auditor/Grant can confirm the scoping.

---

## (g) Three new bench corners (all three angles agree)

Added as NEW discriminating axes alongside the legacy slope/floor structure (KEEP-BOTH; full
datasheet landing gated on the pre-reg result — fallout scope item 2).

1. **Sidereal / orientation period-modulation.** The 4₁ screw axes are the crystallographic
   ⟨100⟩ axes; the K4 rest frame ≈ CMB rest frame
   (`preferred-frame-and-emergent-lorentz.md`). The pump period `p` is the screw z-pitch, so the
   slope should **modulate with plate-normal-vs-screw-axis orientation as the Earth rotates
   through the substrate/CMB rest frame.** This is a **PERIOD effect, NOT (qℓ)⁴-suppressed** —
   it is sharper than the cubic dispersion anisotropy (which *is* `(qℓ)⁴`-suppressed). A sidereal
   modulation of the slope, if present, is a screw-axis fingerprint.
2. **Moving-dielectric-slab-at-fixed-gap → exactly zero (null control).** Translating a dielectric
   slab at FIXED gap leaves the readout loop linking unchanged → **zero signal.** A clean
   drag/entrainment discriminator: any mechanism that *entrains* substrate texture would pump here;
   the registry-pump does not. (Both A-G5 and B-G5 predict the null.)
3. **The STAIRCASE phase-native readout.** The honest Thouless signature is **quantized charge per
   closed 2-axis drive cycle** — an integer × C·e per cycle, shape-independent, **V-independent,
   present at V=0** (the pumped current is in-phase with dither VELOCITY, not with V; parasitic
   capacitive coupling is ∝V, extrapolates to zero at V→0). **A linear slope with NO staircase is
   dictionary-echo, not linking** — the staircase is the chord-grade observable Grant's
   epistemology wants. `slope-without-staircase = dictionary echo.`

*(Phase-space note, not bench-ready: a 2:3 Lissajous drive is a phase-space discriminator between
the 4-fold structural screw (null at 2:3, response at 4-fold harmonics) and the Cosserat (2,3)
winding channel (response at 2:3). Coordinate-legal only in phase space — do NOT build real-space
trefoils. Stage-2, not a bench corner.)*

---

## Claim-quality entry (minted — CANDIDATE, do not inflate)

- **clm-cleave-coupling-adjudication** — *The Cleave-01 plate-displacement → topological-charge
  coupling is UNDECIDABLE-AT-PAPER; the sole surviving mechanism class is an adiabatic
  Thouless-class registry pump over the 4₁ screw texture, whose existence (C≠0) and slope
  (C×146.7 or C×586.8 fC/µm) are gated on an uncomputed Chern number and on the sliding-vs-locked
  substrate reading. Grant ruled (b): the engine adjudicates via anchor-reproduction.*
  - **class:** adjudication / consistency-class.
  - **solidity:** CANDIDATE. The mechanism is constructible-with-gaps (Angle A) and conceded as the
    sole survivor by the null proof (Angle C), but no gate reaches DERIVED — G4 OPEN (Chern
    uncomputed), G7 FAIL for the exact bench value (both surviving periods are √2-family off).
  - **asserted-vs-derived:** the *forms* (linear-in-x, polarity-odd, gap-independent,
    area-independent) are FORM-forced; the *value* 414.9 fC/µm is a VALUE-import through the
    ξ_topo unit-bridge, NOT a derived pump efficiency.
  - **downstream gate:** `research/2026-07-02_cleave-registry-pump-chern_prereg.md` (frozen) →
    `..._result.md` (the engine verdict).


