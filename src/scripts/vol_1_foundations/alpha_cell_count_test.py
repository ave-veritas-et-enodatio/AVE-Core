"""
α Class-2 lift discriminating test: CELL-COUNT (effective mode volume).
=======================================================================

CLAIM UNDER TEST
----------------
α⁻¹ = Q, and canonically Q = cell-count = mode-count
(`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/
op21-multi-mode-mode-counting.md:144`). The hypothesis: the relaxed electron
(2,3) mode occupies N ≈ 4π³ + π² + π = 137.036 effective Nyquist cells, so that
α = 1/137 reads as "one radiative leak per 137 cavity modes." If N emerges
α-free and geometry-free from a GENERIC seed that dynamically selects its own
bound geometry, that lifts the α derivation toward Class 2 (axiom-manifestation
emergence). If N≠137, that is reported honestly.

COORDINATE-SYSTEM STATUS (phase-space-coordinate-check, A46 — LOAD-BEARING)
--------------------------------------------------------------------------
The corpus N_modes = N_cells count is defined over the Clifford-torus embedding
T² ⊂ S³ ⊂ ℂ² — a PHASE-SPACE manifold (op21-multi-mode-mode-counting.md:104),
at the Golden Torus R·r = 1/4 in lattice-natural units. The three Λ's
(4π³, π², π) are dimensionless geometric measures of PHASE-SPACE submanifolds.
The corpus's own numerical verification (op21_multimode_derivation.py) integrates
over those explicit phase-space parametric domains ([0,2π)^k angular variables).

This driver measures N_eff in REAL-SPACE: the participation number of the
real-space lattice energy density u(i,j,k) on the Yee grid. Per A46, a
real-space N_eff compared against a phase-space φ²-Clifford-torus 137 prediction
is a COORDINATE MISMATCH and is structurally uninformative FOR THE CORPUS CLAIM.

Therefore this driver's load-bearing scientific output is the REAL-SPACE binding
behavior (does a generic (2,3) seed bind/persist vs a random-direction baseline,
and if so what real-space geometry does it select). The N_eff-vs-137 comparison
is reported as a real-space diagnostic with the coordinate caveat attached — NOT
as a phase-space confirmation/refutation of α⁻¹ = N_cells. A phase-space-native
cell-count is a separate measurement (the corpus already has it analytically; a
forward phase-space participation count would require bond-port (V_inc, V_ref)
decomposition the FDTD field does not expose).

HARD GUARDS (the whole point — violating any one invalidates the result)
------------------------------------------------------------------------
G1 FORWARD-NOT-FIT (ave-driver-script-honesty): report whatever N_eff comes out.
   No seed/param/threshold is tuned to hit 137. There is NO minimize/curve_fit/
   target-residual anywhere in this file. This is a forward measurement.
G2 NO IMPOSED GEOMETRY: the seed is a GENERIC (R, r) at round mid-grid values,
   NOT the Golden Torus (R=φ/2≈0.809, r=(φ−1)/2≈0.309 in ℓ_node units). The
   dynamics relax it. R_GOLDEN_TORUS / R_GOLDEN_TORUS_MINOR / RR_GOLDEN_TORUS /
   PHI are NEVER imported or used to build a seed.
G3 NO CHARGE / α IN THE COUNT: N_eff is a pure energy-density participation
   number. e_charge, ALPHA, ALPHA_COLD, ALPHA_COLD_INV, XI_TOPO, V_SNAP are
   NEVER used to compute N_eff. Confinement uses V_YIELD-scale (α-free relative
   to the count: the count never divides by α). 137 / α is never fed into the
   measure.
G4 THRESHOLD-FREE: N_eff is the participation number (Σuᵢ)² / Σuᵢ² — NOT a
   tunable |field|² > cutoff count. PML cells are excluded BEFORE any reduction
   (substrate-native sampling discipline, A-Rule 10 corollary).

OUTCOMES
--------
A  (LIFT):       binds with generic seed, relaxes, N_eff ≈ 137, geometry
                 dynamically selected, no α/charge in → strong.
B  (RELOCATION): N_eff ≈ 137 only with imposed Golden-Torus seed.
C  (FAIL):       binds but N_eff ≠ 137.
INCONCLUSIVE:    does not bind — cell-count needs a bound-state mechanism first.

(Per the coordinate caveat above, an A/B/C verdict here is a REAL-SPACE verdict.)

Run:
    python src/scripts/vol_1_foundations/alpha_cell_count_test.py
"""

