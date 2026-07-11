"""EP-CMRR acceptance test (U5) — the equivalence-principle common-mode-rejection
differential-pair on the certified Master-Equation medium.

FROZEN prereg: research/2026-07-11_ep-cmrr-acceptance-test_prereg_FROZEN.md
(frozen by push BEFORE this driver existed; the tethered_pivot_x34b.py pattern).

SECTOR = A1 dilatation / gravity (the longitudinal-bulk V scalar,
`ave.core.master_equation_fdtd`). DOF carried = YES (bulk V scalar). REGIME =
sub-yield (S(A)≈1). DRIVE = uniform (common-mode) vs tidal/gradient
(differential). Kernel variable = the DIFFERENTIAL strain ∇V, NOT |V| and NOT
the drive magnitude |g| — that distinction is the whole content of this test.

CLASS = consistency / certification. NO chord mint. Per P10 (below) this test
CERTIFIES-AND-EXPOSES an installed keying's EP-status; it does NOT adjudicate T4.

INVARIANT-S9/S10: this is a certification/consistency test — a `sup-`-class
simulation, NEVER an `exp-`. It certifies the differential-pair INSTRUMENT and
mints no chord, so (like T0.2/T0.3 in `test_l0_medium.py`) it has no clm-/def-
beneficiary and is tracked by test-id, not a hosted `sup-` node.

P10 (binding, verbatim from the frozen prereg): the engine returns whatever
keying is installed (X36 install-tautology,
`research/2026-07-09_x36-node-bottleneck_result.md:54,89,215`). The test's value
is making the installed keying's EP-status VISIBLE — a strain-keyed medium is
WEP-exact (LEG-A passes), a |g|-keyed medium is WEP-violating (LEG-A fires). The
banked galactic η_eff(g_N) MOND keying installed as local-|g| keying FAILS LEG-A
BY DESIGN of MOND phenomenology (a0 is a local-acceleration scale) — that failure
is the honest EXPOSURE of a WEP-violating keying, NOT a bug. The P11 sabotage arm
is that |g|-keyed / MOND-class exposure in miniature.

flag-don't-fix: the engine's raw saturation_kernel keys on the absolute |V|,
which under a sustained uniform drive is itself common-mode-SENSITIVE. The
EP-correct variable is the differential ∇V. Whether the bulk-sector kernel should
key on |V| or ∇V is a KB/Grant physics question this test EXPOSES, not resolves.
"""

from __future__ import annotations

import time

import numpy as np

from ave.core.master_equation_fdtd import MasterEquationFDTD

from . import _ep as EP
from . import _viz as VZ

# ── frozen parameters (from the prereg; NOT tuned to output) ──────────────────
_N = 40
_N_STEPS = 100
_F0 = 0.02  # uniform common-mode amplitude; keeps V_center < 0.5·V_yield
_TARGET_STRAIN_B = 0.2  # LEG-B tidal-strain target (γ set analytically to hit it)
_SABOTAGE_A = 0.3  # planted |g|-keyed strain under the uniform drive

# ── R6-teeth probe parameters (post-freeze amendment; see result-doc amendment) ──
_PROBE_STEPS = 150  # probe propagation length for the evolved-observable detector
_PROBE_SIGMA = 2.0
_PROBE_AMP = 0.05  # small — the probe itself does not load any kernel


def _fresh_medium() -> MasterEquationFDTD:
    return MasterEquationFDTD(N=_N)


