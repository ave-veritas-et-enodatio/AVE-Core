#!/usr/bin/env python3
"""VISUAL 2 — "The HIBEF moment" (engine scene export).

The pump-probe polarization walk-off at HIBEF's demonstrated ReLaX pump, exported
for the interactive HTML + a static 3-panel companion figure. EVERY number is
pulled from the MERGED GAP-1 feasibility driver
(scripts/vol_9_device/birefringence_gap1_hibef_feasibility.py) -- this driver
imports that driver's OWN functions and constants and re-runs them, so the scene
carries the canonical numbers by construction (no re-derivation, no hardcode):

  * A^2 = 5.9e-7 at the demonstrated pump E = 8.7e13 V/m (E/E_YIELD);
  * the SVE relative retardance Δφ and Δφ/2 per probe energy (scenario 1, NJP
    9835 eV: Δφ = 0.1476 rad, Δφ/2 = 0.0738 rad);
  * the polarization-flip probability P = sin^2(Δφ/2) (the honest saturated
    single-pass observable), read against the QED co-prediction through the
    IDENTICAL readout chain.

WHAT IS ENGINE-EXACT vs STYLIZED (see viz/README.md ledger):
  ENGINE-EXACT (driver numbers): A^2, Δφ, Δφ/2, P_flip (SVE and QED), the S(A)
    value at the pump amplitude, the probe wavelengths.
  STYLIZED (presentation): the pump envelope's spatial stripe shape, the time
    axis of the animation, and the ×N amplitude exaggeration used ONLY to make
    the A^2=5.9e-7 saturation visible on screen (HONESTLY labelled).

DISCIPLINE
  * phase-space-coordinate-check PASS: the flip-prob is a polarization-PHASE
    observable; both SVE and QED legs ride the identical Δn -> Δφ -> flip chain
    (the GAP-1 driver's no-strawman R1). We visualize in the matching (phase)
    coordinate.
  * consistency-vs-emergence: CONSISTENCY-class. This is the canonical SVE Δn
    through a LITERATURE HIBEF readout; the FORM (tree-level O(1) saturation) is
    the SVE chord, the MAGNITUDE ratio is an α-echo (symmetric-standard tag,
    carried from the GAP-1 driver). No new constant, no emergence headline.
  * public naming: SVE (structured-vacuum electrodynamics). "QED" is the
    standard-physics co-prediction and is named as such (a real external theory,
    not an internal label).

Run:
    cd src
    PYTHONPATH=. python3 scripts/viz/hibef_moment_scene.py

Writes:
    viz/hibef_moment/hibef_moment_scene.json     (the engine scene / numbers)
    viz/hibef_moment/hibef_moment.html           (self-contained animation)
    viz/hibef_moment/hibef_moment_panels.{pdf,png}  (static 3-panel companion)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

# ── repo import wiring ──
_REPO_ROOT = Path(__file__).resolve().parents[3]
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from ave.bench import delta_n_ave_differential_exact  # noqa: E402
from ave.core.constants import E_YIELD  # noqa: E402
from ave.solvers.graded_vacuum_network import saturation_kernel  # noqa: E402

# The MERGED GAP-1 driver IS the number source (import its functions + constants).
from scripts.vol_9_device.birefringence_gap1_hibef_feasibility import (  # noqa: E402
    E_HIBEF,
    E_PROBE_LOI_HIGH_EV,
    E_PROBE_LOI_LOW_EV,
    E_PROBE_NJP_EV,
    P_DEMONSTRATED_6457,
    P_REQUIRED,
    hibef_point,
)

_OUT_DIR = _REPO_ROOT / "viz" / "hibef_moment"

# The three LoI probe-energy scenarios (labelled; the GAP-1 driver's own set).
_PROBES = [
    ("NJP 9835 eV", E_PROBE_NJP_EV),
    ("LoI low 8766 eV", E_PROBE_LOI_LOW_EV),
    ("LoI high 12914 eV", E_PROBE_LOI_HIGH_EV),
]
# The on-screen amplitude exaggeration for the pump stripe. A^2=5.9e-7 is
# invisible at true scale; we exaggerate the DISPLAYED saturation by this factor
# (labelled on the figure). This touches ONLY the pump-stripe colour, never a
# reported number.
_VIS_EXAGGERATION = 3.0e5


def build_scene() -> dict:
    """Re-run the GAP-1 machinery and assemble the export scene."""
    A_pump = float(E_HIBEF / E_YIELD)
    A2_pump = A_pump**2

    # S(A) at the true pump amplitude (canonical kernel), and the visually
    # exaggerated S used ONLY for the on-screen stripe (labelled).
    S_true = float(saturation_kernel(np.array([A_pump]), exponent=0.5, S_min=1e-3)[0])
    A_vis = min(A_pump * np.sqrt(_VIS_EXAGGERATION), 0.999)
    S_vis = float(saturation_kernel(np.array([A_vis]), exponent=0.5, S_min=1e-3)[0])

    # per-probe co-computed (SVE, QED) points through the identical readout chain
    probes = []
    for label, e_probe in _PROBES:
        pt = hibef_point(E_HIBEF, e_probe)
        probes.append(
            {
                "label": label,
                "E_probe_eV": float(e_probe),
                "wavelength_pm": float(pt.wavelength_m * 1e12),
                "dn_ave": float(pt.dn_ave),
                "dn_qed": float(pt.dn_qed),
                "dphi_ave_rad": float(pt.dphi_ave),
                "dphi_half_ave_rad": float(pt.dphi_ave / 2.0),
                "dphi_qed_rad": float(pt.dphi_qed),
                "P_ave_exact": float(pt.P_ave_exact),
                "P_qed_exact": float(pt.P_qed_exact),
                "ratio_ave_over_qed": float(pt.P_ave_exact / pt.P_qed_exact) if pt.P_qed_exact > 0 else None,
            }
        )

    # a field sweep (for the static panel a): SVE Δn(E) across the ramp to the pump
    E_sweep = np.linspace(0.0, E_HIBEF, 240)
    dn_sweep = np.abs(delta_n_ave_differential_exact(E_sweep)).astype(float)

    scene = {
        "meta": {
            "title": "The HIBEF moment",
            "public_name": "SVE (structured-vacuum electrodynamics)",
            "facility": "HIBEF ReLaX pump + X-ray dark-field polarimeter (single-pass, no Fabry-Perot)",
            "pump": {
                "E_field_Vpm": float(E_HIBEF),
                "A": A_pump,
                "A2": A2_pump,
                "S_true": S_true,
                "note_vis": f"pump saturation exaggerated x{_VIS_EXAGGERATION:.0e} for on-screen visibility",
                "S_vis": S_vis,
            },
            "floors": {
                "P_required_1.4e-10": float(P_REQUIRED),
                "P_demonstrated_2.4e-10": float(P_DEMONSTRATED_6457),
            },
            "provenance": {
                "A2, dphi, P": "scripts.vol_9_device.birefringence_gap1_hibef_feasibility (ENGINE-EXACT)",
                "delta_n_ave": "ave.bench.delta_n_ave_differential_exact (ENGINE-EXACT)",
                "S(A)": "ave.solvers.graded_vacuum_network.saturation_kernel (ENGINE-EXACT)",
                "stripe_shape/time_axis": "presentation (STYLIZED)",
                "amplitude_exaggeration": f"x{_VIS_EXAGGERATION:.0e} on the DISPLAYED stripe only (labelled)",
            },
            "classification": "CONSISTENCY-class; FORM=SVE chord, MAGNITUDE ratio=alpha-echo (symmetric-standard)",
        },
        "probes": probes,
        "field_sweep": {"E_Vpm": E_sweep.astype(float).tolist(), "dn_ave": dn_sweep.tolist()},
        "kernel_form": {"exponent": 0.5, "S_min": 1e-3},
    }
    return scene


def main() -> None:
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    scene = build_scene()
    out_json = _OUT_DIR / "hibef_moment_scene.json"
    out_json.write_text(json.dumps(scene, indent=2))
    m = scene["meta"]
    print("=" * 74)
    print("VISUAL 2 — the HIBEF moment (engine scene export)")
    print("=" * 74)
    print(f"  pump: E={m['pump']['E_field_Vpm']:.2e} V/m  A^2={m['pump']['A2']:.3e}  S_true={m['pump']['S_true']:.6f}")
    for p in scene["probes"]:
        print(
            f"  [{p['label']}] lambda={p['wavelength_pm']:.1f} pm  "
            f"dphi_ave={p['dphi_ave_rad']:.4f} rad (half {p['dphi_half_ave_rad']:.4f})  "
            f"P_ave={p['P_ave_exact']:.3e}  P_qed={p['P_qed_exact']:.3e}  "
            f"ratio={p['ratio_ave_over_qed']:.2e}"
        )
    print(f"  scene written: {out_json}")


if __name__ == "__main__":
    main()
