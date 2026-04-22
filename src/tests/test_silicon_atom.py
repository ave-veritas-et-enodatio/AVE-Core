"""
Test Silicon Atom — ABCD+MCL Hybrid IE Solver
==============================================

Validates that the hybrid solver (Split-Layer Architecture):
  Phase A: ABCD cascade for [Ne] core screening
  Phase B: MCL T²(N_eff) for 3s²3p² same-shell loading
produces a physically reasonable IE for Si.
"""

from ave.nuclear.silicon_atom import first_ionization, IE_SI_AVE, IE_SI_NIST, R_VAL_SI


class TestSiliconIE:
    """IE from ABCD+MCL hybrid solver."""

    def test_ie_positive(self):
        """Sanity: IE must be positive (bound state)."""
        assert IE_SI_AVE > 0

    def test_ie_exceeds_cavity_solver(self):
        """Hybrid must exceed the old cavity solver's 5.06 eV.
        The ABCD cascade accounts for 3s/3p penetration into the
        [Ne] core, which Gauss Z_eff=4 misses entirely."""
        assert IE_SI_AVE > 7.0, f"Hybrid IE {IE_SI_AVE:.2f} eV should exceed cavity solver (5.06 eV)"

    def test_ie_within_30pct_of_nist(self):
        """Current hybrid gives +22.8%. Track as regression target.
        The over-estimate comes from ABCD Z_eff_core = 5.63 (too high).
        Expected to improve when screening profile is refined."""
        err = abs(IE_SI_AVE - IE_SI_NIST) / IE_SI_NIST
        assert err < 0.30, (
            f"IE error {err*100:.1f}% exceeds 30% tolerance. " f"AVE={IE_SI_AVE:.3f}, NIST={IE_SI_NIST:.3f}"
        )

    def test_nist_reference(self):
        """Verify NIST reference value is correct."""
        assert abs(IE_SI_NIST - 8.1517) < 0.001

    def test_port_impedance_positive(self):
        """Valence orbital radius must be positive and finite."""
        assert R_VAL_SI > 0
        assert R_VAL_SI < 1e-9  # smaller than 1 nm


class TestFirstIonization:
    """API compatibility."""

    def test_returns_float(self):
        ie = first_ionization()
        assert isinstance(ie, float)

    def test_matches_module_constant(self):
        assert first_ionization() == IE_SI_AVE