def _seed_probe(eng: MasterEquationFDTD) -> MasterEquationFDTD:
    """Seed an identical Gaussian probe at the box centre (R6 teeth)."""
    eng.inject_gaussian((_N // 2, _N // 2, _N // 2), _PROBE_SIGMA, _PROBE_AMP)
    return eng


# ─────────────────────────────────────────────────────────────────────────────
# LEG-A — common-mode (uniform body force): rigid acceleration, ZERO strain
# ─────────────────────────────────────────────────────────────────────────────
def test_ep_cmrr_leg_a_common_mode_zero_strain():
    """LEG-A [CERTIFICATION] — a uniform body force loads a strain-keyed kernel
    ZERO (infinite CMRR by construction).

    A spatially-uniform body force on the translation-invariant medium produces
    rigid translation (V = ½·f0·t², uniform in space) → zero differential strain
    → a strain-keyed kernel stays at S = 1 everywhere.

    PRE-REGISTERED BINS (frozen):
      * PASS : deep-interior A_strain_A < 1e-3 AND min S_strain_A > 0.999.
      * FAIL : A_strain_A >= 1e-3 (a uniform drive spuriously loads the kernel).
    """
    eng = _fresh_medium()
    f = EP.uniform_body_force(eng, _F0)
    EP.evolve_body_force(eng, f, _N_STEPS)
    a_strain = EP.differential_strain_field(eng)
    s_strain = EP.strain_keyed_S(eng, a_strain)

    a_max = float(a_strain.max())
    s_min = float(s_strain.min())
    print("\n--- LEG-A common-mode (uniform drive; certified strain-keyed) ---")
    print(f"  V_center                 : {eng.V[_N // 2, _N // 2, _N // 2]:.4f} (V_yield=1)")
    print(f"  deep-interior A_strain max: {a_max:.3e}  (PASS < 1e-3)")
    print(f"  min S_strain             : {s_min:.6f}  (PASS > 0.999)")

    assert a_max < 1e-3, f"FAIL: uniform drive loaded a strain-keyed kernel — A_strain={a_max:.3e}"
    assert s_min > 0.999, f"FAIL: strain-keyed S dipped under common-mode — S={s_min:.6f}"


# ─────────────────────────────────────────────────────────────────────────────
# LEG-B — differential (gradient/tidal body force): kernel loads on the tide
# ─────────────────────────────────────────────────────────────────────────────
def test_ep_cmrr_leg_b_differential_loads():
    """LEG-B [CERTIFICATION] — a gradient (tidal) body force loads the strain-keyed
    kernel per the tide (NOT trivially null).

    γ is set ANALYTICALLY (γ = 0.4·V_yield/t²) to target A_strain ≈ 0.2 — a
    computed INPUT, not a tuned output.

    PRE-REGISTERED BINS (frozen):
      * PASS : measured A_strain_B within 5% of the analytic target 0.2 AND
               min S_strain_B < 0.999 (the kernel measurably loads on the tide).
      * FAIL : A_strain_B off target by >= 5% OR min S_strain_B >= 0.999.
    """
    eng = _fresh_medium()
    t = _N_STEPS * eng.dt
    gamma = (2.0 * _TARGET_STRAIN_B * eng.V_yield) / (t**2)
    f = EP.gradient_body_force(eng, gamma, axis=0)
    EP.evolve_body_force(eng, f, _N_STEPS)
    a_strain = EP.differential_strain_field(eng)
    s_strain = EP.strain_keyed_S(eng, a_strain)

    a_med = float(np.median(a_strain))
    s_min = float(s_strain.min())
    rel = abs(a_med - _TARGET_STRAIN_B) / _TARGET_STRAIN_B
    print("\n--- LEG-B differential (tidal drive; certified strain-keyed) ---")
    print(f"  γ (analytic)             : {gamma:.4e}")
    print(f"  measured A_strain (med)  : {a_med:.4f}  vs target {_TARGET_STRAIN_B}  (rel {rel:.3f}, PASS < 0.05)")
    print(f"  min S_strain             : {s_min:.4f}  (PASS < 0.999 — kernel loads)")

    assert rel < 0.05, f"FAIL: tidal strain off analytic target — measured {a_med:.4f} vs 0.2 (rel {rel:.3f})"
    assert s_min < 0.999, f"FAIL: kernel did not load on a real tide — S={s_min:.4f}"


# ─────────────────────────────────────────────────────────────────────────────
# P11 — sabotage: key the kernel on |g| (force magnitude) → LEG-A must FIRE
# ─────────────────────────────────────────────────────────────────────────────
def test_ep_cmrr_p11_sabotage_gmag_keying_fires_leg_a():
    """P11 [SABOTAGE / TEETH] — a deliberately |g|-keyed kernel FIRES LEG-A on an
    EVOLVED observable.

    Plant a common-mode-sensitive coupling: key the kernel on the drive magnitude
    |f| instead of the strain (f_yield = |f0|/0.3 → A_sab ≈ 0.3 under the uniform
    drive). |f| ≡ |f0| everywhere under the common-mode drive, so the sabotaged
    kernel LOADS. The banked MOND local-|g| keying is this same |g|-keyed exposure.

    R6 TEETH (post-freeze amendment; result-doc amendment §R6): plant the
    magnitude-keyed coupling INTO the evolution — under the common-mode drive the
    |g|-keyed kernel modulates the stiffness to c_eff²=c0²/S(A_sab) EVERYWHERE,
    whereas a strain-keyed kernel a common-mode drive leaves untouched stays at
    c_eff²=c0². A probe pulse propagates faster through the |g|-loaded medium; the
    detector fires on the EVOLVED field divergence, with a clean-vs-clean run as
    the (exactly-zero) negative control. The earlier arithmetic-only assert had no
    teeth (the evolve was dead code for it); this fixes that.

    PRE-REGISTERED (frozen) BIN — kept, not loosened:
      * min S_sab < 0.99 (the |g|-keyed kernel loads under common-mode; the
        formula-level keying check).
    R6 TEETH BINS (post-freeze):
      * FIRES  : evolved L2 field divergence (|g|-loaded vs strain-keyed) > 1e-2.
      * NEG-CTRL: clean-vs-clean divergence < 1e-9 (determinism — the detector does
        NOT fire when nothing is planted).
    """
    # (i) frozen formula-level keying check — kept
    eng = _fresh_medium()
    f = EP.uniform_body_force(eng, _F0)
    EP.evolve_body_force(eng, f, _N_STEPS)
    f_yield = abs(_F0) / _SABOTAGE_A
    s_min = float(EP.magnitude_keyed_S(eng, f, f_yield).min())

    # (ii) R6 evolved teeth — the |g|-keying planted into the stepping
    s_kernel = float(np.sqrt(1.0 - _SABOTAGE_A**2))  # S(A_sab) at the planted A_sab
    ceff_sq_sab = 1.0 / s_kernel  # c0²=1 → loaded stiffness (|g|-keyed under common-mode)
    ceff_sq_clean = 1.0  # strain-keyed under common-mode: unloaded
    e_clean = _seed_probe(_fresh_medium())
    e_sab = _seed_probe(_fresh_medium())
    e_ctrl = _seed_probe(_fresh_medium())
    EP.evolve_probe(e_clean, ceff_sq_clean, _PROBE_STEPS)
    EP.evolve_probe(e_sab, ceff_sq_sab, _PROBE_STEPS)
    EP.evolve_probe(e_ctrl, ceff_sq_clean, _PROBE_STEPS)
    fire = EP.field_l2_divergence(e_sab, e_clean)
    null = EP.field_l2_divergence(e_ctrl, e_clean)

    print("\n--- P11 sabotage (|g|-keyed kernel; LEG-A must FIRE — evolved teeth) ---")
    print(f"  planted A_sab                : {_SABOTAGE_A:.3f}")
    print(f"  (frozen) min S_sab           : {s_min:.4f}  (loads if < 0.99)")
    print(f"  loaded c_eff² (|g|-keyed)    : {ceff_sq_sab:.4f}  vs clean {ceff_sq_clean:.4f}")
    print(f"  EVOLVED L2 divergence (fire) : {fire:.4f}  (FIRES if > 1e-2)")
    print(f"  negative control (clean|clean): {null:.2e}  (< 1e-9)")

    assert s_min < 0.99, f"FAIL: |g|-keyed kernel did not load under common-mode — S_sab={s_min:.4f}"
    assert fire > 1e-2, (
        f"FAIL: |g|-keyed evolution did NOT diverge from the strain-keyed run — "
        f"L2={fire:.3e} (the detector has no evolved teeth)"
    )
    assert null < 1e-9, f"FAIL: negative control fired — clean-vs-clean L2={null:.2e} (non-deterministic)"


# ─────────────────────────────────────────────────────────────────────────────
# R5 CONTROL — damping-inclusive stepper; verdicts must be unchanged
# ─────────────────────────────────────────────────────────────────────────────
def test_ep_cmrr_r5_damping_inclusive_control():
    """R5 CONTROL [post-freeze amendment; result-doc amendment §R5] — the frozen
    body-force driver OMITTED the certified step()'s PML damping line (the smooth
    drives launch no wave to absorb — the omission was disclosed only post-freeze).
    This control re-runs LEG-A / LEG-B through the SAME stepper WITH the certified
    `V *= self.damping` line REINSTATED and confirms the certification VERDICTS are
    unchanged.

    Note: with damping ON, the LEG-A A_strain metric picks up a small PML-seeded
    boundary residual (the PML shrinks V near the edge → a spurious gradient that
    diffuses toward the read window) — which is EXACTLY why the frozen driver
    omitted damping. The verdict-level invariant `min S` is robust to it.

    ASSERT (verdict-level, must match the no-damping legs):
      * LEG-A (damped): min S_strain > 0.999 (strain-keyed kernel does NOT load
        under common-mode — WEP-exact verdict unchanged).
      * LEG-B (damped): min S_strain < 0.999 (loads on the tide — verdict unchanged).
    """
    eng_a = _fresh_medium()
    EP.evolve_body_force(eng_a, EP.uniform_body_force(eng_a, _F0), _N_STEPS, apply_damping=True)
    a_a = EP.differential_strain_field(eng_a)
    s_a_min = float(EP.strain_keyed_S(eng_a, a_a).min())

    eng_b = _fresh_medium()
    t = _N_STEPS * eng_b.dt
    gamma = (2.0 * _TARGET_STRAIN_B * eng_b.V_yield) / (t**2)
    EP.evolve_body_force(eng_b, EP.gradient_body_force(eng_b, gamma, axis=0), _N_STEPS, apply_damping=True)
    a_b = EP.differential_strain_field(eng_b)
    s_b_min = float(EP.strain_keyed_S(eng_b, a_b).min())

    print("\n--- R5 damping-inclusive CONTROL (certified PML line reinstated) ---")
    print(f"  LEG-A (damped): A_strain residual {float(a_a.max()):.2e}  min S {s_a_min:.6f}  (verdict > 0.999)")
    print(f"  LEG-B (damped): A_strain(med) {float(np.median(a_b)):.4f}  min S {s_b_min:.4f}  (verdict < 0.999)")

    assert s_a_min > 0.999, f"FAIL: damping CHANGED the LEG-A verdict — min S {s_a_min:.6f} (kernel loaded)"
    assert s_b_min < 0.999, f"FAIL: damping CHANGED the LEG-B verdict — min S {s_b_min:.4f} (kernel did not load)"


# ─────────────────────────────────────────────────────────────────────────────
# Certification summary (differential pair) — all three legs together
# ─────────────────────────────────────────────────────────────────────────────
def test_ep_cmrr_certification_summary_cmrr_infinite():
    """SUMMARY [CERTIFICATION] — the differential pair separates a strain-keyed
    (WEP-exact) medium from a |g|-keyed (WEP-violating) one; CMRR → ∞ for the
    strain-keyed medium.

    PRE-REGISTERED BIN (frozen):
      * PASS : CMRR = A_strain_B / max(A_strain_A, 1e-12) > 1e3 AND the |g|-keyed
               arm fires (min S_sab < 0.99) AND the strain-keyed LEG-A does not
               (min S_strain_A > 0.999).
      * FAIL : any of the three.
    """
    t0 = time.time()

    eng_a = _fresh_medium()
    fa = EP.uniform_body_force(eng_a, _F0)
    EP.evolve_body_force(eng_a, fa, _N_STEPS)
    a_a = EP.differential_strain_field(eng_a)
    s_a = EP.strain_keyed_S(eng_a, a_a)

    eng_b = _fresh_medium()
    t = _N_STEPS * eng_b.dt
    gamma = (2.0 * _TARGET_STRAIN_B * eng_b.V_yield) / (t**2)
    fb = EP.gradient_body_force(eng_b, gamma, axis=0)
    EP.evolve_body_force(eng_b, fb, _N_STEPS)
    a_b = EP.differential_strain_field(eng_b)

    f_yield = abs(_F0) / _SABOTAGE_A
    s_sab = EP.magnitude_keyed_S(eng_a, fa, f_yield)

    a_a_max = float(a_a.max())
    a_b_med = float(np.median(a_b))
    # Frozen-bin CMRR carries a 1e-12 divide-floor GUARD; the LEG-A residual is
    # EXACTLY 0, so any displayed ratio is floor-limited, NOT a measurement (R7).
    cmrr_floor_limited = a_b_med / max(a_a_max, 1e-12)
    s_a_min = float(s_a.min())
    s_sab_min = float(s_sab.min())
    runtime = time.time() - t0

    print("\n--- EP-CMRR certification summary ---")
    print(f"  strain-keyed LEG-A min S : {s_a_min:.6f}  (WEP-exact: > 0.999)")
    print(f"  |g|-keyed   LEG-A min S  : {s_sab_min:.4f}  (WEP-violating: fires < 0.99)")
    print(f"  LEG-A residual A_strain  : {a_a_max:.1e}  (exactly 0)")
    print(f"  CMRR                     : ∞ by construction (residual exactly 0; "
          f"the {cmrr_floor_limited:.0e} a 1e-12-floor artifact, NOT a measurement)")
    print(f"  4-leg driver runtime     : {runtime:.2f}s")

    assert a_a_max < 1e-12, f"FAIL: LEG-A residual not ~0 — {a_a_max:.3e} (CMRR not ∞)"
    assert a_b_med > 1e-3, f"FAIL: LEG-B differential too small — {a_b_med:.3e}"
    assert cmrr_floor_limited > 1e3, "FAIL: frozen CMRR bin (floor-limited) not satisfied"
    assert s_a_min > 0.999, f"FAIL: strain-keyed LEG-A loaded — S={s_a_min:.6f}"
    assert s_sab_min < 0.99, f"FAIL: |g|-keyed arm did not fire — S={s_sab_min:.4f}"

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        labels = ["strain-keyed\nLEG-A (uniform)", "|g|-keyed\nLEG-A (uniform)", "strain-keyed\nLEG-B (tide)"]
        vals = [s_a_min, s_sab_min, float(EP.strain_keyed_S(eng_b, a_b).min())]

        def _draw(fig):
            ax = fig.subplots(1, 1)
            bars = ax.bar(labels, vals, color=["#2ca02c", "#d55e00", "#1f77b4"])
            ax.axhline(1.0, color="k", ls="--", lw=0.8, label="S=1 (no loading)")
            ax.axhline(0.99, color="#888888", ls=":", lw=0.8, label="LEG-A fire threshold")
            ax.set_ylabel("min S(A) over deep interior")
            ax.set_ylim(0.9, 1.005)
            ax.set_title("EP-CMRR: strain-keyed rejects common-mode; |g|-keyed fires")
            ax.legend(fontsize=8)
            for b, v in zip(bars, vals):
                ax.annotate(f"{v:.4f}", xy=(b.get_x() + b.get_width() / 2, v),
                            xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)

        path = VZ.save_simple_figure("EP-CMRR", "equivalence-principle common-mode rejection", _draw)
        print(f"  [viz] EP-CMRR figure -> {path}")
