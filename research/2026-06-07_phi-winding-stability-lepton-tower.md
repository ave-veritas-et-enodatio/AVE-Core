[↑ Research](index.md)

# φ-Winding-Stability + KAM Lepton-Tower — the LAST open α-route (PREREG + ALPHA-FREE FIRST-PASS)

**Date:** 2026-06-07
**Status:** PREREG + FIRST-PASS RESULT. **VERDICT: the route HITS THE UNFORCED-φ WALL.** Both conjuncts of the hypothesis fail under an α-free examination. The §18 Golden-Torus FIT verdict **STANDS** — and is no longer contingent on *this* route (the one route §20 left open is now examined and closed at the wall). One first-principles route (z₀-from-K4 rigidity-percolation) remains separately open.
**Branch:** `analysis/2026-06-07-phi-winding-stability` (off `origin/main`; worktree-isolated).
**Driver:** [`src/scripts/vol_1_foundations/phi_winding_stability_kam_firstpass.py`](../src/scripts/vol_1_foundations/phi_winding_stability_kam_firstpass.py) (α-free first-pass; `make verify` clean).
**Predecessor:** the epic-doc §20 hinge (`AVE-Core-genesis-wt/_orchestration/2026-06-07_electron-synthesis-epic.md:174-181`); the two prior α-¼ negatives ([`2026-06-04_alpha-class2-bijection-result.md`](2026-06-04_alpha-class2-bijection-result.md) kinematic bridge; [`2026-06-04_alpha-quarter-adversarial-rechallenge.md`](2026-06-04_alpha-quarter-adversarial-rechallenge.md) ¼-relaxation).

> **⚠ ANTI-PATTERN MARKER.** This is the THIRD distinct α-¼-emergence framing to be examined and closed (after the ¼-relaxation engine tests and the kinematic unit-bridge). The φ-winding-stability framing was the one the prior two negatives explicitly left UNTESTED (`2026-06-04_alpha-quarter-adversarial-rechallenge.md:54`: *"the secondary predictions — KAM lepton-tower … — are untested"*). It is now examined. The recurring rescue SHAPE (*"the prior negatives tested the wrong layer; the REAL mechanism (KAM winding-stability) selects φ"*) fails for a single, structural reason given in §8. Do not reconstruct it a fourth time without reading §8.

---

## §0 TL;DR

The ONLY open α-route (epic §20) is: **is φ FORCED as the most-stable electron winding** → R·r=¼ in pure ℓ_node² geometry (NO voltage bridge, NO α-substitution) → α⁻¹=4π³+π²+π=137.036 a genuine derivation of the observable? It requires **two conjuncts, BOTH of which must hold**:

- **(a)** the electron PICKS the most-stable winding (a *selection-principle* hypothesis), AND
- **(b)** the (2,3) winding FORCES R/r=φ² (a *geometry-forcing* hypothesis).

**Both fail, α-free:**

- **(a) FALSE.** KAM "most-stable = most-irrational" selects the **irrational golden mean φ** — a quasiperiodic orbit that **never closes** (not a localized particle) — and its best *rational* approximants are the **Fibonacci ladder** (2,3)→(3,5)→(5,8)→…, where stability *increases* with index. (2,3)=3/2 is the **LEAST-stable** golden convergent (|q/p−φ|=0.118, the largest in the ladder, driver [2]). The corpus selects (2,3) by **MINIMALITY** (smallest crossing c=3, lightest lepton — `torus-knot-uniqueness.md:85-93` §6), which is the **OPPOSITE** selection principle from "most-stable." So the electron does NOT pick the most-stable winding; it picks the *simplest* one.
- **(b) FALSE.** KAM stability constrains the **rotation number** (winding / frequency ratio q/p), **not** the geometric **aspect ratio** R/r. These are **independent DOF of the same phasor Lissajous**. The (2,3) knot's own natural (geodesic) aspect ratio is **q/p = 3/2**, NOT φ²=2.618 (driver [3]). No (2,q) winding has geodesic aspect ratio φ². KAM cannot force R/r=φ².

**The discriminator the brief proposed — (2,5),(2,7) → m_μ, m_τ α-free — does not exist as a KAM object** (§5): no α-free (p,q)→mass relation is in the corpus; the corpus lepton tower is α-DEPENDENT Cosserat torsion on FIXED (2,3); and (2,5),(2,7) are the corpus **BARYON** topologies (proton, Δ), retired as lepton assignments at FI-13 (`torus-knot-uniqueness.md:112-118`).

