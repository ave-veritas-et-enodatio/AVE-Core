# Cavity-Census Stage-1 — imposed-cavity mode census — **DRAFT prereg**

> **DRAFT for Grant review — freeze-by-push occurs at execution; nothing below is
> frozen until that commit.** This document is the execution-ready draft of the
> Stage-1 imposed-cavity mode-census prereg. It is written to be frozen *as-is by
> push* once Grant walks it, but it carries no enforcement weight while it is a
> DRAFT: the bins, thresholds, and battery matrix are proposals, not commitments.
> The freeze commit (a separate `freeze` push) precedes the first driver commit in
> git history (ave-prereg v1.7 Step 3.11, model
> `research/2026-07-13_genesis-npersist-n14-battery_prereg_FROZEN.md`). **Open
> freeze-time decisions are collected in §7 — those are the questions the walk must
> close before the freeze push.**

**Provenance.** Post the **Wall-A ruling (Grant 2026-07-14)** which unfroze this arc.
The Wall-A ruling is being propagated to the KB in a **sibling lane**
(`docs/wall-a-ruling-propagation`); at this DRAFT's HEAD (`c12f2bdb`) that branch has
**not yet committed** — its content is cited here **as in-flight**, not as tracked
corpus. The load-bearing pieces of the ruling carried into this draft: **(1)** the
Γ=−1 envelope's operative register is the **amplitude rail** (the S(A)→0 level-set),
not a fixed geometry; **(2)** a **ropelength floor** exists as the geometric-minimum
wall location; **(3)** the **excited-states-lift-off rider** — the settled wall should
sit at the floor at ground state and lift off it at larger cavity scale; **(4)** the
**deficit-knee re-tag**. Any reference to a Wall-A tracked leaf below is a placeholder
to be re-verified against the sibling lane's landed commit at freeze time (§7).

**Grounding cards (read + carried).**
- Census walk card — instrument inventory, battery constraints, D3-movement map, six
  freeze candidates, sampling arithmetic (grounding synthesis 2026-07-13).
- Conflation map — the two-walls register census; the **config question** (geometric
  mask vs native S(A) gate); the `coupled_eigensolve` `D=1/S(A)` amplitude-native fact
  (envelope-register audit synthesis 2026-07-13).

---

## Sector header (mandatory)

- **SECTOR** — the census wall terminates the **A1 dilatation-mass channel** ($Z_{\text{bulk}}\to0$
  short, the impedance-$\Gamma=-1$ of the confinement surface,
  `vol9/ch3-pin-port-configuration/device-circuit-models.md:161`). The **(2,3) winding it
  is being asked about is a T2 / Cosserat micro-rotation charge/helicity DOF**
  (`coupled_cage_winding.py:43-52`). **A1 ⊥ T2**: the census imposes an A1-sector wall and
  asks whether a T2-sector winding *emerges as the closure class of that wall's reflection
  map*. The imposed wall is **NOT** the $\Gamma_{\text{spinor}}=-1$ $2\pi\to4\pi$ stability
  wall — do-not-re-collide (`device-circuit-models.md:161`).
