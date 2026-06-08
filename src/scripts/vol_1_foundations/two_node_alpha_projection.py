#!/usr/bin/env python3
r"""Two-node projection test for an alpha-scale screened residue.

SCOPE NOTE (2026-06-07 two-node alpha projection first pass):
This script tests a narrow alpha-free geometric hypothesis:

    A single K4 node sees only a partial scalar projection of the electron's
    precessing (2,3) phase-space flux-tube profile; a canonical adjacent A/B
    two-node baseline is the minimal projector that can expose the screened
    covariance residue of the full 2D profile.

It does NOT simulate the K4-TLM engine and does NOT derive the electron profile
from dynamics. The (2,3) phase-space profile and Golden-Torus dimensions are
canonical inputs from the existing Class-B alpha leaf. The only question asked
here is whether the "two nodes are required to project the full profile" idea
produces an alpha-scale RMS or variance residue without importing alpha.

Alpha is imported for COMPARISON ONLY in the final adjudication.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:  # pragma: no cover - plotting is optional
    plt = None

import ave.core.constants as _avc
from ave.core.constants import ALPHA_COLD, ALPHA_COLD_INV


PROJECT_ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = PROJECT_ROOT / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PHI = (1.0 + math.sqrt(5.0)) / 2.0
P_WINDING = 2
Q_WINDING = 3
R_PHASE = PHI / 2.0
R_MINOR = (PHI - 1.0) / 2.0


def verify_canonical_sources() -> None:
    """Guard that comparison constants come from AVE-Core's canonical module."""

    constants_path = Path(_avc.__file__).as_posix()
    if not constants_path.endswith("src/ave/core/constants.py"):
        raise RuntimeError(f"ave.core.constants loaded from unexpected path: {constants_path}")
    if not (100.0 < ALPHA_COLD_INV < 200.0 and 0.0 < ALPHA_COLD < 0.01):
        raise RuntimeError("canonical alpha comparison constants outside expected range")


def phase_space_profile(theta: np.ndarray) -> np.ndarray:
    """Canonical alpha-free (2,3) phase-space profile.

    The profile is a 2D Lissajous shadow of the Clifford-torus winding in
    (V_inc, V_ref). R and r are the Golden-Torus semi-scales from the corpus;
    alpha is not used to define them.
    """

    v_inc = R_PHASE * np.cos(P_WINDING * theta) + R_MINOR * np.cos(Q_WINDING * theta)
    v_ref = R_PHASE * np.sin(P_WINDING * theta) - R_MINOR * np.sin(Q_WINDING * theta)
    return np.column_stack([v_inc, v_ref])


def unit(angle: float) -> np.ndarray:
    return np.array([math.cos(angle), math.sin(angle)], dtype=float)


def project(profile: np.ndarray, axes: list[np.ndarray]) -> np.ndarray:
    return np.column_stack([profile @ axis for axis in axes])


def covariance_metrics(samples: np.ndarray) -> dict[str, float | list[float]]:
    centered = samples - samples.mean(axis=0, keepdims=True)
    cov = np.cov(centered, rowvar=False)
    cov = np.atleast_2d(cov)
    eigvals = np.linalg.eigvalsh(cov)
    eigvals = np.maximum(eigvals, 0.0)
    positive = eigvals[eigvals > 1e-12]
    positive_total = float(np.sum(positive))
    rank = int(len(positive))
    if positive_total == 0.0:
        screened_variance = 0.0
        rms_fraction = 0.0
    elif rank < 2:
        # A rank-1 scalar sample has no transverse residual; it is partial, not complete.
        screened_variance = 0.0
        rms_fraction = 0.0
    else:
        # For N>2 projection channels, the sample covariance has N-2 null
        # directions from redundant readout columns. Those nulls are not a
        # screened physical residue, so score the positive spectrum only.
        screened_variance = float(positive[0] / positive_total)
        rms_fraction = float(math.sqrt(screened_variance))

    condition_ratio = float(positive[-1] / positive[0]) if rank >= 2 and positive[0] > 0 else None

    return {
        "variance_total": float(np.trace(cov)),
        "positive_variance_total": positive_total,
        "rank_positive": rank,
        "complete_projector": bool(rank >= 2),
        "eigenvalues": [float(v) for v in eigvals],
        "positive_eigenvalues": [float(v) for v in positive],
        "screened_variance_fraction": screened_variance,
        "screened_rms_fraction": rms_fraction,
        "condition_ratio_positive": condition_ratio,
    }


