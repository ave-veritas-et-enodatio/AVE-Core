# Double-Slit Dark-Wake on the K4-TLM Substrate — Pre-Reg / Build Brief

Status: BUILD (Option (i): imposed-trajectory mechanism animation)
Branch: `viz/double-slit-ave`
Driver: `src/scripts/vol_1_foundations/k4tlm_double_slit_dark_wake.py`
Result doc: `research/2026-06-04_k4tlm-double-slit-darkwake-result.md`

## 1. Mechanism (canonical, honest)

A moving localized transverse source traces an electron-defect trajectory toward
the slit plane. Its **real K4-TLM transverse wake** (the radiated V-sector field)
spreads and passes through **both** slits, producing real-space interference on a
downstream screen plane.

- **Panel A — no observer:** coherent wake through both slits -> `|E|^2` fringes.
- **Panel B — observer at slit 2:** a local Ohmic / Gamma-mismatch impedance load
  (`Z_det`) at slit 2 thermalizes the wake throughput there, so the screen
  pattern collapses toward the single-slit diffraction envelope -> fringe
  visibility drops **continuously** (not binary).

Canonical mechanism leaf (on `main`):
`manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md`
(defect through one slit; continuous transverse wake through both; Ohmic detector
at slit 2 thermalizes phase energy -> decoherence; Born rule
`P(click|x) = |dt A(x)|^2 / integral|dt A|^2`).

Consolidated EE leaves `double-slit-ee-mapping.md` + `photon-ee-mapping.md` are on
**PR #85, NOT yet on main** — cited by canonical path, pending-merge.

## 2. Honest-framing note (load-bearing — on the figure + in the result doc)

> Dark-wake mechanism on the K4-TLM substrate; the defect TRAJECTORY is imposed;
> the transverse wake, the interference fringes, and the Gamma-mismatch which-path
> decoherence are real engine physics.

