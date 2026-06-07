# Neutrino-sector "3" re-grounding check — per-bond → per-Cosserat-sector substitution under the z=4 diamond resolution

**Date:** 2026-06-07
**Lane:** implementer (substrate-physics trace + classification; NO walk-back executed — surfaced only, per flag-don't-fix)
**Branch:** `analysis/2026-06-07-neutrino-3-regrounding` (off `origin/main` @ `d5b71d5c`)
**Status:** complete — trace + three groundings + δ_CP/Δc_crit verdicts + classification + flagged contradiction + walk-back recommendation (surfaced, not executed).
**Upstream resolution-of-record:** `_orchestration/2026-06-07_lattice-net-resolution.md` (on branch `analysis/2026-06-06-session-handoff`) — **Net = z=4 diamond.** This doc closes its one open work item.

> **One-line verdict.** The δ_CP "1/3" **re-grounds cleanly** on the 3 Cosserat microrotational sectors and **restores 1.3556π exactly on z=4** (1/3 = 1/3, not 1/4) — sector- and crossing-groundings both survive the diamond. The **sharper** exposure — `Δc_crit` (the θ₁₃ screening threshold) — re-grounds on the 3 Cosserat sectors **only via a genuine mechanism-substitution** (intrinsic 3-component angular momentum, not bond-channel count); as *written* (`chiral-screening.md:13`) it is bond-count and flips 3→4, which **catastrophically unscreens θ₁₃** (0.022 → ~0.44). The re-grounding is **a legitimate re-attribution that preserves the numbers** — but ONLY because the original per-bond reading was *coincidental* at z=3 (where bonds = sectors = crossings = 3). **Recommendation: keep z=4, fix the bond-wording** in the 5 flagged spots — *conditional on Grant adjudicating the Δc_crit mechanism-substitution*, which is the one load-bearing physics call. Clean-ish outcome (sector-grounded), with one genuine-physics caveat at Δc_crit.

---

## §0 — Scope, skill-selection plan, honest framing

**Narrow scope (do NOT re-litigate the net).** The net decision is **resolved: z=4 diamond** (`lattice-net-resolution.md`, sources `a4472bc5` + `aea3cc7d`, grep-confirmed). The z=3 srs leaves are the unbacked-numerology outliers; the engine computes entirely on z=4. This doc does the **narrow substitution check** the resolution doc left open: does the neutrino sector's "3" survive the diamond by re-grounding on the **3 Cosserat microrotational sectors** (the spin's SU(2) generators, present on every 6-DOF node regardless of coordination) and/or the **trefoil crossing number** (a knot invariant), or is it irreducibly the z=3 bond-count?

**Skill-selection plan (fired this session):**
- `ave-prereg` — corpus-grepped the full ch03-neutrino-sector + the cross-leaf "3"-footprint before any conclusion (§1).
- `substrate-native-check` — the 3 Cosserat sectors (Ax 1 microrotational DOF) + the trefoil knot invariant are the candidate substrate-native groundings; walked the V-sector-vs-Cos-sector + the Op14 cross-sector transfer mechanism (§3).
- `consistency-vs-emergence` — classified the re-grounding (δ_CP is consistency-class; the substitution is a re-attribution, not an emergence-class re-derivation; Step 8 canonical-ceiling check applied) (§4).
- `verify-before-cite` — every file:line below was grepped/read this session in the worktree at `d5b71d5c`; verbatim quotes pulled from the read.
- `ave-canonical-leaf-pull` — enumerated the canonical leaves carrying the "3" (chiral-screening, delta-cp-violation, pmns-eigenvalues, index, vol2/claim-quality, eq_axiom_1.tex).
- `ave-discrimination-check` — checked whether the re-grounding touches the neutrino sector's genuinely-novel content (§4, the JUNO falsifier note).
- `flag-don't-fix` — the walk-back is **surfaced, not executed**; the axiom-vs-leaf contradiction is surfaced with both verbatim file:lines (§5).