from __future__ import annotations

import numpy as np

# Canonical-source discipline (ave-canonical-source): import canonical constants;
# never hard-code. NOTE the deliberate exclusions enforcing guard G3 — the
# answer-bearing constants are NOT imported:
#   NOT imported: ALPHA, ALPHA_COLD, ALPHA_COLD_INV, V_SNAP, XI_TOPO, e_charge,
#                 PHI, R_GOLDEN_TORUS, R_GOLDEN_TORUS_MINOR, RR_GOLDEN_TORUS.
# V_YIELD is imported only to set the confinement amplitude scale (the α-free
# macroscopic saturation onset); it never enters the N_eff arithmetic.
import ave.core.constants as _avc
from ave.core.constants import V_YIELD
from ave.core.fdtd_3d import FDTD3DEngine

# Canonical-source verification: ensure ave.core.constants is the AVE-Core source.
assert _avc.__file__.endswith("ave/core/constants.py"), (
    "ave.core.constants is not the AVE-Core canonical source"
)

# ---------------------------------------------------------------------------
# Targets (geometry computed from π only — no α, no charge: guard G3 holds).
# These are COMPARISON references, printed as targets, never fed into N_eff.
# ---------------------------------------------------------------------------
TARGET_FULL = 4.0 * np.pi**3 + np.pi**2 + np.pi  # 137.0363... (the headline claim)
TARGET_VOL = 4.0 * np.pi**3  # 124.025...        (dominant volume term alone)


# ---------------------------------------------------------------------------
# Seed builders — copied in spirit from the validated scaffold at
# src/tests/test_fdtd3d_electron_torus_knot_seed.py (PASS/PARTIAL/NULL discipline),
# kept self-contained here. Seeds are GENERIC: caller passes (R, r) in cells.
# ---------------------------------------------------------------------------
def build_torus_knot_E_seed(engine, R, r, amplitude, p=2, q=3, knot_thickness=2.0):
    """Vector E_x,E_y,E_z tracing the (p,q) torus-knot tangent on a toroidal shell.

    Hedgehog (power-law) envelope around the (R, r) shell; E ∥ knot tangent.
    Maxwell evolution auto-generates B via curl coupling. (R, r) in cells.
    """
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0

    i, j, k = np.indices((nx, ny, nz))
    x = i - cx
    y = j - cy
    z = k - cz

    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R) ** 2 + z**2 + 1e-12)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho_xy - R)

    envelope = amplitude / (1.0 + (rho_tube / knot_thickness) ** 2)

    dphi_x = -(R + r * np.cos(psi)) * np.sin(phi)
    dphi_y = (R + r * np.cos(psi)) * np.cos(phi)
    dphi_z = np.zeros_like(phi)
    dpsi_x = -r * np.sin(psi) * np.cos(phi)
    dpsi_y = -r * np.sin(psi) * np.sin(phi)
    dpsi_z = r * np.cos(psi) * np.ones_like(phi)

    t_x = p * dphi_x + q * dpsi_x
    t_y = p * dphi_y + q * dpsi_y
    t_z = p * dphi_z + q * dpsi_z
    t_mag = np.sqrt(t_x**2 + t_y**2 + t_z**2 + 1e-12)

    engine.Ex += envelope * t_x / t_mag
    engine.Ey += envelope * t_y / t_mag
    engine.Ez += envelope * t_z / t_mag


def build_random_direction_baseline(engine, R, r, amplitude, knot_thickness=2.0, seed=42):
    """Same hedgehog envelope, RANDOM direction per cell (no topology). Falsifier."""
    rng = np.random.RandomState(seed)
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0

    i, j, k = np.indices((nx, ny, nz))
    x = i - cx
    y = j - cy
    z = k - cz
    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R) ** 2 + z**2 + 1e-12)
    envelope = amplitude / (1.0 + (rho_tube / knot_thickness) ** 2)

    rx = rng.randn(nx, ny, nz)
    ry = rng.randn(nx, ny, nz)
    rz = rng.randn(nx, ny, nz)
    rmag = np.sqrt(rx**2 + ry**2 + rz**2 + 1e-12)
    engine.Ex += envelope * rx / rmag
    engine.Ey += envelope * ry / rmag
    engine.Ez += envelope * rz / rmag


