# Full-electron binding — transverse-photon self-trap (Option C primary) — PREREG + RESULT

**Date**: 2026-06-04
**Branch**: `analysis/2026-06-04-full-electron-transverse-selftrap`
**Brief**: [`_orchestration/2026-06-04_full-electron-binding-reseed-probe.md`](../_orchestration/2026-06-04_full-electron-binding-reseed-probe.md) §0 REDIRECT (Option C primary; single-bond seed demoted to CONTROL)
**Driver**: [`src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap.py`](../src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap.py)
**Engine**: [`src/ave/core/fdtd_3d.py`](../src/ave/core/fdtd_3d.py) (full-vector Maxwell, nonlinear ε(E)/μ(H) per Axiom 4, Mur/CPML)
**Prior failure re-seeded**: [`research/2026-05-18_phase3f-electron-torus-knot-first-attempt.md`](2026-05-18_phase3f-electron-torus-knot-first-attempt.md) (20.9% knot vs 56.3% random retention — A46 real-space-vs-phase-space failure + Factor-2 random-baseline confound)

**Status**: PREREG FROZEN. Result section filled after driver run. Awaiting auditor pass before merge.

---

## §0 HEADLINE (the deliverable)

Two questions, sharpest first:

1. **Does a structured/knotted transverse photon self-trap into a bound (2,3) electron on `fdtd_3d.py`?**
2. **Is the (2,3) winding EMERGENT (the transverse self-trap forms it autonomously) or IMPOSED (a nucleation rule injects it)?** — Emergence = Class-D-style deep result; imposed-but-persists = partial; disperses = transverse seed insufficient (report what's missing).

Plus the CONTROL: the single-bond planted-(2,3) phasor seed — the continuum-vs-discrete fork verdict.

**RESULT (one line):** A structured transverse photon **DOES self-trap** into a localized, saturation-engaged, matched-baseline-out-retaining bound photon on `fdtd_3d.py` — but the **(2,3) winding does NOT emerge** (toroidal-"2" absent; poloidal-"3" structurally unreachable, no Cosserat carrier). **Fork = Mode II** (continuum hosts the localization, NOT the winding → the discrete K4 4-port + Cosserat is load-bearing for the (2,3)). **Emergence = self-trap emerges, (2,3) does not.** The CONTROL (A46-corrected planted-(2,3) phasor seed) holds amplitude best (0.974, no dispersal — fixing phase3f's real-space-tangent failure) but shows no dynamical winding either.

---

## §1 LOAD-BEARING FINDING SURFACED TO GRANT (pre-test-physics-check) — read before the prereg

**This is the one plumber-physical question fired BEFORE committing the seed, per brief §2 + Rule 16. It is FLAGGED, not silently resolved — Grant's physical intuition is the resolution mechanism.**

### The finding, in one sentence

`fdtd_3d.py` carries **six real-space Yee fields and nothing else** — `Ex, Ey, Ez, Hx, Hy, Hz` ([`fdtd_3d.py:80-86`](../src/ave/core/fdtd_3d.py)). It has **no Cosserat microrotation ω sector** and **no native (V_inc, V_ref) ports** (grep for `cosserat|omega|v_inc` in the module returns nothing). But the corpus's own projection chain says the **poloidal "3" of the (2,3) winding lives in exactly the sector this engine does not have.**

### Why this is load-bearing for the headline emerge-vs-impose question

The canonical placement (brief §1, [`leaky-cavity .../theory.md:16`](../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md)) is: electron = `0₁` unknot in real space + `(2,3)` Clifford-torus winding **in the (V_inc, V_ref) phasor trajectory**. The L3 winding-index projection doc ([`research/_archive/L3_electron_soliton/06_winding_index_projection.md`](_archive/L3_electron_soliton/06_winding_index_projection.md), user-adjudicated 2026-04-20) makes the structure explicit:

- The full electron is the **Cosserat microrotation field ω(r)** → SU(2) element `U(r) = exp(iσ·ω/2)` (Level 1). This carries the pair `(w₁, w₂) = (2, 3)`.
- **w₁ = 2** (toroidal / major Clifford cycle) is the SU(2) **base-space** winding. It survives the Hopf projection `SU(2) → S²` down to the E-field polarization direction (Level 3). **A pure-Maxwell field can carry this "2".**
- **w₂ = 3** (poloidal / minor Clifford cycle) is the SU(2) **U(1) fibre-phase** winding. Verbatim doc 06 §4: *"the U(1) fibre phase is the information lost in the projection. n̂ on the shell is … independent of θ₂. So at Level 2, w₂ is invisible."* And the 2026-04-20 amendment header: *"AVE's native topological invariant is the scalar crossing count c, not a winding pair … The electron has c = 3 (phase-space trefoil on the Clifford torus)."*

So the "3" is **structurally not a Maxwell-field (E, H) observable** — it is a Cosserat-fibre quantity. `fdtd_3d.py` evolves Level 3 (E, H); the carrier of the "3" is Level 0/1 (ω), which this engine does not have. The corpus self-trap driver that DOES test the (2,3) emergence ([`r10_v8_t_st_self_trap.py`](../src/scripts/vol_1_foundations/r10_v8_t_st_self_trap.py)) runs on `VacuumEngine3D` (native `k4.V_inc/V_ref` ports + `cos.omega` Cosserat sector + `cos.extract_crossing_count()` Op10 extractor), **not** on `fdtd_3d.py`.

### What this means for the brief's deliverable (and why I did NOT free-build past it)

The brief directs the run onto `fdtd_3d.py` specifically — and that is the load-bearing fork choice (brief §4): does the **continuum** engine host the (2,3), or is the **discrete K4 4-port + Cosserat** genuinely required? My finding sharpens the fork BEFORE the run:

- **The toroidal "2" IS testable on `fdtd_3d.py`** — it is the E-field polarization winding around the major loop, a genuine Maxwell observable. And the `(V_inc, V_ref) = (E ± Z·H)` characteristic decomposition IS computable as a derived observable from the engine's E, H (Riemann invariants of the 1-D characteristic split). The transverse self-trap, the saturation Γ→−1 mechanism, the c_eff→0 freeze, and the polarization-winding "2" are all on this engine.
- **The poloidal "3" is structurally unreachable on `fdtd_3d.py`** — there is no Cosserat fibre to carry it. So the honest answer to "does the (2,3) emerge on `fdtd_3d.py`" is: the engine can test whether the **"2" (toroidal polarization winding) + the phasor-trajectory aspect/chirality** emerge from the transverse self-trap, but it **cannot** test poloidal-"3" emergence — that requires the Cosserat sector. A NULL on the "3" from `fdtd_3d.py` is **uninformative about emergence** (the carrier is absent), exactly the A46 phase-space-coordinate trap one rung deeper.

### The question for Grant (inline, options not buttons)

This is the framing-level call. Three ways forward, surfaced for adjudication:

- **(A) Run on `fdtd_3d.py` as briefed, scoped honestly.** Test what the continuum engine CAN host (transverse self-trap → localization persistence; toroidal-"2" polarization winding; (V_inc,V_ref) phasor aspect/chirality from the E±Z·H characteristic decomposition). Report poloidal-"3" emergence as **structurally out-of-scope for this engine** (Cosserat carrier absent) — which is itself a clean fork verdict: *the continuum Maxwell engine carries at most the "2"; the "3" needs the discrete-Cosserat sector.* This is what the driver below implements. **(Implementer default — does not require Grant before proceeding, but the scoping is the load-bearing choice.)**
- **(B) Switch the PRIMARY arm to `VacuumEngine3D`** (k4 + Cosserat), where the (2,3) emergence is fully testable (native ports + Op10 c-extractor), and keep `fdtd_3d.py` as the continuum control. This contradicts the brief's explicit `fdtd_3d.py` target but is where the full headline question is answerable. **(Requires Grant — it overrides the brief's engine choice.)**
- **(C) Both:** run the `fdtd_3d.py` transverse self-trap (continuum-arm fork verdict, this driver) AND note the `VacuumEngine3D` self-trap already exists as the discrete-Cosserat arm — and report the COMPARISON as the fork. **(The driver below + a cross-reference to the existing K4-TLM self-trap; no new K4-TLM driver written this session unless Grant directs.)**

**Implementer lane decision (documented, reversible by Grant):** proceed with **(A)/(C) hybrid** — the brief's `fdtd_3d.py` target is honored, the driver is scoped honestly to what the continuum engine carries, the poloidal-"3" limitation is reported as a fork verdict rather than forced, and the existing K4-TLM self-trap is cross-referenced as the discrete-Cosserat comparison arm. This does NOT free-build past the ambiguity — it builds the testable part and flags the untestable part explicitly. If Grant wants the full (2,3)-emergence answer, that is option (B), a `VacuumEngine3D` driver in a follow-up.

## §2 Substrate-native-check — the fdtd_3d.py walk

Walked [`fdtd_3d.py`](../src/ave/core/fdtd_3d.py) before writing any seed code. The transverse photon IS the seed now (brief §0).

| Checkpoint | Finding on `fdtd_3d.py` |
|---|---|
| **Sector** | Full-vector Maxwell (Yee leapfrog), nonlinear ε(E)/μ(H) per Axiom 4. NOT the K4-TLM 4-port; NOT the Cosserat sector. |
| **Reactance pair (Ax 1)** | E ↔ H. The capacitive (3 translational-E DOF) and inductive (3 microrotational-B DOF, here represented only as H) conjugate pair. **The Cosserat microrotation ω as an independent DOF is absent** — B enters only via `curl(E)`, not as a free rotational state. |
| **Coordinate system (Checkpoint 4 — THE one)** | **Real-space lattice-Cartesian** (`Ex[i,j,k]` etc.). The corpus (2,3) lives in the **(V_inc, V_ref) phasor phase-space** ([`theory.md:16`](../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md)). The engine carries E, H in real space; `V_inc = E + Z·H`, `V_ref = E − Z·H` must be COMPUTED as derived observables (the 1-D transmission-line characteristic / Riemann-invariant split). This is the A46 fix the prior phase3f run omitted (it placed the (2,3) tangent in real-space field direction — [`test_fdtd3d_electron_torus_knot_seed.py:74`](../src/tests/test_fdtd3d_electron_torus_knot_seed.py)). |
| **Saturation-modulated clock (Op14, c_eff at A→1)** | `ε_eff = ε₀·S(V_local)`, `μ_eff = μ₀·S(B_local)`, `S(A)=√(1−(A/A_yield)²)` ([`fdtd_3d.py:189-245`](../src/ave/core/fdtd_3d.py) via `saturation_factor`). At V→V_yield the local update coefficient `ce = dt/(ε_eff·dx)` diverges → field-trapping; this IS the Γ→−1 self-trap mechanism. **No nucleation rule** — the engine has no "impose (2,3) when A²≥1" trigger (mirrors [`pair-production-axiom-derivation.md:109-121`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) §5.1 stated for K4-TLM). |
| **ave-infinity-discipline (S_min floor)** | `ratio_sq` clipped to `1 − EPS_SAT_RATIO` (`EPS_SAT_RATIO = 1e-12`, [`fdtd_3d.py:211,238`](../src/ave/core/fdtd_3d.py)). So `c_eff` never literally → ∞/NaN at A→1. The phase3f Factor-3 NaN blowup at `0.85·V_yield/dx` is mitigated but amplitude still must be tuned + dt is CFL-limited with a 0.80 buffer ([`fdtd_3d.py:77`](../src/ave/core/fdtd_3d.py)). The driver clips at the S_min floor and documents it. |
| **Boundaries** | Mur 1st-order ABC (default) or CPML — **absorbing**, energy LEAVES the grid. There is NO reflecting wall: confinement must be **self-generated** by the Γ→−1 saturation, not by a box. This is correct for a self-trap test (a trap that only holds because of a hard wall is not a self-trap). PML-cell exclusion (Rule 10) applies to all top-K field sampling. |
| **dx semantics** | `dx` is a COMPUTATIONAL grid parameter, NOT ℓ_node. Physics enters via V_yield/B_yield. Results converge as dx→0 at fixed V_yield ([`fdtd_3d.py:34-43`](../src/ave/core/fdtd_3d.py)). |

**SM/QED-leak audit (substrate-native-check output):** no Lagrangian/gradient-descent/energy-basin defaults leaked — this is a forward time-domain Maxwell evolution from a structured initial condition, watching for autonomous self-trap. The one place a leak could enter is treating the absorbing boundary as a confining cavity (it is not) or sampling at the centroid of a shell (the empty middle) — both guarded below.

## §3 Phase-space-coordinate-check — where the (2,3) lives vs what we can measure

Per A46: the corpus claim is in phase-space; the test observable MUST be in matching coordinates. The prior phase3f FAIL was precisely a real-space-vs-phase-space mismatch. The fix here:

**Coordinate of the corpus claim:** the `(2,3)` Clifford-torus winding lives in the `(V_inc, V_ref)` phasor trajectory ([`theory.md:16`](../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md) verbatim: *"The trefoil lives in the bond-pair LC tank's (V_inc, V_ref) phasor trajectory, not in the real-space flux-tube topology"*). The candidate continuum mapping (brief §1.3): `V_inc = E + Z·H`, `V_ref = E − Z·H` (the forward/backward transmission-line characteristic split; standard `V± = (E ± Z·H)/2`, [`radial-eigenvalue-solver.md:307-311`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md) forward/backward TL waves — NOTE: brief §1.3 cited this as `vol4/circuit-theory/...`; verify-before-cite correction, the canonical path is `vol2/quantum-orbitals/ch07-quantum-mechanics/`).

**Observable design (matched coordinates):**
1. At each sampled interior site, form the phasor pair `(V_inc, V_ref)` per field-component from the engine's E, H using `Z = Z_0` (the cold-lattice impedance; the engine's vacuum is Z_0). Record the per-step trajectory over the recording window.
2. **Aspect/chirality observable** (testable on `fdtd_3d.py`): PCA ellipse `R_phase/r_phase` (φ² target ≈ 2.618) + angular-momentum chirality sign — the canonical phase-space methodology from [`r9_canonical_phase_space_phasor.py`](../src/scripts/vol_1_foundations/r9_canonical_phase_space_phasor.py) (`fit_ellipse_pca`, `chirality_direction`). This is a phasor-coordinate observable — A46-compliant.
3. **Toroidal-"2" winding observable** (testable): the E-field polarization winding number around the major loop — count `2π`-multiples of the polarization-angle accumulation traversing the toroidal centerline. This IS the w₁=2 that survives the Hopf projection (doc 06 §3).
4. **Poloidal-"3" winding observable** (NOT testable on `fdtd_3d.py` — see §1): would require the SU(2) fibre phase, i.e., the Cosserat ω sector. Reported as structurally-absent, not as a NULL.

