# Result — Electron-Q graded-vacuum-network (Build-A, Stages 0–3)

**Prereg:** `research/2026-06-19_electron-Q-coupled-network_prereg.md` (frozen commit
`4ae50ba0`, the FIRST commit of this branch — frozen-before-build).
**Branch:** `analysis/2026-06-19-electron-Q-coupled-network` (worktree off `origin/main`
@ 39ab0a25).
**Scope:** Build-A = Stages 0–3 ONLY (native operator + ISOLATION eigensolver +
lossless/Nyquist sanity). H_couple / the coupled solve / Fork-A coupling = Build-B —
NOT run (HALT, see below).

---

## HEADLINE (one line)

**GATE1 (the MANDATORY validate-on-known gate) FAILS: the native isolation-leg
eigenmode Q is LOSSLESS-CONFINED (Q ≫ 45, growing toward ∞ with resolution) — NOT in
the [20,45] band, NOT ~137, NOT ~3. Per the prereg, Build-A HALTS; we do NOT push to
the coupled leg.** The PRIOR (α = ECHO; the cold cage gives Q ≈ 30.8, not 137) is
PRESERVED, and the eigensolver gives a clean, single-mechanism reason it cannot
reproduce 30.8 either: the eigenmode-Q and the time-domain ringdown-Q are different
observables.

---

## GATE TABLE (Build-A)

| Gate | Spec | Result | Verdict |
|---|---|---|---|
| **GATE1** | Q_isolation in [20,45], validate-on-known | Q ≫ 45 (N24→1.8e5, N32→1.2e8, N48→1.1e13). Not 137, not 3. | **FAIL → HALT** |

> **Headline-config note (2026-06-19, frac discipline).** The N24/N32/N48 numbers above are
> the **PINNED-TEST** config `_COLD = dict(frac=0.9, S_min=1e-3, sigma_port=2.0)`
> (`test_graded_vacuum_network_isolation.py:47`), reproduced per-N in isolated processes:
> N24→1.7e5, N32→1.2e8, N48→1.1e13 (the headline rounds 1.7e5→1.8e5). The solver *default*
> `IsolationConfig.frac=0.999` (`graded_vacuum_network.py:292`) gives a **deeper** wall and
> hence **larger** Q (N24→2.3e12, N32→1.2e16) — same direction, more lossless. **The GATE1
> verdict (Q ≫ 45, lossless-confined, monotone-growing with N) is robust to both fracs**;
> the headline cites the pinned-test config, not the solver default.
| **GATE2** | EM port CLOSED → Q=∞ | Q = 1.4e16, Im(ω) = 4e-17 | **PASS** |
| **GATE4** | gapped, peak>bin1, ω·dt≪π, shear resolved | ω_re>0 gapped; cross-check ω·dt=0.0157≪π; vector branch PSD-resolved | **PASS** |
| anti-coincidence (DEC-5) | Q ≠ Z_RADIATION=29.98 | open-port Q ~ 1.8e5 (computed, not read) | **PASS** |
| α-free (grep) | zero α/Q_TANK/137/RHO_BULK in input code | zero code tokens (prose-only) | **PASS** |
| α→2α invariance (strongest) | Q must NOT move | \|dQ/Q\| = 2e-10 | **PASS** |
| DEC-1 exponent robustness | FAIL holds √S AND S^{1/4} | √S: Q=1.8e5; S^{1/4}: Q=1.4e4 — both ≫45 | **robust** |

---

## BIN ASSIGNMENT

Per the frozen prereg:

- The CHORD bin requires ALL of (1) Q in [127,147], (2) α-free inputs, (3) α-invariant,
  (4) GATE1 passed first. **Items (2) and (3) PASS** (genuinely α-free, |dQ/Q|=2e-10),
  but **item (4) FAILS** (GATE1 is not satisfiable in the eigenframe) and **item (1)
  is moot** (Q is ≫147, not in [127,147]). → **NOT CHORD.**
- The ECHO bin (a) = "Q stays ~order of isolation [10,60] (couplings fail to supply the
  store)". The isolation eigen-Q is ≫60 (lossless), so it is not ECHO-(a) at face value
  either. The honest classification is a **MOVED-NEGATIVE / NULL-AT-THE-VALIDATE-GATE**:
  the validate-on-known anchor (reproduce the cold-cage ~30.8) is **not reproducible in
  the eigenframe** because the eigenmode-Q is a different observable from the ringdown-Q.

