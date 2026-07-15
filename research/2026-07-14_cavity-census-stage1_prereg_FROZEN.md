# Cavity-Census Stage-1 — imposed-cavity mode census — **FROZEN prereg**

> **FROZEN by push (ave-prereg v1.7 Step 3.11, model
> `research/2026-07-13_genesis-npersist-n14-battery_prereg_FROZEN.md`).** This file
> is the DRAFT (`research/2026-07-14_cavity-census-stage1_prereg_DRAFT.md`, on main
> via PR #681) promoted to frozen, with the seven §7 open items RESOLVED in §0 below.
> The freeze commit is pushed ALONE, BEFORE the first instrument/driver commit — the
> freeze precedes the driver in git history. The bins, thresholds, tolerances, and
> battery matrix below are COMMITMENTS from this push forward. Only Grant merges.

**HEAD at freeze.** `db06ba82` (origin/main; PR #681 DRAFT + PR #682 Wall-A ruling both
landed). Every file cite in §0 re-verified at this HEAD this session (verify-before-cite).

---

## §0 — FREEZE RESOLUTIONS (the seven §7 items — CLOSED at freeze)

The seven open items from the DRAFT's §7 are resolved as follows. Items **(5)** and **(6)**
are additionally flagged **"core-session default — Grant veto window open"** in the freeze
commit message (they were Grant-veto-flagged in the docket; the core session chose the
default and left the veto window open).

**(1) Wall-A dependency — RESOLVED (ruling on main).** The Wall-A ruling landed on main via
**PR #682** (`_orchestration/2026-07-10_rulings-docket.md:511-603`, the 2026-07-14
continuation). The load-bearing content re-verified at HEAD `db06ba82`:
- **Floor (ROLE-1):** the ropelength radius **`ℓ_node/(2π)`** (one-pitch closure `2πR = ℓ_node`,
  horn-torus `R = r`) is the geometric MINIMUM; the ground state SATURATES it
  (`electron-unknot-cosserat-seeder.md:18` — "`R_loop = r_tube = ℓ_node/(2π) ≈ 0.16 ℓ_node`
  (Bounding Limit 1 saturation)"; docket `:522-531,:585`).
- **Rail (ROLE-2):** the `Γ=−1` wall **IS** the local `S(A)→0` amplitude discontinuity
  (amplitude-primary mechanism); **Location = max(dynamical S→0 locus, geometric floor)**;
  for the ground state these **coincide** (docket `:533-538,:586`;
  `breathing-soliton-v14-mode-i.md:101` floor+rail annotation).
- **Lift-off rider:** any non-ground-state cavity should **LIFT OFF the floor** — located
  ABOVE the ropelength minimum; **the cavity-census R-ladder is the named instrument**
  (docket `:529-531`).
- **Deficit-knee re-tag (ROLE-3):** the `A²=2α` (`A=√(2α)`) contour is the **deficit knee**
  (`ΔS=α`, regime-I boundary; coordinate authority `src/ave/core/chiral_lattice_v10.py:29-30`,
  `A_YIELD_SQ = 2.0*ALPHA`), reflecting `Γ≈−0.002` — **NOT the TIR wall** (docket `:540-553`).
  The census does **not** place any wall at the √(2α) contour.

**(2) Floor tolerance — RADIUS-DISCRIMINATING (grid-spacing-derived; DOES-NOT-SETTLE first-class).**
The settled wall location `R_wall/ℓ_node` is reported with a **grid-resolution-derived uncertainty**
(± half the lattice spacing at that rung, in `ℓ_node` units). The **FLOOR-COINCIDENCE bin
(`SETTLES-AT-FLOOR`) fires iff `|R_wall − ℓ_node/(2π)| < 2 × Δgrid`**, where `Δgrid` is the
lattice cell spacing at that rung expressed in `ℓ_node` units (`Δgrid = 1/ℓ_node_cells`, see §0-anchor).
**No dimensionally-forced O(1)-`ℓ_node` window** is admitted (the conflation-map warning honored):
the tolerance is a fixed multiple of the *grid spacing*, not an O(1) fraction of `ℓ_node`, so a
wall that settles at the canonical rung (`R_wall ≈ ℓ_node`) is correctly NOT-at-floor.
**`DOES-NOT-SETTLE-AT-FLOOR` is a first-class winnable bin** (`SETTLES-ABOVE-FLOOR` /
`SETTLES-BELOW-FLOOR` / `NO-SETTLE`).

**(3) Mask rung coverage — compute-driven; minimum {1, 1.6, 10, 100}; actual stated here.**
Target: all eight rungs. **Minimum coverage {1, 1.6, 10, 100} is MET.** Actual coverage at
freeze (compute receipt in §0-anchor + §6):
- **3D coupled-eigensolve winding census (bins i, ii, iv, vi):** rungs **{0.16, 0.5, 1, 1.6, 3}**
  (both shapes × both BC modes). Rung **3** is the dense-solve edge (`N≈56`); attempted, dropped
  with disclosure if it exceeds the concurrency budget.
- **Sphere-leg ABCD radial cross-check (bin v mode-ratios + bin iii floor read):** **all eight
  rungs {0.16, 0.5, 1, 1.6, 3, 10, 30, 100}** (1-D radial cascade, cheap).
- **Rungs {10, 30, 100}** have **no 3-D coupled winding read** (infeasible dense; `R ≥ 80` cells) —
  covered by the sphere-ABCD leg only. **Disclosed, not silently capped.** The winding-class bins
  (i, ii, iv) at {10, 30, 100} report `NOT-RUN-3D (compute)`.

**(4) Cold-linear winding read — EIGENVECTOR two-sector phasor fields (mechanics documented).**
The `(p,q)` is read from the **complex eigenvector's** two-sector phasor structure, NOT a
time-orbit. Mechanics (frozen):
- The coupled eigenvector `v = [a_A1, b_ω]` (two complex scalar fields on the N³ lattice).
- **Toroidal read (the "2"):** sweep the toroidal angle `φ ∈ [0,2π)`; at each `φ` reduce the
  **A1 sector** to a single complex number `Φ_A1(φ) = Σ_{meridian disk at φ} a_A1(x)`
  (the sector-cross-section integral — the static-field analog of `phase_space_winding.py:39-40`'s
  `arg(Σ_x a_A1)`, with the loop parameter replacing time). `p = ` net turns of `arg Φ_A1(φ)`.
- **Poloidal read (the "3"):** sweep the poloidal angle `θ ∈ [0,2π)`; reduce the **ω sector**
  to `Ψ_ω(θ) = Σ_{toroidal ring at θ} b_ω(x)`. `q = ` net turns of `arg Ψ_ω(θ)`
  (`phase_space_winding.py:41-42`).
- **Dual counter (F4):** `p,q` read by BOTH unwrap-count AND circulation integral
  (`phase_space_winding._net_turns_unwrap` / `_net_turns_circulation`); they must **agree
  within 0.20 turns** or the read is `INCONCLUSIVE`.
- **Nyquist:** the poloidal loop must be sampled at **≥10 points/period** of the winding
  (`nyquist_min=10.0`); a sub-resolved loop is `INCONCLUSIVE-Nyquist` **before it is anything else**.
- This is the **PHASOR (Lissajous/quadrature) coordinate** (Rail 3), NOT the real-space
  director extractor. **It is NOT read off the seeded template `ê_w`** — `ê_w` carries the
  planted `(2,3)` by construction and reading it is the tautology the census forbids (it is used
  ONLY as the planted-winding gate's positive control, §4 bin-firing). The eigenvector's own
  `[a_A1, b_ω]` phase structure is the emergence read.

**(5) Dial keying — HEADLINE on canonical two-sector Clifford [Grant-veto flagged].** The
**headline closure-class** is keyed on the **canonical two-sector Clifford angles**
(A1-toroidal `φ` / ω-poloidal `ψ` per `coupled_cage_winding.py:43-52`,
`phase_space_winding.py:39-42`). The **direction-winding / fibre-phase decomposition**
(coordinate-prereg, `research/2026-06-05_2-3-winding-extractor-coordinate-prereg.md`) runs
**KEEP-BOTH secondary**, reported per bin. **Core-session default; Grant veto window open.**
*Build note (honest):* the coordinate-prereg direction leg requires a **vector director**; the
rigid-template eigenvector's ω sector is a **scalar** `b_ω`, so the only available director is
the seeded `ê_w` — reading it is **tautological** (always direction=2). The secondary
decomposition is therefore reported as **`SEED-CARRIED (tautological direction leg)`** and
routed to the plant-gate, NOT treated as a genuine emergence read (§4 fool-mode).

**(6) R-ladder anchor — EXTENDED DOWN to the tube-skin/floor rung [Grant-veto flagged].** The
ladder is extended down to include the ground-state floor rung:
**`R/ℓ_node ∈ {0.16, 0.5, 1, 1.6, 3, 10, 30, 100}`** (the Wall-A floor at
`ℓ_node/(2π) ≈ 0.159` is rung `0.16`). **Core-session default; Grant veto window open.**

**(7) Firewall — CONFIRMED in-branch, no fourth engine.** The build **extends
`coupled_eigensolve`** (imposed interior Dirichlet mask on its Hermitian `H`) **+ a sphere-leg
radial ABCD cross-check**. **No new engine class.** The mask is a real diagonal
projection/penalty on the existing `_assemble_H()` operator; the radial leg is an α-clean 1-D
ABCD cascade (the METHOD of `radial_eigenvalue.py`, NOT its α-loaded atomic potential — see
Rail-5 note in §0-anchor). Confirmed: no standalone imposed-BC cavity solver (which would be a
fourth firewalled object needing Grant sign-off, `SKILL.md:44`).

### §0-anchor — the dimensionless lattice anchor (frozen)

- **`ℓ_node` maps to `ℓ_node_cells = 8.0` lattice cells** (the Compton unit's discretization;
  the canonical validated winding scale is `R≈7` cells, so rung `R/ℓ_node=1 → R=8` cells sits at
  the validated scale). Every geometry radius is `R_cells = (R/ℓ_node) × 8`. **All outputs are the
  dimensionless ratio `R/ℓ_node`; no cell count and no absolute length leaves the prereg** (Rail 2).
- **Floor in cells:** `ℓ_node/(2π) = 8/(2π) = 1.273` cells. `Δgrid = 1/8 = 0.125 ℓ_node` at every
  rung (uniform lattice); floor tolerance `2·Δgrid = 0.25 ℓ_node`.
- **Feasibility (compute receipt):** coupled DOF `= 2·N³`; `N ≳ 2·R_cells + 2·pml`. Timings this
  session: `N=32` (65k DOF) eigsh k=12 in ~1.4 s; `N=48` ~10 s; `N≥64` tens of s. Rungs
  `{0.16,0.5,1,1.6}` → `R_cells ∈ {1.3, 4, 8, 12.8}` → `N ∈ {16,20,32,40}` comfortable; rung `3`
  → `R=24`, `N≈56` (edge); rungs `{10,30,100}` → `R ∈ {80,240,800}` infeasible dense (sphere-ABCD
  only). **Concurrency: moderate (the shared-machine thrash lesson) — serial battery, no parallel
  eigsh storms.**
- **Rail-5 (no-α) note — a frozen declaration I flag I could not honor verbatim:** the DRAFT §2
  names `radial_eigenvalue.py` as the sphere-leg host, but that module **imports `ALPHA`**
  (`radial_eigenvalue.py:64`) and is an α-loaded atomic solver — wiring it onto a verdict path
  would violate Rail 5. **Resolution:** the sphere leg reuses the ABCD transfer-matrix **METHOD**
  (the `cosh/cos` section cascade, `radial_eigenvalue._abcd_section`) in a **new α-clean radial
  routine** (Dirichlet spherical Helmholtz, dimensionless `k·R`), NOT the α-carrying
  `radial_eigenvalue_abcd()` atomic potential. Same method, α-free. Flagged here per
  flag-don't-fix; surfaced to the auditor lane.

---

*(The frozen body below is the DRAFT §Sector-header through §6, carried verbatim as the
commitment. Where §0 above resolves a §7 item, §0 governs.)*

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
  `electron-identification.md:13`) is **Stage 2** (task #45). A Stage-1 pass is **not** the
  self-consistent electron.
- **REGIME** — **KEEP-BOTH**: cold-linear (Hermitian eigensolve, primary) and
  driven-toward-saturation (time-domain ping, secondary). The regime flag is **frozen per
  bin** before running — a linear null in a regime where the closure cannot exist is
  **ARTIFACT-eligible, not a negative** (Plumber Q3).
- **PHASE-STATE** — the wall is imposed on the **cold medium** (cold-linear leg) or driven
  toward the self-stiffened flow (driven leg). The interior excitation is a **broadband
  kick / eigenmode extraction**, never a seeded finished mode (CP8 fence, §5).
- **Instrument** — extend the **α-clean Hermitian eigensolver** `coupled_eigensolve.py` with
  an **imposed boundary**; sphere leg cross-checked via an **α-clean ABCD radial cascade** (the
  `radial_eigenvalue.py` METHOD, α-free — §0-anchor Rail-5 note). Reads are
  **dimensionless-only** (winding integers, mode-frequency ratios, floor-coincidence booleans).
  No α on any verdict path.
- **consistency-vs-emergence** — a census that returned **(2,3) as the ground-state closure
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
2026-07-09** and canonized at four leaves (`electron-identification.md:57-62`;
`substrate-perspective-electron.md:93-103,135-145`; `the-abandoned-interior.md:84-97`;
`hollow-vortex-binding.md:28-37`). The census **stress-tests the ruling's two legs with new
evidence** — it does not re-litigate the ruling. The precursor-vs-end-state sub-fork
(`clm-uatcql`, `vol2/claim-quality.md:1146`) stays **explicitly OPEN — not silently resolved.**

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

**Ruled reuse target.** Extend `src/ave/solvers/coupled_eigensolve.py` — the **α-clean
conservative Hermitian eigensolve** of the native K4 stiffness (real eigenvalues = the lossless
reactive cage; α-clean import-guard triad at `:85-89`). Its confinement is currently
**emergent-periodic** (the S(A)-front, `D=1/S(A)`); the arc's extension = give it an **imposed
boundary**. **Extend this, do not build fresh** (firewall §0 item 7).

### The config question — KEEP-BOTH

| BC mode | What it is | Build status | Wall-A role |
|---|---|---|---|
| **(a) amplitude-clamp** | native **S(A)-gate** — the solver's existing `D = 1/S(A)` path; the wall **location is field-decided**, settling wherever the amplitude clips to yield | **already native** | the **mechanism-faithful** choice — the operative Γ=−1 register IS the amplitude rail (Wall-A ROLE-2) |
| **(b) geometric-mask** | an **imposed geometric Dirichlet mask** at a *fixed* radius — the wall location is **posited** at the ropelength floor | **genuinely new capability** | the **floor-geometry** choice — pins the wall at the ropelength minimum (Wall-A ROLE-1) |

**Running both, and comparing where the amplitude-clamped wall settles against where the
geometric mask puts it, IS the FLOOR TEST** (bin iii): does the field-decided wall settle **at**
the ropelength floor at ground state, and **lift off** it at larger R (the lift-off rider)?

**Do-not-conflate reminder (torus erratum, on main).** On this lattice, an enclosure with **no
imposed geometric mask and `pml=0` is a periodic torus (energy-closed-PERIODIC), NOT a Dirichlet
reflecting box** (`k4_tlm.py:128,:352,:393,:437-440`;
`research/2026-07-13_genesis-npersist-n14-battery_RESULT.md`). The **geometric-mask BC (b) is what
actually produces a walled Dirichlet box**. Every "closed" label means **the imposed reflecting
wall (a or b)**; the fool-mode meters (bin vi) state periodic-vs-Dirichlet per bin.

**Detectors.**
- **(p,q) winding** — `src/ave/solvers/phase_space_winding.py`, a **Lissajous/quadrature winding,
  NOT real-space linking** (`:39-45`); dual counters (unwrap + circulation) gated to **agree within
  0.20 turns**; **poloidal Nyquist ≥ 10 samples/period**; asserts α-freedom. Applied to the
  eigenvector's two-sector phasor fields per §0 item (4).
- **Localization meters** — participation number **PN = 1/Σpᵢ²** and **central-core-fraction**,
  computed **per-sector** (A1-energy, T2/Φ_link, **never summed**) under **both** the reflecting
  wall **and** an absorbing-PML twin.
- **Sphere-leg cross-check** — an **α-clean ABCD radial cascade** (the `radial_eigenvalue.py`
  transfer-matrix method, α-free; §0-anchor Rail-5 note) hosting the imposed radial Dirichlet step.

## §3 — THE BATTERY

| Axis | Values | Rationale |
|---|---|---|
| **Shape** | **sphere** (null geometry) × **horn-torus** ($R=r$) | if (2,3) shows in the **sphere too**, the winding is **closure-forced, not geometry-smuggled** |
| **BC mode** | **amplitude-clamp** × **geometric-mask** | running both is the floor test |
| **R-ladder** | $R/\ell_{\text{node}} \in \{0.16, 0.5, 1, 1.6, 3, 10, 30, 100\}$ | resolution-dial scaling; the crossover $R_\times$ (class change / lift-off) is a **derived dimensionless target**; floor rung `0.16` and hollow-vortex rung `1.6` (Wall B) are canon-relevant |
| **Regime** | **cold-linear eigensolve** (primary) × **driven-ping** (secondary) | **frozen per bin**; a linear null on a possibly-nonlinear closure = ARTIFACT-eligible |
| **Decomposition** (read-axis) | **canonical two-sector Clifford** (HEADLINE) × **coordinate-prereg pair** (secondary) | both run; the closure-class claim states **which pair** it is keyed on, per bin (§0 item 5) |

**Control overlay (fool-mode).** Each localization read is also computed under an **absorbing-PML
twin** — a KEEP-BOTH control on the *meters*.

## §4 — THE FROZEN BINS

*(Bins exhaustive and mutually exclusive; every bin has an INCONCLUSIVE / null landing so "no
closure" and "artifact" can win.)*

**(i) Ground-state winding class** — per (shape × BC × R), the (p,q) of the lowest interior mode.
Bins: `(0,0)` / `(1,1)` / **`(2,3)`** / `other-(p,q)` / `NON-INTEGER (no closure)` /
`INCONCLUSIVE-Nyquist` / `NOT-RUN-3D (compute)`.

**(ii) Geometry dependence** — winding-class comparison across the two shapes.
Bins: `CLOSURE-FORCED` (same class both shapes) / `GEOMETRY-SET` / `TORUS-ONLY` / `NEITHER`.

**(iii) THE FLOOR TEST** — two sub-reads, both dimensionless booleans:
- **Ground-state coincidence** — does the amplitude-clamped wall's settled location coincide with
  the ropelength floor (`|R_wall − ℓ_node/(2π)| < 2·Δgrid`, §0 item 2) at the ground-state rung?
  Bins: `SETTLES-AT-FLOOR` / `SETTLES-ABOVE-FLOOR` / `SETTLES-BELOW-FLOOR` / `NO-SETTLE`.
- **Lift-off rider** — does the amplitude-clamped wall lift off the floor at larger R?
  Bins: `LIFTS-OFF` / `STAYS-PINNED` / `INCONCLUSIVE`.

**(iv) SU(2) 4π-closure check** — does the "2" present as a **4π (double-traversal)** closure of
the toroidal angle before the trajectory closes?
Bins: `2π-closes` / `4π-closes` / `unresolved`.

**(v) Dimensionless mode-ratio ladder** — first-N mode-frequency **ratios** + **degeneracy counts**
per shape (spectrum fingerprint, scale-free). **No absolute frequency, no radius, nothing ∝ the
imposed scale** leaves the prereg.

**(vi) Fool-mode discriminators** — per-mode **participation-ratio PN** and **core-fraction**,
**per-sector** (A1-energy, T2/Φ_link — **never summed**), under **BOTH** the imposed reflecting
wall **AND** the absorbing-PML twin.
- **Refusal (frozen):** `E_persist ≡ 1.0` (conservation identity, zero discriminating power) and
  **raw φ-retention** are **inadmissible as localization evidence**.
- **Enclosure label (torus erratum):** each bin states periodic-vs-Dirichlet.

## §5 — RAILS (verbatim-class; these do not move at freeze)

1. **Existence-NOT-formation.** Stage 1 reads existence-given-boundary only. It does **not**
   refill the twice-falsified self-formation slot (A47 v11b). The interior-field genesis negatives
   "rule out the interior-field route, **NOT the electron's existence**"; this test "was never
   run" (`genesis-chord-falsification-ledger.md:26`). **mass = A1 (#260) untouched.**
2. **Dimensionless outputs only.** Admissible: winding integers (p,q); mode-frequency ratios;
   degeneracy counts; geometry-invariance booleans; per-sector participation numbers;
   floor-coincidence booleans. **Inadmissible:** any absolute frequency, any radius, anything ∝ the
   imposed scale.
3. **(p,q) in PHASOR coordinates only.** Never read (p,q) off a single bond's (V_inc, V_ref). The
   phase-space detector `phase_space_winding.py` is a **Lissajous/quadrature** winding; the
   **real-space** extractors (`charge_quantization.py:136,:208`; `fast_winding_extractor.py:165`)
   are a **different coordinate** and are **never** cited as "the winding detector" without naming
   the family.
4. **Sector-ownership (A1 ⊥ T2).** The imposed wall terminates the **A1 mass channel**; it is
   **NOT** the $\Gamma_{\text{spinor}}=-1$ $2\pi\to4\pi$ wall. Never phrase "the winding confines
   the mass". Carry the **STRUCTURE-derived / SELECTION-imported** tag: the (p,q) *structure* is
   axiom-derived, the (2,3) *selection* is imported (`electron-identification.md:50,77,101`).
5. **No α seeding.** No `ALPHA` / `Q_TANK` / `KAPPA_CHIRAL_ELECTRON` / `V_SNAP` on any verdict
   path (the `coupled_eigensolve.py:85-89` import-guard triad enforces this at import time). The
   sphere-leg ABCD cross-check is **α-clean** (§0-anchor Rail-5 note).
6. **CP8/CP10 emergence fence.** The wall **is** a boundary condition (CP10) — imposing it is not
   plant-the-composite. **Fence 1:** do **not** also seed a finished localized mode inside and read
   persistence (the CP8 plant); the excitation is a broadband interior kick / eigenmode extraction.
   **Fence 2:** Stage 1 is static-wall existence-given-boundary; self-consistency is Stage 2.

### The D3-movement map

| Census outcome | D3 movement |
|---|---|
| (2,3) is the ground-state closure class in **both** shapes | **Strongest support for the IDENTITY leg**; also converts the (2,3) SELECTION import→derivation — a separate, larger claim with its own adjudication |
| (2,3) in the **horn-torus only** | Winding is geometry-keyed; IDENTITY leg weakened toward "boundary **shape** data"; feeds the OPEN topology→shape chain (`device-circuit-models.md:157-159`) |
| some (p,q) ≠ (2,3), or **no integer closure class** | The emergence suspicion **fails**; (2,3) SELECTION stays imported; **COEXIST stands unchanged. NOT a falsification of the electron** |
| **Stage-2** (task #45): imposed wall's balance locus coincides with the mode it contains | ENVELOPE leg supported |
| **Stage-2**: no coincidence / mode requires interior structure the singularity forbids | **The ONLY outcome class that genuinely re-opens D3 territory** |

**Residual that must NOT be silently resolved:** the precursor-vs-end-state sub-fork
(`clm-uatcql`, `vol2/claim-quality.md:1146`; sub-fork-OPEN text at `:1160`) stays **OPEN**.

## §6 — EXECUTION PLAN

1. **Instrument-build** — extend `coupled_eigensolve` with (a) the amplitude-clamp tag and (b) the
   geometric-mask Dirichlet path; the α-clean sphere-leg ABCD cross-check; the eigenvector-winding
   read into `phase_space_winding` coordinates (both decompositions); the PN / core-fraction
   per-sector meters and the PML-twin control; the plant-firing gates. **Run early** (Rule 10):
   PML-cell exclusion before any top-K extraction; density-peak sampling on the shell;
   reactance-pair tracking over the driven-ping window.
2. **Battery runs** — the §3 matrix; cheap null-geometry spine first (sphere + amplitude-clamp),
   expensive corners last; the coverage of §0 item 3.
3. **RESULT doc** — bins per §4; honest closure (Rule 11) if the suspicion fails decisively.
4. **Adversarial review** — via the `.claude/workflows/ave-adversarial-pr-review.js` wrapper.
5. **DO-NOT-MERGE** — only Grant merges.

**Compute note.** Conservative Hermitian eigensolves are cheap; the scaling risk is the R-ladder
(§0-anchor). Rungs `{10,30,100}` are sphere-ABCD-only. The driven-ping (secondary regime) is the
more expensive leg and **may be scoped to a spot-check** where the cold-linear read returns
`NON-INTEGER`/`INCONCLUSIVE`/`(0,0)` — disclosed at result time; the frozen regime flag makes a
cold-only null ARTIFACT-eligible on any winding bin where nonlinearity is load-bearing.

---

*FROZEN by push. Freeze precedes the driver in git history. Only Grant merges.*