**Honest one-line answer to "is (2,3)→φ DERIVED or ASSERTED":** **ASSERTED** (a co-location of two orthogonal constraints on one LC tank). The KAM framing does not convert the assertion to a derivation — it *relocates* the gap and introduces a new **rational-resonant vs irrational-quasiperiodic** tension the corpus's own minimality+three-regime derivations do not carry.

---

## §1 The claim, scoped honestly (PREREG)

**Corpus claim under test** (epic §20:177, verbatim): a *"winding-stability / KAM argument that R/r=φ² (the (2,3) most-irrational, hardest-to-phase-lock winding) is the UNIQUELY STABLE, FORCED electron winding → pins R·r=¼ in pure ℓ_node² geometry (NO voltage bridge, NO α-substitution) → α⁻¹=4π³+π²+π=137.036 becomes a genuine derivation of the OBSERVABLE."*

**Why the route, if it held, would flip §18.** §18 found R·r=¼ is a FIT: the substrate's own α-free derivation forces R·r→4π²α≈0.288 (not ¼); ¼ is recovered only by substituting α. The chain there runs **R·r=¼ ⇒ φ** (`ch8-alpha-golden-torus.md:75-79`), with φ a *shadow* of the α-absorbing ¼. The φ-stability route would **reverse the arrow**: establish R/r=φ² as a *primary* geometric fact (via KAM), then R·r=¼ follows from {R/r=φ², R−r=½} **with no α-substitution**. The driver [1] confirms this algebra exactly:

> {R/r=φ², R−r=½} ⟹ R·r=¼, R=φ/2, r=(φ−1)/2 — **engine-checked, α-free** (driver [1], asserts pass to 1e-12).

So the **entire** route reduces to one question: **can KAM establish R/r=φ² as primary?** Everything below is the examination of that question. The R−r=½ self-avoidance leg (regime (b), `ch8:45`) is α-free and not at issue; the contested leg is R/r=φ².

**The two conjuncts, restated as pre-registered claims:**

| Conjunct | Claim | Status after first-pass |
|---|---|---|
| **(a)** | the electron picks the **most-stable** winding | **FALSIFIED** (§3, §4) — corpus selects by minimality; (2,3) is the least-stable golden convergent |
| **(b)** | the (2,3) winding **forces** R/r=φ² | **NOT FORCED** (§3) — KAM acts on winding, not aspect ratio; independent phasor DOF |

---

## §2 ALPHA-CIRCULARITY GUARD (headlined — every input traced)

Per `consistency-vs-emergence` v1.3. The route's prize is α⁻¹ as a **Class D emergence** (dimensionless observable from primitives with NO α input). The guard: trace every input to this first-pass and confirm α never enters the construction.

| Quantity | Source | α-free? |
|---|---|---|
| Winding integers (p,q), Fibonacci F_n | pure integers | ✅ |
| φ = (1+√5)/2, φ² | `constants.PHI` (√5, no α) | ✅ |
| KAM stability proxy (|q/p − φ|, continued-fraction) | pure number theory | ✅ |
| Geodesic aspect ratio R/r = q/p | torus-knot geometry | ✅ |
| Crossing c, Hopf Q_H, self-link SL | topological invariants of (p,q) | ✅ |
| {R/r=φ², R−r=½} ⟹ R·r=¼ algebra | √5-quadratic | ✅ |
| CODATA m_μ/m_e=206.768, m_τ/m_e=3477.23 | **comparison-only targets** (never fit) | n/a |
| corpus m_μ=1/(α√(3/7)), m_τ=8π/α | **α-DEPENDENT, printed for contrast only** | ❌ (this is the point — the existing tower USES α) |

The construction (conjuncts (a),(b)) is **α-free on input**. α appears ONLY in the comparison print, to exhibit that the corpus lepton tower *uses* α and that no α-free (p,q)→mass relation exists. **Classification of the target:** IF the route closed, α⁻¹ would lift to **Class D emergence**; the first-pass finds it does NOT close, so α⁻¹ remains **Class B substrate-mechanism manifestation + Class 4 observable consistency** — the existing §18 / `ch8:148` classification, **unchanged**.