# ---------------------------------------------------------------------------
# Measurement: PML mask + participation number + real-space (R, r) of the
# energy-density distribution. All guards live here.
# ---------------------------------------------------------------------------
def interior_mask(engine):
    """Boolean mask excluding PML cells (guard G4 — substrate-native sampling).

    When use_pml is False the engine uses Mur ABC (no PML region); we still trim
    one boundary cell per face because the Mur update overwrites the outer layer.
    """
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    t = engine.pml_layers if engine.use_pml else 1
    mask = np.zeros((nx, ny, nz), dtype=bool)
    mask[t : nx - t, t : ny - t, t : nz - t] = True
    return mask


def participation_number(u, mask):
    """Threshold-free effective mode volume in cells (guard G4).

        N_eff = (Σ_i u_i)² / Σ_i u_i²   over interior cells only.

    u is the per-cell EM energy density (J/m³); N_eff is invariant to overall
    scale of u, so no amplitude/threshold tuning can move it (guard G1). A
    uniform field over M cells gives N_eff = M; a delta gives N_eff = 1.
    """
    uu = u[mask]
    s1 = float(np.sum(uu))
    s2 = float(np.sum(uu**2))
    if s2 <= 0.0:
        return 0.0
    return (s1 * s1) / s2


def relaxed_R_r(engine, u, mask):
    """Real-space (R, r) of the energy-density torus, in CELLS.

    R = energy-weighted mean cylindrical radius √(x²+y²) about the lattice axis
        through the energy centroid (z-axis by construction of the seed).
    r = energy-weighted RMS distance from that mean torus centerline.
    Density-weighted (not centroid-offset) per substrate-native sampling — the
    centroid of a shell is the empty middle, so we weight by u on the shell.
    Returns (R_cells, r_cells, peak_frac_in_pml) where the last is a guard probe.
    """
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    i, j, k = np.indices((nx, ny, nz))
    x = i - cx
    y = j - cy
    z = k - cz
    rho = np.sqrt(x**2 + y**2)

    w = np.where(mask, u, 0.0)
    W = float(np.sum(w))
    if W <= 0.0:
        return float("nan"), float("nan"), float("nan")
    R = float(np.sum(w * rho) / W)
    # minor radius: RMS distance from the (R, z=centroid) centerline in the
    # (rho, z) meridional plane
    z_bar = float(np.sum(w * z) / W)
    d_tube_sq = (rho - R) ** 2 + (z - z_bar) ** 2
    r = float(np.sqrt(np.sum(w * d_tube_sq) / W))

    # Guard probe: what fraction of total (un-masked) energy sits in PML cells?
    # If large, the "bound" state is really frozen-absorbing PML artifact.
    full = float(np.sum(u))
    pml_frac = (full - W) / full if full > 0 else float("nan")
    return R, r, pml_frac


def run_and_probe(engine, n_steps, probe_every=20):
    """Evolve; track peak |E|, total energy, and (R,r) drift over the window.

    Records both the C-state proxy (½ε|E|²) and L-state proxy (½μ|H|²) via the
    full energy density (reactance-pair discipline) at each probe.
    """
    times, peak_E, tot_E = [], [], []
    Rs, rs = [], []
    mask = interior_mask(engine)
    for step in range(n_steps):
        engine.update_magnetic_field()
        engine.update_electric_field()
        if engine.use_pml:
            engine.apply_pml()
        else:
            engine.apply_mur_abc()
        if step % probe_every == 0:
            E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
            u = engine.energy_density()  # ½ε_eff|E|² + ½μ_eff|H|² — full LC energy
            times.append(step * engine.dt)
            peak_E.append(float(E_mag[mask].max()))
            tot_E.append(float(np.sum(u[mask])))
            R, r, _ = relaxed_R_r(engine, u, mask)
            Rs.append(R)
            rs.append(r)
    return {
        "t": np.array(times),
        "peak_E": np.array(peak_E),
        "tot_E": np.array(tot_E),
        "R": np.array(Rs),
        "r": np.array(rs),
    }


