"""TETHERED-PIVOT MODE-LOCKING — does a WALL-ANCHORED (2,3) traversal MODE-LOCK
where #417's FREE orbit TRACKED the carrier knob?

FROZEN PRE-REG: research/2026-07-09_tethered-pivot-mode-locking_prereg.md.

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (the #417 harness + ONE new ingredient: the ANCHOR)
═══════════════════════════════════════════════════════════════════════════════
#417 (phase_space_winding.py) ran the FREE conservative inter-grade A1↔ω orbit and
returned BREAK: the phase-space traversal reads the CARRIER ratio and the winding
ratio TRACKS the detuning knob continuously (ratio-follows-knob). The W5 circuit
walk proposed that a WALL-ANCHORED traversal — the poloidal loop terminated on the
torus axis — makes the (2,3) integers BC-quantized MODE INDICES (discrete, knobless),
so #417's kill "structurally cannot fire." This module tests that DIRECTLY, in the
SAME phase-space read, by adding one boundary condition: a Γ=−1 wall that pins ONE
quadrature of the winding host b_ω on the equatorial (z≈0) axis-anchored node-plane.

  ANCHOR (gut-check a — the axis): the equatorial node-plane M = tube cells with
  |z| ≤ z_anchor, field-supported, PML-excluded interior. Node-at-center.

  QUADRATURE SELECTOR (gut-check b — #260 μ-sign selector):
    capacitive/short → pin Re(b_ω)[M]=0 (V/d-node, I-antinode);
    magnetic/open    → pin Im(b_ω)[M]=0 (I/q-node).
  Degenerate energy; the choice is the μ-sign selector. Signature 3 (termination
  flip) is the first direct ENGINE PROBE of the #260 adjudication.

  BC in the phase dynamics, NOT a drive: the projection can only REMOVE norm, never
  add it ⇒ the #417 anti-pumping guard holds BY CONSTRUCTION (a lock under an
  energy-REMOVING wall cannot be a pumped illusion). The clamp is a lossy-Dirichlet
  Γ=−1 wall (not strictly conservative); the removed-norm budget is tracked and
  reported (honest energy bookkeeping — NO strict-unitarity claim for clamped runs).

═══════════════════════════════════════════════════════════════════════════════
THE READ (reuse #417 verbatim — phase-space, α-free)
═══════════════════════════════════════════════════════════════════════════════
  toroidal φ(t)=arg(Σ a_A1) ("2"); poloidal ψ(t)=arg(Σ b_ω) ("3");
  traversal rotation number ρ = (net φ-turns)/(net ψ-turns). Two-method read
  (unwrap + circulation) with the F4 caveat honored: the two are the same
  wrapped-increment estimator (near-zero added assurance); the LOAD-BEARING
  discriminator is the DETUNING RESPONSE of ρ (does it track or lock).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# REUSE (anti-rebuild, Rule 14): the #417 harness — seed, reads, energy gate.
from ave.solvers.phase_space_winding import (
    PhaseSpaceWindingConfig,
    _net_turns_circulation,
    _net_turns_unwrap,
    _sector_phase,
    build_seeded_sim,
)

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time). The observable is a pure arg() ratio.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"


@dataclass
class TetheredPivotConfig:
    """Frozen tethered-pivot config. Wraps the #417 phase-space config + the ONE
    new ingredient (the anchor). `branch` selects the μ-sign quadrature (§3)."""

    N: int = 20
    pml_thickness: int = 3
    R: float = 7.0
    r: float = 2.3
    a1_amplitude: float = 0.60
    a1_radius: float = 5.5
    rate: float = 0.3
    omega_b: float = 1.0
    omega_s: float = 1.0
    chi: int = +1
    dt: float = 0.066
    n_steps: int = 500   # headline resolution (#417 used 600); the slope-rate read
                         #   is window-noise-immune, so this only sharpens the plateaus
    # the anchor (frozen §3)
    z_anchor: float = 1.0          # equatorial half-width (lattice cells)
    supp_eps: float = 1e-6         # field-support threshold for M
    branch: str = "capacitive"     # "capacitive"→pin Re ; "magnetic"→pin Im ; "off"
    # frozen sweep grid (§5/§6)
    sweep_os: tuple[float, ...] = (0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00,
                                   1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40)
    rational_points: tuple[tuple[int, int], ...] = ((1, 1), (2, 3), (3, 2), (1, 2))

    def to_ps_cfg(self, *, omega_b: float | None = None, omega_s: float | None = None,
                  winding_on: bool = True) -> PhaseSpaceWindingConfig:
        return PhaseSpaceWindingConfig(
            N=self.N, pml_thickness=self.pml_thickness, R=self.R, r=self.r,
            a1_amplitude=self.a1_amplitude, a1_radius=self.a1_radius, rate=self.rate,
            omega_b=self.omega_b if omega_b is None else omega_b,
            omega_s=self.omega_s if omega_s is None else omega_s,
            chi=self.chi, dt=self.dt, n_steps=self.n_steps, winding_on=winding_on,
        )


# ═════════════════════════════════════════════════════════════════════════════
# THE ANCHOR (the one new ingredient)
# ═════════════════════════════════════════════════════════════════════════════
def anchor_mask(sim, *, z_anchor: float = 1.0, supp_eps: float = 1e-6) -> np.ndarray:
    """The equatorial node-plane M (frozen §3): winding-host tube cells with
    |z| ≤ z_anchor (z = k − center), field-supported, PML-excluded interior. This is
    the axis-anchored / node-at-center family (gut-check a) — the z≈0 plane through
    the torus axis, terminating the poloidal loop."""
    N = sim.N
    c = (N - 1) / 2.0
    _, _, k = np.indices((N, N, N))
    z = k - c
    supp = np.abs(sim.b_w) > supp_eps
    return (np.abs(z) <= z_anchor) & supp & sim.interior


def apply_clamp(sim, mask: np.ndarray, branch: str) -> float:
    """Project one quadrature of b_ω to zero on the anchor set (the Γ=−1 wall).
    capacitive → Re(b_ω)[M]=0 (V-node); magnetic → Im(b_ω)[M]=0 (I-node). Returns
    the norm REMOVED this step (≥0 — the projection is dissipative, never generative)."""
    if branch == "off":
        return 0.0
    before = float(np.sum(np.abs(sim.b_w[mask]) ** 2))
    if branch == "capacitive":
        sim.b_w[mask] = 1j * np.imag(sim.b_w[mask])   # kill V/d-quadrature
    elif branch == "magnetic":
        sim.b_w[mask] = np.real(sim.b_w[mask]) + 0.0j  # kill I/q-quadrature
    else:
        raise ValueError(f"unknown branch '{branch}'")
    after = float(np.sum(np.abs(sim.b_w[mask]) ** 2))
    return before - after


@dataclass
class ClampedTrace:
    t: np.ndarray
    phi_tor: np.ndarray
    psi_pol: np.ndarray
    e_total: np.ndarray
    removed_cum: np.ndarray            # cumulative norm removed by the clamp
    var_re_anchor: np.ndarray          # var(Re b_ω) over M each step
    var_im_anchor: np.ndarray          # var(Im b_ω) over M each step


def trace_orbit_clamped(cfg: TetheredPivotConfig, *, omega_b: float, omega_s: float,
                        branch: str, n_steps: int | None = None) -> ClampedTrace:
    """Seed the electron → conservatively step() → APPLY the clamp each step → trace
    the two Clifford global phases + the energy ledger + the anchor-quadrature
    variances (for the dead-actuator gate). The read is #417's verbatim; the only
    change is the per-step clamp projection."""
    n = cfg.n_steps if n_steps is None else n_steps
    ps = cfg.to_ps_cfg(omega_b=omega_b, omega_s=omega_s)
    sim = build_seeded_sim(ps)
    mask = anchor_mask(sim, z_anchor=cfg.z_anchor, supp_eps=cfg.supp_eps)

    t = np.zeros(n + 1)
    phi = np.zeros(n + 1)
    psi = np.zeros(n + 1)
    e = np.zeros(n + 1)
    removed = np.zeros(n + 1)
    vre = np.zeros(n + 1)
    vim = np.zeros(n + 1)

    def _rec(i):
        phi[i] = _sector_phase(sim.a_A1.reshape(-1))
        psi[i] = _sector_phase(sim.b_w.reshape(-1))
        e[i] = sim.total_energy()
        t[i] = sim.time
        vre[i] = float(np.var(np.real(sim.b_w[mask]))) if mask.any() else 0.0
        vim[i] = float(np.var(np.imag(sim.b_w[mask]))) if mask.any() else 0.0

    _rec(0)
    cum = 0.0
    for i in range(1, n + 1):
        sim.step()
        cum += apply_clamp(sim, mask, branch)
        removed[i] = cum
        _rec(i)

    return ClampedTrace(t=t, phi_tor=phi, psi_pol=psi, e_total=e, removed_cum=removed,
                        var_re_anchor=vre, var_im_anchor=vim)


# ═════════════════════════════════════════════════════════════════════════════
# ROTATION NUMBER (the traversal read — two methods, F4 caveat honored)
# ═════════════════════════════════════════════════════════════════════════════
def _winding_rate(angles: np.ndarray) -> float:
    """The mean winding RATE (turns per step) = slope of the linear fit to the
    unwrapped phase / 2π. This is the window-noise-IMMUNE rotation-number estimator:
    unlike endpoint turns (Δφ over the window), a least-squares slope averages the
    sloshing modulation and does NOT jump when the window fails to contain an integer
    number of periods (the #417 quasi-periodic-window caveat). The standard robust
    rotation-number read; what the pre-reg §4 'DETUNING RESPONSE of ρ' load-bearing
    discriminator requires."""
    y = np.unwrap(angles)
    x = np.arange(len(y), dtype=float)
    return float(np.polyfit(x, y, 1)[0] / (2.0 * np.pi))


def rotation_number(tr: ClampedTrace) -> dict:
    """The traversal rotation number ρ, read TWO ways.

    PRIMARY (load-bearing, pre-reg §4) — SLOPE-based rate ratio ρ = (φ-rate)/(ψ-rate),
    window-noise-immune. The DETUNING-RESPONSE discriminator: LOCK ⇒ ρ holds plateaus
    vs the knob; TRACK ⇒ ρ follows the knob (as #417's free orbit did).

    SECONDARY (F4 two-method) — endpoint net turns by unwrap AND circulation. F4 caveat
    HONORED: the two share a wrapped-increment estimator (near-vacuous agreement) AND
    endpoint turns are window-noise-SENSITIVE; F4 is NOT the discriminator."""
    n = len(tr.phi_tor) - 1
    p_u = _net_turns_unwrap(tr.phi_tor, 0, n)
    q_u = _net_turns_unwrap(tr.psi_pol, 0, n)
    p_c = _net_turns_circulation(tr.phi_tor, 0, n)
    q_c = _net_turns_circulation(tr.psi_pol, 0, n)
    phi_rate = _winding_rate(tr.phi_tor)
    psi_rate = _winding_rate(tr.psi_pol)
    rho_slope = phi_rate / psi_rate if abs(psi_rate) > 1e-9 else float("nan")
    rho_ends = p_u / q_u if abs(q_u) > 1e-9 else float("nan")
    return {
        # primary (load-bearing, window-noise-immune)
        "rho": rho_slope, "phi_rate": phi_rate, "psi_rate": psi_rate,
        # secondary (F4 two-method endpoint read)
        "rho_endpoints": rho_ends,
        "phi_turns": p_u, "psi_turns": q_u,
        "phi_turns_circ": p_c, "psi_turns_circ": q_c,
        "two_reads_agree": bool(abs(p_u - p_c) < 0.2 and abs(q_u - q_c) < 0.2),
        "psi_resolved": bool(abs(psi_rate) * n >= 0.5),
    }


# ═════════════════════════════════════════════════════════════════════════════
# SIGNATURE 1 — MODE-LOCKING vs TRACKING (the fine detuning sweep)
# ═════════════════════════════════════════════════════════════════════════════
def detuning_sweep(cfg: TetheredPivotConfig, *, branch: str) -> dict:
    """ρ(ω_s) over the frozen fine sweep (ω_b=1 fixed), for the given branch AND for
    the clamp-OFF control. LOCK ⇒ plateaus+jumps; TRACK ⇒ ρ_anchored ≈ ρ_free
    continuous. Also records the four rational points {1:1,2:3,3:2,1:2}."""
    os_arr = np.array(cfg.sweep_os, dtype=float)
    rho_anch = np.full(len(os_arr), np.nan)
    rho_free = np.full(len(os_arr), np.nan)
    psi_anch = np.full(len(os_arr), np.nan)
    for i, os in enumerate(os_arr):
        ta = trace_orbit_clamped(cfg, omega_b=cfg.omega_b, omega_s=os, branch=branch)
        tf = trace_orbit_clamped(cfg, omega_b=cfg.omega_b, omega_s=os, branch="off")
        rho_anch[i] = rotation_number(ta)["rho"]
        rho_free[i] = rotation_number(tf)["rho"]
        psi_anch[i] = rotation_number(ta)["psi_turns"]

    rationals = {}
    for (pb, qs) in cfg.rational_points:
        tr = trace_orbit_clamped(cfg, omega_b=float(pb), omega_s=float(qs), branch=branch)
        trf = trace_orbit_clamped(cfg, omega_b=float(pb), omega_s=float(qs), branch="off")
        rationals[f"{pb}:{qs}"] = {
            "rho_anchored": rotation_number(tr)["rho"],
            "rho_free": rotation_number(trf)["rho"],
            "carrier_ratio": pb / qs,
        }
    return {"os": os_arr.tolist(), "rho_anchored": rho_anch.tolist(),
            "rho_free": rho_free.tolist(), "psi_turns_anchored": psi_anch.tolist(),
            "rational_points": rationals}


def lock_detector(os: np.ndarray, rho_anchored: np.ndarray, rho_free: np.ndarray,
                  *, flat_tol: float = 0.03, jump_tol: float = 0.15) -> dict:
    """Distinguish LOCK (anchor-INDUCED plateaus + discrete jumps) from TRACK
    (ρ_anchored ≈ ρ_free — the anchor changes nothing).

    CONTROL-SUBTRACTED discriminator (pre-reg §4 'the DETUNING RESPONSE of ρ' +
    §6 the clamp-OFF control as the mandated baseline): the coupled tank's ρ(ω_s)
    already SATURATES near 1.0 at high ω_s, so the FREE control ITSELF has a large
    absolute staircase_fraction. Thresholding the anchored curve's ABSOLUTE flatness
    conflates that shared baseline with an anchor effect. The physical question — does
    the ANCHOR change the response — is answered by the EXCESS of anchored over free:
      excess_staircase = fraction of intervals where anchored is flat AND free is NOT
                         (anchor-INDUCED plateaus, baseline-subtracted);
      track_R2         = R² of ρ_anchored vs ρ_free (1 ⇒ the anchor changes nothing).
    LOCK ⇔ excess_staircase≥0.4 AND excess_jumps≥1 (anchor adds plateaus/jumps the
    free control lacks). TRACK ⇔ track_R2≥0.9 AND excess_staircase<0.2 (anchored
    follows free; no anchor-induced plateaus). The ABSOLUTE metrics are also reported
    (transparency — they are what a control-BLIND detector would have binned)."""
    os = np.asarray(os, float)
    ra = np.asarray(rho_anchored, float)
    rf = np.asarray(rho_free, float)
    ok = np.isfinite(ra) & np.isfinite(rf)
    ra, rf = ra[ok], rf[ok]
    if len(ra) < 3:
        return {"verdict": "INCONCLUSIVE", "reason": "too few resolved sweep points"}
    da, df = np.abs(np.diff(ra)), np.abs(np.diff(rf))
    a_flat, f_flat = da < flat_tol, df < flat_tol
    staircase_fraction = float(np.mean(a_flat))          # ABSOLUTE (control-blind)
    free_staircase_fraction = float(np.mean(f_flat))     # the shared baseline
    jump_count = int(np.sum(da > jump_tol))
    # anchor-INDUCED (baseline-subtracted): flat/jump where the free control is NOT
    excess_staircase = float(np.mean(a_flat & ~f_flat))
    excess_jumps = int(np.sum((da > jump_tol) & ~(df > jump_tol)))
    ss_res = float(np.sum((ra - rf) ** 2))
    ss_tot = float(np.sum((ra - ra.mean()) ** 2)) + 1e-30
    track_R2 = 1.0 - ss_res / ss_tot
    max_abs_dev = float(np.max(np.abs(ra - rf)))
    is_lock = bool(excess_staircase >= 0.4 and excess_jumps >= 1)
    is_track = bool(track_R2 >= 0.9 and excess_staircase < 0.2)
    verdict = "LOCK" if is_lock else ("TRACK" if is_track else "PARTIAL")
    return {"staircase_fraction": staircase_fraction,
            "free_staircase_fraction": free_staircase_fraction,
            "excess_staircase": excess_staircase, "excess_jumps": excess_jumps,
            "jump_count": jump_count, "track_R2": track_R2,
            "max_abs_dev": max_abs_dev, "verdict": verdict}


# ═════════════════════════════════════════════════════════════════════════════
# SIGNATURE 2 — HYSTERESIS (up vs down ramp, state carried = memory)
# ═════════════════════════════════════════════════════════════════════════════
def hysteresis_ramp(cfg: TetheredPivotConfig, *, branch: str,
                    block_steps: int = 100) -> dict:
    """Ramp ω_s up (0.7→1.4) then down (1.4→0.7) CARRYING the state across the ramp
    (memory). Per ω_s block, read the incremental windowed ρ. LOCK ⇒ jump locations
    differ up-vs-down (hysteresis loop, width>0); TRACK ⇒ width≈0."""
    grid = np.array(cfg.sweep_os, float)

    def _ramp(order):
        ps = cfg.to_ps_cfg(omega_s=order[0])
        sim = build_seeded_sim(ps)
        mask = anchor_mask(sim, z_anchor=cfg.z_anchor, supp_eps=cfg.supp_eps)
        rhos = []
        for os in order:
            # retune the ω_s carrier in-place (config swap; state carried = memory).
            # _assemble_H reads self.cfg.omega_s each step, so this retunes live.
            sim.cfg = cfg.to_ps_cfg(omega_s=float(os)).to_coupled_cfg()
            phis = [_sector_phase(sim.a_A1.reshape(-1))]
            psis = [_sector_phase(sim.b_w.reshape(-1))]
            for _ in range(block_steps):
                sim.step()
                apply_clamp(sim, mask, branch)
                phis.append(_sector_phase(sim.a_A1.reshape(-1)))
                psis.append(_sector_phase(sim.b_w.reshape(-1)))
            # slope-based block rate (window-noise-immune); guard the ρ singularity —
            # skip a block whose poloidal winding is unresolved (|ψ-rate|·block ≪ 1),
            # else φ/ψ→∞ manufactures a spurious "hysteresis" spike (the endpoint-read
            # artifact that contaminated the initial run).
            pr = _winding_rate(np.array(phis))
            qr = _winding_rate(np.array(psis))
            rhos.append(pr / qr if abs(qr) * block_steps >= 0.5 else np.nan)
        return np.array(rhos)

    rho_up = _ramp(grid)
    rho_dn = _ramp(grid[::-1])[::-1]   # re-align to ascending grid
    ok = np.isfinite(rho_up) & np.isfinite(rho_dn)
    width = float(np.max(np.abs(rho_up[ok] - rho_dn[ok]))) if ok.any() else float("nan")
    return {"os": grid.tolist(), "rho_up": rho_up.tolist(), "rho_down": rho_dn.tolist(),
            "hysteresis_width": width, "hysteresis_seen": bool(width > 0.10)}


# ═════════════════════════════════════════════════════════════════════════════
# SIGNATURE 3 — TERMINATION FLIP (the #260 μ-sign selector probe)
# ═════════════════════════════════════════════════════════════════════════════
def termination_flip(cfg: TetheredPivotConfig, *, points=((1, 1), (2, 3), (3, 2), (1, 2))) -> dict:
    """Rerun cap (Re-node) vs mag (Im-node): does the traversal ORIENTATION INVERT?
    FLIP ⇒ the #260 μ-sign selector is a live temporal-winding observable; NO-FLIP ⇒
    the selector does not manifest in this read (report the null, no rescue).
    Orientation = sign(ψ-winding-rate) (the poloidal traversal direction, robust)."""
    rows = {}
    n_flip = 0
    n_res = 0
    for (pb, qs) in points:
        tc = trace_orbit_clamped(cfg, omega_b=float(pb), omega_s=float(qs), branch="capacitive")
        tm = trace_orbit_clamped(cfg, omega_b=float(pb), omega_s=float(qs), branch="magnetic")
        rc = rotation_number(tc)
        rm = rotation_number(tm)
        oc = float(np.sign(rc["psi_rate"]))
        om = float(np.sign(rm["psi_rate"]))
        flipped = bool(oc != 0 and om != 0 and oc != om)
        resolved = bool(rc["psi_resolved"] and rm["psi_resolved"])
        rows[f"{pb}:{qs}"] = {
            "psi_turns_cap": rc["psi_turns"], "psi_turns_mag": rm["psi_turns"],
            "rho_cap": rc["rho"], "rho_mag": rm["rho"],
            "orientation_cap": oc, "orientation_mag": om,
            "flipped": flipped, "resolved": resolved,
        }
        if resolved:
            n_res += 1
            if flipped:
                n_flip += 1
    return {"points": rows, "n_resolved": n_res, "n_flipped": n_flip,
            "flip_seen": bool(n_res > 0 and n_flip == n_res)}


# ═════════════════════════════════════════════════════════════════════════════
# GATE — DEAD-ACTUATOR (the clamp must demonstrably constrain)
# ═════════════════════════════════════════════════════════════════════════════
def dead_actuator_gate(cfg: TetheredPivotConfig, *, branch: str, n_steps: int = 60) -> dict:
    """The pinned quadrature's variance over M must COLLAPSE vs unclamped (frozen §7:
    var_clamped/var_unclamped < 0.05). A clamp that does not collapse the variance is
    a DEAD actuator ⇒ INCONCLUSIVE (no verdict on a dead clamp)."""
    tr_c = trace_orbit_clamped(cfg, omega_b=cfg.omega_b, omega_s=cfg.omega_s,
                               branch=branch, n_steps=n_steps)
    tr_o = trace_orbit_clamped(cfg, omega_b=cfg.omega_b, omega_s=cfg.omega_s,
                               branch="off", n_steps=n_steps)
    if branch == "capacitive":
        v_c = float(np.mean(tr_c.var_re_anchor[1:]))
        v_o = float(np.mean(tr_o.var_re_anchor[1:]))
        quad = "Re(b_ω) / V-node"
    else:
        v_c = float(np.mean(tr_c.var_im_anchor[1:]))
        v_o = float(np.mean(tr_o.var_im_anchor[1:]))
        quad = "Im(b_ω) / I-node"
    ratio = v_c / (v_o + 1e-30)
    return {"branch": branch, "pinned_quadrature": quad, "var_clamped": v_c,
            "var_unclamped": v_o, "var_ratio": ratio,
            "actuator_live": bool(ratio < 0.05)}


# ═════════════════════════════════════════════════════════════════════════════
# GATE — ENERGY LEDGER (clamp OFF conserves; clamp ON non-pumping)
# ═════════════════════════════════════════════════════════════════════════════
def energy_ledger(cfg: TetheredPivotConfig, *, branch: str, n_steps: int = 200) -> dict:
    """clamp OFF conserves joint norm to #417 standard (<1e-6); clamp ON is
    monotone-NON-PUMPING (max_t E(t) ≤ E(0)·(1+1e-9)) with the removed-norm budget
    reported. A clamp that PUMPS ⇒ INCONCLUSIVE (a pumped lock is an artifact)."""
    tr_o = trace_orbit_clamped(cfg, omega_b=cfg.omega_b, omega_s=cfg.omega_s,
                               branch="off", n_steps=n_steps)
    tr_c = trace_orbit_clamped(cfg, omega_b=cfg.omega_b, omega_s=cfg.omega_s,
                               branch=branch, n_steps=n_steps)
    e0_o, e0_c = tr_o.e_total[0], tr_c.e_total[0]
    off_drift = float(np.max(np.abs(tr_o.e_total - e0_o)) / (abs(e0_o) + 1e-30))
    on_max_gain = float((np.max(tr_c.e_total) - e0_c) / (abs(e0_c) + 1e-30))
    removed_frac = float(tr_c.removed_cum[-1] / (abs(e0_c) + 1e-30))
    return {
        "off_conserved": bool(off_drift < 1e-6), "off_max_rel_drift": off_drift,
        "on_non_pumping": bool(on_max_gain <= 1e-9), "on_max_rel_energy_gain": on_max_gain,
        "on_removed_norm_frac": removed_frac,
    }


# ═════════════════════════════════════════════════════════════════════════════
# VALIDATE-ON-KNOWN — the lock-detector must separate a planted staircase from a
# planted linear (tracking) rotation number
# ═════════════════════════════════════════════════════════════════════════════
def _planted_locked(os: np.ndarray) -> np.ndarray:
    """A synthetic rotation-number STAIRCASE: ρ locked at rational plateaus with
    discrete jumps (the LOCK signature)."""
    ra = np.empty_like(os)
    for i, x in enumerate(os):
        if x < 0.85:
            ra[i] = 1.5
        elif x < 1.05:
            ra[i] = 1.0
        elif x < 1.25:
            ra[i] = 2.0 / 3.0
        else:
            ra[i] = 0.5
    return ra


def _planted_tracking(os: np.ndarray) -> np.ndarray:
    """A synthetic LINEAR (tracking) rotation number ρ = 1/os (the carrier ratio
    ω_b/ω_s at ω_b=1) — continuous, no plateaus (the TRACK signature)."""
    return 1.0 / os


def validate_lock_detector() -> dict:
    """The lock-detector must read a planted STAIRCASE as LOCK and a planted LINEAR
    as TRACK; else it is broken → HALT (frozen §7)."""
    os = np.array([0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.10,
                   1.15, 1.20, 1.25, 1.30, 1.35, 1.40])
    locked = _planted_locked(os)
    tracking = _planted_tracking(os)
    d_lock = lock_detector(os, locked, tracking)      # rho_free = tracking (contrast)
    d_track = lock_detector(os, tracking, tracking)   # anchored == free ⇒ TRACK
    return {
        "planted_locked_verdict": d_lock["verdict"],
        "planted_locked_metrics": d_lock,
        "planted_tracking_verdict": d_track["verdict"],
        "planted_tracking_metrics": d_track,
        "ok": bool(d_lock["verdict"] == "LOCK" and d_track["verdict"] == "TRACK"),
    }


# ═════════════════════════════════════════════════════════════════════════════
# TOP-LEVEL DRIVER — validate → gates → 3 signatures → binned verdict
# ═════════════════════════════════════════════════════════════════════════════
def run_tethered_pivot(cfg: TetheredPivotConfig | None = None) -> dict:
    """Run the full frozen tethered-pivot test and bin LOCK/TRACK/PARTIAL/INCONCLUSIVE
    (pre-reg §8). Sequence: validate-on-known → dead-actuator + energy gates →
    signature 1 (sweep + lock-detector) → signature 2 (hysteresis) → signature 3
    (termination flip)."""
    cfg = cfg or TetheredPivotConfig()
    out: dict = {"config": {k: getattr(cfg, k) for k in
                            ("N", "n_steps", "z_anchor", "omega_b", "R", "r", "dt")}}

    # 0. VALIDATE-ON-KNOWN
    vlk = validate_lock_detector()
    out["validate_on_known"] = vlk
    if not vlk["ok"]:
        out["verdict"] = "HALT"
        out["reason"] = f"lock-detector broken: locked→{vlk['planted_locked_verdict']}, tracking→{vlk['planted_tracking_verdict']}"
        return out

    # 1. GATES (dead-actuator + energy) on the primary capacitive branch
    dead = dead_actuator_gate(cfg, branch="capacitive")
    dead_mag = dead_actuator_gate(cfg, branch="magnetic")
    eng = energy_ledger(cfg, branch="capacitive")
    out["dead_actuator"] = {"capacitive": dead, "magnetic": dead_mag}
    out["energy_ledger"] = eng
    if not (dead["actuator_live"] and dead_mag["actuator_live"]):
        out["verdict"] = "INCONCLUSIVE"
        out["reason"] = "dead-actuator: clamp did not collapse the pinned-quadrature variance"
        return out
    if not eng["on_non_pumping"]:
        out["verdict"] = "INCONCLUSIVE"
        out["reason"] = f"clamp PUMPS (max rel gain {eng['on_max_rel_energy_gain']:.2e}) — a pumped lock is an artifact"
        return out

    # 2. SIGNATURE 1 — mode-locking vs tracking (capacitive branch)
    sweep = detuning_sweep(cfg, branch="capacitive")
    det = lock_detector(np.array(sweep["os"]), np.array(sweep["rho_anchored"]),
                        np.array(sweep["rho_free"]))
    out["signature_1_mode_locking"] = {"sweep": sweep, "detector": det}

    # 3. SIGNATURE 2 — hysteresis (control-subtracted: the free clamp-OFF ramp has its
    #    OWN short-block read-noise width; only the EXCESS over that baseline is an
    #    anchor-induced loop, per §6's mandated control).
    hys = hysteresis_ramp(cfg, branch="capacitive")
    hys_off = hysteresis_ramp(cfg, branch="off")
    excess_width = float(hys["hysteresis_width"] - hys_off["hysteresis_width"])
    hys["free_control_width"] = hys_off["hysteresis_width"]
    hys["excess_width"] = excess_width
    hys["hysteresis_seen"] = bool(excess_width > 0.10)   # override: EXCESS over control
    out["signature_2_hysteresis"] = hys

    # 4. SIGNATURE 3 — termination flip (#260 selector)
    flip = termination_flip(cfg)
    out["signature_3_termination_flip"] = flip

    # BIN (pre-reg §8) — no preferred outcome. Signatures are anchor-INDUCED
    # (control-subtracted): a feature the free clamp-OFF orbit already has is NOT the
    # anchor's doing.
    s1 = det["verdict"]                       # LOCK / TRACK / PARTIAL (excess-based)
    s2 = hys["hysteresis_seen"]               # bool (excess over free control)
    s3 = flip["flip_seen"]                    # bool
    if s1 == "LOCK" and s2 and s3:
        verdict = "LOCK"
        reason = ("all 3 signatures: ρ holds rational plateaus + discrete jumps, "
                  "hysteresis at the jumps, cap↔mag orientation flip → the (2,3) gains "
                  "a DERIVED protection mechanism (BC quantization); SELECTION stays IMPORTED")
    elif s1 == "TRACK" and (not s2) and (not s3):
        verdict = "TRACK"
        reason = ("the anchored ρ STILL follows the knob (track_R2="
                  f"{det['track_R2']:.3f}, excess_staircase={det['excess_staircase']:.3f} vs "
                  f"free_staircase={det['free_staircase_fraction']:.3f} — the anchor adds NO "
                  f"plateaus the free control lacks), no excess hysteresis, no termination "
                  "flip → the pivot picture DIES, banked next to #417; the carrier-set "
                  "global-phase mechanism is ROBUST to anchoring")
    else:
        verdict = "PARTIAL"
        reason = (f"per-signature: mode-locking={s1}, hysteresis={s2}, termination_flip={s3} "
                  "— report each; name what held and what did not")
    out["verdict"] = verdict
    out["reason"] = reason
    out["signature_summary"] = {"mode_locking": s1, "hysteresis": bool(s2), "termination_flip": bool(s3)}
    return out


if __name__ == "__main__":
    import json

    print("TETHERED-PIVOT MODE-LOCKING — anchored (2,3) traversal vs #417 free tracking")
    print("=" * 78)
    cfg = TetheredPivotConfig()
    res = run_tethered_pivot(cfg)
    print(json.dumps(res.get("signature_summary", {}), indent=2))
    if "signature_1_mode_locking" in res:
        d = res["signature_1_mode_locking"]["detector"]
        print(f"signature-1 detector: {d}")
        print(f"hysteresis width: {res['signature_2_hysteresis']['hysteresis_width']:.4f}")
        print(f"termination flip: n_flipped={res['signature_3_termination_flip']['n_flipped']}"
              f"/{res['signature_3_termination_flip']['n_resolved']}")
    print("-" * 78)
    print(f"VERDICT: {res['verdict']}")
    print(f"REASON : {res['reason']}")