---

## §3 The KAM argument, made rigorous — and the (2,3)↔φ crux

### §3.1 What KAM actually says (the sound part)

KAM (Kolmogorov–Arnold–Moser) + Greene's residue + Aubry–Mather: under a non-integrable perturbation of an integrable Hamiltonian, invariant tori are destroyed in order of how well their **rotation number** ρ (the ratio of the two angular frequencies) is approximated by rationals. **Resonant (rational) tori** ρ=p/q break **first** (Poincaré–Birkhoff). The **last torus to survive** is the one whose ρ is **hardest to approximate by rationals** — the **most-irrational number** — which is the **golden mean φ** = [1;1,1,1,…] (all continued-fraction partial quotients = 1, the slowest-converging CF). This much is standard and correct. **Ground 1 corpus finding: this KAM property is ABSENT from the AVE corpus** — the golden torus is NOT grounded via KAM anywhere; it is derived via the three substrate regimes (`ch8:41-46`). So the KAM argument is an *import*, not a corpus result.

### §3.2 The crux — three DISTINCT roles of φ, conflated by the route

The route's force comes entirely from the word "golden" appearing in three places. They are **three different mathematical objects**:

| Role | Object | Where it lives | Is it the electron? |
|---|---|---|---|
| **R1** | φ as an **irrational rotation-number** (KAM most-stable quasiperiodic orbit) | phase-space frequency ratio; **never closes** | **NO** — a non-closing orbit is not a localized particle |
| **R2** | φ² as a **torus aspect-ratio** R/r (the Golden-Torus *geometry*) | real-space / phasor-ellipse shape | the geometry, derived from {R−r=½, R·r=¼} |
| **R3** | (2,3) as a **rational torus-knot winding** (q/p=3/2) | (V_inc,V_ref) phase-space; **closes after 5 loops** | **YES** — the electron's winding |

KAM stability is a statement about **R1**. The electron is **R3**. The golden-torus geometry is **R2**. The route needs KAM-stability of R1 to transfer to R2 (forcing the aspect ratio) and to coincide with R3 (the electron). **Neither transfer is forced:**

- **R1 ≠ R3 (rational-resonant vs irrational-quasiperiodic).** The KAM-most-stable orbit (R1) is the *irrational* φ, which never closes — it cannot BE a closed (2,3) torus knot. Conversely (2,3)=3/2 is a **rational resonant** torus, the class that breaks **FIRST** under KAM. So the electron's winding is, by KAM's own ordering, among the *least* stable, not the most. The only bridge is "(2,3)=3/2 is the **Fibonacci convergent** of φ" — but (i) 3/2 is only the *3rd* convergent (driver [2]: |3/2−φ|=0.118, the **worst** of the ladder), and (ii) "closest rational to φ" selects the **infinite Fibonacci limit**, not (2,3). Driver [2]: (3,5)→0.049, (5,8)→0.018, (8,13)→0.007 — each MORE stable than (2,3). So if the electron picked the most-stable convergent, it would be the high-Fibonacci limit, **not (2,3)**.

