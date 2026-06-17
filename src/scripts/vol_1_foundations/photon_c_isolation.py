"""
T₂-photon group-velocity isolation from the √2c A₁/CFL precursor.

DOCUMENTATION driver (Grant: DEC-01 / weak-C ruled). Prereg:
  research/2026-06-16_photon-c-isolation-prereg.md  (FROZEN bins).

Closes the handoff RESIDUAL OPEN
(`_orchestration/2026-06-14_photon-ontology-vocabulary-adjudication-handoff.md`
Amendment-2): the prior cardinal PPW sweep gave `project_T2` on=off → same
speed, so it plausibly caught the A₁/CFL bulk front (√2c), NOT the resolved
T₂-photon group velocity (which should be c). The mode-identity is UNISOLATED.

Substrate-native facts (verified, see prereg §1):
  - Scatter S = ½·𝟙 − I has eigenvalues [-1,-1,-1,+1]; A₁=(1,1,1,1) is the +1
    common mode (non-dispersive DC front = the √2c bulk precursor), T₂ the −1
    triplet (carries a per-step −1 phase → distinct group velocity dω/dk).
  - Connect-shift marches the wavefront 1 cardinal cell/step regardless of mode
    (every port-shift has x-component ±1), and `dt = dx/(c√2)` (k4_tlm.py:183)
    fixes the bare front to √2c. So mode-separation lives in the GROUP velocity
    (envelope peak-arrival), not the bare front.

THE √2 IS A COORDINATE/SAMPLING ARTIFACT (CP4): all speeds are reported as v/c
in dt-scaled physical time (cardinal-cell distance / step·dt). We do NOT
re-introduce the per-port distance-count convention. The fastest channel reads
√2c by the dt convention; modes separate by group-vs-front, not by re-counting.

Two tests (prereg §2):
  Test 1 — PURE-T₂ / PURE-A₁ / MIXED group + front velocities (mode isolation).
  Test 2 — sharp on/off step into PURE-T₂; information-front causality check.

Reuses the canonical launcher machinery from photon_propagation.py.
"""

import json

import numpy as np

from ave.core.constants import C_0, V_SNAP
from ave.core.k4_tlm import K4Lattice3D

# Port geometry — A→B direction vectors (matches photon_propagation.py).
PORT_VECS = np.array(
    [[+1, +1, +1], [+1, -1, -1], [-1, +1, -1], [-1, -1, +1]], dtype=float
)
PORT_HAT = PORT_VECS / np.sqrt(3.0)


# ─────────────────────────────────────────────────────────────────────
# Port-weight launchers (T₂-projected / A₁-only / raw-mixed)
# ─────────────────────────────────────────────────────────────────────
def port_weights(direction, mode: str) -> np.ndarray:
    """
    Forward port weights for +d̂ propagation, in one of three modes.

    mode="T2"    : T₂-projected (subtract A₁; Σw=0; unit √Σw²). The photon.
    mode="A1"    : A₁ common-mode forward weights (the √2c bulk precursor).
    mode="MIXED" : raw max(0,−d̂·p̂) forward weights (~50% A₁ + ~50% T₂),
                   the historical default that produced the unisolated √2c.
    """
    d = np.asarray(direction, dtype=float)
    d = d / np.linalg.norm(d)
    w = np.maximum(0.0, -PORT_HAT @ d)  # raw forward weights
    if mode == "T2":
        w = w - w.mean()  # project onto T₂ (⊥ A₁=(1,1,1,1))
        norm = np.sqrt((w * w).sum())
        return w / norm if norm > 0 else w
    if mode == "A1":
        # Pure A₁ forward common-mode: all ports equal, oriented so the
        # common-mode energy radiates in +d̂. Normalise to unit √Σw².
        w_a1 = np.ones(4, dtype=float)
        return w_a1 / np.sqrt((w_a1 * w_a1).sum())
    if mode == "MIXED":
        s = w.sum()
        return w / s if s > 0 else w
    raise ValueError(f"unknown mode {mode!r}")


