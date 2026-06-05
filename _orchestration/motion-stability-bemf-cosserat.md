# Motion-stability via back-EMF — native Cosserat/dark-wake τ_zx on VacuumEngine3D

**Status:** IN-PROGRESS — implementor (worktree `analysis/motion-stability-bemf-cosserat`).
Continuation of a stalled run that confirmed engine + host + observer but failed the boost.

## §1 The hypothesis + the decisive question (Grant)

**Grant's hypothesis — stability FROM motion:** the native `τ_zx` back-EMF of a MOVING
self-trap *stabilizes* it. Operationally: retention(v) slope > 0, and the stability gain
tracks the native `τ_zx` (positive correlation), MORE than a linear (SM-counterfactual)
control at matched amplitude/saturation.

**Canonical default CONTRADICTS:** the saturated (2,3) self-trap is a static Γ=−1 knot;
moving it needs an external drive, and the deeply-saturated core (A²≈8.9 ⇒ S=√(1−A²)
clamped to 0 ⇒ z_local at the rupture floor) has `c_eff = c·√S → 0` — a **frozen local
clock**. By the canon, a frozen-core trap is **pinned**: it is stable *because static*,
not via motion.

**Why THIS engine is the real adjudication:** the Maxwell-engine version returned
CONTRADICTS but only saw the **E/H projection** of τ_zx (anti-correlated −0.81). The
`VacuumEngine3D` dark-wake observer carries the **native** back-EMF stress
`τ_zx = z_local·∂_x(A²)` directly (K4 saturation-modulated impedance × strain gradient,
`vacuum_engine.py:1533`) — not a field projection. This is the native-carrier adjudication.

## §2 Confirmed substrate (reused from the stalled run — NOT re-verified)

- **Engine:** `VacuumEngine3D.from_args(N=48, pml=4, T=0, V_SNAP conv, disable_cosserat_lc_force=True,
  enable_cosserat_self_terms=True, use_asymmetric_saturation=True, axiom_4_enabled=True)`
  (`r10_vacuumengine3d_transverse_2_3_emergence.py:setup_engine`). A28-corrected coupling.
- **Durable host (Arm-C config):** `initialize_2_3_voltage_ansatz(k4, R=0.22·N, r=R/φ², amplitude=0.40)`
  (`tlm_electron_soliton_eigenmode.py`). Gives **max A²_interior ≈ 8.90**, peak-bond amp ≈ 1.60,
  **retention ≈ 0.88–0.91** over ~60 steps. THIS is the target amplitude (the r10 value), NOT the
  failed-boost A²≈25 over-crank.
- **Native back-EMF observer:** `DarkWakeObserver(propagation_axis=0)` reads `max|τ_zx|` and a 1-D
  `τ_zx_slab` cleanly at the core (`vacuum_engine.py:1457`).

## §3 The boost (the fix — replaces the failed port-pairing)

The winding-extractor reads the quadrature phasor `(ox, oy) = (V0+V1, V2+V3)` — and the ansatz
plants exactly this: ports {0,1} carry `cos(2φ+3ψ)`, ports {2,3} carry `sin(2φ+3ψ)`, so
`ox ∝ cos(θ_wind)`, `oy ∝ sin(θ_wind)`. The boost applies a **+x spatial phase gradient to the
full phasor coherently**:

    (ox', oy') = R(k_x·x) · (ox, oy),   R(α) = [[cos α, −sin α], [sin α, cos α]]

