"""
Crystal Engine — the State-C elastodynamic graft for electron-genesis
=====================================================================

Implements the design prereg
`research/2026-06-09_crystal-engine-elastodynamic-graft_design-prereg.md`:
a three-branch chiral micropolar (I4₁32) crystal that hosts the electron as a
self-assembled, trapped LONGITUDINAL bulk-modulus acoustic resonance born by
TRANSVERSE-SHEAR → LONGITUDINAL-BULK mode conversion.

NO-QED rule (Grant directive 2026-06-09): the trapped electron is the
LONGITUDINAL bulk mode (the "3"), NOT a self-trapped transverse photon.
Absorb/emit = the Axiom-4 crystallize/melt (saturate/desaturate) cycle.

Two branches are integrated here (the third, microrotation, is mass-gapped and
enters only as the helicity carrier of the shear seed):

  (2) LONGITUDINAL BULK  V  — the electron / the "3". Governed by the validated
      scalar Master Equation (`master_equation_fdtd.py`): c_eff(V)=c0·(1-A²)^(-1/4)
      → ∞ in the saturated core, self-creating the Γ=-1 TIR wall. THE BULK-TRAP.
      v14 Mode I PASS (`two-engine-architecture-a027.md:32-37`).
  (1) TRANSVERSE SHEAR   w  — the photon (Cosserat shear). Linear vector wave at
      c_T, mechanically blind to the bulk. Carries helicity h (the chirality).

Branch speeds are TIED by the substrate Poisson ratio ν_vac=2/7 at the canonical
K=2G operating point (NOT free knobs, `ave-fundamental-ground-up-implementation`):
    c_L²/c_T² = 2(1-ν)/(1-2ν) = (K + 4G/3)/G |_{K=2G} = 10/3   (DERIVED).

ADD-2 (the one new primitive — closes GAP-1, the genesis-23/24 dead ω→V source):
the chiral shear→bulk CONVERTER = the I4₁32 chirality's gyrotropic transverse↔
longitudinal coupling (Grant adjudication 2026-06-09: AXIOM CONSEQUENCE — engine-
completeness of Axiom 1's non-centrosymmetry, NOT a new postulate). Rendered as a
CONSERVATIVE velocity-space rotation localized at the saturation FRONT
(substrate-native-check CP10 boundary-not-bulk; ave-conserved-vs-pumped energize-
LOCK): per cell it rotates the velocity pair (∂_t V, ∂_t w_chiral) by a chirality-
signed angle θ_χ = κ̃·h·g_front, which CONSERVES (∂_t V)²+(∂_t w_χ)² EXACTLY (an
orthogonal rotation). It ENERGIZES the bulk from the photon (∂_t V grows from a
nonzero shear velocity even at V≡0) and LOCKS (the rotation is bounded; the c_eff
wall confines) — the opposite of genesis-24's one-way EMF pump that detonated
(E_V: 7→6.8e8, |L| unbounded). Coupling κ̃=6/5=pq/(p+q) is the (2,3) topology —
α-FREE (NOT κ_chiral=1.2α); chirality sign h selects matter vs antimatter.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import NU_VAC, R_II


class CrystalEngine:
    """Two-branch chiral elastodynamic crystal (bulk V ⊗ shear w) + conserved
    gyrotropic converter. Leapfrog FDTD, engine-natural (α-free) units."""

    def __init__(
        self,
        N: int,
        dx: float = 1.0,
        V_yield: float = 1.0,
        c0: float = 1.0,
        cfl_safety: float = 0.30,
        pml_thickness: int = 4,
        A_cap: float = 0.99,
        S_min: float = 0.05,
        kappa_tilde: float = 6.0 / 5.0,
        converter_on: bool = True,
        front_center: float = R_II,
        front_width: float = 0.18,
    ):
        """
        Args mirror MasterEquationFDTD where shared (the bulk branch IS that
        validated engine). New:
            kappa_tilde:  the (2,3) topological converter coupling pq/(p+q)=6/5
                          (α-FREE — the chord route; NOT κ_chiral=1.2α).
            converter_on: master switch for ADD-2 (False ⇒ bare two-branch
                          baseline / centrosymmetric κ_χ→0 limit).
            front_center: A-value of the saturation front where the converter
                          acts (R_II=√3/2, the Non-Linear→Saturated boundary;
                          CP10 boundary-localized, NOT a bulk-volume coupling).
            front_width:  Gaussian half-width of that shell in A-units.
        """
        self.N = int(N)
        self.dx = float(dx)
        self.V_yield = float(V_yield)
        self.c0 = float(c0)  # the bulk (longitudinal) speed c_L
        self.A_cap = float(A_cap)
        self.S_min = float(S_min)
        self.kappa_tilde = float(kappa_tilde)
        self.converter_on = bool(converter_on)
        self.front_center = float(front_center)
        self.front_width = float(front_width)

        # Branch speeds tied by ν_vac=2/7 at K=2G (DERIVED, not knob-set).
        # c_L²/c_T² = 2(1-ν)/(1-2ν) = 10/3 at ν=2/7.
        self.cL2_over_cT2 = 2.0 * (1.0 - NU_VAC) / (1.0 - 2.0 * NU_VAC)
        self.c_T = self.c0 / np.sqrt(self.cL2_over_cT2)  # transverse shear speed

        # CFL governed by the FASTER branch under saturation: c_eff_max = c0/√S_min.
        c_eff_max = self.c0 / np.sqrt(self.S_min)
        self.dt = cfl_safety * self.dx / (c_eff_max * np.sqrt(3.0))

        # State — bulk scalar V (the "3") and transverse shear 3-vector w (photon)
        Nn = self.N
        self.V = np.zeros((Nn, Nn, Nn), dtype=np.float64)
        self.V_prev = np.zeros((Nn, Nn, Nn), dtype=np.float64)
        self.w = np.zeros((Nn, Nn, Nn, 3), dtype=np.float64)
        self.w_prev = np.zeros((Nn, Nn, Nn, 3), dtype=np.float64)

        # helicity of the seeded photon (set by seed_photon); chirality selector
        self.helicity = 1.0

        self.pml_thickness = int(pml_thickness)
        self._build_damping_mask()

        # energy-ledger bookkeeping (the conserved-vs-pumped guard, CP6/ledger)
        self.converter_work = 0.0  # Σ per-cell rotation residual (should ≈ 0)

        self.time = 0.0
        self.step_count = 0

    # ------------------------------------------------------------------ masks
    def _build_damping_mask(self):
        i, j, k = np.indices((self.N, self.N, self.N))
        d = np.minimum.reduce(
            [np.minimum(i, self.N - 1 - i), np.minimum(j, self.N - 1 - j), np.minimum(k, self.N - 1 - k)]
        )
        damping = np.ones((self.N, self.N, self.N), dtype=np.float64)
        if self.pml_thickness > 0:
            in_pml = d < self.pml_thickness
            atten = 1.0 - 0.05 * ((self.pml_thickness - d[in_pml]) / self.pml_thickness) ** 2
            damping[in_pml] = np.maximum(0.5, atten)
        self.damping = damping

    def interior_mask(self) -> np.ndarray:
        """PML-excluded interior (A-Rule 10 corollary — PML cells are frozen-
        absorbing artifact, never interior physics).

        CACHED (speedup, bit-identical): the mask depends only on N and
        pml_thickness, both fixed at construction and never mutated, so it is
        built once on first call and the SAME array returned thereafter. Every
        caller reads it (multiply / boolean-index) — none mutate it. getattr
        with a None default makes the cache work for every subclass without an
        __init__ change."""
        m = getattr(self, "_interior_mask_cache", None)
        if m is None:
            p = self.pml_thickness
            i, j, k = np.indices((self.N, self.N, self.N))
            m = (i >= p) & (i < self.N - p) & (j >= p) & (j < self.N - p) & (k >= p) & (k < self.N - p)
            self._interior_mask_cache = m
        return m

    # ------------------------------------------------------------ operators
    @staticmethod
    def _laplacian(F: np.ndarray, dx: float) -> np.ndarray:
        """7-point 2nd-order Laplacian on a scalar field (interior; boundary 0)."""
        L = np.zeros_like(F)
        L[1:-1, 1:-1, 1:-1] = (
            F[2:, 1:-1, 1:-1]
            + F[:-2, 1:-1, 1:-1]
            + F[1:-1, 2:, 1:-1]
            + F[1:-1, :-2, 1:-1]
            + F[1:-1, 1:-1, 2:]
            + F[1:-1, 1:-1, :-2]
            - 6.0 * F[1:-1, 1:-1, 1:-1]
        ) / (dx**2)
        return L

    @staticmethod
    def _laplacian_vec(F: np.ndarray, dx: float) -> np.ndarray:
        """7-point Laplacian over the 3 LEADING spatial axes of a (N,N,N,C)
        vector field, in one pass.

        BIT-IDENTICAL to looping ``_laplacian(F[..., c], dx)`` over the trailing
        component axis: same stencil, same float64 operands, same per-element
        op order (the arithmetic is component-independent), boundary left 0.
        Replaces the ``for comp in range(3)`` per-component calls in the vector
        (w, ω) sectors of step() — a speedup (fewer Python calls / temporaries),
        NOT a physics change."""
        L = np.zeros_like(F)
        L[1:-1, 1:-1, 1:-1, :] = (
            F[2:, 1:-1, 1:-1, :]
            + F[:-2, 1:-1, 1:-1, :]
            + F[1:-1, 2:, 1:-1, :]
            + F[1:-1, :-2, 1:-1, :]
            + F[1:-1, 1:-1, 2:, :]
            + F[1:-1, 1:-1, :-2, :]
            - 6.0 * F[1:-1, 1:-1, 1:-1, :]
        ) / (dx**2)
        return L

    def saturation_kernel(self, V: np.ndarray) -> np.ndarray:
        """S(A)=√(1-A²), A=|V|/V_yield, clipped to [S_min, 1] (the A-034 kernel)."""
        A = np.abs(V) / self.V_yield
        A = np.minimum(A, self.A_cap)
        return np.sqrt(np.maximum(1.0 - A**2, self.S_min**2))

    def c_eff_squared(self, V: np.ndarray) -> np.ndarray:
        """c_eff²(V)=c0²/S(A) — the bulk-trap (→∞ in the saturated core)."""
        S = self.saturation_kernel(V)
        return (self.c0**2) / np.maximum(S, self.S_min)

    def strain_field(self) -> np.ndarray:
        return np.abs(self.V) / self.V_yield

    def _front_window(self) -> np.ndarray:
        """g_front(r): the saturation FRONT shell where the gyrotropic mode-
        conversion engages — a thin band at A≈R_II (CP10 boundary, NOT a bulk
        volume). Zero in vacuum (A→0) and in the deep frozen core (A→1)."""
        A = self.strain_field()
        return np.exp(-((A - self.front_center) ** 2) / (2.0 * self.front_width**2))

    # ------------------------------------------------------------- ADD-2
    def _microrotation_x(self, w: np.ndarray) -> np.ndarray:
        """Ω_w = (∇×w)·n̂ along the photon propagation axis n̂=x̂ — the shear
        MICROROTATION about the propagation direction, the parity-odd helicity
        carrier the chiral coupling reads. (∇×w)_x = ∂_y w_z - ∂_z w_y."""
        wz_y = (np.roll(w[..., 2], -1, axis=1) - np.roll(w[..., 2], 1, axis=1)) / (2.0 * self.dx)
        wy_z = (np.roll(w[..., 1], -1, axis=2) - np.roll(w[..., 1], 1, axis=2)) / (2.0 * self.dx)
        return wz_y - wy_z

    def _converter_forces(self):
        """The chiral gyrotropic shear↔bulk coupling (ADD-2), derived from ONE
        Hamiltonian coupling term (NOT bolted on — Grant 2026-06-09: the I4₁32
        chirality's gyrotropic transverse↔longitudinal coupling, an AXIOM
        CONSEQUENCE / engine-completeness of Axiom-1 non-centrosymmetry):

            H_couple = γ ∫ g_front(r) · V · Ω_w  d³r,   γ = κ̃ = 6/5 (α-FREE),
                       Ω_w = (∇×w)·x̂  (the microrotation / helicity carrier).

        The EOM forces are the functional derivatives (provably conserve the
        TOTAL H = E_V + E_w + H_couple — the continuum cancellation is exact;
        ave-conserved-vs-pumped energize-LOCK, NOT a one-way pump):
            f_V    = -δH/δV    = -γ g Ω_w                 (sources V from shear —
                                                           NONZERO at V≡0 ⇒ closes
                                                           GAP-1 / bootstraps)
            f_w_z  = -δH/δw_z  = +γ ∂_y(g V)              (the reciprocal back-
            f_w_y  = -δH/δw_y  = -γ ∂_z(g V)               reaction onto the shear)
        g_front>0 ONLY at the saturation front (CP10 boundary, not bulk) — and
        g_front≈0 wherever V≈0, so a lone photon (no saturated seed) cannot
        bootstrap (reproduces genesis-23's null by construction)."""
        g = self._front_window()
        gV = g * self.V
        Omega_w = self._microrotation_x(self.w)
        f_V = -self.kappa_tilde * g * Omega_w
        f_w = np.zeros_like(self.w)
        d_gV_dy = (np.roll(gV, -1, axis=1) - np.roll(gV, 1, axis=1)) / (2.0 * self.dx)
        d_gV_dz = (np.roll(gV, -1, axis=2) - np.roll(gV, 1, axis=2)) / (2.0 * self.dx)
        f_w[..., 2] = +self.kappa_tilde * d_gV_dy
        f_w[..., 1] = -self.kappa_tilde * d_gV_dz
        return f_V, f_w

    def _coupling_energy(self) -> float:
        """H_couple = γ∫ g V Ω_w — the conversion ledger term (kept for the
        joint H = E_V + E_w + H_couple conservation check)."""
        g = self._front_window()
        Omega_w = self._microrotation_x(self.w)
        dens = self.kappa_tilde * g * self.V * Omega_w * self.interior_mask()
        return float(dens.sum())

    # --------------------------------------------------------------- step
    def step(self):
        """One leapfrog step of the two-branch crystal + the ADD-2 converter.
        Converter forces enter the ACCELERATION (Hamiltonian-derived, energy-
        conserving), NOT as a velocity rescale."""
        c_eff_sq = self.c_eff_squared(self.V)
        a_V = c_eff_sq * self._laplacian(self.V, self.dx)
        # vectorized shear Laplacian (bit-identical to the per-component loop)
        a_w = (self.c_T**2) * self._laplacian_vec(self.w, self.dx)

        if self.converter_on:
            f_V, f_w = self._converter_forces()
            a_V = a_V + f_V
            a_w = a_w + f_w
            self.converter_work += float(np.sum(f_V * self.bulk_velocity()) * self.dt)

        V_new = 2.0 * self.V - self.V_prev + (self.dt**2) * a_V
        w_new = 2.0 * self.w - self.w_prev + (self.dt**2) * a_w

        V_new *= self.damping
        w_new *= self.damping[..., None]
        self.V_prev, self.V = self.V, V_new
        self.w_prev, self.w = self.w, w_new
        self.time += self.dt
        self.step_count += 1

    # ------------------------------------------------------------- seeding
    def seed_bulk(self, center, sigma, frac, helical=True, k_wind=None):
        """Seed a pre-compressed / saturated bulk seed (the generative precursor,
        CP8 — a 'Lane-1' mass already present, NOT the planted (2,3)). frac sets
        the seed depth A=frac (frac·V_yield). If helical, give it a slow chiral
        phase so the converter has a handed substrate to imprint on (still NOT a
        closed (2,3): a single-winding precursor)."""
        cx, cy, cz = center
        i, j, k = np.indices((self.N, self.N, self.N))
        r2 = (i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2
        env = np.exp(-r2 / (2.0 * sigma**2))
        amp = frac * self.V_yield
        if helical and k_wind is not None:
            phase = k_wind * np.arctan2(j - cy, i - cx)
            self.V += amp * env * np.cos(phase)
        else:
            self.V += amp * env
        self.V_prev = self.V.copy()  # stationary start (∂_t V = 0)

    def seed_photon(self, center, sigma, wavelength, amplitude, helicity=1.0, direction=(1, 0, 0)):
        """Seed a transverse Z₀-matched helical shear photon (CP8 generative
        precursor; NOT a planted knot). Propagates along `direction`, circularly
        polarized in the two transverse axes with handedness `helicity`."""
        self.helicity = float(helicity)
        cx, cy, cz = center
        i, j, k = np.indices((self.N, self.N, self.N))
        r2 = (i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2
        env = np.exp(-r2 / (2.0 * sigma**2))
        d = np.asarray(direction, dtype=float)
        d = d / np.linalg.norm(d)
        s = i * d[0] + j * d[1] + k * d[2]  # coordinate along propagation
        kk = 2.0 * np.pi / wavelength
        # transverse axes (the two not-parallel-to-d); for d=x these are y,z
        ax1 = (np.argmax(np.abs(d)) + 1) % 3
        ax2 = (np.argmax(np.abs(d)) + 2) % 3
        self.w[..., ax1] += amplitude * env * np.cos(kk * s)
        self.w[..., ax2] += amplitude * env * helicity * np.sin(kk * s)
        # give it a forward group velocity (∂_t w ≠ 0): set w_prev one phase back
        self.w_prev = self.w.copy()
        self.w_prev[..., ax1] = amplitude * env * np.cos(kk * s + kk * self.c_T * self.dt)
        self.w_prev[..., ax2] = amplitude * env * helicity * np.sin(kk * s + kk * self.c_T * self.dt)

    # ----------------------------------------------------- reactance pair
    def bulk_velocity(self) -> np.ndarray:
        """∂_t V (the L-state of the bulk reactance pair, CP6)."""
        return (self.V - self.V_prev) / self.dt

    def shear_velocity(self) -> np.ndarray:
        """∂_t w (…,3) (the shear L-state)."""
        return (self.w - self.w_prev) / self.dt

    def phase_space_vinc_vref(self, omega_char: float):
        """The (V_inc, V_ref) Clifford-torus phasor fields (A46 coordinates).

        The bulk reactance pair (V, ∂_t V/ω_char) IS the native phase-space (CP6):
            V_inc = V + i·(∂_t V/ω_char)   (forward characteristic)
            V_ref = V - i·(∂_t V/ω_char)   (backward characteristic)
        Returns (Vinc_x, Vinc_y, Vref_x, Vref_y) real 3D arrays — the
        (Re, Im) the contour-winding extractor traces toroidally/poloidally.
        This is the phase-space, NOT real-space (the A46 trap that voided 30+
        prior tests). A pure breathing mode has no spatial phase winding; only a
        HELICAL (chiral, spinning) bulk resonance does — exactly what the chiral
        converter must imprint to close the (2,3)."""
        pV = self.bulk_velocity()
        y = pV / max(omega_char, 1e-12)
        return self.V.copy(), y.copy(), self.V.copy(), (-y).copy()

    # ----------------------------------------------------------- ledger
    def bulk_energy(self, interior_only: bool = True) -> float:
        """E_V = ½∫(∂_t V)² + ½∫c0²(∇V)²  (the trapped-bulk energy = the latent
        heat = the candidate mₑc²). PML-excluded by default (CP7)."""
        pV = self.bulk_velocity()
        gx, gy, gz = np.gradient(self.V, self.dx)
        dens = 0.5 * pV**2 + 0.5 * (self.c0**2) * (gx**2 + gy**2 + gz**2)
        if interior_only:
            dens = dens * self.interior_mask()
        return float(dens.sum())

    def shear_energy(self, interior_only: bool = True) -> float:
        """E_w = ½∫(∂_t w)² + ½∫c_T²|∇w|² over the transverse branch."""
        pw = self.shear_velocity()
        dens = 0.5 * np.sum(pw**2, axis=-1)
        for comp in range(3):
            gx, gy, gz = np.gradient(self.w[..., comp], self.dx)
            dens += 0.5 * (self.c_T**2) * (gx**2 + gy**2 + gz**2)
        if interior_only:
            dens = dens * self.interior_mask()
        return float(dens.sum())

    def total_energy(self, interior_only: bool = True) -> float:
        """H = E_V + E_w — the joint ledger. Conservative converter ⇒ H flat
        (energize-LOCK); a pump ⇒ H drifts/detonates (genesis-24)."""
        return self.bulk_energy(interior_only) + self.shear_energy(interior_only)

    def bulk_energy_conserved(self, interior_only: bool = True) -> float:
        """The master equation's variable-coefficient conserved energy
        E = ½∫(∂_tV)²/c_eff² + ½∫|∇V|²  (kinetic weighted by 1/c_eff², NOT the
        naive ½c0²|∇V|² which the nonlinear breather grows). Much flatter — the
        honest ledger for the conservation check."""
        pV = self.bulk_velocity()
        c_eff_sq = self.c_eff_squared(self.V)
        gx, gy, gz = np.gradient(self.V, self.dx)
        dens = 0.5 * pV**2 / np.maximum(c_eff_sq, 1e-30) + 0.5 * (gx**2 + gy**2 + gz**2)
        if interior_only:
            dens = dens * self.interior_mask()
        return float(dens.sum())

    def field_intensity(self) -> dict:
        """Field-amplitude boundedness monitor (PML-excluded) — the genesis-24-
        comparable detonation gate. genesis-24's EMF pump detonated max|V_inc|
        → 1.08e4 / E_V=ΣV_inc² → 6.8e8; energize-LOCK keeps these O(1)."""
        m = self.interior_mask()
        Vi = self.V * m
        wi = self.w * m[..., None]
        return {
            "EV_field": float(np.sum(Vi**2)),
            "max_V": float(np.max(np.abs(Vi))),
            "Ew_field": float(np.sum(wi**2)),
            "max_w": float(np.max(np.abs(wi))),
        }

    def spin_L(self) -> float:
        """|L| = |∫ r×(∂_t w) | proxy over interior — the conserved shear angular
        momentum (energize-LOCK ⇒ bounded; pump ⇒ |L|~t, genesis-24's 5→43)."""
        pw = self.shear_velocity()
        m = self.interior_mask()
        i, j, k = np.indices((self.N, self.N, self.N))
        c = (self.N - 1) / 2.0
        rx, ry, rz = (i - c) * m, (j - c) * m, (k - c) * m
        Lx = np.sum(ry * pw[..., 2] - rz * pw[..., 1])
        Ly = np.sum(rz * pw[..., 0] - rx * pw[..., 2])
        Lz = np.sum(rx * pw[..., 1] - ry * pw[..., 0])
        return float(np.sqrt(Lx**2 + Ly**2 + Lz**2))

    # ---------------------------------------------------- the Γ=-1 wall
    #
    # WAVE-TYPED INDEX (sign-lock w35sn2bq3, landed 2026-06-17 task #12):
    # n=√(εμ) tracks the εμ PRODUCT; a single scalar CANNOT serve both wave
    # types because the EM-transverse and shear/gravitational indices are
    # RECIPROCAL. The wave-speed identity c_eff²=c0²/S (master_equation_fdtd
    # .py:148-151) is the kernel-base anchor:
    #   * EM-transverse  n_EM    = c0/c_eff = S^{+1/2} → 0  (core STIFFENS;
    #                    the saturated core is transparent/fast to the photon)
    #   * shear / grav   n_shear = c0/c_eff = S^{−1/2} → ∞  (light SLOWS;
    #                    the Shapiro/lensing gravitational analog)
    # The legacy magnitude was S^{1/4} (an exponent defect — half the physical
    # power). Corrected to ½ here: SIGN-SAFE (deepens the Γ=−1 wall, never
    # flips it). See the wave-type FLAGs in the task-12 PR for the KB n_eff
    # overload (vacuum-birefringence-e4.md:12 √S vs substrate-perspective-
    # electron.md:58 1/√S) — a KB-OWNER decision, surfaced not silently fixed.
    def n_em_index(self) -> np.ndarray:
        """EM-transverse refractive index n_EM = S(A)^{+1/2} → 0 in the
        saturated core (the photon channel; core stiffens, n falls toward 0)."""
        return self.saturation_kernel(self.V) ** 0.5

    def n_shear_index(self) -> np.ndarray:
        """Shear / gravitational refractive index n_shear = S(A)^{−1/2} → ∞ in
        the saturated core (the Shapiro/lensing channel; light slows). The
        RECIPROCAL of n_em_index — a single scalar cannot serve both."""
        return self.saturation_kernel(self.V) ** (-0.5)

    def refractive_index(self) -> np.ndarray:
        """Back-compat alias = the EM-transverse GROUP index n_EM = S(A)^{+1/2} → 0
        in the saturated core. The historical callers (gamma_bulk, the v14 Mode-I /
        cage / apparatus-floor diagnostics) all read the "n→0 in core" sense, so
        this preserves that direction at the CORRECTED ½ magnitude. New code
        should call the wave-typed n_em_index() / n_shear_index() explicitly.

        HARD-SCOPED (Stage 1, `test_stage1_transverse_modes.py::S1.2`): PINNED to the
        EM GROUP index √S (NOT the PHASE index S, NOT n_shear=1/√S). The Stage-1
        wave-typing gate fails if the alias drifts, so Stage 4 (which inherits this)
        cannot silently re-conflate c_EM and c_shear. See ave-kb/CLAUDE.md:79-80."""
        return self.n_em_index()

    def gamma_bulk(self) -> dict:
        """Smith-Γ on the BULK branch, IMPEDANCE-ROUTED + μ-LOAD-SCOPED.

        Routes Γ through the impedance Z_eff (matching the canonical live wall
        cosserat_field_3d.py:500,1647-1648  Z_eff=Z0·√(S_μ/S_ε), Γ=(Z−1)/(Z+1)),
        NOT the mode-degenerate n-based Γ=(n−1)/(n+1) that is sign-correct only
        by coincidence for a μ-load. CrystalEngine carries a SINGLE bulk-
        dilatation kernel S (one scalar V), so this models the MAGNETIC μ-LOAD:
        Z_eff = Z0·√S → 0 (Z0≡1 engine units), giving Γ → −1, the electron's
        reflective short = THE WALL. In vacuum S→1 ⇒ Z_eff→1 ⇒ Γ→0.

        SCOPE ASSERTION (load-type guard): this is the μ-load branch ONLY. An
        ε-load (Z_eff=Z0/√S→∞) would give Γ=+1 (the OPEN anti-trap). A future
        ε-load import MUST NOT reuse this method's Z_eff form — see the Z-
        convention guard in universal_operators.universal_dynamic_impedance.

        Identical to the old n-based Γ in SIGN and at the matched/short limits
        (Γ=0 at S=1, Γ→−1 at S→0); differs in interior MAGNITUDE because Z=√S
        vs n=√S enter (Z−1)/(Z+1) the same way here (μ-load: n_EM=√S=Z_eff/Z0),
        so the bulk μ-load Γ is numerically the EM-index Γ — by construction,
        not coincidence. SMOKE-1 asks: does Γ_min drive toward −1?"""
        S = self.saturation_kernel(self.V)
        # μ-load impedance, Z0 ≡ 1 in engine units: Z_eff = Z0·√S → 0 short.
        Z_eff = S ** 0.5
        gamma = (Z_eff - 1.0) / (Z_eff + 1.0)
        m = self.interior_mask()
        gi = gamma[m]
        return {
            "gamma_min": float(gi.min()),
            "gamma_mean": float(gi.mean()),
            "frac_short": float((gi < -0.5).mean()),
        }

    def __repr__(self):
        return (
            f"CrystalEngine(N={self.N}, dt={self.dt:.3e}, c_L={self.c0}, "
            f"c_T={self.c_T:.4f}, cL2/cT2={self.cL2_over_cT2:.4f}, "
            f"kappa_tilde={self.kappa_tilde}, converter_on={self.converter_on}, "
            f"step={self.step_count})"
        )