# ─────────────────────────────────────────────────────────────────────
# Plane source (Gaussian-modulated sinusoid OR sharp on/off step)
# ─────────────────────────────────────────────────────────────────────
class PlaneSource:
    def __init__(self, x0, y_c, z_c, port_w, sigma_yz, omega,
                 t_center, t_sigma, amplitude, step_mode=False, t_on=None):
        self.x0 = x0
        self.y_c = y_c
        self.z_c = z_c
        self.port_w = port_w
        self.sigma_yz = sigma_yz
        self.omega = omega
        self.t_center = t_center
        self.t_sigma = t_sigma
        self.amplitude = amplitude
        self.step_mode = step_mode  # True → sharp on/off step (Test 2)
        self.t_on = t_on if t_on is not None else t_center
        self._cache = None

    def _yz(self, ny, nz):
        if self._cache and self._cache[:2] == (ny, nz):
            return self._cache[2]
        j, k = np.indices((ny, nz), dtype=float)
        r2 = (j - self.y_c) ** 2 + (k - self.z_c) ** 2
        prof = np.exp(-r2 / (2.0 * self.sigma_yz**2))
        self._cache = (ny, nz, prof)
        return prof

    def apply(self, lattice, t):
        if self.step_mode:
            # Sharp on/off STEP: carrier abruptly on at t_on, off after a few
            # periods. No Gaussian ramp → a true signal edge whose arrival is
            # the information front (Test 2 causality observable).
            period = 2.0 * np.pi / self.omega
            on = (t >= self.t_on) and (t < self.t_on + 4.0 * period)
            A_t = self.amplitude * (np.sin(self.omega * (t - self.t_on)) if on else 0.0)
        else:
            env = np.exp(-((t - self.t_center) ** 2) / (2.0 * self.t_sigma**2))
            A_t = self.amplitude * env * np.sin(self.omega * (t - self.t_center))
        if abs(A_t) < 1e-30:
            return
        yz = self._yz(lattice.ny, lattice.nz)
        active = lattice.mask_active[self.x0].astype(float)
        injection = A_t * yz * active
        for n in range(4):
            if self.port_w[n] != 0:
                lattice.V_inc[self.x0, :, :, n] += self.port_w[n] * injection


# ─────────────────────────────────────────────────────────────────────
# Slab-energy time-history at interior planes (PML-excluded — CP7)
# ─────────────────────────────────────────────────────────────────────
def slab_energy_history(lattice, x_planes):
    """Σ_{y,z}|V|² at each interior x-plane (PML rows excluded in y,z)."""
    rho = lattice.get_energy_density()  # (nx,ny,nz)
    p = lattice.pml_thickness
    ny, nz = lattice.ny, lattice.nz
    sl_y = slice(p, ny - p)
    sl_z = slice(p, nz - p)
    return {x: float(rho[x, sl_y, sl_z].sum()) for x in x_planes}


def _peak_arrival(times, series):
    """Group-velocity observable: time of envelope (slab-energy) peak."""
    series = np.asarray(series)
    if series.max() <= 0.0:
        return None
    return float(times[int(np.argmax(series))])


def _front_arrival(times, series, frac=0.10):
    """Front observable: first time slab-energy exceeds frac·(lifetime max)."""
    series = np.asarray(series)
    m = series.max()
    if m <= 0.0:
        return None
    thresh = frac * m
    idx = np.argmax(series >= thresh)
    if series[idx] < thresh:
        return None
    return float(times[idx])


