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

## §2 — The three groundings, and the δ_CP arithmetic

The three candidate sources of the "3", and whether each survives z=4 diamond:

| Grounding | What "3" is | z-dependent? | Survives z=4 diamond? | Canonical anchor |
|---|---|---|---|---|
| **Bond-count** | lattice coordination number z (= number of nearest-neighbor bonds per node) | **YES** — z=3 srs vs z=4 diamond | **NO** → becomes **4** | `chiral-screening.md:11` (z=3); contradicted by `eq_axiom_1.tex:20` (z=4) |
| **Cosserat sectors** | the 3 microrotational DOF $\omega_x,\omega_y,\omega_z$ (spin's SU(2)/SO(3) generators) on every 6-DOF node | **NO** — 3D rotation has 3 generators regardless of coordination | **YES** → stays **3** | `eq_axiom_1.tex:20` ("three microrotational … origin of intrinsic spin") |
| **Trefoil crossings** | $c_{\text{trefoil}} = 3$, the minimal crossing number of the (2,3) torus knot | **NO** — knot invariant, lattice-independent | **YES** → stays **3** | `delta-cp-violation.md:23` ("$1/c_{\text{trefoil}} = 1/3$") |

Two of the three (sectors, crossings) are z-**independent** and survive; only bond-count moves. The whole question is **which of the three was load-bearing** for the number — and the corpus, by welding them, never had to decide. z=4 forces the decision.

### §2.1 — δ_CP arithmetic: does per-sector restore 1.3556π on z=4?

The δ_CP middle term is the only one in play; the $\pi$ base (torsional half-turn, `delta-cp-violation.md:22`) and the $\pi/45$ junction term ($1/(c_1 c_3)$, `delta-cp-violation.md:24`) do **not** involve the connectivity "3":

| Grounding (middle term) | middle = | $\delta_{CP}/\pi = 1 + \text{middle} + 1/45$ | exact | vs NuFIT 1.36 |
|---|---|---|---|---|
| z=3 per-bond (**original**) | $1/3$ | $1 + 1/3 + 1/45$ | $61/45 = \mathbf{1.3556}$ | **0.3% ✓** |
| z=4 per-bond (**naive flip**) | $1/4$ | $1 + 1/4 + 1/45$ | $229/180 = \mathbf{1.2722}$ | ~6.5% (inside the wide $\pm0.2$ band, but degraded ~20×) |
| z=4 **per-sector** (3 Cosserat) | $1/3$ | $1 + 1/3 + 1/45$ | $61/45 = \mathbf{1.3556}$ | **0.3% ✓ RESTORED** |
| z=4 **per-crossing** (trefoil c=3) | $1/3$ | $1 + 1/3 + 1/45$ | $61/45 = \mathbf{1.3556}$ | **0.3% ✓ RESTORED** |

Worked: $1 = 180/180$, $1/4 = 45/180$, $1/45 = 4/180$ → $229/180 = 1.2722$ (z=4 bond). $1 = 45/45$, $1/3 = 15/45$, $1/45 = 1/45$ → $61/45 = 1.3556$ (per-sector / per-crossing).

**ANSWER (deliverable Q2): YES — per-sector restores 1.3556π exactly on z=4.** Because the per-sector denominator is the **3 microrotational DOF** (z-independent), the middle term stays $1/3$, not $1/4$. The restoration is exact, not approximate. Per-crossing (trefoil $c=3$, a knot invariant) gives the identical $1/3$ and is equally exact.

### §2.2 — per-sector vs per-crossing: which is the stronger grounding (for the neutrino)?

Both give $1/3$. For the **neutrino specifically**, the **Cosserat-sector grounding is stronger** than the trefoil-crossing grounding:

- The neutrino **IS a Cosserat torsional excitation** — `index.md:11`: *"a propagating helical coil in the Cosserat (torsional) sector of the lattice."* The chiral phase being divided is a **torsional** quantity, and torsion lives in the microrotational sector (Ax 1). Dividing the chiral phase over the **3 rotational generators** is physically native to the object.
- The "structural chirality" being shared is itself a **Cosserat order parameter** — resolution-doc point 3: *"Chirality = a `k_χ` Cosserat order-parameter on the diamond."* So the natural denominator of "share of the structural chirality" is the 3 Cosserat components, **not** the bonds and **not** the trefoil.
- The trefoil $c=3$ is **NOT the neutrino's own topology**: `index.md:11` says the neutrino is *"an open helix with $c$ turns … not a closed loop"* with $c = 5,7,9$. The trefoil (the (2,3) torus knot, $c=3$) is a **borrowed** reference chiral unit (the minimal (2,q) knot), not the neutrino soliton. So per-crossing grounds the neutrino's δ_CP on an object the neutrino is not.

The trefoil grounding is, in the **abstract**, the most lattice-independent kind (a knot invariant cannot move with the net) — but for *this* observable the Cosserat-sector grounding is the better-motivated one. **Net: per-crossing is weaker than per-sector for the neutrino** (borrowed topology), though both restore the number.

---

## §3 — The sharper exposure: Δc_crit = 3 → 4 and the θ₁₃ screening flip

δ_CP **survives even the naive bond-flip** (1.272π is still inside the wide ±0.2 NuFIT band). The θ₁₃ screening threshold does **not** — this is where the z=3→z=4 question actually has teeth.

### §3.1 — The θ₁₃ flip arithmetic

θ₁₃ is the $\nu_1\leftrightarrow\nu_3$ mixing, a $\Delta c = |9-5| = 4$ transition. `delta-cp-violation.md:30` classifies it *"Screened ($\Delta c = 4 > 3$)"*; `pmns-eigenvalues.md:40,43` confirm *"Screened Regime … $\Delta c = 4 > \Delta c_{\text{crit}} = 3$ … Only perturbative junction coupling survives"* → $\sin^2\theta_{13} = 1/(c_1 c_3) = 1/45$. **The smallness of θ₁₃ is entirely a consequence of being screened.** Unscreen it and it falls back to the compliance formula $\sin^2\theta \sim \Delta c/c$ (cf. `pmns-eigenvalues.md:25`, $\theta_{12}: \Delta c/c_2 = 2/7$):

| Grounding | Δc_crit | θ₁₃ test (Δc=4) | $\sin^2\theta_{13}$ | vs NuFIT 0.0220 |
|---|---|---|---|---|
| z=3 per-bond (**original**) | **3** | $4 > 3$ → **SCREENED** | $1/(c_1c_3) = 1/45 = 0.0222$ | **1.0% ✓** |
| z=4 per-bond (**naive flip**) | **4** | $4 > 4$? **NO** → **UNSCREENED** (compliance) | $\sim \Delta c/c = 4/9 \approx 0.44$ | **~20× off ✗ CATASTROPHIC** |
| z=4 **per-sector** (3 Cosserat) | **3** | $4 > 3$ → **SCREENED** | $1/45 = 0.0222$ | **1.0% ✓ PRESERVED** |

(θ₁₂ at Δc=2 and θ₂₃ at the midpoint are **robust either way**: $2 \le 3$ and $2 \le 4$ both leave θ₁₂ in compliance; θ₂₃ is the threshold-independent impedance-matched midpoint. **Only θ₁₃ sits on the knife-edge** — it is the single prediction that lives or dies on whether Δc_crit is 3 or 4.) So: if Δc_crit is irreducibly bond-count, θ₁₃ does not merely degrade like δ_CP — it **breaks ~20×** (0.022 → ~0.44). This is why the resolution doc called Δc_crit the sharper exposure.

### §3.2 — Does Δc_crit re-ground on the 3 Cosserat sectors?

This is the **one genuinely load-bearing physics call**, and it is **harder** than the δ_CP one. Two readings, both with real physical content:

**Bond-channel reading (as written, `chiral-screening.md:13`).** *"Each K4 bond transfers at most 1 unit per interaction. With 3 bonds per node, the maximum single-interaction transfer is Δc_crit = 3."* The transfer of torsional angular momentum between nodes is an **inter-node** process, and inter-node coupling physically goes **through bonds**. This is **not** an empty heuristic — the Op14 cross-sector trading mechanism (`op14-cross-sector-trading.md:11`) shows torsional/Cosserat energy is exchanged *"via the bond LC tank's inductive side"* (the $\Phi_{\text{link}}$ channel, empirically $\rho(H_{\text{cos}}, \Sigma|\Phi_{\text{link}}|^2) = -0.990$). So the **carrier** of torsional-AM transfer genuinely is the bonds. Under this reading Δc_crit = z = **4**, and θ₁₃ breaks.

**Cosserat-sector reading (the candidate re-grounding).** Torsional angular momentum is an **SO(3)/SU(2) object with exactly 3 independent components** ($\omega_x,\omega_y,\omega_z$) — the same 3 microrotational DOF Ax 1 names as the origin of spin (`eq_axiom_1.tex:20`). A single coupling event can exchange **at most one quantum per rotational channel** → **at most 3 independent units**, *regardless of how many bonds carry them*. This is a **selection rule set by the mediator's angular-momentum content** (the standard origin of selection rules: Δℓ is bounded by the mediator's spin, not by the number of spatial channels), not a channel-count. Under this reading Δc_crit = 3 (z-independent), and θ₁₃ is preserved.

