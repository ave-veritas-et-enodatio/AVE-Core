# PRE-REG (FROZEN) — QED-TRACE Many-Body Screening-Sum Gate

**Date:** 2026-07-14 · **Branch:** `analysis/qed-trace-screening-sum`
**Worktree base:** `origin/main` @ `240d59d8` (the beta-gate merge PR #685).
**Program:** QED-TRACE (read QED's math as compressed medium data; ontology fence intact).
**Predecessor:** the beta-function gate (`research/2026-07-14_qed-trace-beta-gate_RESULT.md`) —
`WRONG-FORM` for the **two-body pointwise pairwise dress**. This gate probes the residual route that
result left EXPLICITLY OPEN (§7 scope boundary, verbatim):

> "The gate computed the two-body saturation-dressed force (form-factor class); it never computed the
> lattice's many-body screening SUM between the two probes. That many-body scale-integrated
> medium-response route is UNPROBED, NOT CLOSED."

> **FREEZE DISCIPLINE.** This document is pushed as its own commit BEFORE the driver runs. The
> adjudication criteria (§4 bins, §6 gates, §3 register definitions, §5 solver + convergence criterion)
> are frozen here. Post-hoc bin re-definition or criterion-dropping to convert ❌→✅ is a Rule-11
> violation. Any change after the result run lands as a DATED AMENDMENT below the frozen body (frozen
> bytes untouched; git is the trail). The plant formulas (§6) were checked for self-consistency BEFORE
> freezing (the beta gate's frozen G-plant-log formula was sign-self-contradictory; the beta gate's
> frozen G-null was design-defective — both are corrected here, not repeated).

---

## 1. MISSION + a-priori expectation

**The one question:** does the **self-consistent many-body screening SUM** — the intervening lattice
cells between two seeded windings, each polarizing in the TOTAL field (probe field PLUS every other
cell's induced polarization: the Clausius-Mossotti / self-consistent-screening ladder), kernel-ON —
produce **NON-POWER-LAW (logarithmic) scale dependence** in the **TRANSFER coupling** between the two
probes, where the beta gate's **pairwise** dress gave a pure power law?

**Why this is the residual route, not a repeat.** The beta gate probed *pointwise algebraic
compositions* of the Op14 kernel (the pairwise dress, the `F/F_Coulomb` two-body force, the A44
skin-suppression) — each is a finite algebraic function of `A² = (d_sat/r)²`, and an analytic-in-`r²`
function **cannot be a `ln`** by finite manipulation. But QED's `ln(q)` does NOT come from a pointwise
object: it comes from **scale-integration of an algebraic integrand over a self-consistent screening
hierarchy** (the vacuum-polarization insertion resummed across scales). The classical analog of THAT
operation is a **polarizable medium whose cells screen self-consistently**: the many-body dipole-dipole
coupling carries a `1/r³` kernel whose spherical-shell integral `∫ 4πr² dr · r⁻³ = 4π ∫ dr/r` is
**logarithmic** — IF the self-consistently-induced dipole DENSITY between the probes is scale-invariant
(`∝ 1/r³`) across the perturbative range. Whether the Op14 saturation response produces that
scale-invariant density is the **genuinely unprobed empirical question this gate answers**. The pairwise
dress structurally cannot carry this (it has no inter-cell coupling); the many-body sum can.

**A-priori expectation (stated honestly, per the consensus-bias rail): GENUINELY UNKNOWN.** This is the
one QED-TRACE route where the outcome is not pre-figured by a prior corpus computation. Two honest poles:

- A **LOG-EMERGES (QED sign)** here would be the **QED-TRACE program's chord** — the classical
  self-consistent screening ladder reproducing QED's running FORM, the one non-dictionary content the
  program could earn. It would upgrade `q-g20f` from scoped-import to a computed FORM-match.
- A clean **WRONG-FORM (power law, no log)** **completes the category closure**: it would show the
  many-body scale-integration ALSO fails to emit `ln`, closing the last open route the beta gate named,
  and converting "AVE reproduces QED running" to a fully-scoped import with the mechanism named (the
  self-consistent saturation response does not produce a scale-invariant dipole density → the shell
  integral is not logarithmic). This is a corpus-improving negative, not a shame result (Rule 11).

**No pre-judgement is baked into the design.** The kernel-OFF null (α0=0 ⇒ no dipoles ⇒ `α_eff≡1`), the
Born-vs-converged self-consistency knife, and the remove-intermediate-cells many-body knife are all wired
so a log CAN emerge if the physics supports it (this is NOT a disabled-DOF null: the inter-cell dipole
coupling that could carry the log is ON by construction and its removal demonstrably changes the result —
verified as a machine gate).

**Sector header (as-designed).** MODE: static/quasi-static two-body TRANSFER coupling between two seeded
Cosserat windings, mediated by a self-consistent polarizable medium (the many-body screening SUM).
REGIME: cold, **KERNEL ON** (Op14/Ax4 saturation sets each cell's polarizability) — with a **kernel-OFF
control** (α0=0, no polarizable response) as the null. PHASE-STATE: **sub-yield perturbative** — the
intervening bridge medium is weakly strained (`A ≪ 1` between the probes), the fair QED-running analog
(a small departure over ≥2 decades of SEPARATION); the near-saturated small-separation regime
(`R ≲ 10 d_sat`, bridge `A→1`) is the non-perturbative Pauli-wall analog and is EXCLUDED, exactly as the
beta gate excluded `r/d_sat ∈ [1.02,3]`. SECTOR: the graded-Coulomb screening cloud of induced cell
dipoles = the vacuum-polarization cloud; the two-probe transfer force through it = the
vacuum-polarization-corrected Coulomb law. Platform firewall: the canonical Op14 capacitive/saturation
grade (`universal_saturation`, `universal_pairwise_energy`, clm-gdd70j) sets the per-cell polarizability;
a NEW self-consistent dipole-lattice solver (below) performs the many-body sum. No new ENGINE (no FDTD /
no VacuumEngine3D) — a static electrostatic self-consistent-field solve over Op14-graded polarizable
cells.

---

## 2. SUBSTRATE-NATIVE WALK (pre-build; Posture-B reference-walk)

- **K4 / lattice checkpoint:** the intervening cells ARE lattice cells; the screening SUM is a sum over
  real-space lattice sites between the two probes. Real-space, on the lattice. ✓
- **Cosserat checkpoint:** the two probes are the seeded (2,q) micro-rotation windings (the charge
  carrier, `clm-ze4clw`); the graded-Coulomb dress around each = the polarizable screening cloud. Each
  intervening cell's polarization = its capacitive/impedance grade under local strain. ✓
- **Op14 checkpoint (load-bearing):** the per-cell polarizability is DERIVED from the Op14/Ax4
  saturation grade, NOT plugged in from a QED/Lagrangian susceptibility. A cell at local strain `A`
  carries the capacitive grade `C_eff/C₀ = 1/√(1−A²)` (the SAME reactive grade
  `simulate_running_alpha.py` and the beta gate's reactive register used, `universal_saturation`
  A=Ax4), so its excess polarizability (susceptibility) is `χ(A) = 1/√(1−A²) − 1` (→ `A²/2` in weak
  field: far cells weakly polarizable; → ∞ as `A→1`: cells saturate = maximally polarizable). This is
  the substrate-native polarizability; the QED susceptibility is NOT imported. ✓
- **phase-space-vs-real-space (A46):** the screening SUM is a real-space sum over cell positions; the
  transfer coupling `F(R)/F_bare(R)` is a real-space through-coupling; the claim (does self-consistent
  screening produce `ln(R)`) is a real-space claim. Coordinates match — A46-clean. ✓
- **SM/QED default-leak check:** no Lagrangian, no gradient-descent, no continuum-Helmholtz, no
  energy-basin. The solver is an electrostatic self-consistent-field (impedance/capacitance) solve — the
  EE-native language. The one imported number is `α_fs` (CODATA), used ONLY as the coefficient TARGET
  (`−α/3π`) and firewalled off the FORM/sign determination (§7 rail). ✓

---

## 3. ★ THE TRANSFER-REGISTER REQUIREMENT (inherited from the beta gate, load-bearing)

The beta gate's headline finding: the SAME kernel reads **opposite signs in the two registers** — the
TRANSFER (through-coupling/force) register and the REACTIVE (stored-energy/impedance) register — so
**sign is set by REGISTER, not physics** unless the QED-faithful register is used. QED's running α is
defined off the **scattering amplitude** = a TRANSFER quantity. Therefore, exactly as frozen in the beta
gate:

**(a) PRIMARY (binned) = the TRANSFER register.**
> `α_eff^transfer(R) ≡ F_z(R) / F_z,bare(R)`, where `F_z(R)` is the axial force on probe-1 including the
> field of ALL self-consistently-induced cell dipoles, and `F_z,bare(R) = −q₁q₂/R²` is the bare
> two-probe Coulomb force. Kernel-OFF (α0=0) ⇒ no dipoles ⇒ `α_eff^transfer ≡ 1` (flat, NO running by
> construction). Running = scale-dependence of `α_eff^transfer(R)` vs separation `R`. Short distance
> (high energy) ↔ small `R`; long distance ↔ large `R`. **QED sign = `α_eff^transfer` GROWS as `R`
> decreases** (coupling stronger at short distance). `α_eff<1` growing at short distance = the
> WRONG-SIGN signature (coupling weakens).

**(b) KEEP-BOTH second column = the REACTIVE register (reported, NOT binned as primary).**
> `α_eff^reactive(R) ≡ W_sat(R) / W_lin(R)`, the ratio of the self-consistent **saturated** stored
> polarization energy `W = ½ Σ_i p_i·E_i` to the same solve run with the **linearized** polarizability
> `χ_lin(A) = A²/2` (the leading un-saturated grade). Far field (`R` large, bridge `A→0`)
> ⇒ `χ→χ_lin` ⇒ ratio → 1; near field the saturation enhancement departs from 1 — the direct analog of
> the beta gate's reactive `Z/Z₀` dress. Reported alongside the transfer column at every scale; its own
> form/sign noted. **The bin is read on the TRANSFER register** (the reactive register's sign is known
> to be register-artifactual from the beta gate; KEEP-BOTH banks it without letting it drive the
> verdict).

**Fit target (frozen, applied identically to both registers):** fit the departure of `α_eff(R)` against
BOTH `M_log: α = c₀ + c₁·ln(R)` and `M_pow: α = 1 + a·(R_ref/R)^p` (`R_ref = R_HI`), select by ΔBIC
(§6). The QED chord requires `M_log` selected AND `c₁` sign matching α-grows-at-short-distance AND (for
the full chord) coefficient → `−α/3π` in `1/α` space. **Reuse the beta-gate fitter verbatim**
(`fit_log_vs_power`, `qed_trace_beta_gate.py`) — it is already proven (beta gate G-plant-log /
G-plant-pow / G-separability) to find a real log, reject a spurious log on a `p=0.3` power law, and
separate the two at ≥2 decades.

---

## 4. THE FIVE FROZEN BINS (same family as the beta gate)

Binned **on the TRANSFER register** (primary); the reactive column reported alongside. `INCONCLUSIVE-RANGE`
(§6) can pre-empt any if the achieved range cannot statistically separate log from small-exponent power.

| Bin | Signature (transfer register) | Consequence (frozen) |
|---|---|---|
| **LOG-EMERGES** | genuine `ln(R)`, QED sign (α GROWS at short distance), coeff → `−α/3π` | **The QED-TRACE program's CHORD.** The many-body self-consistent screening SUM reproduces QED's running FORM classically; `q-g20f` upgrades from scoped-import to computed FORM-match; `clm-bqtasn` strengthen-by closes POSITIVE. **RIGHT-FORM / WRONG-COEFF** sub-case (log, right sign, wrong prefactor) = **FORM-chord / VALUE-echo**, files into the forces-FORMS-imports-VALUES meta-finding. |
| **WRONG-FORM** | power law in `(R_ref/R)`, **no log** | **Category closure COMPLETE.** The last open route (many-body scale-integration) also fails to emit `ln`; the beta gate's §7 boundary is CLOSED; the q-g20f scoped-import re-tag can drop the "unprobed" caveat and read as a full scoped import. Mechanism named: the self-consistent saturation response does not produce a scale-invariant dipole density. Routed to auditor. |
| **WRONG-SIGN** | a genuine `ln(R)` running with α **WEAKENING** at short distance ON THE TRANSFER READING | Fires against the asserted `q-g20f` sign; a real log but the wrong direction. Worse than wrong-form for the sign claim; still a FORM-partial (log emerged). Routed to auditor. |
| **NULL-FLAT** | negligible transfer running (`\|α_eff−1\|` below the null threshold across the window) | The many-body sum adds no scale-dependence beyond the pairwise dress at this α0; gate closes; running stays imported. |
| **INCONCLUSIVE-RANGE** | achieved ≥2-decade range cannot separate log from small-exponent power (§6 separability FAILS) | Gate honestly INCONCLUSIVE on form; report the range limit; no bin claimed. |

**Genuineness precondition on any non-NULL bin (frozen).** A LOG-EMERGES / WRONG-FORM / WRONG-SIGN
verdict is only reported as a **many-body** result if the two genuineness knives (§6: Born-vs-converged
AND remove-intermediate-cells) confirm the result is genuinely carried by the self-consistent inter-cell
sum. If Born ≡ converged (self-consistency adds nothing) AND/OR removing the intervening cells does not
change the result, the verdict is re-tagged **RELABELED-PAIRWISE** (the sum is a disabled/spectator
degree of freedom and the result is the beta gate's pairwise dress under a new name — an instrument
finding, not new physics). This is the structural-null stencil lens: a null (or a positive) on a
coupling that turns out to be a spectator validates a disabled flag, not physics.

**Scope of a null verdict (frozen concession).** A null/WRONG-FORM is scoped to "**the classical +
kernel-ON lattice, self-consistent polarizable-cell screening between seeded windings, perturbative
window**." It does not re-open or re-close the sourced-charge no-go (`clm-nogo4l`), which stays closed by
its own argument. It does close the beta gate's named "many-body scale-integrated route."

---

## 5. INSTRUMENT — the self-consistent dipole-lattice screening solver (NEW; no new engine)

Driver: `src/scripts/vol_2_subatomic/qed_trace_screening_sum_gate.py` (new; reuses the beta gate's
`fit_log_vs_power`, register discipline, 5-bin classifier, and the Op14 capacitive grade — a static
electrostatic self-consistent-field solve, NOT a new FDTD/VacuumEngine3D engine).

**Geometry (frozen).** Two like probes `q₁=q₂=+1` at `±R/2 ẑ` (like-winding pair, matching the beta
gate's Arm A). Transfer force is the axial (`z`) component.

**Cell mesh (frozen).** Two per-probe clouds; around each probe center, cells at Fibonacci-sphere
directions (`n_ang=24`) on log-radial shells (`n_r=16` shells, `ρ ∈ [1.05·d_sat, r_max_fac·R]`,
`r_max_fac=1.2`; shell volume `4πρ²Δρ / n_ang` per cell). Cells within `d_sat` of EITHER probe are
excluded (the Pauli-wall region carries no perturbative polarizable medium). Near-coincident cells (from
the two overlapping clouds in the bridge) are removed by greedy dedup at `min_sep = 0.25·(v_cell)^{1/3}`
(near-probe cells kept first). The dipole kernel is softened at the finite cell scale
`r_soft = 0.3·(v_cell)^{1/3}` (physical lattice discreteness; regularizes near-coincidence).

**Per-cell polarizability (frozen, Op14-derived).** `α_i = α0 · χ(A_i) · v_cell`, with
`χ(A)=1/√(1−A²)−1`, `A_i = |E_total,i| / E_yield`, `E_yield = K/d_sat²`. Overall scale `α0` (the medium's
polarizability density) is FIREWALLED off the FORM determination (like the beta gate firewalled α):
**primary `α0 = 0.03`** (perturbative, SCF-convergent); the FORM verdict is confirmed α0-independent by
a robustness sweep `α0 ∈ {0.01, 0.03, 0.1, 0.2}` (self-adversarial, §6).

**Self-consistent solve (frozen convergence criterion).** Two-layer self-consistency:
1. **Inner (dipole-dipole, EXACT):** for fixed `{α_i}`, the induced dipoles satisfy the linear system
   `(I − diag(α)·M) p = diag(α)·E_probe`, where `M_ij` is the (softened) dipole field tensor
   `(3 n̂n̂ − I)/r³` (`i≠j`, diagonal zero). Solved by direct dense `np.linalg.solve` — this is the
   many-body sum (each cell polarizes in the field of every other cell), resummed exactly.
2. **Outer (saturation SCF):** `α_i` depends on the total-field strain `A_i = |E_total,i|/E_yield`,
   updated after each inner solve under linear under-relaxation (`damp = 0.4`). **Converged when the
   relative α-change `‖α_new−α_old‖/‖α_new‖ < 1e-8`** (frozen); `maxiter = 400`. A scale point that
   fails to converge is FLAGGED and excluded from the fit with disclosure (never silently dropped).

**Scale sweep (frozen).** `R/d_sat ∈ [30, 3000]` (**2.0 decades**, perturbative), `N_scale = 16`,
geomspace. (Mirrors the beta gate's perturbative `[3,3000]` choice on the SEPARATION axis; small-`R`
near-saturated bridge excluded as the non-perturbative Pauli-wall analog.)

**Legs (all in the frozen driver):**
1. **PRIMARY — transfer + reactive sweep** across the 16 scales; fit both registers `M_log` vs `M_pow`;
   report the `α_eff(R)` table (both registers) and the bin.
2. **GENUINENESS knife A — Born vs converged.** At every scale, ALSO compute the Born (first-order)
   result: dipoles respond to the PROBE field only (`p = diag(α)·E_probe`, inter-cell `M` OFF in the
   `p`-equation). Compare the Born transfer curve's FORM+coefficient to the converged one. Report
   `self_consistency_changes_form` and the coefficient ratio.
3. **GENUINENESS knife B — remove-intermediate-cells.** At two reference scales, re-run with the
   "bridge" cells (within a cylinder of radius `R/2` about the axis AND `|z| < R/2`, i.e. the region
   between the probes) REMOVED. Report the fractional change in `α_eff^transfer`. A genuine many-body
   sum through the intervening medium MUST change; no change ⇒ RELABELED-PAIRWISE.
4. **KERNEL-OFF null control.** `α0 = 0` ⇒ no dipoles ⇒ `α_eff^transfer ≡ 1` at all scales. AMENDED
   amplitude criterion (§6).

---

## 6. MACHINE GATES (corrected from the beta gate's two frozen defects)

| Gate | Test | Fires when |
|---|---|---|
| **G-null (kernel-OFF)** — AMENDED amplitude axis (the beta gate's frozen fit-based G-null was DESIGN-DEFECTIVE: model-selection on ~1e-10 numerical noise + an unimplementable `\|p\|>1e-6` disjunct; NOT repeated) | with `α0=0`, `max\|α_eff^transfer−1\|` over the window is flat | `max\|α_eff−1\| ≥ 1e-6` ⇒ instrument artifact (the null must be flat to machine precision, since α0=0 kills every dipole) |
| **G-plant-log** — SIGN-CORRECT plant (the beta gate's frozen `+(1/3π)ln` formula was sign-self-contradictory; the CORRECT QED-sign plant is used) | inject `α_synth = 1 + (α_fs/3π)·ln(R_HI/R)` (α GROWS at small R = QED sign) → DETECTED as log, right sign | fitter fails to select `M_log` or gets the sign wrong ⇒ fitter blind |
| **G-plant-pow** | inject `α_synth = 1 + 0.25·(R_HI/R)^{0.3}` (small exponent = hardest case) → DETECTED as power, NOT mis-fit as log | fitter selects `M_log` on a known power law ⇒ over-privileges the log (consensus-bias failure) |
| **G-separability** | at the 2-decade window, a planted true-log and a planted `p=0.3` power are BOTH decisively classified (`\|ΔBIC\|>10`) | if 2 decades cannot separate ⇒ `INCONCLUSIVE-RANGE` exists and fires honestly |
| **G-genuineness-A (Born≠converged)** | the inter-cell sum must be live: Born and converged must not be identical to machine precision | `\|α_conv−α_Born\|/\|α_conv−1\| < 1e-6` at all scales ⇒ self-consistency is a spectator ⇒ RELABELED-PAIRWISE re-tag |
| **G-genuineness-B (bridge-removal)** | removing the intervening cells must change the transfer coupling | fractional change `< 1e-6` ⇒ the intervening medium is a spectator ⇒ RELABELED-PAIRWISE re-tag |

**Model-selection statistic (frozen, verbatim from the beta gate):** ΔBIC = BIC(M_pow) − BIC(M_log),
both k=2 params, same n, same response space ⇒ ΔBIC = n·ln(SSE_pow/SSE_log). ΔBIC > +10 ⇒ decisive
`M_log`; ΔBIC < −10 ⇒ decisive `M_pow`; `|ΔBIC| ≤ 10` ⇒ INCONCLUSIVE. `P_GRID = linspace(0.3, 8.0, 155)`.

**Plant-formula self-consistency check (done BEFORE freeze).** G-plant-log plants in α-space with coeff
`+α/3π` and `ln(R_HI/R)` ⇒ α > 1 at small R = α GROWS at short distance = the QED sign, and the fitter's
QED-sign witness (`c₁ < 0` in `α = c₀ + c₁ ln R`) reads True — internally consistent (the beta gate's
frozen `1/α`-space `+1/3π` formula was NOT; not repeated). G-null uses the amplitude criterion only (the
beta gate's frozen fit-based criterion is design-defective; not repeated). Both defects the beta gate
banked as AMENDMENTS A2.1/A2.3 are pre-corrected here.

---

## 7. RAILS (frozen)

- **Consensus-bias (binding):** I carry QED priors by training volume. The fit must not privilege the
  log (G-plant-pow enforces; both models get k=2). A clean lattice negative is an ontology difference,
  not a demerit; a log, if found, must survive BOTH genuineness knives before it is called the chord.
- **No α seeding on the FORM path.** `α_fs` (CODATA) is a legitimate operating INPUT (the coefficient
  target `−α/3π`, the plant self-test). It is firewalled off the FORM/sign determination and off the
  medium polarizability scale `α0` (which is a free native parameter, swept for robustness). The
  log-vs-power verdict is read from the solver geometry, not from any imported α.
- **Structural-null stencil lens (binding).** The inter-cell dipole coupling is the load-bearing DOF; a
  verdict is only "many-body" if the genuineness knives confirm the coupling is live (not a spectator).
  A disabled-coupling null would validate a bug, not physics — the knives prevent that.
- **Consistency-vs-emergence tag:** the per-cell Op14 saturation grade is **CONSISTENCY / ECHO**
  (charge-agnostic; same kernel as the beta gate). The gate's earnable content is the FORM/SIGN category
  answer of the many-body SUM, not a value. A LOG here would be a FORM-emergence claim (the running FORM
  emerging from the self-consistent sum) with the coefficient still an echo/value-import — headline the
  FORM, not the value. **Pure physics** — no external context in any tracked file.

---

## Discipline skills applied (Posture-B reference-walk, pre-build)

- **substrate-native-check:** §2 walk — K4/Cosserat/Op14/A46 checkpoints cleared; the per-cell
  polarizability is DERIVED from the Op14 capacitive grade, not an imported QED susceptibility; the
  solver is an EE-native electrostatic SCF, no Lagrangian/gradient-descent/Helmholtz/energy-basin leak.
- **pre-test-physics-check:** the plumber-physical question (does a self-consistent polarizable medium's
  `1/r³` shell integral emit a log where the pairwise dress could not?) is the §1 mission, surfaced
  before design.
- **phase-space-coordinate-check (A46):** real-space sum vs real-space claim — coordinates match (§2).
- **consistency-vs-emergence:** tagged CONSISTENCY/ECHO for the value; FORM-emergence is the only chord
  content on offer (§7).
- **Rule-10 empirical-driver discipline:** the solver mechanics (SCF convergence across the window,
  kernel-OFF null flatness, fitter plant-detection) were live-fire-validated on a throwaway prototype
  BEFORE freezing THESE criteria — WITHOUT computing the sealed real `α_eff(R)` verdict (convergence
  behavior informed the frozen `damp=0.4`, `tol=1e-8`, and the perturbative window choice).

---

## Receipts (grep/read-verified this session at base `240d59d8`)

| Claim | Receipt |
|---|---|
| Beta gate §7 scope boundary: many-body screening SUM UNPROBED NOT CLOSED | `research/2026-07-14_qed-trace-beta-gate_RESULT.md:214-217` |
| Beta gate corrected mechanism: log emerges via scale-integration over a self-consistent screening hierarchy | `research/2026-07-14_qed-trace-beta-gate_RESULT.md:210-213` |
| Beta gate AMENDMENT A2: fixed G-null (amplitude, not model-selection-on-noise) + fixed G-plant-log (α/3π, not sign-contradictory 1/3π) | `research/2026-07-14_qed-trace-beta-gate_prereg_FROZEN.md:346-402` |
| Op14 capacitive/saturation grade `C_eff/C₀=1/√(1−A²)`, `S(A)=√(1−A²)` (Ax4) | `src/ave/core/universal_operators.py:75-115,140-216` (clm-gdd70j) |
| Beta-gate fitter + register discipline + 5-bin classifier reused | `src/scripts/vol_2_subatomic/qed_trace_beta_gate.py:118-157,365-408` |
| Winding = charge carrier, integer-quantized | `clm-ze4clw`; `test_winding_charge_closure.py:19,29,34` |
| Sourced-charge no-go stays closed by its own argument (pairs/topology OPEN) | `manuscript/ave-kb/common/the-sourced-charge-no-go-cascade.md` (clm-nogo4l) |

---

*Frozen 2026-07-14. Result + PR follow in subsequent commits. Amendments (if any) appended below this
line with date + rationale; frozen body bytes above are untouched.*

---

## AMENDMENT A1 (2026-07-14, post-run — three verdict-preserving integrator-time refinements)

Three shipped-code-vs-frozen deviations, all surfaced at integrator time (Rule 10 — bugs manifest only
when the solver runs), all **verdict-preserving** (the `WRONG-FORM` / decisive-power verdict holds — and
SHARPENS — under each; none biases the fit toward or away from the log), all reconciled here (frozen body
above untouched). The frozen ADJUDICATION CRITERIA (§4 bins, §6 gates + ΔBIC statistic, the two
genuineness knives, the transfer-register primary) are UNCHANGED.

**A1.1 — Interaction-force self-subtraction (the frozen transfer definition was ill-posed).** §3(a) froze
`α_eff^transfer ≡ F_z(R)/F_z,bare(R)` with `F_z(R)` = "the axial force on probe-1 including the field of
ALL induced dipoles", intent "kernel-OFF ⇒ α_eff ≡ 1 (flat)". The RAW `F_z` is **dominated by an
unphysical self-force**: probe-1's own (nominally isotropic) screening cloud does not perfectly
angularly cancel, leaving an `R`-independent residual that, divided by the tiny bare force `1/R²`, BLOWS
UP far-field (`α_eff ≈ −1.3e4` at `R=3000`). The shipped driver isolates the genuine interaction force
by SUBTRACTING probe-1's isolated self-cloud force: `F_transfer = F_dip(both probes) − F_dip(probe-1
alone, q=(1,0))`, which delivers the frozen intent exactly (`→1` far-field, kernel-OFF `≡1` flat to
machine ε). This is the direct analog of the beta gate's own A1 repair (`F·r²/K → F/F_Coulomb` to deliver
"bare → 1"). The genuineness knives VALIDATE the observable is physical, not a subtraction artifact:
bridge-removal changes it 51% (medium-mediated) and Born-vs-converged changes it 9.4% (self-consistency
active).

**A1.2 — Antipodal-symmetric angular sampling.** §5 froze "Fibonacci-sphere directions (n_ang=24)"; the
shipped `_fib_sphere` uses **antipodal-symmetric** Fibonacci (12 points + their 12 antipodes). Antipodal
symmetry makes each probe's ISOTROPIC self-cloud exert exactly zero net axial force (each radial dipole's
contribution cancelled by its antipode's), so the interaction-force extraction (A1.1) is not contaminated
by an angular-discretization self-force. Verdict-neutral (does not bias log-vs-power); with raw
non-antipodal Fibonacci the verdict already leaned power/grows-short, antipodal sharpens it.

**A1.3 — Orientation-averaging (`N_ORIENT=8`, seeded).** Not in the frozen spec; added to suppress the
DETERMINISTIC angular-discretization noise (a fixed ~0.005 ripple + a reproducible artifact dip at
`R≈416` that appears identically at all tolerances — confirmed NOT iterative: tightening SCF `tol` from
`1e-8`→`1e-12` changes the curve by 0). Each scale point is averaged over 8 random SO(3) rotations of the
mesh pattern (reproducible seed `20260714`). This is isotropic noise reduction — it cannot bias
log-vs-power. Single-orientation the transfer already selected/leaned `M_pow` grows-short (`dBIC≈−6.7`
inconclusive at 8 pts → decisive `M_pow dBIC=−24.7` averaged at 16 pts); the averaging sharpens
inconclusive→decisive POWER, never toward log.

**A1.4 — Added robustness legs (disclosed, not gating).** A 3-decade window-robustness leg (`R/d_sat ∈
[30, 30000]`, decisive `M_pow dBIC=−21.0`) and the `α0` form-robustness sweep (§5, frozen) confirm the
verdict is window- and `α0`-independent (never `M_log` at any `α0 ∈ {0.01,0.03,0.1,0.2}`).

**Net:** every deviation makes the observable well-posed / cleaner without touching the frozen bins,
gates, or genuineness criteria. The verdict is `WRONG-FORM`, decisively (`dBIC=−24.7` at 2 decades,
`−21.0` at 3 decades), genuinely many-body (both knives pass).