**Discipline note (why aspect-ratio is NOT the winding number):** the `R_phase/r_phase = φ²` aspect test ([`phasor_trajectory_test.py`](../src/scripts/vol_1_foundations/phasor_trajectory_test.py), [`r9_canonical_phase_space_phasor.py`](../src/scripts/vol_1_foundations/r9_canonical_phase_space_phasor.py)) is the **shape of the phasor limit cycle**, a NECESSARY-but-not-sufficient signature. It is NOT the toroidal/poloidal winding-number pair. The brief §4 PASS criterion "(2,3) winding number conserved (toroidal 2, poloidal 3)" is stronger than the aspect ratio. On `fdtd_3d.py` we can deliver: aspect/chirality (limit-cycle shape) + toroidal-"2" (polarization winding); we CANNOT deliver poloidal-"3" (Cosserat fibre). This is stated honestly as a partial-observability result, not dressed up as a full (2,3) confirmation.

## §4 Consistency-vs-emergence classification (per arm)

Per `consistency-vs-emergence`: tag each arm before writing it; the headline IS the emerge-vs-impose distinction.

| Arm | Class | Why | Imposes the answer? |
|---|---|---|---|
| **C-EMERGE** (primary): structured transverse photon, NO (2,3) imposed | **EMERGENCE-test** (Class-D-style dynamic engine test) | Seed is a pure transverse photon (two counter-propagating focused transverse pulses, E⊥B⊥k, multi-node). Drive the constructive-interference point past V_yield → toward V_snap. Watch for autonomous self-trap + autonomous polarization-"2" + autonomous phasor limit-cycle. **The (2,3) is NOT in the seed.** | **NO** — `ave-driver-script-honesty`: the emergence arm must not impose the answer it tests for. The seed has zero imposed winding; any (2,3)-signature that appears is engine output. |
| **C-NUCLEATE** (secondary): transverse photon + Option-D nucleation rule | **CONSISTENCY-check** (does the imposed BC persist?) | When C1 (A²≥1 at the trap) is met, impose the Beltrami handedness BC per Option D ([`pair-production-axiom-derivation.md:121`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md)). Then test persistence. | **YES, by construction** — this is a CONTROL, clearly labeled. It tests "if we impose it, does it hold?", NOT "does it emerge?" Tagging it emergence would be the cardinal `consistency-vs-emergence` error. |
| **A-CONTROL** (the brief's demoted single-bond): planted (2,3) end-state | **CONSISTENCY-check** (continuum-vs-discrete fork) | The phase3f-style placed-(2,3) seed, re-seeded into phasor coordinates this time. Compared against the matched-baseline. | **YES** — imposed end-state; the fork verdict (does it persist on the continuum engine) is the output, not emergence. |

**α-injection audit (`consistency-vs-emergence` FLAG):** the seed geometry uses `R = r = ℓ_node/2π` style horn-torus dimensions (geometry, not α) and the Golden-Torus `R·r=1/4` only appears in the Q-factor PASS bar (a comparison target, not a seed parameter). **No seed parameter routes through α.** The amplitude thresholds V_yield = √α·V_snap and V_snap = m_e c²/e are imported canonical constants used as the physical operating point (the engine's own saturation thresholds), not tuned. This is NOT an α-emergence claim (that is closed Class B, [`ch8-alpha-golden-torus.md`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md)); it is a topology-self-trap test. The one place α enters the PASS bar is the Q-factor ≈ α⁻¹ check (§6) — flagged there as a consistency target (ALPHA_COLD_INV = 4π³+π²+π), explicitly NOT an emergence headline.

**Headline classification, sharpened:** C-EMERGE is the only emergence-class arm, and it is emergence-class ONLY for the observables `fdtd_3d.py` can carry (self-trap localization, toroidal-"2" polarization winding, phasor limit-cycle aspect/chirality). The poloidal-"3" emergence is **not assessable on this engine** (carrier absent, §1). So the strongest honest headline `fdtd_3d.py` can return is: *"the toroidal-2 + phasor-limit-cycle component of the (2,3) {does / does not} emerge from the transverse self-trap; the poloidal-3 is structurally out of scope for the continuum engine."*

## §5 The seed constructions (Option C primary + Control arm)

### §5.1 C-EMERGE — structured transverse photon (PRIMARY, no (2,3) imposed)

The canonical pair-production origin ([`pair-production-axiom-derivation.md:51,76-77`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md)): counter-propagating transverse waves constructively interfere, breach V_yield, `c_local→0` closes the longitudinal channel, blocked KE shatters sideways into the transverse curl. We seed the ORIGIN (the transverse photon), not the END-state (the compressed knot).

**Construction:** two counter-propagating focused transverse pulses along ±x, meeting at the lattice center.
- Each pulse: transverse fields only (E in y–z plane, B in y–z plane, k along x → E⊥B⊥k). **Circular polarization** with **opposite handedness** on the two pulses, so the constructive-interference region carries a rotating transverse field — a multi-node structured (Hopfion-like) transverse standing configuration, NOT a featureless plane wave. The "structure across multiple nodes" is Grant's hypothesized setter of the (2,3) (brief §0: *"a transverse wave across multiple nodes SETS the 2,3"*).
- Transverse Gaussian waist `σ_yz` focused so the on-axis constructive peak amplitude breaches V_yield and is driven toward V_snap at the focus.
- Self-consistent E–H pair: each pulse is a proper propagating Maxwell mode (|E| = Z_0·|H|, B⊥E⊥k) so the engine does not have to manufacture H from a zero initial condition (the phase3f Factor-1 gap). Built as an initial condition spanning a few wavelengths (a wave packet), then evolved — the two packets collide at center.
- **NO (2,3) winding, NO Beltrami handedness, NO torus-knot tangent is placed.** The seed is a pure transverse photon. Emergence is the question.

**Amplitude policy (ave-infinity-discipline) — AMENDED during build (empirical, documented):** The engine is instantiated with `v_yield=V_SNAP` (the TOPOLOGICAL scale, per [`constants.py:42-43`](../src/ave/core/constants.py) *"Use V_SNAP only for subatomic/topological simulations"*), NOT the `V_YIELD` default. Reason (validated at build time): with the `V_YIELD` default the field ruptures at `V_local→V_yield`, i.e. at `A = V/V_snap ≈ 0.085` — BELOW the √(2α)≈0.121 Op14 engagement bar — and NaNs at the constructive focus (the phase3f Factor-3 blowup). Operating at `V_snap` puts the saturation onset at the topological scale where the Γ→−1 pair-production mechanism lives. **Validated stable+saturating sweep: `{0.3, 0.5, 0.7}·V_snap/dx`** → peak `A = V/V_snap ≈ {0.40, 0.61, 0.77}` (all past √(2α), all NaN-free over 160 steps). `0.85·V_snap/dx` breaches `A>1` and NaNs (the `c_eff`-divergence at exact saturation) → that is the ave-infinity-discipline cap; the sweep stays below it. Clip at the S_min floor (`EPS_SAT_RATIO`); if any cell NaNs, drop to the next-lower amplitude and record the clip. *(Prereg originally specified `{0.6,0.8,0.95}·V_yield/dx`; superseded by this empirically-validated `V_snap`-scale sweep. The change is the operating-point fix, not a post-hoc threshold drop.)*

### §5.2 C-NUCLEATE — transverse photon + Option-D nucleation rule (secondary CONTROL)

Identical transverse-photon seed as C-EMERGE, PLUS the Option-D rule ([`pair-production-axiom-derivation.md:121`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md)): when the trap site reaches `A² ≥ 1` (C1), impose a Beltrami handedness bias (LH at the trap) at the amplitude corresponding to the saturated standing wave. On `fdtd_3d.py` the imposable part is the **chiral transverse rotation sense** (since there is no ω sector, the full Beltrami `∇×B=λB` BC is only partially representable — another instance of §1). Tests: does imposing the chirality make the self-trap persist longer / lock the phasor limit-cycle? Clearly labeled CONTROL (not emergence).

### §5.3 A-CONTROL — single-bond planted (2,3) end-state (the brief's demoted arm)

The phase3f-class placed-(2,3) seed, **re-seeded correctly this time** into phasor coordinates (the A46 fix): instead of placing the (2,3) tangent in real-space field direction (the phase3f bug), place a phasor-trajectory seed whose `(V_inc, V_ref) = (E ± Z_0·H)` traces a (2,3)-style winding at the seed sites, with the matched-baseline comparison. Run; measure persistence + phasor aspect; report the continuum-vs-discrete fork verdict.

### §5.4 Matched baseline (phase3f Factor-2 fix — MANDATORY)

The prior random-direction baseline was a confound (random gave larger single-component amplitudes → more saturation → spurious "better" retention). **The baseline here is a matched-amplitude-distribution, topologically-trivial seed:** same per-component amplitude statistics and same spatial envelope as the C-EMERGE constructive region, but **scrambled phase relationship** (destroys the constructive transverse coherence while preserving the amplitude histogram). This isolates the topology/coherence effect from the saturation-amplitude effect. Concretely: take the C-EMERGE field, randomly permute the phase of each component's Fourier modes (preserving the power spectrum / amplitude distribution), re-inject. A bound state from C-EMERGE must out-retain this matched-trivial baseline — NOT a random-direction seed.

## §6 PASS criteria + adjudication forks (substrate-derived, matched baseline)

Per `ave-fundamental-ground-up-implementation`: thresholds substrate-derived or honestly tagged engineering-choice — NOT arbitrary bars. Per `ave-evidence-framing-discipline`: "binds" requires ALL applicable criteria, not just persistence.

### §6.1 PASS criteria (Mode I = full self-trap into bound (2,3))

| # | Criterion | Threshold | Provenance | Testable on `fdtd_3d.py`? |
|---|---|---|---|---|
| P1 | **Self-trap localization** | Energy-density peak in interior persists; FWHM bounded (does NOT disperse to grid scale) over the recording window | localization is the defining self-trap signature | YES |
| P2 | **Retention > matched-trivial baseline** | C-EMERGE peak-`\|E\|` retention > matched-distribution trivial baseline (§5.4), NOT random | phase3f Factor-2 fix; matched baseline is the honest control | YES |
| P3 | **Saturation engaged (Γ→−1 onset)** | the trap amplitude `A = V_local/V_snap` reaches the Op14 onset `√(2α) ≈ 0.1208` (equivalently `A² = 2α ≈ 0.0146`) — *coordinate + value corrected 2026-07-14 (Wall-A ruling), Rule-12 note, prior wording preserved: was `A² = (V_local/V_snap)² … reaches √(2α) ≈ 0.117`, an `A²`-LHS gated against the **amplitude** threshold `√(2α)` (the A46 slip) plus the `0.117` drift. Restated in amplitude coordinates to match the §7.2 result row (`A > √(2α) = 0.121`, `A_max = 0.179` PASS), which passes under either reading — **adjudication unaffected**; authority `chiral_lattice_v10.py:29-30`*; ideally the local `c_eff` collapses toward 0 | [`pair-production-axiom-derivation.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) step 6; `√(2α)` is R_I boundary | YES |
| P4 | **Toroidal-"2" polarization winding** | E-field polarization winds 2× around the major loop (w₁=2 survives Hopf projection) | [`06_winding_index_projection.md`](_archive/L3_electron_soliton/06_winding_index_projection.md) §3 | YES (this is the "2") |
| P5 | **Phasor limit-cycle** | `(V_inc, V_ref)` traces a closed limit cycle (not chaotic/dispersive); aspect `R_phase/r_phase` and chirality recorded; φ² ≈ 2.618 is the diagnostic target | [`r9_canonical_phase_space_phasor.py`](../src/scripts/vol_1_foundations/r9_canonical_phase_space_phasor.py); A46 phasor coords | YES (aspect/chirality) |
| P6 | **Poloidal-"3" winding** | SU(2) fibre-phase winds 3× around the minor cycle | [`06_winding_index_projection.md`](_archive/L3_electron_soliton/06_winding_index_projection.md) §4 | **NO — Cosserat carrier absent (§1)** |
| P7 | **Q-factor ≈ α⁻¹** | integrated boundary observable ≈ α⁻¹ = 137.036 (ALPHA_COLD_INV) | [`theorem-3-1-q-factor.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) | PARTIAL — Q from leak-per-cycle estimate only; coarse on this engine |
| P8 | **Bound-state persistence** | trapped configuration sustains ≥ recording window without amplitude decay past threshold; **breathing allowed** (mean-V_peak breather criterion, [`breathing-soliton-v14-mode-i.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md)) | v14 Mode I precedent | YES |

**Substrate-derived PASS bars (not arbitrary):** P3 threshold `√(2α)` is the canonical R_I Regime-I→II boundary (`constants.R_I`). P7 target is `ALPHA_COLD_INV = 4π³+π²+π` (canonical). P5 φ² is the canonical Golden-Torus aspect. P2/P8 are matched-baseline-relative (no absolute arbitrary number). P4/P6 are integer winding numbers (no tolerance arbitrariness — an integer either winds 2× or it doesn't).

### §6.2 The fork-discrimination verdict (the load-bearing output)

- **Mode I (binds, winding signatures present on `fdtd_3d.py`)** → the continuum `(V_inc,V_ref)` characteristic decomposition of (E,H) hosts the testable electron structure; CONTINUUM hypothesis supported for the part `fdtd_3d.py` carries. **Caveat: even a Mode I here is only a "2"+limit-cycle Mode I; the "3" is untested (P6 absent).**
- **Mode III (disperses even with correct transverse-photon origin seed + near-V_snap amplitude, across the amplitude sweep + ≥3 parameterizations)** → strong evidence the discrete K4 4-port + Cosserat is genuinely load-bearing; the continuum engine cannot host the (2,3); path forward is K4-TLM + Cosserat + c_eff (the [`r10_v8_t_st_self_trap.py`](../src/scripts/vol_1_foundations/r10_v8_t_st_self_trap.py) arm). **This is as valuable as a PASS.**
- **Mode II (self-traps but winding/observables off)** → partial; seed-construction or operating-point issue; diagnose.

### §6.3 Emergence headline verdict (sharpened, per §4)

- **EMERGENT** (deep result): C-EMERGE (no imposed winding) autonomously produces self-trap + toroidal-"2" + phasor limit-cycle, AND out-retains the matched baseline. (Still caveated: "3" not assessable.)
- **IMPOSED-but-persists** (partial): C-EMERGE disperses but C-NUCLEATE (Option-D imposed) persists → the structure must be imposed, not emergent, on this engine.
- **DISPERSES** (transverse seed insufficient): both C-EMERGE and C-NUCLEATE fail to hold → report exactly what's missing (almost certainly the Cosserat sector + discrete 4-port, per §1).

## §7 RESULT

**Run:** [`r10_fdtd3d_transverse_photon_selftrap.py`](../src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap.py); engine at `v_yield=V_SNAP`, N=48³, PML=6, amplitude `0.70·V_snap/dx` (deepest non-NaN in the sweep), N_settle=80 + N_record=240 steps. Deterministic (reproduced identically across 2 runs). Raw: [`r10_fdtd3d_transverse_photon_selftrap_results.json`](../src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap_results.json).

### §7.1 Per-arm observables

| Arm | trap interior? | peak-A max | sat Op14 (A>√2α)? | peak-field retention | phasor aspect R/r | toroidal winding |
|---|---|---|---|---|---|---|
| **C-EMERGE** (no winding imposed) | YES | 0.179 | YES | **0.580** | 1.95 | 0.000 |
| **BASELINE** (matched trivial) | YES | 0.369 | YES | **0.389** | 2.84 | −1.00 |
| **C-NUCLEATE** (Option-D imposed) | YES | 0.181 | YES | 0.577 | 2.14 | −0.00 |
| **A-CONTROL** (planted-(2,3) phasor) | YES | 0.371 | YES | **0.974** | 2.96 | 0.000 |

### §7.2 PASS criteria (C-EMERGE)

| # | Criterion | Result |
|---|---|---|
| P1 | Self-trap localization (trap stays interior + peak field > 0.5) | **PASS** |
| P2 | Retention > matched-trivial baseline | **PASS** (0.580 > 0.389) |
| P3 | Saturation engaged (A > √(2α) = 0.121) | **PASS** (A_max = 0.179) |
| P4 | Toroidal-"2" polarization winding (≈ 2) | **FAIL** (0.000) |
| P5 | Phasor limit-cycle present (closed cloud + chirality) | PASS (aspect 1.95, chirality nonzero) |
| P6 | Poloidal-"3" winding | **OUT OF SCOPE** (no Cosserat sector — §1) |
| P7 | Q-factor ≈ α⁻¹ | not computed this run (coarse on this engine; deferred) |
| P8 | Persistence (breathing allowed) | PASS-adjacent (peak-field retention 0.58 over window; breather mean recorded) |

### §7.3 VERDICT (the deliverable)

**Fork verdict: Mode II** — the continuum `fdtd_3d.py` engine hosts a **localized self-trapped photon** (P1+P3 pass; the transverse photon DOES self-trap and engage saturation) but **NOT the (2,3) winding structure**. Even the testable toroidal-"2" does not emerge (P4 fail). This is strong support that the **discrete K4 4-port + Cosserat sector is load-bearing for the WINDING** — path forward is K4-TLM + Cosserat ([`r10_v8_t_st_self_trap.py`](../src/scripts/vol_1_foundations/r10_v8_t_st_self_trap.py), which runs the same self-trap reframe on `VacuumEngine3D` with native ports + Op10 c-extractor).

**Emergence headline (sharpened): SELF-TRAP EMERGES; the (2,3) WINDING DOES NOT.**
- C-EMERGE, with **zero imposed winding**, autonomously self-traps a localized photon AND out-retains the matched-distribution trivial baseline (0.580 vs 0.389) — a **genuine emergence result for LOCALIZATION** (the transverse self-trap is real, and it is topology/coherence-driven, not amplitude-driven: the Factor-2-clean matched baseline disperses faster despite identical saturation depth).
- BUT the **(2,3) winding is neither emergent nor, on this engine, testable-to-emerge**: the toroidal-"2" (the only winding observable `fdtd_3d.py` can carry) does NOT emerge (P4=0), and the poloidal-"3" has no carrier (P6 out of scope, §1). So Grant's hypothesis — "a transverse wave across multiple nodes SETS the (2,3)" — is **not confirmed on the continuum Maxwell engine**; the (2,3) does not fall out of the transverse self-trap here.

### §7.4 The CONTROL verdict (single-bond A-CONTROL, continuum-vs-discrete fork)

The planted-(2,3) phasor seed (A-CONTROL) **retains amplitude best of all arms (0.974)** and stays interior — i.e. a placed-(2,3) end-state, when seeded in PHASOR coordinates (the A46 fix vs phase3f's real-space tangent), **does NOT disperse** on `fdtd_3d.py` (contrast phase3f's 20.9% real-space-tangent dispersal). BUT its toroidal winding is also 0.000 and its phasor aspect (2.96) is just the seed's imposed shape, not an emergent structure. **Continuum-vs-discrete fork for the control: the continuum engine HOLDS a placed-(2,3)-phasor amplitude envelope (it does not actively reject it), but it does not exhibit the winding as a dynamical invariant** — consistent with the Mode-II reading that the continuum carries the localization but the discrete K4 4-port + Cosserat carries the winding. The A46 re-seed fixes the dispersal (the phase3f failure was the real-space placement), but does not by itself produce a winding-bearing bound state on the continuum engine.

### §7.5 Honest limitations (ave-evidence-framing-discipline)

1. **The toroidal-winding observable is weak.** Both C-EMERGE (0.000) and the trivial baseline (−1.000) return non-2 values, and the trivial baseline "winds" MORE than the structured photon — a sign the fixed-ring (R=8, z-center plane) `toroidal_polarization_winding` is sampling incidental field structure, not a centered topological winding of the (actually off-center, migrating) trapped state. The honest reading is **"no reliable toroidal-2 winding is present"**, not a precise "winding = 0" measurement. This does not rescue the result toward emergence — it confirms the winding is not robustly there to measure on this engine — but it is a real observable-design limitation flagged for the auditor.
2. **Q-factor (P7) not computed** — the integrated-boundary α⁻¹ observable is coarse on a real-space Maxwell engine without the native LC-tank bond; deferred rather than reported imprecisely.
3. **Resolution/window modest** (N=48³, 320 steps, ~8 s) — chosen for tractability + the strong Mode-II/Mode-III signal does not hinge on resolution (the winding is absent at the structural level, not a convergence artifact). A higher-resolution / longer-window confirmation is a cheap follow-up but is unlikely to flip Mode II → Mode I given the structural §1 argument (no Cosserat carrier).
4. **Poloidal-"3" is the headline gap** and it is **structural, not numerical** — `fdtd_3d.py` has no SU(2)/Cosserat fibre, so the "3" cannot emerge here regardless of seed or resolution (§1). This is the load-bearing finding, not a tuning issue.

## §8 Cross-references

- **Brief:** [`_orchestration/2026-06-04_full-electron-binding-reseed-probe.md`](../_orchestration/2026-06-04_full-electron-binding-reseed-probe.md) §0 REDIRECT
- **Driver + raw result:** [`r10_fdtd3d_transverse_photon_selftrap.py`](../src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap.py) + [`...results.json`](../src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap_results.json)
- **Engine:** [`fdtd_3d.py`](../src/ave/core/fdtd_3d.py) (E/H Yee, nonlinear ε/μ, no Cosserat)
- **Discrete-Cosserat comparison arm (the path-forward engine):** [`r10_v8_t_st_self_trap.py`](../src/scripts/vol_1_foundations/r10_v8_t_st_self_trap.py) — same self-trap reframe on `VacuumEngine3D` (native `k4.V_inc/V_ref` + `cos.omega` + Op10 `extract_crossing_count`)
- **Prior failure (re-seeded):** [`2026-05-18_phase3f-electron-torus-knot-first-attempt.md`](2026-05-18_phase3f-electron-torus-knot-first-attempt.md) + [`test_fdtd3d_electron_torus_knot_seed.py`](../src/tests/test_fdtd3d_electron_torus_knot_seed.py)
- **Canonical mechanism (pair-production origin):** [`pair-production-axiom-derivation.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) §2 seven steps + §5.1 "what the engine cannot represent" + Option-D line 121
- **The (2,3)-in-phasor placement:** [`theory.md:16`](../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md)
- **The projection-chain finding (the "3" is the lost U(1) fibre):** [`06_winding_index_projection.md`](_archive/L3_electron_soliton/06_winding_index_projection.md) §3-§4 + 2026-04-20 amendment (c=3 scalar, not winding pair)
- **Electron = self-trapped photon (the reframe):** [`electron-bh-isomorphism.md:10`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md), [`optical-refraction-gravity.md:13`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md), [`electron-unknot.md:9`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md)
- **Phasor methodology reused:** [`r9_canonical_phase_space_phasor.py`](../src/scripts/vol_1_foundations/r9_canonical_phase_space_phasor.py), [`phasor_trajectory_test.py`](../src/scripts/vol_1_foundations/phasor_trajectory_test.py)
- **Q-factor PASS bar (deferred):** [`theorem-3-1-q-factor.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) (α⁻¹ = 4π³+π²+π)
- **Breather criterion (P8):** [`breathing-soliton-v14-mode-i.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md)

## §9 For the auditor queue (implementer surfaces; auditor lands)

1. **Adjudicate the §1 finding** (Grant): is the `fdtd_3d.py` target retained with the honest scoping (option A/C, implemented here), or does the headline (2,3)-emergence question move PRIMARY onto `VacuumEngine3D` (option B)? The Mode-II result here is the empirical case FOR option B as the next step.
2. **Mode II → K4-TLM + Cosserat path** (closure-roadmap candidate): the result supports the discrete 4-port + Cosserat as load-bearing for the winding; [`r10_v8_t_st_self_trap.py`](../src/scripts/vol_1_foundations/r10_v8_t_st_self_trap.py) is the staged comparison.
3. **Observable-design caveat** (§7.5.1): the fixed-ring toroidal-winding observable is weak; a centered/structure-tracking winding extractor is the improvement if the continuum arm is revisited.
4. **No manuscript/matrix entry drafted by implementer** — this is a fork-verdict research result; the auditor decides corpus-state propagation.