**Net:** the discriminating test does NOT promote α from echo→chord at the electron.
The prior (α = ECHO; cold cage Q ≈ 30.8 ≠ 137) is preserved and reinforced. The
eigensolver adds: the isolation-leg bound mode is a **near-perfect lossless reactive
standing mode** whose Q is set by geometric radiative leak (→0 as the μ-load-short wall
deepens), NOT by the EM-port admittance and NOT by α.

---

## THE SINGLE MECHANISM (Rule 11 — one mechanism explains the failure)

The cold-cage `Q_ringdown = 30.75` (reproduced EXACTLY this session: ω_cutoff=2.868,
ipk=15, peak_mean=456, zero_crossings=23, matching `test_l3_mass_cage.py:25` to the
digit) is a **driven, finite-grid, time-domain ringdown** observable: a shell-breathing
kick on a posited core, evolved 6000 steps, with the decay envelope fit by a Hilbert
transform. Its value is dominated by transient shedding + continuum coupling + the
windowed-envelope fit — NOT by the intrinsic linewidth of the bound mode.

The **native eigenmode Q** measures the intrinsic radiative linewidth of the same
confined mode. The μ-load SHORT (Γ→−1) saturated wall is a near-perfect mirror, so the
bound mode barely reaches the matched EM port at the box boundary (`port_frac` → 0 as N
grows or the wall deepens). With essentially no radiative leak, Im(ω) → 0 and Q → ∞.

These two Qs are **different observables**. The validate-on-known step (HR3: reproduce
~30.8) is therefore not satisfiable in the eigenframe — not because of an α-leak (the
α→2α test proves α-invariance to 10 sig-figs), not because of a solver bug (the mode is
gapped, discrete, core-localised, and matches the dense solve to 3e-16), but because the
eigensolver is measuring the lossless-reactive linewidth, which the time-domain ringdown
is not.

Confirmation the failure is structural, not a tuning artifact:
- Sweeping the port admittance `sigma_port` over 1 → 2000 **raises** Q (8.7e7 → 1.1e11):
  a more-mismatched boundary reflects more, so no admittance brings the confined mode
  into [20,45].
- Even unphysically shallow/leaky walls (frac=0.3–0.6, S_min=0.05–0.3) bottom out at
  Q ≈ 162, still ~4× above the band.

---

## WHAT PASSED (the build is sound; the negative is real, not a bug)

- **Native stencil (HR1):** `L_native = adjoint_tetrahedral_divergence ∘ D ∘
  tetrahedral_gradient` on the diamond/srs TETRA_OFFSETS stencil. The Cartesian 7-pt
  Laplacian (`crystal_engine.py:154`, `master_equation_fdtd.py:124`) is **never
  imported**. The keeper `test_cosserat_field_3d.py:32` passes. Operator verified
  sign-consistent (L(linear)=0, L(r²)=uniform const) and symmetric **positive**-
  semidefinite (the sign convention was pinned EMPIRICALLY at integrator time — the
  first-draft NSD comment was a bug, corrected).
- **α-free (HR2):** only `Z_0, C_0, NU_VAC=2/7, KAPPA_TILDE=6/5, L_NODE` + geometry are
  imported. Import-guards assert `Q_TANK / ALPHA / RHO_BULK / ELECTRON` absent. The
  Q-determining mechanical quantity is the dimensionless ρ-cancelling ratio
  `Z_bulk/Z_shear = c_L/c_T = √(10/3) = 1.8257` (`crystal_engine.py:27`, DERIVED,
  α-invariant).
- **α→2α invariance:** doubling ALPHA leaves Q unchanged to |dQ/Q| = 2e-10 — the
  load-bearing proof there is NO α-leak.
- **GATE2 / GATE4 / anti-coincidence:** all PASS (see table).

---

## FLAGS SURFACED (Flag-don't-fix — for Grant/auditor adjudication)

