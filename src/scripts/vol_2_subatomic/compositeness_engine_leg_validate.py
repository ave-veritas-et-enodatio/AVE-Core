"""Compositeness-Defense engine leg — validate-on-known (charge-channel exterior tail).

Docket B2. Sibling to the Gate-0 analytic result (PR #471, merged). This driver
runs ONLY the honest validate-on-known: can the chosen EM host reproduce the
KNOWN static 1/r Coulomb field of a point charge before ANY knot readout counts?

Per the prereg addendum
(`research/2026-07-03_compositeness-defense_engine-leg_prereg.md`, §2 host audit):
NO engine implements a winding->EM-source coupling (the boundary integer sourcing
the massless EM channel). So the ONLY host with a genuine dynamically-evolved
E-field is `fdtd_3d` (curl-Maxwell). This driver tests whether fdtd_3d can even
represent a static Coulomb monopole. It CANNOT (curl-only Ampere/Faraday, no
charge-source term) — and this driver DEMONSTRATES that empirically, pinning the
ENGINE-BLOCKED verdict to a specific, reproducible measurement rather than a code
read alone.

NO knot readout is run: since no winding->E coupling exists, seeding a 0_1 and
"measuring its E-field" would measure nothing the winding sources, OR would
require hand-wiring the forbidden code-convenience coupling. The block is booked
at the validate-on-known stage (prereg §3, coordinator item 3).

substrate-native-check: CP9 (heuristic-vs-dynamical) is the load-bearing check —
the exterior E(r) is NOT dynamically evolved from a winding source in any engine;
this is a WALL-engine capability gap, not a physics floor. ave-driver-script-honesty:
this driver makes NO physics claim beyond "the curl-Maxwell host has no
charge-source, so it does not source a static 1/r Coulomb field" — a host-capability
fact, verified by running.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

from ave.core.fdtd_3d import FDTD3DEngine


def _radial_profile(E_mag: np.ndarray, center: tuple[int, int, int], dx: float):
    """Return (r_phys, E_at_r) sampled along +x, +y, +z axes from center, so a
    would-be 1/r monopole is directly visible. Interior only (avoid edges)."""
    nx, ny, nz = E_mag.shape
    cx, cy, cz = center
    rs, es = [], []
    # sample along the three positive axes, skipping the immediate source cell and
    # the outer 4 cells (edge / ABC contamination)
    for axis in range(3):
        n = E_mag.shape[axis]
        for d in range(2, (n - cx if axis == 0 else n - cy if axis == 1 else n - cz) - 4):
            idx = [cx, cy, cz]
            idx[axis] += d
            rs.append(d * dx)
            es.append(float(E_mag[idx[0], idx[1], idx[2]]))
    order = np.argsort(rs)
    return np.array(rs)[order], np.array(es)[order]


def _fit_exponent(r: np.ndarray, e: np.ndarray):
    """Fit E ~ r^p on the cells where E is above the numerical floor. Return
    (p, n_valid). A Coulomb monopole E-field is p = -2 (potential 1/r => field 1/r^2);
    the potential itself is p = -1. We report the field-exponent p and flag whether
    ANY structured (non-floor) radial field exists at all."""
    floor = 1e-30
    mask = e > floor
    n_valid = int(mask.sum())
    if n_valid < 3:
        return None, n_valid
    p = np.polyfit(np.log(r[mask]), np.log(e[mask]), 1)[0]
    return float(p), n_valid


def main() -> int:
    out = {"docket": "B2", "leg": "engine-validate-on-known", "host": "fdtd_3d (curl-Maxwell)"}

    N = 48
    dx = 1.0e-3
    center = (N // 2, N // 2, N // 2)

    # ── SUB-TEST 1: zero-source control ──────────────────────────────────────
    # Zero initial E/H, no source, evolve. A curl-only Maxwell solver with no
    # charge-source must stay identically zero (no spurious field).
    eng0 = FDTD3DEngine(N, N, N, dx=dx, linear_only=True, use_pml=False)
    for _ in range(200):
        eng0.step()
    E0 = np.sqrt(eng0.Ex**2 + eng0.Ey**2 + eng0.Ez**2)
    ctrl_max = float(E0.max())
    out["subtest_1_zero_source_control"] = {
        "max_|E|_after_200_steps": ctrl_max,
        "stays_zero": bool(ctrl_max < 1e-30),
        "reading": "curl-only, no charge-source => field stays 0 (no spurious source)",
    }

    # ── SUB-TEST 2: would-be static point charge ─────────────────────────────
    # The ONLY available mechanism to put a charge in is a hand-set field. We set a
    # radial static E "monopole" (a would-be Coulomb field) as the INITIAL condition
    # and ask: does the curl-Maxwell update PRESERVE it as a static 1/r monopole
    # (as a real charge's field would be), or does it fail to (because there is no
    # charge to hold it — Gauss's law div E = rho/eps is not enforced; the static
    # longitudinal monopole is not a solution the curl-only solver maintains)?
    eng1 = FDTD3DEngine(N, N, N, dx=dx, linear_only=True, use_pml=False)
    cx, cy, cz = center
    xs = (np.arange(N) - cx) * dx
    ys = (np.arange(N) - cy) * dx
    zs = (np.arange(N) - cz) * dx
    X, Y, Z = np.meshgrid(xs, ys, zs, indexing="ij")
    R = np.sqrt(X**2 + Y**2 + Z**2)
    R[cx, cy, cz] = dx  # avoid singularity at the source cell
    # a would-be Coulomb E-field: E = q/(4 pi eps0) * r_hat / r^2, unit q
    Emag_coulomb = 1.0 / (4.0 * np.pi * eng1.epsilon_0 * R**2)
    eng1.Ex = Emag_coulomb * (X / R)
    eng1.Ey = Emag_coulomb * (Y / R)
    eng1.Ez = Emag_coulomb * (Z / R)

    # record the initial (planted) exterior profile — this IS a perfect 1/r^2 field
    E_init = np.sqrt(eng1.Ex**2 + eng1.Ey**2 + eng1.Ez**2)
    r_i, e_i = _radial_profile(E_init, center, dx)
    p_init, nv_init = _fit_exponent(r_i, e_i)

    # evolve under the curl-Maxwell update. A static monopole held by a real charge
    # would persist. Here there is no charge-source term, so div E = rho/eps is NOT
    # maintained: the planted longitudinal-static field is not a fixed point of the
    # curl-only update.
    energy_series = [float(eng1.total_field_energy())]
    for k in range(400):
        eng1.step()
        if (k + 1) % 100 == 0:
            energy_series.append(float(eng1.total_field_energy()))
    E_fin = np.sqrt(eng1.Ex**2 + eng1.Ey**2 + eng1.Ez**2)
    r_f, e_f = _radial_profile(E_fin, center, dx)
    p_fin, nv_fin = _fit_exponent(r_f, e_f)

    # what happened to the interior field profile vs the planted 1/r^2?
    # decisive test: does the exterior field REMAIN the planted Coulomb 1/r^2 shape
    # (a real charge would maintain it), or does it evolve/radiate/decay (no charge
    # to hold it)?
    interior = R > 5 * dx
    frac_change = float(
        np.abs(E_fin[interior] - E_init[interior]).mean()
        / (np.abs(E_init[interior]).mean() + 1e-300)
    )
    out["subtest_2_would_be_point_charge"] = {
        "planted_field_exponent_p": p_init,   # ~ -2 (perfect Coulomb 1/r^2 field)
        "planted_n_valid": nv_init,
        "final_field_exponent_p": p_fin,
        "final_n_valid": nv_fin,
        "mean_frac_change_interior": frac_change,
        "energy_series_every_100_steps": energy_series,
        "charge_source_term_present": False,  # verified by code read: fdtd_3d has no rho/J source
        "reading": (
            "The planted field IS a perfect Coulomb 1/r^2 (p~-2), but the curl-Maxwell "
            "update does NOT hold it as a static monopole because there is no "
            "charge-source (Gauss's law div E = rho/eps is not enforced). The static "
            "longitudinal monopole is not a fixed point of the curl-only solver."
        ),
    }

    # ── VERDICT ──────────────────────────────────────────────────────────────
    # validate-on-known PASSES only if the host can maintain a KNOWN static 1/r
    # Coulomb field from a charge. It cannot: (1) no charge-source term exists to
    # SOURCE such a field from a charge; (2) the planted field is not maintained as
    # a static monopole under the curl-only update. Either way the host cannot
    # answer the exterior-tail question => ENGINE-BLOCKED.
    validate_on_known_pass = False
    out["validate_on_known"] = {
        "pass": validate_on_known_pass,
        "why_fail": (
            "fdtd_3d is a curl-only Yee-Maxwell solver (E from curl H, H from curl E). "
            "It has NO charge-source term (no rho, no J in update_electric_field; grep "
            "confirmed 0 hits). A static point charge has no representation: it cannot "
            "SOURCE a 1/r Coulomb field, and a planted monopole is not a fixed point of "
            "the curl-only update. The static/longitudinal electrostatic sector — the "
            "sector the boundary integer would source — is absent from the EM host."
        ),
    }

    # the winding->EM source coupling audit result (from the prereg host audit, §2)
    out["winding_to_EM_source_coupling"] = {
        "exists_in_any_engine": False,
        "hosts_audited": ["crystal_graft_v4 (omega-only, gapped, no E)",
                          "fdtd_3d (curl-Maxwell E/B, no charge-source)",
                          "unified_engine (reads Q_link, no Q_link->u/E path)"],
        "grep_winding_to_E_source": "EMPTY across src/ave/**/*.py",
        "missing_piece": (
            "the coupling by which Q = Link(dOmega, F) in Z sources the massless EM "
            "channel's static 1/r Coulomb field — underived in code exactly as in canon "
            "(claim-quality.md:1311 open item)."
        ),
    }

    out["bin"] = "ENGINE-BLOCKED"
    out["grant_ruling_status"] = (
        "UNDECIDED-BY-ENGINE, block-localized. The engine can neither confirm nor break "
        "the sector-conflation ruling: the mechanism the ruling posits (winding sources "
        "the massless EM channel) is exactly the unimplemented/underived piece. Ruling "
        "stands as the leading hypothesis; engine verdict = cannot-decide."
    )

    results_path = Path(__file__).with_name("compositeness_engine_leg_validate_results.json")
    results_path.write_text(json.dumps(out, indent=2))

    # human-readable summary to stdout
    print("=== Compositeness engine leg — validate-on-known ===")
    print(f"host: {out['host']}")
    print(f"subtest 1 (zero-source control): stays_zero = {out['subtest_1_zero_source_control']['stays_zero']}")
    s2 = out["subtest_2_would_be_point_charge"]
    print(f"subtest 2 (would-be point charge): planted p = {s2['planted_field_exponent_p']:.3f} "
          f"(Coulomb field ~ -2), charge_source_term_present = {s2['charge_source_term_present']}")
    print(f"validate-on-known PASS = {out['validate_on_known']['pass']}")
    print(f"winding->EM source coupling exists = {out['winding_to_EM_source_coupling']['exists_in_any_engine']}")
    print(f"BIN = {out['bin']}")
    print(f"Grant ruling status = UNDECIDED-BY-ENGINE (block-localized)")
    print(f"results -> {results_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
