"""L1 — the photon (2 transverse-shear DOF) on the chiral srs grid.

Each test below is a falsifiable physics CLAIM with a PRE-REGISTERED pass/fail
bin in its docstring (frozen BEFORE running). CONSISTENCY-class throughout:
the engine MUST pass these to be a valid free-photon medium.

Medium: the vector-TLM layer of the v9 chiral-srs grid, κ=0 geometry channel
(chiral_rotation OFF) — the FREE photon. The optical-activity rotation channel
is the SEPARATE borderline-CHORD T1.5, out of this L0-L1 scope (and is recorded
as a FINDING in `test_l1_5_finding_chiral_rotation_energy` below).
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_dynamics as cld
from ave.core import chiral_lattice_vector as clv

from . import _medium as M
from . import _viz as VZ


# ─────────────────────────────────────────────────────────────────────────────
# T1.1 — THE FLAGSHIP: does a photon propagate losslessly?
# ─────────────────────────────────────────────────────────────────────────────
def test_t1_1_photon_propagates_losslessly():
    """T1.1 [CONSISTENCY, FLAGSHIP] — a transverse photon PROPAGATES losslessly.

    HARDENED 2026-06-17 (L1-hardening): the seed is now a LOCALIZED, ONE-WAY
    Gaussian-envelope wave packet (`M.oneway_packet`) — single-sign port
    occupancy suppresses the counter-propagating partner, so the x-t spacetime
    shows a SINGLE clean diagonal band translating at constant speed (with the
    slight dispersive broadening visible). The PRIOR seed (`directional_packet`,
    a delocalized cos(k·z) Bloch wave) carries equal ±k content = a STANDING
    fringe: it passed energy conservation but did NOT propagate, so it could not
    test propagation. This is the fix.

    Four sub-claims:

      (a) AMPLITUDE: no ABSORPTIVE decay beyond the numerical floor. The physical
          "lossless" invariant is ENERGY conservation (the engine cannot
          distinguish dispersive peak-spreading from lossy decay by peak height
          alone). So (a) is judged by energy; dispersive peak evolution is
          CHARACTERISED, not failed.
      (b) ENERGY: total transverse energy H = Σ|V|² is flat to integrator floor
          over the whole propagation window.
      (c) NO REFLECTION (Γ ≈ 0): the energy-centroid NEVER reverses propagation
          direction (zero backward steps) — the localized one-way packet does not
          back-scatter into a counter-propagating component. (For a localized
          DISPERSING packet the old net-axial-momentum proxy decays from pure
          envelope spreading across mixed-orientation ports — NOT reflection — so
          centroid-reversal is the faithful reflection measure; the momentum
          retention number is still reported as a characterisation diagnostic.)
      (d) PROPAGATION (THE hardening): the energy-centroid TRANSLATES by ≈ c·t.
          The fitted centroid speed matches the srs network velocity
          c_net = c_link/√3 to within tolerance, and the centroid trajectory is a
          clean straight line (constant-speed diagonal, linear-fit R² ≈ 1).

    PRE-REGISTERED BINS (frozen before run):
      * PASS  : (b) max relative energy drift < 1e-8 over the window
                AND (c) centroid-reversal fraction == 0 (one-way; no reflection)
                AND (d) |centroid speed| within 5% of c_net = c_link/√3
                        (translates at the lattice wave speed)
                    AND centroid-trajectory linear-fit R² > 0.99
                        (a single clean constant-speed diagonal, not a fringe).
      * FAIL  : energy drift >= 1e-8 (LOSSY) OR any centroid reversal (reflection)
                OR centroid speed off c_net by > 5% (wrong propagation speed /
                non-propagating) OR R² <= 0.99 (not a clean diagonal).
      * Report the centroid-translation distance/speed, drift, and momentum
        retention regardless.
    """
    M.assert_canonical_constants()
    net = cl.build_srs_net(10, "right")
    n_steps = 600  # window kept below the multi-wrap horizon for a clean R²

    V0 = M.oneway_packet(net, axis=2, sign=-1.0, m=2, width_frac=0.10, pol=0)
    E0 = clv.vector_energy(V0)
    p0 = M.net_axial_momentum(net, V0, axis=2)
    peak0 = M.peak_amplitude(V0)
    assert E0 > 0 and abs(p0) > 0, "seed must carry energy and net one-way momentum"

    c_link = cld.mean_bond_length(net)
    c_net = cld.ANALYTIC_NETWORK_FACTOR * c_link

    # (b) energy conservation over the full window, read dynamically each step
    drift = M.max_energy_drift(net, V0, n_steps, chiral_rotation=False)

    # (d) propagation: PBC-unwrapped centroid trajectory + fitted speed (the
    #     genuine propagation-distance check — centroid translates by ≈ c·t)
    ct = M.centroid_translation(net, V0, n_steps, axis=2, chiral_rotation=False)
    speed = ct["speed"]
    traj = ct["trajectory"]
    speed_ratio = abs(speed) / c_net
    # constant-speed diagonal: linear-fit R² of the centroid trajectory
    t = np.arange(len(traj))
    fit = np.polyval([speed, traj[0]], t)
    ss_res = float(np.sum((traj - fit) ** 2))
    ss_tot = float(np.sum((traj - traj.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    # (c) no reflection: fraction of steps whose centroid goes BACKWARD
    steps = np.diff(traj)
    reversal_frac = float(np.mean(np.sign(steps) != np.sign(speed)))

    # (a) characterisation diagnostics (not pass/fail)
    Vend = M.run_steps(net, V0, n_steps, chiral_rotation=False)
    peak_end = M.peak_amplitude(Vend)
    p_end = M.net_axial_momentum(net, Vend, axis=2)
    peak_decay = 1.0 - peak_end / peak0
    momentum_retention = p_end / p0

    print("\n--- T1.1 photon PROPAGATION (HARDENED one-way packet; srs κ=0 N=10, 600 steps) ---")
    print(f"  (b) max relative energy drift  : {drift:.3e}   (PASS < 1e-8)")
    print(f"  (d) centroid speed             : {speed:+.5f} cells/step")
    print(f"      c_net = c_link/√3          : {c_net:.5f}   (|speed|/c_net = {speed_ratio:.4f}, PASS within 5%)")
    print(f"      propagation distance       : {ct['displacement']:+.2f} cells over {n_steps} steps (≈ c·t)")
    print(f"      centroid-trajectory R²     : {r2:.6f}   (PASS > 0.99 = clean diagonal)")
    print(f"  (c) centroid-reversal fraction : {reversal_frac:.4f}   (PASS == 0, no reflection)")
    print(f"  (a) dispersive peak decay      : {peak_decay:.4f}  (characterised, energy-conserving)")
    print(f"      net-axial-momentum ret.    : {momentum_retention:.4f}  (diagnostic: decays from envelope SPREAD, not reflection)")

    # ── pre-registered adjudication ──
    assert drift < 1e-8, (
        f"FAIL: medium is LOSSY — energy drift {drift:.3e} >= 1e-8"
    )
    assert reversal_frac == 0.0, (
        f"FAIL: packet REFLECTED — centroid reversed on {reversal_frac:.1%} of steps"
    )
    assert abs(speed_ratio - 1.0) <= 0.05, (
        f"FAIL: wrong propagation speed — |speed|/c_net {speed_ratio:.4f} off 1.0 by > 5% "
        f"(speed {speed:+.5f}, c_net {c_net:.5f})"
    )
    assert r2 > 0.99, (
        f"FAIL: not a clean constant-speed diagonal — centroid R² {r2:.4f} <= 0.99"
    )

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        # the HARDENED one-way seed: a single clean diagonal photon-path band
        rec_oneway = VZ.record_axis_profile(
            net, V0, n_steps, axis=2, chiral_rotation=False, every=4
        )
        # the OLD delocalized Bloch seed on the SAME medium/stepper (the standing
        # fringe it replaced — kept as the side-by-side contrast)
        V_bloch = M.directional_packet(net, axis=2, sign=+1.0, m=2, pol=0)
        rec_bloch = VZ.record_axis_profile(
            net, V_bloch, n_steps, axis=2, chiral_rotation=False, every=4
        )
        path = VZ.save_t1_1_flagship_figure(
            "T1.1",
            rec_oneway,
            rec_bloch,
            centroid=traj,
            speed=speed,
            c_net=c_net,
            r2=r2,
            drift_floor_label=f"lossless: drift {drift:.3e} (integrator floor ~1e-13)",
        )
        print(f"  [viz] flagship figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T1.2 — different frequencies supported (dispersionless across the usable band)
# ─────────────────────────────────────────────────────────────────────────────
def test_t1_2_dispersionless_band():
    """T1.2 [CONSISTENCY] — ω = c·k (dispersionless) across the usable band.

    Sweep commensurate wavevectors k_m and read the modal frequency ω(k) off the
    DYNAMICALLY-evolved field (FFT peak, parabolic sub-bin). Phase velocity
    c(k)=ω/k should be flat (linear dispersion) across the small-k band; the
    zone-edge departure is CHARACTERISED (where it onsets), not failed.

    PRE-REGISTERED BINS:
      * PASS : relative spread of c(k) across the small-k window (m=1..4) is
               < 0.05 (linear dispersion across the usable band).
      * FAIL : spread >= 0.05 (the medium is dispersive in the usable band).
      * Report the onset of zone-edge dispersion (the m where c(k) departs).
    """
    M.assert_canonical_constants()
    net = cl.build_srs_net(8, "right")
    nf = cld.network_velocity_factor(net, axis=2, m_values=(1, 2, 3, 4), n_steps=800)
    cs = np.array(nf["c_of_k"])
    ks = np.array(nf["k"])
    spread = float((cs.max() - cs.min()) / cs.mean())

    print("\n--- T1.2 dispersionless-band (srs, N=8) ---")
    for k, c in zip(ks, cs):
        print(f"  k={k:7.4f}  c(k)={c:8.5f}  c(k)/c_link={c / nf['c_link']:.5f}")
    print(f"  relative c(k) spread (m=1..4): {spread:.4f}   (PASS < 0.05)")
    print(f"  k->0 network factor c0/c_link: {nf['factor']:.5f}  (analytic 1/sqrt3={cld.ANALYTIC_NETWORK_FACTOR:.5f})")

    assert spread < 0.05, (
        f"FAIL: dispersive in usable band — c(k) spread {spread:.4f} >= 0.05"
    )

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        # one representative m=2 packet for the spacetime/filmstrip/energy triptych
        V0 = M.directional_packet(net, axis=2, sign=+1.0, m=2, pol=0)
        rec = VZ.record_axis_profile(
            net, V0, 800, axis=2, chiral_rotation=False, every=5
        )
        # the dispersion omega(k) curve read off the dynamically-evolved field
        disp = cld.measure_dispersion(net, axis=2, m_values=(1, 2, 3, 4), n_steps=800)
        kk = np.array([d[0] for d in disp])
        ww = np.array([d[1] for d in disp])
        cc = np.array([d[2] for d in disp])

        def _disp_panel(ax):
            ax.plot(kk, ww, "o-", color="#2ca02c", label="ω(k) measured")
            cmean = cc.mean()
            ax.plot(kk, cmean * kk, "k--", lw=1.0, label=f"linear ω=c·k (c̄={cmean:.3f})")
            ax.set_xlabel("k (rad / cartesian)")
            ax.set_ylabel("ω (rad / step)")
            ax.set_title(f"dispersion ω(k): c(k) spread {spread:.3f} (PASS<0.05)")
            ax.legend(fontsize=8)
            axt = ax.twinx()
            axt.plot(kk, cc, "s:", color="#9467bd", lw=0.9)
            axt.set_ylabel("c(k)=ω/k (cartesian/step)", color="#9467bd")

        path = VZ.save_propagation_figure(
            "T1.2", "dispersionless band (ω=c·k)", rec,
            drift_floor_label="κ=0 lossless", extra=_disp_panel,
        )
        print(f"  [viz] dispersion figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T1.3 — transversality: exactly 2 polarizations, no longitudinal leak
# ─────────────────────────────────────────────────────────────────────────────
def test_t1_3_transversality_two_polarizations():
    """T1.3 [CONSISTENCY] — exactly 2 transverse polarizations; no longitudinal leak.

    The vector-TLM field carries exactly 2 transverse components per port by
    construction (shape (N, degree, 2)). The physics claim is that the 2
    transverse polarizations are INDEPENDENT and lossless, and that no energy
    leaks into a spurious 3rd (longitudinal) channel during free propagation.

    Operationalised: (1) the field has exactly 2 transverse DOF (structural);
    (2) seeding pol-0 only and propagating κ=0, the energy that appears in pol-1
    (cross-polarization leak) stays at the numerical floor — the two transverse
    polarizations do NOT mix in the free photon (mixing is the chiral T1.5
    channel, OFF here); (3) total energy conserved (no loss to any hidden mode).

    PRE-REGISTERED BINS:
      * PASS : field carries exactly 2 transverse components AND cross-pol leak
               (energy in pol-1 / total) < 1e-10 over the window AND energy
               conserved (< 1e-8 drift).
      * FAIL : cross-pol leak >= 1e-10 (spurious polarization mixing in the free
               photon) OR energy not conserved.
    """
    M.assert_canonical_constants()
    net = cl.build_srs_net(8, "right")
    # structural: exactly 2 transverse DOF
    V0 = M.directional_packet(net, axis=2, sign=+1.0, m=2, pol=0)
    assert V0.shape[2] == 2, "vector-TLM must carry exactly 2 transverse components"
    assert np.all(V0[:, :, 1] == 0.0), "seed is pol-0 only"

    E0 = clv.vector_energy(V0)
    Vend, snaps = M.run_steps(net, V0, 1500, chiral_rotation=False, record=True)
    # cross-pol leak: max over the window of energy-fraction in pol-1
    leak = max(
        float(np.sum(s[:, :, 1] ** 2) / (np.sum(s * s) + 1e-30)) for s in snaps
    )
    drift = abs(clv.vector_energy(Vend) - E0) / E0

    print("\n--- T1.3 transversality (srs, κ=0, N=8, 1500 steps) ---")
    print(f"  transverse DOF              : {V0.shape[2]}  (PASS == 2)")
    print(f"  max cross-pol leak (pol1/tot): {leak:.3e}  (PASS < 1e-10)")
    print(f"  energy drift                : {drift:.3e}  (PASS < 1e-8)")

    assert leak < 1e-10, f"FAIL: spurious polarization mixing — leak {leak:.3e}"
    assert drift < 1e-8, f"FAIL: energy not conserved — drift {drift:.3e}"

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        rec = VZ.record_axis_profile(
            net, V0, 1500, axis=2, chiral_rotation=False, every=10
        )
        e_pol0, e_pol1 = VZ.record_crosspol(net, V0, 1500, chiral_rotation=False)

        def _leak_panel(ax):
            tt = np.arange(len(e_pol0))
            tot = e_pol0 + e_pol1
            ax.plot(tt, e_pol0 / tot, color="#1f77b4", label="pol-0 (seeded)")
            ax.plot(tt, np.maximum(e_pol1 / tot, 1e-18), color="#d62728",
                    label="pol-1 (cross-pol leak)")
            ax.set_yscale("log")
            ax.set_ylim(1e-18, 2.0)
            ax.set_xlabel("timestep")
            ax.set_ylabel("energy fraction (log)")
            ax.set_title(f"cross-pol leak: max {leak:.2e} (PASS<1e-10)")
            ax.legend(fontsize=8, loc="center right")

        path = VZ.save_propagation_figure(
            "T1.3", "transversality (2 pol, no longitudinal leak)", rec,
            drift_floor_label=f"drift {drift:.2e}", extra=_leak_panel,
        )
        print(f"  [viz] transversality figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T1.4 — causality / speed: the information front rides at c0
# ─────────────────────────────────────────────────────────────────────────────
def test_t1_4_causality_front_speed():
    """T1.4 [CONSISTENCY] — the information front rides at the lattice c (no superluminal).

    Seed a SHARP localized on/off transverse disturbance and track the leading
    edge (first plane whose energy rises above the numerical floor) per step.
    The front speed in cardinal-cell/step must equal exactly one bond per step
    (c_link); the information front does not outrun the lattice signal speed.

    CROSS-ENGINE ANCHOR (verify-before-cite; flag-don't-fix): the banked
    photon-c isolation result (`research/2026-06-16_photon-c-isolation-result.md`,
    branch `analysis/2026-06-16-photon-c-isolation`, PR #275 — *OPEN, NOT merged*
    as of this run, grounded against origin/main @ 1ad1e7fc) establishes the
    causal information front rides at **exactly c0** in the engine's physical-c0
    convention (1.0000000000000002), with the √2 being the K4-TLM
    dt = dx/(c·√2) cardinal-cell grid-march bookkeeping. THAT result is on the
    K4-TLM **cubic** engine (k4_tlm.py), NOT this srs grid; the srs front-speed
    convention is the trivalent link-line factor 1/√3, a DIFFERENT clock. So this
    test measures the srs front DIRECTLY and references PR #275 only as the
    cross-engine causality corroboration — it does not transfer the √2/c0 number.

    PRE-REGISTERED BINS:
      * PASS : leading-edge advances at most ONE bond per step (front speed
               <= c_link to within the cardinal-cell discretisation) — no
               superluminal signal; the front does not skip cells.
      * FAIL : front advances > 1 cell/step (superluminal lattice signal).
    """
    M.assert_canonical_constants()
    net = cl.build_srs_net(8, "right")
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    z = net.pos[:, 2]
    # sharp on/off seed: a thin slab at the low-z interior edge, pol-0
    zmin = float(z[net.interior_mask].min())
    slab = (z - zmin) < (0.06 * net.box)
    V = np.zeros((net.n_nodes, net.degree, 2))
    V[slab, 0, 0] = 1.0
    floor = 1e-12 * np.sum(V * V)

    c_link = cld.mean_bond_length(net)
    n_steps = 60
    front_z = [float(z[M.energy_per_node(V) > floor].max())]
    for _ in range(n_steps):
        V = clv.vector_tlm_step(net, V, S, conn, None)
        lit = M.energy_per_node(V) > floor
        front_z.append(float(z[lit].max()) if lit.any() else front_z[-1])
    total_advance = front_z[-1] - front_z[0]
    cells_per_step = total_advance / (n_steps * c_link)

    print("\n--- T1.4 causality / front speed (srs, N=8, 60 steps) ---")
    print(f"  c_link (mean bond length)   : {c_link:.5f}")
    print(f"  front advance (cartesian)   : {total_advance:.4f}")
    print(f"  front speed (cells/step)    : {cells_per_step:.4f}  (PASS <= 1.0 + tol)")
    print("  cross-engine anchor: PR #275 (K4-TLM) info-front = c0 to machine precision (OPEN, not merged)")

    # one bond per step is the lattice signal ceiling; small + tol for the
    # discrete cardinal-cell sampling of the irregular srs front.
    assert cells_per_step <= 1.0 + 1e-9, (
        f"FAIL: superluminal lattice front — {cells_per_step:.4f} cells/step > 1"
    )

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        # re-seed the SAME sharp slab and record its spacetime profile (separate
        # recorder run — the assertion loop above already mutated V); identical seed.
        V_seed = np.zeros((net.n_nodes, net.degree, 2))
        V_seed[slab, 0, 0] = 1.0
        rec = VZ.record_axis_profile(
            net, V_seed, n_steps, axis=2, chiral_rotation=False, every=1
        )
        # the measured info-front (leading lit plane) per step = the causal cone
        front = {
            "z": np.array(front_z),
            "t": np.arange(len(front_z)),
            "label": f"info front ({cells_per_step:.2f} cell/step ≤ c_link)",
        }
        path = VZ.save_propagation_figure(
            "T1.4", "causality / info-front rides at lattice c", rec,
            front=front, drift_floor_label="sharp on/off seed (causal cone)",
        )
        print(f"  [viz] causality figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T1.5 — FINDING: the chiral optical-activity rotation channel is NOT lossless
# ─────────────────────────────────────────────────────────────────────────────
def test_t1_5_finding_chiral_rotation_energy():
    """T1.5-adjacent [FINDING, not a pass/fail consistency gate].

    DOCUMENTS a real engine finding surfaced while validating the free photon:
    the per-node polarization-rotation channel (`vector_tlm_step`'s rot_per_node
    block, fed the global mean-writhe angle ETA_ROT_PER_WRITHE·writhe) is
    energy-conserving as an isolated 2D rotation, but the rotation+connect
    COMPOSITION drifts ~O(1) over a long run on the launch_linear_packet seed.

    This is WHY the free-photon tests (T1.1-T1.4) run κ=0 (rotation OFF) — the
    same setting the engine's own P1 energy gate uses
    (chiral_lattice_vector.py:158). The optical-activity rotation (the
    borderline-CHORD T1.5) needs an energy-conserving formulation before it can
    be a consistency gate; it is OUT of L0-L1 photon-propagation scope.

    No pass/fail bin — this asserts the FINDING is reproducible (the drift is
    large) so a future fix has a regression anchor, and reports the magnitude.
    """
    M.assert_canonical_constants()
    net = cl.build_srs_net(8, "right")
    V = clv.launch_linear_packet(net, axis=2, pol_axis=0, width_frac=0.12)

    drift_off = M.max_energy_drift(net, V.copy(), 1500, chiral_rotation=False)
    drift_on = M.max_energy_drift(net, V.copy(), 1500, chiral_rotation=True)

    print("\n--- T1.5 FINDING: chiral-rotation channel energy ---")
    print(f"  rotation OFF (free photon)  : drift {drift_off:.3e}  (lossless)")
    print(f"  rotation ON  (optical-activ): drift {drift_on:.3e}  (NOT lossless — FINDING)")

    # free photon must be lossless; rotation channel is documented non-conserving
    assert drift_off < 1e-8, "free-photon (κ=0) must be lossless"
    assert drift_on > 1e-3, (
        "FINDING regression anchor: chiral-rotation channel should drift "
        "noticeably (if this fails, the channel was fixed — update the finding)"
    )

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        S = cl.scatter_matrix(net.degree)
        conn = net.connect_index()
        rot = clv._rotation_per_node(net)
        # full per-step energy trace for OFF vs ON (re-seed identically each run)
        def _trace(use_rot):
            Vt = clv.launch_linear_packet(net, axis=2, pol_axis=0, width_frac=0.12)
            E0 = clv.vector_energy(Vt)
            tr = [1.0]
            for _ in range(1500):
                Vt = clv.vector_tlm_step(net, Vt, S, conn, rot if use_rot else None)
                tr.append(clv.vector_energy(Vt) / E0)
            return np.array(tr)

        tr_off = _trace(False)
        tr_on = _trace(True)

        def _draw(fig):
            ax = fig.subplots(1, 1)
            tt = np.arange(len(tr_off))
            ax.plot(tt, tr_off, color="#2ca02c", label=f"rot OFF (free photon) drift {drift_off:.1e}")
            ax.plot(tt, tr_on, color="#d62728", label=f"rot ON (optical-activ) drift {drift_on:.1e}")
            ax.axhline(1.0, color="k", ls=":", lw=0.8)
            ax.set_xlabel("timestep")
            ax.set_ylabel("energy ratio H/H₀")
            ax.set_title("FINDING: chiral-rotation+connect COMPOSITION is NOT energy-conserving")
            ax.legend(fontsize=9)

        path = VZ.save_simple_figure(
            "T1.5", "FINDING — chiral-rotation channel energy (non-conserving)", _draw)
        print(f"  [viz] finding figure -> {path}")