- **R1 → R2 is a category leap (frequency-ratio → aspect-ratio², and why squared?).** Even granting winding-number=φ, that is a **frequency ratio**, not a geometric **aspect ratio** R/r. In the bond LC phasor, the (V_inc,V_ref) trajectory is a Lissajous ellipse: its **aspect ratio R/r is the eccentricity**, while its **winding is how the phasor rotates** — these are **independent DOF** (Ground 1's exact finding: "orthogonal constraints on the same LC tank"). KAM stabilizes the winding; it says nothing about the eccentricity. And the leap φ→φ² (a *square*) is unexplained: a rotation-number φ does not geometrically imply an aspect-ratio φ². Driver [3] makes this concrete: the (2,3) knot's own *geodesic* aspect ratio is **q/p = 3/2**, NOT φ²=2.618; no (2,q) has geodesic aspect ratio φ².

### §3.3 The honest answer: ASSERTED, not derived

**Is (2,3)→φ DERIVED or ASSERTED?** **ASSERTED** — a co-location, exactly as Ground 1 concluded. The (2,3) winding is DERIVED (knot minimality, `torus-knot-uniqueness.md` §1-§6). The golden-torus geometry R/r=φ² is DERIVED (three regimes, `ch8:41-79`) — but *downstream of* R·r=¼ (the α-absorbing knob), with φ a shadow. The **link** "(2,3) winding forces R/r=φ²" has **no corpus derivation**, and the KAM framing does **not** supply one: it would need R1→R2 and R1=R3, both of which fail. The KAM import, far from forcing φ, **introduces a new tension** (R1 irrational vs R3 rational) that the corpus's minimality+three-regime derivations avoid. **The unforced-φ gap §20 flagged is real and the KAM route does not close it.**

---

## §4 Conjunct (a) — "the electron picks the most-stable winding" is FALSIFIED by the corpus's own (2,3) derivation

The brief's weak-point (a) asks: *why most-stable, not lowest-energy/simplest?* The first-pass answers it decisively, α-free:

- The corpus's actual (2,3) selection principle is **MINIMALITY**: *"the electron MUST be (2,3) — it's the only assignment consistent with electron = lightest non-trivial stable lepton"* (`torus-knot-uniqueness.md:93`), forced by "smallest non-trivial coprime pair, lowest crossing number c=3" (§5-§6). This is **smallest/simplest**, the *opposite* of most-stable.
- Driver [2] shows (2,3) is the **LEAST-stable** golden convergent (|q/p−φ|=0.118 is the maximum over the ladder; every higher Fibonacci knot is more stable). So "(2,3) = the most-irrational, hardest-to-phase-lock winding" (epic §20:177) is **factually inverted**: among golden convergents, (2,3) is the *easiest* to phase-lock, not the hardest.
- "Most-stable" taken literally selects the **irrational φ-torus** (R1), which never closes — not a particle. Taken as "most-stable closed knot," it selects the high-Fibonacci limit (3,5),(5,8),… — **not (2,3)**, and an ever-growing knot, not a ground state.

So conjunct (a) is not merely unproven — it **contradicts** the corpus's load-bearing (2,3)-uniqueness derivation. The electron is the *simplest* winding; "most-stable" is a different, conflicting principle that does not land on (2,3).

---

## §5 The lepton-tower discriminator — NOT COMPUTABLE α-free (and why)

The brief: *if (2,5),(2,7) → m_μ, m_τ track the KAM winding-stability ordering ALPHA-FREE, that separates "φ forced by stability" from "¼ imposed, φ a shadow."* Per `consistency-vs-emergence`, I checked for an α-free (p,q)→mass relation before computing. **There is none, and the premise is false on three independent grounds (Ground 2 confirmed):**

1. **No α-free (p,q)→mass formula exists in the corpus.** The only lepton-mass framework is Cosserat-torsion, and it is **α-DEPENDENT** at every level: m_μ/m_e = 1/(α√(3/7)) ≈ 209.3 (`lepton-spectrum.md:37`), m_τ/m_e = 8π/α ≈ 3444 (`lepton-spectrum.md:59`). Both USE α (driver [4]).
2. **Leptons are NOT a (2,q) winding tower.** Per FI-13 (resolved 2026-05-18, `torus-knot-uniqueness.md:102-118`): leptons climb a **Cosserat-torsion ladder on FIXED (2,3) topology** (electron = (2,3)+0 quanta, muon = (2,3)+1, tau = (2,3)+N). They do **not** climb the (2,q) ladder.
3. **(2,5),(2,7) are the corpus BARYON topologies.** (2,5) = proton cinquefoil, (2,7) = Δ baryon (`torus-knot-uniqueness.md:54-57,112-116`). The brief's "(2,5),(2,7) leptons" assignment was **explicitly retired** at FI-13. So the discriminator's *premise* is a topology that the corpus assigns to a different particle family.

**Could the KAM-stability ordering of (2,q) reproduce the mass ladder anyway?** No, α-free: driver [4] reports the α-free invariants of (2,5),(2,7) (c=5,7; Q_H=10,14; SL=3,5) — none lands near 206.77 / 3477.23, and the (2,q) winding ratios (5/2, 7/2) **march away** from φ (driver [3]), so they are not even a KAM-stability tower. **Constructing an α-free f(p,q) that hits the masses by trying functions is the coincidence-magnet the brief warns against** — I did not do it; per `ave-discrimination-check` that would manufacture a false positive. The KAM-stable tower (if leptons were one) would be the **Fibonacci ladder** (2,3)→(3,5)→(5,8) (driver [2]), which is *neither* the corpus lepton tower *nor* the brief's (2,odd) tower.

**Discriminator verdict: it does not exist as a KAM object.** The test the brief proposed to separate "φ forced" from "φ shadow" cannot run, because its premise (α-free (2,q) lepton tower) is corpus-false. This is itself informative: the **absence** of an α-free lepton tower is consistent with "¼ imposed, φ a shadow" and provides **no** support for "φ forced by stability."

---

## §6 First-pass computation (driver) — the α-free record

[`phi_winding_stability_kam_firstpass.py`](../src/scripts/vol_1_foundations/phi_winding_stability_kam_firstpass.py), `make verify` clean. Key outputs (full run in commit):

- **[1]** {R/r=φ², R−r=½} ⟹ R·r=¼ exactly (R=0.8090169944=φ/2, r=0.3090169944=(φ−1)/2; asserts to 1e-12). *The would-be derivation's algebra is sound — the only missing piece is making R/r=φ² primary, which §3 shows KAM cannot do.*
- **[2]** Golden convergents = Fibonacci knots; |q/p−φ|: (2,3)→**0.1180** (worst), (3,5)→0.0486, (5,8)→0.0180, (8,13)→0.0070, … (monotone-decreasing). **(2,3) is the least-stable convergent; the KAM-stable ladder grows both indices.**
- **[3]** (2,q) geodesic aspect ratios vs φ²=2.618034: (2,3)→1.5 (|Δ|=1.118), (2,5)→2.5 (|Δ|=0.118), (2,7)→3.5, … **No (2,q) geodesic aspect ratio = φ²; (2,3)'s is 1.5.**
- **[4]** CODATA m_μ/m_e=206.768, m_τ/m_e=3477.23 vs corpus α-DEPENDENT 209.33 / 3444.09 (USE α); α-free invariants of (2,5),(2,7) land nowhere near the masses. **No α-free (p,q)→mass relation.**

---

## §7 Falsifier + outcome categories (PREREG discipline)

Pre-registered before adjudication; the route closes or flips on these:

| Outcome | Condition | What it would mean | Result |
|---|---|---|---|
| **φ-FORCED (route closes, α DERIVED)** | A substrate-native argument forces **R/r=φ² as primary** (independent of R·r=¼), AND an **α-free** secondary prediction (the lepton tower) confirms the KAM ordering | α⁻¹=4π³+π²+π lifts to **Class D emergence**; §18 FIT → DERIVED | ❌ NOT MET |
| **φ-SHADOW (route fails, FIT stands)** | KAM constrains only the winding, not R/r; (2,3) selected by minimality not stability; no α-free lepton tower | §18 FIT verdict STANDS; α value un-derived; φ a shadow of the α-absorbing ¼ | ✅ **MET** (§3,§4,§5) |
| **PARTIAL / NEW-HYPOTHESIS** | one conjunct holds, the other open | would warrant a scoped follow-up | ❌ — both conjuncts fail; nothing partial survives |

**The single falsifying mechanism (Rule 11 honest closure).** Every failure above has **one cause**: **KAM stability is a property of the rotation number (winding), and R/r=φ² is the geometric aspect ratio — an independent DOF of the same phasor Lissajous.** KAM cannot reach the aspect ratio; the winding it *can* reach is the irrational φ (not the rational, closed (2,3) particle), and is selected in the corpus by minimality (which makes (2,3) the *least*-stable convergent), not stability. One mechanism explains the (a)-failure, the (b)-failure, and the non-existence of the discriminator. **Clean negative; branch closed; no rescue attempted.**

---

## §8 Why the rescue always fails (anti-pattern, for the record)

The recurring α-¼ rescue SHAPE is *"the prior negatives tested the wrong layer ([static/cold/kinematic]); the REAL mechanism ([dynamical/warm/KAM]) selects R·r=¼."* The φ-winding-stability framing was the last untested instance of this shape. It fails because **R·r=¼ and R/r=φ² are the same algebra read two directions** (driver [1]); to make φ² *primary* you need a mechanism that fixes the **aspect ratio** R/r without first fixing R·r — and KAM, the proposed mechanism, fixes neither: it fixes a **rotation number**, a third quantity that (i) is irrational at the stable point (not the rational (2,3)), and (ii) is geometrically independent of the aspect ratio. The over-determination of ¼ by "≥6 routes" remains the coincidence-magnet tell (`2026-06-04_alpha-quarter-adversarial-rechallenge.md:54`): ½ is the generic fraction of resonant/spin-½/matched physics; KAM adds a *seventh* restatement of "it's a half-thing," not an independent derivation, and its one *discriminating* secondary prediction (the lepton tower) **does not exist** (§5).

---

## §9 PRE-TEST-PHYSICS-CHECK — the one plumber question for Grant

Per Rule 16 / `pre-test-physics-check`, surfaced BEFORE freezing, not after. The substrate-walk surfaces exactly one physical ambiguity that Grant can collapse in one sentence and that the whole route hinges on:

> **Is the electron's winding the RATIONAL, CLOSED (2,3)=3/2 torus knot, or the IRRATIONAL, NEVER-CLOSING golden orbit φ?** KAM "most-stable" is the *irrational* φ-torus (the last to break, a quasiperiodic orbit that never closes). A closed (2,3) knot is a *rational resonant* torus (the first class to break). The corpus identifies the electron with **both** the golden-torus *geometry* (R/r=φ², an aspect ratio) and the (2,3) *winding* (a rational rotation number). Plumber-physically: is the electron a **closed loop of current that returns on itself** (rational (2,3), a real-space soliton — then it is NOT the KAM-stable object) or a **standing pattern whose two frequencies are incommensurate** (irrational φ, the KAM-stable quasiperiodic orbit — then it is NOT a closed knot and the (2,3) label is only an approximant)? They cannot both be "the most-stable" in the KAM sense — that is the unforced-φ gap. **If the answer is "closed (2,3) knot," conjunct (a) is dead and the route closes (this doc's finding). If "irrational φ standing pattern," then (2,3) is a label for the nearest Fibonacci convergent and a DIFFERENT derivation of R/r=φ² is needed — one not routed through the (2,3) winding at all.** Which is the physical electron?

