"""R3 lattice decoration discriminator — executable gates per prereg."""

import numpy as np
import pytest

from ave.core import chiral_lattice as cl
from ave.core.lattice_decoration_discriminator import (
    CONTROL_WRITHE_FRAC,
    decoration_signed_proxy,
    run_r3_battery,
)
from ave.topological.cosserat_field_3d import KAPPA_CHIRAL_ELECTRON


class TestR3WritheReplay:
    def test_srs_enantiomorph_writhe_sign_flip(self):
        wr, _, _, _ = cl.net_ring_writhe(cl.build_srs_net(6, "right"))
        wl, _, _, _ = cl.net_ring_writhe(cl.build_srs_net(6, "left"))
        wd, _, _, _ = cl.net_ring_writhe(cl.build_diamond_net(6))
        assert wr * wl < 0
        assert abs(wr + wl) < 1e-2 * abs(wr)
        assert abs(wd) < CONTROL_WRITHE_FRAC * abs(wr)


class TestR3DecorationChannel:
    def test_kappa_zero_gives_zero_proxy(self):
        arm = decoration_signed_proxy(0.0)
        assert abs(arm.signed_proxy) < 1e-11

    def test_kappa_sign_flips_proxy(self):
        p = decoration_signed_proxy(+KAPPA_CHIRAL_ELECTRON)
        m = decoration_signed_proxy(-KAPPA_CHIRAL_ELECTRON)
        assert p.signed_proxy * m.signed_proxy < 0
        assert p.mean_h > 0.5


class TestR3Battery:
    def test_full_battery_assigns_d1_bin(self):
        res = run_r3_battery(L=6)
        assert res.gates["R3-P1_writhe_replay"]
        assert res.gates["R3-P2_bishop_mirror_odd"]
        assert res.gates["R3-P3_arm3_writhe_null"]
        assert res.gates["R3-P4_arm3_kappa0_null"]
        # Decoration channel is κ-consistent but typically weaker than srs Bishop
        assert res.d1_bin in ("D1-A", "D1-MIXED", "D1-B", "D1-INCONCLUSIVE")
        if not res.gates["R3-P5_arm3_kappa_signed"]:
            assert res.d1_bin in ("D1-A", "D1-MIXED")

    def test_decoration_rho_recorded(self):
        res = run_r3_battery(L=6)
        assert res.rho_decoration_vs_srs is not None
        assert res.rho_decoration_vs_srs >= 0.0
