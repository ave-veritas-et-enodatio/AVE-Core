---
id: manifest-type-residue
title: 19 of 37 rows have a `type` that contradicts the manifest they now live in
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-13
source: manuscript/consistency-manifest.yaml
anchor: "derived_prediction        — genuine forward prediction (Class D)"
---

The 2026-08-13 split gave each manifest a semantic — forward vs reproduced-against-a-known-value —
and **nothing gates a row's `type` against the file it sits in.** An audit added a
`type: consistency_check` row to the forward file and a `derived_prediction` row to the consistency
file; `make verify` stayed green.

**The residue, measured:**

- **18 of 35** rows in `consistency-manifest.yaml` still declare `type: derived_prediction` — which
  the schema defines as *"genuine forward prediction (Class D)"* — while carrying a measured
  `error_percent` against a known value. Includes `P24`, `P05`, `P06`, `P03`, `P04`, `P07`, `P08`,
  `P25`, `P11_12`, `P13`, `P22`, `P26_28`, `P29_32`, `P33_38`, `P39`, `P46`.
- **1 of 2** rows in the forward manifest (`P_A034_solar_flare`) is `type: axiom_manifestation`,
  not a forward type either.

**Why it was not fixed in the split.** The four rows that *were* re-typed (P42, P47, P20_21,
P44_45) were named by Grant's ruling, and the ruling's stated basis — that `consistency_check` *"is
the closer fit"* — applies verbatim to these 18. Extending it unasked would have been the fifth-row
over-reach the split was already flagged for once (P19). **The scope was right; the silence was
not** — the split shipped a file whose header asserts a semantic that half its own rows' `type`
contradicts, with nothing recording it.

**The decision:** re-type the 18 in one pass on the P42 basis, or add a gate reconciling
file-membership against `type`, or declare `type` orthogonal to file-membership and say so in both
headers. Any of the three closes it; leaving it silent re-creates exactly the confusion the split
exists to remove.
