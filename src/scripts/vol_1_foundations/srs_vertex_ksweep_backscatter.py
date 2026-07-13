"""srs vertex k-sweep backscatter driver (carrier-wave frame) — T4 ontology fork.

Adjudicates the srs per-vertex Γ=−1/3 ontology fork (docket T4): is the per-vertex
mismatched-tee reflection physically expressed for propagating collective (Bloch)
modes, or homogenized away? Launches FORWARD wavepackets on the srs scalar-TLM
lattice across a k-sweep and measures the backscatter fraction R(k·ℓ_node), with
the saturation KERNEL OFF (linear lattice).

FROZEN prereg: research/2026-07-13_srs-vertex-ksweep-backscatter_prereg_FROZEN.md
Handoff:       _orchestration/2026-07-13_srs-vertex-ksweep-handoff.md

Sector header — MODE linear wavepacket propagation (carrier/homogenization
property of the network, NOT a saturation test); REGIME cold, KERNEL OFF (no
Op14; the combinatorial scatter+connect step is orthogonal ⇒ lossless to machine
ε; Axiom 3: the −1/3 is reactive back-scatter / redistribution, never loss);
PHASE-STATE freely-propagating sub-yield; SECTOR scalar/compression channel.

Discipline: substrate-native-check (scatter+connect on the srs graph, NOT a
continuum solver; the eigenmode-population observable is REJECTED because momentum
does not commute with the one-step operator — see prereg §Measurement design);
ave-driver-script-honesty (this is a FORWARD measurement — no CODATA target, no
fit; the classifier is frozen in the prereg); ave-canonical-source (constants
imported, verified). consistency-vs-emergence: peer-with-SM consistency physics on
the reflection axis (a periodic medium is transparent long-λ / reflective at band
edges) — the deliverable is the quantitative band-edge characterization, NOT an
AVE-distinct chord. Platform firewall: srs scalar-TLM ONLY (no cage / VacuumEngine3D);
reuses the frozen v9 scaffold graph + Op5 scatter primitives (no new chiral_lattice_vN).
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_dynamics as cld
from ave.core.constants import C_0, EPSILON_0, HBAR, L_NODE, M_E, MU_0, Z_0
from ave_path_util import sim_output

AXIS = 2  # ẑ = propagation axis
PER_VERTEX_GAMMA2 = 1.0 / 9.0  # |Γ|² = 1/9 bare-tee scale (COUNTING fact)
NETWORK_VG = cld.ANALYTIC_NETWORK_FACTOR  # 1/√3 long-wavelength network velocity

# ── frozen production config (mirrors the prereg tables) ─────────────────────
PRIMARY_L = 16
CONVERGE_LS = (12, 20)
KELL_SWEEP = np.linspace(0.15, 3.00, 18)
WIDTH_FRAC = 0.09
Z0_PCTILE = 12.0
T_BURN = 15
P_DISORDER = 0.5
DISORDER_SEED = 12345
PLANT_D_ANGLE = 0.15

# frozen metric windows + thresholds
LW_LO, LW_HI = 0.15, 0.50
BE_LO, BE_HI = 2.00, 3.00
SIGMA_MAX_I = 0.35     # (i.a) long-λ suppression vs incoherent limit
RHO_MIN_I = 2.0        # (i.b) band-edge rise ratio
RBE_MIN = 0.5 * PER_VERTEX_GAMMA2   # (i.c)/(iii) half the bare-tee scale = 0.05556
DRIFT_MAX = 1e-8       # G1 lossless
SRANK_MIN = 0.7        # G3 monotone-rise
ENANTIO_TOL = 0.20     # G4 chirality-blind


# ── canonical-source cross-check ─────────────────────────────────────────────
def verify_constants(net: cl.LatticeNet) -> dict:
    """ave-canonical-source gate. Verifies the imported constants against their
    canonical DEFINING RELATIONSHIPS (never against hardcoded CODATA literals —
    that is the magic-number anti-pattern verify_universe.py guards). The only
    literals here are geometric (1.0) and tolerances."""
    nn = _mean_nn_bond(net)
    checks = {
        # canonical definitions (constants.py:113,293,112)
        "L_NODE == HBAR/(M_E*C_0)": (L_NODE, HBAR / (M_E * C_0)),
        "Z_0 == sqrt(MU_0/EPSILON_0)": (Z_0, float(np.sqrt(MU_0 / EPSILON_0))),
        "EPSILON_0 == 1/(MU_0*C_0^2)": (EPSILON_0, 1.0 / (MU_0 * C_0 * C_0)),
        # geometric: a_cell=2√2 ⇒ NN bond ≡ node pitch ℓ_node = 1.0 (driver units)
        "NN_bond_cellunits == 1.0": (nn, 1.0),
    }
    report = {}
    for name, (got, want) in checks.items():
        ok = abs(got - want) <= 1e-9 * abs(want) if want != 0 else got == want
        report[name] = {"value": float(got), "expected": float(want), "ok": bool(ok)}
        if not ok:
            raise AssertionError(f"verify_constants FAILED: {name}: {got} != {want}")
    return report


def _mean_nn_bond(net: cl.LatticeNet) -> float:
    ds = []
    for u in range(net.n_nodes):
        for v in net.neighbors[u]:
            d = net.pos[v] - net.pos[u]
            d -= net.box * np.round(d / net.box)
            ds.append(np.linalg.norm(d))
    return float(np.mean(ds))


# ── observable plumbing (frozen) ─────────────────────────────────────────────
def port_zvel(net: cl.LatticeNet) -> np.ndarray:
    """Axial velocity w[u,p] = −bond_unit[u][p]·ẑ of the STORED incident pulse
    (it arrived travelling neighbour→u ⇒ along −bond_unit). Shape (N, degree)."""
    bu = np.array([[net.bond_unit[u][p] for p in range(net.degree)]
                   for u in range(net.n_nodes)])
    return -bu[:, :, AXIS]


def prep(net: cl.LatticeNet) -> dict:
    """Per-lattice bundle: scatter matrix, a GATHER permutation for the fast
    one-step (V_new_flat = Vr_flat[gather], equivalent to the scatter+connect
    CONNECT map), and the axial-velocity split. Precomputed once per lattice."""
    S = cl.scatter_matrix(net.degree)
    src, dst = net.connect_index()
    D = net.n_nodes * net.degree
    gather = np.empty(D, dtype=np.int64)
    gather[dst] = src  # V_new.flat[dst]=Vr.flat[src] ⇔ V_new_flat = Vr_flat[gather]
    w = port_zvel(net)
    return {"net": net, "S": S, "gather": gather, "w": w,
            "wf": np.maximum(w, 0.0), "wb": np.maximum(-w, 0.0), "D": D}


def forward_packet(net, w, k, width_frac=WIDTH_FRAC):
    """Forward Gaussian launch: env·cos(k z)·relu(w) on forward ports (w>0)."""
    z = net.pos[:, AXIS]
    z0 = np.percentile(z[net.interior_mask], Z0_PCTILE)
    sigma = width_frac * net.box
    env = np.exp(-0.5 * ((z - z0) / sigma) ** 2)
    V = np.zeros((net.n_nodes, net.degree))
    fwd = w > 1e-9
    V[fwd] = (env[:, None] * np.cos(k * z[:, None]) * w)[fwd]
    return V


def _plant_d_pairs(net, w):
    """Per node, the most-forward and most-backward port index (for lossless
    sabotage plant D: an orthogonal fwd↔bwd rotation)."""
    pf = np.argmax(w, axis=1)
    pb = np.argmin(w, axis=1)
    return pf, pb


def evolve_R(bundle, k, *, disorder=False, plant=None, width_frac=WIDTH_FRAC):
    """Evolve a forward k-packet; return the frozen estimator R + diagnostics.

    R = mean_t b(t) over [T_BURN, ⌊t_transit⌋], b = E_bak/(E_fwd+E_bak). Fast
    one-step via the precomputed GATHER permutation. `plant` ∈ {None,'A','B','D'}
    corrupts the EVOLVED field (sabotage). Returns max energy drift (G1) too.
    """
    net, S, gather = bundle["net"], bundle["S"], bundle["gather"]
    w, wf, wb, D = bundle["w"], bundle["wf"], bundle["wb"], bundle["D"]
    ST = S.T
    deg = net.degree
    sign = None
    if disorder:
        rng = np.random.default_rng(DISORDER_SEED)
        sign = np.ones(D)
        sign[rng.random(D) < P_DISORDER] = -1.0
    if plant == "A":
        # kill-backward: zero all BACKWARD-moving ports (w<0), keep forward+transverse
        # (w>=0). Removing that energy is LOSSY ⇒ G1 fires; the surviving field has no
        # backward energy ⇒ b→0 ⇒ fakes bin (iii) NULL. (Prereg §Sabotage plant A.)
        keep = (w >= -1e-9).reshape(-1).astype(float)
    if plant == "B":
        inj = 0.02 * (w < -1e-9).reshape(-1).astype(float)  # backward source (ADDS E)
    if plant == "D":
        pf, pb = _plant_d_pairs(net, w)
        rows = np.arange(net.n_nodes)
        cD, sD = np.cos(PLANT_D_ANGLE), np.sin(PLANT_D_ANGLE)
    Vf = forward_packet(net, w, k, width_frac).reshape(-1)  # flat (D,)
    e0 = float(Vf @ Vf)
    t_transit = net.box / NETWORK_VG
    steps = int(np.ceil(3 * t_transit))
    b = np.empty(steps)
    drift = 0.0
    for t in range(steps):
        Vr = (Vf.reshape(net.n_nodes, deg) @ ST).reshape(-1)  # scatter
        if disorder:
            Vr *= sign
        if plant == "D":  # lossless orthogonal fwd↔bwd rotation per node
            Vg = Vr.reshape(net.n_nodes, deg)
            a = Vg[rows, pf].copy(); d = Vg[rows, pb].copy()
            Vg[rows, pf] = cD * a - sD * d
            Vg[rows, pb] = sD * a + cD * d
        Vf = Vr[gather]                                        # connect (gather)
        if plant == "A":
            Vf = Vf * keep
        elif plant == "B":
            Vf = Vf + inj
        e = Vf * Vf
        etot = float(e.sum())
        ef = float(e @ wf.reshape(-1)); eb = float(e @ wb.reshape(-1))
        b[t] = eb / (ef + eb + 1e-30)
        drift = max(drift, abs(etot - e0) / e0)
    it = int(t_transit)
    return {
        "R": float(np.mean(b[T_BURN:it])),
        "R_median": float(np.median(b[T_BURN:it])),
        "R_long": float(np.median(b[T_BURN:int(2.5 * it)])),
        "drift": float(drift),
        "b0": float(b[0]),
    }


def sweep(bundle, ks, *, disorder=False, width_frac=WIDTH_FRAC):
    return np.array([evolve_R(bundle, k, disorder=disorder, width_frac=width_frac)["R"]
                     for k in ks])


# ── metrics + frozen classifier ──────────────────────────────────────────────
def _window_mean(ks, R, lo, hi):
    m = (ks >= lo) & (ks <= hi)
    return float(np.mean(R[m])) if m.any() else float("nan")


def _spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    rx -= rx.mean(); ry -= ry.mean()
    denom = np.sqrt((rx * rx).sum() * (ry * ry).sum())
    return float((rx * ry).sum() / denom) if denom > 0 else 0.0


@dataclass
class Metrics:
    R_LW: float
    R_BE: float
    R_dis: float
    gamma2: float
    rho: float
    sigma: float
    s_rank: float


def compute_metrics(ks, R_pristine, R_disorder) -> Metrics:
    R_LW = _window_mean(ks, R_pristine, LW_LO, LW_HI)
    R_BE = _window_mean(ks, R_pristine, BE_LO, BE_HI)
    R_dis = float(np.mean(R_disorder))
    return Metrics(
        R_LW=R_LW, R_BE=R_BE, R_dis=R_dis, gamma2=PER_VERTEX_GAMMA2,
        rho=R_BE / R_LW if R_LW > 0 else float("inf"),
        sigma=R_LW / R_dis if R_dis > 0 else float("inf"),
        s_rank=_spearman(ks, R_pristine),
    )


def classify(m: Metrics) -> tuple[str, dict]:
    """Frozen three-way classifier from the prereg."""
    cond_i = {
        "i.a sigma<=0.35": m.sigma <= SIGMA_MAX_I,
        "i.b rho>=2.0": m.rho >= RHO_MIN_I,
        "i.c R_BE>=0.5*gamma2": m.R_BE >= RBE_MIN,
        "i.d R_dis>=2*R_LW": m.R_dis >= 2 * m.R_LW,
    }
    cond_ii = {
        "ii.a sigma>0.35": m.sigma > SIGMA_MAX_I,
        "ii.b rho<2.0": m.rho < RHO_MIN_I,
        "ii.c R_LW>=0.5*gamma2": m.R_LW >= RBE_MIN,
    }
    cond_iii = {
        "iii.a R_BE<0.5*gamma2": m.R_BE < RBE_MIN,
        "iii.b R_LW<0.5*gamma2": m.R_LW < RBE_MIN,
    }
    if all(cond_i.values()):
        verdict = "(i) HOMOGENIZATION-SPLIT"
    elif all(cond_ii.values()):
        verdict = "(ii) REAL-AT-ALL-K"
    elif all(cond_iii.values()):
        # frozen bin-(iii) meter-blind sub-clause: if the disorder control ALSO
        # reads low, the meter is blind ⇒ INDETERMINATE, not a genuine null.
        verdict = ("INDETERMINATE (meter blind — disorder control also low)"
                   if m.R_dis < 0.15 else "(iii) NULL-EVERYWHERE")
    else:
        verdict = "INDETERMINATE / MIXED"
    return verdict, {"cond_i": cond_i, "cond_ii": cond_ii, "cond_iii": cond_iii}


# ── band-structure cross-check ───────────────────────────────────────────────
def band_edge_probe(net):
    """v_g(k) from the canonical dispersion machinery; where does v_g drop?"""
    disp = cld.measure_dispersion(net, axis=AXIS, m_values=(1, 2, 3, 4, 5, 6), n_steps=600)
    ks = [k for k, _, _ in disp]
    cs = [c for _, _, c in disp]  # phase velocity c(k); network factor = c/c_link
    c_link = cld.mean_bond_length(net)
    return {
        "k": [float(x) for x in ks],
        "phase_velocity_over_clink": [float(c / c_link) for c in cs],
        "long_wavelength_factor": float(cs[0] / c_link),
        "analytic_factor_1_over_sqrt3": float(NETWORK_VG),
    }


# ── sabotage battery ─────────────────────────────────────────────────────────
def sabotage_battery(bundle):
    """Each plant corrupts the EVOLVED field; assert the frozen gate catches it.
    Probe at a long-λ and a band-edge k."""
    k_lw, k_be = 0.30, 2.80
    out = {}
    # G1 lossless on pristine (must PASS)
    pr = evolve_R(bundle, k_be)
    out["pristine_drift"] = pr["drift"]
    out["G1_pristine_lossless_pass"] = pr["drift"] < DRIFT_MAX
    # Plant A — kill-backward (LOSSY → G1 must trip)
    a = evolve_R(bundle, k_be, plant="A")
    out["plantA_kill_backward"] = {"R": a["R"], "drift": a["drift"],
                                   "G1_trips": a["drift"] >= DRIFT_MAX}
    # Plant B — inject-source (ADDS ENERGY → G1 must trip)
    b = evolve_R(bundle, k_be, plant="B")
    out["plantB_inject_source"] = {"R": b["R"], "drift": b["drift"],
                                   "G1_trips": b["drift"] >= DRIFT_MAX}
    # Plant D — lossless fwd↔bwd mix (G1 PASSES, but flattens/elevates R → G3 trips)
    d_lw = evolve_R(bundle, k_lw, plant="D")
    d_be = evolve_R(bundle, k_be, plant="D")
    clean_lw = evolve_R(bundle, k_lw)
    clean_be = evolve_R(bundle, k_be)
    rho_clean = clean_be["R"] / clean_lw["R"] if clean_lw["R"] > 0 else float("inf")
    rho_plantD = d_be["R"] / d_lw["R"] if d_lw["R"] > 0 else float("inf")
    out["plantD_lossless_mix"] = {
        "R_lw": d_lw["R"], "R_be": d_be["R"], "drift_lw": d_lw["drift"],
        "G1_passes": d_lw["drift"] < DRIFT_MAX and d_be["drift"] < DRIFT_MAX,
        "rho_clean": float(rho_clean), "rho_plantD": float(rho_plantD),
        # G3 signature: plant D collapses the band-edge rise (rho→~1) and
        # elevates the long-λ floor toward the incoherent scale
        "G3_trips_rise_collapse": rho_plantD < RHO_MIN_I and rho_clean >= RHO_MIN_I,
        "G3_trips_lw_elevated": d_lw["R"] > 2 * clean_lw["R"],
    }
    return out


# ── main ─────────────────────────────────────────────────────────────────────
def main():
    result: dict = {"config": {
        "primary_L": PRIMARY_L, "converge_Ls": list(CONVERGE_LS),
        "kell_sweep": [float(x) for x in KELL_SWEEP], "width_frac": WIDTH_FRAC,
        "p_disorder": P_DISORDER, "disorder_seed": DISORDER_SEED,
        "per_vertex_gamma2": PER_VERTEX_GAMMA2, "network_vg": float(NETWORK_VG),
        "thresholds": {"sigma_max_i": SIGMA_MAX_I, "rho_min_i": RHO_MIN_I,
                       "RBE_min": RBE_MIN, "drift_max": DRIFT_MAX,
                       "srank_min": SRANK_MIN, "enantio_tol": ENANTIO_TOL},
    }}

    # primary lattice (right enantiomorph)
    print(f"[srs-ksweep] building primary L={PRIMARY_L} ...", flush=True)
    net = cl.build_srs_net(PRIMARY_L, "right")
    bundle = prep(net)
    result["verify_constants"] = verify_constants(net)
    ks = KELL_SWEEP

    print(f"[srs-ksweep] primary L={PRIMARY_L} N={net.n_nodes} box={net.box:.3f}; "
          f"sweeping ...", flush=True)
    R_pristine = sweep(bundle, ks)
    R_disorder = sweep(bundle, ks, disorder=True)

    # enantiomorph control (left) for the chirality-blind gate G4
    print("[srs-ksweep] building left enantiomorph ...", flush=True)
    netL = cl.build_srs_net(PRIMARY_L, "left")
    bundleL = prep(netL)
    R_left = sweep(bundleL, ks)

    m = compute_metrics(ks, R_pristine, R_disorder)
    verdict, cond = classify(m)

    # gates
    enantio_dev = np.abs(R_pristine - R_left) / (np.abs(R_pristine) + 1e-9)
    g1 = float(evolve_R(bundle, float(ks[-1]))["drift"]) < DRIFT_MAX
    gates = {
        "G1_lossless": bool(g1),
        "G2_meter_not_blind": bool(m.R_dis >= 2 * m.R_LW),
        "G3_monotone_rise": bool(m.s_rank >= SRANK_MIN),
        "G4_enantiomorph_symmetry": bool(np.median(enantio_dev) < ENANTIO_TOL),
        "G4_max_dev": float(np.max(enantio_dev)),
        "G4_median_dev": float(np.median(enantio_dev)),
    }

    # convergence boxes (report R_LW, R_BE only)
    conv = {}
    for LL in CONVERGE_LS:
        print(f"[srs-ksweep] convergence build L={LL} ...", flush=True)
        nc = cl.build_srs_net(LL, "right")
        Rc = sweep(prep(nc), ks)
        conv[f"L{LL}"] = {"R_LW": _window_mean(ks, Rc, LW_LO, LW_HI),
                          "R_BE": _window_mean(ks, Rc, BE_LO, BE_HI),
                          "R_of_k": [float(x) for x in Rc]}

    result.update({
        "kell": [float(x) for x in ks],
        "R_pristine": [float(x) for x in R_pristine],
        "R_disorder": [float(x) for x in R_disorder],
        "R_left_enantiomorph": [float(x) for x in R_left],
        "metrics": asdict(m),
        "classifier_conditions": cond,
        "verdict": verdict,
        "gates": gates,
        "convergence": conv,
        "band_structure": band_edge_probe(net),
        "sabotage": sabotage_battery(bundle),
    })

    # ── outputs ──────────────────────────────────────────────────────────────
    out_json = sim_output("srs_vertex_ksweep_backscatter.json")
    out_json.write_text(json.dumps(result, indent=2))
    print(f"[srs-ksweep] verdict: {verdict}")
    print(f"[srs-ksweep] R_LW={m.R_LW:.4f} R_BE={m.R_BE:.4f} R_dis={m.R_dis:.4f} "
          f"sigma={m.sigma:.3f} rho={m.rho:.3f} s_rank={m.s_rank:.3f}")
    print(f"[srs-ksweep] gates: {gates}")
    print(f"[srs-ksweep] wrote {out_json}")

    _figure(ks, R_pristine, R_disorder, R_left, m, verdict)
    return result


def _figure(ks, R_pristine, R_disorder, R_left, m, verdict):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ave.viz import style
    style.apply()  # house white style (feedback_figure_house_style_white_default)

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.plot(ks, R_pristine, "o-", color="#0072B2", label="pristine srs (coherent)")
    ax.plot(ks, R_left, "s--", color="#56B4E9", alpha=0.7,
            label="left enantiomorph (G4)")
    ax.plot(ks, R_disorder, "^-", color="#D55E00",
            label="phase-disordered (incoherent limit)")
    ax.axhline(PER_VERTEX_GAMMA2, color="#000000", ls=":", lw=1.2,
               label=r"per-vertex $|\Gamma|^2=1/9$")
    ax.axhline(RBE_MIN, color="#999999", ls="-.", lw=0.9,
               label=r"$|\Gamma|^2/2$ (tee-resolves threshold)")
    ax.axvspan(LW_LO, LW_HI, color="#0072B2", alpha=0.06)
    ax.axvspan(BE_LO, BE_HI, color="#D55E00", alpha=0.06)
    ax.set_xlabel(r"$k\cdot\ell_{\mathrm{node}}$  (dimensionless)")
    ax.set_ylabel(r"backscatter fraction $R = \langle E_{\mathrm{bak}}/E_{\mathrm{tot}}\rangle_t$")
    ax.set_ylim(0, 0.55)
    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=8, frameon=False)
    txt = (f"verdict: {verdict}\n"
           f"$\\sigma=R_{{LW}}/R_{{dis}}={m.sigma:.2f}$   "
           f"$\\rho=R_{{BE}}/R_{{LW}}={m.rho:.2f}$")
    ax.text(0.02, 0.97, txt, transform=ax.transAxes, va="top", fontsize=8,
            bbox=dict(boxstyle="round", fc="white", ec="#999999", alpha=0.9))
    fig.tight_layout()
    out_png = sim_output("srs_vertex_ksweep_backscatter.png")
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    print(f"[srs-ksweep] wrote {out_png}")


def refig_from_json():
    """Regenerate the figure from the saved JSON (no re-run of the sweep)."""
    data = json.loads(sim_output("srs_vertex_ksweep_backscatter.json").read_text())
    ks = np.array(data["kell"])
    m = Metrics(**data["metrics"])
    _figure(ks, np.array(data["R_pristine"]), np.array(data["R_disorder"]),
            np.array(data["R_left_enantiomorph"]), m, data["verdict"])


if __name__ == "__main__":
    import sys
    if "--refig" in sys.argv:
        refig_from_json()
    else:
        main()
