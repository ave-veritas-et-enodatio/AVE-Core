---
id: proton-node-span
title: Multi-node vs single-node proton — a .tex sentence and an engine docstring assert opposite geometry
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-06-08
source: manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex
anchor: "Borromean knot spans multiple fundamental nodes"
---

Both cites live and contradictory at HEAD:

- `manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex:41` — *"The $6^3_2$ Borromean knot
  **spans multiple** fundamental nodes."*
- `src/scripts/vol_6_periodic_table/simulations/semiconductor_binding_engine.py:68` — *"the entire
  nucleus exists **inside a single** saturated lattice node (ℓ_node ≈ 386 fm)."*

The `.py` has **zero commits since 2026-06-08**, so this is not recent drift — it has been shipping
both ways for two months.

**What rides on it:** decides the §43/§45 fork's value axis (`fork-45-value-axis`). Verified
2026-08-13 by sweep at `origin/main` `7d361e96`.