1. **Impedance-ratio reconciliation.** The prereg's headline `Z_bulk/Z_shear =
   √2·√(10/3) = 2.582` COMPOUNDS two distinct transverse references — the EM-photon
   speed √(G/ρ)=c₀ (the √2 = √(K/G), `_bulk.py:102`) AND the mechanical-shear speed c_T
   (`crystal_engine.py:96`). For the two-mechanical-channels build (bulk K vs mechanical
   shear G, DEC-4), the channel-correct ratio is `c_L/c_T = √(10/3) = 1.826` ALONE. Both
   are α-free and α-invariant, so the ambiguity does NOT affect any chord/echo bin (it
   would only shift the bulk/shear gap LOCATION). The solver exposes both
   (`RATIO_BULK_SHEAR_MECH = √(10/3) = 1.82574` primary, `graded_vacuum_network.py:122`;
   `RATIO_BULK_SHEAR_PHOTON = √2·√(10/3) = 2.58199` sensitivity, `:124`). **Needs
   Grant adjudication on which reference is physical for the network coupling.**

   > **Prereg-value-preservation NOTE (2026-06-19, do-not-silently-overwrite).** The
   > **frozen prereg headline value `Z_bulk/Z_shear = √2·√(10/3) = 2.582` is PRESERVED**
   > (not overwritten). The solver's PRIMARY `RATIO_BULK_SHEAR_MECH = √(10/3) = 1.826` is
   > the **channel-correct two-mechanical-channel ratio** (bulk `c_L` / mechanical-shear
   > `c_T`, DEC-4) — the physically-clean ratio when both arms are read on their own `ρc`
   > axis (it does NOT compound the EM-photon `√2 = √(K/G)` factor). The prereg's `2.582`
   > compounds the EM-photon transverse reference into the mechanical-shear arm. **Both are
   > α-free and α-invariant; neither moves any chord/echo bin** (only the bulk/shear gap
   > LOCATION). **FLAG for Grant:** `1.826` (channel-correct, mechanical-only) is the
   > implementer's read of "physical for the network coupling"; `2.582` (frozen prereg) is
   > retained verbatim until Grant adjudicates. Surfaced, not silently resolved
   > (flag-don't-fix).

2. **GATE1 enumerated only two failure modes (~137 leak, ~3 artifact); the actual
   failure is a third (Q→∞, lossless-confined).** The prereg's HALT instruction still
   applies (GATE1 not in band), but the *reason* is the eigenmode-vs-ringdown observable
   mismatch, not a leak or a bin-1 artifact. **This is an eigenframe/observable-design
   question:** if Build-B wants a finite isolation Q to validate against 30.8, the loss
   model must be the *continuum-radiation coupling at the core's outer edge* (where the
   mode actually leaks past the imperfect Γ≈−0.45 wall), NOT a matched port at the box
   boundary. That is a Build-B operator-design decision, surfaced here, NOT resolved.

3. **DEC-3 confinement-surface shape (F8) ASSUMED:** electron = 0₁ unknot, single
   Gaussian node. Flagged assumed-not-derived per the prereg; not exercised at the
   value-discrimination level since GATE1 halted first.

---

## DISPOSITION

- **Build-A: HALTED at GATE1** (the mandatory validate-on-known gate is not satisfiable
  in the eigenframe). Do NOT proceed to Build-B / the coupled leg.
- **α stays ECHO at the electron** (prior preserved; no echo→chord promotion). HR4
  anti-substitution honoured — the 30.8 cold-cage negative is untouched and reproduced.
- **Open for Grant/auditor:** (a) the impedance-ratio reference (Flag 1); (b) whether
  Build-B should re-pose the isolation loss as edge-continuum radiation so the eigen-Q
  is a like-for-like cross-check against the ringdown 30.8 (Flag 2). Until (b) is
  decided, the coupled-leg Q claim has no validated isolation anchor.

---

## REPRODUCIBILITY

- Solver: `src/ave/solvers/graded_vacuum_network.py`
- Tests: `src/tests/test_graded_vacuum_network_operator.py` (Stage 1, **10 tests**),
  `src/tests/test_graded_vacuum_network_isolation.py` (Stage 2/3, **9 tests** — 7 plain +
  the 2 parametrized `[0.5]`/`[0.25]` exponent cases). **19/19 pass** (`pytest --collect-only`
  reports `19 tests collected`). *(Corrected 2026-06-19: the earlier "Stage 1, 11 tests …
  20/20" miscount is fixed to the collected 10 + 9 = 19; no verdict change.)*
- Cold-cage cross-check anchor: `src/tests/engine_acceptance/_bulk.py` +
  `test_l3_mass_cage.py` T3.4b (Q_ringdown=30.75, reproduced exactly).
