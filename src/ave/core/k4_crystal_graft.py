"""
K4 Crystal Graft — the c_eff(V) trap + the conserved ADD-2 converter ON the
K4 4-port (V_inc, V_ref) WINDING carrier
=========================================================================

The arc converged here. Three pieces were individually validated on the SCALAR
Master-Equation bulk (`crystal_engine.py`, Outcome C,
`research/2026-06-09_crystal-engine_result.md`):
  WALL      = c_eff(V) = c0·(1−A²)^(−1/4) bulk-trap → Γ-wall breather.
  CONVERTER = the conserved gyrotropic shear→bulk coupling (ADD-2), the I4₁32
              chirality's transverse↔longitudinal coupling; energize-LOCK, no pump.
  CHARGE    = helicity transfer (sign-flips with chirality).
But the SCALAR bulk has NO multi-component U(1)-fibre to wind (w_tor=w_pol=0).
The winding lives in the K4 4-port (V_inc, V_ref) PHASE-space (A46) — the genesis-24
carrier. THE GRAFT puts the WALL + the SOURCE onto that carrier.

THE HARD PART (and its resolution — a load-bearing finding):
  The K4 connect is FIXED-SPEED np.roll (`k4_tlm.py:378-383`): every wave packet
  advances exactly one diamond-bond per dt — the lattice LIGHT-CONE, the MAXIMUM
  speed. c_eff(V)=c0·(1−A²)^(−1/4) DIVERGES in the saturated core. You CANNOT roll
  faster than the light-cone on a fixed-dt explicit lattice (causality/CFL). So
  c_eff→∞ is NOT representable as a faster transport. BUT c_eff→∞ ⟺ refractive
  index n=c0/c_eff→0 ⟺ a STOPBAND ⟺ TOTAL REFLECTION at the core boundary — and a
  reflective stopband IS representable on the fixed-roll lattice as a BOND IMPEDANCE
  reflection. Op14 already gives the identical law z_local=Z_eff/Z_0=(1−A²)^(−1/4)
  (`k4_tlm.py:291-294`); a wave entering the high-impedance saturated core sees
  Γ_bond=(z−1)/(z+1)→+1 (an open-circuit hard wall) and reflects. The variable
  wave-speed manifests as REFLECTION, not variable roll. This is the physically
  correct TLM encoding of a refractive medium (impedance loading, not retiming the
  connect). genesis-24 had op3_bond_reflection=True yet relaxed to Γ→0/matched
  because Flag-5e-A left K4 strain = V_inc/V_SNAP_SI ≈ 10⁻⁶ → saturation DORMANT.
  THE FIX: pass V_SNAP = V_yield (engine natural units) so the saturation engages.

THE CONVERTER on the K4 (single-integrator, conservative-by-construction):
  The crystal engine's ADD-2 is "a conservative velocity-space rotation localized at
  the saturation FRONT … rotates the velocity pair by a chirality-signed angle θ_χ =
  κ̃·h·g_front, which CONSERVES the pair norm EXACTLY (an orthogonal rotation)"
  (`crystal_engine.py:33-37`). The K4-NATIVE rendering: rotate the post-scatter
  4-port vector V_ref in PORT-space, at the front, in the (monopole ⊗ chiral-
  transverse) plane, by θ_χ = κ̃·h·g_front, chirality-signed by the A/B sublattice
  (the I4₁32 handedness). An orthogonal rotation CONSERVES |V_ref|² per node EXACTLY
  → energize-LOCK by construction (NO detonation is possible: the rotation is bounded
  ‖R‖=1). At h=0 (centrosymmetric) θ=0 → identity → the converter sources EXACTLY
  zero (the parity-odd selection rule). κ̃ = 6/5 = pq/(p+q) is the (2,3) topology —
  α-FREE. The monopole e0=(1,1,1,1)/2 is the LONGITUDINAL bulk ("3" / electron); the
  transverse Hadamard modes e1,e2 are the chiral photon carrier (the K4's native
  twist). The converter energizes the bulk monopole from the chiral photon at the
  front (closes GAP-1) and conserves (closes genesis-24's detonation).

CANONICAL-AVE-ONLY (Grant 2026-06-09): the electron is the LONGITUDINAL bulk monopole
mode of the K4; the photon is the transverse chiral port mode; absorb/emit = Axiom-4
crystallize/melt via the front converter. No QED/Maxwell-vector framing.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import R_II
from ave.core.k4_tlm import K4Lattice3D

# ── Port-space orthonormal basis (the tetrahedral T-symmetry modes) ──────────
# e0 = monopole (LONGITUDINAL bulk "3" / electron). e1,e2,e3 = the transverse
# Hadamard / chiral modes (the photon carrier). Columns are orthonormal:
#   e0 = (+,+,+,+)/2   e1 = (+,+,-,-)/2   e2 = (+,-,+,-)/2   e3 = (+,-,-,+)/2
# Note e2 = (v_right − v_left)/2 with v_right=V0+V2, v_left=V1+V3 — the helicity-
# difference mode the K4's get_helicity_density reads.
_HADAMARD = 0.5 * np.array(
    [
        [1.0, 1.0, 1.0, 1.0],  # e0  monopole / bulk
        [1.0, 1.0, -1.0, -1.0],  # e1  transverse
        [1.0, -1.0, 1.0, -1.0],  # e2  transverse (helicity-difference)
        [1.0, -1.0, -1.0, 1.0],  # e3  transverse
    ],
    dtype=np.float64,
)


class K4CrystalGraft:
    """The c_eff(V) bond-trap + the conserved ADD-2 port-rotation converter on the
    K4 4-port (V_inc, V_ref) winding carrier. Single K4 scatter+connect integrator;
    the converter is inserted between scatter and connect (CP10 front-localized)."""

    def __init__(
        self,
        N: int,
        V_yield: float = 1.0,
        kappa_tilde: float = 6.0 / 5.0,
        converter_on: bool = True,
        pml_thickness: int = 4,
        front_center: float = R_II,
        front_width: float = 0.18,
        helicity: float = 1.0,
    ):
        self.N = int(N)
        self.V_yield = float(V_yield)
        self.kappa_tilde = float(kappa_tilde)
        self.converter_on = bool(converter_on)
        self.front_center = float(front_center)
        self.front_width = float(front_width)
        self.helicity = float(helicity)

        # The carrier + the WALL: op3_bond_reflection renders Op14 z_local as bond Γ;
        # V_SNAP=V_yield (engine units) is the Flag-5e-A fix that genesis-24 missed.
        self.k4 = K4Lattice3D(
            nx=N,
            ny=N,
            nz=N,
            dx=1.0,
            nonlinear=False,
            pml_thickness=pml_thickness,
            op3_bond_reflection=True,
            V_SNAP=self.V_yield,
        )
        # Natural units (c=1, dx=1, dt=1/√2) so the carrier shares the engine clock.
        self.k4.c = 1.0
        self.k4.dt = 1.0 / np.sqrt(2.0)
        self.k4.tau_relax = 1.0
        self.dt = self.k4.dt
        self.pml_thickness = int(pml_thickness)

        # Chirality sign per site from the A/B sublattice (the I4₁32 handedness):
        # +1 on A, −1 on B. This is what makes the converter parity-odd natively.
        self.chi_sign = np.where(self.k4.mask_A, 1.0, np.where(self.k4.mask_B, -1.0, 0.0))

        # ledger bookkeeping
        self.converter_residual = 0.0  # Σ |per-node norm change| (orthogonal ⇒ ≈0)
        self.step_count = 0
        self.time = 0.0

    # ----------------------------------------------------------- masks/strain
    def interior_mask(self) -> np.ndarray:
        """PML-excluded interior (A-Rule 10 corollary)."""
        p = self.pml_thickness
        i, j, k = np.indices((self.N, self.N, self.N))
        return (i >= p) & (i < self.N - p) & (j >= p) & (j < self.N - p) & (k >= p) & (k < self.N - p)

    def strain_field(self) -> np.ndarray:
        """A = |V_inc| / V_yield per node — the saturation strain (drives the wall)."""
        v_tot = np.sqrt(np.sum(self.k4.V_inc**2, axis=-1))
        return v_tot / self.V_yield

    def _front_window(self) -> np.ndarray:
        """g_front(A): the saturation-FRONT shell (peaks at A≈R_II=√3/2, the Non-
        Linear→Saturated boundary). Zero in vacuum (A→0) and in the frozen core
        (A→1). CP10 boundary-localized — NOT a bulk-volume coupling."""
        A = self.strain_field()
        return np.exp(-((A - self.front_center) ** 2) / (2.0 * self.front_width**2))

    # ------------------------------------------------------------- ADD-2
    def _apply_converter(self) -> None:
        """The conserved gyrotropic shear→bulk converter (ADD-2), K4-native.

        Rotate the post-scatter 4-port V_ref in PORT-space, at the front, in the
        (monopole e0 ⊗ chiral-transverse e2) plane, by the chirality-signed angle
            θ(r) = κ̃ · h · χ_sign(r) · g_front(r),
        where h is the seeded photon helicity and χ_sign=±1 is the A/B sublattice
        handedness. An orthogonal rotation CONSERVES |V_ref|² per node EXACTLY
        (energize-LOCK, no pump). At h=0 ⇒ θ=0 ⇒ identity ⇒ sources exactly zero
        (the parity-odd selection rule). Energizes the bulk monopole from the chiral
        photon mode at the front (closes GAP-1)."""
        if not self.converter_on or abs(self.helicity) < 1e-30:
            return
        g = self._front_window()
        theta = self.kappa_tilde * self.helicity * self.chi_sign * g  # (N,N,N)
        # Project V_ref onto the Hadamard basis: a = E · V_ref  (per node)
        Vr = self.k4.V_ref  # (N,N,N,4)
        a = np.einsum("mp,...p->...m", _HADAMARD, Vr)  # (N,N,N,4) mode amplitudes
        m0 = a[..., 0].copy()  # monopole (bulk)
        t2 = a[..., 2].copy()  # chiral transverse
        ct, st = np.cos(theta), np.sin(theta)
        a[..., 0] = ct * m0 - st * t2
        a[..., 2] = st * m0 + ct * t2
        # Reconstruct: V_ref = Eᵀ · a  (E orthogonal ⇒ Eᵀ=E here; |V_ref|² conserved)
        Vr_new = np.einsum("mp,...m->...p", _HADAMARD, a)
        # Track the per-node norm residual (the energize-LOCK proof: ≈0 to fp).
        before = np.sum(Vr**2, axis=-1)
        after = np.sum(Vr_new**2, axis=-1)
        self.converter_residual += float(np.sum(np.abs(after - before)))
        self.k4.V_ref = np.where(self.k4.mask_active[..., None], Vr_new, self.k4.V_ref)

    # --------------------------------------------------------------- step
    def step(self) -> None:
        """One K4 outer step: scatter → [front converter rotation] → connect.
        The c_eff wall lives in connect (the op3 bond Γ from z_local computed in
        scatter); the converter is the front-localized conservative rotation."""
        self.k4._scatter_all()  # V_ref = S·V_inc ; updates z_local from |V_inc|
        self._apply_converter()  # ADD-2 conserved rotation at the front
        self.k4._connect_all()  # bond Γ (the c_eff wall) + np.roll transport
        self.k4.timestep += 1
        self.step_count += 1
        self.time += self.dt

    # ------------------------------------------------------------- seeding
    def seed_bulk(self, center, sigma, frac):
        """Saturated LONGITUDINAL bulk seed = a 'Lane-1' mass already present (CP8
        precursor — the pre-compressed medium the photon nucleates ON). Sets the
        MONOPOLE port component (e0) of V_inc to a sech blob of depth A=frac."""
        cx, cy, cz = center
        i, j, k = np.indices((self.N, self.N, self.N))
        r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
        env = frac * self.V_yield / np.cosh(r / sigma)
        # monopole e0=(1,1,1,1)/2 ⇒ each port gets env/2 so |V_inc| = env.
        add = (env * 0.5)[..., None] * np.ones(4)
        self.k4.V_inc += np.where(self.k4.mask_active[..., None], add, 0.0)

    def seed_photon(self, center, sigma, wavelength, amplitude, helicity=1.0, k_wind=2):
        """Transverse CHIRAL photon (CP8 precursor; NOT a planted knot). Excites the
        transverse Hadamard modes (e1,e2) of V_inc with a circular polarization and
        an azimuthal winding k_wind, so the converter has a handed, winding substrate
        to imprint. Propagates the chirality h via `helicity` (sets the converter's
        rotation SENSE → matter vs antimatter)."""
        self.helicity = float(helicity)
        cx, cy, cz = center
        i, j, k = np.indices((self.N, self.N, self.N))
        r2 = (i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2
        env = amplitude * np.exp(-r2 / (2.0 * sigma**2))
        kk = 2.0 * np.pi / wavelength
        s = i - cx  # propagation along x
        azi = np.arctan2(j - cy, i - cx)  # azimuth for the winding
        # circular polarization in the (e1,e2) transverse plane, with k_wind winding
        c1 = env * np.cos(kk * s + k_wind * azi)
        c2 = env * helicity * np.sin(kk * s + k_wind * azi)
        # map (c1,c2) mode amplitudes back to ports: V += c1·e1 + c2·e2
        add = c1[..., None] * _HADAMARD[1] + c2[..., None] * _HADAMARD[2]
        self.k4.V_inc += np.where(self.k4.mask_active[..., None], add, 0.0)

    # ----------------------------------------------------- phase-space (A46)
    def chiral_phasor(self):
        """The native (V_inc, V_ref) chiral U(1)-fibre phasor — the MULTI-COMPONENT
        carrier the scalar bulk LACKED. Reduce the 4-port V_inc / V_ref onto the two
        transverse Hadamard modes (e1,e2): the complex order parameter is
            ψ_inc = ⟨V_inc,e1⟩ + i⟨V_inc,e2⟩ ,   ψ_ref = ⟨V_ref,e1⟩ + i⟨V_ref,e2⟩ .
        Returns (vinc_x, vinc_y, vref_x, vref_y) real 3D arrays. The winding of ψ
        around a real-space torus contour IS the (2,3) (A46 Clifford-torus coordinate
        — phase-space, NOT real-space R/r)."""
        a_inc = np.einsum("mp,...p->...m", _HADAMARD, self.k4.V_inc)
        a_ref = np.einsum("mp,...p->...m", _HADAMARD, self.k4.V_ref)
        m = self.k4.mask_active
        vinc_x = a_inc[..., 1] * m
        vinc_y = a_inc[..., 2] * m
        vref_x = a_ref[..., 1] * m
        vref_y = a_ref[..., 2] * m
        return vinc_x, vinc_y, vref_x, vref_y

    def bulk_monopole(self) -> np.ndarray:
        """The LONGITUDINAL bulk amplitude per node = ⟨V_inc, e0⟩ (the electron '3').
        This is the real-space-localizable trapped object (the breather)."""
        a0 = np.einsum("mp,...p->...m", _HADAMARD, self.k4.V_inc)[..., 0]
        return a0 * self.k4.mask_active

    # ----------------------------------------------------- the Γ wall
    def gamma_core(self) -> dict:
        """The c_eff WALL on the K4: the bond reflection Γ_bond=(z_B−z_A)/(z_B+z_A)
        at the saturated-core boundary (z_local=(1−A²)^(−1/4)→∞ in the core). The
        deepest |Γ| at the interior impedance step is the wall strength. genesis-24's
        coupled engine relaxed to |Γ|<0.08 (matched, no trap, Flag-5e-A dormant);
        the engaged saturation here drives |Γ|→1 (total reflection = bound state).

        Sign convention: the K4 tracks the VOLTAGE wave, so a high-impedance core is
        an OPEN circuit ⇒ Γ→+1 (vs the crystal engine's velocity-wave Γ→−1 short).
        Both are |Γ|→1 total reflectors — the SAME wall, dual descriptions. The
        load-bearing discriminator is |Γ|→1 (bound) vs genesis-24's |Γ|→0 (matched)."""
        self.k4._update_z_local_field()
        z = self.k4.z_local_field
        m = self.interior_mask() & self.k4.mask_active
        # bond Γ across each port direction (use port-0 A→B vector as representative)
        port_shifts = [(-1, -1, -1), (-1, 1, 1), (1, -1, 1), (1, 1, -1)]
        gmax = 0.0
        gsigned = 0.0
        for sh in port_shifts:
            z_nb = np.roll(z, shift=sh, axis=(0, 1, 2))
            g = (z_nb - z) / (z_nb + z + 1e-12)
            gi = g[m]
            if gi.size and np.max(np.abs(gi)) > gmax:
                gmax = float(np.max(np.abs(gi)))
                gsigned = float(gi[np.argmax(np.abs(gi))])
        z_core = float(z[m].max()) if m.any() else 1.0
        return {
            "gamma_core_abs": gmax,
            "gamma_core_signed": gsigned,
            "z_core_max": z_core,
            "frac_reflective": float((np.abs(z[m] - 1.0) > 0.1).mean()) if m.any() else 0.0,
        }

    # ----------------------------------------------------------- ledger
    def field_intensity(self) -> dict:
        """Boundedness monitor (PML-excluded) — the genesis-24-comparable detonation
        gate (genesis-24's EMF pump detonated max|V_inc|→1.08e4 / E_V→6.8e8)."""
        m = self.interior_mask() & self.k4.mask_active
        Vi = self.k4.V_inc[m]
        Vr = self.k4.V_ref[m]
        return {
            "EV_field": float(np.sum(Vi**2)),
            "max_V": float(np.max(np.abs(Vi))) if Vi.size else 0.0,
            "max_Vref": float(np.max(np.abs(Vr))) if Vr.size else 0.0,
        }

    def interior_energy(self) -> float:
        """E = Σ_interior (V_inc² + V_ref²) — the trapped-bulk energy proxy = latent
        heat = candidate mₑc² (PML-excluded). For the bound-state-persistence check."""
        m = self.interior_mask()[..., None]
        return float(np.sum((self.k4.V_inc**2 + self.k4.V_ref**2) * m))

    def helicity_charge(self) -> float:
        """Integrated K4 helicity (native get_helicity_density) over the interior =
        the conserved CHARGE (sign = handedness). charge=helicity flips with the
        seeded photon helicity."""
        h = self.k4.get_helicity_density() * self.interior_mask()
        return float(h.sum())

    def spin_L(self) -> float:
        """|L| = |∫ r×(helicity-current)| proxy — the conserved angular momentum.
        Energize-LOCK ⇒ bounded; genesis-24's pump ⇒ |L|~t (2.7→43)."""
        # use the helicity-difference transverse mode flux as the circulating current
        a = np.einsum("mp,...p->...m", _HADAMARD, self.k4.V_inc)
        jx, jy = a[..., 1] * self.k4.mask_active, a[..., 2] * self.k4.mask_active
        i, j, k = np.indices((self.N, self.N, self.N))
        c = (self.N - 1) / 2.0
        rx, ry = (i - c), (j - c)
        Lz = np.sum((rx * jy - ry * jx) * self.interior_mask())
        return float(abs(Lz))

    def phi_link_state(self) -> float:
        """The L-state of the reactance pair (CP6): Σ |Φ_link| over the interior.
        Read alongside V_inc (the C-state) every step — a single-phase snapshot can't
        distinguish a static trap from an oscillator at peak (CP6)."""
        m = self.interior_mask()[..., None]
        return float(np.sum(np.abs(self.k4.Phi_link) * m))

    def __repr__(self):
        return (
            f"K4CrystalGraft(N={self.N}, dt={self.dt:.4f}, kappa_tilde={self.kappa_tilde}, "
            f"V_yield={self.V_yield}, converter_on={self.converter_on}, step={self.step_count})"
        )
