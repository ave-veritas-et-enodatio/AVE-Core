# P0 Capability + Transduction Inventory — Static-Existence Epic (2026-08-24)

**Epic:** `_orchestration/2026-08-24_static-existence-epic.md` (branch
`orchestration/2026-08-24-static-existence-epic`, worktree HEAD `a2551384`,
2026-08-24). **Class:** READ-ONLY corpus/engine inventory (P0). Mints no
claims. Every sentence governed by the epic's §5 seven-guard set + the
existence-not-emergence carve.

> **PROVENANCE FAIL-LOUD (logged first).** The three P0 pull results (t2 /
> impos / relax) did NOT reach this synthesis — the dispatch's
> `${JSON.stringify({t2, impos, relax})}` placeholder arrived
> un-interpolated, and no pull-output files exist on disk (searched the
> session scratchpad two ways: directory listing + content grep). Per
> fail-loud, this report is a **direct re-derivation of the P0 inventory
> from the worktree at HEAD `a2551384`**, not a consolidation of lane
> outputs. Every receipt below was read at its cited location in this
> session (verify-before-cite). If the original pull lanes produced
> findings beyond what is here, those outputs are lost to this synthesis
> and the orchestrator should reconcile.

> **Sector / regime declaration.** MODE: static inventory of code + canon
> (no dynamics integrated, no claims minted). SECTOR: the inventory spans
> the T2/Cosserat micro-rotation sector (the winding-owner) and the A1
> dilatation sector (the S-railing bookkeeping) — the A1 ⊥ T2 carve
> (guard 5) is applied per item, never crossed. PHASE-STATE: all machinery
> is inventoried cold (capability), not at any operating point.

---

## Verdicts up front

**V1 — T2/Cosserat channel (pull a): CARRIED and GRADEABLE in the field
engines; NO graded junction-scatter primitive exists for it; the
transverse vertex scattering is UNVERIFIED (absence confirmed two ways).**
The transverse sector is carried by at least four engines (§1.1). Its
grading kernels exist in the vector-FDTD engines (swing-ε DECREASING,
μ-circulation INCREASING) and in the Cosserat energy functional
(`use_saturation=True`). But the only saturation-reading junction-scatter
operator in the tree is the **longitudinal μ-load** form, and the scalar
machinery **explicitly fences off** the ε-load (transverse-analog) form
(§1.3). The standalone-K4 junction is amplitude-independent — S(A)-in-
scatter is *inexpressible* on it (§1.2).

**V2 — Imposition map (pull b): canon provides NO phase-space→real-space
interior transduction map (measured honest negative, 2026-08-24); four
imposition-route candidates exist at sharply different receipt strengths;
EVERY route needs at least a hold-during-relaxation extension.** The
strongest phase-space-honoring primitive is the K4-side
`initialize_2_3_voltage_ansatz` (def-kn0t01-fenced); the strongest
end-to-end machinery is the Cosserat ω impose-and-relax pipeline — whose
own docstring disavows its (2,3) real-space mode as not-the-canonical-
electron. Full ranking + walk questions: `g1-walk-packet.md` (same
directory).

**V3 — Relaxation feasibility (pull c): exactly ONE end-to-end
impose-and-relax pipeline exists (`cosserat_field_3d`), and it is (i)
unconstrained — nothing holds an imposed texture during relaxation — and
(ii) gradient descent on an energy functional, which is a
`substrate-native-check`-flagged SM-default. What "relax the lattice"
means substrate-natively is itself unpinned — routed as a G1 walk
question.** Eigensolve machinery exists as the alternative stationary-state
route (`coupled_eigensolve`, fork-B), with the #415 canonical negative
adjacent (§3.3).

---

## §1 — Pull (a): the T2/Cosserat channel

### 1.1 What carries the transverse / micro-rotation sector (receipts)