def classify_binding(knot, rand):
    """PASS/PARTIAL/NULL/FAIL per the scaffold discipline.

    Compares peak-|E| retention of the (2,3) knot vs the random baseline, and
    checks the knot's energy-density torus does not disperse (R, r roughly held).
    """
    k_ret = knot["peak_E"][-1] / knot["peak_E"][0]
    r_ret = rand["peak_E"][-1] / rand["peak_E"][0]
    ratio = k_ret / r_ret if r_ret > 0 else float("inf")

    # FWHM-proxy: relative growth of minor radius r (dispersion → r grows)
    r0, r1 = knot["r"][0], knot["r"][-1]
    r_growth = (r1 / r0) if (r0 and np.isfinite(r0) and np.isfinite(r1)) else float("nan")

    if k_ret >= 0.80 and np.isfinite(r_growth) and r_growth <= 1.5:
        verdict = "PASS (≥80% peak retention, torus holds <1.5× minor-radius growth)"
    elif ratio >= 1.5 and k_ret >= 0.30:
        verdict = "PARTIAL (knot retention ≥1.5× random, some persistence)"
    elif ratio >= 0.9:
        verdict = "NULL (knot ~ random, photon-like dispersal)"
    else:
        verdict = "FAIL (knot retention < random; topology degrades localization)"
    return verdict, k_ret, r_ret, ratio, r_growth


def assert_guards_held():
    """Static self-audit: confirm forbidden answer-bearing symbols never USED in code.

    Reads THIS source file and asserts none of the guard-G3 forbidden names appear
    as a real NAME token in executable code (i.e. as an actual variable/import
    reference) — string literals, docstrings, and comments are excluded via the
    Python tokenizer, so the forbidden-list strings INSIDE this very function and
    the names quoted in the header docstring do not trip the guard. This turns
    guard G3 into a runtime check rather than a promise (ave-driver-script-honesty).
    """
    import io
    import token as _tok
    import tokenize
    from pathlib import Path

    forbidden = {
        "ALPHA", "ALPHA_COLD", "ALPHA_COLD_INV", "V_SNAP", "XI_TOPO", "e_charge",
        "PHI", "R_GOLDEN_TORUS", "R_GOLDEN_TORUS_MINOR", "RR_GOLDEN_TORUS",
    }
    # The single set literal below is the ONLY place these names appear as
    # strings in code; tokenize classifies them as STRING tokens here, not NAME
    # tokens, so they are excluded from the NAME-token scan that follows.
    src = Path(__file__).read_text()
    name_tokens = set()
    for tk in tokenize.generate_tokens(io.StringIO(src).readline):
        if tk.type == _tok.NAME:
            name_tokens.add(tk.string)
    leaked = sorted(forbidden & name_tokens)
    assert not leaked, (
        f"Guard G3 VIOLATED: answer-bearing symbol(s) referenced as code: {leaked}"
    )
    return True


