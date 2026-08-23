---
id: figure-bit-reproducibility
title: Tracked figures are not bit-reproducible — matplotlib is unpinned (3.10.8 stamps vs 3.10.9 venv)
status: OPEN
owner: unassigned
opened: 2026-08-20
source: _orchestration/docket-entries/2026-08-20-phase2-destination-map.md
anchor: "The line-by-line pass is load-bearing"
---

Found by the #991 repair lane's live-fire (2026-08-20): `simulate_optical_caustic.py` is
deterministic (two consecutive runs → identical blob), but its output ≠ the tracked twin —
the tracked PNG's `Software` chunk reads "Matplotlib version3.10.8" while the venv carries
3.10.9. IHDR geometry and dpi byte-equal; driver and solver unchanged since 2026-05-28;
4.3% of pixels differ with a rigid ~(1,2)px shift component. All four tracked
`s11_denovo_*.png` carry the same 3.10.8 stamp.

**Consequence:** "regenerable" ≠ "bit-reproducible" for every tracked matplotlib render.
Any future byte-identity check between a regenerated figure and its tracked copy is
a-priori unachievable across matplotlib versions; the honest comparison is numeric-artifact
identity (which held bit-exact in the same live-fire) + version-stamped renders.

**Candidate closures, un-endorsed:** (a) pin matplotlib in the venv + record the pin as the
render-provenance rule; (b) accept non-bit-reproducibility, record it in the figure policy,
and make numeric artifacts the identity-bearing outputs (renders = derived views); (c) both —
pin going forward, declare historical stamps authoritative for their era. (b) matches the
corpus's existing driver-is-source-of-truth posture; (a) alone rots at the next venv bump.