| engine | what it carries | grading | receipt |
|---|---|---|---|
| `src/ave/topological/cosserat_field_3d.py` | u(r) + Cosserat ω(r) as independent fields; (2,3) and 0₁ ansatz seeders; gradient-descent relaxers; S readout | energy-functional saturation, `use_saturation=True` (default; `:881,948`); Op3 Γ=−1 reactive node-clamp at the moving front (`:977-1014`) | module docstring `:1-17`: *"relaxes to the ground state by gradient descent on the Cosserat energy functional (optionally with the Axiom-4 saturation kernel)"* |
| `src/ave/topological/k4_cosserat_coupling.py` (`CoupledK4Cosserat`) | K4 ⊗ Cosserat time-domain, unified leapfrog, Axiom-4 W_refl coupling (`L_c = (V²/V_SNAP²)·W_refl(u,ω)`, S1=D, zero new parameters) | via W_refl's 1/S² structure | header `:1-27`; capability-map row `engine-capability-map.md:227`: "CoupledK4Cosserat K4⊗Cosserat time-domain (band-structure host)" |
| `src/ave/topological/vacuum_engine.py` (VacuumEngine3D / loop_gap) | Cosserat ω carrier + 3 channels | softening bulk ρ̄ only | `engine-capability-map.md:55`: *"Its scalar is a **projection** `v_scalar_from_v_inc(V_inc)` … **no independent A1 field**, so it cannot host the stiffening cage"* |
| chiral srs vector-TLM (`chiral_lattice_vector.py`) | transverse-only vector waves on the ratified z=3 srs carrier; L0–L2 acceptance GREEN | frozen; transverse-only | `engine-capability-map.md:54`: *"A1a reports the honest carrier gap: `carried_dof==2` (transverse) vs `axiom_dof==6` (Cosserat)."* |
| `src/ave/core/fdtd_3d.py` / `fdtd_3d_jax.py` | vector EM (transverse) with both T2-sector grades | swing-ε + μ-circulation (§1.4) | §1.4 receipts |

### 1.2 Scatter/step primitives — and the amplitude-independence fact

The standalone-K4 TLM junction **cannot express a graded scatter at all**.
Verbatim (`engine-capability-map.md:368`, verified against
`k4_tlm.py:64,82,88-92,255,335,365,368` this session):

> "the 4-port scatter matrix is **amplitude-independent** —
> `build_scattering_matrix` (`src/ave/core/k4_tlm.py:64`) returns
> `S_ij = 0.5 − δ_ij` for the equal-admittance node junction *regardless*
> of `z_local` (the `2y/y_total = 2y/4y = ½` cancellation at `:88-92` …)
> So the S(A)-kernel-in-scatter pump the §B1 risk feared is
> **inexpressible** on this junction … routes the amplitude-dependent
> `z_strained` **only** into `z_local_field` (`:365`), which feeds the
> lossless Op3 bond-impedance mismatch in `_connect_all`, **never the
> scatter kernel**."

The one saturation-READING scatter operator in the tree is
`src/ave/solvers/vacuum_varactor_scatter.py` — the admittance-weighted
shunt-junction generalization `S_ij = 2Y_j/(Σ_k Y_k) − δ_ij` (header eq. 1)
with the **longitudinal μ-load** varactor map, verbatim (`:41-48`):

> "Bond admittance: `Y_bond = Y0 / sqrt(S(A_bond))` … As the core
> SATURATES (S -> 0): `Z_bond -> 0 => Gamma -> -1` (the mass cage, the
> Z->0 SHORT …). This is the LONGITUDINAL μ-LOAD … It is NOT the
> FORBIDDEN ε-load (`Z_eff = Z0/sqrt(S) -> inf, Gamma=+1`; the SCOPE
> ASSERTION / EPSILON-LOAD FORBID at `crystal_engine.py:466-468`)."

Consumers (grep, two patterns): `fork_b_saturation_tank.py` + three figure
/probe scripts — **no time-stepping engine loop consumes it**; it is
probe/eigensolve machinery.

