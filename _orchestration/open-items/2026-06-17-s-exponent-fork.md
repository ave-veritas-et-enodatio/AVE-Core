---
id: s-exponent-fork
title: The S-exponent fork — n=S^0.25 vs n=S^0.5 disagree, and it BLOCKS every L3/L4 build
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-06-17
source: _orchestration/index.md
anchor: "1. **S-exponent gates L3.**"
---

`master_equation_fdtd.py:165-168` returns **n = S^0.25** while `c_eff_squared` (`:148-151`) implies
**n = S^0.5**. They disagree, and the clash collides with the T1.6 `c_shear = c₀·S^(1/4)`-vs-`√S`
def-lock. A4 verifies the internally-consistent `c_eff² = c₀²/S` form and surfaces the flag.

**★ The gate, verbatim:** *"Must be adjudicated BEFORE any L3/L4 build that consumes n or c_shear"*
(Ch17 requirement 13).

One of three carried-forward forks the source marks *"→ Grant; do NOT auto-resolve."*
Related: the ground-up acceptance engine's L3 mass-cage rung is Grant-gated on exactly this.
Migrated 2026-08-13 from the index.md ledger during the end-to-end read.
