# As-fabbed HOPF-02a wire polylines — vendored copy, PROVENANCE

Read-only vendored copies of the AVE-HOPF as-fabbed wire CSVs, checked in here so the
`pasteur_kappa_desk_calc` driver is hermetic (no cross-repo filesystem dependency at run time).

**AVE-HOPF is READ-ONLY for the lane that vendored these. Nothing was written there.**

| Field | Value |
|---|---|
| Source repo | `AVE-HOPF` (`ave-veritas-et-enodatio/AVE-HOPF`) |
| Source directory | `data/hopf_02/` |
| Source commit (last touching these files) | `29264b483cdce6cdb01b798293b28b9339cabd82` (2026-05-21) |
| AVE-HOPF HEAD at vendoring time | `4c11ab30e4a1984df4c601037875c318e84f1aff` |
| Vendored | 2026-08-02, lane `research/pasteur-kappa-desk-calc` |
| Generator (upstream) | `scripts/hopf_02_build_drill_readback_wire.py` — the canonical source for hole positions, per `hardware/hopf_02_ASSEMBLY_GUIDE.md` |

## Files + sha256 (verified by the driver at every run)

| File | sha256 | points | arc length (mm) |
|---|---|---|---|
| `k23_R_wire.csv` | `76835d45daaf526cbaa182b3134ea0846e821d0dd3cc4103c19fef874fff6e52` | 40 | 230.560 |
| `k23_L_wire.csv` | `4032340d3114c8408fcbc968a53abc5b570e939b3891b3cb5d0400f1a70b8f4b` | 40 | 230.560 |
| `control_wire.csv` | `e7a9675a9c9d0e00db27af41a4610785052ece9cf802efaeaa398c229bdd5797` | 18 | 177.471 |

> The sha256 column above is a human-readable transcript; the AUTHORITATIVE digests are the ones
> asserted in `research/drivers/pasteur_kappa_desk_calc.py` and re-checked on every run. If a
> digest here and there ever disagree, the driver's is the one that gates.

## Format

`x_mm,y_mm,z_mm` — an ordered 3D polyline in board coordinates. `z ∈ {−1.6, 0.0, +1.0}` mm:
`+1.0` = wire standing off the top copper, `0.0` = in a through-hole transit, `−1.6` = under the
1.6 mm FR-4 board. The out-of-plane extent (2.6 mm) is the entire source of the structure's
three-dimensional chirality; `control_wire.csv` has a single `x` value for every point (it lies
in one plane) and is therefore **achiral by construction** — the lane's known-negative.