def make_projectors() -> dict[str, list[np.ndarray]]:
    """Alpha-free projector set.

    Canonical adjacent A/B is represented as conjugate phase-space quadratures.
    Wrong-pair controls duplicate a quadrature or use non-conjugate angles.
    Three/four-node controls test convergence rather than continued drift.
    """

    return {
        "one_node_x": [unit(0.0)],
        "one_node_y": [unit(math.pi / 2.0)],
        "two_node_adjacent_conjugate_xy": [unit(0.0), unit(math.pi / 2.0)],
        "two_node_wrong_same_axis": [unit(0.0), unit(math.pi)],
        "two_node_wrong_45deg_pair": [unit(0.0), unit(math.pi / 4.0)],
        "three_node_120deg": [unit(0.0), unit(2.0 * math.pi / 3.0), unit(4.0 * math.pi / 3.0)],
        "four_node_quadrature": [unit(0.0), unit(math.pi / 2.0), unit(math.pi), unit(3.0 * math.pi / 2.0)],
    }


def run(n_samples: int = 200_000) -> dict:
    theta = np.linspace(0.0, 2.0 * math.pi, n_samples, endpoint=False)
    profile = phase_space_profile(theta)
    profile_metrics = covariance_metrics(profile)

    projectors = make_projectors()
    projector_results = {}
    for name, axes in projectors.items():
        samples = project(profile, axes)
        projector_results[name] = covariance_metrics(samples)

    alpha = float(ALPHA_COLD)
    sqrt_alpha = float(math.sqrt(alpha))
    for result in projector_results.values():
        result["variance_error_vs_alpha_ratio"] = (
            float(result["screened_variance_fraction"] / alpha) if alpha else math.inf
        )
        result["rms_error_vs_sqrt_alpha_ratio"] = (
            float(result["screened_rms_fraction"] / sqrt_alpha) if sqrt_alpha else math.inf
        )

    return {
        "scope": "alpha-free two-node projection first pass; alpha comparison only",
        "inputs": {
            "p_winding": P_WINDING,
            "q_winding": Q_WINDING,
            "phi": PHI,
            "R_phase": R_PHASE,
            "r_phase": R_MINOR,
            "alpha_used_as_input": False,
            "alpha_cold_comparison": float(ALPHA_COLD),
            "alpha_cold_inv_comparison": float(ALPHA_COLD_INV),
            "sqrt_alpha_comparison": sqrt_alpha,
        },
        "full_profile_metrics": profile_metrics,
        "projectors": projector_results,
    }


def plot_results(results: dict) -> None:
    if plt is None:
        return

    labels = list(results["projectors"].keys())
    variances = [results["projectors"][label]["screened_variance_fraction"] for label in labels]
    rms = [results["projectors"][label]["screened_rms_fraction"] for label in labels]
    alpha = results["inputs"]["alpha_cold_comparison"]
    sqrt_alpha = results["inputs"]["sqrt_alpha_comparison"]

    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(11, 8), sharex=True)
    fig.patch.set_facecolor("#0d1117")
    for ax in (ax0, ax1):
        ax.set_facecolor("#0d1117")
        ax.tick_params(colors="white")
        for spine in ax.spines.values():
            spine.set_color("#8b949e")
        ax.grid(True, alpha=0.25, color="#8b949e")

    x = np.arange(len(labels))
    ax0.bar(x, variances, color="#58a6ff")
    ax0.axhline(alpha, color="#ff7b72", linestyle="--", label="alpha")
    ax0.set_ylabel("screened variance", color="white")
    ax0.legend(facecolor="#161b22", edgecolor="#30363d", labelcolor="white")

    ax1.bar(x, rms, color="#7ee787")
    ax1.axhline(sqrt_alpha, color="#ff7b72", linestyle="--", label="sqrt(alpha)")
    ax1.set_ylabel("screened RMS", color="white")
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, rotation=35, ha="right", color="white")
    ax1.legend(facecolor="#161b22", edgecolor="#30363d", labelcolor="white")

    fig.suptitle("Two-node projection screened residue (alpha-free inputs)", color="white")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "two_node_alpha_projection.png", dpi=180)


def main() -> None:
    verify_canonical_sources()
    results = run()
    output_path = OUT_DIR / "two_node_alpha_projection_results.json"
    output_path.write_text(json.dumps(results, indent=2, allow_nan=False) + "\n")
    plot_results(results)

    print("Two-node alpha projection first pass")
    print("alpha is comparison-only; not used in the profile or projectors")
    print(f"alpha_cold = {results['inputs']['alpha_cold_comparison']:.10f}")
    print(f"sqrt(alpha_cold) = {results['inputs']['sqrt_alpha_comparison']:.10f}")
    for name, metrics in results["projectors"].items():
        print(
            f"{name:32s}  variance={metrics['screened_variance_fraction']:.8f} "
            f"({metrics['variance_error_vs_alpha_ratio']:.2f}x alpha), "
            f"rms={metrics['screened_rms_fraction']:.8f} "
            f"({metrics['rms_error_vs_sqrt_alpha_ratio']:.2f}x sqrt(alpha))"
        )


if __name__ == "__main__":
    main()