- **MODE** — Stage 1 imposes a **static** Γ=−1 boundary and reads **existence-given-boundary
  ONLY**. Whether the wall is itself mode-sourced (self-consistency,
  `electron-identification.md:13`) is **Stage 2** (rides the $T_{ij}$ register; task #45).
  A Stage-1 pass is **not** the self-consistent electron.
- **REGIME** — **KEEP-BOTH**: cold-linear (Hermitian eigensolve, primary) and
  driven-toward-saturation (time-domain ping, secondary). The regime flag is **frozen per
  bin** before running — a linear null in a regime where the closure cannot exist is
  **ARTIFACT-eligible, not a negative** (Plumber Q3).
- **PHASE-STATE** — the wall is imposed on the **cold medium** (cold-linear leg) or driven
  toward the self-stiffened flow (driven leg). The interior excitation is a **broadband
  kick / eigenmode extraction**, never a seeded finished mode (CP8 fence, §5).
- **Instrument** — extend the **α-clean Hermitian eigensolver** `coupled_eigensolve.py` with
  an **imposed boundary**; sphere leg cross-checked via `radial_eigenvalue.py` (ABCD). Reads
  are **dimensionless-only** (winding integers, mode-frequency ratios, floor-coincidence
  booleans). No α on any verdict path.
- **consistency-vs-emergence** — a census that returns **(2,3) as the ground-state closure
  class α-free** would be **converting the (2,3) SELECTION from IMPORT toward DERIVATION**
  (`electron-identification.md:50,77,101`) — an **emergence-class** claim that gets its **own**
  adjudication, **not** silently folded into a Stage-1 pass. Every other read (existence,
  spectrum fingerprint, geometry-invariance) is **consistency-class**.

---

## §1 — MISSION + registered framing

**Mission.** Stage 1 of the **imposed-cavity mode census** (task #49). Impose a Γ=−1 TIR
closed surface of electron scale as a **boundary-condition object**, excite the interior,
and **census the interior modes in phase-space coordinates**. Read **existence-given-boundary**:
which winding class, if any, is the ground-state closure of the cavity's reflection map.

**Registered framing (Grant 2026-07-13, docket row D3).** This arc is the **D3 COEXIST
stress-test**, **NOT a re-opening of a closed fork.** D3 was **RULED COEXIST-with-justification
2026-07-09** (`_orchestration/2026-07-09_electron-def-canon-authoring.md:11,21`) and canonized at
four leaves (`electron-identification.md:57-62`; `substrate-perspective-electron.md:93-103,135-145`;
`the-abandoned-interior.md:84-97`; `hollow-vortex-binding.md:28-37`). The census **stress-tests the
ruling's two legs with new evidence** — it does not re-litigate the ruling. The precursor-vs-end-state
sub-fork (`clm-uatcql`, `vol2/claim-quality.md:1159`) stays **explicitly OPEN — not silently resolved.**

**The suspicion under test.** The electron's **(2,3) phase-winding** emerges as the
**ground-state closure class** of the cavity's reflection map — i.e. the winding is set by the
*boundary alone*, genuinely boundary data, with no interior structure storing the selection.

**Scope carve (no formation-route re-opening — verbatim-cited).** The interior-field genesis
negatives "**rule out the interior-field route, NOT the electron's existence**"; the
substrate-correct boundary-observable test "**was never run**"
(`manuscript/ave-kb/common/genesis-chord-falsification-ledger.md:26`). **The census IS that
never-run test** (existence-given-boundary via boundary observables), disjoint from the N1
interior-field negative. Localization premise citable as settled: **boundary/topological**, bulk
self-trap ruled out (`genesis-chord-falsification-ledger.md:86`); **mass = A1 (#260) is untouched.**

## §2 — INSTRUMENT

**Ruled reuse target (walk card).** Extend `src/ave/solvers/coupled_eigensolve.py` — the
**α-clean conservative Hermitian eigensolve** of the native K4 stiffness (real eigenvalues =
the lossless reactive cage; α-clean import-guard triad at `:85-89`; docstring `:9-13,:27,:34-36`).
Its confinement is currently **emergent-periodic** (the S(A)-front, `D=1/S(A)`); the arc's
extension = give it an **imposed boundary**. Lane-1 ruling: **extend this, do not build fresh.**

**Platform-firewall routing (walk card F8; SKILL.md ave-loop-gap-harness-discipline:37-44).** This
is a **stiffening-branch** object. The build is **in-branch tooling** — extend `coupled_eigensolve`
with an imposed mask; sphere leg via `radial_eigenvalue.py` ABCD radial impedance step. **No fourth
engine.** A standalone imposed-BC cavity solver *would* be a fourth firewalled object-class needing
Grant sign-off (`SKILL.md:44`); the in-branch extension route avoids that gate. **(Freeze-time
confirm: §7.)**

### The config question — RESOLVED for this draft: **KEEP-BOTH**

The conflation map surfaced exactly one instrument-config question that must be resolved before
freeze: **is the imposed wall (a) an amplitude clamp, or (b) a geometric Dirichlet mask?** This
draft resolves it as **design for both** — a KEEP-BOTH instrument axis, because running both **is
itself the location-derivation test** the Wall-A ruling opened.

| BC mode | What it is | Build status | Wall-A role |
|---|---|---|---|
| **(a) amplitude-clamp** | native **S(A)-gate** — the solver's existing `D = 1/S(A)` path (`coupled_eigensolve.py:28,:105`); the wall **location is field-decided**, settling wherever the amplitude clips to yield | **already native** to the eigensolver (the conflation map's R13: `D=1/S(A)` is native) | the **mechanism-faithful** choice — the operative Γ=−1 register IS the amplitude rail (Wall-A ruling in-flight) |
| **(b) geometric-mask** | an **imposed geometric Dirichlet/clamp mask** at a *fixed* radius — the wall location is **posited** at the ropelength floor | **genuinely new capability** (walk card: no imposed fixed-geometry surface exists anywhere in `src/ave`) | the **floor-geometry** choice — pins the wall at the ropelength minimum |

**Why KEEP-BOTH and not pick one.** The amplitude-clamp lets the medium decide where the wall
sits; the geometric mask pins it at the geometric floor. **Running both, and comparing where the
amplitude-clamped wall settles against where the geometric mask puts it, IS the FLOOR TEST**
(bin iii, §4): does the field-decided wall settle **at** the ropelength floor at ground state
(the location-derivation debt the Wall-A ruling names), and **lift off** the floor at larger R
(the excited-states-lift-off rider)? A single-BC census cannot ask this; the KEEP-BOTH pair can.

**Honest scope of the new content (conflation map).** Because the amplitude-clamp (a) is *already*
the solver's native behavior, the rail hypothesis "the wall is an amplitude rail" **changes nothing
in the instrument** — its distinct content shrinks to a **tag**. The genuinely-new build is the
**geometric-mask (b)**, and its only load-bearing job is to provide the **fixed-location reference**
the floor test measures the amplitude-clamped wall against. If (b) is expensive at the R=100 rung,
it may be run at a **subset** of rungs (§7 freeze-time decision).

**Do-not-conflate reminder (torus erratum, on main).** On this lattice, an enclosure with **no
imposed geometric mask and `pml=0` is a periodic torus (energy-closed-PERIODIC), NOT a Dirichlet
reflecting box** (`k4_tlm.py:128,:352,:393,:437-440`;
`research/2026-07-13_genesis-npersist-n14-battery_RESULT.md`). The **geometric-mask BC (b) is what
actually produces a walled Dirichlet box**; the amplitude-clamp (a) and the emergent path produce a
saturation-front cavity, not a geometric box. Every "closed" label in this prereg means **the
imposed reflecting wall (a or b)**, and the fool-mode meters (§4 bin vi) must state periodic-vs-Dirichlet
per bin.

**Detectors (walk card).**
- **(p,q) winding** — `src/ave/solvers/phase_space_winding.py`, a **Lissajous/quadrature winding,
  NOT real-space linking** (`:39-45`); dual counters (unwrap + circulation) gated to **agree within
  0.20 turns** (`read_winding` `agree_tol=0.20`); **poloidal Nyquist ≥ 10 samples/period**
  (`nyquist_min=10.0`); orbit-closure within 25% (`closure_quality<0.25`); asserts α-freedom.
- **Localization meters** — participation number **PN = 1/Σpᵢ²** (local, degeneracy-safe, does not
  telescope on the closed graph — `localization-readjudication_result.md:127-128`) and/or
  **central-core-fraction** (`n14 RESULT:246-253`), computed **per-sector** (A1-energy, T2/Φ_link,
  **never summed**) under **both** the reflecting wall **and** an absorbing-PML twin.
- **Sphere-leg cross-check** — `radial_eigenvalue.py` ABCD radial cascade hosts an imposed radial
  impedance step natively (`:2-6,:23,:36-39`); adequate for the sphere leg, inadequate for the
  horn-torus (which needs the 3D imposed-mask path).

## §3 — THE BATTERY

**Core axes** (every axis KEEP-BOTH unless it is a scan):

| Axis | Values | Rationale |
|---|---|---|
| **Shape** | **sphere** (null geometry) × **horn-torus** (canon lean, $R=r=\ell_{\text{node}}/2\pi$, `electron-unknot-cosserat-seeder.md:18`) | if (2,3) shows in the **sphere too**, the winding is **closure-forced, not geometry-smuggled** — the strongest version (Grant ruling, walk card) |
| **BC mode** | **amplitude-clamp** (native S(A)-gate) × **geometric-mask** (imposed Dirichlet) | the §2 KEEP-BOTH instrument axis — running both is the floor test |
| **R-ladder** | $R/\ell_{\text{node}} \in \{1,\ 1.6,\ 3,\ 10,\ 30,\ 100\}$ | resolution-dial scaling test; **crossover $R_\times$** (where the ground-state class changes, or the amplitude-clamped wall lifts off the geometric floor) is a **derived dimensionless target**. Rung 1.6 = the hollow-vortex balance locus (Wall B, `hollow-vortex-binding.md:49`) — a canon-relevant rung, not arbitrary |
| **Regime** | **cold-linear eigensolve** (primary) × **driven-ping** (secondary) | **frozen per bin**; a linear null on a possibly-nonlinear closure = ARTIFACT-eligible (Plumber Q3) |
| **Decomposition** (read-axis) | **canonical two-sector Clifford** (A1-toroidal φ / ω-poloidal ψ, `phase_space_winding.py:39-42` on the `coupled_cage_winding.py:43-52` fields) × **coordinate-prereg pair** (n̂-direction winding = the "2" / U(1) fibre-phase = the "3", `research/2026-06-05_…coordinate-prereg.md:29-30`) | the two decompositions **assign the 2 and the 3 to different physical dials** (canonical: 2 on A1, 3 on ω; coordinate-prereg: 2 on direction, 3 on fibre-phase). **Running both resolves the two-dials question** (Plumber Q4); the closure-class claim states **which pair** it is keyed on, **per bin** |

**Control overlay (fool-mode, #670-inherited).** Each **localization** read (bin vi) is *also*
computed under an **absorbing-PML twin** of the same configuration. This is a KEEP-BOTH control on
the *meters*, distinct from the BC-mode axis (which is about how the *reflecting* wall is imposed).

**Cell count (honest).** Primary eigensolve cells: **shape(2) × BC(2) × R(6) = 24**; × regime(2) =
**48 runs**; each winding-read applied in **both decompositions = 96 winding-reads** over 48 runs.
The PML-twin control doubles only the **localization** sub-reads, not the full battery. **Sphere +
amplitude-clamp** cells are the cheapest and are the **primary null-geometry spine**; the
**horn-torus + geometric-mask + R∈{30,100}** cells are the expensive corners (§6 compute note).

**Sampling arithmetic (walk card, inherited).** Size the driven-ping record so the **poloidal "3"**
is resolved at **≥10 samples/period** (`phase_space_winding.py` `nyquist_min=10.0`) and the
poloidal-rate guard `psi_resolved ≥ 0.5` (`tethered_pivot_winding.py:230`) holds — else the read is
**INCONCLUSIVE-Nyquist before it is anything else.** For the cold eigensolve the winding is read
from the **complex eigenvector's phase winding** around the torus (not a time-orbit); the same
dual-counter agreement (<0.20 turns) and the same do-not-conflate coordinate rails apply. **(The
eigenvector-winding read mechanics are a freeze-time build detail — §7.)**

## §4 — THE FROZEN-BIN CANDIDATES

*(Proposed; enforce only after the freeze push. Bins are exhaustive and mutually exclusive; every
bin has an INCONCLUSIVE / null-outcome landing so "no closure" and "artifact" can win.)*

**(i) Ground-state winding class** — per (shape × BC × R), the (p,q) of the lowest interior mode,
read by `phase_space_winding.py` in the **declared** decomposition, dual-counter agreement <0.20
turns, poloidal Nyquist ≥10 samples/period.
Bins: `(0,0)` / `(1,1)` / **`(2,3)`** / `other-(p,q)` / `NON-INTEGER (no closure)` /
`INCONCLUSIVE-Nyquist`.

**(ii) Geometry dependence** — winding-class comparison across the two shapes.
Bins: `CLOSURE-FORCED` (same class, sphere and horn-torus — **strongest IDENTITY-leg support**) /
`GEOMETRY-SET` (classes differ — winding is boundary-**shape** data) / `TORUS-ONLY` (geometry-smuggled) /
`NEITHER`.

**(iii) THE FLOOR TEST** *(new — from the Wall-A ruling, in-flight)* — the location-derivation debt.
Two sub-reads, both **dimensionless booleans**:
- **Ground-state coincidence** — does the **amplitude-clamped** wall's settled location coincide
  (within a pre-registered dimensionless tolerance, §7) with the **ropelength floor** (the
  geometric-mask location) at ground state?
  Bins: `SETTLES-AT-FLOOR` / `SETTLES-ABOVE-FLOOR` / `SETTLES-BELOW-FLOOR` / `NO-SETTLE`.
- **Excited-state lift-off rider** — does the amplitude-clamped wall **lift off** the floor at larger
  R (the excited-states-lift-off rider)?
  Bins: `LIFTS-OFF` / `STAYS-PINNED` / `INCONCLUSIVE`.
- **Note (in-flight dependency):** the floor value and the coincidence tolerance are **Wall-A-ruling
  inputs**; re-verify against the sibling lane's landed commit at freeze time (§7). The "ropelength
  floor" reference geometry is the geometric-mask location, **not** an α-carrying radius — outputs
  stay dimensionless.

**(iv) SU(2) 4π-closure check** — does the "2" present as a **4π (double-traversal)** closure of the
toroidal angle before the trajectory closes (Grant's double-cover suspicion), guarded by the
three-"2"s disambiguation (this bin **tests**, does not assume).
Bins: `2π-closes` / `4π-closes` / `unresolved`.

**(v) Dimensionless mode-ratio ladder** — first-N mode-frequency **ratios** + **degeneracy counts**
per shape (spectrum fingerprint, scale-free). **No absolute frequency, no radius, nothing ∝ the
imposed scale** leaves the prereg.

**(vi) Fool-mode discriminators** *(the #670-inherited axis)* — per-mode **participation-ratio PN**
and **core-fraction**, **per-sector** (A1-energy, T2/Φ_link — **never summed**), under **BOTH** the
imposed reflecting wall **AND** the absorbing-PML twin.
- **Refusal (frozen):** `E_persist ≡ 1.0` (a conservation identity, zero discriminating power) and
  **raw φ-retention** are **inadmissible as localization evidence** (`n14 RESULT:29-33,:84-88,:162-163,:170-172`).
- **Enclosure label (torus erratum):** the "closed" enclosure on this lattice is **energy-closed-PERIODIC**
  unless the **geometric-mask** BC is active (which makes it Dirichlet). **Each bin states
  periodic-vs-Dirichlet** so a PN read is not mis-attributed to a geometric wall that is actually a torus.

## §5 — RAILS (verbatim-class; these do not move at freeze)

1. **Existence-NOT-formation.** Stage 1 reads **existence-given-boundary** only. It does **not**
   refill the twice-falsified self-formation slot (A47 v11b; `coupled_eigensolve.py:13-14`). The
   interior-field genesis negatives "rule out the interior-field route, **NOT the electron's
   existence**"; this test "was never run" (`genesis-chord-falsification-ledger.md:26`). **mass = A1
   (#260) untouched throughout.**

2. **Dimensionless outputs only** (calibration-circularity rail). Admissible findings: winding
   integers (p,q); mode-frequency **ratios**; degeneracy counts; geometry-invariance booleans;
   per-sector participation numbers; floor-coincidence booleans. **Inadmissible as findings:** any
   absolute frequency, any radius, anything ∝ the imposed scale (the wall's shape **and** scale are
   **inputs** — echoing them back is a calibration identity).

3. **(p,q) in PHASOR coordinates only.** Never read (p,q) off a single bond's (V_inc, V_ref) — that
   is the one-LC C↔L slosh axis, structurally ~1:1, never (2,3) (`…coordinate-prereg.md:25-30`; the
   blind extractor read (8,0) on a planted (2,3)). **Do-not-conflate families:** the phase-space
   detector `phase_space_winding.py` is a **Lissajous/quadrature** winding; the **real-space**
   extractors (`charge_quantization.py:136,:208`; `fast_winding_extractor.py:165`) are a **different
   coordinate** and are **never** cited as "the winding detector" without naming the family.

4. **Sector-ownership (A1 ⊥ T2).** The imposed wall terminates the **A1 mass channel**; it is
   **NOT** the $\Gamma_{\text{spinor}}=-1$ $2\pi\to4\pi$ wall — **do-not-re-collide**
   (`vol9/ch3-pin-port-configuration/device-circuit-models.md:161`; A1⊥T2 per
   `master-equation.md:20`). Never wire the winding into the breather's own (V_inc, V_ref) phasor
   (the genesis-24 `w_pol=0` double-count). Never phrase "the winding confines the mass"
   (`electron-identification.md:47,:53`). Carry the **STRUCTURE-derived / SELECTION-imported** tag: the
   (p,q) *structure* is axiom-derived, the (2,3) *selection* is imported
   (`electron-identification.md:50,:77,:101`).

5. **No α seeding.** No `ALPHA` / `Q_TANK` / `KAPPA_CHIRAL_ELECTRON` / `V_SNAP` on any verdict path
   (the `coupled_eigensolve.py:85-89` import-guard triad enforces this at import time). V_snap/V_yield
   enter **only** as a declared operating-point calibration, never on a verdict read.

6. **CP8/CP10 emergence fence.** The wall **is** a boundary condition = the substrate-native rendering
   of confinement (CP10) — imposing it is **not** plant-the-composite. **Fence 1:** do **not** also
   seed a finished localized mode inside and read persistence (the CP8 plant); the excitation is a
   broadband interior kick / eigenmode extraction, **not** a mode template. **Fence 2:** Stage 1 is
   static-wall existence-given-boundary; the mode-sourced self-consistency check
   (`electron-identification.md:13`) is **Stage 2** — a Stage-1 pass is **not** over-read as the
   self-consistent electron.

### The D3-movement map (which outcomes move which COEXIST leg)

| Census outcome | D3 movement |
|---|---|
| (2,3) is the ground-state closure class in **both** shapes (sphere included) | **Strongest support for the IDENTITY leg** — winding is set by the boundary's reflection map alone (genuine boundary data). Also converts the (2,3) **SELECTION** import→derivation — **a separate, larger claim with its own adjudication**, not silently folded in |
| (2,3) in the **horn-torus only** | Winding is geometry-keyed — the canon envelope carries the selection. IDENTITY leg weakened toward "boundary **shape** data"; feeds the OPEN topology→shape chain (`device-circuit-models.md:157-159`, no BVP solved) |
| some (p,q) ≠ (2,3), or **no integer closure class** | The emergence suspicion **fails**; (2,3) SELECTION stays imported; **COEXIST stands unchanged. NOT a falsification of the electron** (scope carve, §5.1) |
| **Stage-2** (task #45): imposed wall's balance locus coincides dimensionlessly with the mode it contains | ENVELOPE leg supported — container and contents mutually consistent |
| **Stage-2**: no coincidence / mode requires interior structure the singularity forbids | **The ONLY outcome class that genuinely re-opens D3 territory** — the two-questions-two-radii fence would need re-walking |

**Residual that must NOT be silently resolved:** the precursor-vs-end-state sub-fork (`clm-uatcql`,
`vol2/claim-quality.md:1146`; sub-fork-OPEN text at `:1160`) stays **OPEN** (Rule 12 / A47 v11b — a
falsified slot is not refilled).

## §6 — EXECUTION PLAN

1. **Instrument-build commits** — extend `coupled_eigensolve.py` with (a) the amplitude-clamp path
   (largely native — wire the S(A)-gate as an explicit imposed-BC surface) and (b) the geometric-mask
   Dirichlet path (new); the sphere-leg `radial_eigenvalue.py` cross-check; the eigenvector-winding
   read into `phase_space_winding` coordinates; the PN / core-fraction per-sector meters and the
   PML-twin control. **Run early, even imperfect** (Rule 10 empirical-driver discipline): PML-cell
   exclusion before any top-K extraction; density-peak sampling on the shell (centroid of a shell is
   the empty middle); reactance-pair tracking (C-state **and** L-state) over the driven-ping window.
2. **Prereg FREEZE commit, pushed** — after the §7 walk closes, freeze this file *as-is by push*
   **before** the first battery-run commit (freeze precedes driver in git history).
3. **Battery runs** — the §3 matrix; cheap null-geometry spine first (sphere + amplitude-clamp),
   expensive corners last.
4. **RESULT doc** — bins reported per §4; honest closure (Rule 11) if the suspicion fails decisively.
5. **Adversarial review** — via the `.claude/workflows/ave-adversarial-pr-review.js` wrapper.
6. **DO-NOT-MERGE** — only Grant merges; the freeze happens at execution, not at this draft PR.

**Compute note (honest).** Conservative Hermitian **eigensolves are cheap** relative to the FDTD
batteries (no time-stepping, no long ringdown record). The scaling risk is the **R-ladder**: at
`R/ℓ_node = {30, 100}` the lattice must resolve both the major radius and the poloidal "3" at
≥10 samples/period, so N grows and the **dense** eigensolve (`np.linalg.eigh`-class) becomes
memory/time-bound. **Flag:** the R∈{30,100} rungs likely need **sparse shift-invert solvers**
(`scipy.sparse.linalg.eigsh` on the SA end, matching the existing `_cluster_spectrum` gap machinery)
rather than dense. The **geometric-mask (b)** at the top two rungs is the single most expensive
corner; §7 carries the decision to run (b) at a rung-subset if needed. The **driven-ping (secondary
regime)** is the more expensive leg overall and may be scoped to a subset of bins where the
cold-linear read returns `NON-INTEGER` or `INCONCLUSIVE-Nyquist` (i.e. where nonlinearity is the live
artifact-vs-negative question).

---

## Receipts (verified at HEAD `c12f2bdb`, this session; ✅ verified / ⚠️ carried-correction / 🔴 in-flight)

| Receipt | File:line | Status |
|---|---|---|
| Reuse target: α-clean Hermitian eigensolve; import-guard triad | `src/ave/solvers/coupled_eigensolve.py:9-13,:27,:34-36,:85-89` | ✅ |
| `D = 1/S(A)` amplitude-native path (the amplitude-clamp BC (a)) | `coupled_eigensolve.py:28,:105` | ✅ |
| Solver's own "TWO WALLS" resolution (mass cap V_snap vs coupling front V_yield) | `coupled_eigensolve.py:~388-400` | ✅ (corroborates the conflation-map two-walls; not cited as a verdict) |
| Sphere-leg host (radial ABCD impedance step) | `src/ave/solvers/radial_eigenvalue.py:2-6,:23,:36-39` | ✅ |
| (p,q) phasor detector, coordinate + dual-counter + Nyquist gates | `src/ave/solvers/phase_space_winding.py:39-45` (coord); `read_winding` `agree_tol=0.20`, `nyquist_min=10.0`, `closure_quality<0.25` | ✅ |
| Two-sector fields (A1 mass / ω winding) | `src/ave/solvers/coupled_cage_winding.py:43-52` | ✅ |
| Coordinate-prereg decomposition (2 on direction n̂ / 3 on fibre-phase) + (V_inc,V_ref) 1:1 trap | `research/2026-06-05_2-3-winding-extractor-coordinate-prereg.md:17,:25-30` | ✅ |
| Poloidal-rate guard | `src/ave/solvers/tethered_pivot_winding.py:230` | ✅ (carried from walk card; re-verify at freeze) |
| Real-space extractors (do-not-conflate) | `charge_quantization.py:136,:208`; `fast_winding_extractor.py:165` | ✅ (carried) |
| Sector-ownership: A1 mass wall vs Γ_spinor — do-not-re-collide; topology→shape OPEN (D4) | `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:157-159,:161` | ✅ (canonical path is **vol9/ch3**, not vol2) |
| A1⊥T2 no-double-count | `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20` | ✅ (carried) |
| Scope carve verbatim (rule out interior-field route, NOT existence; "never run") | `manuscript/ave-kb/common/genesis-chord-falsification-ledger.md:26` | ✅ |
| Localization = boundary/topological; bulk self-trap ruled out; mass=A1 untouched | `genesis-chord-falsification-ledger.md:86` | ✅ |
| STRUCTURE-derived / SELECTION-imported tag | `electron-identification.md:50,:77,:101` | ✅ (carried) |
| Fool-mode #670 numbers + PN/core-fraction meters | `research/2026-07-13_genesis-npersist-n14-battery_RESULT.md:29-33,:84-88,:162-163,:170-172,:246-253` | ✅ (on main) |
| PN degeneracy-safe, does not telescope | `research/2026-07-03_localization-readjudication_result.md:127-128` | ✅ (carried) |
| Torus erratum: pml=0 = periodic torus, NOT reflecting box | `k4_tlm.py:128,:352,:393,:437-440`; `n14 RESULT` | ✅ (on main, commit `0a8e5543`) |
| D3 RULED COEXIST 2026-07-09; four landing leaves; census = stress-test | `_orchestration/2026-07-09_electron-def-canon-authoring.md:11,:21`; `electron-identification.md:57-62`; docket `2026-07-10_rulings-docket.md:482` | ✅ |
| Precursor-vs-end-state sub-fork OPEN | `clm-uatcql`, `vol2/claim-quality.md:1146` (id); sub-fork-OPEN text at `:1160` | ✅ **(docket carried `:1159` — corrected to id `:1146`/text `:1160`; same claim block)** |
| Firewall: stiffening branch + fourth-engine gate | `~/.claude/skills/ave-loop-gap-harness-discipline/SKILL.md:37-44` | ✅ (carried) |
| Wall-A ruling (floor + amplitude-rail + lift-off rider + deficit-knee re-tag) | sibling lane `docs/wall-a-ruling-propagation` (at HEAD = `c12f2bdb`, **not yet committed**) | 🔴 **in-flight — no tracked leaf yet; re-verify at freeze** |

---

## §7 — OPEN ITEMS for the freeze-time decision (the walk must close these)

1. **Wall-A ruling landing.** The floor value, the amplitude-rail mechanism cite, the excited-state
   lift-off rider, and the deficit-knee re-tag are **in-flight** in `docs/wall-a-ruling-propagation`
   and have **no tracked leaf** at this HEAD. Bin (iii) and the §2 floor test **depend on them**.
   Re-verify against the sibling lane's landed commit before the freeze push; if the ruling changes
   the floor definition, bin (iii)'s coincidence tolerance changes with it.
2. **Floor-coincidence tolerance.** The dimensionless tolerance for `SETTLES-AT-FLOOR` (bin iii) is
   **not yet set** — it must be **radius-discriminating** (the conflation map's warning: the O(1)
   ℓ_node landing is dimensionally forced and unfireable if the tolerance is loose), and it must allow
   **"does not settle at floor"** to win.
3. **Geometric-mask (b) rung coverage.** Run (b) at **all six** R-rungs, or a **subset** (e.g.
   {1, 1.6, 3, 10}) with {30,100} amplitude-clamp-only? Compute-driven; §6 flags the top-two rungs as
   the expensive corner.
4. **Eigenvector-winding read mechanics.** For the cold-linear leg, the (p,q) read is from a **complex
   eigenvector's phase winding**, not a time-orbit — the exact reduction (which eigenvector-phase field
   feeds `phase_space_winding`, how the dual-counter agreement is defined on a static field) is a build
   detail to pin before freeze.
5. **Two-dials keying.** Both decompositions are run (KEEP-BOTH), but the **headline closure-class
   claim** must state **which pair** it is keyed on (Plumber Q4 — Grant call; canonical A1/ω vs
   coordinate direction/fibre-phase).
6. **Which skin is the wall standing in for?** (Plumber Q2 / conflation map.) The R-ladder spans both
   the Wall-A tube skin (~0.16 ℓ_node, below the ladder floor of 1) and the Wall-B bubble
   (~1.6 ℓ_node, rung 2). The ladder currently starts at **R=1**; if the wall is meant to sit at the
   **0.16 tube skin**, the ladder floor is wrong. **Freeze-time: confirm the ladder's physical anchor.**
7. **Firewall confirm.** The in-branch `coupled_eigensolve` extension is the ruled route (no fourth
   engine); confirm this holds once the geometric-mask (b) code exists (Plumber Q5).

---

*DRAFT — pending Grant review. Freeze-by-push at execution. Only Grant merges.*