def main():
    print("=" * 74)
    print("α CELL-COUNT TEST — real-space participation number N_eff (forward)")
    print("=" * 74)
    print("COORDINATE STATUS: N_eff measured in REAL-SPACE (lattice-Cartesian).")
    print("  Corpus 137 = N_cells lives in PHASE-SPACE (Clifford torus T²⊂S³⊂ℂ²).")
    print("  Per A46 this comparison is a coordinate diagnostic, NOT a phase-space")
    print("  confirmation of α⁻¹ = N_cells. Load-bearing output = binding behavior.")
    print()
    print(f"  Targets (π-only, α-free): full 4π³+π²+π = {TARGET_FULL:.4f}")
    print(f"                            vol-only 4π³    = {TARGET_VOL:.4f}")

    # Runtime guard self-audit (guard G3).
    assert_guards_held()
    print("\n  [guard G3] static self-audit PASS — no α/charge/Golden-Torus symbol "
          "in N_eff code path.")

    # Grid + run params. dx is a numerical grid parameter (NOT ℓ_node); physics
    # enters via V_yield. (R, r) seeds are in CELLS — GENERIC mid-grid, NOT the
    # Golden Torus (guard G2).
    N = 48
    DX = 0.01
    N_STEPS = 600
    PROBE_EVERY = 20
    # Amplitude: a moderate fraction of V_yield/dx — α-free saturation onset.
    # 0.5 chosen to engage Axiom-4 nonlinearity without rupturing (per scaffold).
    AMPLITUDE = 0.5 * V_YIELD / DX

    # GENERIC seed geometries in cells (guard G2): round mid-grid values, plus a
    # small spread. NONE is the Golden Torus. With a 48-cell grid, R≈10, r≈4 is
    # a neutral fat torus well inside the interior; the spread probes seed-
    # independence of whatever geometry the dynamics select.
    generic_seeds = [
        (10.0, 4.0),
        (12.0, 3.0),
        (8.0, 5.0),
    ]

    results = []
    for (R0, r0) in generic_seeds:
        print("\n" + "-" * 74)
        print(f"GENERIC seed (R, r) = ({R0}, {r0}) cells  [NOT Golden Torus]")
        print("-" * 74)

        eng_k = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=False, use_pml=False)
        build_torus_knot_E_seed(eng_k, R0, r0, AMPLITUDE, p=2, q=3, knot_thickness=2.0)
        seed_peak = np.sqrt(eng_k.Ex**2 + eng_k.Ey**2 + eng_k.Ez**2).max()
        print(f"  knot   seed peak |E| = {seed_peak:.3e} V/m")
        knot = run_and_probe(eng_k, N_STEPS, PROBE_EVERY)

        eng_r = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=False, use_pml=False)
        build_random_direction_baseline(eng_r, R0, r0, AMPLITUDE, knot_thickness=2.0)
        rand = run_and_probe(eng_r, N_STEPS, PROBE_EVERY)

        verdict, k_ret, r_ret, ratio, r_growth = classify_binding(knot, rand)

        # Final-state real-space measurement on the knot engine.
        mask = interior_mask(eng_k)
        u_final = eng_k.energy_density()
        N_eff = participation_number(u_final, mask)
        R_relax, r_relax, pml_frac = relaxed_R_r(eng_k, u_final, mask)

        print(f"  binding: {verdict}")
        print(f"    knot peak-|E| retention = {k_ret:.3f}   random = {r_ret:.3f}   "
              f"ratio = {ratio:.3f}")
        print(f"    knot minor-radius growth = {r_growth:.3f}× (dispersion if ≫1)")
        print(f"    knot max dielectric strain ratio = {eng_k.max_strain_ratio:.4f} "
              f"(Op14 saturation engaged if >0)")
        print(f"  N_eff (real-space participation, boundary-excluded) = {N_eff:.2f} cells")
        print(f"    vs 137.036 (full): ratio {N_eff / TARGET_FULL:.3f}   "
              f"vs 124.0 (vol): ratio {N_eff / TARGET_VOL:.3f}")
        print(f"  relaxed real-space torus (cells): R = {R_relax:.2f}, r = {r_relax:.2f}, "
              f"R·r = {R_relax * r_relax:.2f}")
        print(f"    [guard G4 probe] fraction of total energy in excluded boundary "
              f"cells = {pml_frac:.3f}")

        results.append({
            "seed": (R0, r0), "verdict": verdict, "k_ret": k_ret, "ratio": ratio,
            "N_eff": N_eff, "R_relax": R_relax, "r_relax": r_relax,
            "strain": eng_k.max_strain_ratio, "pml_frac": pml_frac,
        })

    # ---------------------------------------------------------------
    # Verdict synthesis (REAL-SPACE — coordinate caveat applies).
    # ---------------------------------------------------------------
    print("\n" + "=" * 74)
    print("VERDICT (real-space; see coordinate caveat in header)")
    print("=" * 74)
    bound = [r for r in results if r["verdict"].startswith(("PASS", "PARTIAL"))]
    if not bound:
        print("INCONCLUSIVE — no generic seed binds (all NULL/FAIL vs random "
              "baseline). Cell-count needs a bound-state mechanism first; the "
              "FDTD (2,3) E-seed disperses photon-like, consistent with the "
              "corpus position that the (2,3) is a PHASE-SPACE winding, not a "
              "real-space attractor on the vector Maxwell engine.")
    else:
        N_vals = np.array([r["N_eff"] for r in bound])
        near_full = np.any(np.abs(N_vals - TARGET_FULL) / TARGET_FULL < 0.10)
        print(f"At least one generic seed bound ({len(bound)}/{len(results)}). "
              f"N_eff over bound seeds = {N_vals.round(1).tolist()}")
        if near_full:
            print("OUTCOME A candidate (REAL-SPACE): generic seed bound and N_eff "
                  "≈ 137 — but this is a REAL-SPACE count; confirming the lift "
                  "requires the PHASE-SPACE cell-count (coordinate caveat). Flag "
                  "to Grant; do not headline as Class-2 lift on real-space alone.")
        else:
            print("OUTCOME C (REAL-SPACE): binds but N_eff ≠ 137 in real-space. "
                  "Expected if 137 is phase-space-native (real-space and "
                  "phase-space measures needn't match for AVE solitons, "
                  "doc 28 §3-§4).")
    print("\nGUARDS held: G1 forward-not-fit (no fit anywhere) | G2 generic seed "
          "(no Golden Torus) | G3 no α/charge in N_eff (static self-audit PASS) | "
          "G4 threshold-free participation number, boundary cells excluded.")


if __name__ == "__main__":
    main()
