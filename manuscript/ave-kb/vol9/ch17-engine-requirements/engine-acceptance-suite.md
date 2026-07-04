[↑ Ch.17 Engine Requirements](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Derivation-support wiring leaf for the ground-up engine-acceptance suite (src/tests/engine_acceptance/). Hosts one sup- node per acceptance test that strengthens a clm-/def- beneficiary's DERIVATION confidence (INVARIANT-S9: a simulation is a sup-, never an exp-). No new substrate-physics claim — every sup- wires an already-canonical claim, authoring quality + on-point fraction as *pending* (INVARIANT-S10: a pending support contributes nothing and never drags a beneficiary to pending)."
sup-id: sup-uiny42
supports:
  - clm-hd9bee: *pending*
sup-id: sup-zf5d1t
supports:
  - def-7c3f9e: *pending*
sup-id: sup-u7r3vu
supports:
  - clm-dfaiwj: *pending*
sup-id: sup-l2ah0k
supports:
  - clm-8nkvwy: *pending*
sup-id: sup-2qja9z
supports:
  - clm-gz7ryg: *pending*
  - clm-8nkvwy: *pending*
sup-id: sup-su0h1a
supports:
  - clm-3npynp: *pending*
  - clm-djpx2v: *pending*
sup-id: sup-iryl5d
supports:
  - clm-djpx2v: *pending*
sup-id: sup-xn9y6c
supports:
  - clm-3npynp: *pending*
  - clm-j550uh: *pending*
sup-id: sup-xey8a8
supports:
  - clm-yr6tu4: *pending*
sup-id: sup-w6tjvs
supports:
  - def-7c3f9e: *pending*
  - def-0pt1ac: *pending*
sup-id: sup-oicgzy
supports:
  - clm-crbl60: *pending*
  - clm-8nkvwy: *pending*
sup-id: sup-1sq5c1
supports:
  - clm-8nkvwy: *pending*
sup-id: sup-lorxuk
supports:
  - clm-k9up5c: *pending*
  - clm-07kd5v: *pending*
sup-id: sup-874l1g
supports:
  - clm-8nkvwy: *pending*
  - clm-5s5b0d: *pending*
sup-id: sup-ftxwil
supports:
  - clm-3zz0f6: *pending*
  - clm-8nkvwy: *pending*
sup-id: sup-evhfcd
supports:
  - clm-sysqaf: *pending*
  - clm-m7qd0w: *pending*
sup-id: sup-1ecv2m
supports:
  - clm-kezk9z: *pending*
  - clm-uatcql: *pending*
sup-id: sup-xgx063
supports:
  - clm-ka5zdx: *pending*
  - clm-unk0bd: *pending*
sup-id: sup-wuy333
supports:
  - clm-rtdmsn: *pending*
sup-id: sup-x7h9yh
supports:
  - clm-ka5zdx: *pending*
  - clm-uatcql: *pending*
sup-id: sup-3kq9w7
supports:
  - clm-crbl60: *pending*
sup-id: sup-mz4t0p
supports:
  - clm-gz7ryg: *pending*
-->

# Engine-Acceptance Suite — Derivation-Support Map (L0–L2 + Op/scale tier + L3 EXISTENCE rung)

This leaf wires the ground-up engine-acceptance suite (`src/tests/engine_acceptance/`)
into the KB claim-DAG. The suite is a pytest regression gate built from the medium
up, one excitation-layer at a time, each test a falsifiable physics claim with a
frozen pre-registered pass/fail bin (the orchestration plan
`_orchestration/2026-06-16_groundup-engine-acceptance-plan.md`). Per the §8
STANDING PER-LAYER COMPLETION RITUAL step 1.5 (MAP-TO-SPINE), each green test that
**strengthens** an already-canonical `clm-`/`def-` is materialized here as a `sup-`
derivation-support node.

**Sims register as `sup-`, never `exp-` (INVARIANT-S9).** A simulation is not an
experiment: it feeds a claim's *derivation* confidence (the min-branch), never its
*experimental* solidity. `exp-` is reserved for a physical apparatus AVE designs,
originates, and controls. Each `sup-` here lifts the DERIVATION branch of its
beneficiary.

**Every fraction is `*pending*` (INVARIANT-S10).** The local rigor `quality` and
every `supports:` on-point fraction are authored `*pending*` — this leaf WIRES the
graph; it does not SCORE it. A `*pending*` support contributes nothing to a
beneficiary's `local_quality` and **must never drag a beneficiary with otherwise-valid
quality to pending** (CRITICAL clause, `manuscript/ave-kb/CLAUDE.md:235`). Back-solving
a fraction is forbidden.

**Tests with NO clm-/def- target get NO sup- node** (a `sup-` with no beneficiary is
malformed). Five green tests are medium-validity checks or honest gap-findings with no
positive claim to strengthen — tracked by test-id in the plan §9, not wired here:

- **T0.2** (Z₀ = √(μ₀/ε₀)) and **T0.3** (isotropy) — Class-A identity / medium-validity,
  no `clm-` beneficiary (plan §9 Spine: "— (medium-validity, no clm-)").
- **A1a** (6-DOF/node + srs connectivity) — a STRUCTURE check whose load-bearing output
  is the HONEST DOF-capability FINDING (`carried_dof == 2` vs `axiom_dof == 6`); it
  records a gap, it does not strengthen a positive claim.
- **T1.7** (longitudinal-bulk wave) and **T1.8** (Cosserat micro-rotation wave) —
  STOP-and-report MEDIUM-EXTENSION FINDINGS (the mode is NOT carried). A finding that a
  mode is absent records the precise L3/L4 medium-extension gap; it does not strengthen
  the precursor's derivation. Wiring a `sup-` to a precursor from an absence-finding
  would mis-credit the precursor. Tracked by test-id; not wired.

The matching `### Quality` entries (one per `sup-` above) live in the Vol 9 register
`../claim-quality.md`. The frozen pre-registered bins and the substrate-native-check
walk live in each test's docstring.

## Layer index

| Layer | Test (file) | sup- node | beneficiaries |
|---|---|---|---|
| L0-medium | T0.1 (`test_l0_medium.py`) | sup-uiny42 | clm-hd9bee |
| L0-axioms | A1b (`test_l0_axioms.py`) | sup-zf5d1t | def-7c3f9e |
| L0-axioms | A2 (`test_l0_axioms.py`) | sup-u7r3vu | clm-dfaiwj |
| L0-axioms | A3b (`test_l0_axioms.py`) | sup-l2ah0k | clm-8nkvwy |
| L0-axioms | A4 (`test_l0_axioms.py`) | sup-2qja9z | clm-gz7ryg, clm-8nkvwy |
| L1-photon | T1.1 (`test_l1_photon.py`) | sup-su0h1a | clm-3npynp, clm-djpx2v |
| L1-photon | T1.2 (`test_l1_photon.py`) | sup-iryl5d | clm-djpx2v |
| L1-photon | T1.3 (`test_l1_photon.py`) | sup-xn9y6c | clm-3npynp, clm-j550uh |
| L1-photon | T1.4 (`test_l1_photon.py`) | sup-xey8a8 | clm-yr6tu4 |
| L1-photon | T1.5 (`test_l1_photon.py`) | sup-w6tjvs | def-7c3f9e, def-0pt1ac |
| L1-multiwave | T1.6 (`test_l1_multiwave.py`) | sup-oicgzy | clm-crbl60, clm-8nkvwy |
| L2-em-media | T2.1 (`test_l2_em_in_media.py`) | sup-1sq5c1 | clm-8nkvwy |
| L2-em-media | T2.2 (`test_l2_em_in_media.py`) | sup-lorxuk | clm-k9up5c, clm-07kd5v |
| L2-em-media | T2.3 (`test_l2_em_in_media.py`) | sup-874l1g | clm-8nkvwy, clm-5s5b0d |
| L2-em-media | T2.4 (`test_l2_em_in_media.py`) | sup-ftxwil | clm-3zz0f6, clm-8nkvwy |
| Op/scale tier | Op-primitive + scale-invariance (`test_operators.py`) | sup-evhfcd | clm-sysqaf, clm-m7qd0w |
| L3-existence | T3.1 longitudinal-mode-is-real (`test_l3_mass_cage.py:214`) | sup-3kq9w7 | clm-crbl60 |
| L3-existence | T3.2 c_eff(V) stiffening (`test_l3_mass_cage.py:388`) | sup-mz4t0p | clm-gz7ryg |
| L3-existence | T3.3 Γ=−1 wall (`test_l3_mass_cage.py:526`) | sup-1ecv2m | clm-kezk9z, clm-uatcql |
| L3-existence | T3.4a mass=cutoff (`test_l3_mass_cage.py:645`) | sup-xgx063 | clm-ka5zdx, clm-unk0bd |
| L3-existence | T3.4b cold/α-FREE Q (`test_l3_mass_cage.py:645`) | sup-wuy333 | clm-rtdmsn *(echo-corroboration)* |
| L3-existence | T3.4c persistence (`test_l3_mass_cage.py:645`) | sup-x7h9yh | clm-ka5zdx, clm-uatcql |

## L3 EXISTENCE rung (T3.1 / T3.2 precursors + T3.3 / T3.4 posited mass-cage, RUNG-1)

> **🔴 NATIVE-STENCIL QUALIFIER on the bulk Γ=−1 cage rows T3.3/T3.4 (2026-06-24, Rule 12 — rows + bins UNCHANGED).** These rows **POSIT** a saturated A1-scalar core and test what properties it exhibits GIVEN the core (consistency-class, on the Cartesian Master-Equation engine). The Stage-2 native-cage make-or-break ([`research/2026-06-24_engine-stage2-native-cage_result.md`](../../../../research/2026-06-24_engine-stage2-native-cage_result.md)) returned energy-certified **MODE-III DISPERSE**: the cage does **not dynamically SELF-TRAP a seeded sech on the native K4 stencil** (WITH c_eff(V)). So the **bulk self-focusing-well route is RULED OUT (a Cartesian-grid artifact)** and the **Cartesian PASS on these rows = a continuum-reference**, not a native-substrate self-forming cage. This **sharpens** the existing "HONEST SCOPE — POSITS not SELF-FORMING" qualifier (:237): not only is self-formation un-shown, the *dynamical bulk self-trap is now falsified natively*. What STANDS: the cage as a Γ=−1 **boundary condition** + the static gapped bound-mode / persistence consistency checks (boundary/topological localization); the CI-gated bins are unchanged. **mass = A1 (#260) untouched.**
>
> 🟡 **EVIDENTIARY-EXPOSURE POINTER (2026-07-03, verdict-exposure sweep — status-demotion, NOT retraction):** the Stage-2 MODE-III DISPERSE evidence this qualifier leans on is now **HIGH-exposed** (diamond `TETRA_OFFSETS` `L_D` nullspace-heavy / sublattice-decoupled; the positive control ran on the *Cartesian* engine, not the native pipeline) and **UNDER RE-ADJUDICATION**. The rows + bins remain unchanged and CI-gated; what re-opens is the *sharper* "dynamical bulk self-trap falsified natively" claim, not the rows themselves. **mass = A1 (#260) untouched.** See [`research/2026-07-03_engine-verdict-exposure-sweep_result.md`](../../../../research/2026-07-03_engine-verdict-exposure-sweep_result.md).

The L3 EXISTENCE rung extends the suite past the valid-medium L0–L2 layers into the
**bound longitudinal-bulk (A1 scalar) cage** — the mass precursor. The T3.1/T3.2
PRECURSORS establish the medium first (the longitudinal grade EXISTS + propagates, and
its `c_eff(V)` stiffens toward yield = the cage-forming kernel); the T3.3/T3.4 tests then
**POSIT** a saturated A1-scalar core (consistency-class; positing is legitimate — it is
NOT self-formation, which is the gated rung-2) and test what the corpus says a bound
electron-cage must exhibit. **A1 SCALAR ONLY throughout** (`converter_on=False` — the
two-3s guard, [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20:
never read charge/spin/μ off the scalar cage). The companion property×bucket sheet is
[`electron-bound-resonator-coverage.md`](../../vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md)
(the electron = `BoundResonator` instance-1, def-b42e9d).

- **T3.1 → sup-3kq9w7 → clm-crbl60** [CHORD — AVE-distinct existence vs QED]. A
  propagating longitudinal-BULK (A1 dilatation) compression mode IS REAL on the extended
  medium — it is the Heaviside-Gibbs-EXCISED scalar grade (def-9a4f07) that QED
  gauge-DELETES (Gupta-Bleuler leaves 2 transverse on-shell), and AVE KEEPS as a physical
  acoustic branch. Measured (not asserted): the launched compression PROPAGATES (one-way
  pulse-peak speed > 0.3·c₀ on the PML-excluded interior), has a RISING acoustic dispersion
  ω(k) (dω/dk > 0), and runs at the K=2G dilatation speed `c_bulk = √(2G/ρ) = √2·c₀`
  (|c_bulk/c₀ − √2| < 1e-9) — a SECOND, faster channel distinct from the c₀ transverse
  photon. This FLIPS the T1.7 ⊘ absence-finding (the srs vector-TLM carried 2 transverse
  DOF only; the canonical Master-Equation scalar engine now carries the longitudinal grade).
  Lifts the DERIVATION branch of the vacuum bulk-modulus / K=2G claim (clm-crbl60: the mode
  propagates at exactly the `c_bulk = √(K/ρ) = √(2G/ρ)` speed that claim's `K_vac = 2G_vac`
  Cauchy relation + `G_vac = ρ_bulk·c₀²` construction predict; the `√2·c₀` measurement is
  the empirical confirmation of that bulk-modulus → bulk-speed cross-check, α-FREE). The
  "chord" tag is AVE-DISTINCT EXISTENCE (the QED-counterfactual), NOT a forced-number chord.
- **T3.2 → sup-mz4t0p → clm-gz7ryg** [Axiom-4 MANIFESTATION / consistency]. The
  longitudinal-bulk effective speed STIFFENS, `c_eff(V) = c₀·S^(−1/2) → ∞` as A → A_yield
  (S → 0), driven by the canonical Axiom-4 kernel `S(A) = √(1−A²)` read DIRECTLY from the
  engine's authoritative `c_eff_squared` (`master_equation_fdtd.py:148-151`, the
  #278-corrected ½-power form). Measured across the sweep A ∈ {0…0.99}: cold limit
  c_eff/c₀(0)=1 (<1e-12), monotone-rising, matches `(1−A²)^(−1/4)` to <1e-9 (an S^0.25 read
  would FAIL), diverges past the I→II and II→III regime edges toward the wall. This is the
  CAGE PRECURSOR (CP8 generative-precursor): the bond stiffens C_eff=C₀/S→∞ at yield, the
  T3.3 Γ=−1 wall is the END of this stiffening. Tagged Axiom-4 MANIFESTATION / consistency —
  NOT a chord (no forced dimensionless number falls out; the stiffening is the axiom's
  constitutive law expressed in the longitudinal sector). Lifts the DERIVATION branch of the
  single-kernel A-034 claim (clm-gz7ryg: `S(A)=√(1−A²)` governs every reorganization at
  every scale; T3.2 confirms the SAME kernel manifesting in the longitudinal-bulk sector).
- **T3.3 → sup-1ecv2m → clm-kezk9z, clm-uatcql** [CONSISTENCY / FORM-chord]. On the
  posited cage, Γ_bulk crosses the canonical OP2 engaged-gate −0.25 (Γ_min(0.95)=−0.283,
  Γ_min(0.99)=−0.454), descends monotonically toward −1, and →0 in vacuum. Read via the
  **α-FREE** impedance route `crystal_engine.gamma_bulk()` (Z_eff=√S→0 ⇒ Γ→−1), NOT
  `gamma_em_sq` (the 1−α bake, `cvr_model.py:364`). The literal −1 is UNREACHABLE (the
  S_min-clipped floor, by design). Lifts the DERIVATION branch of the Γ=−1 confinement
  wall (clm-kezk9z, sol 0.90) and the electron's Γ=−1 TIR-cavity property (clm-uatcql).
- **T3.4a → sup-xgx063 → clm-ka5zdx, clm-unk0bd** [FORM-chord / VALUE-definitional]. A
  DISCRETE gapped breathing eigenmode ω_cutoff≈2.87 (natural units; peak/mean≈456, 23
  zero-crossings) EXISTS on the posited cage. The mass=ground-state-cutoff-energy of the
  bound resonator is the FORM (a chord); m_e the VALUE is NEVER a cage output
  (definitional, `constants.py` symbol `M_E` "Input 1"; `electron-identification.md:50` "CALIBRATION
  ANCHOR, not derivation"). Lifts the DERIVATION branch of the mass-closure standing-wave
  theorem (clm-ka5zdx) and the electron body-topology bound-loop (clm-unk0bd).
- **T3.4b → sup-wuy333 → clm-rtdmsn** [ECHO-CORROBORATION — NOT a Q-value chord]. The cold,
  α-FREE Q from ring-down is **Q_ringdown≈30.8 (Q_linewidth≈3.8), NOT 137**. Two α-bake
  guards enforced (no Q_TANK = `cvr_model.py:72`, no M.ELECTRON, no gamma_em_sq). Because α
  was never baked, the α-free cold cage does NOT reproduce 137 ⇒ the corpus Q=1/α
  (`cvr_model.py:72`) is an **instance-baked ECHO**, not a cage-emergent chord. This is a
  clean chord-vs-echo NEGATIVE that **CORROBORATES the already-canonical value-scoped-echo
  framing** of clm-rtdmsn ([`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md):19,
  the "echo at the value level" verdict; :21 the instrument-echo-trap). The support is
  wired to record the empirical corroboration; it does **NOT** strengthen any "Q=137 is
  forced/derived" reading (there is none — clm-rtdmsn already scopes Q=1/α as a
  calibration identity that "predicts no independent value").
- **T3.4c → sup-x7h9yh → clm-ka5zdx, clm-uatcql** [FORM — NOT topological-winding
  protection]. With zero drive, the bare posited cage holds a non-radiating standing mode
  (late/mid≈1.31, late_min≈0.34·amp0). This is PERSISTENCE of the standing reactive
  structure (ave-conserved-vs-pumped: measured zero-drive, not pumped), strengthening the
  saturation-locked standing-wave stability (clm-ka5zdx) and the electron bound-resonator
  identification (clm-uatcql). It is NOT the topological-winding protection (that is the
  winding sector, bucket B, NOT cage-testable).

**Measurement-design finding (Rule 10, surfaced at integrator time):** the posited
Gaussian core does NOT ring under a monopole/DC kick — it slowly RELAXES (the dominant FFT
component is bin 1, whose ω scales as 1/n_steps = a run-length artifact, NOT a physical
mode). The discrete bound mode is excited only by a radial-SHELL **breathing** kick (∂_t V
on the wall, no monopole DC). Recorded in T3.4a's docstring; it does not change any bin.

**HONEST SCOPE.** The L3 rung POSITS the cage; it does NOT show the cage SELF-FORMING
(that is the gated rung-2 / genesis decider, L5 in the §9 matrix). The FORM-chords here
are "GIVEN a saturated core, the corpus's reflective wall + gapped bound mode + persistence
manifest, α-free" — CONSISTENCY-class, not emergence. The one genuine chord-vs-echo
question (cold-Q) returned a clean ECHO. No dimensionful electron VALUE (m_e, e, α, Q=137)
is a cage output. 🔴 *(2026-06-24 SHARPER QUALIFIER: the Stage-2 native-cage make-or-break adds that the **dynamical bulk self-trap is FALSIFIED natively** (energy-certified MODE-III DISPERSE) — so the posited cage is not only un-self-formed, its bulk self-focusing-well realization is a Cartesian artifact. The surviving route is the Γ=−1 BOUNDARY condition + topology; mass = A1 (#260) untouched.)*

> **Figures:** each test emits a `<test-id>_debug.png` at
> `research/figures/engine_acceptance/` (KF_VIZ=1; regen via
> `python -m tests.engine_acceptance.regen`), mirrored into
> `manuscript/vol_9_vacuum_datasheet/figures/engine_acceptance/` for the Vol 9 build.
> Figures carry no spine id (§1.5: no `fig-` prefix); each inherits its test's `sup-`
> provenance through this leaf.

---
