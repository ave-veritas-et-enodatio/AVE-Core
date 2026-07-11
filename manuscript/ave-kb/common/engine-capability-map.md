[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "audit-synthesis of engine DOF-coverage + a forward design proposal. The capability matrix is verified-state (every cell audit-grounded against a file:line / PR anchor); the three incompatibilities are canon-derived; the substrate-complete engine is NOT built — design-class. Generalizes two-engine-architecture-a027.md from N engines to the one-engine convergence target. Hosts no new derived numbers."
-->

# Engine capability map — the 7 DOF of a complete electron, and which engine hosts what

> **Routing + synthesis aid (no-claim).** The N-engine generalization of [`two-engine-architecture-a027.md`](two-engine-architecture-a027.md) (K4-TLM + Master-Equation). **Class split (load-bearing honesty):**
> - **§2 capability matrix = VERIFIED-STATE** — every cell grounded against a file:line / PR anchor (see [`figures/engine_capability_matrix.yaml`](figures/engine_capability_matrix.yaml)).
> - **§3 incompatibilities = CANON-DERIVED** — the firewalls *are* the spec.
> - **§4 substrate-complete engine = DESIGN PROPOSAL** — hypothesis-class, **not a built or validated engine.** Do not read §4 as describing something that exists.

---

## §1 — The seven DOF a complete electron needs simultaneously

A complete, stable, moving, charged electron requires all seven at once. No single engine carries more than one or two; that gap is the whole point of this map.

> **🔴 LOCALIZATION-MECHANISM REFRAME (2026-06-24; Rule 12 — body preserved).** The Stage-2 native-cage make-or-break ([`research/2026-06-24_engine-stage2-native-cage_result.md`](../../../research/2026-06-24_engine-stage2-native-cage_result.md)) returned energy-certified **MODE-III DISPERSE**: a seeded sech does NOT self-focus into a persistent bound core on the native K4 stencil (WITH c_eff(V)). So the **bulk-interior self-trap is a Cartesian-grid artifact (RULED OUT)** — rest-mass localization is **topological/coupling (the (2,3) winding + H_couple pin the A1 core) + the Γ=−1 boundary cavity**, NOT an autonomous bulk self-focusing well. **mass = A1 (#260) is UNTOUCHED** — only WHAT LOCALIZES the A1 core changes. Read the "$c_{\text{eff}}\to\infty$ self-creates the cage" phrasing below as the cage-as-BOUNDARY (the surviving route), not the cage-as-bulk-self-focus (the falsified route).
>
> 🔴 **LOCALIZER RELABEL (2026-06-24 second pass, Rule 12 — supersedes "the (2,3) winding + H_couple pin the A1 core" above; body preserved).** The "winding + H_couple pin the A1 core" attribution predates the **S3 cavity-pinning result (DISPERSE-FALSIFIED) + the coupled eigensolve (#415)** and the **phase-space coupling-winding BREAK (#417)** — both internal dynamical loci now NEGATIVE: winding + H_couple does **NOT** pin the dispersing core (the phase-space orbit carries the carrier ratio, not the (2,3)). The surviving **localizer is the Γ=−1 boundary CAVITY-eigenmode** (fork-b A1 mass cavity EXISTS); the **(2,3) winding RIDES the cage as STATIC charge** (`Link`, un-walked-back), it does not pin the mass. **mass = A1 (#260) UNTOUCHED.** See the epic summary `research/2026-06-24_engine-reroute-epic-summary.md`.

> 🟡 **EVIDENTIARY-EXPOSURE POINTER (2026-07-03, verdict-exposure sweep — status-demotion, NOT retraction).** The Stage-2 / S3 / #415 / #417 evidence the two reframe banners above lean on is now **HIGH/MEDIUM-exposed** (diamond `TETRA_OFFSETS` `L_D` nullspace-heavy / sublattice-decoupled; DISPERSE positive control on the *Cartesian* engine; #417 (2,3) verdict on an achiral host) and **UNDER RE-ADJUDICATION**. This affects only the empirical basis for *which localizer wins*; **mass = A1 (#260) untouched.** See [`research/2026-07-03_engine-verdict-exposure-sweep_result.md`](../../../research/2026-07-03_engine-verdict-exposure-sweep_result.md).

| DOF | Why the electron needs it |
|---|---|
| **A1 mass-cage** (stiffening $c_{\text{eff}}\to\infty$) | rest mass = the self-trapped longitudinal-bulk wall; $c_{\text{eff}}\to\infty$ at the saturated core self-creates the $\Gamma=-1$ TIR cage 🔴 *(2026-06-24: the BULK self-focus reading is the FALSIFIED route — see the reframe banner above; the surviving localizer is the **Γ=−1 boundary CAVITY-eigenmode** — NOT the winding. Second pass (#415 + #417 both NEGATIVE): the (2,3) winding does NOT pin the A1 core, it RIDES the cage as static charge (Link); mass = A1 untouched)* |
| **Cosserat winding** (charge) | charge = the $(2,3)$ Beltrami micro-rotation helicity the cage must carry |
| **3-channel coupling** (EM / shear / bulk) | the electron lives across all three impedance channels; a complete engine must carry *and couple* them |
| **constitutive loop** (remanence) | mass persists at zero drive (ferrite $B_r$ analogue); the canonical kernel is anhysteretic, so this is the open R10 gap |
| **boost-covariance** (motion) | a moving electron must Lorentz-transform; transport/boost is absent from every engine |
| **chiral grid** (srs handedness) | structural parity is set by the $I4_1 32$ srs grid; a cubic grid is achiral and cannot carry it |
| **node-creation** (genesis) | pair production / lattice-node birth; no engine hosts it (cosmological front) |

---

## §2 — The capability matrix (verified-state)

![Engine × DOF capability map](figures/engine_capability_map.png)

> **Living tracker.** The figure renders from [`figures/engine_capability_matrix.yaml`](figures/engine_capability_matrix.yaml) via `figures/engine_capability_map.py`. Each cell carries its anchor in the YAML; a status change (e.g. a cage-test PASS, or a loop that stops being imposed) is a **one-line YAML edit + re-render**.

**What each engine uniquely provides — and the columns no engine fills:**

- **Master Equation FDTD** (`src/ave/core/master_equation_fdtd.py`) — the **only** engine with the **A1 cage**: `c_eff(V)=c0·(1−A²)^(−1/4)→∞`, v14 Mode I PASS (`:13,148-151`; `two-engine-architecture-a027.md:19,32-37`) — 🔴 *(2026-06-24: this Mode-I PASS is **Cartesian-only = continuum cross-check reference**; the **native-stencil self-trap is FALSIFIED (Mode-III)**, [`research/2026-06-24_engine-stage2-native-cage_result.md`](../../../research/2026-06-24_engine-stage2-native-cage_result.md). NOT deleted — it is the valid continuum cross-check the native run must recover, `2026-06-23_full-engine-pathway.md`. The bulk self-trap is a Cartesian artifact; mass = A1 untouched.)*. Scalar ⇒ irrotational ⇒ **no winding** (`cavitation_flow.py:12`).
- **crystal_engine / graft-v2..v4** (`src/ave/core/crystal_engine.py`) — the cage **with the transverse-shear→longitudinal-bulk conversion** + gyrotropic coupling (`:9,224`). Cage **sign** confirmed; **magnitude is apparatus/exponent-bound** — see §6.
- **cavitation_flow** (`src/ave/core/cavitation_flow.py`) — the **only** engine that hosts **circulation** (vector velocity + Kelvin-conserved circulation, `:16-17,33`). It is explicitly *a fourth object — NOT the $\Gamma=-1$ cage* (`:28`).
- **chiral srs lattice / v9** — the **only** engine with the **chiral grid** (srs $I4_1 32$). Optical-activity facts (signed / enantiomorph-odd / diamond-null / writhe-sourced / lossless reciprocal gyrator) confirmed [#195]. **Magnitude $\pm75.46°$/unit DEMOTED** (PR #374): that figure is an `ETA_ROT_PER_WRITHE=1.0` engineering decree (`chiral_lattice_vector.py:27,93`), NOT derived transport. The substrate-DERIVED bulk g₀ (writhe-aware vector-TLM) **converges to the 4₁ screw pitch** ($\mp2.21589$ rad / lattice-z-unit, signed, L-independent, diamond-null); k→0 continuum / physical-rad-m mapping PENDING (literal value ~40 OOM over the cosmic bound). Frozen; transverse-only. **Acceptance-suite status (2026-06-16/17):** the ground-up L0–L2 suite (`src/tests/engine_acceptance/`) runs on this grid and is GREEN — it proves the srs medium is a **valid medium** (lossless transverse propagation T1.1, dispersionless band T1.2, transversality T1.3, causality T1.4, lossless chiral rotation A1b/T1.5, achromatic SYM lensing T2.2, α-invariance T2.4). The chirality is now confirmed **lossless with rotation ON** (Axiom-3) after the copy-first view-aliasing fix (`chiral_lattice_vector.py:49-58`), not just structurally present. **The suite forces ZERO chords** — the chord-DOFs in §2 (`a1_cage`, `winding`, `loop`, `boost`, `node_creation`) are NOT advanced by it (they live at the unbuilt L3–L5 rungs); medium-validity is a different axis than chord-DOF coverage, so **no matrix cell flips on this arc**. A1a reports the honest carrier gap: `carried_dof==2` (transverse) vs `axiom_dof==6` (Cosserat).
- **VacuumEngine3D / loop_gap_harness** (`src/ave/topological/vacuum_engine.py`) — Cosserat ω carrier + 3-channel (incl. *softening* bulk ρ̄). Its scalar is a **projection** `v_scalar_from_v_inc(V_inc)` (def `cross_sector_coupling.py:226`, used at `k4_cosserat_coupling.py:499`) — **no independent A1 field**, so it cannot host the stiffening cage.
- **SPICE-CVR cell** — circuit-domain constitutive law; ε-varactor present, μ-inductor + bulk absent from the `.lib`; its loop is **imposed (IMPOSED-LATCH)**, not emergent (`spice_cvr_loop.py:224`; [#215] retraction `575ed12d`).
- **Empty columns (no engine):** **constitutive loop**, **boost-covariance**, **node-creation** — these are the genuine missing physics (§6).

Full per-cell status + anchors: [`figures/engine_capability_matrix.yaml`](figures/engine_capability_matrix.yaml).

---

## §3 — The three mutual-incompatibility findings (canon-derived — the firewalls ARE the spec)

The engines do not merely *happen* to split the DOF — three of the splits are **forced** by canon. The incompatibilities define what a complete engine must reconcile.

1. **Irrotational ↮ winding.** The stiffening-cage engine is a scalar potential, and `∇×∇V ≡ 0` — *irrotational, so it cannot host circulation* (`cavitation_flow.py:10-19`, verbatim). The cage engine therefore cannot carry the Cosserat winding; the winding needs a vector/rotational sector.
2. **Cubic ↮ self-trap, and cubic ↮ chirality.** The K4-TLM cubic grid implements $Z(V)$ but **not** $c_{\text{eff}}(V)$ — *"without c_eff(V) the wave cannot self-trap at A→1, which is why v14a-e all returned Mode III"* (`master_equation_fdtd.py:15-18`; `two-engine-architecture-a027.md:24`). A cubic grid is also achiral. So the cubic engines can neither self-trap the cage **nor** carry structural handedness — the winding's handedness needs the srs grid (v9). 🔴 *(2026-06-24: the "without c_eff(V) ⇒ Mode III" escape-hatch — i.e. that ADDING c_eff(V) would recover the self-trap — is **REFUTED**: the native K4 stencil **WITH** c_eff(V) STILL returned Mode-III DISPERSE, energy-certified ([`research/2026-06-24_engine-stage2-native-cage_result.md`](../../../research/2026-06-24_engine-stage2-native-cage_result.md)). So Mode-III is the **substrate's verdict, not a missing-modulation artifact** — the bulk self-trap is a Cartesian-grid artifact (RULED OUT); boundary/topological localization STANDS; mass = A1 untouched.)*
3. **Anhysteretic ↮ loop.** The canonical kernel $S(A)=\sqrt{1-A^2}$ is anhysteretic — zero enclosed loop area ⇒ **no remanence** (`loop-gap-electron-resonator-closure-doctrine.md:18`). Every attempt to get retention imposes a latch by hand (the [#215] IMPOSED-LATCH). The loop is the deepest open gap (R10).

**Underlying firewall — stiffening vs softening.** The A1 dilatation's *own* wall is the **stiffening** branch (`c_eff→∞`, the BULK-TRAP, `crystal_engine.py:18-20`). The `bulk_rarefaction_sector` / `cavitation_flow` pocket is the **softening** branch (`c_bulk→0` at ρ̄_cav) — canon flags it *"a FOURTH object — NOT Γ=−1"* (`cavitation_flow.py:28`). The electron cage is the **stiffening** wall; the softening pocket is a distinct (candidate) object. Conflating them is the firewall violation.

---

## §4 — Substrate-complete-engine spec (DESIGN PROPOSAL — hypothesis/forward class)

> **This engine does not exist.** It is the convergence target the incompatibilities define — a forward spec, not a validated result.

> **🔴 2026-06-16 STAGE-1 VERIFICATION + KEYSTONE FINDINGS (Rule 12 — §1–§5 PRESERVED; source: keystone-lane Stage-1 gate + chord/echo audit workflow `wenqg7x94` + INVARIANT-S2 Q1=B).**
> - **Bucket-2 is now EMPIRICALLY VERIFIED, not just inferred:** the Stage-1 gate measured the coupled `VacuumEngine3D` wall at the **transverse-Meissner Z≈Z₀** (the softening proxy), while the standalone `c_eff(V)` cage gives **Z_long→0.376·Z₀ and HELD** (solver adequate). So the "softening-only / cannot host the stiffening cage" finding (`:45`, `:79`) is a **measured result**, not just a structural inference. *(0.376 is the `A_cap=0.99` clamp floor — a **formed** stiffening wall vs the coupled engine's Z≈Z₀, **not** an asymptotic short toward 0; independently reconfirmed by Stage-1.5 Layer-a `Z_tank_long_formation_floor=0.376`. Do not cite 0.376 as a physical Z→0 asymptote.)*
> - **The §4 load-bearing engineering challenge is the TWO-GRID RECONCILIATION** — the continuum-scalar-FDTD grid the `c_eff(V)` cage lives on vs the K4-tetrahedral grid the Cosserat ω lives on. The "union of pieces" below is buildable; this grid-bridge is the hard part.
> - **The stiffening⊥softening firewall (`:61`) is IMPLEMENTATION, not fundamental:** per INVARIANT-S2 Q1=(B) (Grant-ratified) every real node carries BOTH the A1-stiffening (C_eff→∞, Z→0) AND the T2-softening (ε_eff→0, Z→∞) as **orthogonal reactances driven by the same S** — the engines split what the substrate unifies; coupling them is faithful, not a violation. (Firewall §3.1, ∇×∇V≡0, still holds: the scalar cage needs a SEPARATE coupled vector sector — which the Cosserat engine provides.)
> - **SUCCESS CRITERION for the §4 engine (chord/echo audit):** "it works" = it DEMONSTRATES **α-free FORM-emergence** (the (2,3) winding self-forms from generic IC, α-free, the α-free Q emerges), **NOT** a 𝓜/𝓠/𝓙 magnitude readout — m_e is a calibration input, |Q|=1 is generic-for-any-soliton, and the α=𝓜+𝓙+𝓠 decomposition is Class-B echo (`../vol1/ch8-alpha-golden-torus.md:135`; `boundary-observables-m-q-j.md:70`).
> - **R10 (anhysteretic↔loop / remanence, §3.3) stays the SEPARATE retention wall** — whether the formed electron STAYS, not whether it forms. Parked from the existence test.

A single K4-Cosserat engine that simultaneously:
- runs on the **chiral srs grid** (hosts handedness — from v9),
- carries the **`c_eff(V)` stiffening kernel** (hosts the A1 cage — from Master-Equation FDTD),
- is **rotational** (hosts the winding — the sector `cavitation_flow` proves is needed, on the srs grid),
- carries and couples the **three channels** (from the harness),
- is **hysteretic** (hosts the constitutive loop — *open*),
- is **boost-covariant** (hosts motion — *open*).

= the union of **v9 (grid) + Master-Equation (cage) + harness (Cosserat / channels) + the three open DOF (loop, boost, node)**.

This is the *correctly-specified* version of the "one platform" the LOOP-GAP harness rule reached for — that rule under-specified it as `VacuumEngine3D`, which is **softening-only and projects its scalar from the transverse readout**, so it structurally cannot host the stiffening cage. The complete engine is **one platform per firewalled branch, converging** — not one engine retrofitted.

---

## §5 — Build-order DAG (staged, not big-bang)

Per `substrate-native-check` Checkpoint 8 (seed the generative precursor, grow one layer at a time; each layer validated before the next, so a failure localizes to one DOF):

```
chiral srs grid (v9)
      │
      ▼
add c_eff(V) stiffening kernel        ← cage channel on the chiral grid
      │
      ▼
seed photon precursor → self-trap     ← cage AND winding emerge together (not planted)
      │
      ▼
add constitutive loop (remanence)     ← OPEN: must be emergent, not an imposed latch
      │
      ▼
add boost-covariance (motion)         ← OPEN
      │
      ▼
node-creation (genesis)               ← OPEN
```

Big-bang assembly is rejected: a single all-DOF engine that fails gives an ambiguous dispersal (is it the physics, the seed, or the engine?). Staged growth disambiguates — each non-emergent layer is a localized structural-capability finding, not a global failure.

---

## §6 — Open frontier (the genuine missing physics)

- **Loop, boost, node-creation are absent from *every* engine.** These are not engine-choice gaps; they are unbuilt physics. The loop (R10 remanence) is the deepest: the kernel is anhysteretic, and every "retention" so far is imposed (§3.3).
- **The cage magnitude is not yet demonstrated to reach $\Gamma=-1$.** graft-v2's `Γ_min=−0.849` is the deepest **static-seed** read on **non-binding clips** — it sits *exactly on the clip floor* in all 10 sweep cells (corr 1.0000, residual 0.0000); the deepest *dynamical* wall at the standard `A_cap=0.999` is **−0.37** (also clip-bound), exponent-corrected to ~**−0.65** (`research/2026-06-09_crystal-graft-v2_result.md:32`). **What survives: the wall SIGN (short, Γ<0) + the monotone-with-depth trend. The magnitude is apparatus/exponent-dependent, and −1 is NOT demonstrated.**
- **Exponent defect — RESOLVED (Grant F1 ruling, 2026-07-07).** `master_equation_fdtd.py:148-151` sets `c_eff²=c0²/S`, so the physical refractive index is `n=c0/c_eff=S^0.5`; the code now RETURNS this — `n_em_index()` at `:184-188` returns `S^0.5` with the in-code correction note at `:172-183`, mirrored in `crystal_engine.py:431-432`. Resolved by Grant's F1 ruling (`research/2026-07-07_electron-lock_design-note.md:316-319`; canonical `S^0.5` per `research/2026-06-30_electron-portmap-derivation_result.md:550`). The legacy `S^0.25` (old `:169` anchor, drifted) is retired; downstream `Γ=(n−1)/(n+1)` magnitudes no longer understate the wall depth from this defect.
- **`n_eff` symbol OVERLOADED (√S EM vs 1/√S gravitational) — LIVE (KB-owner decision).** The genuinely-open item, NOT the exponent defect: the code flags that `n_eff` means √S EM-transverse (`vacuum-birefringence-e4.md:108-110`, the `δn_iso=√S−1` content) vs 1/√S gravitational (`substrate-perspective-electron.md:60`, the `n_eff=1/√S` row) and declines to silently reconcile it (`master_equation_fdtd.py:178-180`, `crystal_engine.py:433-435`). ⚠ The SOURCE comments at `master_equation_fdtd.py:178-179` carry STALE anchors (`:12` / `:58`) — flag-only; engine module untouched in this PR. flag-don't-fix: a KB-owner symbol decision — no symbol picked here.

---

## §7 — Gravity / QED-extension engine capabilities (a DIFFERENT axis than the 7-DOF electron matrix)

> **Scope note (flag-don't-fix — schema honesty).** The §2 matrix above tracks the **7 DOF of a complete
> electron** on the *electron engines* (Master-Equation FDTD, crystal_engine, K4-TLM, cavitation_flow, srs, the
> harness). It has **no "back-reaction" / "two-way" / "self-gravitation" row** — those are not electron-cage DOF.
> The GR-QED extension engine (`src/ave/gravity/`, `src/ave/qed/`) is a **separate build axis** (a correction ON
> the inherited GR/QED continuum solvers), so its capabilities are tracked here in prose, NOT as a new column in
> the electron DOF matrix (which would misuse that schema). The GR-QED arc's ★make-or-break — **two-way
> gravitational back-reaction (item #86)** — was flagged **ABSENT** by the engine-architecture frontier; it is
> now **LANDED (2026-06-29)**. This section records the transition.

| GR-QED engine capability | Before | After (2026-06-29) | Anchor |
|---|---|---|---|
| **Two-way gravitational back-reaction (#86)** — the field sources ITSELF; $M_{\text{eff}}$ emerges from the converged field energy | **ABSENT** (the ★make-or-break; only the one-way $T_{00}^{\text{matter}}\to\varepsilon_{11}$ forward solve existed) | **PRESENT / landed** — self-consistent Picard fixed point, provably contractive ($\rho$ measured $<1$), energy-stationary, all 4 at-risk gates + recover-GR green | clm-w5ez6i; `backreaction.solve_backreaction`; recover-GR gate `backreaction.recover_gr_weak_field` |
| **Saturating-modulus strong-field correction** — bulk stiffens to a yield shell at $r_{\text{sat}}=3.5\,r_s$ | absent (linear core only) | **PRESENT** — elliptic relaxation on the native K4 stencil; clip-independence gate green (yield-physics, not the clamp, sets the wall) | clm-zbvfpi; `gw_propagation.relax_finite_core_strain`, `clip_independence_gate` |
| **Brillouin-zone UV cutoff** — 1-loop finite by mode-count, no counterterm | (analytic claim only: clm-3i66gp "UV divergence naturally absent") | **PRESENT** — numerical driver confirmation; finite-vs-divergent side-by-side; distinct-cutoff discipline declared | clm-1wmyx3; `qed/brillouin_cutoff.loop_integral_brillouin_zone` |

**Honest class (do NOT over-read).** These are **engine-capability / consistency-class** landings, not new
value-level chords. The back-reaction makes $M_{\text{eff}}$ EMERGENT (architectural win) but the value-map
$r_s=2GM_{\text{eff}}/c^2$ still imports $G$; recover-GR is consistency-class. What #86 UNBLOCKS is the
*reversible* self-gravitation loop — the DE-tracks-matter chord (the irreversible F6 depletion primitive) is a
**separate, still-UNBUILT Stage-4** capability (see
[`../vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md`](../vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md)
§5: F6 = ABSENT-INVENTED; `solve_backreaction` is static-elliptic, no $a(t)$ evolver). Landing #86 is a
necessary precursor, NOT the chord itself. Canonical detail:
[`../vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md`](../vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md).

---

## §8b — 2026-07-04 engine-capability refresh (carrier-tagged module status — ADDITIVE)

> **Refresh note (KEEP-BOTH, dated supersession — NOT a rewrite).** §2's engine × DOF matrix
> (verified 2026-06-13) stands as the DOF-coverage source of truth. This section ADDS the
> **carrier axis** the 2026-07-03 D1 ratification made load-bearing, and folds in the day's
> engine changes. Where a §2 cell and a §8b row disagree, the §8b date wins for
> carrier/validation-state; §2 wins for DOF-mechanism coverage. Every cite re-verified at
> `origin/main` HEAD `d187ed59` (PR#500 merged), verify-before-cite.
>
> **Class:** INFRASTRUCTURE / INSTRUMENT-AUDIT. No physics chord/echo/emergence claim is minted
> here. `mass = A1` (PR#260 / #311 ECHO-final) is untouched by everything below.

### §8b.0 — D1 RATIFICATION (2026-07-03): srs-z3 is the production carrier

Grant ratified (`_orchestration/2026-07-03_srs-migration-policy.md`; ruling record
`research/2026-06-12_lattice-d1-adjudication-memo.md` 2026-07-03 addendum; def-entry `def-4b1a2c`):
**srs-z3** — the true Sunada-K4 / Laves / (10,3)-a / srs net (degree-3, chiral, $I4_1 32$ — the
object Axiom 1 names) — is the engine's **production carrier**. The historical achiral **diamond
z=4** (`TETRA_OFFSETS`) engine is re-tagged a **non-canonical instrument** (statics-pathological;
verdicts carrier-tagged). This is an **ENGINEERING-FIDELITY** ruling — the engine implements the
lattice the axiom already names — **no new ontological claim beyond Axiom 1.** The policy EXECUTES
NOTHING (migration is future-arc work); it sets three standing rules: (1) new engine work builds on
srs-z3 by default; (2) every `TETRA_OFFSETS` module gets, at next touch, MIGRATE or an explicit
`# non-canonical instrument` scope-tag; (3) every future engine verdict declares its carrier.

**Carrier vocabulary (this refresh):**
- **srs-z3** — chiral Laves z=3 net; the ratified production carrier. Well-posed graph Laplacian
  `L_srs = Bᵀ·diag(D)·B` (nullspace dim 1 = the physical DC mode). CARRIES chirality (writhe ≠ 0,
  L/R sign-flip) → can host the (2,3) winding = charge.
- **diamond-z4 (instrument-tagged)** — achiral bipartite-FCC `TETRA_OFFSETS` net. `L_D =
  Div·diag(D)·Grad` connects only same-parity nodes → two non-communicating sublattices, an
  8–16-dim frozen nullspace (`native_cage_imex.py`). CANNOT carry chirality. Retained as a
  *documented instrument* (the α / Lorentz chains were hosted here — P1 migration gate; §8b.3).
- **Cartesian (7-pt)** — `CrystalEngine` / `MasterEquationFDTD` continuum FDTD; the reference /
  continuum-cross-check carrier. NOT diamond, NOT srs. Hosts the `c_eff(V)` cage cross-check and
  the Q≈30.8 cold-cage clean-negative (`crystal_engine.py:154`).
- **k-space** — spectral / Bloch-eigensolve carrier (Debye spectrum, band-structure eigensolves).

### §8b.1 — carrier-tagged engine-module table (the lattice-carrying modules)

Per the srs-migration-policy §B inventory + a grep census of the 175 `src/ave/` modules (the
~30 that touch a substrate lattice; the remaining ~145 are constants / analytic / circuit /
facade / utility modules that carry no lattice DOF). Migration status per the policy ladder.

| Module | Carrier | Role | Validation state | Migration status (policy) | Claims served |
|:--|:--|:--|:--|:--|:--|
| `topological/cosserat_field_3d.py` | diamond-z4 | **defines** `TETRA_OFFSETS` (`:134-139`) + Grad/Div/helicity primitives | root of the stencil pathology (odd coord-sum → checkerboard nullspace) | rung-1 (migrate first); carrier-tag at next touch | `clm-ze4clw` (Q=Link winding) primitives |
| `solvers/native_cage_imex.py` | diamond-z4 | Stage-2 native-cage IMEX `L_D = Div·diag(D)·Grad` | **CLASS-1 exposed** (HIGH #1); DISPERSE re-booked on srs (see §8b.2) | **rung-1: re-run LANDED on srs**; fold `assemble_L_srs` in as default; retire `L_D` to instrument | bulk-self-trap make-or-break |
| `solvers/coupled_cage_winding.py` | diamond-z4 | Stage-3 A1↔ω PDE, extends Stage-2 `L_D` | **CLASS-1 exposed** (HIGH #2, inherits #1) | **rung-2: TOP OPEN re-run** (S3 cavity-pinning on srs, gated downstream) | Stage-3 cavity-pinning |
| `solvers/srs_cage_winding.py` | **srs-z3** | `SrsCageWinding` / `assemble_L_srs` (`Bᵀ·diag·B`, nullspace dim 1) | GREEN; the migration TARGET pattern | **already srs** — the destination, not a source | localization re-run operator |
| `solvers/spectral_liveness.py` | srs-z3 + diamond | **NEW (2026-07-03)** — spectral-liveness diagnostic; nullspace-energy fraction of a seed vs any SPD div-form operator | GREEN (7 keepers `test_spectral_liveness.py`); reproduces the exposure independently | already srs-aware; first-class reusable | the Step 3.8 readout-liveness gate (INFRASTRUCTURE) |
| `topological/srs_dec.py` | **srs-z3** | **NEW (2026-07-03)** — DEC 2-complex on girth-10 faces; exact `∂₁,∂₂`; ∂∂=0 (int64 exact) | GREEN (14 keepers `test_srs_dec_operators.py`, ~0.5 s); THEOREM stated (§8b.4) | born-on-srs; new infrastructure | `clm-ze4clw` (harmonic sector), `clm-4r4jiy` (co-exact Coulomb) |
| `topological/srs_dec_punctured.py` | **srs-z3** | **NEW (2026-07-03)** — punctured-domain DEC (lane-Z fluxoid step-0); solid-torus tube puncture opens Δb₁=+1 | GREEN (`test_srs_dec_punctured.py`); disc-fill certifies the core-linking meridian | born-on-srs | winding-DOF-on-H₁ (`[DOORWAY-NO-PINNING]`; FORM-derived/VALUE-imported) |
| `topological/k4_cosserat_coupling.py` | diamond-z4 | `CoupledK4Cosserat` K4⊗Cosserat time-domain (band-structure host) | dynamical rank-2 eigensolve (no statics-nullspace bite); MED #21 (#417 phase-space) | rung-4 re-run (#417 (2,3) BREAK on srs); **name walk-back target d5** (not a statics migrate) | #417 phase-space winding |
| `solvers/graded_vacuum_network.py` | srs + diamond | graded-Z network; builds srs via `build_srs_net` (`:87`) but also uses the 4 diamond diagonals | mixed; statics `Div·Grad` on diamond leg | carrier-tag at next touch | graded vacuum impedance network |
| `solvers/node_scattering_multiplicity.py` | srs/diamond connect-map | Fork-A REFUTE-R3; uses CONNECT-map not dense cube | LOW (self-caught R3 overclaim, Rule 12) | opportunistic (rung-6) | node-scattering multiplicity |
| `core/scalar_grade_seed.py` | diamond-z4 | seeds A1 grade using `TETRA_OFFSETS` helicity | seed helper | migrates with the operators it feeds | A1 grade seeding |
| `gravity/gw_propagation.py` | diamond-z4 | GW permutation-difference operators on the 4 diagonals; **`relax_finite_core_strain`** (saturating-modulus) | LOW (#27 back-reaction leg live); clip-independence gate GREEN | carrier-tag at next touch (rung-6) | `clm-zbvfpi` (saturating-modulus), #86 leg |
| `gravity/backreaction.py` | Cartesian / K4-native | **#86 two-way back-reaction** — Picard fixed point (`solve_backreaction`), recover-GR gate | **PRESENT / LANDED 2026-06-29**; contractive (ρ<1), energy-stationary, 4 at-risk gates GREEN | n/a (GR-QED extension axis, §7) | `clm-w5ez6i` (back-reaction), recover-GR |
| `qed/brillouin_cutoff.py` | k-space | Brillouin-zone UV cutoff (`loop_integral_brillouin_zone`) | PRESENT; finite-vs-divergent side-by-side | n/a (GR-QED axis) | `clm-1wmyx3` (UV-finite by mode-count) |
| `facade/unified_engine.py` | diamond-z4 facade | N³-node diamond-K4 facade over the above | facade; migrates when backends do | carrier-tag at next touch (rung-6) | unified-engine facade |
| `core/crystal_engine.py` | Cartesian (7-pt) | graft-v2..v4; `c_eff(V)` cage SIGN-confirmed | cage SIGN + monotone-with-depth; magnitude apparatus-bound (§6) | n/a (Cartesian reference, not a migration target) | cage-stiffening, Q≈30.8 cold-cage |
| `core/master_equation_fdtd.py` | Cartesian (7-pt) | the `c_eff(V)` A1-cage continuum FDTD; v14 Mode-I PASS | Mode-I PASS = continuum cross-check reference (native self-trap FALSIFIED, §8b.2) | n/a (Cartesian reference) | A1-cage (§2 `master_eq` row) |
| `core/fdtd_3d.py`, `core/fdtd_3d_jax.py` | Cartesian (7-pt) | free-EM FDTD; **circulation-keyed vacuum μ-grade (PR#500)** | GREEN — loaded-μ energy debt DISCHARGED at HEAD (`\|dH/H\|=1.44×10⁻³`, μ-attributable); test `test_vca_mu_circulation_keying.py` (470 lines) | n/a (Cartesian free-EM) | Route-C μ-keying (birefringence FORK-1) |
| `core/chiral_lattice.py` | **srs-z3** (+ diamond builder) | `build_srs_net` (z=3 chiral) AND `build_diamond_net` (achiral z=4 — walk-back name target d8) | GREEN; L0–L2 acceptance suite GREEN | destination; `build_diamond_net` callers scope-tag as instrument | chiral-grid (§2 `srs_v9`) |
| `core/chiral_lattice_v9..v17.py` | srs-z3 | genesis / chiral-lattice series (v9 FROZEN falsifier; v13 "LOCALIZATION-LANDED") | v9 frozen; series exploratory | already srs | genesis exploration |
| `solvers/vacuum_varactor_scatter.py` | srs/diamond connect-map | S(A) per-bond scatter operator | LOW; recovers bedrock at S=1 | opportunistic | vacuum-varactor scatter |
| `solvers/fork_b_saturation_tank.py` | srs-z3 | fork-b A1 mass cavity (the surviving localizer) | cavity-eigenmode EXISTS | already srs | boundary-cavity localization |
| `core/cavitation_flow.py` | achiral flow grid | the "fourth object" — softening rarefaction pocket + circulation | circulation HAVE (Kelvin-conserved); firewalled from the cage | n/a (not diamond/srs) | winding/circulation (§2 `cavitation_flow`) |
| `topological/vacuum_engine.py` | diamond-K4 | `VacuumEngine3D` / loop-gap harness; softening-only, scalar = projection | §2 `harness` row (softening-only, no independent A1) | carrier-tag at next touch | three-channel harness |

### §8b.2 — localization re-adjudication LANDED on srs (rung-1 done)

The Stage-2 bulk-self-trap DISPERSE make-or-break — flagged CLASS-1-exposed (diamond `L_D`
93%-frozen-nullspace, no same-pipeline positive control) by the 2026-07-03 verdict-exposure sweep
(`research/2026-07-03_engine-verdict-exposure-sweep_result.md`) — was **re-asked on the canonical
srs-z3 carrier with a proven-live readout** (`research/2026-07-03_localization-readjudication_result.md`):

> **VERDICT `[DISPERSES-ON-SRS-LIVE]`.** A smooth A1 core, seeded on srs-z3, DISPERSES at every
> box size (participation number grows 16.5×/24.5×/27.0× at L=4/6/8, energy-conserved to ~1e-9)
> — while the SAME instrument reads a known-bound positive control as `LOCALIZED_PERSIST`. The
> boundary/topological localization reroute (#403/#404) **stands, now grounded** on the Axiom-1
> carrier rather than the exposed diamond instrument.

Seduction-trap explicitly rejected: the exposure did NOT establish "the electron localizes in the
bulk after all." **mass = A1 untouched** (only the localization MECHANISM was ever at stake).
Class: MANIFESTATION (α-free, no CODATA). The srs instrument is cleaner on all five axes
(§5 of that doc): well-posed statics, nullspace dim 1, 89.5% smooth-core live fraction (vs
diamond's 6.5%), clean positive control, and it carries the chirality the charge lives in.

### §8b.3 — retired instruments (2026-07-03)

Two instruments were RETIRED this day — recorded so the map does not read them as live engines:

- **Stage-2a nonlinear static .OP** (`src/scripts/vol_2_subatomic/em_readout_stage2_nonlinear_op.py`)
  — **RETIRED** (`research/2026-07-03_em-readout-stage2-redesign_prereg.md` §R3). It cannot answer
  the winding-emergence question: (a) its only readable signal is the anchor-source `κτ` (not
  physics), and (b) a source-free version returns `φ ≡ const` by theorem. `run_decisive_winding_sweep`
  never unlocks. Preserved as the reasoning-record + the theorem's empirical triple (nullspace +
  ablation), NOT as a live instrument.
- **The blind Stage-1 readout** (the #477 catch) — a merged null read on a **structurally-degenerate
  global-sum observable** without a same-pipeline positive control. This catch *triggered* the whole
  verdict-exposure sweep (CLASS-2 blind-readout pathology). The Stage-1b operator pair
  (`_srs_curl_nodes`, `_srs_node_divergence`) is pinned as a **regression** — NOT a DEC pair
  (`div∘curl` RMS ≈ 0.35, decisively not a machine zero); superseded by the `srs_dec` operators (§8b.4).

### §8b.4 — the srs DEC theorem + liveness doctrine (new infrastructure)

- **srs DEC operators (`ave.topological.srs_dec`).** A valid ∂₂ on the srs girth-10 faces;
  ∂₁∂₂=0 (int64 EXACT); harmonic dims (b₀,b₁,b₂)=(1,3,over-complete). **THEOREM** (srs curl-class
  charge-neutrality, cold-linear-static-local): for any 2-cochain `c`, `div(curl_adj(c)) = −∂₁∂₂c = 0`
  identically — **every curl-class field is divergence-free = zero enclosed charge at every radius**,
  as a structural identity, not a numerical near-zero. Upgrades the Stage-1b `{∇×ω, ω}` closure from
  an operator-pair property to a class theorem. SCOPE: NOTHING claimed for non-curl couplings,
  S(A)-modulated couplings, nonlinear statics, dynamics, or the winding's topological Q (which lives
  in the harmonic H₁ sector, §8b.4 punctured). Reconciled with the solver Laplacian: `BᵀB = ∂₁∂₁ᵀ = −L0`
  EXACTLY (same operator, sign convention only).
- **Winding-DOF lands on H₁ (punctured DEC).** Puncturing srs with the winding's solid-torus tube
  opens exactly one new source-free harmonic 1-cochain (Δb₁=+1, stable L=3,4,5); a ball core opens
  none. But the flux VALUE is unpinned — verdict `[DOORWAY-NO-PINNING]`: the harmonic DOF exists (FORM
  lattice-forced), its flux quantum is imported (VALUE = α-echo). A FORM-derived / VALUE-imported
  instance on charge-flux.
- **Liveness doctrine (Step 3.8 / trigger-10, ave-prereg v1.4).** Operationalized this day: any
  null / disperse / does-not-exist read must first pass a **same-pipeline readout-liveness gate**
  (Step 3.8a) — the instrument must be shown ABLE to register the OPPOSITE (a positive control on the
  SAME operator), and the seed's nullspace-energy fraction read BEFORE the verdict. Enforced by
  `spectral_liveness.py`. This is the doctrine that the exposure sweep's CLASS-2 (blind readout)
  pathology violated — an energy-conservation gate is a rigor guard, NOT a liveness proof.

### §8b.5 — #86 two-way back-reaction: TRUE state confirmed

§7's transition (ABSENT → LANDED 2026-06-29) is re-confirmed at this HEAD: `backreaction.solve_backreaction`
is the self-consistent Picard fixed point (provably contractive, energy-stationary, recover-GR gate
green, `clm-w5ez6i`). Honest class unchanged: this makes `M_eff` EMERGENT (architectural win) but the
value-map `r_s = 2GM_eff/c²` still imports G — consistency-class, NOT a new value-chord. The DE-tracks-matter
irreversible-depletion chord remains a separate, still-UNBUILT Stage-4 capability.

### §8b.6 — engine-upgrade program COMPLETE (2026-07-04; PRs #512 / #513 / #515)

The five-item engine-upgrade program (tracker `_orchestration/2026-07-04_engine-upgrade-program.md`)
— chartered to retire the "uncertified operator drives a verdict" failure class the verdict-exposure
sweep exposed (§8b.3) — is **COMPLETE**. Class INFRASTRUCTURE / INSTRUMENT-HARDENING; no physics
chord/echo/emergence minted; `mass = A1` (PR#260 / #311) untouched. Program-completion rows (cites
verified at their merge PRs):

| Item | Deliverable | State | PR |
|:--|:--|:--|:--|
| **1 — DEC canonicalization** | `operator_registry.py::OPERATOR_SETS` (4 sets registered w/ carrier + adjoint spec); **CI-certified** by `test_operator_adjoint_consistency.py` (adjoint-consistency + ∂∂=0; 15 pass / 3 skip). Sign-convention split (srs `div=−∂₁` vs solver/diamond `div=+gradᵀ`) recorded per-set, reconciled not forced (Rule-10 catch). 2 non-adjoint heuristics scope-tagged, NOT registered. | **✅ LANDED** | #512 |
| **2 — validation-harness library** | `src/ave/validation/` (5 guards: planted-source, structural-degeneracy, runtime-independence, hardened equation-audit, spectral-liveness re-export); each with a positive AND a negative test. Retrofit demo on the 48×48 micropolar Φ(k). 20 tests green. | **✅ LANDED** | #512 |
| **5 — carrier-declaration guard** | `src/ave/core/carrier.py` `Carrier` enum (srs-z3 / diamond-z4-instrument / cartesian-reference / k-space); diamond-stencil consumers REQUIRE `instrument_scope=` (RAISE on new construction, DeprecationWarning on frozen-provenance = KEEP-BOTH). Byte-identity preserved (`native_cage L_D` sha256 unchanged). 12 keepers. | **✅ LANDED** | #512 |
| **4 — SPICE phase-1 ladder** | ngspice-46-backed **validate-on-known ladder 5/5 PASS** (HALT-gate never tripped): RC/LC transients, Ax4 kernel in A1+T2 sectors, Poisson `.OP`==MNA, LC-chain dispersion, live **bias-couples-to-wave** DC→AC. `src/ave/bench/spice_runner.py`; 3 `.lib` syntax bugs caught+fixed at first live parse. `research/2026-07-04_spice-phase1-ladder_result.md`. | **✅ LANDED** | #513 |
| **3 — Lorentz-on-srs (the P1 make-or-break)** | The migration policy's **P1 acceptance gate CLEARS** `[ISOTROPY-EMERGES]` on srs-z3: leading-order c isotropic to machine precision, NO cold birefringence (transverse branches degenerate `1.7e-14`), the (qℓ)⁴ isotropy FORM re-clears carrier-native (`κ_srs=−1/12`, cubic-point-group fact), the chiral k-linear gyrotropy is srs-distinct + below-bound. First full consumer of items 1/2/5. The Lorentz leg PASSES; the α-chain P1 leg is separate (not this arc). | **✅ LANDED** (PR #515 MERGED 2026-07-04) | #515 |

**Scope honesty:** the 🟡
weak-C demotion of `clm-k4d4ph` / `clm-yr6tu4` is UNCHANGED by this program (the raw eigensolve
band-edge anisotropy is O(k²) on BOTH carriers; gate `wejkhvnfb` OPEN). The two varactor
ADJUDICATION-PENDING questions in the SPICE lane remain OPEN (Grant-gated).

### §8b.7 — 2026-07-10/11 vertex + eigencavity instrument refresh (ADDITIVE)

The vertex arc (x33–x38) and the x40/x42 landings added new **instruments** (INSTRUMENT /
INFRASTRUCTURE class — no physics chord/echo/emergence minted; `mass = A1` untouched). Held to
the §2 no-claim bar (every row grounded against a file:line + prereg + merge-PR anchor):

| Instrument | Role | Class / boundary | Anchor (prereg + PR) |
|:--|:--|:--|:--|
| `core/junction_scattering.py` | **X38** srs vertex S₁₁ EXTRACTION + canonical Op6 bore selection (route d): does the substrate SELECT the junction extent `f` by minimizing junction reflection? | INSTRUMENT; **anti-install boundary (G-A gate)** — consumes ONLY geometry (`:10-13`, `μ₀/ε₀/ℓ` cancel, no OMEGA_C/M_E install) | `research/2026-07-10_x38-s11-bore-selection_prereg_FROZEN.md`; #619 (honesty-lag fix #621) |
| `core/junction_parasitics.py` | **X37** srs vertex junction-parasitic EXTRACTION — the vertex equivalent circuit DERIVED from bond geometry (120° bonds + srs twist), NOT installed | INSTRUMENT; **anti-install boundary (G-A gate)** — geometry-only (`:10-16`; the `1/√(L_jC_j)=ω_C` #613 install is the exact error X37 exists to avoid) | `research/2026-07-10_x37-junction-parasitics_prereg_FROZEN.md`; #616 (fix #620) |
| `solvers/tethered_pivot_x34b.py` | **x34b** control-subtracted excess detector, frozen a-priori — a THIN driver over the merged x34 solver (Rule-14, no fork-copy); returned TRACK → BANKED NEGATIVE | INSTRUMENT; frozen-a-priori control-subtraction | `research/2026-07-10_tethered-pivot-rerun_prereg.md`; #626 |
| `topological/srs_dec.py` (**addition** to the §8b.1 row) | **x40** srs-girth witness: `enumerate_girth_faces()` (`:140`) enumerates the girth-10 rings as the 2-cells (`SRS_GIRTH=10`, `:127-157`) — the witness behind R-B's `trapped = 1/girth` theorem (N=10 → 1/10) | INFRASTRUCTURE; born-on-srs (extends the existing GREEN §8b.1 row) | #632 (correction #638) |
| `src/scripts/vol_2_subatomic/x42_atomic_eigencavity.py` (**not** a `src/ave/` module — a Vol-2 script driver) | **x42** atomic eigencavity — hydrogen as an eigencavity; test `src/tests/test_x42_atomic_eigencavity.py` | INSTRUMENT (research/script driver) | #634 (repairs #639) |

**Status-stamp re-confirm:** §2 / §8b.1 cells unchanged by this refresh (KEEP-BOTH — the additive
rows do not flip any existing status). The X36 install-tautology (§below / `research/2026-07-09_x36-node-bottleneck_result.md`)
and the X38 bore-fork disposition remain PENDING-GRANT.

---

## §8 — Figure-artifact hygiene policy (2026-07-04, D4 — going-forward)

> **Policy note (infrastructure, no physics).** Landed with the 2026-07-04 engine-capability
> refresh + figure-disposition pass. This governs which rendered artifacts the repo tracks.

**Figures are derived artifacts.** The driver + its committed input data are the artifact of
record; the rendered binary (`.png`/`.pdf`/`.svg`/`.gif`) is a regenerable convenience. Three
standing rules:

1. **Only CITED figures are tracked.** A figure is *cited* iff it is referenced from a `.tex`
   (`\includegraphics`) or a `.md` (markdown image / explicit path). Cited figures live in the
   volumes' `figures/` dirs and are committed. Everything else is scratch.
2. **Driver-output scratch dirs are git-ignored.** `src/tests/outputs/`, `src/scripts/**/_output/`,
   and `**/simulations/outputs/` are ignored (`.gitignore`, D4 block). A driver may write freely
   there; nothing in those dirs is tracked unless explicitly allowlisted.
3. **Drivers must be deterministic-regenerable.** A deleted uncited figure must be reproducible by
   re-running its named driver (recorded in the sibling result-doc / test). If a figure is *not*
   regenerable, it is not scratch — it is a tracked asset and belongs in `figures/` with a
   provenance note (orphan-non-regenerable artifacts are a Grant-call, not auto-deleted).

**Known policy smell (flagged, not fixed — future-arc item).** 38 CITED figures currently live
inside scratch `_output/` dirs (e.g. `src/scripts/vol_9_device/_output/*.png` cited by the vol-9
datasheet). They are `!`-allowlisted in `.gitignore` so they stay tracked, but cited renders
*belong in `figures/`*. Migrating them (and repointing the `\includegraphics` paths) is a
mechanical future-arc cleanup, deliberately NOT done in the D4 pass (path-repointing risks a
build break; out of the hygiene pass's scope).

---

## Cross-references

- [`../vol4/circuit-theory/ch1-vacuum-circuit-analysis/unified-engine-design-doctrine.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/unified-engine-design-doctrine.md) — the **design doctrine** companion to this capability map: the ontology (grid IS lattice), the continuum-vs-discrete dispatch, the coupling layer, the honesty guards, and *what the engine is for*. This map audits *what each engine carries*; the doctrine says *how the converged engine is built and used*.
- [`two-engine-architecture-a027.md`](two-engine-architecture-a027.md) — the K4-TLM + Master-Equation parent this generalizes
- [`loop-gap-electron-resonator-closure-doctrine.md`](loop-gap-electron-resonator-closure-doctrine.md) — the anhysteretic-loop / channel-routing doctrine
- [`../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md`](../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md) — the three-impedance law (3-channel DOF)
- `src/ave/core/master_equation_fdtd.py`, `crystal_engine.py`, `cavitation_flow.py`; `src/ave/topological/vacuum_engine.py` — the engines
- [`figures/engine_capability_matrix.yaml`](figures/engine_capability_matrix.yaml) — the matrix source-of-truth (per-cell anchors)