NOT claimed: a from-scratch emergent or free-propagating electron (that is the
separate option-(ii) probe). The moving object is NOT a "helical photon" — that
dual-sector framing is retracted at
`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`
("Doc 105's dual-sector helical-photon framing ... is empirically wrong ... The
canonical photon is single-sector").

**CP5 note (substrate-native-check):** the trajectory is imposed (moving source)
BECAUSE a Gamma=-1 self-trapped core has `c_local -> 0` and cannot free-propagate;
the free-propagation question is the separate option-(ii) probe, not this build.

## 3. STEP-0 engine-API findings (`src/ave/core/k4_tlm.py`, `photon_propagation.py`)

All confirmed by live-fire smoke runs before writing the driver (Rule 10).

**(a) Thin 2D slab — CONSTRAINT.** `K4Lattice3D(nx,ny,nz,...)` runs as a thin-z
slab, BUT the sponge PML (`__init__` ~:227-235) is **isotropic** — it damps in x,
y, AND z. With `pml_thickness=P`, a thin slab needs `nz >= 2*P + a few` or the
ENTIRE z-extent is inside the z-PML and the field decays to ~0 (verified: `nz=8,
P=8` -> 0 interior z-layers, energy -> 1e-18 by step 100). Locked: `nz=24, P=8`
-> 8 interior z-layers at `pml_mask~1.0`. Sample/inject in the interior z-band
`zc-3..zc+3` with `zc=nz//2`.

**(b) Transverse T_2 source.** Two viable injectors:
  - Forward-port T_2 plane/line: weights `(-1/2,-1/2,+1/2,+1/2)*1/sqrt2` for +x
    (`photon_propagation.forward_port_weights`, A_1-projected, `sum(w)=0`). This
    is COLLIMATED — a beam, not a fan. Verified: a forward-T_2 line source does
    NOT illuminate two well-separated slits (wall slit-balance ~0.00); unusable
    for Young geometry from a single emitter.
  - **Isotropic `inject_point_source(x,y,z,amp)` (`:516`)** — adds `amp/2` to all
    4 ports of one active node -> a radiating (cylindrical-in-slab) wake that DOES
    illuminate both slits. **This is the locked injector** (an oscillating point
    emitter upstream of the wall). It excites both A_1 and T_2, but at linear-
    vacuum amplitude this is a faithful radiated V-sector wake; the screen
    observable is the transverse `|E|^2` interference, which is what the canonical
    leaf measures.

**(c) Slit WALL.** Deactivate wall cells: set `mask_active=False`, `mask_A=False`,
`mask_B=False` at the wall column (3 cells thick in x, full z) with two y-gaps for
the slits. Deactivated cells force `V_ref=0` (`_scatter_all` :349 `V_ref[~mask_active]=0`)
and receive nothing in `_connect_all` (only `mask_A`/`mask_B` sites get `new_inc`)
-> a perfect (non-absorbing) reflector. Verified: wake passes only through the
slit apertures; downstream interference appears.

**(d) Sponge PML.** `pml_thickness=8`. `_connect_all` :440-457 severs the
np.roll wrap so the domain is a true bounded box, not a torus. Screen/intensity
sampling EXCLUDES PML cells (`P <= i,j,k <= N-P-1`) per A-Rule 10 / CP7.

**(e) Anisotropic kinematics (load-bearing for the forward-prediction).** Per
`photon_propagation.py` docstring + `constants.py:497`: cardinal-axis (+x)
propagation is at `c*sqrt(2)` (A_1/longitudinal) / `c` (T_2/transverse); the
wavelength in CELLS for a carrier `omega = 2*pi*c/(lambda_cells*dx)` set from the
isotropic `c` is `lambda_cells` along the wavefront. The Fraunhofer prediction
uses `lambda_cells` directly (the cell-pitch wavelength of the radiated wake).

**(f) E ~ (V_inc + V_ref) screen observable.** Per the canonical Lagrangian
(`L = 1/2 eps0 |dt A|^2 - ...`), `E ~ -dt A ~ (V_inc + V_ref)`. Screen observable
= time-averaged `sum_ports (V_inc + V_ref)^2` over the interior z-band (squared ->
A/B sublattice-sign-clean). Verified to give cleaner fringes than the raw
`get_energy_density()` (= `sum(V_inc^2 + V_ref^2)`); both give the same washout
physics. **`|E|^2 = sum(V_inc+V_ref)^2` is the locked screen observable** (it is
the `|dt A|^2` of the canonical Born-rule leaf).

**Locked configuration:** `NX=200, NY=140, NZ=24, PML=8`; isotropic oscillating
point emitter at `(x_src=16, y=NY/2, z=NZ/2)`; wall at `x=80` (3 cells thick),
`slit_sep=30`, `slit_w=3`; carrier `lambda_cells=8`; `amp=0.05*V_SNAP = 25.55 kV
< V_YIELD = 43.65 kV` (Axiom 4 dormant, linear vacuum, `nonlinear=False`);
observer = Ohmic `(1-Z_det)` multiplicative load on `V_inc` AND `V_ref` over the
slit-2 aperture + downstream throughput cells; screen at `x=NX-PML-12=180`;
time-average over the second half of the run.

## 4. Forward-predicted fringe spacing (ave-driver-script-honesty: PREDICT, no fit)

Fraunhofer (small-angle) two-slit fringe spacing:

    Delta_y = lambda_cells * L / d

with `lambda_cells = 8` (wake cell-pitch wavelength), `d = slit_sep = 30` cells,
`L = screen_x - wall_x = 180 - 80 = 100` cells:

    Delta_y_predicted = 8 * 100 / 30 = 26.7 cells

This is stated BEFORE the production render. The geometry is near-field-ish
(L/d ~ 3.3), so the small-angle Fraunhofer value is an approximation; the result
doc reports predicted vs observed and the residual is attributed to near-field
curvature, NOT tuned away. (STEP-0 smoke at `lambda=8, d=30, L=100` gave 3 screen
peaks with ~28-cell spacing -> consistent with the 26.7 prediction to within the
near-field tolerance.)

**Visibility prediction (which-path).** No observer -> two-slit pattern, high
visibility. Observer (Ohmic load at slit 2) -> pattern collapses toward the
single-slit diffraction envelope of slit 1 alone. STEP-0 smoke (|E|^2 observable):
two-slit V=0.92, single-slit V=0.72, observer V=0.72 (lands on single-slit, as the
mechanism predicts). The washout is **continuous** in `Z_det` (V: 0.895 -> 0.878
-> 0.828 over `Z_det` strength 0 -> 0.3 -> 0.6), i.e. dark-wake/Born-continuous,
NOT Copenhagen-binary. Visibility-vs-Z_det is the optional fourth deliverable.

## 5. Auditor queue

- [ ] Confirm `|E|^2 = sum(V_inc+V_ref)^2` is the right `|dt A|^2` proxy vs the
      canonical Lagrangian (the `1/2 eps0 |dt A|^2` kinetic term -> `E = -dt A`,
      so `|dt A|^2 ~ |E|^2`; sign/normalization not load-bearing for fringe
      geometry or visibility).
- [ ] Confirm the isotropic `inject_point_source` wake (A_1 + T_2 mixed) is an
      acceptable stand-in for the defect's radiated transverse wake in this
      MECHANISM-illustration build, given that a pure-T_2 forward beam cannot
      illuminate two separated slits from a single emitter (documented STEP-0
      constraint). The interference + decoherence physics measured on-screen is
      the transverse `|E|^2`, which is photon-sector regardless.
- [ ] Honest-caption present on figure + result doc (imposed trajectory; real
      wake/fringes/decoherence). Not "helical photon"; not free-propagating
      electron.
- [ ] PR #85 EE leaves (`double-slit-ee-mapping.md`, `photon-ee-mapping.md`) cited
      by canonical path with pending-merge note; re-point to live path post-merge.
- [ ] Forward-predicted Delta_y = 26.7 cells stated before render; observed
      reported with near-field residual, not tuned.