This question is *for Grant* (framing-level, third-source-of-truth per lane discipline). It is NOT drafted as an axiom or methodology pivot.

---

## §10 Classification + discrimination check

**consistency-vs-emergence:** the route's target α⁻¹ would be Class D emergence IF forced; the first-pass finds NOT forced → α⁻¹ stays **Class B substrate-mechanism manifestation + Class 4 observable consistency** (unchanged from `ch8:148`/§18). The first-pass itself is a **negative** (no class promotion).

**ave-discrimination-check (run in reverse — negative result):** the only quasi-positive observation here is "the KAM-stable knot ladder is the Fibonacci ladder, and (2,3) is the least-stable convergent." This is **NOT** promoted as an AVE-distinct anchor — it is a *diagnostic* showing the proposed discriminator doesn't exist, and it is consistent with the corpus's *own* finding that leptons are NOT a winding tower (they are (2,3)+Cosserat torsion). No foreword / matrix promotion derives from this doc. SM-counterfactual: in SM/QED α is a measured input with no derivation; nothing here changes that — the honest framing is symmetric with SM (the §18 closing state).

**phase-space-coordinate-check:** the (2,3) winding lives in (V_inc,V_ref) phase-space (`ch8:29`); R/r=φ² is the phasor-ellipse aspect ratio; KAM's rotation-number-vs-aspect-ratio distinction (§3.2) IS the coordinate-discipline crux — the route conflates a phase-space frequency ratio (winding) with a phasor-ellipse aspect ratio. Matched throughout; no real-space-vs-phase-space leak.