distributed back onto the ports proportionally (V0,V1 share the new `ox'`; V2,V3 share `oy'`,
keeping each port's intra-pair split). This rotates `ox+i·oy` by `exp(i k_x x)` — a genuine +x
traveling-wave boost on the channel the winding lives in. NOT the port-pairs (which the stalled
run showed is not a clean traveling wave).

K4 geometry consistency: ports {0,1} have px=+1 (toward +x), ports {2,3} have px=−1 — so the
phasor naturally pairs +x-hemisphere vs −x-hemisphere ports; a +x-progressing phase on
`ox+i·oy` is the physical advection direction.

## §4 ANTI-STALL — linear-pulse smoke test FIRST (≤2 boost variants)

Before touching the self-trap, validate the boost on a **sub-saturation linear pulse** (no
self-trap; a localized below-A²_op14 phasor blob with the same (ox,oy) structure):
- Seed → apply the coherent boost → confirm the **centroid MOVES** (v>0, monotone in k_x).
- **LINEAR moves** → boost works → proceed to the full test.
- **LINEAR does NOT move after 2 coherent-boost variants** → boost is the blocker; STOP, write
  blocker + diagnosis here, return. (The last run stalled iterating past 2 tries — do NOT.)

Two variants budgeted: (V1) reset-each-step phasor rotation (re-impose `exp(i k_x x)` each step),
(V2) one-shot phase gradient at t=0 then free evolution. If both fail → BLOCKED-boost.

## §5 The decisive disambiguation (the result either way)

Once the boost moves a LINEAR pulse, apply the SAME boost to the SELF-TRAP (Arm-C, A²≈8.9):

- **LINEAR moves but SELF-TRAP does NOT (v≈0)** → the saturated knot is **genuinely PINNED**
  (frozen-clock c_local→0). **CONTRADICTS** Grant cleanly (stable because static, not via motion).
  A real, clean finding — report as CONTRADICTS-via-PIN.
- **SELF-TRAP moves AND retention rises with v AND tracks native `τ_zx` (positive) MORE than the
  LINEAR control** → **SUPPORTS** Grant. Apply `ave-discrimination-check` before ANY positive
  framing (the prior "MOVES" positive collapsed under audit on LINEAR-control + saturated-while-
  moving + baseline-fairness axes).

## §6 The test (if the boost validates)

Sweep v ∈ {0, low, mid} via k_x ∈ {0, k_lo, k_mid}. Arms:
- **SELF-TRAP(v):** retention, FWHM, native `τ_zx`, peak-A trajectory (confirm saturated-while-moving).
- **LINEAR(v):** the SM-counterfactual — same boost on a non-self-trapping pulse.
- **BASELINE(v):** genuinely matched — same interior energy + A-trajectory (opposite-v superposition,
  NOT phase-scramble).

Fixed-peak-|E| across the sweep (no saturation-depth confound). Instrument peak-A throughout.

## §7 Forward-predicted SIGN (pre-run, no fit — ave-driver-script-honesty)

Given §1 (S=0 frozen core at A²≈8.9 ⇒ c_eff→0) the **substrate-default prediction is PIN**:
the LINEAR control advects (sub-saturation, c_eff≈c), the SELF-TRAP does NOT (v_knot/v_linear ≪ 1),
retention(v) **flat-or-falling**, native-τ_zx-vs-stability correlation **≤ 0** (the frozen core's
τ_zx is the static rupture-floor stress, not a motion-induced stabilizer). **Predicted verdict:
CONTRADICTS-via-PIN.** A SUPPORTS (knot advects + retention(v) slope>0 + positive τ_zx tracking)
would overturn the static-trap canon and triggers full `ave-discrimination-check`.

## §8 Discipline applied (mandatory set)

`substrate-native-check` CP8 (boost the durable host; matched baseline; PIN/null = clean structural
finding — DONE: confirmed S=0 frozen-core regime at A²≈8.9, PIN is canonically-expected) ·
`phase-space-coordinate-check` (native τ_zx is a real-space stress field read by the native observer
— MATCH; boost phasor (V0+V1,V2+V3) is the genuine quadrature of the planted winding, no fabrication
— MATCH) · `ave-discrimination-check` (LINEAR SM-counterfactual + matched BASELINE + interpretive-
alternatives — MANDATORY before any positive) · `consistency-vs-emergence` (Class D: novel motion-
stability prediction) · `ave-canonical-source` (ALPHA from `ave.core.constants`; `verify_constants`) ·
`ave-driver-script-honesty` (forward-predicted sign above; no fit) · `ave-evidence-framing-discipline` ·
Pure-AVE-corpus.

## §9 Deliverables

1. This brief.
2. `src/scripts/vol_1_foundations/motion_stability_bemf_cosserat_probe.py`.
3. `research/2026-06-04_motion-stability-bemf-cosserat-result.md` — VERDICT, the LINEAR-moves-but-
   knot-pins disambiguation, retention(v), native-τ_zx-vs-stability correlation, A-trajectory, the
   Maxwell-vs-Cosserat contrast, honest framing, auditor queue.
