"""
Faddeev-Skyrme Hamiltonian Solver for the AVE Topological Network.
Solves for the 1D scalar rest-mass minimum of the structural metric defect.

NOTE: The energy functional used here is the 1D radial projection of the
full 3D hedgehog Hamiltonian. The angular σ-model terms (sin²f, sin⁴f/r²)
are deliberately excluded because the AVE architecture handles the 3D tensor
contribution separately via the Borromean eigenvalue equation in tensors.py.

CRITICAL: The 1D functional is scale-free — it has no natural energy
minimum at finite integration coordinate. Without a confinement bound, the
soliton spreads indefinitely (r_opt → ∞, I → 580). The physical confinement
is set by the topological crossing number of the soliton's winding.

[dimensional-provenance note 2026-06-08]: r_opt below is the DIMENSIONLESS
coupling-budget ratio κ_FS / c, NOT a real-space length / "confinement
radius". κ_FS = 8π is a pure geometric constant (constants.py:683-687). The
solver's integration coordinate normalises ℓ_node = 1 purely as the
Nyquist-gradient-cutoff unit (see the gradient_yield comment in
_energy_density below), so a numeric r_opt is a pure number, not a multiple
of ℓ_node. The only MEASURED proton size is the sub-node charge radius
D_p ≈ 0.841 fm (≈ 460× smaller than ℓ_node = 386 fm) — the proton is NOT a
~5 ℓ_node extended object.

THE TORUS KNOT LADDER (Phase Winding Classification):
  The electron's topology is an unknot (0₁), but its phase winding
  number follows the (2,3) pattern with c₃ = 3 crossings.
  The proton's phase winding is a (2,5) cinquefoil torus knot with
  c₅ = 5 crossings.  The (2,q) torus knots require odd q; there is
  no stable (2,4) configuration (the figure-eight is not a torus knot).

  The crossing number sets the DIMENSIONLESS coupling-budget ratio (NOT a
  real-space "confinement radius" / "radial extent") because each crossing
  absorbs a fraction of the total coupling. The per-crossing budget ratio
  is therefore:

      r_opt = κ_FS / c₅ = κ_FS / 5   (a pure number, NOT a length)

  This divides the total Faddeev-Skyrme coupling by the number of
  topological crossings through which the phase must wind. [relabel
  2026-06-08: prior text "confinement radius" / "soliton's radial extent"
  framed r_opt as a length — a dimensional category error; r_opt is
  dimensionless, κ_FS = 8π being a pure geometric constant.]

  CROSS-SCALE CONNECTION (confinement ↔ atomic void floor):
    At nuclear scale (Regime I, S→0): the crossing number sets the
    dimensionless coupling-budget ratio r_opt = κ/c (a pure number, NOT a
    soliton radius).  The SAME lattice packing fraction φ = π√2/6 (FCC,
    K=2G) bounds the saturated zone geometry.

    At atomic scale (Regime II, S≈1): the junction crossing count c
    drains phase space via Op10.  The void fraction (1-φ ≈ 0.26)
    bounds the drain: IE ≥ E_base × (1-φ).

    Both scales: crossing count partitions the available resource.
    The FCC packing fraction φ governs both.
"""

import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

# As of P5-A the historical circular dependency between this module and
# ave.core.constants has been eliminated: constants.py no longer runs the
# Faddeev-Skyrme solver at import time (its outputs are stored as verified
# literals there).  EPS_NUMERICAL and CROSSING_NUMBER_CINQUEFOIL therefore
# live canonically in ave.core.constants and are imported from there.
from ave.core.constants import CROSSING_NUMBER_CINQUEFOIL, EPS_NUMERICAL


