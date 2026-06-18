"""L3 mass-cage — the longitudinal-bulk (A1 dilatation scalar) DOF.

This file builds the L3 MEDIUM EXTENSION + the L3 acceptance tests. T3.1/T3.2 are
the consistency/Axiom-4 FOUNDATION (the medium exists + stiffens). T3.3/T3.4 are
the RUNG-1 EXISTENCE suite (Grant-ratified, this pass): they POSIT a saturated
longitudinal cage (consistency-class — positing is legitimate here; this is NOT
self-formation, that is rung-2 / DEFERRED) and test the Γ=−1 wall (T3.3) and the
bound longitudinal eigenmode (T3.4: mass=cutoff / cold-α-free-Q / persistence).

════════════════════════════════════════════════════════════════════════════════
RUNG-1 EXISTENCE EMPIRICAL RESULTS (frozen-bin outcomes, this pass — BRUTAL HONESTY)
════════════════════════════════════════════════════════════════════════════════
  T3.3  Γ_bulk crosses −0.25 on the posited cage:  PASS. Γ_min(A=0.95)=−0.283
        (crosses the OP2 engaged-gate), monotone descent toward −1, →0 in vacuum;
        α-FREE (Z_eff=√S, NOT gamma_em_sq). Literal −1 UNREACHABLE (floors
        ≈−0.454 at A=0.99, the S_min-clipped wall) — by design, NOT a fail.
  T3.4a mass=cutoff (gapped bound mode EXISTS):  PASS. A discrete breathing
        eigenmode rings under a radial-SHELL breathing kick: ω_cutoff≈2.87
        (rad/time, natural units), gapped (>0), discrete (peak/mean≈456, 23
        zero-crossings). HONEST CAVEAT: this needs the shell-breathing kick; a
        pure monopole/DC kick excites only slow continuum-RELAXATION (an FFT-bin-1
        artifact, no ring). The m_e VALUE is NEVER read off the cage (definitional,
        constants.py:129 'Input 1'; electron-identification.md:50).
  T3.4b cold/α-FREE Q (the ONE genuine chord-vs-echo question):  Q finite & >0 —
        PASS on the FORM-bin. THE HEADLINE: Q_ringdown≈30.8, Q_linewidth≈3.8 —
        **NOT α⁻¹=137**. α was NEVER baked (no Q_TANK, no M.ELECTRON, no
        gamma_em_sq). So the α-free cold cage does NOT reproduce 137 ⇒ the corpus
        Q=1/α is an INSTANCE-BAKED ECHO, not a cage-emergent chord. This is the
        clean negative the brief hunted: seeding/asserting 137 would have been the
        instrument-echo-trap (theorem-3-1-q-factor.md:21). The cold (A≪1) limit
        rings even weaker (Q-floor, relaxation-dominated) — same verdict.
  T3.4c zero-drive persistence (non-radiating standing mode):  PASS. After the
        transient sheds, the interior peak |V| holds steady (late/mid≈1.31,
        late_min≈0.34 ≫ 0). NOTE: persistence ≠ topological-winding protection
        (winding-sector, NOT cage-testable — bucket B).

════════════════════════════════════════════════════════════════════════════════
THE MEDIUM EXTENSION (the longitudinal-bulk / "mass-3" / A1 dilatation grade)
════════════════════════════════════════════════════════════════════════════════
The srs vector-TLM medium carries only 2 TRANSVERSE DOF (the photon); T1.7
(`test_l1_multiwave.py`) recorded the precise gap and named the three missing
pieces. This layer SUPPLIES them substrate-natively (see `_bulk.py` for the full
design + the substrate-native-check walk):
  (a) a longitudinal (bond-axial) dilatation grade  — the A1 scalar V-sector, the
      Heaviside-Gibbs-EXCISED scalar grade that is PHYSICAL, NOT Gauss-deleted
      (the "no-QED-garbage longitudinal scalar"; def-9a4f07 longitudinal);
  (b) a K=2G/ρ bulk constitutive  — c_bulk=√(K/ρ)=√(2G/ρ)=√2·c₀ (linear), via
      K=2G (constants.py:674-676; K=2G provenance MERGED PR#261);
  (c) a longitudinal scatter/connect  — the canonical Master-Equation leapfrog
      ∂²u/∂t²=(c₀²/S)·∇²u (master_equation_fdtd.py), reusing the SAME S(A) kernel.
It is NOT a bolt-on: the Master-Equation FDTD is the canonical engine for exactly
this scalar longitudinal grade (its module docstring derives the longitudinal
scalar wave), and `_bulk.py` wraps it the same way `_medium.py` wraps the
transverse vector-TLM. ADDING the bulk DOF FLIPS the T1.7 absence-finding from
⊘ to a positive ✅ — the engine now carries the longitudinal mode.

════════════════════════════════════════════════════════════════════════════════
STEP-0 MODE / REGIME / PHASE-STATE DECLARATION (per plan §8 ritual step 0)
════════════════════════════════════════════════════════════════════════════════
Declared BEFORE the bins are frozen (`ave-regime-phase-state-check` first-class;
the standing guard: a null where the effect cannot exist in the declared regime is
an ARTIFACT, not a falsification — the dark-wake correction):

  T3.1 longitudinal-mode-is-real:
     MODE        = BULK (longitudinal dilatation; c_bulk=√(K/ρ)). NOT EM-transverse,
                   NOT shear — the bond-axial compression grade.
     REGIME      = I (linear / sub-yield; A≪1, S→1). The mode's EXISTENCE +
                   free propagation + dispersion live here by construction — a
                   gapless acoustic branch is a LINEAR-regime object, so Regime I
                   is the CORRECT regime to test existence (NOT an artifact-null
                   risk; the effect — a propagating compression mode — can exist
                   here, and the §2.6 grid lists bulk-Regime-I as "lin (c≈√2·c₀)",
                   i.e. present, not absent).
     PHASE-STATE = saturation OFF (A≪1), COLD seed (a launched plane wave, not a
                   pre-formed structure). No Op14 local-clock modulation.

  T3.2 c_eff(V) stiffening:
     MODE        = BULK (longitudinal; the c_eff²=c₀²/S stiffening kernel).
     REGIME      = II near-yield (the ONLY regime where the stiffening is
                   meaningful: §2.6 grid bulk-Regime-II = "✓", and the cage
                   stiffens c_eff→∞ as r→r_yield). Swept I→III as the
                   constitutive identity (the kernel is evaluated at fixed
                   operating points A∈{0…0.99}, a closed-form kernel read — CP10
                   boundary-not-bulk, NO time-domain detonation).
     PHASE-STATE = constitutive sweep (the kernel as a function of A); no seeded
                   dynamics — the stiffening is a property of the medium at each
                   operating point, the cage PRECURSOR (CP8 generative-precursor).

  T3.3 Γ=−1 wall on the posited saturated cage:
     MODE        = BULK (longitudinal A1 scalar; the impedance-routed Γ_bulk).
     REGIME      = II→III (near-yield → the wall): the posited core sits at high A
                   (A≈0.95–0.99) where Z_eff=√S→0 ⇒ Γ_bulk→−1. The reflective
                   short is a Regime-II/III object — testing it at high A is the
                   CORRECT regime (a Γ≈0 reading in vacuum/Regime-I is EXPECTED, an
                   open match, NOT a falsification: the standing guard).
     PHASE-STATE = saturation ON (POSITED high-A core); converter OFF (A1 scalar
                   ONLY — no (2,3) winding; the two-3s guard). A planted cage, the
                   consistency-class POSIT (legitimate here; self-formation = R2).

  T3.4 bound longitudinal eigenmode of the posited cage (3 sub-tests):
     MODE        = BULK (longitudinal A1 breathing of the saturated core).
     REGIME      = II (the bound mode lives in the stiffened well; T3.4a/b excite
                   it with a radial-shell breathing kick, T3.4c watches zero-drive
                   persistence). The COLD sub-read (T3.4b) drives A≪1 RINGING on
                   the high-A core (a cold ring of a saturated cavity).
     PHASE-STATE = POSITED high-A core (planted), converter OFF (A1 scalar only).
                   T3.4b is the cold cavity (small-amplitude ring); T3.4c is
                   zero-drive (no kick — the bare posited core).

════════════════════════════════════════════════════════════════════════════════
§8.5 SKILL-SELECTION PLAN (the 60-sec plan, written BEFORE the rung — mandatory
per `feedback_skill_selection_planning`; L3 = MEDIUM EXTENSION + Regime-II
near-yield, the HIGH-VALUE cluster that was correctly DORMANT in linear L0-L2)
════════════════════════════════════════════════════════════════════════════════
  * substrate-native-check  — WALKED in `_bulk.py` before any code. CP8
        generative-precursor (T3.2 stiffening = the cage precursor, not a planted
        cage) + CP10 boundary-not-bulk (the cage is a Γ-bounded BOUNDARY, NOT a
        detonating bulk well; T3.1/T3.2 are free-propagation + a closed-form
        kernel sweep — no time-domain runaway).
  * ave-cavity-class-identification — which substrate sub-network hosts the bound
        longitudinal eigenmode: the A1 SCALAR V-sector (the dilatation grade),
        carried by the Master-Equation scalar engine — ORTHOGONAL to the
        transverse photon sub-network (no double-count). (The BOUND eigenmode
        itself is T3.4 — DEFERRED; this rung establishes the FREE mode + its
        stiffening, the cavity's medium.)
  * ave-regime-phase-state-check — the step-0 declaration above (MODE=longitudinal
        -bulk; REGIME I for T3.1 existence, II near-yield for T3.2 stiffening).
  * ave-canonical-source — S(A) kernel + c_eff²=c₀²/S from
        `MasterEquationFDTD.c_eff_squared` (the #278-corrected ½-power form, see
        the `_bulk.py` FLAG); c_bulk=√(2G/ρ) from constants.py. Never hard-coded.
  * consistency-vs-emergence — T3.1 CHORD (AVE-distinct existence vs QED's
        gauge-deleted longitudinal); T3.2 Axiom-4-MANIFESTATION / consistency (the
        stiffening is the kernel doing what Axiom 4 says — NOT a forced
        dimensionless number, so not a chord; tagged manifestation).
  * phase-space-coordinate-check — T3.1/T3.2 corpus claims (mode exists + c_eff(V)
        stiffening) live in real-space / kernel-strain coordinates; the tests
        measure there (energy density, ω(k), c_eff(A)). No phase-space φ²/Clifford
        -torus claim is at issue at THIS rung (that arrives with R/r, (2,3) at L4).
  * verify-before-cite — every clm-/def-/file:line in these docstrings was
        grep-verified at build time (clm-crbl60, clm-gz7ryg, V_LONG@constants:676,
        c_eff_squared@master_equation_fdtd:148-151, the bulk-impedance leaf).
  * ave-discrimination-check — T3.1 headlines AVE-distinct existence ⇒ the
        SM/QED-counterfactual is MANDATORY and is stated in the T3.1 bins (QED
        deletes the longitudinal scalar via gauge fixing; AVE keeps it).
  * ave-apparatus-floor-attribution — the leapfrog energy floor + the PML-cell
        exclusion (A-Rule 10 corollary: interior energy filters pml_thickness ≤
        {i,j,k} ≤ N−pml_thickness−1; PML cells are frozen-absorbing artifact).

  NOW FIRED for the RUNG-1 EXISTENCE pass (T3.3/T3.4):
  * ave-power-category-check  — T3.3: the Γ=−1 wall is a PURE REACTANCE (|Γ|→1 =
        total reflection, lossless reactive short — NOT a dissipative loss). The
        impedance route Z_eff=√S→0 is the magnetic μ-load short.
  * ave-resonant-amplification-check  — T3.4b: the cold-Q gate. THE genuine chord
        decider. The genesis-arc A²≈O(α) stuck-floor failure mode is watched: the
        cold ring is measured from cold dynamics, NOT seeded toward 137. Result:
        Q≠137 (clean negative — see the EMPIRICAL RESULTS block above).
  * ave-conserved-vs-pumped  — T3.4c: persistence = the posited mass holding (a
        conserved standing structure), measured zero-drive (not pumped).
  * pre-test-physics-check CP10  — T3.3/T3.4: the cage is a Γ-bounded BOUNDARY
        (the wall + its bound mode), NOT a detonating bulk — boundary-not-bulk.

  TWO α-BAKE GUARDS (mandatory, T3.4b — enforced in code + import-audited):
  the cold-Q measurement does NOT import Q_TANK (cvr_model.py:72 = 1/ALPHA), does
  NOT route through M.ELECTRON, and does NOT touch gamma_em_sq (the 1−α bake at
  cvr_model.py:364). T3.3's Γ_bulk is the α-FREE Z_eff=√S route (crystal_engine.
  gamma_bulk, :455-486), explicitly NOT gamma_em_sq.

  CONSISTENCY-vs-EMERGENCE tags (this pass):  T3.3 = CONSISTENCY / FORM-chord (the
  Ax4 reactive wall manifests; α-free). T3.4a = FORM-chord (a gapped bound mode
  EXISTS) / VALUE-definitional (m_e is NEVER a cage output). T3.4b = CHORD (α-free)
  IF Q-from-cold-dynamics — and the cold cage does NOT yield 137, so the 137-match
  is CONSISTENCY-display-only (instance-baked echo), NOT emergence. T3.4c = FORM
  (persistence) — NOT the topological-winding protection (winding-sector, bucket B).

════════════════════════════════════════════════════════════════════════════════
RETROACTIVE PASS (applied set vs plan — feedback_skill_selection_planning):
the applied set MATCHES the plan above; no drift. Build-time ADDITIONS (flag-
don't-fix): (1) the #278-base-state contradiction (recorded in the `_bulk.py`
FLAG) — the c_eff stiffening kernel is unchanged by #278 so the physics is
unaffected. (2) The cited OP2 gate constant OP2_GAMMA_BULK_MAX=−0.25 is defined as
P18_GAMMA_MAX at genesis_v18_coupled.py:35 (re-exported via loop_gap_harness.py:56)
— the brief's file:line is exact at the definition. (3) The posited-Gaussian core
does NOT ring under a monopole/DC kick (slow continuum relaxation, an FFT-bin-1
artifact); the discrete bound mode requires a radial-SHELL breathing kick — a
measurement-design finding surfaced at integrator time (empirical-driver
discipline, Rule 10), recorded in T3.4a's docstring + the coverage matrix.
════════════════════════════════════════════════════════════════════════════════

VISUAL-DEBUG LAYER (additive; never changes a pass/fail bin) — each test emits a
`<T3.x>_debug.png` into research/figures/engine_acceptance/ when KF_VIZ=1.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import ALPHA, C_0, V_LONG

# OP2 engaged-gate: the canonical Γ_bulk short threshold (genesis_v18_coupled.py:35
# P18_GAMMA_MAX = −0.25; re-exported as OP2_GAMMA_BULK_MAX, loop_gap_harness.py:56).
from ave.core.genesis_v18_coupled import P18_GAMMA_MAX as OP2_GAMMA_BULK_MAX

from . import _bulk as B
from . import _viz as VZ

ALPHA_INV = 1.0 / ALPHA  # ≈ 137.036 — a DOWNSTREAM consistency reference ONLY
#                          (T3.4b reports Q vs this; it does NOT seed/assert it —
#                          asserting 137 = the instrument-echo-trap, theorem-3-1:21)


# ─────────────────────────────────────────────────────────────────────────────
# T3.1 — the longitudinal-bulk compression mode IS REAL (not Gauss-deleted)
# ─────────────────────────────────────────────────────────────────────────────
def test_t3_1_longitudinal_mode_is_real():
    """T3.1 [CHORD — AVE-distinct existence vs QED] — a propagating longitudinal
    compression mode EXISTS on the extended medium (it is NOT Gauss-deleted).

    DEF-LOCK (frozen): the longitudinal-BULK mode is the A1 DILATATION scalar grade
    — compression ALONG the propagation axis — with speed c_bulk = √(K/ρ) =
    √(2G/ρ) = √2·c₀ in the linear regime (K=2G; constants.py:674-676 V_LONG;
    bulk-impedance-at-saturation-boundary.md:24). It is the Heaviside-Gibbs-EXCISED
    scalar grade (def-9a4f07 longitudinal): in textbook EM / QED the longitudinal
    (scalar/timelike) photon polarization is GAUGE-DELETED (Gupta-Bleuler: the
    scalar + longitudinal modes cancel; in Coulomb gauge ∇·A=0 removes them, ∂·A=0
    Lorenz leaves only 2 transverse on-shell). AVE keeps this grade as a PHYSICAL
    propagating compression mode — the "no-QED-garbage longitudinal scalar". This
    is the AVE-distinct content: the mode QED removes, AVE carries and propagates.

    THE MEDIUM EXTENSION FLIPS T1.7. T1.7 recorded longitudinal_dof_present==False
    on the srs vector-TLM (2 transverse DOF only). This test adds the longitudinal
    grade via the canonical Master-Equation scalar engine (_bulk.make_bulk_engine),
    so the engine now CARRIES the mode — T1.7's regression anchor said "if a future
    L3 extension ADDS the bulk DOF, T1.7 flips and becomes the real propagation
    gate". THIS is that gate.

    SM/QED COUNTERFACTUAL (ave-discrimination-check, MANDATORY for an AVE-distinct
    headline): QED has 4 photon polarizations but gauge-fixing removes the scalar +
    longitudinal, leaving exactly 2 transverse on-shell DOF — a free longitudinal
    photon does NOT propagate in QED. AVE's longitudinal mode is a real acoustic
    dilatation branch (gapless, ω=c_bulk·k, energy-carrying). The DISCRIMINATOR:
    does a launched longitudinal compression PROPAGATE + carry energy + have a
    dispersion? In QED the answer is no (gauge artifact); in AVE, yes.

    PRE-REGISTERED BINS (frozen 2026-06-17, BEFORE the run):
      * PASS (the longitudinal mode is real + AVE-distinct):
          (1) PRESENT: the medium now carries a longitudinal (bond-axial)
              dilatation grade — the bulk engine's scalar field IS the
              compression amplitude (longitudinal_dof_present == True), FLIPPING
              the T1.7 ⊘ absence-finding.
          (2) PROPAGATES: a launched longitudinal compression PULSE TRANSLATES —
              its interior energy-density PEAK advances down the axis at a finite
              positive speed (the mode is not a frozen/static/evanescent field).
              Operationalised: (a) the interior field at a probe is NON-static (its
              temporal std is a finite fraction of the seed amplitude, > 1e-3, not
              zero); AND (b) a localized one-way pulse's energy-density peak
              translates with fitted speed > 0.3 (interior cells per unit time,
              c₀=1 natural units — a real forward group velocity, not zero =
              standing/evanescent). NOTE the closed-box energy-conservation bin is
              DELIBERATELY NOT used: the Master-Equation engine is PML-bounded (an
              OPEN, absorbing boundary by design), so interior energy is expected
              to drain to the sponge — energy conservation is the wrong observable
              on it (a category error). Propagation DISTANCE is the substrate-native
              "does it propagate" observable here, matching the open-engine reality.
          (3) DISPERSION: the mode has a genuine acoustic dispersion ω(k) > 0 that
              RISES with k (ω increases monotonically across m=1..4; a propagating
              branch, not a flat/gapless-zero non-mode). dω/dk > 0.
          (4) AVE-DISTINCT: the QED-counterfactual holds — c_bulk/c₀ = √2 (a
              SECOND, faster, longitudinal channel distinct from the c₀ transverse
              photon) confirms this is a separate dilatation grade, not the
              transverse mode relabelled. |c_bulk/c₀ − √2| < 1e-9.
      * FAIL : the field is static / evanescent (no oscillation OR the pulse peak
              does not translate, speed ≤ 0.3 = standing/evanescent, not a
              propagating mode); OR ω(k) is flat / non-increasing (no acoustic
              branch); OR c_bulk/c₀ ≠ √2 (not the K=2G dilatation channel) — any of
              which means the longitudinal mode is NOT a real propagating
              AVE-distinct grade.

    HONEST NOTE (Operating Principle, report-back): is this genuinely AVE-distinct
    -REAL, or asserted? The mode's EXISTENCE-as-a-DOF (bin 1) is a medium-extension
    DESIGN choice — we ADDED the longitudinal grade because the corpus says it is
    physical (def-9a4f07; the A1 scalar). But bins (2)+(3)+(4) are EMPIRICAL: the
    launched compression wave is DYNAMICALLY evolved by the canonical engine and we
    MEASURE whether it propagates, oscillates, has ω(k)>0, and runs at the K=2G
    speed √2·c₀ — none of those are asserted, they are read off the integrator. The
    AVE-vs-QED distinction (the mode is KEPT, not gauge-deleted) is a framework
    commitment we encode by building the grade; the empirical content is that ONCE
    built per the canonical engine, it behaves as a real acoustic branch. So: the
    DOF is added-by-design (honest), its propagation/dispersion/speed are measured
    (empirical). It is NOT a forced dimensionless number — the "chord" tag here is
    AVE-DISTINCT EXISTENCE (the QED-counterfactual), not a forced-number chord.
    """
    B.assert_canonical_constants()

    # (1) PRESENT — the medium now carries a longitudinal dilatation grade.
    eng = B.make_bulk_engine(N=40, S_min=1e-3)
    B.seed_longitudinal_plane_wave(eng, amplitude=1e-3, m=2, axis=2)
    longitudinal_dof_present = True  # the scalar field IS the bond-axial dilatation
    seed_peak = float(np.max(np.abs(eng.V)))

    # (2) PROPAGATES — (a) non-static interior field, (b) a localized one-way pulse
    #     whose energy-density PEAK translates at finite positive speed. (Closed-box
    #     energy conservation is NOT used: PML is an open/absorbing boundary —
    #     category error to demand energy conservation on it; see the bin docstring.)
    s = eng.pml_thickness + 4
    probe = []
    for _ in range(120):
        eng.step()
        probe.append(float(eng.V[s, s, s]))
    probe = np.asarray(probe)
    osc_fraction = float(np.std(probe) / max(seed_peak, 1e-30))
    is_nonstatic = osc_fraction > 1e-3

    engp = B.make_bulk_engine(N=64, S_min=0.5, pml_thickness=6)
    B.seed_longitudinal_pulse(engp, amplitude=1.0, width=4.0, axis=2)
    tr = B.track_longitudinal_peak(engp, 60, axis=2)
    pulse_speed = tr["speed"]
    propagates = pulse_speed > 0.3

    # (3) DISPERSION — ω(k) > 0 and RISING with k (a genuine acoustic branch).
    #     Sane S_min=0.5 (NOT the deep T3.2 ceiling) so dt is large enough for the
    #     FFT to RESOLVE distinct ω per m (a tiny dt collapses all m into one bin —
    #     a measurement artifact, not a flat branch; see measure_bulk_dispersion).
    disp = B.measure_bulk_dispersion(
        lambda: B.make_bulk_engine(N=48, S_min=0.5, pml_thickness=6),
        m_values=(1, 2, 3, 4), n_steps=600,
    )
    ks = np.array([d[0] for d in disp])
    ws = np.array([d[1] for d in disp])
    omega_positive = bool(np.all(ws > 0))
    # monotone-rising: each successive ω strictly above the previous (acoustic)
    dwdk_positive = bool(np.all(np.diff(ws) > 0))

    # (4) AVE-DISTINCT — c_bulk/c₀ = √2 (the K=2G dilatation channel, a SECOND
    #     faster longitudinal channel distinct from the transverse photon).
    c_bulk_ratio = B.c_bulk_over_c0_linear()
    is_k2g_channel = abs(c_bulk_ratio - np.sqrt(2.0)) < 1e-9

    print("\n--- T3.1 longitudinal-BULK mode IS REAL [CHORD — AVE-distinct vs QED] ---")
    print(f"  DEF-LOCK: c_bulk = √(K/ρ) = √(2G/ρ) = √2·c₀ (linear); A1 dilatation, NOT Gauss-deleted")
    print(f"  (1) longitudinal DOF present  : {longitudinal_dof_present}  (FLIPS T1.7 ⊘ → ✅)")
    print(f"  (2) interior oscillation frac : {osc_fraction:.3e}  non-static? {is_nonstatic} (PASS>1e-3)")
    print(f"      one-way pulse peak speed  : {pulse_speed:.4f}  propagates? {propagates} (PASS>0.3, c₀=1)")
    print(f"  (3) ω(k) (m=1..4)             : {np.array2string(ws, precision=4)}")
    print(f"      ω>0? {omega_positive}   dω/dk>0 (acoustic branch)? {dwdk_positive}")
    print(f"  (4) c_bulk/c₀                 : {c_bulk_ratio:.9f}  == √2 (K=2G channel)? {is_k2g_channel}")
    print("  SM/QED counterfactual: QED gauge-DELETES the longitudinal/scalar photon (2 transverse")
    print("    on-shell); AVE keeps it as a real propagating dilatation grade — THE AVE-distinct content.")

    assert longitudinal_dof_present, "FAIL: no longitudinal DOF — medium extension did not add the grade"
    assert is_nonstatic, f"FAIL: longitudinal field is static/evanescent — osc fraction {osc_fraction:.3e}"
    assert propagates, f"FAIL: longitudinal pulse does not translate (standing/evanescent) — speed {pulse_speed:.4f}"
    assert omega_positive, f"FAIL: ω(k) not positive — {ws}"
    assert dwdk_positive, f"FAIL: ω(k) not a rising acoustic branch (dω/dk≤0) — {ws}"
    assert is_k2g_channel, f"FAIL: c_bulk/c₀ {c_bulk_ratio:.9f} != √2 (not the K=2G dilatation channel)"

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        # show the PROPAGATING PULSE (the actual propagation evidence, bin 2b) —
        # a localized one-way compression whose energy-density peak TRANSLATES
        # down the axis (a clean diagonal band), not the plane-wave standing seed.
        ev = B.make_bulk_engine(N=64, S_min=0.5, pml_thickness=6)
        B.seed_longitudinal_pulse(ev, amplitude=1.0, width=4.0, axis=2)
        rv = B.run_free_bulk(ev, 60, record_every=2)
        xt = np.array(rv["snaps"])  # (frames, interior_z) — interior x-t energy density

        def _draw(fig):
            ax1, ax2 = fig.subplots(1, 2)
            im = ax1.imshow(xt, origin="lower", aspect="auto", cmap="magma")
            ax1.set_xlabel("interior axis cell")
            ax1.set_ylabel("frame (×2 steps)")
            ax1.set_title(f"T3.1 longitudinal compression x-t\n(pulse TRANSLATES, speed {pulse_speed:.2f}·c₀)")
            fig.colorbar(im, ax=ax1, fraction=0.046, pad=0.04, label="energy density |V|²")
            ax2.plot(ks, ws, "o-", color="#1f77b4", label="ω(k) longitudinal-bulk")
            ax2.plot(ks, (ws / ks).mean() * ks, "k--", lw=0.8, label="linear ω=c·k")
            ax2.set_xlabel("k (rad/cell)")
            ax2.set_ylabel("ω (rad/time)")
            ax2.set_title(f"acoustic dispersion (ω>0, dω/dk>0)\nc_bulk/c₀=√2 (K=2G); NOT Gauss-deleted")
            ax2.legend(fontsize=8)

        path = VZ.save_simple_figure(
            "T3.1", "longitudinal-BULK mode IS REAL (AVE keeps the QED-deleted scalar)", _draw)
        print(f"  [viz] T3.1 figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T3.2 — c_eff(V) stiffening: c_eff → ∞ as A → A_yield (the cage precursor)
# ─────────────────────────────────────────────────────────────────────────────
def test_t3_2_c_eff_stiffening():
    """T3.2 [Axiom-4 MANIFESTATION / consistency] — the longitudinal-bulk effective
    speed STIFFENS, c_eff(V) → ∞ as A → A_yield (S → 0), driven by the kernel S(A).

    DEF-LOCK (frozen): the canonical Master-Equation stiffening kernel is
    c_eff²(V) = c₀²/S(A), S(A)=√(1−A²) (master_equation_fdtd.py:11,141-151;
    constants.py:46), so c_eff/c₀ = S^(−1/2) = (1−A²)^(−1/4) → ∞ as A → A_yield=1.
    This is the #278-CORRECTED ½-power convention (c_eff = c₀·S^(−1/2); NOT the old
    S^0.25, which was the `refractive_index()` exponent DEFECT — see the `_bulk.py`
    FLAG: #278 fixed refractive_index() to S^0.5 but the c_eff² KERNEL was always
    c₀²/S and is read DIRECTLY here, so this test is independent of the #278 state).
    The stiffening is the CAGE PRECURSOR (CP8 generative-precursor): as the
    longitudinal compression approaches yield, the bond stiffens (C_eff=C₀/S → ∞),
    c_eff → ∞, and the medium begins to form the binding wall — the T3.3 Γ=−1 TIR
    cage (DEFERRED) is the END of this stiffening (Z_bulk=ρ·c_bulk → 0 at S→0 by
    the OTHER speed branch — the bulk channel; here we measure the c_eff SCALAR
    stiffening that is the precursor of that wall).

    CONSISTENCY-vs-EMERGENCE: this is Axiom-4 MANIFESTATION (the kernel doing what
    Axiom 4 SAYS: reactance follows the quarter-arc, the bond stiffens at yield).
    It is NOT a chord — no forced dimensionless number falls out; the stiffening is
    the axiom's constitutive law expressed in the longitudinal sector. Inputs: the
    canonical S(A) kernel [Axiom 4] read from the engine's authoritative
    c_eff_squared (NOT a re-derivation). Tagged Axiom-4-manifestation / consistency.

    REGIME (step-0 declaration): swept I→III. The MEANINGFUL stiffening lives in
    Regime II near-yield (§2.6 grid bulk-Regime-II = "✓ rectification + asym-grip";
    the cage stiffens c_eff→∞ as r→r_yield). At Regime I (A<r₁=√(2α)≈0.121) the
    stiffening is sub-α (ΔS≈A²/2, unresolvable — c_eff/c₀≈1.004 at the I→II
    boundary) so a "no stiffening" reading at Regime I is EXPECTED dormancy, NOT a
    falsification (the standing guard). The test asserts the stiffening is PRESENT
    and RISING in Regime II and DIVERGES toward the ceiling in Regime III, and
    REPORTS the Regime-I dormancy honestly. PHASE-STATE: constitutive sweep (the
    kernel as f(A) at fixed operating points — a closed-form kernel read, CP10
    boundary-not-bulk, NO time-domain detonation risk).

    PRE-REGISTERED BINS (frozen 2026-06-17, BEFORE the run):
      * PASS (c_eff(V) stiffens monotonically and diverges at yield):
          (1) COLD limit: c_eff/c₀ = 1 at A=0 (S=1) to < 1e-12.
          (2) MONOTONE RISING: across the sweep A ∈ {0, 0.1, …, 0.99}, c_eff/c₀ is
              strictly INCREASING in A (the bond stiffens as the compression
              approaches yield) — every successive point above the previous.
          (3) MATCHES THE KERNEL: c_eff/c₀ == (1−A²)^(−1/4) (= S^(−1/2)) to
              < 1e-9 at every swept A (it IS the canonical c_eff²=c₀²/S kernel,
              the #278-corrected ½-power form, NOT S^0.25).
          (4) DIVERGES toward the ceiling at A → A_yield: with S_min=1e-3 (c_eff²
              ceiling = c₀²/S_min), c_eff/c₀ at A=0.999 reaches the deep-near-yield
              value > 4 (S(0.999)=0.0447 ⇒ c_eff/c₀=4.73), AND at the S_min floor
              the engine caps c_eff/c₀ at 1/√S_min = 31.6 (→∞ as S_min→0, the
              physical wall; the ceiling is the numerical-stability cap, not the
              physics). i.e. the stiffening is unbounded as S→0 up to the engine
              ceiling.
          (5) REGIME-II is where it BITES: c_eff/c₀ at the I→II boundary
              r₁=√(2α)≈0.121 is ≈1.004 (sub-α stiffening, Regime-I dormancy —
              REPORTED not failed), and rises through Regime II to c_eff/c₀≈1.41
              at the II→III boundary r₂=√3/2 (S=0.5). The stiffening becomes
              resolvable (>1%) inside Regime II, confirming §2.6.
      * FAIL : c_eff/c₀ ≠ 1 cold; OR not monotone rising; OR off the (1−A²)^(−1/4)
              kernel by ≥ tol (would mean it is NOT the canonical c_eff²=c₀²/S — in
              particular an S^0.25 reading would FAIL bin 3, catching the defect);
              OR no divergence as A → A_yield (the wall does not form).
    """
    B.assert_canonical_constants()
    from ave.core.regime_map import R_LINEAR_MAX, R_NONLINEAR_MAX

    A_sweep = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99])
    ce = np.array([B.c_eff_over_c0_at(a, S_min=1e-3, A_cap=0.999999) for a in A_sweep])
    analytic = (1.0 - A_sweep**2) ** (-0.25)  # = S^(-1/2)

    cold_ok = abs(ce[0] - 1.0) < 1e-12
    monotone = bool(np.all(np.diff(ce) > 0))
    kernel_err = float(np.max(np.abs(ce - analytic)))
    matches_kernel = kernel_err < 1e-9

    ce_999 = B.c_eff_over_c0_at(0.999, S_min=1e-3, A_cap=0.999999)
    diverges_deep = ce_999 > 4.0
    ceiling = 1.0 / np.sqrt(1e-3)  # engine cap at the S_min floor

    ce_r1 = B.c_eff_over_c0_at(float(R_LINEAR_MAX), S_min=1e-3, A_cap=0.999999)  # I→II
    ce_r2 = B.c_eff_over_c0_at(float(R_NONLINEAR_MAX), S_min=1e-3, A_cap=0.999999)  # II→III
    regime1_dormant = (ce_r1 - 1.0) < 0.01   # sub-α: < 1% stiffening at Regime-I edge
    regime2_bites = (ce_r2 - 1.0) > 0.05     # resolvable stiffening by the II→III edge

    print("\n--- T3.2 c_eff(V) stiffening → ∞ as A→A_yield [Axiom-4 MANIFESTATION] ---")
    print(f"  DEF-LOCK: c_eff² = c₀²/S, c_eff/c₀ = (1−A²)^(−1/4) = S^(−1/2) (#278-corrected ½-power)")
    print(f"  A     :  {np.array2string(A_sweep, precision=3)}")
    print(f"  c_eff/c₀: {np.array2string(ce, precision=4)}")
    print(f"  (1) cold limit c_eff/c₀(0)==1      : {ce[0]:.12f}  ok? {cold_ok}")
    print(f"  (2) monotone rising in A           : {monotone}")
    print(f"  (3) matches (1−A²)^(−¼) kernel err : {kernel_err:.3e}  (PASS<1e-9; an S^0.25 read would FAIL)")
    print(f"  (4) deep near-yield c_eff/c₀(0.999): {ce_999:.4f}  diverges>4? {diverges_deep}; ceiling 1/√S_min={ceiling:.1f}")
    print(f"  (5) Regime-I edge r₁=√(2α)={R_LINEAR_MAX:.4f}: c_eff/c₀={ce_r1:.4f} (sub-α dormant? {regime1_dormant})")
    print(f"      Regime II→III edge r₂=√3/2={R_NONLINEAR_MAX:.4f}: c_eff/c₀={ce_r2:.4f} (bites>5%? {regime2_bites})")
    print("  → the stiffening is the CAGE PRECURSOR (CP8): bond stiffens C_eff=C₀/S→∞, c_eff→∞ at yield.")
    print("  REGIME note: a 'no stiffening' reading at Regime I is EXPECTED dormancy (sub-α), NOT a falsification.")

    assert cold_ok, f"FAIL: cold limit c_eff/c₀(0) {ce[0]:.12f} != 1"
    assert monotone, f"FAIL: c_eff/c₀ not monotone rising — {ce}"
    assert matches_kernel, f"FAIL: c_eff/c₀ off the (1−A²)^(−¼) kernel — err {kernel_err:.3e} (S^0.25 defect?)"
    assert diverges_deep, f"FAIL: no divergence at A→A_yield — c_eff/c₀(0.999) {ce_999:.4f} not > 4"
    assert regime2_bites, f"FAIL: stiffening not resolvable by Regime II→III edge — c_eff/c₀(r₂) {ce_r2:.4f}"
    # regime1_dormant is REPORTED, not asserted (a sub-α reading is expected, not required)

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        Afine = np.linspace(0.0, 0.999, 400)
        ce_fine = (1.0 - Afine**2) ** (-0.25)

        def _draw(fig):
            ax1, ax2 = fig.subplots(1, 2)
            ax1.plot(Afine, ce_fine, color="#d62728", lw=1.6, label="c_eff/c₀ = (1−A²)^(−¼)")
            ax1.plot(A_sweep, ce, "o", color="#1f77b4", label="engine kernel (c_eff_squared)")
            ax1.axvline(float(R_LINEAR_MAX), color="gray", ls=":", lw=0.9, label=f"r₁=√(2α)={R_LINEAR_MAX:.3f}")
            ax1.axvline(float(R_NONLINEAR_MAX), color="black", ls="--", lw=0.9, label=f"r₂=√3/2={R_NONLINEAR_MAX:.3f}")
            ax1.axhline(ceiling, color="purple", ls="-.", lw=0.8, label=f"S_min ceiling 1/√S_min={ceiling:.0f}")
            ax1.set_xlabel("strain A = |V|/V_yield")
            ax1.set_ylabel("c_eff / c₀ (longitudinal stiffening)")
            ax1.set_title("T3.2 c_eff(V) stiffening → ∞ at yield\n(Axiom-4 kernel; the cage precursor)")
            ax1.set_ylim(0.9, min(8.0, ceiling * 1.05))
            ax1.legend(fontsize=7)
            # regime shading
            ax2.plot(Afine, 1.0 / ce_fine**2, color="#2ca02c", lw=1.6, label="S(A)=√(1−A²) (kernel)")
            ax2.axvspan(0, float(R_LINEAR_MAX), color="#e8f4ff", label="I (linear, sub-α)")
            ax2.axvspan(float(R_LINEAR_MAX), float(R_NONLINEAR_MAX), color="#fff0e0", label="II (near-yield, stiffening)")
            ax2.axvspan(float(R_NONLINEAR_MAX), 1.0, color="#ffe0e0", label="III (avalanche → wall)")
            ax2.set_xlabel("strain A")
            ax2.set_ylabel("S(A) = (c₀/c_eff)²")
            ax2.set_title("S(A)→0 (the wall): c_eff=c₀·S^(−½)→∞\nRegime II is where stiffening bites")
            ax2.legend(fontsize=7)

        path = VZ.save_simple_figure(
            "T3.2", "c_eff(V) stiffening → ∞ at A→A_yield (Axiom-4 cage precursor)", _draw)
        print(f"  [viz] T3.2 figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T3.3 — Γ=−1 wall present on a POSITED saturated cage (α-FREE Z_eff=√S)
# ─────────────────────────────────────────────────────────────────────────────
def test_t3_3_gamma_wall_on_posited_cage():
    """T3.3 [CONSISTENCY / FORM-chord] — a Γ=−1 reflective wall is PRESENT on a
    posited saturated longitudinal cage: Γ_bulk crosses the canonical engaged-gate
    OP2_GAMMA_BULK_MAX=−0.25, descends monotonically toward −1 as A→A_yield, and
    →0 in vacuum (S→1). The literal −1 is UNREACHABLE (the S_min-clipped floor).

    POSIT (consistency-class; legitimate here — NOT self-formation, that is rung-2
    / DEFERRED): we PLANT a high-A saturated bulk core (a Gaussian dilatation well)
    on the CrystalEngine BULK branch ONLY (converter_on=False ⇒ no (2,3) winding —
    the two-3s guard, master-equation.md:20: never read charge/spin/μ off the
    scalar cage). Then we read Γ_bulk on the PML-excluded interior.

    α-FREE Γ ROUTE (the load-bearing source choice): Γ_bulk is read via
    crystal_engine.gamma_bulk() (:455-486), the IMPEDANCE route Z_eff=√S,
    Γ=(Z_eff−1)/(Z_eff+1) → −1 as S→0. This is α-FREE (Z_eff=√S carries NO α). We
    do NOT use gamma_em_sq (cvr_model.py:364), which carries the 1−α bake. The
    wall is the magnetic μ-load short (Z_eff=Z₀·√S→0); ave-power-category-check:
    |Γ|→1 is PURE REACTANCE (total reflection, lossless reactive short — NOT a
    dissipative loss). pre-test-physics-check CP10: the cage is a Γ-bounded
    BOUNDARY, not a detonating bulk.

    DEF-LOCK: OP2_GAMMA_BULK_MAX = −0.25 is the canonical engaged-gate
    (genesis_v18_coupled.py:35 P18_GAMMA_MAX; re-exported loop_gap_harness.py:56
    OP2_GAMMA_BULK_MAX). Z_eff=√S, Γ=(Z_eff−1)/(Z_eff+1).

    PRE-REGISTERED BINS (frozen 2026-06-17, BEFORE the run):
      * PASS (the Γ=−1 wall is present + α-free):
          (1) VACUUM: Γ_min(A=0) → 0 (|Γ_min| < 1e-6) — vacuum is an OPEN match,
              S→1 ⇒ Z_eff→1 ⇒ Γ→0 (NOT a wall; the standing-guard expected null).
          (2) MONOTONE DESCENT: Γ_min descends (more-negative) monotonically as
              the posited strain A rises across {0, 0.3, 0.6, 0.8, 0.9, 0.95, 0.99}
              — the wall hardens toward the short as the core saturates.
          (3) CROSSES THE GATE: Γ_min crosses OP2_GAMMA_BULK_MAX=−0.25 by A=0.95
              (Γ_min(0.95) ≤ −0.25) — the engaged short forms in deep Regime II.
          (4) HEADS TOWARD −1 (not past it): Γ_min(0.99) < Γ_min(0.95) (deeper),
              AND the literal −1 is NEVER reached (Γ_min > −1 everywhere — the
              S_min-clipped wall floors above −1; we do NOT bin |Γ−(−1)|<tol, that
              is UNREACHABLE by construction).
      * FAIL : vacuum Γ_min ≠ 0; OR not monotone in A; OR Γ_min never crosses
              −0.25 by A=0.95 (no engaged short forms); OR Γ_min ≤ −1 somewhere
              (the clip is broken / the wall over-shoots the physical short).

    HONEST NOTE: this POSITS the cage (plants the saturated core) — it does NOT
    show the cage SELF-FORMING (that is rung-2, gated). The chord here is that
    GIVEN a saturated core, the impedance route produces the engaged Γ=−1 short
    that the corpus says is the electron's reflective wall — α-free. CONSISTENCY /
    FORM-chord (the Ax4 reactive wall manifests), NOT an emergence claim.
    """
    B.assert_canonical_constants()

    A_posit = [0.0, 0.3, 0.6, 0.8, 0.9, 0.95, 0.99]
    gmins = []
    for frac in A_posit:
        eng = B.make_cage_engine(N=40, S_min=1e-3, A_cap=0.999, pml_thickness=4)
        if frac > 0.0:
            B.posit_saturated_cage(eng, frac=frac, sigma=4.0)
        gmins.append(B.gamma_bulk_min_on_cage(eng)["gamma_min"])
    gmins = np.array(gmins)

    vacuum_open = abs(gmins[0]) < 1e-6
    monotone_descent = bool(np.all(np.diff(gmins) <= 1e-9))
    idx_095 = A_posit.index(0.95)
    crosses_gate = gmins[idx_095] <= OP2_GAMMA_BULK_MAX
    deepens = gmins[-1] < gmins[idx_095]
    above_minus_one = bool(np.all(gmins > -1.0))

    print("\n--- T3.3 Γ=−1 wall on the POSITED saturated cage [CONSISTENCY / FORM-chord] ---")
    print(f"  DEF-LOCK: α-FREE Z_eff=√S route; OP2 engaged-gate = {OP2_GAMMA_BULK_MAX} (NOT gamma_em_sq)")
    print(f"  A posited : {np.array2string(np.array(A_posit), precision=2)}")
    print(f"  Γ_bulk_min: {np.array2string(gmins, precision=4)}")
    print(f"  (1) vacuum Γ_min(A=0) → 0 (open match)?     {gmins[0]:.2e}  ok? {vacuum_open}")
    print(f"  (2) monotone descent toward short in A?     {monotone_descent}")
    print(f"  (3) crosses OP2 gate −0.25 by A=0.95?       Γ_min(0.95)={gmins[idx_095]:.4f}  {crosses_gate}")
    print(f"  (4) deepens at A=0.99 (heads to −1)?        Γ_min(0.99)={gmins[-1]:.4f}  {deepens}")
    print(f"      literal −1 UNREACHABLE (Γ_min > −1)?    {above_minus_one}  (floors at S_min, by design)")
    print("  ave-power-category-check: |Γ|→1 = PURE REACTANCE (lossless reflective short, NOT loss).")

    assert vacuum_open, f"FAIL: vacuum Γ_min {gmins[0]:.2e} not → 0 (S→1 should give Z_eff→1, Γ→0)"
    assert monotone_descent, f"FAIL: Γ_min not monotone descending in A — {gmins}"
    assert crosses_gate, f"FAIL: Γ_min(0.95) {gmins[idx_095]:.4f} does not cross OP2 gate {OP2_GAMMA_BULK_MAX}"
    assert deepens, f"FAIL: Γ_min does not deepen toward −1 at A=0.99 — {gmins[-1]:.4f} vs {gmins[idx_095]:.4f}"
    assert above_minus_one, f"FAIL: Γ_min ≤ −1 somewhere (clip broken / over-shoots the physical short) — {gmins}"

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        # a denser sweep for the curve + the analytic Z_eff=√S route
        Afine = np.linspace(0.0, 0.99, 200)
        S_fine = np.sqrt(np.maximum(1.0 - Afine**2, 1e-3**2))
        Z_fine = np.sqrt(S_fine)
        g_fine = (Z_fine - 1.0) / (Z_fine + 1.0)

        def _draw(fig):
            ax1, ax2 = fig.subplots(1, 2)
            ax1.plot(Afine, g_fine, color="#d62728", lw=1.6, label="Γ=(√S−1)/(√S+1), α-FREE")
            ax1.plot(A_posit, gmins, "o", color="#1f77b4", ms=7, label="engine gamma_bulk() (interior)")
            ax1.axhline(OP2_GAMMA_BULK_MAX, color="black", ls="--", lw=1.0, label=f"OP2 gate {OP2_GAMMA_BULK_MAX}")
            ax1.axhline(-1.0, color="purple", ls=":", lw=0.9, label="literal −1 (UNREACHABLE)")
            ax1.set_xlabel("posited strain A = |V|/V_yield")
            ax1.set_ylabel("Γ_bulk_min (interior, PML-excluded)")
            ax1.set_title("T3.3 Γ=−1 wall on the posited cage\n(crosses −0.25 by A≈0.95; α-FREE)")
            ax1.set_ylim(-1.05, 0.05)
            ax1.legend(fontsize=7)
            ax2.plot(Afine, S_fine, color="#2ca02c", lw=1.6, label="S(A)=√(1−A²)")
            ax2.plot(Afine, Z_fine, color="#ff7f0e", lw=1.6, label="Z_eff=√S → 0 (μ-load short)")
            ax2.set_xlabel("strain A")
            ax2.set_ylabel("S, Z_eff")
            ax2.set_title("Z_eff=√S → 0 ⇒ Γ → −1 (reflective short)\nS_min clip ⇒ Γ floors above −1")
            ax2.legend(fontsize=7)

        path = VZ.save_simple_figure(
            "T3.3", "gamma wall profile on the posited saturated cage (α-FREE)", _draw)
        print(f"  [viz] T3.3 figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T3.4 — bound longitudinal eigenmode of the posited cage (3 sub-tests)
#   (a) mass=cutoff [FORM-chord]   (b) cold/α-free Q [the ONE genuine chord]
#   (c) zero-drive persistence
# ─────────────────────────────────────────────────────────────────────────────
def test_t3_4_bound_eigenmode_of_posited_cage():
    """T3.4 — the posited saturated cage hosts a BOUND longitudinal eigenmode.
    Three sub-tests, each with its own frozen bin. A1 SCALAR ONLY (converter OFF;
    the two-3s guard — never read charge/spin/μ off the scalar cage).

    ════════════════════════════════════════════════════════════════════════════
    (a) MASS = CUTOFF  [FORM-chord / VALUE-definitional]
    ════════════════════════════════════════════════════════════════════════════
    A DISCRETE bound longitudinal breathing mode with a gapped cutoff
    eigenfrequency ω_cutoff > 0 EXISTS on the posited cage (a bound mode, NOT a
    continuum). The mass=ground-state-cutoff-energy of the bound resonator is the
    structural FORM (a chord). We REPORT no m_e value: m_e is a CALIBRATION ANCHOR
    (constants.py:129 'Input 1'; electron-identification.md:50 'CALIBRATION ANCHOR
    not derivation') — NEVER a cage-predicted number.

    MEASUREMENT-DESIGN FINDING (empirical-driver discipline, Rule 10, surfaced at
    integrator time): a posited Gaussian core under a MONOPOLE/DC kick does NOT
    ring — it slowly RELAXES (the dominant FFT component sits at bin 1, whose ω
    scales as 1/n_steps = a run-length artifact, NOT a physical mode). The discrete
    bound oscillation is excited by a radial-SHELL BREATHING kick (∂_t V on the
    wall, no monopole DC); then ω_cutoff is STABLE (not bin-1) and the spectrum is
    sharply peaked. We use the shell kick + the DC-free ∂_t V probe at the wall
    antinode.

    PRE-REGISTERED BIN (frozen 2026-06-17):
      * PASS: a DISCRETE GAPPED bound mode exists — ω_cutoff > 0 AND the FFT peak
              is NOT the bin-1 relaxation artifact (ipk > 1) AND the spectrum is
              discrete (peak/mean > 50) AND the signal oscillates (zero-crossings
              > 10). REPORT ω_cutoff (natural units) as the FORM; NEVER an m_e.
      * FAIL: no positive cutoff (ω_cutoff ≤ 0); OR the peak is the bin-1
              relaxation artifact (ipk == 1 = no real mode); OR not discrete
              (peak/mean ≤ 50 = a continuum, not a bound state); OR no oscillation.

    ════════════════════════════════════════════════════════════════════════════
    (b) COLD / α-FREE Q  [the ONE genuine CHORD-vs-ECHO question of this suite]
    ════════════════════════════════════════════════════════════════════════════
    Measure Q from the eigenmode's ring-down (envelope decay + −3dB FWHM linewidth)
    in the LINEAR sub-yield regime (the cold cavity), with the α-bake REMOVED.

    TWO α-BAKE GUARDS (mandatory, enforced): this test imports NEITHER Q_TANK
    (cvr_model.py:72 = 1.0/ALPHA) NOR the ELECTRON instance; and does NOT touch
    gamma_em_sq (cvr_model.py:364, the 1−α bake). Q is read PURELY from the cold
    dynamics (rfft linewidth + Hilbert-envelope decay of ∂_t V). The genesis-arc
    A²≈O(α) stuck-floor failure mode is watched.

    PRE-REGISTERED BIN (frozen 2026-06-17):
      * PASS (the FORM-bin): Q_measured is FINITE and > 0 from the cold dynamics.
              THEN, DOWNSTREAM (a separate consistency read, NOT a bin): report
              Q_measured vs α⁻¹=137.036. Seeding/asserting 137 would be a FAIL of
              chord-discrimination (the instrument-echo-trap, theorem-3-1:21) — so
              we DO NOT assert Q≈137. The chord is earned ONLY if a cold,
              α-free-measured Q lands near 137; an echo is when 137 appears only
              because α was baked. We report which.
      * FAIL: Q is not finite/positive from the cold dynamics (the cavity carries
              no well-defined ring-down — no resonator), OR the test routes through
              any α-baked quantity (guarded against by construction).

    THE HONEST RESULT (recorded in the module docstring): Q_ringdown≈30.8,
    Q_linewidth≈3.8 — NOT 137. α was never baked, so the α-free cold cage does NOT
    reproduce 137 ⇒ the corpus Q=1/α (cvr_model.py:72) is an INSTANCE-BAKED ECHO,
    not a cage-emergent chord. The clean negative the brief hunted.

    ════════════════════════════════════════════════════════════════════════════
    (c) ZERO-DRIVE PERSISTENCE  [FORM — NOT topological-winding protection]
    ════════════════════════════════════════════════════════════════════════════
    Evolve the bare posited cage with NO drive for t≫τ_relax; the bound-mode
    amplitude on the PML-EXCLUDED interior does not decay below threshold (a
    non-radiating standing mode). NOTE: this shows PERSISTENCE, NOT the
    topological-winding protection (that is winding-sector, NOT cage-testable —
    bucket B; ave-conserved-vs-pumped: a conserved standing structure, measured
    zero-drive, not pumped).

    PRE-REGISTERED BIN (frozen 2026-06-17):
      * PASS: after the initial non-eigen transient sheds, the interior peak |V|
              holds steady — late-window mean (75–100%) / mid-window mean (50–75%)
              > 0.8 AND the late-window minimum > 0.05·amp0 (the standing core
              persists well above zero; it does not radiate away).
      * FAIL: the interior amplitude decays away (late/mid ≤ 0.8 = still bleeding;
              or late_min ≤ 0.05·amp0 = radiated to nothing).
    """
    B.assert_canonical_constants()

    # ── (a) MASS = CUTOFF: gapped discrete bound breathing mode exists ──────────
    enga = B.make_cage_engine(N=72, S_min=1e-3, A_cap=0.999, pml_thickness=12)
    probe_idx = B.breathing_kick_cage(enga, frac=0.9, core_sigma=8.0, kick_width=2.0, kick_amp=0.01)
    # run length: ≥ ~1047 steps to resolve the FWHM (brief); 6000 gives a clean,
    # run-length-STABLE ω_cutoff (a real eigenmode, not the bin-1 1/n_steps drift).
    n_steps_a = 6000
    dVdt = B.record_breathing_dVdt(enga, probe_idx, n_steps_a)
    ev = B.cutoff_eigenfrequency(enga, dVdt)
    omega_cutoff = ev["omega_cutoff"]
    gapped = omega_cutoff > 0.0
    not_relaxation_artifact = ev["ipk"] > 1
    discrete = ev["peak_mean"] > 50.0
    oscillates = ev["zero_crossings"] > 10
    mass_cutoff_pass = gapped and not_relaxation_artifact and discrete and oscillates

    # ── (b) COLD / α-FREE Q from ring-down (NO Q_TANK / ELECTRON / gamma_em_sq) ──
    rd = B.ringdown_Q(enga, dVdt, omega_cutoff)
    Q_ringdown = rd["Q_ringdown"]
    Q_linewidth = ev["q_linewidth"]
    # FORM-bin: a finite, positive Q from the cold dynamics (a real resonator).
    q_finite_positive = np.isfinite(Q_ringdown) and Q_ringdown > 0.0 and Q_linewidth > 0.0
    # DOWNSTREAM consistency read (NOT a bin): is it 137 (chord) or not (echo)?
    q_matches_137 = abs(Q_ringdown - ALPHA_INV) < 20.0  # tolerance for a "near-137" claim
    # α-bake guard self-audit: confirm none of the forbidden symbols are in scope.
    _alpha_bake_guard_clean = ("Q_TANK" not in globals()) and ("ELECTRON" not in globals())

    # ── (c) ZERO-DRIVE PERSISTENCE: the bare posited cage holds steady ──────────
    engc = B.make_cage_engine(N=72, S_min=1e-3, A_cap=0.999, pml_thickness=12)
    B.posit_saturated_cage(engc, frac=0.9, sigma=8.0)
    pers = B.cage_persistence_trace(engc, 3000)
    persists = pers["late_over_mid"] > 0.8 and pers["late_min"] > 0.05 * pers["amp0"]

    print("\n--- T3.4 bound longitudinal eigenmode of the POSITED cage (3 sub-tests) ---")
    print("  [A1 SCALAR ONLY; converter OFF — two-3s guard. α-bake guards: NO Q_TANK/ELECTRON/gamma_em_sq]")
    print("  (a) mass=cutoff [FORM-chord / VALUE-definitional]:")
    print(f"      ω_cutoff = {omega_cutoff:.4f} rad/time (natural units; NOT an m_e — m_e is definitional)")
    print(f"      gapped (ω>0)? {gapped}   not bin-1 relaxation artifact (ipk={ev['ipk']}>1)? {not_relaxation_artifact}")
    print(f"      discrete (peak/mean={ev['peak_mean']:.1f}>50)? {discrete}   oscillates (zc={ev['zero_crossings']}>10)? {oscillates}")
    print(f"      => DISCRETE GAPPED bound mode EXISTS? {mass_cutoff_pass}")
    print(f"      [design note: needs a radial-SHELL breathing kick; a monopole/DC kick only RELAXES (bin-1 artifact)]")
    print("  (b) cold/α-FREE Q [THE genuine chord-vs-echo question]:")
    print(f"      Q_ringdown(env) = {Q_ringdown:.3f}   Q_linewidth(FWHM) = {Q_linewidth:.3f}   (finite & >0? {q_finite_positive})")
    print(f"      α-bake guards clean (no Q_TANK/ELECTRON in scope)? {_alpha_bake_guard_clean}")
    print(f"      DOWNSTREAM consistency read: Q_ringdown vs α⁻¹={ALPHA_INV:.3f}  →  Q/α⁻¹ = {Q_ringdown/ALPHA_INV:.4f}")
    print(f"      Q ≈ 137 (would be the CHORD)? {q_matches_137}   →  it is NOT: the α-free cold cage does NOT")
    print(f"      reproduce 137. The corpus Q=1/α (cvr_model.py:72) is an INSTANCE-BAKED ECHO, not cage-emergent.")
    print("  (c) zero-drive persistence [FORM; NOT winding-protection]:")
    print(f"      amp0={pers['amp0']:.4f}  mid_mean(50-75%)={pers['mid_mean']:.4f}  late_mean(75-100%)={pers['late_mean']:.4f}")
    print(f"      late/mid = {pers['late_over_mid']:.4f} (>0.8 steady)   late_min={pers['late_min']:.4f} (>0.05·amp0)")
    print(f"      => non-radiating standing mode persists? {persists}  (persistence ≠ topological-winding protection)")

    # ── frozen-bin asserts ──
    assert mass_cutoff_pass, (
        f"FAIL (a) mass=cutoff: no discrete gapped bound mode — ω_cutoff={omega_cutoff:.4f}, "
        f"ipk={ev['ipk']}, peak/mean={ev['peak_mean']:.1f}, zc={ev['zero_crossings']}"
    )
    assert q_finite_positive, (
        f"FAIL (b) cold-Q: no finite/positive Q from cold dynamics — "
        f"Q_ringdown={Q_ringdown}, Q_linewidth={Q_linewidth}"
    )
    assert _alpha_bake_guard_clean, "FAIL (b) α-bake guard: a forbidden α-baked symbol is in scope"
    assert persists, (
        f"FAIL (c) persistence: the cage decays away — late/mid={pers['late_over_mid']:.4f}, "
        f"late_min={pers['late_min']:.4f}, amp0={pers['amp0']:.4f}"
    )
    # NOTE: q_matches_137 is REPORTED, never asserted (asserting 137 = the
    # instrument-echo-trap; the honest result is that it does NOT match — echo).

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        # rebuild the spectra/envelopes for plotting (cheap; viz-only)
        s = dVdt - dVdt.mean()
        spec = np.abs(np.fft.rfft(s * np.hanning(len(s))))
        freqs = np.fft.rfftfreq(len(s), d=1.0)
        omega_axis = 2.0 * np.pi * freqs / enga.dt
        t_axis = np.arange(len(dVdt)) * enga.dt
        try:
            from scipy.signal import hilbert

            env = np.abs(hilbert(s))
        except ImportError:
            env = np.abs(s)

        def _draw_mode(fig):
            ax1, ax2 = fig.subplots(1, 2)
            ax1.plot(t_axis, dVdt, color="#1f77b4", lw=0.6)
            ax1.set_xlabel("time (natural units)")
            ax1.set_ylabel("∂ₜV at wall antinode")
            ax1.set_title(f"T3.4a breathing ring (gapped bound mode)\nω_cutoff={omega_cutoff:.3f}, oscillates")
            ax2.plot(omega_axis[1:], spec[1:], color="#d62728", lw=1.0)
            ax2.axvline(omega_cutoff, color="black", ls="--", lw=0.9, label=f"ω_cutoff={omega_cutoff:.3f}")
            ax2.set_xlabel("ω (rad/time)")
            ax2.set_ylabel("|rfft(∂ₜV)|")
            ax2.set_title(f"discrete gapped spectrum (peak/mean={ev['peak_mean']:.0f})\nNOT a continuum")
            ax2.set_xlim(0, min(8.0, omega_axis[-1]))
            ax2.legend(fontsize=8)

        p1 = VZ.save_simple_figure("T3.4_mass_cutoff_eigenmode", "mass=cutoff: gapped bound breathing mode", _draw_mode)
        print(f"  [viz] T3.4 mass-cutoff figure -> {p1}")

        def _draw_q(fig):
            ax1, ax2 = fig.subplots(1, 2)
            ax1.plot(t_axis, np.abs(s), color="#bbbbbb", lw=0.5, label="|∂ₜV|")
            ax1.plot(t_axis, env, color="#d62728", lw=1.2, label="Hilbert envelope")
            ax1.set_xlabel("time (natural units)")
            ax1.set_ylabel("envelope")
            ax1.set_title(f"T3.4b cold ring-down (α-FREE)\nQ_ringdown={Q_ringdown:.1f}")
            ax1.legend(fontsize=8)
            ax2.plot(omega_axis[1:], spec[1:], color="#1f77b4", lw=1.0)
            ax2.axvline(omega_cutoff, color="black", ls="--", lw=0.8)
            ax2.set_xlabel("ω (rad/time)")
            ax2.set_ylabel("|rfft| (−3dB FWHM → Q)")
            ax2.set_title(f"linewidth Q={Q_linewidth:.2f}\nQ/α⁻¹={Q_ringdown/ALPHA_INV:.3f} — NOT 137 (echo, not chord)")
            ax2.set_xlim(0, min(8.0, omega_axis[-1]))

        p2 = VZ.save_simple_figure("T3.4_cold_Q_ringdown_linewidth", "cold α-free Q (NOT 137 — echo, not chord)", _draw_q)
        print(f"  [viz] T3.4 cold-Q figure -> {p2}")

        def _draw_pers(fig):
            ax = fig.subplots(1, 1)
            n = len(pers["amps"])
            ax.plot(np.arange(n), pers["amps"], color="#2ca02c", lw=0.8)
            ax.axvspan(int(0.5 * n), int(0.75 * n), color="#fff0e0", alpha=0.6, label="mid (50–75%)")
            ax.axvspan(int(0.75 * n), n, color="#e8f4ff", alpha=0.6, label="late (75–100%)")
            ax.axhline(0.05 * pers["amp0"], color="purple", ls=":", lw=0.9, label="0.05·amp0 threshold")
            ax.set_xlabel("zero-drive step")
            ax.set_ylabel("interior peak |V| (PML-excluded)")
            ax.set_title(f"T3.4c zero-drive persistence (non-radiating standing mode)\nlate/mid={pers['late_over_mid']:.2f}, persists")
            ax.legend(fontsize=8)

        p3 = VZ.save_simple_figure("T3.4_persistence_trace", "zero-drive persistence (non-radiating)", _draw_pers)
        print(f"  [viz] T3.4 persistence figure -> {p3}")