**Honest framing up front.** This is a **consistency-class** sector throughout (FI-13 already reclassified θ₁₃ from emergence Class D to consistency Class C: c_1·c_3=45 is chosen-not-derived). The re-grounding does **not** change that class — it fixes the *why* behind the "3," not the predictive status. No new substrate primitive is introduced (the 3 Cosserat sectors are already canonical Axiom 1 content), so per Step 8c the classification **stays at the canonical ceiling** — this is not a promotion.

---

## §1 — The trace: where the "3" actually enters

There are **two distinct "3"s** in the neutrino sector, with **different physical roles** and **different re-grounding fates**:

### (A) The δ_CP "1/3" term (the chiral-phase share)

Verbatim, `delta-cp-violation.md:23`:

> *"$\pi/3$: One K4 bond's share of the structural chirality. Because the lattice is 3-connected, each bond carries $1/3$ of the total chiral phase. Equivalently, $1/c_{\text{trefoil}} = 1/3$ — the trefoil has $c = 3$ crossings *because* the K4 lattice is 3-connected. These are the same geometric fact."*

This line is the crux. It **welds three readings of the "3" into one** and explicitly attributes the *primary* reading to **bond-count** ("Because the lattice is 3-connected, each bond carries 1/3"), with the trefoil reading as "equivalently," and a *causal* claim ("the trefoil has c=3 crossings **because** the K4 lattice is 3-connected"). The δ_CP result itself (`delta-cp-violation.md:17`, `:33`; `index.md:26`): $\delta_{CP} = (1 + 1/3 + 1/45)\pi = 61\pi/45 = 1.3556\pi$ (NuFIT 1.36, 0.3%).

### (B) The Δc_crit = 3 screening threshold (the θ₁₃ regime selector)

Verbatim, `chiral-screening.md:11,13`:

> :11 *"The SRS/K4 lattice is chiral … and 3-connected: each node has exactly 3 bonds."*
> :13 *"To couple two torsional modes with crossing number difference $\Delta c$ … Each K4 bond transfers at most 1 unit per interaction. With 3 bonds per node, the maximum single-interaction transfer is:"* → `:18` $\Delta c_{\text{crit}} = 3$.

This is an **explicit bond-count derivation**: 3 bonds × 1 unit/bond = 3 units max transfer. Then `chiral-screening.md:24` welds the same three facts:

> *"The screening threshold $\Delta c_{\text{crit}} = 3$ is simultaneously the K4 lattice connectivity, the trefoil crossing number, and the number of Cosserat sectors. These three facts are structurally identical: the trefoil has $c = 3$ crossings *because* the K4 lattice is 3-connected."*

The same weld appears at the **claim-quality** level, `vol2/claim-quality.md:218` (entry `clm-7o8clt`, conf 0.6):

> *"The chiral screening threshold $\Delta c_{crit} = 3$ is simultaneously the K4 lattice connectivity, the trefoil crossing number, and the number of Cosserat sectors — these three facts are structurally identical, not independent coincidences."*

— and `clm-7o8clt`'s `depends-on` (`vol2/claim-quality.md:232`) lists *"INVARIANT-S2 / Axiom 1 (K4 3-connectivity = trefoil c=3 = Δc_crit; torus-knot crossing numbers)."* `index.md:11` lists the three derivation inputs as *"the torus knot crossing numbers (c_1=5, c_3=9), the vacuum Poisson ratio (ν_vac=2/7), and the K4 lattice connectivity (3)."*

**Where the "3" enters — verdict:** In **both** (A) and (B), the corpus text makes **bond-count ("3-connected", "3 bonds per node")** the *primary* reading, with trefoil-crossings and Cosserat-sectors asserted as **welded-identical** ("the same geometric fact", "structurally identical, not independent coincidences", "the trefoil has c=3 crossings *because* the lattice is 3-connected"). So as *written*, the "3" enters via **bond-count**, and the sector/crossing readings ride along only because the corpus asserts they are the same number. **That weld is exactly what z=4 breaks** (§2–§3): under the diamond, bonds = 4 while Cosserat-sectors = 3 and trefoil-crossings = 3 — the three are **no longer identical**, and the corpus's "not independent coincidences" claim becomes **false**.

---