**substrate-native-check (prose-derivation, trigger 6):** KAM is a *Hamiltonian-perturbation* construct (continuum/SM-adjacent). The AVE substrate is discrete K4-TLM scatter+connect, not an integrable-Hamiltonian-plus-perturbation. So importing KAM whole-cloth is itself an SM-adjacent move requiring grounding: the corpus has **no** KAM derivation (Ground 1), and the "invariant tori" of KAM are not established to be the AVE phasor tori. This is a *further* reason the route is not substrate-native — flagged, not papered over.

---

## §AUDITOR QUEUE

Implementer-lane surfacing per Rule 15 + flag-don't-fix. The auditor lands the KB / manuscript / `COLLABORATION_NOTES` / roadmap entries; I surface findings + provenance. **No KB/manuscript files were edited by this session** — result lives in `research/` + the driver only.

### AQ-1 (top) — epic §20/§21: the LAST open α-route is now examined and CLOSED at the unforced-φ wall

Epic §21:181 states *"The ONLY open α-route remaining is the φ-winding-stability (§20, untested)."* **It is now tested and closed (this doc).** Auditor action: update epic §20/§21 (in `AVE-Core-genesis-wt/_orchestration/2026-06-07_electron-synthesis-epic.md`) to record the φ-winding-stability route as **examined → both conjuncts fail → §18 FIT no longer contingent on this route.** Per substitution-not-retraction (Rule 12): do NOT refill the slot with a new α-route; the only separately-open route (z₀-from-K4 rigidity-percolation, `ch8:11`) is untouched here and keeps its own status.

