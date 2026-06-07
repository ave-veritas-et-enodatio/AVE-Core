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

## §4 — Classification: legitimate re-derivation, or post-hoc relabel? (consistency-vs-emergence)

**The numbers are preserved by per-sector and CHANGED by per-bond-at-z=4.** That is settled arithmetic (§2.1, §3.1). The honest question (deliverable framing #5) is whether the per-sector substitution is a *legitimate re-derivation* or a *post-hoc relabel*. Answer, split by term:

- **δ_CP "1/3": legitimate re-attribution, preserves the number.** The chiral phase is torsional and the chirality is a Cosserat order-parameter (resolution point 3) — the quantity *was always* a 3-Cosserat-component object; the "per K4 bond" wording (`delta-cp-violation.md:23`) was a **coincidental mislabel** that read true only because z=3 made bonds = sectors. The re-grounding does not invent the 3 from new physics; it **re-attributes an already-correct number to its true z-independent source**. This is the good kind of relabel — physically motivated, number-preserving.

- **Δc_crit "3": number-preserving ONLY under a contested mechanism-substitution.** Here the per-sector reading is **not** a near-relabel (§3.2): the written mechanism (bond transport, Op14-carried) genuinely points at z=4. Preserving the number requires *adopting the SU(2)-selection-rule bottleneck over the bond-channel bottleneck* — a real physics choice. If Grant adjudicates the selection-rule reading, the number is preserved legitimately; if he adjudicates the transport reading, θ₁₃ walks back.

**Per-bond and per-sector give the same "3" ONLY because the per-bond reading was coincidental — say which: it was coincidental.** At z=3, coordination = Cosserat-component-count = trefoil-crossing-count = 3, so the corpus could weld all three (`chiral-screening.md:24`, `vol2/claim-quality.md:218`) and never decide which was load-bearing. The weld's own words — *"structurally identical, not independent coincidences"* — are **falsified by z=4**: the diamond makes coordination = 4 while the other two stay 3, so they ARE independent, and **two of the three (sectors, crossings) were the real carriers; bond-count was the coincidental passenger.**

**Consistency-vs-emergence class (unchanged by the re-grounding).** δ_CP and θ₁₃ are **Class C consistency-class** already (FI-13: $c_1=5$ chosen-not-derived → $c_1 c_3 = 45$ is a consistency identification, not emergence). The re-grounding fixes the *provenance of the "3,"* not the predictive status — it does **not** lift the class. Per `consistency-vs-emergence` Step 8 (classification-promotion check): the 3 Cosserat sectors are **already canonical Axiom 1 content** (`eq_axiom_1.tex:20`), so **no new substrate primitive** is introduced; classification **stays at the canonical ceiling** (Step 8c). This is a wording/provenance correction, NOT a solidity promotion. `clm-7o8clt` (0.60) and `clm-rji99i` (0.55) confidences should **not** move on the strength of the re-grounding.

**Discrimination-check note (the novel content is untouched).** The neutrino sector's one genuinely-forward / falsifiable claim — the **inverted mass hierarchy** ($m_i \propto 1/c_i^2$, $m_1>m_2>m_3$, the JUNO falsifier per `delta-cp-violation.md:40,63-77`) — depends on the **crossing numbers 5,7,9**, NOT on the connectivity "3." It is **completely unaffected** by the z=3↔z=4 question and survives regardless of how the "3" re-grounds. The re-grounding is housekeeping on the consistency-class PMNS angles; it does not touch the sector's discriminating prediction.

---

## §5 — FLAG (don't fix): the axiom-vs-leaf contradiction the weld was hiding

Surfaced per flag-don't-fix, with both verbatim file:lines. This is the **load-bearing internal contradiction**, and it predates this session — the weld at `chiral-screening.md:24` was masking it:

- **Canonical Axiom 1** — `manuscript/common_equations/eq_axiom_1.tex:20` (verbatim): *"…governed by the right-handed $I4_1 32$ chiral space group, **with 4-fold K4 nearest-neighbor connectivity at each node**. Each node is micropolar (Cosserat-type), carrying six intrinsic degrees of freedom per node: **three translational** … and **three microrotational** …"* → coordination **z = 4**; the "3" is the **microrotational sector count**, explicitly distinct from connectivity.

- **Neutrino leaf** — `chiral-screening.md:11` (verbatim): *"The SRS/K4 lattice is chiral … and **3-connected: each node has exactly 3 bonds**."* → coordination **z = 3**.

These **directly contradict**: the axiom says **4-fold connectivity + 3 microrotational DOF**; the neutrino leaf says **3 bonds** and then welds connectivity ≡ trefoil ≡ sectors. The resolution-of-record adjudicated **z = 4** (axiom wins; the z=3 srs leaves are the outliers). So `chiral-screening.md:11`'s "3 bonds" is **already wrong against the canonical axiom**, independent of the neutrino arithmetic. **Crucially, Axiom 1 itself already separates the two "3"s** the neutrino leaf welded: it puts **4** on connectivity and **3** on the microrotational sectors. That is the strongest possible support for the per-sector re-grounding of δ_CP — *the axiom already says the sector-3 and the connectivity-number are different things, and the connectivity number is 4.*

**Adjacent contradiction (same root, outside the neutrino sector — surfaced, not in scope to fix):** `vol1/claim-quality.md` is **internally inconsistent** on the same axis — `:141` asserts *"chiral SRS net (coordination z = 3)"* while `:1188` asserts *"K4 graph topology (4-neighbor connectivity, Axiom 1)."* Both in one file. Flagged for the broader z=3-leaf walk-back the resolution doc already queued; not a neutrino-sector item.

**Terminology hazard to disambiguate (flag, do not silently resolve):** the phrase "**3 Cosserat sectors**" is used with **two different meanings** in the corpus. (i) Here / resolution-doc / `eq_axiom_1.tex:20`: the **3 microrotational components** $\omega_x,\omega_y,\omega_z$ (the SU(2) generators). (ii) `vol1/claim-quality.md:520`: *"Three Cosserat sectors (translation, rotation, curvature-twist) produce three lepton generations"* — a **different triplet** (three DOF-*types*, not the three rotational components). The δ_CP / Δc_crit re-grounding relies on reading (i). If the walk-back wording uses "3 Cosserat sectors," it must specify **reading (i)** explicitly, or the two will collide.

---

## §6 — Walk-back recommendation (SURFACED, not executed)

Per flag-don't-fix and lane discipline, I do **not** execute any of this; I surface it for Grant + the auditor lane. The verdict splits cleanly on Grant's one Δc_crit adjudication:

### If Grant adjudicates Δc_crit → 3 (Cosserat SU(2) selection-rule): KEEP z=4, FIX WORDING

Re-ground (don't delete) the bond-attribution in these spots; the numbers are all preserved:

| Leaf:line | Current (bond-count) | Re-ground to |
|---|---|---|
| `chiral-screening.md:11` | "3-connected: each node has exactly 3 bonds" | z=4 diamond connectivity; the screening "3" is the **3 Cosserat microrotational sectors** (reading (i)), not the bond count |
| `chiral-screening.md:13` | "Each K4 bond transfers at most 1 unit … 3 bonds per node → Δc_crit=3" | torsional AM is intrinsically 3-component (SU(2)); max 3 independent quanta per interaction regardless of z |
| `chiral-screening.md:24` | "structurally identical: the trefoil has c=3 *because* the lattice is 3-connected" | **sever the weld** — sectors (3) and trefoil-crossings (3) coincide; connectivity (4) does **not**; they are **not** "the same geometric fact" |
| `delta-cp-violation.md:23` | "One K4 bond's share … because the lattice is 3-connected, each bond carries 1/3" | one **Cosserat-sector's** share of the chiral order-parameter; 3 sectors → 1/3 (equivalently 1/c_trefoil) |
| `delta-cp-violation.md:30` | "Screened (Δc = 4 > 3)" | keep — but footnote that the "3" is Δc_crit = **sector count**, not connectivity |
| `index.md:11`, `:22` | "K4 lattice connectivity (3)" / "(K4 connectivity = trefoil crossing number)" | "3 Cosserat microrotational sectors (= trefoil c=3)"; drop "connectivity" |
| `vol2/claim-quality.md:217,218,232` | "K4 lattice connectivity (3)"; "structurally identical, not independent coincidences"; depends-on "K4 3-connectivity" | re-ground input to "3 Cosserat sectors"; **delete the "not independent coincidences" claim** (z=4 falsifies it); fix the depends-on |

This is the **clean (sector-grounded) outcome**: numbers preserved, provenance corrected, **no prediction lost**, solidity unchanged (no promotion — §4).

### If Grant adjudicates Δc_crit → 4 (bond-transport bottleneck): WALK BACK θ₁₃ (Rule 12)

δ_CP still re-grounds and survives (per-sector restores 1.3556π; even naive bond-flip stays in-band). But θ₁₃ **unscreens and breaks ~20×** (0.022 → ~0.44). Then per Rule 12 (substitution-not-retraction): preserve the body, add a 🔴 header to the θ₁₃ screened-regime derivation (`pmns-eigenvalues.md:40-49`, `delta-cp-violation.md:30`), and the "all four PMNS from three inputs" framing (`index.md:11`, `vol2/claim-quality.md:217`) loses θ₁₃ → "three of four." θ₁₂, θ₂₃, δ_CP, and the inverted-hierarchy JUNO falsifier survive. This is the **messy outcome — but note it is messy only at Δc_crit, and only if the transport reading wins.**

**My read (implementer lane, non-binding):** the SU(2)-selection-rule reading is physically the stronger one — the transferred quantity (self-linking / torsional AM) is intrinsically 3-component and cannot exceed 3 independent quanta even on a 4-bond node, and **Axiom 1 already separates connectivity (4) from the rotational-sector count (3)**. But the Op14/Φ_link bond-carrier is real, so this is genuinely Grant's call, not mine.

---

## §7 — Deliverable verdict + return summary

1. **Where the "3" enters:** bond-count is the **primary written reading** in both terms (`chiral-screening.md:11,13`; `delta-cp-violation.md:23`; `index.md:11`; `vol2/claim-quality.md:217,232`), with trefoil-crossings + Cosserat-sectors **welded as "structurally identical"** (`chiral-screening.md:24`, `vol2/claim-quality.md:218`). The weld is what z=4 breaks.

2. **δ_CP on z=4:** **YES, per-sector restores 1.3556π exactly** (middle term 1/3, not 1/4; $61/45$, NuFIT 0.3%). Per-crossing equal; per-sector the stronger grounding for the neutrino.

3. **Δc_crit / θ₁₃:** re-grounds on the 3 Cosserat sectors **via a genuine SU(2)-selection-rule mechanism-substitution** (→ stays 3, θ₁₃ preserved) — but as *written* it is bond-count (→ 4, θ₁₃ breaks ~20×) and the substitution is **contested** (Op14/Φ_link gives torsional-AM transport a real bond carrier). **The one question for Grant.**

4. **Verdict:** **KEEP z=4 + fix the bond-wording** (clean, sector-grounded outcome) — **conditional on Grant adjudicating Δc_crit = 3 via the angular-momentum-component reading.** δ_CP's re-grounding is clean and unconditional; **only θ₁₃ hangs on the Δc_crit call.** If Grant takes the bond-transport reading instead, walk back θ₁₃ alone (Rule 12) — δ_CP and the JUNO falsifier survive either way. **Outcome is clean (sector-grounded), with one genuine-physics caveat localized to Δc_crit — NOT messy z=3-dependence across the board.**

5. **Flagged (not fixed):** `eq_axiom_1.tex:20` (z=4 + 3 microrotational) **directly contradicts** `chiral-screening.md:11` (z=3, 3 bonds) — the axiom already separates connectivity-4 from sector-3, which is itself the strongest support for the re-grounding. Adjacent: `vol1/claim-quality.md:141` (z=3) vs `:1188` (z=4) self-contradiction; "3 Cosserat sectors" terminology collision (`eq_axiom_1.tex:20` ω-components vs `vol1/claim-quality.md:520` DOF-types).

**Doc:** `research/2026-06-07_neutrino-3-regrounding-check.md`
**Branch:** `analysis/2026-06-07-neutrino-3-regrounding` (off `origin/main` @ `d5b71d5c`) — pushed, NOT merged.

