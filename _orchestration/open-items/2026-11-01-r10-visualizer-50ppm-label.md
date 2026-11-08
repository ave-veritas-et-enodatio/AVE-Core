---
id: r10-visualizer-50ppm-label
title: A live "50 ppm" label survives in the r10 visualizer, outside the R3 sweep's scope
status: OPEN
owner: unassigned
opened: 2026-11-01
source: src/scripts/vol_1_foundations/r10_path_alpha_v14_soliton_visualizer.py
anchor: "Route B (50 ppm to PDG"
---

**The ask (one line):** *`r10_path_alpha_v14_soliton_visualizer.py:21` and `:308` still carry the
"50 ppm" label on the Q-G19α Route B closure, and `:308` renders into a figure caption.*

The 2026-08-03 ruling struck the ppm deviation labels on $C_2$ with no number substituted
(`docket-entries/2026-08-03-petermann-amendments.md`). `f953a38e`, the R3 residue sweep, covered
`manuscript/` only. Its message flagged these two lines as live and left them, and that message
was their only record until this item.

Nothing is changed here. The figure is not regenerated, and neither line is edited. The wording
R3 used in place of the label is itself awaiting Grant on #1039, so these two lines wait on that
answer.