class TopologicalHamiltonian1D:
    def __init__(self, node_pitch: float, scaling_coupling: float = 1.0) -> None:
        """
        Initializes the 1D solver for the localized non-linear phase defect.

        Args:
            node_pitch (float): Fundamental structural spacing (Axiom 1).
            scaling_coupling (float): The generalized Faddeev coupling constant.

                ⚠ PRECONDITION: If the caller passes KAPPA_FS from
                src/ave/core/constants.py (the canonical proton-baryon
                coupling), the value is ALREADY thermally softened at
                import time:

                    KAPPA_FS = KAPPA_FS_COLD * (1 - DELTA_THERMAL)
                           = 8π * (1 - 1/(14π²))
                           ≈ 24.951       (constants.py:563–566)

                The thermal softening δ_th = 1/(14π²) is the proton
                core's thermal correction at its native ~10¹³ K regime.
                This solver does NOT re-apply the softening — the input
                κ is expected to be already-softened. If you're passing
                a different coupling (e.g. KAPPA_FS_COLD for a
                sensitivity check or T→0 limit), pass the intended
                value explicitly.

                See also: src/ave/core/constants.py `KAPPA_FS` definition
                (~line 566), LIVING_REFERENCE.md Rule D2, and
                docs/framing_and_presentation.md §D2 for the
                "preconditions applied before solver entry" pattern.
        """
        self.l_node = node_pitch
        self.kappa = scaling_coupling

    def _phase_profile(self, r: float, r_opt: float, n: float) -> float:
        """
        Standard 1D topological profile interpolating smoothly between:
        phi(0) = pi (inverted core phase)
        phi(inf) = 0 (relaxed unbroken vacuum)
        """
        if r == 0:
            return np.pi

        scaled_r = r / r_opt

        # Power-law bounded profile matching standard topological ansatz
        return np.pi / (1.0 + (scaled_r) ** n)

    def _energy_density_integrand(self, r: float, r_opt: float, n: float) -> float:
        """
        Evaluates the local energy density of the Faddeev-Skyrme functional
        at a specific radius r, including Axiom 4 gradient saturation.

        The lattice has a maximum resolvable phase gradient of π/ℓ_node
        (one full half-rotation per cell).  When the solver's continuous
        profile produces gradients approaching this limit, the saturation
        factor S(|dφ/dr| / (π/ℓ_node)) smoothly reduces the effective
        gradient — the same operator that governs FDTD field updates,
        plasma cutoff, and galactic rotation drag.

        Note: The true 3D tensor trace uses external geometric bounding
        from `tensors.py`.  Here we evaluate the 1D radial scalar.
        """
        # Central-difference derivative for improved accuracy
        dr = 1e-6
        phi1 = self._phase_profile(r, r_opt, n)
        phi2 = self._phase_profile(r + dr, r_opt, n)
        dphi_dr = (phi2 - phi1) / dr

        # Axiom 4: gradient saturation at the lattice Nyquist limit
        # The solver operates in natural units where r is measured in
        # units of ℓ_node (i.e. ℓ_node = 1).  The maximum resolvable
        # phase gradient is therefore π per unit length (one half-
        # rotation per cell).
        gradient_yield = np.pi  # π / ℓ_node = π / 1 in natural units
        from ave.core.universal_operators import universal_saturation

        S = universal_saturation(dphi_dr, gradient_yield)
        dphi_dr_eff = dphi_dr * S

        # Quadratic stiffness term (Standard Dirichlet tension)
        kinetic_term = 0.5 * (dphi_dr_eff**2)

        # Quartic stabilization term (Skyrme/Faddeev Tensor repulsion)
        # Prevents the defect from collapsing to a singularity
        # In 1D radial projection, sin²(phi)/r² dominates
        skyrme_term = 0.5 * (np.sin(phi1) ** 2) / (r**2 + EPS_NUMERICAL)

        # Total density scaled spherically
        density = 4 * np.pi * (r**2) * (kinetic_term + (self.kappa**2) * skyrme_term * dphi_dr_eff**2)

        return density

    def solve_scalar_trace(self, crossing_number: int = CROSSING_NUMBER_CINQUEFOIL) -> float:
        """
        Minimizes the 1D topological Hamiltonian to find the absolute lowest
        energy stable profile of the fundamental defect.

        The confinement bound r_opt ≤ κ/c divides the total Faddeev-Skyrme
        coupling by the crossing number, partitioning the coupling equally
        among the topological crossings through which the phase must wind.

        Preconditions applied to self.kappa BEFORE entry (see __init__ docstring):
          - Thermal softening δ_th = 1/(14π²) ≈ 7.21×10⁻³ is applied in
            src/ave/core/constants.py:563–566 (KAPPA_FS = KAPPA_FS_COLD × (1 − DELTA_THERMAL)).
            This solver receives the already-softened κ and does not re-apply.
            For T→0 / cold-limit behavior, instantiate with scaling_coupling=KAPPA_FS_COLD.

        Args:
            crossing_number: The number of topological crossings for the
                (2,q) torus knot.  Default is 5 (proton cinquefoil).
                The torus knot ladder uses odd q: 5, 7, 9, 11, 13, ...

        Returns:
            float: The integrated energy eigenvalue in dimensionless mass units.
        """
        # Confinement bound from crossing number
        r_opt_max = self.kappa / crossing_number

        def objective(params):
            """Integrate the Faddeev-Skyrme energy density for a trial (r_opt, n) profile."""
            r_opt, n = params
            # Integrate the energy density from core out to 10 * r_opt
            integral, _ = quad(self._energy_density_integrand, 0.0, 10.0 * r_opt, args=(r_opt, n), limit=100)
            return integral

        # Initial guesses: optimal radius roughly 1.0, power profile n=2
        initial_guess = [1.0, 2.0]

        # Bound the radius by the confinement, n > 0
        bounds = [(0.1, r_opt_max), (1.0, 4.0)]

        result = minimize(objective, initial_guess, bounds=bounds, method="L-BFGS-B")

        # Return the minimized dimensionless energy scalar
        return result.fun

    # -------------------------------------------------------------------------
    # ROUTE A — the composite 6₂³ ∪ 0₁ neutron: the one new capability the
    # corpus TBD-pin names (neutron-identification.md:36/:77/:54). The threaded
    # 0₁ unknot's tube (transverse thickness ≥ 1 ℓ_node by Ax1) occupies the
    # cage's central void and displaces the winding shell OUTWARD by d, which is
    # "the additional threaded-electron constraint adding to the FS energy
    # integral" (:77). Cage phase is held at π on [0, d] (the fully-wound core
    # now occupied by the threaded tube), then winds down over (d, ∞) with the
    # SAME functional and the SAME c=5 confinement (the proton stays a proton).
    # The spherical 4πr² measure weights the displaced shell more → the FS
    # energy RISES → the elastic-expansion mass surplus (:25). This is the ONLY
    # rendering of the three physical candidates (inner-exclusion, r_opt-stretch,
    # shift-outward) that produces the canon-required POSITIVE surplus; the other
    # two give the wrong sign and are ruled out BY the corpus. Rendering is
    # CANON-FORCED, not invented (see the frozen prereg's substrate-native walk).
    #
    # This is a NON-INTRUSIVE addition: solve_scalar_trace (the bare proton path)
    # is untouched, and solve_composite_trace(d=0) reduces EXACTLY to it (a
    # built-in consistency check the driver asserts). [dimensional-provenance:
    # d is in the solver's dimensionless ℓ_node Nyquist-cutoff unit, NOT a
    # real-space length — same convention as r_opt.]
    # -------------------------------------------------------------------------
    def _composite_energy_density_integrand(
        self, r: float, r_opt: float, n: float, d: float
    ) -> float:
        """Faddeev-Skyrme energy density for the threaded-composite cage.

        Identical to `_energy_density_integrand` except the cage winding shell is
        displaced outward by the threaded-tube radius `d`: φ(r) = π on [0, d]
        (core occupied by the 0₁ tube), φ(r) = π/(1 + ((r−d)/r_opt)ⁿ) on (d, ∞).
        Axiom 4 gradient saturation is applied identically (same Nyquist yield).
        """

        def phi_of(rr: float) -> float:
            if rr <= d:
                return np.pi
            return np.pi / (1.0 + ((rr - d) / r_opt) ** n)

        dr = 1e-6
        phi1 = phi_of(r)
        phi2 = phi_of(r + dr)
        dphi_dr = (phi2 - phi1) / dr

        # Axiom 4: gradient saturation at the lattice Nyquist limit (unchanged).
        gradient_yield = np.pi  # π / ℓ_node = π / 1 in natural units
        from ave.core.universal_operators import universal_saturation

        S = universal_saturation(dphi_dr, gradient_yield)
        dphi_dr_eff = dphi_dr * S

        kinetic_term = 0.5 * (dphi_dr_eff**2)
        # In the held-core region [0, d], φ = π so sin²(φ) = 0 and the Skyrme
        # term vanishes there (the tube's fully-wound core carries no gradient
        # tension) — the surplus comes entirely from the displaced winding shell.
        #
        # ⚠ CHANNEL-EXCISION DISCLOSURE (2026-07-14 adversarial review): the
        # `density` below multiplies skyrme_term by the spherical 4πr² measure,
        # which cancels its 1/r² EXACTLY, leaving 4π·κ²·0.5·sin²(φ)·dφ_eff² — a
        # function of φ and dφ/dr with NO explicit r. Under the rigid outward
        # shift φ(r)=φ_bare(r−d) this κ²-weighted term is therefore SHIFT-
        # INVARIANT and cancels IDENTICALLY in E_comp − E_bare (it does NOT merely
        # "vanish on [0, d]" — the WHOLE channel drops out of the difference;
        # live-fire: Skyrme d-surplus ≈ −7e-7, κ-coupled fraction ≈ −2.8e-8; the
        # entire threading surplus lives in the κ-FREE kinetic_term above). Since
        # δ_th enters ONLY through κ (KAPPA_FS = KAPPA_FS_COLD·(1−δ_th)) and κ
        # appears at just two sites — this quartic coefficient and the
        # r_opt_max=κ/5 bound in solve_composite_trace — the ablation's δ_th-
        # loading of the SPLIT is confined to the r_opt-bound residual; the
        # FS-route (quartic) loading channel is structurally absent from the
        # difference. => C5 is NOT adjudicable in this 1D shift proxy; the ablation
        # is CHANNEL-BLIND. A faithful C5 test needs a 3D composite build that
        # retains the quartic linking channel.
        skyrme_term = 0.5 * (np.sin(phi1) ** 2) / (r**2 + EPS_NUMERICAL)

        density = 4 * np.pi * (r**2) * (kinetic_term + (self.kappa**2) * skyrme_term * dphi_dr_eff**2)
        return density

    def solve_composite_trace(
        self,
        threading_displacement: float,
        crossing_number: int = CROSSING_NUMBER_CINQUEFOIL,
    ) -> float:
        """Composite 6₂³ ∪ 0₁ FS scalar trace: the bare-cage minimization with the
        threaded-electron constraint (winding shell displaced outward by
        `threading_displacement` = d, in ℓ_node cutoff units).

        Same energy functional, same crossing-number confinement (c=5, the proton
        stays a proton). `solve_composite_trace(0.0)` reduces EXACTLY to
        `solve_scalar_trace()` (the d=0 consistency check).

        Args:
            threading_displacement: d — the outward displacement of the cage's
                winding shell by the threaded 0₁ tube. d ≥ 1 ℓ_node by Axiom 1
                (no flux tube below transverse thickness 1 ℓ_node).
            crossing_number: (2,q) crossing number; default 5 (proton cinquefoil,
                unchanged — the composite cage is still a proton).

        Returns:
            float: the minimized composite FS energy I_comp(d) in dimensionless
                mass units (same units as `solve_scalar_trace`).
        """
        d = threading_displacement
        r_opt_max = self.kappa / crossing_number

        def objective(params):
            r_opt, n = params
            # Integrate out to 10·r_opt PAST the displaced core wall at d.
            integral, _ = quad(
                self._composite_energy_density_integrand,
                0.0,
                10.0 * r_opt + d,
                args=(r_opt, n, d),
                limit=100,
            )
            return integral

        initial_guess = [1.0, 2.0]
        bounds = [(0.1, r_opt_max), (1.0, 4.0)]
        result = minimize(objective, initial_guess, bounds=bounds, method="L-BFGS-B")
        return result.fun
