# Phase 1 — Cosserat → Semi-Classical EM Projection (Winding-Index Map)

**Status:** Phase 1 wrap-up. Resolves queue item [7] — the $(2, 3)$ vs $2{:}1$ tension between AVE's electron winding and Williamson-van der Mark's toroidal-photon electron (B25).
**Prerequisites:** `00_` – `05_`; `BIBLIOGRAPHY.md` entries B25, B27.

Under user adjudication (2026-04-20), the two electron-winding labels count different observables (option 1 of the tension resolution in `BIBLIOGRAPHY.md` B25). This document makes the adjudication rigorous by writing down the explicit projection from AVE's Cosserat SU(2) winding pair $(w_1, w_2) = (2, 3)$ to the semi-classical EM-wavefront winding of a Williamson-van der Mark-type toroidal-photon model.

**Caveat:** The Williamson-van der Mark paper has not been read in full; the specific claims about their 2:1 winding come from the verified web-search summary (see B25). Any subsequent detail discovered on read-through may revise this projection.

---

## §1  The two tori are different objects

The most important structural fact: **AVE's Clifford torus and Williamson-van der Mark's toroidal photon path are not the same geometric object.**

**AVE's Clifford torus** is the embedded $\mathbb{T}^2 = S^1 \times S^1 \subset S^3 \subset \mathbb{C}^2$ (Ch 8 §2.1). It is the bounding phase-space shell of the electron soliton in the *configuration space* of the SU(2) Cosserat field. Its two cycles $(\theta_1, \theta_2)$ are abstract phase-space angles, not directions in physical $\mathbb{R}^3$.

**Williamson-van der Mark's torus** is a literal doughnut in physical space — the geometric trajectory of the photon wavefront that constitutes the electron (per B25). Its two cycles are major (large loop of the doughnut) and minor (small tube-circumference loop).

