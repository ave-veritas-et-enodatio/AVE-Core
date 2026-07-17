"""AVE thermal / entropy-sink (R7) instrumentation.

Sector: R7 thermal / entropy-sink (T2 latent-heat channel). NOT A1 mass,
NOT Cosserat (2,3) winding/charge.

Currently exports the F6 bath meter — the rebuilt mode-count detector mandated
by the JOINT detector-rebuild GATE (hardware-ratings-map §7, post-#711/#714).
"""

from __future__ import annotations

from ave.thermal.f6_bath_meter import (
    LatticeBathCoupler,
    OscillatorBath,
    make_collar_mask,
)

__all__ = ["OscillatorBath", "LatticeBathCoupler", "make_collar_mask"]
