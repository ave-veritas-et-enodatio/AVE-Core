# Stage-1.5 Pre-Reg — α-FREE two-sector convergence engine, winding-emergence lane

**2026-06-16 · Rule-11 FREEZE · banked BEFORE any build · inherits the
electron-existence discrimination pre-reg's 4-part success criterion.**

**Branch:** `analysis/2026-06-16-boundary-mqj-stage15-alphafree-emergence`
(off `origin/analysis/2026-06-16-boundary-mqj-selftrap-integrator-zwall`).
**Worktree-isolated. Do NOT merge — main is PROTECTED.**

---

## 0 — Inherited frozen targets (NOT re-derived here)

- **Success criterion** = `reconciliation-handoffs/2026-06-16_electron-existence-discrimination-prereg.md` §"Pre-registered success criterion for the Stage-1.5+ build" (4 parts, verbatim below).
- **The gap this closes** = `research/2026-06-07_electron-genesis-observer-bridge-prereg.md:30,117`
  ("inserting α converts it to a calibration model"; "no current engine
  simultaneously carries the bound-state dynamics AND the bond-phasor/reactance
  observer"). This was the OBSERVER_ARCHITECTURE_GAP verdict.
- **The current-suite gap** = `research/2026-06-08_electron-genesis-finish-adjudication.md:11`
  — `electron_genesis_finish.py` **plants** `initialize_electron_unknot_sector(R=0.5, r=0.25)`
  (a finished `0_1` torus ansatz) + a `seed_sech_v_inc` blob and runs **one-way**
  Cosserat→K4 (`disable_cosserat_lc_force=True`). It measures B2 planted-persistence,
  NOT emergent formation. The unknot circulation is **seeded, not demonstrated**.
- **The Stage-1 result on this branch** (`e0d240e7`): the coupled `VacuumEngine3D`
  gate returned **`c_eff(V)-STRUCTURAL-GAP`** — the wall forms (`n_sat=207`, A²_cos=5.5)
  but Z does **NOT** collapse to 0 (`Z_wall_post_median=1.003`, floor=0.847). It
  measures the **transverse** Meissner `Z_eff=√(S_μ/S_ε)≈Z₀` (achromatic softening
  proxy), NOT the **longitudinal** A1 stiffening tank `Z_tank=√(L/C_comp)→0`.
  Confirms `engine-capability-map.md:45,79`: `VacuumEngine3D` has **no independent
  A1 field** — its scalar is the read-only projection `v_scalar_from_v_inc(V_inc)`
  (`cross_sector_coupling.py:226`). **THIS is the structural gap Stage-1.5 must close.**

## 0.1 — Known-positive numerical floor (inherited, NOT re-litigated)

Per the Stage-1 bucket-1 gate: the **standalone `MasterEquationFDTD` v14 cage HELD**
(`instrument_adequate=True`), with its longitudinal `Z_long=√S → 0.376` toward 0.
**This is the numerical-adequacy reference for Stage-1.5.** If a *coupled* run blows
up where the *cage-alone* held, the failure localizes to the cross-sector / two-grid
coupling — it is **physics, not the integrator**.

**Correction folded (Stage-1 result panel `wvvx6y6zb`):** the `Z_long=0.376` floor is
the **`A_cap=0.99` numerical CLAMP** floor (`master_equation_fdtd.py:68` `A_cap`),
NOT an asymptotic Z→0. The asymptote requires `A→1`; the clamp halts the strain at
0.99, so `S_min`-clamped `Z_long=√S_clamp`. Reported as a clamp floor, not a limit.

---

## 1 — THE SUCCESS CRITERION (pre-registered; magnitudes NOT substituted)

The multi-week two-grid build is **worth its cost ONLY IF scoped to α-free emergence**.
**SUCCESS** (all four; verbatim from the discrimination pre-reg §"success criterion"):

1. The **(2,3) winding + Γ=−1 confinement SELF-FORM from generic/precursor IC** —
   NO planted (2,3). (substrate-native-check **CP8**.)
2. **WITHOUT α inserted anywhere** (α-free) — inserting α = a calibration model,
   NOT emergence.
3. The **α-free Q EMERGES** (~137 falls out WITHOUT being told) — the form-chord readout.
4. **Z→0 longitudinal confinement is NECESSARY but NOT SUFFICIENT** — it gates
   trap-FORMATION, not emergence.

**Reading m_e / e / ℏ/2 off the region is NOT the success criterion** — m_e is a
calibration INPUT (`ℓ_node ≡ ℏ/m_e c`; `electron-identification.md:50,64`), |Q|=1 is
generic-for-any-soliton, and the α=𝓜+𝓙+𝓠 magnitude decomposition is canonically
**Class-B / (R·r)-collinear / ECHO** (`ch8-alpha-golden-torus.md:135,148,150,152`).
**Magnitudes RE-DERIVE the echo. The chord is FORM-EMERGENCE.**

## 1.1 — Meta-frame (why the build is worth it)

FORM-deriving / VALUE-importing at the keystone: the electron's **FORM
self-generating IS the chord** (the deepest one — the foundational object
self-assembles); its **VALUE** (m_e, α=137) is **echo** (input + already-adjudicated
per the α-keystone-echo ruling).

---

## 2 — Consistency-vs-emergence classification (fired BEFORE the build)

Per `consistency-vs-emergence`, each Stage-1.5 readout is pre-classified:

| Readout | Class | Why |
|---|---|---|
| (2,3) winding self-forms from generic IC (no plant) | **EMERGENCE** | the chord; nothing tells the seed to wind |
| Γ=−1 confinement self-forms | **EMERGENCE** (gated by Z→0, necessary-not-sufficient) | trap-FORMATION, not value |
| α-free Q ≈ 137 emerges without being told | **EMERGENCE** (the form-chord readout) | no α in dynamics → if 137 appears it is selected, not inserted |
| Longitudinal Z_tank → 0 at wall | **MANIFESTATION** (Axiom-4 stiffening) | necessary gate; NOT sufficient |
| m_e, e, ℏ/2 read off the region | **ECHO** (definitional / generic / Class-B) | DO NOT headline; calibration inputs |
| α=𝓜+𝓙+𝓠 magnitude decomposition | **ECHO** (Class-B, (R·r)-collinear) | `ch8:135,148,150,152` — re-derives the echo |

**α-free is load-bearing.** Any path that imports `ALPHA` / `KAPPA_CHIRAL` /
`V_yield=√α·V_snap` / `delta_lock_fraction=α` into the **dynamics** is a CALIBRATION
MODEL, not emergence — flag it and route around it. Per the substrate audit:
`vacuum_engine.py:180-181,427,1278` (`_V_YIELD_FRAC=√α`, `_REGIME_I_BOUND_A2=2α`,
`V_YIELD=√α·V_SNAP`, `delta_lock_fraction=α`) are α-bearing → those normalization
paths are OFF the emergence dynamics. `master_equation_fdtd.py` + `crystal_engine.py`
+ `cosserat_field_3d.py` are α-FREE (V_yield=1.0 natural unit, `omega_yield=π`,
`epsilon_yield=1`) → the cage + winding sectors are built on THOSE. (A canonical-source
GATE may *assert* `ALPHA==CODATA` as provenance, but α never enters an update equation.)

---

## 3 — Phase-space coordinate discipline (fired BEFORE the build)

Per `phase-space-coordinate-check` (A46): the corpus chord-claims live in
**impedance/phase-space coordinates** — Z (impedance plane), Γ (reflection),
Q (dimensionless self-impedance Q-factor), winding number (topological).
The Stage-1.5 readouts are therefore measured in **matching coordinates**:

- **Z_tank = √(L/C_comp)** at the wall (longitudinal A1 tank impedance), NOT a
  lattice-Cartesian field magnitude. → 0 = stiffening confinement gate.
- **Q** = dimensionless self-impedance Q-factor of the trapped mode (energy-stored /
  energy-leaked-per-cycle at the Γ=−1 boundary), NOT a real-space φ² profile.
- **Winding** = the (2,3) topological linking/twist integer of the Cosserat
  micro-rotation field around the trap (phase-space topology), NOT a Cartesian count.

A real-space φ² profile compared against a phase-space φ² prediction is
uninformative (A46) — so the emergence read is in Z / Γ / Q / winding-integer space.

---

## 4 — The engine to build (α-free two-sector convergence) + WHY two sectors

**Capability-map §3.1 (canon-derived firewall): irrotational A1 cage ↮ winding.**
`∇×∇V ≡ 0` — the A1 scalar c_eff(V) cage CANNOT carry the winding. They MUST be
**two coupled sectors**:

- **Sector A — the A1 cage (continuum-scalar FDTD):** an INDEPENDENT, integrated,
  α-free scalar longitudinal field `V(r,t)` with the Master-Equation stiffening
  kernel `∂²V/∂t² = c_eff²(V)·∇²V`, `c_eff(V) = c₀·(1−A²)^(−¼) → ∞`,
  `A = |V|/V_yield` with **V_yield = 1.0 (generic natural unit, NOT √α·V_snap)`.
  Ported from `master_equation_fdtd.py:13,148-151`. This is the longitudinal Z→0
  stiffening tank the projection `v_scalar_from_v_inc` could NOT host. **This
  replaces the read-only projection with a real integrated field.**

- **Sector B — the winding (K4-tetrahedral Cosserat ω):** the VECTOR
  `CosseratField3D` (`cosserat_field_3d.py:766`) — `(u, omega)` micro-rotation on
  the K4 diamond A/B sublattice, `omega_yield=π`, `k_hopf=π/3` (the (2,3)/Q_H=6
  anchor). α-FREE. The vector ω is what can carry the winding the scalar cannot.
  (NOTE: the existing `cosserat_master_equation_fdtd.py` couples a **scalar** ω —
  that scalar CANNOT host the (2,3) vector winding; Stage-1.5 needs the **vector**
  Cosserat sector. This is a NEW coupling, not a reuse of the scalar-ω engine.)

- **The two-grid reconciliation (THE CORE MULTI-WEEK CHALLENGE):** continuum-scalar
  FDTD grid (the c_eff(V) cage) ⊗ K4-tetrahedral grid (the Cosserat ω) couple
  through a **shared front** — the A1 strain field A²_V(r) modulates the Cosserat
  moduli/front, and the Cosserat micro-rotation energy density sources the A1 field's
  local amplitude. MINUS the chiral-srs grid (chirality parked = sign-only;
  magnitudes achiral-OK). Expect this to be the hard part; if it hits a genuine
  wall, REPORT the obstruction precisely — do NOT force a result.

- **The precursor seed (CP8):** a **generic transverse ω-photon with NO planted
  (2,3)** — let the dynamics self-form the winding + confinement. Seed the
  GENERATIVE precursor, do NOT plant the finished electron.

**CP10:** Γ=−1 / Z→0 rendered as an Op17-bounded BOUNDARY CONDITION, not a bulk
force → no |ω| blow-up. The bulk V→ω W_refl gradient force (the documented runaway
channel) is OFF this path.

---

## 5 — Build-order DAG (staged, one validated layer per commit; §5 cap-map)

Per CP8 (grow one layer at a time; each validated before the next, so a failure
localizes to ONE DOF). **Big-bang assembly rejected.**

- **Layer (a) — α-free A1 c_eff(V) field self-traps on its own grid.**
  Independent integrated scalar field; seed a sub-yield blob; show the longitudinal
  `Z_tank = √S → 0` stiffening at the saturated core (necessary gate). Validate
  against the known-positive floor (§0.1). VALIDATED ⇒ commit.
- **Layer (b) — couple Sector A ⊗ Sector B; coupled system stable (no blow-up).**
  Shared-front coupling. Full-Hamiltonian ledger flat/decaying (passive); |ω|
  bounded; coupled-stability validated against the cage-alone floor. VALIDATED ⇒ commit.
- **Layer (c) — seed generic precursor, run α-FREE; emergence probe.**
  Observe whether the (2,3) winding + Γ=−1 SELF-FORM (no planted (2,3)) and whether
  an α-free Q emerges. This is the chord read. Report WHICH layer reached + what each
  showed.

---

## 6 — Witnesses + corrections (Empirical-driver discipline, Rule 10)

- **Full-Hamiltonian witness** `total_hamiltonian()` (`k4_cosserat_coupling.py:927-929`),
  NOT `sum(ω²)`. KEEP-BOTH the engine's own `impedance_hamiltonian()`.
- **|ω| trajectory** (C-state) AND **|ω̇|** (L-state) — the reactance pair recorded at
  every sample over the window (A-Rule 10): a snapshot of ω alone can't distinguish a
  static config from an oscillator caught at peak.
- **Long-window persistence** ≥10 Compton periods (NOT a truncated short window);
  the run N is **labeled explicitly** (Stage-1 headline was N=18 fast-artifact, not the
  N=24 default — correction 1).
- **PML cell exclusion** (A-Rule 10 corollary): top-K field-density / saturated-cell
  extractions filter `pml ≤ {i,j,k} ≤ N−pml−1` before any argpartition. PML cells are
  frozen-absorbing artifact.
- **Density-peak sampling**, not centroid: sample at energy-density peaks (top-K |field|²),
  not centroid+offset (the centroid of a shell is the empty middle).
- **The 4 Stage-1 result-doc corrections** (panel `wvvx6y6zb`), folded:
  1. label run N explicitly (Stage-1 headline N=18, not N=24 default);
  2. cite the **long-window** persistence (≥10P) run, not a truncated short window;
  3. emit the **S_μ/S_ε split** AND the **longitudinal Z_tank=√(L/C_comp)** at the
     wall in the JSON;
  4. annotate that the known-positive `Z_long=0.376` is the **A_cap=0.99 numerical
     CLAMP** floor, not asymptotic Z→0.

---

## 7 — Adjudication bins (frozen; NOT dropped post-hoc — Rule 11; honest closure — Rule 11)

The Stage-1.5 verdict reports WHICH build layer was reached and bins the emergence
read (only if layer (c) runs):

- **LAYER-A-ONLY** — α-free A1 field self-traps (Z_tank→0) standalone; coupling not
  yet stable. Honest progress (a GOOD report per the brief).
- **LAYER-B-STABLE** — two-grid coupling stable (no blow-up, ledger flat, |ω| bounded);
  emergence probe not yet run. Honest progress.
- **TWO-GRID-WALL** — the two-grid reconciliation hit a genuine obstruction; the
  obstruction is reported precisely (NOT papered over). Honest negative.
- **EMERGENCE-NEGATIVE** — layer (c) ran; the (2,3) winding did NOT self-form, OR Z→0
  did not gate, OR no α-free Q emerged. Clean negative; mechanism named; per Rule 11
  this is the discipline working — record the falsification, do NOT debug toward a rescue.
- **EMERGENCE-CANDIDATE** — layer (c) ran; (2,3) winding + Γ=−1 SELF-FORMED from
  generic IC (no plant) AND an α-free Q emerged. Requires auditor review + Grant
  adjudication of chord-vs-echo. **The implementer does NOT conclude chord/echo —
  the orchestrator adjudicates** (scope guard).

**A forced magnitude readout is NOT a pass.** Reading m_e/e/ℏ/2 off the region is
ECHO and does NOT satisfy the criterion. "I reached layer (b), coupling stable,
emergence probe not yet run" is a GOOD report.

---

## 8 — Scope guards (frozen)

- Do NOT read m_e/e/ℏ/2 as success (echo).
- Do NOT insert α into dynamics (calibration model).
- Do NOT touch R10 anhysteretic/remanence (separate retention wall, parked).
- Do NOT compute rigorous 𝓠=Link / 𝓙=Wind yet unless emergence is reached (Stage 2).
- Do NOT conclude chord/echo (orchestrator adjudicates).
- Do NOT merge. Do NOT draft Ax-5 candidates (per A44 missing-axiom-vs-engine-bug).
- Chirality parked (sign-only); magnitudes achiral-OK → no chiral-srs grid this stage.

---

## 9 — Cross-refs

- Discrimination pre-reg: `reconciliation-handoffs/2026-06-16_electron-existence-discrimination-prereg.md`
- Emergence-bridge prereg: `research/2026-06-07_electron-genesis-observer-bridge-prereg.md`
- Planted-ansatz finding: `research/2026-06-08_electron-genesis-finish-adjudication.md`
- Capability map (§3.1, §4, §5): `manuscript/ave-kb/common/engine-capability-map.md`
- Two-engine architecture: `manuscript/ave-kb/common/two-engine-architecture-a027.md`
- α-echo anchor (Class-B): `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md:135,148,150,152`
- Stage-1 gate driver + result: `src/scripts/vol_1_foundations/boundary_mqj_selftrap_zwall_gate.py`, commit `e0d240e7`
