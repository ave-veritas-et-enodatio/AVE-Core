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