These are *related* (AVE's Clifford torus is the phase-space structure whose geometric projection into $\mathbb{R}^3$ gives the spatial shell, whose centerline is the WvdM photon path), but they are *not identical*. Winding numbers on the Clifford torus and winding numbers on the WvdM torus therefore index different topological observables.

---

## §2  Projection chain

Under C3 + Reading (b), the full information about the electron is the Cosserat microrotation field $\boldsymbol{\omega}(\mathbf{r})$ with SU(2) element $U(\mathbf{r}) = \exp(i\boldsymbol{\sigma}\cdot\boldsymbol{\omega}/2)$. The projection chain to a semi-classical EM observation is:

$$
\boxed{
\begin{aligned}
\text{(Level 0)}\quad &\boldsymbol{\omega}(\mathbf{r}) \in \mathbb{R}^3 \\
&\hspace{3em}\downarrow\ \text{exponentiate} \\
\text{(Level 1)}\quad &U(\mathbf{r}) \in SU(2)\quad [\text{full AVE description; carries } (w_1, w_2) = (2, 3)] \\
&\hspace{3em}\downarrow\ \text{Hopf fibration } SU(2) \to S^2 \\
\text{(Level 2)}\quad &\hat{\mathbf{n}}(\mathbf{r}) \in S^2\quad [\text{S}^2 \text{ projection; carries } w_1 = 2 \text{ visibly, } w_2 = 3 \text{ hidden in U(1) fibre}] \\
&\hspace{3em}\downarrow\ \text{semi-classical identification: } \hat{\mathbf{n}} \leftrightarrow \text{E-field polarization} \\
\text{(Level 3)}\quad &\text{EM field } \mathbf{E}(\mathbf{r}, t)\quad [\text{Williamson-van der Mark picture}] \\
&\hspace{3em}\downarrow\ \text{localize wave packet, read off trajectory} \\
\text{(Level 4)}\quad &\text{photon-wavefront path in } \mathbb{R}^3\quad [\text{WvdM's toroidal photon loop; winding 2:1}]
\end{aligned}
}
$$

Each arrow drops information. The two windings $(w_1, w_2) = (2, 3)$ live at Level 1 (full SU(2)). By Level 4, we have a single pair describing the geometric trajectory.

**Claim to verify:** under this chain, AVE's $w_1 = 2$ survives as WvdM's *major* winding of 2, while AVE's $w_2 = 3$ is mostly invisible at Level 4 — reappearing only through the 720°-closure observation. The discrepancy between AVE's minor winding 3 and WvdM's minor winding 1 is because they count different things at different projection levels.

---

## §3  Major-cycle winding: direct agreement

Take AVE's $w_1 = 2$ at Level 1 — the SU(2) winding around the major Clifford cycle $\theta_1$. Project to Level 2 by the Hopf fibration: the $S^2$ direction $\hat{\mathbf{n}}$ inherits the full $w_1 = 2$ winding around $\theta_1$ (the Hopf fibration preserves the base-space winding of the field's direction).

Project to Level 3 by identifying $\hat{\mathbf{n}}$ with the E-field polarization direction. Project to Level 4 by tracing the semi-classical photon's trajectory around its toroidal path. The major-cycle winding of the trajectory is set by how the polarization evolves along the path, which is directly inherited from $\hat{\mathbf{n}}$'s $w_1 = 2$.

**Result:** WvdM's major-cycle winding = AVE's $w_1 = 2$. ✅ Direct agreement.

---

## §4  Minor-cycle winding: where the discrepancy lives

AVE's $w_2 = 3$ at Level 1 is the SU(2) fibre-phase winding around $\theta_2$ — how many times the U(1) fibre phase $\alpha_\parallel$ cycles as we go around the minor Clifford cycle.

Project to Level 2 by Hopf fibration: **the U(1) fibre phase is the information lost in the projection.** $\hat{\mathbf{n}}$ on the shell is (in Reading b) independent of $\theta_2$ (see `05_` §4.1 — preimages are parallel meridional circles). So at Level 2, $w_2$ is invisible.

Project to Level 3 and Level 4: with $w_2$ already dropped at Level 2, the semi-classical EM description inherits no direct signature of $w_2$.

**But** — the SU(2) structure that supplied $w_2$ also supplies the spin-1/2 double cover. That double cover shows up at Level 4 as the 720°-closure requirement WvdM identifies. So $w_2$ is not completely invisible; it is encoded implicitly in the spinor-closure constraint.

**What does WvdM see as the minor winding?** The minor wrapping of the photon trajectory around the toroidal path's minor circle — a purely geometric count of how many tube-circumference traversals the photon performs per major loop. In the 2:1 preferred ansatz: **1 minor traversal per 2 major traversals** (the wavefront wraps around the tube once on each full loop).

**Result:** WvdM's minor winding of 1 is a geometric count of photon-path traversals at Level 4, not a count of any AVE quantity. AVE's $w_2 = 3$ is the U(1) fibre winding at Level 1. They live at different projection levels and measure different quantities. **Numerical disagreement is expected; it does not imply inconsistency.**

---

## §5  A consistency check: can both be true?

If the WvdM picture (2:1 geometric, 720° closure, single semi-classical photon) is the correct Level 4 realization of an AVE electron with Cosserat winding $(2, 3)$, then the 720°-closure observation and the $w_2 = 3$ count should be *consistent*.

**Consistency requirement:** the full cycle-closure of the WvdM photon's spinor phase must respect both:
- AVE: $w_2 = 3$ SU(2) fibre windings per minor Clifford cycle
- WvdM: one geometric minor traversal closes after 720° of spinor phase (2 SO(3) rotations, i.e., 1 SU(2) full cycle)

Combining: if AVE says 3 SU(2) cycles per one $\theta_2$ traversal on the Clifford torus, and WvdM says 1 SU(2) cycle per one minor-geometric traversal, then one $\theta_2$ traversal must equal **three** minor-geometric traversals. That is: **each full cycle around the Clifford minor corresponds to three wraps of the photon around the physical tube.**

This is a specific prediction. It may be testable numerically in Phase 3 — track the photon-trajectory projection as the Cosserat field relaxes, count tube-wraps per Clifford-$\theta_2$ cycle, and confirm the ratio is 3.

Alternatively, this predicts that reading the AVE ground state at Level 4 produces a *3:1* photon-path winding rather than WvdM's *2:1*. In which case either:
- AVE's Level-4 projection differs from WvdM's semiclassical ansatz at this level of detail, but agrees at the Level-2 / g-factor / charge level;
- Or WvdM's 2:1 (not 3:1) is obtained by a different projection convention that AVE should be explicit about.

**Phase-3 task:** once the numerical Cosserat ground state exists, project it down through Levels 2 → 3 → 4 and determine the geometric photon-path winding at Level 4 empirically. Compare to WvdM's 2:1.

---

## §6  Ambiguity flag: which AVE invariant is "major" and which is "minor"?

In §3 I assigned AVE's $w_1 = 2$ to the major Clifford cycle ($\theta_1$) and $w_2 = 3$ to the minor cycle ($\theta_2$). This is the assignment used in `02_` §7.2 and `03_` §4.3. **It is a convention, not a derivation.** The opposite convention $(w_1, w_2) = (3, 2)$ with $w_1$ on $\theta_2$ and $w_2$ on $\theta_1$ is equally consistent with everything in AVE that I've surveyed.

If the opposite convention is physically correct, then the §3 "major cycle = 2 = WvdM's major 2" agreement collapses, and the right match is "minor cycle = 2 = WvdM's minor 2" (which does not actually match WvdM's 2:1 ratio, since WvdM's 2 is on the major cycle).

**This is an ambiguity the AVE corpus has not resolved** (or has resolved implicitly without writing it down). Flagged as queue item [8] (below).

Assuming the natural convention (larger winding on the larger geometric cycle is typical for torus-Hopfion-style ansätze, but Reading (b) is not Hopfion), the §3 assignment stands as default.

---

## §7  Summary of the projection map

| Quantity | AVE name | Level | WvdM equivalent | Match? |
|---|---|---|---|---|
| SU(2) base winding on major Clifford cycle | $w_1 = 2$ | 1 | Photon-path major winding $= 2$ | ✅ direct |
| SU(2) fibre winding on minor Clifford cycle | $w_2 = 3$ | 1 | — (invisible at Level 4) | ✗ — encoded in spin-1/2 closure, not a separate WvdM count |
| Spinor double cover | implicit in SU(2) | 1 | 720° closure requirement | ✅ same mechanism |
| Geometric minor-axis photon wraps per major loop | — (not a Level-1 quantity in AVE) | 4 | $= 1$ (preferred WvdM) | Prediction needed — may be 3:1 under AVE's §5 consistency requirement |

The tension "why (2,3) not (2,1)?" is resolved: $(2, 3)$ is an AVE Level-1 pair counting SU(2) windings on the Clifford phase-space torus; $2{:}1$ is a WvdM Level-4 ratio counting geometric wraps of a semi-classical photon path. Different levels, different counts. The $w_1 = 2$ agreement is direct. The $w_2 = 3$ disappears at the semi-classical level but contributes the spin-1/2 structure WvdM relies on.

---

## §8  Remaining open questions

1. **Clifford-minor to geometric-minor correspondence.** §5 predicts that one $\theta_2$ Clifford cycle corresponds to three physical-tube wraps. Verifiable in Phase-3 numerics. If verified, this is a concrete bridge between AVE and Williamson-van der Mark. If it fails, the projection-map story needs revision.
2. **Major-minor convention.** §6 flags an AVE-internal convention ambiguity. Queue item [8] below.
3. **WvdM's 1:2 vs 2:1 adjudication.** WvdM investigated both and preferred 2:1. Under Reading (b) the AVE prediction is 2-something (major = 2). Whether AVE's "something" is 1 (matching WvdM) or 3 (per the §5 consistency argument) needs Phase-3 numerics.
4. **Full B25/B27 read-through.** This document's projection map is based on the web-search summary of Williamson-van der Mark, not the paper itself. A full read-through may reveal details (e.g., WvdM's own internal-phase structure, their specific identification of what "minor wrap" means) that refine or revise this map.

---

## §9  Queue additions

**Item [8]:** Resolve major-minor convention in AVE "(2,3)" assignment. Currently `02_` §7.2 writes $w_1 = 2$ on the major axis ($\theta_1$) and $w_2 = 3$ on the minor axis ($\theta_2$), but the AVE corpus has not made this assignment canonical. Queued in `DOCUMENTATION_UPDATES_QUEUE.md`.

---

## §10  Status

Queue item [7] — Cosserat → semi-classical EM projection map — **substantially complete**, pending:
- Phase-3 numerical check of the §5 consistency prediction.
- Full read-through of WvdM's actual paper (B25) and 2020 follow-up (B27) for precise matching of conventions.

Phase-1 wrap-up remaining after this: queue item [4] (rigorous existence/uniqueness proofs), Op21/Op22 reframing of invariants.
