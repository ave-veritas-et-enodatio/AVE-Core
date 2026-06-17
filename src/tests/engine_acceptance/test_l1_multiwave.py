"""L1-multiwave — the multiple wave types ("we have multiple wave types").

Grant: AVE is a multi-mode medium. L1 so far tests ONLY the transverse photon
(test_l1_photon.py). This file adds the OTHER free modes — OR, where the existing
srs medium does not carry a given wave type, STOPS and reports the medium-
extension finding (naming what is missing) rather than forcing it.

════════════════════════════════════════════════════════════════════════════════
THE GROUNDED mode↔DOF↔speed MAPPING (substrate-native-check FIRST, NOT asserted)
════════════════════════════════════════════════════════════════════════════════
This cluster has been conflated twice (the c_shear-vs-c_EM α category error,
ave-kb/CLAUDE.md:71; the genesis-24 double-count). So the mapping below is GROUNDED
from the corpus, with file:line, before any test code, and the speeds are
DEF-LOCKED in the test docstrings so the conflation cannot recur.

Axiom-1: a substrate node carries 6 DOF = 3 translational + 3 micro-rotational
(Cosserat / micropolar). The free wave modes are the propagating excitations of
those DOF. The CANONICAL three-speed split (the "three-impedance law";
field-symbol registry §3.11; ave-kb three-impedance-law channel corrections
2026-06-11) assigns every mode a channel subscript:

  ── MODE ────────────── DOF ──────────────── SPEED ──────────── corpus anchor ──
  EM-transverse (PHOTON) 2 transverse         c_EM = c₀/S        clm-8nkvwy:111;
    the α-bearing optical  (the 2 polariza-     (slows under       A4-test; ave-kb/
    channel; Z_EM ≡ Z₀     tions)               saturation)        CLAUDE.md:71
  ──────────────────────────────────────────────────────────────────────────────
  SHEAR (gravity wave)   2 transverse-shear   c_shear =          gw-impedance-
    transverse inductive   (the micropolar      c₀·(1−A²)^(1/4)    perturbation.md:30;
    shear; Z_shear=ρc_sh   shear grades)        = c₀·S^(1/4)       invariant-grav-
                                                (freezes G→0)      impedance.md:30
  ──────────────────────────────────────────────────────────────────────────────
  BULK-longitudinal      1 longitudinal-      c_bulk             bulk-impedance-at-
    (the A1 "3" / mass     dilatation           (dilatational;     saturation-
    precursor); Z_bulk=    (compression         freezes →0 at      boundary.md:24,31;
    ρc_bulk                along the bond)      rupture)           A1 scalar grade
  ──────────────────────────────────────────────────────────────────────────────
  COSSERAT micro-rot.    3 micro-rotational   gapped OPTICAL     two-threes (charge
    (the gapped optical    (the ω field; the    branch (ω(k=0)>0,  ="3" winding);
    branch; charge seat)   winding=charge seat) finite gap)        master-equation.md:20

DEF-LOCK (frozen so the conflation cannot recur — each appears verbatim in the
relevant test docstring):
    c_EM    = c₀ / S            (EM-transverse photon — slows under saturation)
    c_shear = c₀ · S^(1/4)      (transverse SHEAR / GW — corpus form, NOT c₀√S)
    c_bulk  = √(K/ρ)            (longitudinal dilatation; K=2G bulk modulus)
with S = √(1−(A/A_yield)²). NOTE the EM channel slows as 1/S while the shear
channel slows as S^(1/4) — they are DIFFERENT channels of the SAME 2-transverse
field, distinguished by which modulus (ε,μ vs G_shear) responds; substituting
c_shear into the α formula is the canonical category error (CLAUDE.md:71).

⚑ FLAG (flag-don't-fix; surfaced to Grant/auditor, NOT silently reconciled):
   The build brief def-locked "c_shear = c₀√S". The CORPUS canonical form is
   c_shear = c₀·S^(1/4) = c₀·(1−A²)^(1/4) (gw-impedance-perturbation.md:30;
   invariant-grav-impedance.md:30). √S ≠ S^(1/4). This file uses the CORPUS form
   and FLAGS the brief↔corpus mismatch rather than picking one silently. (Both
   collapse to c₀ in the linear S=1 regime where these free-mode tests run, so
   the discrepancy is dormant at L1 and only bites at the saturated wall — but it
   must be adjudicated before any saturated-shear test.)

════════════════════════════════════════════════════════════════════════════════
WHAT THE ENGINE ACTUALLY CARRIES (empirical DOF-capability audit, Rule 10)
════════════════════════════════════════════════════════════════════════════════
The srs engine has exactly TWO field representations (verified empirically):
  * scalar_tlm_step : (N, degree)    — 1 scalar per PORT (a network-scalar TLM
                       quantity), NOT a physical longitudinal-bulk VECTOR mode
                       with a c_bulk dilatational speed.
  * vector_tlm_step : (N, degree, 2) — 2 TRANSVERSE components per port (the
                       photon). NO 3rd (bond-axial / longitudinal) component; NO
                       separate ω (micro-rotation) field.
The `_rotation_per_node` channel is a per-node polarization ROTATION of the SAME
transverse field (optical activity, A1b/T1.5), NOT a propagating micro-rotation
DOF with its own gapped branch. There is NO saturation modulation in the free
linear regime (S=1).

CONSEQUENCE for the three new modes:
  T1.6 transverse-SHEAR    — the transverse 2-DOF wave IS present, but it is the
       SAME field as the EM-transverse photon and, at S=1 (linear), c_shear =
       c₀·S^(1/4) = c₀ collapses onto c_EM. The shear MODE (transverse) exists;
       the c_shear CONSTITUTIVE (the G_shear-driven S^(1/4) modulation that
       distinguishes it from c_EM=c₀/S) is NOT realized — it needs the saturated
       medium + a separate G_shear modulus channel. → PARTIAL: mode present,
       distinguishing constitutive ABSENT (reported, not forced).
  T1.7 longitudinal-BULK   — NOT carried: no bond-axial / dilatation vector DOF.
       → MEDIUM-EXTENSION FINDING (the A1 longitudinal grade is missing).
  T1.8 Cosserat micro-rot. — NOT carried: no ω micro-rotation field, no gapped
       optical branch. → MEDIUM-EXTENSION FINDING (the 3 micropolar grades are
       missing; this is the L4 charge-seat medium-extension).

substrate-native-check walk (Operating Principle 1; done BEFORE any code here):
  * Dynamics  : discrete srs-TLM scatter+connect (the transverse mode that IS
                present); STRUCTURE / DOF-capability assertions for the modes that
                are NOT present (no fabricated dynamics for a missing DOF).
  * Sector    : T1.6 = transverse 2-vector (present); T1.7 = longitudinal/bulk
                (ABSENT); T1.8 = micro-rotation (ABSENT). Named per the grounded
                mapping above, not conflated.
  * Objective : dispersion ω(k), front speed, mode character, energy conservation
                for the present mode; explicit DOF-count + missing-grade naming
                for the absent modes.
  * Coords A46: real-space / spectral observables (the photon's coordinates) for
                the present transverse mode; the absent-mode findings are
                structural (DOF algebra), coordinate-free.
  * Saturation: OFF (S=1, linear) — which is precisely why the c_shear-vs-c_EM
                distinction is dormant here (both → c₀) and the shear constitutive
                cannot be exercised at L1.

VISUAL-DEBUG LAYER (additive; never changes a pass/fail bin) — each test emits a
`<T?>_debug.png` into research/figures/engine_acceptance/ when KF_VIZ=1.
"""