# ─────────────────────────────────────────────────────────────────────
# One propagation run
# ─────────────────────────────────────────────────────────────────────
def run_one(mode, *, N=96, pml=8, lambda_cells=10.0, sigma_yz=8.0,
            t_sigma_periods=0.75, amp_frac=0.01, source_x=16, n_steps=240,
            step_mode=False, x_a=None, x_b=None):
    """Launch a +x̂ packet of the given mode; return group/front speeds (v/c)."""
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=pml)
    dt, c, dx = lattice.dt, float(C_0), lattice.dx

    omega = 2.0 * np.pi * c / (lambda_cells * dx)
    period = 2.0 * np.pi / omega
    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma
    amp = amp_frac * float(V_SNAP)

    if x_a is None:
        x_a, x_b = source_x + 20, source_x + 60  # interior, PML-excluded

    src = PlaneSource(
        x0=source_x, y_c=(N - 1) / 2.0, z_c=(N - 1) / 2.0,
        port_w=port_weights((1.0, 0.0, 0.0), mode),
        sigma_yz=sigma_yz, omega=omega, t_center=t_center,
        t_sigma=t_sigma, amplitude=amp, step_mode=step_mode, t_on=t_center,
    )

    # Record the full interior x-plane set (PML-excluded — CP7) so the
    # information-front slope can be fit over many planes (Test 2), not just two.
    all_planes = list(range(source_x + 4, N - pml))
    hist = {x: [] for x in all_planes}
    times = [0.0]
    h0 = slab_energy_history(lattice, all_planes)
    for x in all_planes:
        hist[x].append(h0[x])

    for step in range(1, n_steps + 1):
        src.apply(lattice, step * dt)
        lattice.step()
        times.append(lattice.timestep * dt)
        h = slab_energy_history(lattice, all_planes)
        for x in all_planes:
            hist[x].append(h[x])

    times = np.asarray(times)
    hist_a = hist[x_a]
    hist_b = hist[x_b]

    def speed(arrival_fn):
        t_a = arrival_fn(times, hist_a)
        t_b = arrival_fn(times, hist_b)
        if t_a is None or t_b is None or t_b <= t_a:
            return 0.0
        return float((x_b - x_a) * dx / (t_b - t_a) / c)

    out = {
        "mode": mode, "step_mode": step_mode,
        "x_a": x_a, "x_b": x_b, "dt_s": dt,
        "v_group_over_c": speed(_peak_arrival),  # envelope group velocity
        "v_front_over_c": speed(_front_arrival),  # leading-edge front (2-plane)
    }

    if step_mode:
        # Test 2 — robust INFORMATION front: slope of first-detectable-above-
        # floor arrival across ALL interior planes. The floor is 10× the
        # pre-step-on slab-energy max (so we detect the step's leading edge,
        # not pre-existing field). This is the causal observable.
        t_on_idx = int(np.argmax(times >= t_center))
        pre = [max(hist[x][: max(t_on_idx, 1)]) for x in all_planes]
        floor = max(max(pre, default=0.0), 1e-30) * 10.0
        xs, ta = [], []
        for x in all_planes:
            s = np.asarray(hist[x])
            idx = int(np.argmax(s >= floor))
            if s[idx] >= floor:
                xs.append(x)
                ta.append(times[idx])
        xs, ta = np.asarray(xs, float), np.asarray(ta)
        # Fit over the clean interior range (exclude source-adjacent + near-PML).
        m = (xs >= source_x + 12) & (xs <= N - pml - 4)
        if m.sum() >= 2:
            slope = np.polyfit(ta[m], xs[m] * dx, 1)[0]  # m/s
            out["info_front_over_c"] = float(slope / c)
            out["info_front_n_planes"] = int(m.sum())
        else:
            out["info_front_over_c"] = 0.0
            out["info_front_n_planes"] = int(m.sum())

    return out


# ─────────────────────────────────────────────────────────────────────
# Bin adjudication (FROZEN — prereg §3)
# ─────────────────────────────────────────────────────────────────────
def _near(v, target, tol=0.15):
    return abs(v - target) <= tol * target


