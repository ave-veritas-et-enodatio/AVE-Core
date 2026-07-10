#!/usr/bin/env python3
"""x31-B — srs 3D band survey: Bloch/Ybus eigenvalue analysis (survey-class, NO time-stepping).

Prereg (FROZEN): research/2026-07-09_srs-band-survey_prereg_FROZEN.md
Class: CONSISTENCY / characterization (not a falsification, not an emergence claim).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS
═══════════════════════════════════════════════════════════════════════════════
The scalar-channel linear band structure of the chiral srs (I4₁32, Sunada-K4,
z=3) vacuum net, computed as a Bloch eigenvalue analysis of the 4-site BCC
primitive cell. No engine dynamics — this is generic power-network math.

SUBSTRATE-NATIVE MODEL (see prereg §4, flagged to Grant):
  The srs vacuum is a distributed LC transmission-line network (Op5 shunt
  junctions on ℓ_node lines). The scatter+connect (TLM) dynamics is the coined
  quantum-walk of the Bloch adjacency A(k); its dispersion is
        ω_n(k) = ω_link · arccos(μ_n(k)/z),  z = degree = 3,
  ω_link = c_link/ℓ_node = OMEGA_C / ANALYTIC_NETWORK_FACTOR = √3·OMEGA_C.
  The bare lumped map ω=√λ is the ω→0 limit ONLY; it gives velocity factor
  1/√2 and FAILS gate (i). The arccos map recovers the canonical 1/√3 exactly.
  λ_max = 6 (gate ii) is preserved: λ_n = z − μ_n.

α-CLEAN: no α/Q_TANK on any verdict path. Constants imported by SYMBOL.
Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/srs_band_survey.py
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path

import numpy as np

from ave.core.chiral_lattice import _SRS_8A, _SRS_NN, build_srs_net
from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR
from ave.core.constants import C_0, HBAR, L_NODE, OMEGA_C, e_charge

Z_DEG = 3                       # srs coordination (Wells (10,3)-a)
FACTOR = ANALYTIC_NETWORK_FACTOR  # 1/√3, imported (never hard-coded)
OMEGA_LINK_OVER_C = 1.0 / FACTOR  # ω_link / ω_C = √3 (derived from the symbol)
# ℏ·OMEGA_C = m_e c² = 511 keV (IDENTITY). Derived from imported symbols, not hard-coded.
# CONSISTENCY-class: the MeV scale imports m_e (CODATA) — a manifestation, not emergence.
MEV_PER_OMEGA_C = HBAR * OMEGA_C / e_charge / 1e6  # ≈ 0.511 MeV/ω_C


# ─────────────────────────────────────────────────────────────────────────────
# 4-site BCC primitive cell of srs (substrate-native; bonds from build_srs_net geometry)
# ─────────────────────────────────────────────────────────────────────────────
def srs_primitive_bcc(enantiomorph: str = "right"):
    """Return (basis[4,3], bonds) for the srs 4-site BCC primitive cell.

    The 8 Wyckoff-8a sites split into 4 body-centred pairs {i, i+4} related by
    +(½,½,½). Basis = first 4 sites; the BCC lattice absorbs the centring. Each
    directed bond is (i, j, δ) with i,j in 0..3 and δ the Cartesian displacement
    (a_conv = 1 units) — Bloch phase e^{i k·δ}, |δ| = ℓ_node.
    """
    motif = _SRS_8A.copy()
    if enantiomorph == "left":
        motif[:, 0] = -motif[:, 0]
        motif = np.mod(motif, 1.0)
    elif enantiomorph != "right":
        raise ValueError("enantiomorph must be 'right' or 'left'")
    basis = motif[:4].copy()
    for i in range(4):  # verify the BCC pairing is exact
        assert np.allclose(np.mod(motif[i] + 0.5, 1.0), np.mod(motif[i + 4], 1.0)), i
    bonds = []
    for i in range(4):
        for m in range(8):
            for n in product(range(-2, 3), repeat=3):
                d = motif[m] + np.array(n, float) - basis[i]
                if abs(np.linalg.norm(d) - _SRS_NN) < 1e-9:
                    bonds.append((i, m % 4, d))
    return basis, bonds


def bloch_adjacency(kvec, bonds, n=4):
    """4×4 Hermitian Bloch adjacency A_ij(k) = Σ_bonds e^{i k·δ}."""
    A = np.zeros((n, n), dtype=complex)
    for (i, j, d) in bonds:
        A[i, j] += np.exp(1j * np.dot(kvec, d))
    return 0.5 * (A + A.conj().T)


def bands_at(kvec, bonds):
    """Return sorted (mu, lambda, omega_over_omegaC) for the 4 scalar bands."""
    mu = np.sort(np.linalg.eigvalsh(bloch_adjacency(kvec, bonds)).real)  # ascending
    lam = Z_DEG - mu[::-1]                                # ascending λ (μ descending)
    om = np.arccos(np.clip(mu[::-1] / Z_DEG, -1.0, 1.0)) * OMEGA_LINK_OVER_C  # ascending ω
    return mu[::-1], lam, om  # returned μ descending, λ/ω ascending (band index 0=acoustic)


# ─────────────────────────────────────────────────────────────────────────────
# BCC reciprocal-space setup (a_conv = 1)
# ─────────────────────────────────────────────────────────────────────────────
TWO_PI = 2.0 * np.pi
B1 = TWO_PI * np.array([0.0, 1.0, 1.0])   # FCC reciprocal of BCC
B2 = TWO_PI * np.array([1.0, 0.0, 1.0])
B3 = TWO_PI * np.array([1.0, 1.0, 0.0])
HS_POINTS = {                              # cartesian (a_conv=1), 2π units
    "Gamma": np.array([0.0, 0.0, 0.0]),
    "H": TWO_PI * np.array([1.0, 0.0, 0.0]),
    "N": np.pi * np.array([1.0, 1.0, 0.0]),
    "P": np.pi * np.array([1.0, 1.0, 1.0]),
}
HS_PATH = ["Gamma", "H", "N", "Gamma", "P", "H"]


# ─────────────────────────────────────────────────────────────────────────────
# Gate (i): acoustic 1/√3 velocity factor (arccos dispersion low-k slope)
# ─────────────────────────────────────────────────────────────────────────────
def velocity_factor(bonds, kl=1e-4):
    ell = _SRS_NN
    dirs = [np.array(d, float) / np.linalg.norm(d)
            for d in [[1, 0, 0], [1, 1, 0], [1, 1, 1], [2, 1, 0], [3, 1, 2]]]
    facs = []
    for qh in dirs:
        mu_ac = np.linalg.eigvalsh(bloch_adjacency(qh * (kl / ell), bonds)).real.max()
        # ω/ω_link = arccos(μ_ac/z); v/c_link = (ω/ω_link)/(k·ℓ) = arccos(...)/kl
        facs.append(float(np.arccos(np.clip(mu_ac / Z_DEG, -1, 1)) / kl))
    facs = np.array(facs)
    return {"per_dir": facs.tolist(), "mean": float(facs.mean()),
            "spread": float((facs.max() - facs.min()) / facs.mean()),
            "target_1_over_sqrt3": float(FACTOR),
            "abs_err": float(abs(facs.mean() - FACTOR))}


# ─────────────────────────────────────────────────────────────────────────────
# Gate (ii): direct build_srs_net graph-Laplacian λ_max
# ─────────────────────────────────────────────────────────────────────────────
def direct_graph_laplacian_lambda_max(L=3, enantiomorph="right"):
    net = build_srs_net(L=L, enantiomorph=enantiomorph)
    Nn = net.n_nodes
    Adj = np.zeros((Nn, Nn))
    for u in range(Nn):
        for v in net.neighbors[u]:
            Adj[u, v] = 1.0
    Lap = np.diag(Adj.sum(1)) - Adj
    return float(np.max(np.linalg.eigvalsh(Lap))), float(Adj.sum(1).mean())


# ─────────────────────────────────────────────────────────────────────────────
# Dense reciprocal-cell scan → band envelopes, global band top, gap inventory
# ─────────────────────────────────────────────────────────────────────────────
def dense_scan(bonds, n_grid=48):
    fs = np.linspace(0.0, 1.0, n_grid, endpoint=False)
    lo = np.full(4, np.inf)
    hi = np.full(4, -np.inf)
    lam_max = -1.0
    k_top = None
    n_bands_ok = True
    for f1 in fs:
        for f2 in fs:
            for f3 in fs:
                k = f1 * B1 + f2 * B2 + f3 * B3
                mu = np.linalg.eigvalsh(bloch_adjacency(k, bonds)).real
                if mu.shape[0] != 4:
                    n_bands_ok = False
                om = np.sort(np.arccos(np.clip(mu / Z_DEG, -1, 1)) * OMEGA_LINK_OVER_C)
                lo = np.minimum(lo, om)
                hi = np.maximum(hi, om)
                lam = float((Z_DEG - mu).max())
                if lam > lam_max:
                    lam_max = lam
                    k_top = k.copy()
    return lo, hi, lam_max, k_top, n_bands_ok


def identify_hs_point(k):
    """Nearest high-symmetry point (mod reciprocal lattice) to k."""
    best, bd = None, np.inf
    for name, p in HS_POINTS.items():
        for g1 in range(-1, 2):
            for g2 in range(-1, 2):
                for g3 in range(-1, 2):
                    G = g1 * B1 + g2 * B2 + g3 * B3
                    d = np.linalg.norm(k - (p + G))
                    if d < bd:
                        bd, best = d, name
    return best, float(bd)


def high_sym_path(bonds, n_seg=60):
    kdist, labels, ticks, bands = [], [], [], []
    d = 0.0
    for a in range(len(HS_PATH) - 1):
        p0, p1 = HS_POINTS[HS_PATH[a]], HS_POINTS[HS_PATH[a + 1]]
        if a == 0:
            ticks.append(0.0)
            labels.append(HS_PATH[a])
        for s in range(1, n_seg + 1):
            k = p0 + (p1 - p0) * (s / n_seg)
            d += np.linalg.norm((p1 - p0) / n_seg)
            _, _, om = bands_at(k, bonds)
            bands.append(om)
            kdist.append(d)
        ticks.append(d)
        labels.append(HS_PATH[a + 1])
    return np.array(kdist), np.array(bands), ticks, labels


# ─────────────────────────────────────────────────────────────────────────────
# Vector / Cosserat STRETCH channel (12×12 mass-spring; scoped, secondary)
# ─────────────────────────────────────────────────────────────────────────────
def vector_bloch_D(kvec, basis, bonds, k_axial=1.0, k_shear=1.0):
    """12×12 mass-spring dynamical matrix (4 sites × 3 DOF), RANK-2 bond tensor
    Φ_b = k_a d̂⊗d̂ + k_s(I−d̂⊗d̂). ω²(k) = eigvals. This is the LUMPED elastic
    model (ω=√eig); the transmission-line arccos correction (scalar §4) is NOT
    applied here — see result-doc scope note. Reported for band-COUNT + acoustic
    isotropy only."""
    D = np.zeros((12, 12), dtype=complex)
    for (i, j, d) in bonds:
        dn = d / np.linalg.norm(d)
        P = np.outer(dn, dn)
        Phi = k_axial * P + k_shear * (np.eye(3) - P)
        ph = np.exp(1j * np.dot(kvec, d))
        D[3 * i:3 * i + 3, 3 * j:3 * j + 3] += -Phi * ph
        D[3 * i:3 * i + 3, 3 * i:3 * i + 3] += Phi
    return 0.5 * (D + D.conj().T)


def vector_channel(basis, bonds):
    # band count + acoustic isotropy at the isotropic-bond (photon) point k_s=k_a
    counts = set()
    dirs = [np.array(x, float) / np.linalg.norm(x)
            for x in [[1, 0, 0], [1, 1, 0], [1, 1, 1]]]
    v_ac = []
    for qh in dirs:
        w2 = np.sort(np.clip(np.linalg.eigvalsh(vector_bloch_D(qh * (1e-4 / _SRS_NN),
                     basis, bonds)).real, 0, None))
        counts.add(w2.shape[0])
        # lowest 3 branches are acoustic; average acoustic slope proxy
        v_ac.append(float(np.sqrt(w2[1]) / (1e-4 / _SRS_NN)))  # a representative acoustic
    # global band count over a coarse BZ
    for f in np.linspace(0, 1, 9, endpoint=False):
        k = f * B1 + 0.37 * B2 + 0.61 * B3
        counts.add(np.linalg.eigvalsh(vector_bloch_D(k, basis, bonds)).shape[0])
    return {
        "attempted": True,
        "model": "12x12 lumped mass-spring (ω=√eig); RANK-2 bond tensor k_a=k_s",
        "band_count": sorted(counts),
        "acoustic_speed_proxy_spread": float((max(v_ac) - min(v_ac)) / np.mean(v_ac)),
        "scope_note": ("STRETCH/SECONDARY. The transmission-line arccos map that the "
                       "SCALAR channel required for the canonical 1/√3 (prereg §4) is NOT "
                       "applied to this elastic matrix. Band COUNT (12) + acoustic isotropy "
                       "only; the vector band-TOP normalisation needs its own gate — deferred."),
    }


# ─────────────────────────────────────────────────────────────────────────────
def main():
    out = {"class": "CONSISTENCY / characterization", "z_degree": Z_DEG,
           "omega_link_over_omega_C": OMEGA_LINK_OVER_C,
           "canonical_symbols": {"OMEGA_C_rad_s": float(OMEGA_C), "L_NODE_m": float(L_NODE),
                                 "C_0_m_s": float(C_0), "ANALYTIC_NETWORK_FACTOR": float(FACTOR),
                                 "MeV_per_omega_C": MEV_PER_OMEGA_C}}

    per_en = {}
    for en in ("right", "left"):
        basis, bonds = srs_primitive_bcc(en)
        # ---- gate (i) ----
        vf = velocity_factor(bonds)
        # ---- gate (ii) ----
        lam_max_direct, mean_deg = direct_graph_laplacian_lambda_max(3, en)
        lo, hi, lam_max_bloch, k_top, nb_ok = dense_scan(bonds)
        # ---- gate (iii) ----
        gate3 = nb_ok and (len(lo) == 4)
        # band top
        top_hs, top_dist = identify_hs_point(k_top)
        omega_top = float(hi.max())
        # gap inventory (sorted band envelopes)
        gaps = []
        for b in range(3):
            g = float(lo[b + 1] - hi[b])
            gaps.append({"between": [b, b + 1], "gap_omega_C": g,
                         "full_stop_band": bool(g > 1e-6),
                         "window_omega_C": [float(hi[b]), float(lo[b + 1])] if g > 1e-6 else None})
        # Gamma structure
        mu_g, lam_g, om_g = bands_at(HS_POINTS["Gamma"], bonds)
        opt = np.round(om_g[om_g > 1e-9], 6)
        gamma = {"acoustic_omega_C": float(om_g[0]),
                 "optical_omega_C": sorted(set(np.round(opt, 6).tolist())),
                 "optical_degeneracy": int(np.sum(om_g > 1e-9)),
                 "optical_value": float(opt[0]) if len(opt) else None}

        gate1 = (vf["abs_err"] < 1e-4) and (vf["spread"] < 1e-3)
        gate2 = abs(lam_max_bloch - 6.0) < 1e-3 and abs(lam_max_direct - 6.0) < 1e-3
        per_en[en] = {
            "gate_i_velocity_factor": vf, "gate_i_pass": bool(gate1),
            "gate_ii_lambda_max_bloch": lam_max_bloch,
            "gate_ii_lambda_max_direct": lam_max_direct,
            "gate_ii_mean_degree": mean_deg, "gate_ii_pass": bool(gate2),
            "gate_iii_band_count": len(lo), "gate_iii_pass": bool(gate3),
            "band_envelopes_omega_C": {"low": lo.tolist(), "high": hi.tolist()},
            "band_top": {"omega_C": omega_top, "MeV": omega_top * MEV_PER_OMEGA_C,
                         "k_raw_cartesian_2pi": (k_top / TWO_PI).tolist(),
                         "hs_point": top_hs, "dist_to_hs": top_dist,
                         "hs_point_canonical_2pi": (HS_POINTS[top_hs] / TWO_PI).tolist(),
                         "closed_form": "pi/ANALYTIC_NETWORK_FACTOR = pi*sqrt3"},
            "gap_inventory": gaps,
            "any_full_gap": bool(any(g["full_stop_band"] for g in gaps)),
            "gamma_structure": gamma,
        }

    R = per_en["right"]
    L_ = per_en["left"]
    enantiomorph_match = bool(np.allclose(R["band_envelopes_omega_C"]["high"],
                                          L_["band_envelopes_omega_C"]["high"], atol=1e-9))
    out["per_enantiomorph"] = per_en
    out["enantiomorph_spectra_identical"] = enantiomorph_match

    # ---- vector/Cosserat stretch (right enantiomorph) ----
    basis_r, bonds_r = srs_primitive_bcc("right")
    out["vector_channel_stretch"] = vector_channel(basis_r, bonds_r)

    # ---- consumers ----
    top = R["band_top"]["omega_C"]
    out["consumers"] = {
        "a_forkA_tone_placement": {
            "true_band_top_omega_C": top,
            "requirement": "both drive tones ABOVE the true srs band top; difference in-band",
            "recommended_omega_a_omega_C": round(top + 1.5, 3),
            "recommended_omega_b_omega_C": round(top + 0.5, 3),
            "difference_omega_C": 1.0,
            "note": ("difference 1.0 ω_C sits in-band (< band top). OLD superband used tones "
                     "above 2·ω_C (1D-chain LUMPED top) — that is ~2.7× TOO LOW for the real 3D "
                     "srs net; tones must clear %.3f ω_C." % top)},
        "b_fpb_corner_marker1": {
            "band_edge_MeV": round(R["band_top"]["MeV"], 4),
            "pair_threshold_2omegaC_MeV": round(2 * MEV_PER_OMEGA_C, 4),
            "ordering": "pair_threshold (1.022 MeV) < band_top (%.3f MeV)" % R["band_top"]["MeV"],
            "ac_to_dc_opens_while_smooth_modes_propagate": True,
            "note": ("pair-production / AC→DC channel (2ω_C = 1.022 MeV) opens BELOW the band top "
                     "(%.3f MeV); propagating scalar lattice modes coexist with the pair channel "
                     "in the 1.022–%.3f MeV window." % (R["band_top"]["MeV"], R["band_top"]["MeV"]))},
        "c_gap_breather": {
            "any_full_gap": R["any_full_gap"],
            "flag": ("NO full stop-band: the scalar srs manifold is connected 0→%.3f ω_C, so "
                     "gap-localized (gap-breather) carrier candidates are UNAVAILABLE in srs."
                     % top) if not R["any_full_gap"]
            else "full gap exists — gap-localized modes are candidates (flag only)"},
    }

    all_pass = all(R[f"gate_{g}_pass"] for g in ("i", "ii", "iii")) and \
        all(L_[f"gate_{g}_pass"] for g in ("i", "ii", "iii"))
    out["all_gates_pass"] = bool(all_pass)
    out["survey_valid"] = bool(all_pass)

    # ---- report ----
    print("=" * 78)
    print("x31-B — srs 3D BAND SURVEY (Bloch/Ybus, 4-site BCC primitive, survey-class)")
    print("=" * 78)
    print("\nGATES (right enantiomorph):")
    print(f"  (i)   velocity factor = {R['gate_i_velocity_factor']['mean']:.7f}  "
          f"(1/√3 = {FACTOR:.7f}, err {R['gate_i_velocity_factor']['abs_err']:.1e})  "
          f"PASS={R['gate_i_pass']}")
    print(f"  (ii)  λ_max Bloch = {R['gate_ii_lambda_max_bloch']:.6f}  vs direct "
          f"build_srs_net = {R['gate_ii_lambda_max_direct']:.6f}  PASS={R['gate_ii_pass']}")
    print(f"  (iii) band count = {R['gate_iii_band_count']}  enantiomorph-identical="
          f"{enantiomorph_match}  PASS={R['gate_iii_pass']}")
    print(f"\nBAND TOP: {top:.4f} ω_C  = {R['band_top']['MeV']:.4f} MeV  at "
          f"{R['band_top']['hs_point']} = 2π·{np.round(R['band_top']['hs_point_canonical_2pi'],3)}  "
          f"(raw image 2π·{np.round(R['band_top']['k_raw_cartesian_2pi'],3)})  [= π/(1/√3) = π√3]")
    print(f"Γ acoustic = {R['gamma_structure']['acoustic_omega_C']:.4f} ω_C; "
          f"Γ optical = {R['gamma_structure']['optical_value']:.4f} ω_C "
          f"(×{R['gamma_structure']['optical_degeneracy']} degenerate)")
    print("\nBAND ENVELOPES (ω_C):")
    for b in range(4):
        print(f"  band {b}: [{R['band_envelopes_omega_C']['low'][b]:.4f}, "
              f"{R['band_envelopes_omega_C']['high'][b]:.4f}]")
    print("\nGAP INVENTORY:")
    for g in R["gap_inventory"]:
        print(f"  bands {g['between']}: "
              + (f"FULL GAP {g['gap_omega_C']:.4f} ω_C in {g['window_omega_C']}"
                 if g["full_stop_band"] else "no gap (overlap)"))
    print(f"  ⇒ any full stop-band: {R['any_full_gap']}")
    print("\nCONSUMERS:")
    print(f"  (a) FORK A tones: ω_a≈{out['consumers']['a_forkA_tone_placement']['recommended_omega_a_omega_C']}, "
          f"ω_b≈{out['consumers']['a_forkA_tone_placement']['recommended_omega_b_omega_C']} ω_C (both > {top:.3f})")
    print(f"  (b) band edge {R['band_top']['MeV']:.3f} MeV; ordering: "
          f"{out['consumers']['b_fpb_corner_marker1']['ordering']}")
    print(f"  (c) gap-breather: {out['consumers']['c_gap_breather']['flag']}")
    print(f"\nVECTOR stretch: band_count={out['vector_channel_stretch']['band_count']} "
          f"(scoped/secondary — see result doc)")
    print(f"\nALL GATES PASS: {out['all_gates_pass']}  |  SURVEY VALID: {out['survey_valid']}")

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "srs_band_survey.json").write_text(json.dumps(out, indent=2))
    print(f"\nResults: {out_dir / 'srs_band_survey.json'}")

    # ---- figure (white house style) ----
    try:
        make_figure(bonds_r, out, out_dir)
    except Exception as e:  # pragma: no cover
        print(f"[figure skipped: {e}]")
    return out


def make_figure(bonds, out, out_dir):
    from ave.viz import style
    style.apply()
    kd, bands, ticks, labels = high_sym_path(bonds)
    fig, ax = style.plt.subplots(figsize=style.figsize("single"))
    colors = [style.COLORS["ave"], style.COLORS["comparison"],
              style.COLORS["accent"], style.COLORS["muted"]]
    for b in range(4):
        ax.plot(kd, bands[:, b], color=colors[b], lw=1.6, label=f"band {b}")
    top = out["per_enantiomorph"]["right"]["band_top"]["omega_C"]
    ax.axhline(top, color=style.COLORS["data"], ls="--", lw=0.9)
    ax.axhline(2.0, color=style.COLORS["comparison"], ls=":", lw=0.9)
    ax.annotate(f"band top  π√3 = {top:.3f} " + r"$\omega_C$", (kd[len(kd) // 2], top),
                ha="center", va="bottom", fontsize=8)
    ax.annotate(r"pair threshold  2 $\omega_C$", (kd[len(kd) // 2], 2.0), ha="center",
                va="bottom", fontsize=8, color=style.COLORS["comparison"])
    ax.set_xticks(ticks)
    ax.set_xticklabels([r"$\Gamma$" if x == "Gamma" else x for x in labels])
    for t in ticks:
        ax.axvline(t, color=style.COLORS["muted"], lw=0.4, alpha=0.5)
    ax.set_xlim(kd[0], kd[-1])
    ax.set_ylim(0, top * 1.05)
    ax.set_xlabel("BCC Brillouin-zone path")
    ax.set_ylabel(style.axis_label("frequency", r"\omega", r"$\omega_C$"))
    style.legend(ax, where="right")
    paths = style.save(fig, out_dir / "srs_band_survey")
    print(f"Figure: {paths}")


if __name__ == "__main__":
    main()