### AQ-2 — `ch8-alpha-golden-torus.md:11` Class-B caveat can cite a THIRD closed α-¼ route

The clm-0ktpcn Class-B caveat lists the dynamical (4 α-lift) and kinematic (bijection) closed routes. **Append the φ-winding-stability route as analytically closed 2026-06-07 (this doc):** both conjuncts fail α-free — (a) corpus selects (2,3) by minimality, not stability, and (2,3) is the least-stable golden convergent; (b) KAM constrains the winding, not the aspect ratio R/r. The chapter title / Class-B framing is **unchanged**; the caveat's honest framing strengthens.

### AQ-3 — pre-test-physics-check question for Grant (§9) is OPEN and framing-level

Surface §9's plumber question (closed-(2,3)-knot vs irrational-φ-standing-pattern) to Grant. It is the physical fork the route hinges on and is the auditor/Grant adjudication item, not an implementer pivot.

### AQ-4 — DO NOT promote as a positive anchor

Clean negative; adds no AVE-distinct empirical anchor (§10). Ensure no foreword / predictions-matrix promotion derives from this doc. The only corpus-state change is **caveat-strengthening** (a third α-¼ route closed) + the open §9 framing question.

### Provenance table (verify-before-cite — grep-verified at cited line, 2026-06-07)

| Citation | Verified content |
|---|---|
| `_orchestration/2026-06-07_electron-synthesis-epic.md:177` (genesis-wt) | the "(1) winding-stability / KAM argument … (2) DISCRIMINATING secondary prediction — the KAM lepton-tower across (2,5),(2,7)" actionable |
| `_orchestration/2026-06-07_electron-synthesis-epic.md:181` (genesis-wt) | "The ONLY open α-route remaining is the φ-winding-stability (§20, untested …)" |
| `torus-knot-uniqueness.md:93` | "the electron MUST be (2,3) — it's the only assignment consistent with electron = lightest non-trivial stable lepton" |
| `torus-knot-uniqueness.md:102-118` | leptons = (2,3)+Cosserat torsion (FI-13); (2,5)=proton, (2,7)=Δ baryon |
| `lepton-spectrum.md:37` | m_μ = m_e/(α√(3/7)) — α-DEPENDENT |
| `lepton-spectrum.md:59` | m_τ = m_e·p_c/α² = 8π m_e/α — α-DEPENDENT |
| `ch8-alpha-golden-torus.md:75-79` | R·r=¼ ∧ R−r=½ ⟹ R=φ/2 (the corpus arrow runs ¼ ⇒ φ) |
| `ch8-alpha-golden-torus.md:11` | clm-0ktpcn Class-B caveat (closed α-¼ lift-routes) |
| `2026-06-04_alpha-quarter-adversarial-rechallenge.md:54` | "the secondary predictions — KAM lepton-tower … — are untested or automatic" |
| `constants.py` `PHI` | `PHI = (1.0 + np.sqrt(5.0)) / 2.0` (α-free) |

### Files this session produced (worktree-isolated, branch `analysis/2026-06-07-phi-winding-stability`)
- `research/2026-06-07_phi-winding-stability-lepton-tower.md` (this doc)
- `src/scripts/vol_1_foundations/phi_winding_stability_kam_firstpass.py` (α-free first-pass; `make verify` PASSES; α-free construction; no hardcoded α/137 literal)