**R40-B2a adjacency (guard 6, cite-don't-load-bear):** the operator's
phase-space reading carries the demotion stamp in-file
(`vacuum_varactor_scatter.py:72`: "[DEMOTED 2026-08-11 - R40-B2a: NEEDS
RE-DERIVATION, not dead …]"). Any P1/P2 reuse cites the stamp.

### 1.3 The transverse vertex scattering: UNVERIFIED (absence, stated as an absence)

Search report, not a corpus claim: (method 1) an API-map read of
`k4_tlm.py` (`grep -n "def \|class "`, then reading
`build_scattering_matrix` and the class methods) finds one shunt-junction
scatter and no series/transverse junction; (method 2) the capability map's
own carrier-gap row (`engine-capability-map.md:54`, `carried_dof==2` vs
`axiom_dof==6`) and the ε-load SCOPE ASSERTION
(`crystal_engine.py:471-474`: *"this is the μ-load branch ONLY. An ε-load
(`Z_eff=Z0/√S→∞`) would give Γ=+1 (the OPEN anti-trap). A future ε-load
import MUST NOT reuse this method's Z_eff form"*) corroborate that no
transverse-graded scatter/vertex primitive has been built or verified.
**No claim is made that none exists anywhere in the 18-repo workspace;
the claim is scoped to this tree at HEAD `a2551384` under these two
methods.**

### 1.4 The T2 grading kernels that DO exist (field engines)

- **Swing-ε (DECREASING, the transverse-T2 permittivity):**
  `fdtd_3d_jax.py:109-113` (read verbatim this session):
  `ratio_sq = (V_local/v_yield)**2` clipped, then
  `eps_base * jnp.sqrt(1.0 - ratio_sq)` — the `ε_eff = ε_0·S` kernel the
  rim-inversion leaf cites for `Z_wave = √(μ/ε) → ∞` (clm-zdual1).
- **μ-circulation (INCREASING relativistic inductor):**
  `fdtd_3d.py:339-343` (read verbatim): "Relativistic inductor:
  `μ_eff = mu_base / √(1 − A_I²)` — INCREASING", keyed on circulation
  `A_I` (Route-C canon). **The μ-at-core open sub-detail travels with any
  reuse** (`saturation-rim-inversion.md`, clm-zdual1 flag: "What `A_I`
  actually does AT the knot core is not pinned by canon").
- **Cosserat energy-functional saturation:**
  `cosserat_field_3d.py:652` `_update_saturation_kernels` +
  `:731` `_energy_density_saturated` (ω_yield / ε_yield kernels).

**Sector note (guard 5, no adjudication):** canon carries BOTH "charge
port Z_shear→0, Γ=−1 self-trap at V_yield"
(`resonant-lc-solitons.md:138`, RESOLVED=T2 Grant 2026-06-30) AND
"transverse-T2 permittivity ε_0·S→0 opens Z_wave→∞, Γ=+1" (INVARIANT-S2,
`resonant-lc-solitons.md:41`) — *"Orthogonal reactances, both |Γ|=1,
differing only in boundary phase."* The P1 prereg must declare which
reactance its Γ(A) locus reads; this report only inventories both.

---

## §2 — Pull (b): the imposition map

### 2.1 The governing constraint (measured, 2026-08-24)

The Class-C transduction pull's honest negative, verbatim
(`research/2026-08-24_smith-annulus_result.md:421-424`, post-adversarial-
verify, survived):

> "canon provides NO map that carries the annulus's radial PROFILE into
> any real-space observable. Under M/Q/J the entire interior trace is
> invisible; what survives is the wall's existence (→ M), the integer
> winding (→ Q), and time-averaged envelope strain (→ far field)."

Only the edges project. Any imposition route that writes phase-space
interior structure into real-space fields is therefore doing something
canon has no map for — the exact transduction hazard (guard 3) the G1
walk exists to adjudicate.

### 2.2 What the imposed object is per canon (the receipts each route must honor)

- The named test: *"Impose the `(2,3)` winding as a **boundary
  condition**, relax the lattice, and ask whether the relaxed core
  **rails `S → 0` at the center**"* (`saturation-rim-inversion.md:55`).
- The winding is a PHASE-SPACE object: *"The `(2,3)` 'trefoil' is the
  phase-space winding pattern, NOT a real-space trefoil knot"*
  (`electron-identification.md` §1 property 2, quoted at
  `saturation-rim-inversion.md` and `the-abandoned-interior.md:45`);
  real-space body = 0₁ unknot (INVARIANT-N1 / def-kn0t01 SOLID,
  `vocabulary-register.md:243` per `tlm_electron_soliton_eigenmode.py:18`).
- The winding is STATIC: *"the `(2,3)` winding does NOT dynamically
  'close' at any V — it is a **static Clifford-torus / Link texture**"*
  (`the-abandoned-interior.md:113`); charge = the static imposed Link
  (#416 two-natured ruling).
- α-agnostic (guard 8): *"α is not an invariant of the winding; imposing
  a specific α imposes more than the winding"*
  (`research/2026-08-24_frame-invariance-observer-walk_RECORD.md` §5).

### 2.3 The route candidates (inventory; ranking + physical pictures in the walk packet)

1. **K4-side phase-space voltage ansatz** —
   `initialize_2_3_voltage_ansatz`
   (`src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py:48-91`).
   Verbatim fence (`:57-67`): *"the real-space BODY built here is the
   power-law hedgehog SHELL … an UNKNOT (0₁) … The '(2,3)' enters ONLY as
   PHASE-SPACE winding diagnostics projected onto the real lattice … The
   Cartesian closed form below is the diagnostic shadow of that phase
   winding, not a body curve."* Encodes magnitude (hedgehog envelope) +
   phase (θ = 2φ + 3ψ port quadrature) + chirality (per-port projection
   weight p̂_k·t̂). Precedent consumers: `coupled_engine_eigenmode.py:148`,
   `motion_stability_bemf_longitudinal_probe.py:128`,
   `r8_self_consistent_orbit_hunt.py:129`. **It is a SEEDER (initial
   condition), not a held boundary condition, and writes `V_inc` only.**
2. **Cosserat ω-field real-space texture** —
   `cosserat_field_3d.initialize_2_3_torus_knot_sector` (alias, `:1268`)
   → `initialize_electron_2_3_sector` (`:1023`). Verbatim self-disavowal
   (`:1035-1046`): *"the original 'electron' naming is misleading … This
   seeder writes a (2,3) torus-knot ansatz onto Cosserat ω — which is
   testing (2,3)-torus-knot dynamics in REAL SPACE (a separate physics
   question …), NOT the canonical electron."* The canonical-electron
   seeder in the same module, `initialize_electron_unknot_sector`
   (`:1167`), carries *"NO (p,q) winding"* (`:1256`).
3. **Boundary-Link clamp** — impose Q = Link(∂Ω, F) per the canonical
   charge definition (`boundary-observables-m-q-j.md`, Q row:
   `Link(∂Ω, F_substrate) ∈ ℤ`). READER machinery exists
   (`charge_quantization.py` — Q_link via np.unwrap, "the genuine
   integer-quantized observable"; `boundary_invariants.py`;
   `k4_lattice_holonomy.py` — link-by-link SU(2) lift holonomy with
   anti-tautology scramble). **No CLAMP primitive exists — all three are
   observables, not constraints** (headers read this session).
4. **Coupled eigensolve with winding template** —
   `coupled_eigensolve.py` (#415 machine): Hermitian H on the native L_D
   stencil (fork-B `:169`: *"the stencil IS the connect-map"*), winding as
   fixed template ê_w. Canonical negative adjacent: #415 DOES-NOT-EXIST,
   re-scoped by `phase_space_winding.py:9-13`: *"tested the WRONG LOCUS
   three ways: real-space (vs phase-space), longitudinal-mass-V_snap (vs
   transverse-charge-V_yield), and STATIC eigenstate (vs dynamic ORBIT)"*.

**Anti-candidate (named to fence it):**
`fork_b_saturation_tank.saturated_core_strain_native` (`:120`) imposes
the Gaussian dilatation well A(r) — the saturated core POSIT ("PLANTED,
not self-formed", CP8). It imposes the *conclusion* (an S-profile), not
the winding — using it as the P2 imposition would beg the PROVE-branch
question. Legitimate only as P1 probe-precedent plumbing.

### 2.4 What #415 / #417 actually imposed (the epic's explicit ask)

- **#415** (`coupled_eigensolve.py`): a fixed real-space winding TEMPLATE
  ê_w carrying the (2,3) integer, with an LC amplitude block b_ω on it;
  free (unconstrained) eigensolve; the winding bled off the bound mode
  (rim-inversion leaf's summary; the both-sectors gate (d) is exactly the
  bleed detector).
- **#417** (`phase_space_winding.py`): nothing held — SEEDED
  (`seed_A1_sech + seed_winding`), then unitary Crank–Nicolson evolution;
  the (2,3) read as Clifford-torus angles φ = arg(Σ a_A1),
  ψ = arg(Σ b_ω), θ = 2φ + 3ψ; carrier ratio read (−5,−5) = (1,1)-class.
- **Fork-B precedent**: imposed the scalar A1 amplitude PROFILE (not a
  winding), then eigensolved L_D = Bᵀdiag(1/S)B on the connect-map.

None of the three ever HELD a winding as a constraint during a
relaxation. **The imposition mode the named test asks for has no
precedent run in this tree** — stated as an absence (methods: header +
body reads of all three modules, this session).

---

## §3 — Pull (c): relaxation feasibility

### 3.1 What exists

- **`cosserat_field_3d.relax_to_ground_state` (`:1686`)** — gradient
  descent with backtracking-lr acceptance on the (optionally saturated)
  Cosserat energy; `track_topology_every` records (E, R, r, c) so
  *"the unwinding dynamics are visible in post-hoc analysis"* (`:1697`).
  **Unconstrained**: the body applies `relax_step` to the full (u, ω)
  state; no Dirichlet mask, no winding hold (grep clamp/frozen/pin +
  body read — the only clamp is the Op3 Γ=−1 moving-front node-clamp
  `:977-1014`, a wall spring: *"CP1: the reactive (energy-storing)
  node-clamp, NOT gradient descent"* — checkpoint-10-compliant, but it
  clamps the WALL, not a texture).
- **`cosserat_field_3d.relax_s11` (`:1550`)** — same descent, minimizing
  Σ|Γ|² instead of energy.
- **Eigensolve stationary-state routes** — `coupled_eigensolve.py`
  (Hermitian, native stencil, both-sectors bleed gate);
  `fork_b_saturation_tank` / `fork_b_near_saturation` (posit + L_D
  eigensolve); `radial_eigenvalue.py` (continuum radial).
- **Unitary evolution + time-average** — `CoupledK4Cosserat.step()`
  (Crank–Nicolson/Cayley in the S3 lineage) conserves ‖a‖²+‖b‖² exactly;
  a "relaxed state" read as a time-average is available without any
  dissipation.

### 3.2 The substrate-native tension (flagged, not adjudicated)

The only in-tree relaxer is **gradient descent on an energy functional**
— named by `substrate-native-check` as an SM/QED default to police
("Lagrangian minimization, gradient descent, … energy-basin landscapes").
Simultaneously, Ax3-losslessness makes *dissipative* relaxation un-native
as physics (acceptable only as a declared numerical device). The corpus
does not pin which of {eigensolve / damped-native evolution / unitary
time-average / energy-gradient flow} realizes the named test's "relax the
lattice". **Routed to the G1 walk (packet Q2) — the null's meaning
changes with the choice.**

### 3.3 Guard-2 config adjacency (challenge-canonical-negative)

The named test's own guard travels verbatim
(`saturation-rim-inversion.md:57`): *"no free-precursor genesis, no
`dt→0` pump ramp, impose-and-relax only"* — grep the CONFIG. All §3.1
routes satisfy the no-pump clause structurally (descent/eigensolve/
unitary have no drive term); the #415 non-reconstruction argument must be
made config-level in the P2 prereg (the distinguishing config bit: #415
was an UNCONSTRAINED solve of a seeded template; the named test HOLDS the
winding as a boundary condition — a different operator problem).

### 3.4 Structural-null trap, transverse analog (guard 4 — P0's naming duty)

The in-tree longitudinal receipt (`vacuum_varactor_scatter.py:52-57`,
verbatim): *"A per-NODE-UNIFORM admittance CANCELS at the shunt junction:
in (1) a common factor Y in every Y_j cancels in 2Y_j/Σ_kY_k, reducing
back to (2/n)J − I REGARDLESS of S."* **Transverse-analog candidates
identified by this inventory (to be pinned in the P1/P2 preregs):**
(i) in the Cosserat energy functional only GRADIENTS of ω enter
(`_compute_strain :175`, `_compute_curvature :189`) — a spatially
common-mode component of an imposed ω texture contributes zero curvature
energy and relaxes invisibly; (ii) per the frame-invariance walk §2, a
uniform frame change / common-mode phase is physically inert — an
imposition whose non-trivial content is common-mode (e.g. a global tube
phase α) tests nothing, and a null obtained through it is an artifact.
Both are candidates, named-not-verified; the preregs must demonstrate the
imposed texture's content is differential (per-bond / per-port varying),
exactly as the Class-C prereg's per-bond discipline did.

---

## §4 — EXTENSION-NEEDED (minimal, named)

1. **Texture-hold constraint** — a Dirichlet/projection hold of the
   imposed winding during relaxation (domain-boundary clamp or interior
   constraint). No engine has one; all imposers are seeders (§2.4, §3.1).
2. **(V_inc, V_ref) pair-complete imposition** — the voltage ansatz
   writes `V_inc` only; the Clifford-torus object lives on the pair
   (Γ = V_ref/V_inc quotient, smith-annulus §6 route 2).
3. **Transverse ε-load graded scatter** (P1, not necessarily P2) — the
   Z = Z0/√S, Γ→+1 variant of the admittance-weighted junction, built
   WITHOUT reusing `gamma_bulk`'s Z_eff form (SCOPE ASSERTION,
   `crystal_engine.py:471-474`) and honoring the
   `universal_dynamic_impedance` Z-convention guard; R40-B2a stamps
   travel.
4. **α-family sweep harness** (guard 8) — sweep the imposition
   representative (tube phase) and gate on class-invariance of the
   verdict; no harness exists.
5. **Native relaxation mode, if Grant rules out gradient flow** (walk
   Q2) — damped-native or time-averaged-unitary relaxation on the coupled
   engine.

## §5 — What P0 did NOT find (absences, method-scoped)

- No held-winding relaxation precedent anywhere in `src/` (two grep
  patterns + body reads of the four candidate modules).
- No transverse/series-junction scatter primitive in `k4_tlm.py` or
  `src/ave/solvers/` (API-map read + capability-map corroboration, §1.3).
- No clamp/constraint form of the M/Q/J machinery — readers only (§2.3
  route 3).
- No phase-space→real-space interior map in canon — a MEASURED negative,
  not merely un-found (§2.1).
