"""
AVE double-slit + Born-from-clicks capstone.

Two sectors, kept deliberately separate:

  * ``field_engine`` - the REAL FDTD field. A wavepacket through two slits,
    solved with the *canonical* ``ave.core.fdtd_3d.FDTD3DEngine`` (Yee-cell
    Maxwell on the AVE lattice). Produces the smooth |E|^2 interference field
    and the time-integrated detector-row intensity profile  I(y) == |psi|^2.

  * ``click_detector`` - the honest part. A screen of detector cells that
    accumulate absorbed field energy under fluctuation-dissipation (FDT) noise
    and SELF-TRAP (one click) when the accumulated amplitude crosses the
    Axiom-4 saturation yield  S(A) = sqrt(1 - (A/A_yield)^2) -> 0. First-passage
    threshold-crossing, NOTHING ELSE. There is no Born rule, no p = |psi|^2,
    no sampling-from-|psi|^2 anywhere in the click logic.

The Born rule  p ∝ |E|^2  is RECOVERED as the large-N statistics of the
threshold-crossings - it is never assumed.
"""