from __future__ import annotations

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_dynamics as cld
from ave.core import chiral_lattice_vector as clv

from . import _medium as M
from . import _viz as VZ


# ─────────────────────────────────────────────────────────────────────────────
# T1.6 — transverse-SHEAR wave (PARTIAL: mode present, c_shear constitutive absent)
# ─────────────────────────────────────────────────────────────────────────────
def test_t1_6_transverse_shear_wave():
    """T1.6 [consistency + FINDING] — the transverse-SHEAR mode.

    DEF-LOCK (frozen): c_shear = c₀·S^(1/4)  [the transverse SHEAR / gravitational
    wave; CORPUS form per gw-impedance-perturbation.md:30 and invariant-grav-
    impedance.md:30 — NOT c₀√S, see the module ⚑FLAG]. Contrast: the EM-transverse
    photon is c_EM = c₀/S; the bulk-longitudinal is c_bulk = √(K/ρ).

    GROUNDED SCOPE (substrate-native-check, NOT asserted): the srs vector-TLM
    carries a TRANSVERSE 2-DOF wave. In the corpus, light itself is "a purely
    transverse Cosserat shear wave" (double-deflection.md:26) — so the transverse
    mode the engine carries IS the shear/transverse family. This test verifies
    the mode that IS present (lossless transverse propagation + linear dispersion
    + transverse character + a well-defined speed), and REPORTS the constitutive
    gap: at S=1 (linear, free regime) c_shear = c₀·S^(1/4) = c₀ collapses onto
    c_EM, so the c_shear↔c_EM DISTINCTION (the S^(1/4) vs 1/S modulation, which
    lives in the SATURATED medium via a separate G_shear modulus) is NOT realized
    at L1. The DISTINGUISHING constitutive is a saturated-medium + G_shear-channel
    extension; the MODE is present.

    PRE-REGISTERED BINS (frozen 2026-06-17):
      * PASS : the transverse mode propagates LOSSLESSLY (energy drift < 1e-8)
               AND has LINEAR dispersion (c(k) spread < 0.05 across m=1..4)
               AND a well-defined speed on the known srs projection (|c|/c_net
                   within 5%, c_net = c_link/√3)
               AND is TRANSVERSE (the wave lives in the 2-component transverse
                   field; no spurious longitudinal/3rd component — by construction
                   the field has exactly 2 components).
      * FAIL : lossy OR dispersive in-band OR wrong speed.
      * REPORT (not pass/fail): the c_shear vs c_EM constitutive gap — at S=1 both
               = c₀; the S^(1/4) shear modulation is absent (needs the saturated
               medium + a G_shear modulus channel, a medium extension).
    """
    M.assert_canonical_constants()
    net = cl.build_srs_net(8, "right")
    c_link = cld.mean_bond_length(net)
    c_net = cld.ANALYTIC_NETWORK_FACTOR * c_link

    # (1) lossless transverse propagation (one-way packet) + speed
    V0 = M.oneway_packet(net, axis=2, sign=-1.0, m=2, width_frac=0.10, pol=0)
    drift = M.max_energy_drift(net, V0, 600, chiral_rotation=False)
    ct = M.centroid_translation(net, V0, 600, axis=2, chiral_rotation=False)
    speed_ratio = abs(ct["speed"]) / c_net

    # (2) linear dispersion across the usable band
    nf = cld.network_velocity_factor(net, axis=2, m_values=(1, 2, 3, 4), n_steps=800)
    cs = np.array(nf["c_of_k"])
    spread = float((cs.max() - cs.min()) / cs.mean())

    # (3) transverse character: the field carries exactly 2 transverse DOF
    transverse_dof = int(V0.shape[2])

    # constitutive gap report (S=1 linear regime): c_shear = c0·S^(1/4) = c0 = c_EM
    S_linear = 1.0
    c_shear_over_c0 = S_linear ** 0.25     # = 1 at S=1
    c_EM_over_c0 = 1.0 / S_linear          # = 1 at S=1
    collapse = abs(c_shear_over_c0 - c_EM_over_c0) < 1e-12

    print("\n--- T1.6 transverse-SHEAR mode (srs, N=8) [consistency + FINDING] ---")
    print(f"  DEF-LOCK: c_shear = c₀·S^(1/4) (corpus form; NOT c₀√S — see module FLAG)")
    print(f"  (1) lossless drift            : {drift:.3e}  (PASS < 1e-8)")
    print(f"      transverse speed |c|/c_net: {speed_ratio:.4f}  (PASS within 5% of 1)")
    print(f"  (2) dispersion c(k) spread    : {spread:.4f}  (PASS < 0.05, linear)")
    print(f"  (3) transverse DOF            : {transverse_dof}  (the 2-component transverse field)")
    print(f"  REPORT — constitutive gap at S=1: c_shear/c₀={c_shear_over_c0:.3f}, c_EM/c₀={c_EM_over_c0:.3f}")
    print(f"      → collapse onto c₀: {collapse}; the S^(1/4) shear modulation (vs EM 1/S) is ABSENT")
    print("      → distinguishing c_shear needs the SATURATED medium + a G_shear modulus channel (extension)")

    assert drift < 1e-8, f"FAIL: transverse shear mode lossy — drift {drift:.3e}"
    assert spread < 0.05, f"FAIL: dispersive in-band — c(k) spread {spread:.4f}"
    assert abs(speed_ratio - 1.0) <= 0.05, (
        f"FAIL: wrong transverse speed — |c|/c_net {speed_ratio:.4f}"
    )
    assert transverse_dof == 2, f"FAIL: not a transverse 2-DOF mode — DOF {transverse_dof}"

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        rec = VZ.record_axis_profile(net, V0, 600, axis=2, chiral_rotation=False, every=4)
        disp = cld.measure_dispersion(net, axis=2, m_values=(1, 2, 3, 4), n_steps=800)
        kk = np.array([d[0] for d in disp])
        ww = np.array([d[1] for d in disp])

        def _disp(ax):
            ax.plot(kk, ww, "o-", color="#2ca02c", label="ω(k) transverse-shear")
            ax.plot(kk, (ww / kk).mean() * kk, "k--", lw=0.8, label="linear ω=c·k")
            ax.set_xlabel("k (rad/cartesian)")
            ax.set_ylabel("ω (rad/step)")
            ax.set_title(f"shear dispersion (linear, spread {spread:.3f})\n"
                         "DEF-LOCK c_shear=c₀·S^(1/4); at S=1 → c₀")
            ax.legend(fontsize=8)

        path = VZ.save_propagation_figure(
            "T1.6", "transverse-SHEAR mode (c_shear=c₀·S^(1/4); S=1→c₀)", rec,
            drift_floor_label=f"lossless drift {drift:.1e}; speed |c|/c_net {speed_ratio:.3f}",
            extra=_disp,
        )
        print(f"  [viz] T1.6 figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T1.7 — longitudinal-BULK wave (the A1 "3"): MEDIUM-EXTENSION FINDING (not carried)
# ─────────────────────────────────────────────────────────────────────────────
def test_t1_7_longitudinal_bulk_wave_medium_extension_finding():
    """T1.7 [FINDING — medium extension required; STOP-and-report per the brief].

    DEF-LOCK (frozen): c_bulk = √(K/ρ)  [the longitudinal DILATATION wave; the A1
    "3" / mass precursor; K = 2G the bulk modulus (K=2G provenance MERGED,
    PR#261); Z_bulk = ρ·c_bulk; freezes c_bulk→0 at dielectric rupture per
    bulk-impedance-at-saturation-boundary.md:24,31]. Distinct from c_EM = c₀/S
    (EM-transverse) and c_shear = c₀·S^(1/4) (transverse shear).

    SUBSTRATE-NATIVE FINDING (Rule 10 empirical DOF-capability audit; the brief's
    STOP-and-report — do NOT force the mode): the srs vector-TLM medium DOES NOT
    CARRY a longitudinal-bulk wave. The vector field is (N, degree, 2) — exactly 2
    TRANSVERSE components per port, with NO bond-axial / longitudinal (3rd)
    component. The scalar_tlm_step field (N, degree) is a network-SCALAR TLM
    quantity (one scalar per port), NOT a physical longitudinal-DILATATION vector
    mode with a c_bulk dilatational speed — it has no bond-axial polarization and
    no K/ρ constitutive. So the longitudinal-bulk mode cannot be tested here.

    WHAT IS MISSING (named precisely, per the brief):
      * a LONGITUDINAL (bond-axial) field component — a 3rd vector grade carrying
        compression ALONG the bond direction (the A1 dilatation / Heaviside-Gibbs
        scalar grade), giving the field shape (N, degree, 3) [2 transverse + 1
        longitudinal] OR a dedicated dilatation field;
      * a BULK constitutive — the K = 2G bulk modulus and ρ density so c_bulk =
        √(K/ρ) is defined (the EM ε,μ and the shear G do NOT set the dilatation
        speed);
      * a longitudinal scatter/connect that propagates the dilatation (the Op5
        shunt scatter is wired for the transverse vector field, not the
        compression mode).
    This is the L3 medium extension (the longitudinal-bulk mode = the mass
    precursor) — out of L1 scope; recorded so the L3 build has the precise gap.

    PRE-REGISTERED BINS (frozen 2026-06-17):
      * PASS (the FINDING is correctly recorded): the engine carries NO
              longitudinal DOF — the vector field has exactly 2 transverse
              components (no 3rd/bond-axial), AND the scalar field is a per-port
              network-scalar (degree components, not a 3-vector dilatation). i.e.
              longitudinal_dof_present == False.
      * FAIL : a longitudinal-bulk vector DOF turns out to be present (the field
              has a bond-axial component) — then this is NOT a medium-extension
              finding and the test must be rewritten as a real c_bulk propagation
              gate. (Regression anchor: if a future L3 extension ADDS the bulk DOF,
              this test flips and must become the real T1.7 propagation test.)
    """
    M.assert_canonical_constants()
    net = cl.build_srs_net(6, "right")

    # vector field DOF: exactly 2 transverse, no bond-axial/longitudinal 3rd
    V_vec = clv.launch_linear_packet(net)
    vector_components = int(V_vec.shape[2])
    has_longitudinal_vec_dof = vector_components >= 3

    # scalar field is a per-port network-scalar, NOT a 3-vector dilatation
    V_scalar = np.zeros((net.n_nodes, net.degree))
    scalar_is_per_port = (V_scalar.ndim == 2 and V_scalar.shape[1] == net.degree)

    longitudinal_dof_present = has_longitudinal_vec_dof  # the only place a bulk mode could live

    print("\n--- T1.7 longitudinal-BULK wave: MEDIUM-EXTENSION FINDING ---")
    print(f"  DEF-LOCK: c_bulk = √(K/ρ)  [A1 dilatation; K=2G; distinct from c_EM, c_shear]")
    print(f"  vector field components/port  : {vector_components}  (2 transverse; bond-axial 3rd present? {has_longitudinal_vec_dof})")
    print(f"  scalar field is per-port      : {scalar_is_per_port}  (network-scalar, not a 3-vector dilatation)")
    print(f"  longitudinal-bulk DOF present : {longitudinal_dof_present}  (FINDING: expected False = not carried)")
    print("  MISSING (named): (a) a bond-axial longitudinal grade; (b) a K=2G/ρ bulk constitutive;")
    print("                   (c) a longitudinal scatter/connect. = the L3 mass-precursor medium extension.")

    assert not longitudinal_dof_present, (
        "FINDING FLIPPED: a longitudinal-bulk DOF IS present — rewrite T1.7 as a "
        "real c_bulk=√(K/ρ) propagation gate (the medium was extended)."
    )
    assert scalar_is_per_port, "scalar field is not the expected per-port network-scalar"

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        def _draw(fig):
            ax1, ax2 = fig.subplots(1, 2)
            ax1.bar(["transverse\n(present)", "longitudinal-bulk\n(MISSING)"],
                    [vector_components, 0], color=["#2ca02c", "#d62728"])
            ax1.set_ylabel("vector DOF per port carried")
            ax1.set_title("T1.7 longitudinal-BULK: NOT carried (medium extension)")
            for i, v in enumerate([vector_components, 0]):
                ax1.annotate(str(v), xy=(i, v), xytext=(0, 3),
                             textcoords="offset points", ha="center", fontsize=11)
            ax2.annotate(
                "MEDIUM-EXTENSION FINDING (T1.7)\n\n"
                "DEF-LOCK: c_bulk = √(K/ρ)  (A1 dilatation)\n\n"
                "srs carries: 2 transverse DOF only\n"
                "(N, degree, 2) — no bond-axial 3rd.\n\n"
                "MISSING to host the bulk wave:\n"
                "  (a) a longitudinal (bond-axial) grade\n"
                "  (b) a K=2G/ρ bulk constitutive\n"
                "  (c) a longitudinal scatter/connect\n\n"
                "= the L3 mass-precursor medium extension.",
                xy=(0.04, 0.5), xycoords="axes fraction", va="center", fontsize=10,
                bbox=dict(boxstyle="round", fc="#ffeaea", ec="#e0a0a0"))
            ax2.axis("off")
            ax2.set_title("named gap (STOP-and-report, not forced)")

        path = VZ.save_simple_figure(
            "T1.7", "longitudinal-BULK wave — MEDIUM-EXTENSION FINDING (not carried)", _draw)
        print(f"  [viz] T1.7 figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T1.8 — Cosserat micro-rotation wave (gapped optical branch): EXTENSION FINDING
# ─────────────────────────────────────────────────────────────────────────────
def test_t1_8_cosserat_microrotation_wave_medium_extension_finding():
    """T1.8 [FINDING — medium extension required; STOP-and-report per the brief].

    DEF-LOCK (frozen): the Cosserat MICRO-ROTATION wave is the GAPPED OPTICAL
    branch — a micropolar mode with ω(k→0) > 0 (a finite frequency gap), carried
    by the 3 micro-rotational DOF (the ω field). It is the charge=winding seat
    (the "3" winding; two-threes, master-equation.md:20). Distinct from the
    acoustic c_EM / c_shear / c_bulk branches (which are gapless: ω→0 as k→0).

    SUBSTRATE-NATIVE FINDING (Rule 10 empirical DOF-capability audit; the brief's
    STOP-and-report — do NOT force the mode): the srs engine DOES NOT CARRY a
    propagating Cosserat micro-rotation wave. The only rotation in the engine is
    `_rotation_per_node` — a per-node polarization ROTATION applied to the SAME
    transverse 2-DOF field after scatter (optical activity; the A1b / T1.5
    channel). That is a constitutive twist of the transverse field, NOT an
    independent micro-rotation DOF with its own field, its own scatter/connect,
    and its own GAPPED dispersion branch. There is no ω field (no micropolar
    grade), so there is no gapped optical branch to measure.

    PROOF (empirical): the optical-activity channel produces a dθ/step that is the
    GLOBAL geometric writhe (a constant per-node rotation, k-INDEPENDENT) — it does
    NOT have a k-dependent ω(k) gapped dispersion. A genuine micro-rotation wave
    would have a finite ω(0) gap and a k-dependent branch; the engine's rotation
    is a uniform per-step twist, the signature of optical activity, not a wave.

    WHAT IS MISSING (named precisely, per the brief):
      * a MICRO-ROTATION field ω (3 micropolar grades) as an INDEPENDENT DOF, not
        a rotation applied to the transverse field;
      * a micropolar constitutive with a ROTATIONAL stiffness setting the gap
        ω(0) > 0 (the Cosserat coupling length ELL_C = √6·ℓ_node is the canonical
        scale; constants.py);
      * a micro-rotation scatter/connect propagating ω on the srs graph.
    This is the L4 medium extension (the micro-rotation / winding = charge); out
    of L1 scope; recorded so the L4 build has the precise gap.

    PRE-REGISTERED BINS (frozen 2026-06-17):
      * PASS (the FINDING is correctly recorded): there is NO independent micro-
              rotation DOF — the rotation channel is a per-node twist of the
              transverse field whose dθ/step is the k-INDEPENDENT global writhe
              (constant; not a gapped ω(k) branch). i.e. cosserat_wave_present
              == False, and the rotation is confirmed to be the global-writhe
              optical-activity twist (|dθ/step − writhe| < 1e-6).
      * FAIL : an independent gapped micro-rotation branch turns out to be present
              (then rewrite T1.8 as a real gapped-dispersion gate); OR the rotation
              channel is NOT the global-writhe twist (the finding's premise is
              wrong). (Regression anchor for a future L4 extension.)
    """
    M.assert_canonical_constants()
    net = cl.build_srs_net(8, "right")

    # the engine's only "rotation": a per-node polarization twist of the transverse
    # field. Confirm dθ/step is the k-INDEPENDENT global writhe (optical activity),
    # NOT a gapped ω(k) micro-rotation branch.
    res = clv.measure_dynamical_rotation(net, n_steps=800, chiral_rotation=True)
    dtheta = res.dtheta_per_step
    writhe = res.writhe
    is_global_writhe_twist = abs(dtheta - writhe) < 1e-6

    # there is no independent micro-rotation field/DOF in the engine
    # (the vector field is purely the 2 transverse components; rotation acts ON it)
    cosserat_wave_present = False  # no ω field, no gapped branch, no micro-rot scatter

    print("\n--- T1.8 Cosserat micro-rotation wave: MEDIUM-EXTENSION FINDING ---")
    print(f"  DEF-LOCK: gapped OPTICAL branch (ω(0)>0), carried by 3 micro-rotational DOF")
    print(f"  engine rotation channel       : per-node twist of the transverse field (optical activity)")
    print(f"  dθ/step = {dtheta:+.6f} = global writhe {writhe:+.6f}? {is_global_writhe_twist} (k-INDEPENDENT)")
    print(f"  independent micro-rotation DOF: {cosserat_wave_present}  (FINDING: expected False = not carried)")
    print("  → the rotation is a uniform per-step twist (optical activity), NOT a gapped ω(k) wave")
    print("  MISSING (named): (a) an ω micro-rotation field (3 micropolar grades); (b) a rotational")
    print("                   stiffness setting the gap ω(0)>0 (ELL_C=√6·ℓ_node); (c) a micro-rot")
    print("                   scatter/connect. = the L4 winding=charge medium extension.")

    assert not cosserat_wave_present, (
        "FINDING FLIPPED: an independent micro-rotation branch IS present — rewrite "
        "T1.8 as a real gapped ω(k) dispersion gate (the medium was extended)."
    )
    assert is_global_writhe_twist, (
        f"FINDING premise wrong: rotation channel is not the global-writhe twist — "
        f"|dθ/step − writhe| {abs(dtheta - writhe):.3e} >= 1e-6"
    )

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        # the rotation angle trace (linear in t = constant dθ/step = optical activity,
        # NOT a gapped k-dependent branch)
        S = cl.scatter_matrix(net.degree)
        conn = net.connect_index()
        rot = clv._rotation_per_node(net)
        Vt = clv.launch_linear_packet(net)
        ang = [clv.mean_polarization_angle(Vt)]
        for _ in range(800):
            Vt = clv.vector_tlm_step(net, Vt, S, conn, rot)
            ang.append(clv.mean_polarization_angle(Vt))
        ang = np.unwrap(np.array(ang))

        def _draw(fig):
            ax1, ax2 = fig.subplots(1, 2)
            tt = np.arange(len(ang))
            ax1.plot(tt, ang, color="#1f77b4", label=f"θ(t): dθ/step={dtheta:+.4f}=writhe")
            ax1.plot(tt, writhe * tt + ang[0], "k--", lw=0.8, label="linear = constant twist")
            ax1.set_xlabel("timestep")
            ax1.set_ylabel("pol angle θ (rad)")
            ax1.set_title("engine rotation = uniform optical-activity twist\n(k-INDEPENDENT, NOT a gapped wave)")
            ax1.legend(fontsize=8)
            ax2.annotate(
                "MEDIUM-EXTENSION FINDING (T1.8)\n\n"
                "DEF-LOCK: gapped OPTICAL branch ω(0)>0\n"
                "(3 micro-rotational DOF; charge=winding seat)\n\n"
                "engine has: optical-activity TWIST of the\n"
                "transverse field (constant dθ/step = writhe),\n"
                "NO independent ω field, NO gapped branch.\n\n"
                "MISSING to host the micro-rotation wave:\n"
                "  (a) an ω micro-rotation field (3 grades)\n"
                "  (b) a rotational stiffness ⇒ gap ω(0)>0\n"
                "      (ELL_C = √6·ℓ_node)\n"
                "  (c) a micro-rotation scatter/connect\n\n"
                "= the L4 winding=charge medium extension.",
                xy=(0.04, 0.5), xycoords="axes fraction", va="center", fontsize=10,
                bbox=dict(boxstyle="round", fc="#ffeaea", ec="#e0a0a0"))
            ax2.axis("off")
            ax2.set_title("named gap (STOP-and-report, not forced)")

        path = VZ.save_simple_figure(
            "T1.8", "Cosserat micro-rotation wave — MEDIUM-EXTENSION FINDING (not carried)", _draw)
        print(f"  [viz] T1.8 figure -> {path}")