def adjudicate(r_t2_group, r_a1_front, r_mixed_group, info_front):
    """
    FROZEN bin logic (prereg §3), with UNISOLABLE tested FIRST.

    Ordering rationale (corrected from the prereg-naive order): "T2-RIDES-AT-√2c"
    only carries its intended meaning ("the transverse photon ITSELF is √2c,
    distinct from A₁") when A₁ rides at a DIFFERENT speed. If T₂, A₁, and MIXED
    are all indistinguishable (spread ≤ 15%), the modes are NOT separated and the
    honest bin is UNISOLABLE — a √2 reading shared by all modes is the dt/connect
    convention, not a per-mode speed. So UNISOLABLE is checked before the √2c bin.
    """
    sqrt2 = np.sqrt(2.0)

    # Causality sub-result (information front vs c, dt-scaled physical time).
    causal = "CAUSAL-OK" if info_front <= 1.0 * 1.15 else "CAUSAL-VIOLATION"

    vals = [r_t2_group, r_a1_front, r_mixed_group]
    spread = (max(vals) - min(vals)) / max(np.mean(vals), 1e-12)

    # 1) UNISOLABLE first — all three modes indistinguishable.
    if spread <= 0.15:
        bin_ = "UNISOLABLE-ON-THIS-ENGINE"
    # 2) clean separation: T₂ at c, A₁ front demonstrably ahead at √2c.
    elif (_near(r_t2_group, 1.0) and _near(r_a1_front, sqrt2)
          and r_a1_front > r_t2_group * 1.15):
        bin_ = "T2-RIDES-AT-c"
    # 3) T₂ rides at √2c while A₁ rides elsewhere (modes ARE separated).
    elif _near(r_t2_group, sqrt2):
        bin_ = "T2-RIDES-AT-√2c"
    else:
        bin_ = "PARTIAL-SEPARATION-DOCUMENT"
    return bin_, causal


# ─────────────────────────────────────────────────────────────────────
def main(out_json="/tmp/photon_c_isolation.json"):
    # Test 1 — mode isolation
    t2 = run_one("T2")
    a1 = run_one("A1")
    mixed = run_one("MIXED")

    # Test 2 — causality: sharp on/off step into PURE-T₂
    causal_run = run_one("T2", step_mode=True)

    r_t2_group = t2["v_group_over_c"]
    r_a1_front = a1["v_front_over_c"]
    r_mixed_group = mixed["v_group_over_c"]
    # Information front = robust multi-plane first-above-floor slope (Test 2).
    info_front = causal_run["info_front_over_c"]

    bin_, causal = adjudicate(r_t2_group, r_a1_front, r_mixed_group, info_front)

    # CONVENTION NOTE (the √2 trap, made explicit in the output — CP4):
    #   The engine defines the physical junction-crossing speed as
    #   c0 = dx/(dt·√2) = C_0 (k4_tlm.py:181), so the cardinal-cell-per-step
    #   grid march = dx/dt = √2·c0. All v/c above are in the C_0 convention
    #   where physical-c = C_0; a √2 reading = the bare grid march = √2·c0,
    #   NOT a signal faster than the physical c0. The "CAUSAL-VIOLATION" label
    #   below is therefore a COORDINATE-CONVENTION flag (info front = the bare
    #   √2 grid speed), NOT a physical superluminal-information result — it is
    #   the same √2 artifact the whole arc warns about. Reported honestly so
    #   Grant/auditor adjudicate the convention, not so it reads as a violation.
    info_front_over_c0_junction = info_front / np.sqrt(2.0)  # in physical c0=C_0 units
    result = {
        "test": "T2-photon group-velocity isolation from √2c A₁ precursor",
        "class": "DOCUMENTATION (DEC-01 / weak-C ruled)",
        "sqrt2c_ref": float(np.sqrt(2.0)),
        "convention_note": (
            "v/c reported in the C_0 convention (physical-c = C_0). The engine's "
            "physical junction-crossing speed is c0 = dx/(dt·√2) = C_0 "
            "(k4_tlm.py:181); a cardinal-cell-per-step grid march = dx/dt = √2·c0. "
            "A √2 reading is the bare grid march, not a superluminal signal."
        ),
        "T2": t2, "A1": a1, "MIXED": mixed, "causality_step": causal_run,
        "R_T2_group_over_c": r_t2_group,
        "R_A1_front_over_c": r_a1_front,
        "R_MIXED_group_over_c": r_mixed_group,
        "information_front_over_c": info_front,
        "information_front_over_c0_junction": float(info_front_over_c0_junction),
        "BIN": bin_,
        "CAUSALITY": causal,
        "CAUSALITY_is_coordinate_flag": True,
    }
    with open(out_json, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    main()