**Honest adjudication.** The two readings are **not** the same kind of statement, and the corpus conflated them only because z=3 made channel-count = component-count:
- The δ_CP "share of structural chirality" divides a **chirality order-parameter that already lives in the Cosserat sector** (resolution point 3) — so re-grounding it on the 3 Cosserat components is a **near-relabel**: the quantity was always Cosserat; the "per bond" wording was a coincidental mislabel. **Clean.**
- The Δc_crit "max transfer per interaction" is a **transport-capacity** statement, and transport genuinely has a **bond carrier** (Op14/Φ_link). Re-grounding it on the 3 Cosserat sectors requires **replacing the bottleneck**: from "how many bond channels" (z=4) to "how many independent angular-momentum components the source/sink can hold" (3). That is a **genuine mechanism-substitution**, not a wording fix. It is **physically defensible** — arguably *more* fundamental, since the transferred quantity (self-linking / twist / torsional AM) is intrinsically 3-component and cannot exceed 3 independent quanta even with 4 bonds — but it is **not free**, and it is exactly the kind of substrate-physics call that per `substrate-native-check` (Rule 16) should go to Grant rather than be decided unilaterally by the implementer lane.

**ANSWER (deliverable Q3): Δc_crit CAN re-ground on the 3 Cosserat sectors — via the intrinsic-3-component-angular-momentum (SU(2) selection-rule) argument — and IF it does, Δc_crit stays 3 and θ₁₃ screening is preserved.** But it is **not irreducible-either-way**: as *written* it is bond-count (→4, θ₁₃ breaks), and the re-grounding is a **genuine mechanism-substitution** (not a relabel like δ_CP), because torsional-AM **transport** has a real bond carrier (Op14). So Δc_crit is **re-groundable but contested** — the load-bearing call is *"is the screening bottleneck the bond-channel count (z=4) or the angular-momentum-component count (3)?"* — and that is the **one question for Grant**.

---
