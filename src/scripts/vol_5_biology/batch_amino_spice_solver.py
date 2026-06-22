r"""
Batch Amino Acid SPICE Solver — Topological Resonance Spectra
============================================================
MNA (Modified Nodal Analysis) AC solver for the AVE amino-acid SPICE
netlists. Sweeps each of the 20 standard amino-acid geometries over the
IR band and plots the predicted |H|^2 transmission spectrum.

The .cir netlists are the per-amino-acid L/C transmission-line topologies
(masses -> L via xi_topo, bond stiffnesses -> C via xi_topo); see
spice_organic_mapper for the derivation.

Run: PYTHONPATH=src python src/scripts/vol_5_biology/batch_amino_spice_solver.py

Ported from the Applied-Vacuum-Engineering archive; restyled to the AVE
white manuscript house style (ave.viz.style, Okabe-Ito). The .cir netlist
data is vendored into assets/sim_outputs/spice_models/ from the same archive.
"""

import glob
import os

import matplotlib

import numpy as np

from ave.core.constants import C_0
from ave.viz import style
from ave_path_util import SIM_OUTPUTS, sim_output

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def parse_and_solve_cir(filepath, freqs):
    """MNA AC solve of an AVE .cir netlist; returns |H(f)| at the 'out' node."""
    nodes = {"0": 0}
    components = []
    v_in_node = None
    v_out_node = None

    with open(filepath, "r") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("*") or line.startswith("."):
                continue
            parts = line.split()
            if len(parts) < 4:
                continue

            comp_type = parts[0][0].upper()
            n1, n2 = parts[1], parts[2]
            if n1 not in nodes:
                nodes[n1] = len(nodes)
            if n2 not in nodes:
                nodes[n2] = len(nodes)

            if comp_type in ["R", "L", "C"]:
                val_str = parts[3]
                if val_str.endswith("fF"):
                    val_str = val_str[:-2]
                elif val_str.endswith("pH"):
                    val_str = val_str[:-2]
                elif val_str.endswith("Ohm"):
                    val_str = val_str[:-3]
                try:
                    val = float(val_str)
                    components.append((comp_type, nodes[n1], nodes[n2], val))
                except ValueError as e:
                    print(f"Failed to parse component: {line} -> {e}")
            elif comp_type == "V":
                v_in_node = nodes[n1]

    if "out" in nodes:
        v_out_node = nodes["out"]

    num_nodes = len(nodes)
    unknown_nodes = [i for i in range(num_nodes) if i not in (0, v_in_node)]
    unknown_idx = {n: i for i, n in enumerate(unknown_nodes)}
    N_u = len(unknown_nodes)

    H_mag = []
    for freq in freqs:
        wf = 2 * np.pi * freq
        Y = np.zeros((N_u, N_u), dtype=complex)
        J = np.zeros(N_u, dtype=complex)

        for ctype, n1, n2, val in components:
            if ctype == "R":
                y = 1.0 / val
            elif ctype == "C":
                y = 1j * wf * val
            else:  # L
                y = 1.0 / (1j * wf * val) if wf != 0 else 1e9

            if n1 in unknown_idx:
                i = unknown_idx[n1]
                Y[i, i] += y
                if n2 == v_in_node:
                    J[i] += y * 1.0
            if n2 in unknown_idx:
                j = unknown_idx[n2]
                Y[j, j] += y
                if n1 == v_in_node:
                    J[j] += y * 1.0
            if n1 in unknown_idx and n2 in unknown_idx:
                i, j = unknown_idx[n1], unknown_idx[n2]
                Y[i, j] -= y
                Y[j, i] -= y

        V_u = np.linalg.solve(Y, J)
        if v_out_node in unknown_idx:
            v_out = V_u[unknown_idx[v_out_node]]
        elif v_out_node == 0:
            v_out = 0.0
        elif v_out_node == v_in_node:
            v_out = 1.0
        else:
            v_out = 0.0
        H_mag.append(abs(v_out))

    return np.array(H_mag)


def generate_batch_resonance():
    cir_dir = SIM_OUTPUTS / "spice_models"
    cir_files = glob.glob(str(cir_dir / "*_ave.cir"))

    # 300 cm^-1 to 4000 cm^-1 (convert to Hz: c * cm^-1 * 100)
    wavenumbers = np.linspace(300, 4000, 2000)
    freqs = wavenumbers * C_0 * 100

    style.apply()
    fig, ax = plt.subplots(figsize=style.figsize("wide"))

    peak_data = []
    print(f"Parsing and simulating {len(cir_files)} amino acid geometries...")
    for path in sorted(cir_files):
        name = os.path.basename(path).replace("_ave.cir", "").capitalize()
        H = parse_and_solve_cir(path, freqs)
        H_db = 10 * np.log10(np.clip(H**2, 1e-30, None))

        dominant_idx = np.argmin(H_db)
        peak_data.append((name, wavenumbers[dominant_idx], H_db[dominant_idx]))
        ax.plot(wavenumbers, H_db, label=name, lw=1.3, alpha=0.85)

    print("\n=======================================================")
    print("  Dominant Topological Resonance (Primary Absorption Notch)")
    print("=======================================================")
    print(f"{'Amino Acid':<15} | {'Notch (cm^-1)':<16} | {'Transmission Depth (dB)'}")
    print("-" * 55)
    for name, wn, db in sorted(peak_data, key=lambda x: x[1] if not np.isnan(x[1]) else 0):
        print(f"{name:<15} | {wn:>10.1f} cm^-1     | {db:>8.1f} dB")

    ax.set_xlabel(style.axis_label("Wavenumber", r"\tilde{\nu}", r"cm$^{-1}$"))
    ax.set_ylabel(style.axis_label("Power transfer", r"|H|^2", "dB"))
    ax.set_ylim(-100, 40)
    ax.set_xlim(300, 4000)

    # Neutral IR-band region guides.
    ax.axvspan(600, 1600, alpha=0.05, color=style.COLORS["muted"])
    ax.text(1100, 35, "Fingerprint region", fontsize=9,
            color=style.COLORS["muted"], ha="center")
    ax.axvspan(2500, 3800, alpha=0.05, color=style.COLORS["ave"])
    ax.text(3150, 35, "Stretch region", fontsize=9,
            color=style.COLORS["ave"], ha="center")

    style.legend(ax, where="right", ncol=2, fontsize=7)

    out_path = sim_output("amino_acid_batch_resonance.png")
    style.save(fig, out_path, formats=("png",))
    plt.close(fig)
    print(f"\nBatch sweep complete. Plot saved to: {out_path}")


if __name__ == "__main__":
    generate_batch_resonance()
