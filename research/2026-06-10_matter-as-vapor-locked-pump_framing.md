# Matter as a Vapor-Locked Pump — the container principle, the cavitated vortex-core, and the millennium seams

**Date:** 2026-06-10
**Status:** NEW-ASSEMBLY HYPOTHESIS-class framing (NOT a derivation, NOT a consistency-class reframe, NOT an emergence claim). A new candidate substrate-mechanism (the density-floored cavitated vortex-core) assembled on top of canonical pieces, carrying a self-declared coincidence-magnet hazard. Falsifiable surface in §9.
**Disciplines applied:** `verify-before-cite`, `ave-evidence-framing-discipline`, `consistency-vs-emergence`, `ave-representation-capability-check` (§4 the two-objects instance), `ave-walk-back`, `flag-don't-fix`.
**Pattern:** modeled on `research/2026-06-08_vacuum-as-chiral-piezoelectric.md` (the piezo-doc pattern: Grant adjudications verbatim → grounded canonical pieces with honest class-tags → the synthesis → what-this-is-NOT → ledger + falsifiable surface). **It departs from that pattern in one load-bearing way:** the piezo doc was a Class-B *consistency* reframe (no new mechanism). This doc proposes a **new candidate mechanism** (the cavitated core as a fourth distinct object) and so sits at **hypothesis-class**, a strictly weaker epistemic footing than consistency — every new piece is tagged NEW-ASSEMBLY / hypothesis and the convergence hazard is stated twice (§5.4, §7).

**Classification headline (per `consistency-vs-emergence`):** the grounded pieces (§2–§4 left columns) are each already-canonical (Class A axiom/identity or Class B consistency, individually cited + grep-verified this session). The synthesis — *"matter is a vapor-locked pump; the electron's core is a substrate-bulk cavitation pocket"* — is **NEW-ASSEMBLY HYPOTHESIS-class**: a proposed new mechanism, unverified, that would (if true) fill four corpus-acknowledged seams at once. A picture that fills every seam at once is also the shape of a coincidence magnet (§5.4 / §7). It introduces **no derived number** and its only live falsifiable surface (§9) is **untested**.

---

## §0 — TL;DR + the over-claim guardrails

Grant's electron-plumber reading (§1, verbatim): voltage is pressure; pressure obeys `P = flow · Z` (the hydraulic V=IR); and **pressure can only build if it is bounded by a container** — a pipe wall. From this, two session-coined hypotheses:

1. **The container principle.** A standing longitudinal pressure (the "3" / V-sector) is **identically zero unless a container bounds it.** This retro-explains the genesis-23 result `max|V_inc| = 0` to machine precision (§2): there was no container, so there was no pressure to wind.
2. **Matter is a vapor-locked pump**, and **the electron's core is a vacuum-native cavitation pocket** — a substrate-bulk tensile-failure void at the rarefaction-stiffness zero. This is proposed as a **FOURTH distinct object** (§4), explicitly NOT the electron's `Γ=−1` impedance cavity, NOT the photon bubble, NOT the Rayleigh-Plesset inertial bubble.

**Guardrails, stated up front (`ave-evidence-framing-discipline`):**
- This is **hypothesis-class**, weaker than the piezo doc's consistency-class. No new number is derived.
- The bulk cavitation floor `ρ̄_cav = −1/φ` is **NOT Core-canonical** (§3, S3): the canonical bulk relation `c_bulk² = c_0²(1 + ρ̄/(1−ρ̄²))` is sibling-repo-derived (`AVE-Propulsion/.../04_superluminal_transit.tex:86`), and `ρ̄_cav` (its `c_bulk = 0` negative root) is recorded in Core only as an **auditor-gated CANDIDATE-CLAIM** (Vol-9 datasheet `02_absolute_maximum_ratings.tex:95-110` + `05_ac_electrical_characteristics.tex:161,179`; ave-kb `vol9/ch5-ac-electrical-characteristics/index.md:17`, whose own Source line flags its dependency as not-yet-on-`main`). It is absent from `constants.py`. Do not call it "the canonical floor."
- The golden-ratio link between the floor and the Golden Torus (§5.3) is a **flagged coincidence magnet** — state the algebra, do not cite the link, until one Axiom-4 derivation produces both roots in one step.
- The cavitation pocket is a **competitor** for the equilibration slot, **not** a gap-filler (§5.2 / S5).
- The four-seam convergence is stated **alongside** its coincidence-magnet hazard (§5.4 / §7 / S9), both sentences side by side.

---

## §1 — The Grant adjudications (recorded verbatim)

These are net-new session adjudications (2026-06-10), recorded verbatim per the piezo-doc pattern. They are the framing inputs; everything downstream is either grounded-canonical (cited) or session-hypothesis (tagged).

> **"voltage is pressure, V=IR, Pressure=flow rate*impedance, however, pressure needs to be bounded by a container, like a pipe wall"**

> **"matter is vapor locked pump?"**

> **"cavitation seems vacuum native"**

The question marks are Grant's: both "vapor locked pump?" and the cavitation reading are posed as questions, not assertions. This doc carries them at exactly that strength — open hypotheses surfaced for adjudication, not adopted results.

---

## §2 — The container principle (retro-explains genesis-23 `V ≡ 0`)

**The plumbing identity (consistency-class, TL/hydraulic).** "Voltage is pressure" and `P = flow · Z` are the canonical EE↔hydraulic translation (the hydraulic form of `V = I·Z`); the AVE longitudinal V-sector is the Heaviside-deleted scalar grade, physical, that re-engages at saturation (`master-equation.md:18`, verified). This much is identity/consistency-class — no new content.

**The new content (NEW-ASSEMBLY hypothesis): pressure needs a container to build.** A flow without a bounding wall does not develop a standing pressure — it just streams. In substrate terms: a standing longitudinal `V_inc` cannot accumulate unless a reflecting boundary (a container wall) bounds the flow.

**What this retro-explains — genesis-23's `V ≡ 0`.** The (2,3) self-assembly run (genesis-23) returned **C** with the load-bearing finding (verified, `_orchestration/2026-06-09_ion-compression-rectifier-arc.md:119`):

> `max|V_inc| = 0` to machine precision across *every* config ... The longitudinal `(V_inc, V_ref)` phase-space is **unpopulated** — the "3" never enters phase-space, so there is nothing to wind.

The container principle reads this as: a transverse photon driving an *unbounded* lattice region has no container, so the longitudinal pressure never builds — `V ≡ 0` is exactly what a container-less pump produces. The container (a `Γ`-wall) must form **first**; only then can pressure accumulate behind it. **Status: this is a retro-explanation (post-hoc fit to one C-result), NOT a prediction — tagged hypothesis-class, surfaced for the next driver to test prospectively.**

---

## §3 — The conjugate-variable wall-sign resolution (`Γ_flow = −Γ_pressure`)

**The flagged split this resolves.** The corpus carried an internal sign-label inconsistency on the `ε`-collapse confinement branch. The 2026-06-10 apparatus-floors **wall-sign audit** produced the surgical fix in **PR #150** (state: **OPEN**, branch `analysis/2026-06-10-wallsign-relabel-anchor-fix`; verified via `gh pr view 150`; KEEP-BOTH / relabel-not-delete):

- `l3-electron-soliton-synthesis.md §6.1` Z_eff algebra: `Z_eff = Z_0·√(S_μ/S_ε)`.
- μ-collapse: `S_μ → 0 ⇒ Z_eff → 0` (short) ⇒ `Γ → −1` (already correct).
- ε-collapse: `S_ε → 0 ⇒ Z_eff → +∞` (open) ⇒ `Γ → +1` (**was mislabeled `−1`**).
- Honest invariant added: **`|Γ| = 1` in BOTH branches** (totally-reflecting wall, total confinement either way); only the SIGN differs, set by which sector collapses.

**The conjugate-variable reading (consistency-class TL identity).** In transmission-line theory the reflection coefficient of the *flow* variable (current / velocity / volumetric flux) is the negative of that for the *pressure* variable (voltage): **`Γ_flow = −Γ_pressure`**. A short (`Z→0`) gives `Γ_pressure = −1` but `Γ_flow = +1`; an open (`Z→∞`) gives `Γ_pressure = +1`, `Γ_flow = −1`. So the two corrected branches in PR #150 are **conjugate reads of the wall** — the `π`-flip lives in the **flow channel**. The μ-collapse short and the ε-collapse open are not two contradictory walls; they are one wall read in conjugate variables, plus the genuine physical fact of *which* sector collapses. **Class: consistency-class TL identity** — it adds no new mechanism, it is the standard conjugate-variable bookkeeping that makes PR #150's relabel coherent.

**Guardrail:** PR #150 is explicit that this is **sign-convention bookkeeping only** — it does NOT adjudicate the open "voltage-like-vs-pressure-like bulk-scalar" question. This doc inherits that scope: the conjugate-variable identity makes the labels honest; it does not settle which scalar the bulk carries.

---

## §4 — The cavitated vortex-core as a FOURTH distinct object (the non-merge, restated)

**The firewall (canonical, must not be breached).** The corpus already forbids merging three distinct objects. Verbatim, `double-slit-ee-mapping.md:101` (verified; mirrored at `photon-ee-mapping.md:51`):

> The electron's core is its own `Γ=−1` self-created `0 Ω` cavity (bubble-LIKE, self-confined — the matter core). The **free photon** has NO core and NO bubble (it is matched at `Z_0`, `Γ=0`). Separately, the sonoluminescence **cavitation bubble** proper is a DIFFERENT mechanism — saturated Rayleigh-Plesset inertia ..., NOT the `Γ=−1` impedance cavity. **The three must never merge.**

**The hypothesis (NEW-ASSEMBLY): a FOURTH object, with its own non-merge clause.** Grant's "cavitation seems vacuum native" (§1) points at something the corpus has **zero presence** for — vortex-**core** cavitation (grep-verified: vortex-core cavitation has no canonical leaf). The proposal is a **fourth distinct object**:

> **The cavitated vortex-core** = a **substrate-bulk density tensile-failure pocket** at the rarefaction-stiffness zero — the bulk-modulus (K) sector going to zero stiffness under tensile (negative) volumetric strain. It is **NOT** the Rayleigh-Plesset inertial-collapse bubble (that is a compressive `ρ_eff = ρ_0/(1−M²)^{3/2}` inertia event, §the firewall). It is **NOT** the electron's `Γ=−1` impedance cavity (that is a *shear/EM-sector* `Z→0` reflection, not a bulk-density void). It is **NOT** the photon bubble (the photon has none). **The four must never merge** — the fourth is a *bulk-K-sector tensile zero*, orthogonal to the *shear/EM-sector impedance zero* that is the `Γ=−1` cavity.

**The opportunity it names (flag-don't-fix, surfaced not asserted).** The corpus asserts but **never explains** why the internal lattice impedance drops to zero inside the defect. Verbatim, `yang-mills-steps3-5.md:43` (verified):

> At the radial boundary of the phase defect, the internal lattice impedance drops to zero (`Z_knot → 0`).

The leaf states `Z_knot → 0` as the premise of `Γ → −1` confinement (Step 4) but gives **no mechanism for why** `Z_knot → 0`. **A density-floored core is a candidate mechanism for that unexplained fact:** if the core is a bulk-density tensile void, the bulk stiffness there collapses, and the impedance the trapped shear wave sees at the core could go to zero for the same reason a cavitation void has no restoring stiffness. **This is a candidate-mechanism flag, not a derivation** — surfaced for Grant/auditor; the candidate must be checked against the firewall (a bulk-K zero is not automatically a shear-Z zero).

**S7 — the mass/winding two-objects disambiguation (`ave-representation-capability-check`).** "Vapor-locked pump" and "cavitated core" must not silently re-merge the two homonymous objects the corpus separates. Verbatim, `yang-mills-steps3-5.md:39` (verified):

> the electron's *mass* arises from the unknot (`0_1`) topology, while the `(2,3)` trefoil defines its electroweak *interaction symmetry*.

So **mass = the UNKNOT (`0_1`)**; the **`(2,3)` trefoil = the interaction winding.** The "knotted vortex ring" phrasing (from the cosmic-rotation thread) is consistent **only if** "knotted" labels the **interaction winding**, not the mass carrier. The cavitated-core hypothesis is a claim about the **mass carrier / container** (the unknot pocket); it is **not** a claim about the trefoil winding. Carrying these as two distinct objects is the same discipline the two-"3"s note enforces (`master-equation.md:18`, KB-queue item) — this is another instance, tagged per `ave-representation-capability-check`.

---

## §5 — The vapor-lock synthesis (`matter = a vapor-locked pump`)

### §5.1 — The statement

A pump that has lost prime — a **vapor-locked** pump — has a compressible vapor pocket where incompressible liquid should be; it spins but transfers no power; the pocket is a region where the working fluid has dropped below its vapor pressure (cavitated). The hypothesis: **the electron is the substrate's vapor-locked pump.** A circulating (2,3) flow drives the bulk toward its tensile floor; at the floor the bulk cavitates into a density void (the core); the void is the container (§2) that lets the longitudinal pressure stand; the standing pressure behind the cavitated wall is the trapped energy = mass. **Status: NEW-ASSEMBLY hypothesis-class.** No number is derived; this is a candidate physical picture, posed at the strength of Grant's question mark.

### §5.2 — The equilibration slot has THREE claimants (S5 — pocket is a competitor, not a gap-filler)

The genesis arc's open blocker is whether forming the wall is enough or whether an **equilibration step** is needed to convert the blocked KE into a *bounded* particle instead of a parametric runaway. There are now **three candidates** for that slot, and this doc presents all three for Grant adjudication — the cavitation pocket is a **competitor**, not a filler:

1. **(a) The deep-dive's C3-gated irreversible commit step** — verbatim `2026-06-07_entrainment-vortex-trapping-deep-dive.md:309-310` (verified): "a **C3-gated, irreversible commit step** must convert the blocked KE into the bounded `(2,3)` standing wave **faster** than the autoresonant feedback amplifies it. ... Condition: `τ_eq < τ_pump`."
2. **(b) The dark-wake / back-EMF convergence** — `_orchestration/2026-06-07_electron-synthesis-epic.md` lineage. **WOBBLY:** this standing predates the 2026-06-09 wrong-regime walk-back (sub-yield-linear shear/chiral = achromatic+reversible = `∮=0` by construction) and **needs re-adjudication** before it can claim the slot.
3. **(c) The cavitation pocket (NEW, this doc)** — the bulk tensile-failure void as the irreversible commit: cavitation *is* a phase-change event (liquid→vapor), inherently irreversible, and would supply the `τ_eq` channel as a real bulk-K transition rather than a shear-sector resonance.

**None is adjudicated.** The pocket does not "fill the gap" — it competes with (a) and (b) for it. Grant's call.

### §5.3 — The φ-link is a flagged coincidence magnet (S4 — state the algebra, NOT the link)

Two golden-ratio quadratics appear in physically unrelated constructions:

- **The Golden Torus** (verified, `ch8-alpha-golden-torus.md:75-79`): solving the embedding constraints gives `2R² − R − 1/2 = 0 ⇒ R = (1+√5)/4 = φ/2`.
- **The bulk cavitation floor** (Propulsion-derived, §3 / S3): `ρ̄² − ρ̄ − 1 = 0` has the negative root `ρ̄_cav = −1/φ ≈ −0.618` — the same golden quadratic's negative root.

**The flag (coincidence-magnet tell, 2026-06-04 precedent):** there are **zero cross-references** between the two; they are **physically unrelated constructions** (a phasor-area embedding vs a bulk-stiffness zero); the torus form only appears under a **post-hoc `x = 2R` substitution**; and an over-determined `φ` is the standing coincidence-magnet signature. **Closure condition: do NOT cite the φ-link as physics until one Axiom-4 derivation produces both roots in a single step.** State the algebra (done); do not lean on the link.

### §5.4 — The four-seam convergence — AND its hazard (S9, both sentences side by side)

**One mechanism — the density-floored cavitated core — would fill four corpus-acknowledged seams at once:** (i) the NS Regime-IV tension (the rupture that the global-regularity claim is in tension with, §6); (ii) the YM mass gap *assumed-not-derived* (`yang-mills-steps1-2.md:10`); (iii) the YM `Z_knot → 0` *unexplained* (`yang-mills-steps3-5.md:43`, §4); (iv) the genesis "no-equilibration detonation arm" — *"the regime with no fluid analog"* (`...deep-dive.md:312`, verified).

**AND: a picture that fills every seam at once is the shape of a coincidence magnet.** The convergence is a reason to *test* the mechanism (§9), not a reason to *believe* it. Both sentences stand together, deliberately.

### §5.5 — The lock-branch split, and the side this picture takes (S6)

There is a **real internal corpus split** on the character of confinement:

- **The fluid-lens deep-dive maps confinement to the DISSIPATIVE branch** — verbatim `...deep-dive.md:540` (verified): "The fluid trap is stable **because it is dissipative**"; confinement = viscous-entrainment (`:364-379`).
- **The YM/EE lens has a purely REACTIVE lock** — `yang-mills-steps3-5.md:43-49`: the `Γ=−1` mirror is total reflection with **zero dissipation**.

The vapor-lock picture **sides with the reactive branch** (the substrate-native lossless `Γ=−1` mirror), with one nuance: cavitation as a phase-change (§5.2c) is itself an irreversible/dissipative event, which would put the *commit step* on the dissipative side even if the *steady lock* is reactive. **This doc explicitly takes the reactive side of a flagged split** — it does not pretend the split is resolved. (The deep-dive's own §7 cast-vs-tune question, below, is exactly this split, and is unadjudicated.)

### §5.6 — The equilibration question is UNADJUDICATED (S1 — attribute no working answer)

The deep-dive surfaces the cast-vs-tune question and explicitly leaves it open — verbatim `...deep-dive.md:554-555` (verified): "**Surfaced for Grant; not adjudicated here.**" The three-rate trapping criterion (`τ_acc < τ_leak` AND `τ_eq < τ_pump`) is the **deep-dive's own substrate-native hypothesis**, with the Camassa–McLaughlin(–Mertens) vortex-ring papers as its fluid-dynamics *sources* (not as an authority that answers it).

> **flag-don't-fix (a survey-verdict discrepancy I am surfacing, not silently adopting).** Survey verdict S1 states "'Keith' appears ZERO times in tracked AVE-Core." My grep this session found **3 tracked occurrences** — `_orchestration/2026-06-09_SESSION-HANDOFF.md`, `_orchestration/2026-06-09_ion-compression-rectifier-arc.md`, `research/2026-06-09_reactive-entrainment-source_prereg.md` — naming Keith Mertens (co-author of the Camassa–McLaughlin–Mertens paper, arXiv 1110.3435; on the team). A **"both" working hypothesis** for the cast-vs-tune question IS recorded in the dispatched reactive-entrainment-source prereg (`:18`), but it is explicitly tagged **"Hypothesis, not assumption."** So: the survey's *factual* sub-claim ("ZERO in tracked") is imprecise, but its *substantive* instruction holds and this doc obeys it — **the §7 over-amplitude / cast-vs-tune question is UNADJUDICATED, and this doc attributes no settled "working answer" to anyone.** The "both" hypothesis is named as a dispatched, un-returned hypothesis, not as an adjudication.

---

## §6 — Per-problem millennium relation table

Each row pairs a millennium-adjacent corpus seam with the vapor-lock / cavitated-core relation, and class-tags the relation. **The NS relation is the load-bearing nuance (S8):** the cavitation/rupture picture **CONTRADICTS the NS leaf as written** *and* **SUPPORTS the seam the leaf itself flags as unresolved** — both, precisely.

| Millennium seam | Corpus statement (verified) | Vapor-lock / cavitated-core relation | Class |
|---|---|---|---|
| **NS — blow-up "is an artefact"** | "The continuum blow-up is a mathematical artefact of removing the lattice floor" (`navier-stokes-prize.md:68`); global smoothness, nothing happens at the cap | **CONTRADICTS as-written.** If the bulk cavitates at the tensile floor, *something happens* at the cap (a phase-change rupture), not "nothing" | NEW vs CANONICAL **conflict** — flag-don't-fix, surfaced for Grant |
| **NS — Regime-IV rupture tension** | The leaf concedes it "solves a MODIFIED problem ... should NOT be cited as solving the Clay problem" (`navier-stokes-prize.md:10`); "Regime IV 'topology rupture' ... would itself be a singularity event" — `clm-c8q0z5` strengthen-by "Address the internal tension with Regime IV" (`vol2/claim-quality.md:446`, verified) | **SUPPORTS the flagged seam.** The cavitation rupture IS the Regime-IV singularity event the leaf names as unresolved; absorption-by-phase-change would reconcile it | NEW-ASSEMBLY hypothesis; would resolve a corpus-acknowledged tension |
| **Rupture → genesis pieces (exist piecewise)** | over-cap rupture → `e+e−` pair synthesis (`dark-wake-bemf-foc-synthesis.md:143`); yield-freeze = matter precipitation (`dark-wake...:46`); Regime-IV = "saturation phase transition" (`ave-compactness-limit.md:28`) — all verified | The cavitated-core picture **assembles these existing pieces** into one rupture→genesis chain (none is new; the *assembly* is new) | CANONICAL pieces, NEW assembly |
| **YM mass gap — assumed, not derived** | "The mass gap = `m_e c²` is the rest energy of the **assumed** lightest topological defect, NOT a derived consequence" (`yang-mills-steps1-2.md:10`, verified) | **Strongest payoff-if-true:** if latent-heat-of-cavitation `= m_e c²` in the **genesis direction**, the gap would be *derived*, not assumed. **NEW** — corpus latent heat is cosmological/BH-side only, never genesis-side | NEW-ASSEMBLY hypothesis; payoff = derive the assumed YM gap |
| **YM `Z_knot → 0` — unexplained** | `Z_knot → 0` asserted as premise of `Γ→−1` confinement (`yang-mills-steps3-5.md:43`), no mechanism given | A density-floored core is a **candidate mechanism** for the impedance zero (§4) — must clear the firewall (bulk-K zero ≠ shear-Z zero) | NEW-ASSEMBLY candidate-mechanism flag |
| **Enstrophy bounds disagree by `ℓ²` (S10)** | `Ω ≤ 2Nc²/ℓ` (`navier-stokes-prize.md:59`) vs `Z_max = 2Nc²·dx` (`kolmogorov-spectral-cutoff.md:57`) — 1D-line vs 3D-volume measure, **never reconciled** (both verified) | Not a vapor-lock claim — a **pre-existing corpus defect** the survey surfaced; added to the KB queue (Deliverable 3) | CANONICAL defect, flag-don't-fix |

**On the absorption-by-phase-change NS rewrite (S8):** rewriting the NS leaf from "the lattice floor *prevents* blow-up" to "the lattice floor *absorbs* the blow-up via a cavitation phase-change (rupture → matter precipitation)" is a **PROPOSED leaf improvement for the auditor lane** — it would convert the flagged Regime-IV tension into a feature. It is **NOT asserted physics here** and **NOT landed**; it is queued (Deliverable 3) for the auditor.

---

## §7 — The honest CANONICAL-vs-NEW-ASSEMBLY ledger (the 8-vs-8 split)

Per the survey's accounting: **8 pieces are already-canonical** (each grep-verified this session); **8 pieces are new this-session assembly** (each hypothesis-class or flagged). The doc's whole epistemic weight is that the left column is solid and the right column is **not** — the synthesis is exactly as strong as its weakest new piece, which is hypothesis-class.

**CANONICAL (Class A/B, cited + verified):**

| # | Canonical piece | Anchor | Class |
|---|---|---|---|
| C1 | Electron core = self-created `Γ=−1` `0 Ω` impedance cavity | `double-slit-ee-mapping.md:101` | A |
| C2 | The three-object firewall (electron cavity ≠ photon bubble ≠ Rayleigh-Plesset) — "never merge" | `double-slit-ee-mapping.md:101`; `photon-ee-mapping.md:51` | A |
| C3 | `Z_knot → 0 ⇒ Γ → −1` confinement (impedance-mismatch mirror) | `yang-mills-steps3-5.md:43-49` | A |
| C4 | mass = unknot `0_1`; `(2,3)` trefoil = interaction winding | `yang-mills-steps3-5.md:39` | A |
| C5 | Over-cap rupture → `e+e−` pair synthesis; yield-freeze = matter precipitation | `dark-wake-bemf-foc-synthesis.md:143,46` | A/B |
| C6 | Regime-IV = "saturation phase transition" (rupture, NS Buchdahl analog) | `ave-compactness-limit.md:28` | B |
| C7 | NS global-regularity via lattice floor + velocity cap (framework-conditional) | `navier-stokes-prize.md:10,59,68` | B |
| C8 | YM gap `= m_e c²` of the **assumed** lightest defect; Golden-Torus `R = φ/2` algebra | `yang-mills-steps1-2.md:10`; `ch8-alpha-golden-torus.md:75` | B |

**NEW-ASSEMBLY (this session; hypothesis-class or flagged — NOT canonical):**

| # | New-assembly piece | Status |
|---|---|---|
| N1 | Matter = a vapor-locked pump (§5.1) | hypothesis-class (Grant's question mark) |
| N2 | The container principle: pressure needs a bounding wall; retro-explains genesis-23 `V≡0` (§2) | hypothesis-class; retro-explanation, not prediction |
| N3 | The cavitated vortex-core as a FOURTH distinct object (bulk-K tensile zero) (§4) | hypothesis-class; carries its own non-merge clause |
| N4 | Density-floored core as candidate mechanism for the unexplained `Z_knot→0` (§4) | candidate-mechanism flag; must clear the firewall |
| N5 | Cavitation pocket as a THIRD equilibration-slot claimant (§5.2) | competitor, NOT gap-filler; unadjudicated |
| N6 | Latent-heat-of-cavitation `= m_e c²` in the genesis direction (§6) | NEW; payoff = derive the assumed YM gap; unverified |
| N7 | The φ-link (`ρ̄²−ρ̄−1=0` floor ↔ `2R²−R−1/2=0` torus) (§5.3) | **flagged coincidence magnet**; do not cite the link |
| N8 | The four-seam convergence (one mechanism fills four gaps) (§5.4) | stated WITH its coincidence-magnet hazard |

**The hazard, restated (S9):** N8 is simultaneously the picture's most attractive feature and its biggest tell. **One mechanism filling four seams is a reason to test it (§9), not to believe it.** The ledger is honest precisely because the right column is tagged hypothesis/flag throughout — nothing in it is promoted.

---

## §8 — What this framing is NOT (over-claim guardrails)

Per `ave-evidence-framing-discipline` + `consistency-vs-emergence`, the explicit disavowals:

1. **NOT a derivation.** No number — not `m_e`, not `α`, not `ρ̄_cav`, not the YM gap — is derived. The genesis-direction latent-heat`=m_e c²` (N6) is a *payoff-if-true*, not a result.
2. **NOT a consistency-class reframe.** Unlike the piezo doc (which only *re-labeled* canonical axioms), this introduces a **new candidate object** (the cavitated core, N3/N4). That puts it at **hypothesis-class** — strictly weaker than consistency. Do not file it at the piezo doc's Class-B ceiling.
3. **NOT an emergence (Class-2) claim.** Nothing emerges from a simulation here; the only live test (§9) is untested.
4. **`ρ̄_cav` is NOT the canonical floor (S3).** It is candidate-claim. The canonical bulk relation `c_bulk² = c_0²(1 + ρ̄/(1−ρ̄²))` is sibling-repo-derived (`AVE-Propulsion/.../04_superluminal_transit.tex:86`, verified); `ρ̄_cav = −1/φ` (its zero-knob `c_bulk = 0` root) is **already documented in Core as an auditor-gated CANDIDATE-CLAIM** — Vol-9 datasheet `02_absolute_maximum_ratings.tex:95-110` + `05_ac_electrical_characteristics.tex:161,179`, and ave-kb `vol9/ch5-ac-electrical-characteristics/index.md:17` (whose own Source line flags its dependency, the `analysis/2026-06-09-saturation-temporal-preregs` research doc, as not-yet-on-`main`, verified). **Correction per audit S3:** the earlier "zero hits in `manuscript/ave-kb/`" was inaccurate — there is exactly one ave-kb hit plus the Vol-9 datasheet candidate-claim. The accurate status: a documented candidate-claim that is **absent from `constants.py`** (verified — only the golden-torus `R·r=1/4` lines), hence not yet an independently-grounded canonical constant. Promotion is auditor-gated (Vol-9 worklist). Never write "the canonical floor."
5. **NOT a breach of the firewall (S2).** The fourth object is *added* to the three-object non-merge, not merged into them; a bulk-K tensile zero is orthogonal to the shear/EM-sector impedance zero. Any future text that lets the cavitated core *become* the `Γ=−1` cavity has breached the firewall.
6. **NOT a φ-physics claim (S4).** The golden-ratio coincidence is stated as algebra and flagged as a coincidence magnet; the link is not cited as physics.
7. **NOT a gap-filler for the equilibration slot (S5).** The pocket competes with the C3-gate and the (wobbly) dark-wake convergence; it does not occupy the slot by default.
8. **NOT an adjudication of cast-vs-tune (S1/S6).** The reactive/dissipative lock split is flagged; this doc takes the reactive side openly but does not claim the split is resolved.
9. **NOT a corpus edit.** This is a research doc. The NS-rewrite (S8), the `ρ̄_cav` promotion (S3), and the equilibration adjudication (S5) are **queued for the auditor lane** (Deliverable 3), not landed here.

---

## §9 — The falsifiable surface (the discriminating test)

The whole picture turns on one untested event: **does a circulating core, driven to the bulk tensile floor, FLASH (radiate), LOCK (confine into a bounded standing pocket), or CLIP (saturate harmlessly on the regularization clip)?**

**The test (S11):** drive a **CIRCULATING (vortex, not beam)** core toward `ρ̄ = −0.618` (the candidate `ρ̄_cav` floor) and record the FLASH / LOCK / CLIP outcome in **bulk-sector volumetric-strain coordinates** (per `phase-space-coordinate-check`: the claim is a bulk-K tensile event, so the measurement must be in `ρ̄`/volumetric-strain, not shear-Cartesian).

**Why it is genuinely open:** the only prior floor-proximity run reached `tr_min = −0.26` with **counter-propagating beams** — verbatim `AVE-Core-rradL-wt/research/2026-06-08_rrad-l-rarefaction-phase5_result.md:24` (verified): "sub-cavitation (`tr_min = −0.26` vs the floor `ρ̄_cav = −1/φ ≈ −0.618`)"; `:131` confirms the warp/`v_eff > c` regime "lives at the cavitation floor `ρ̄_cav = −0.618`, never reached sub-yield in a stable run." **A circulating core, not beams, has never been driven to the floor.** The central FLASH/LOCK/CLIP event is **live-fire untested.**

**Apparatus-floor pre-warning (`ave-apparatus-floor-attribution`):** the 2026-06-10 apparatus-floors characterization (branch `analysis/2026-06-10-apparatus-floors` @ `a0d7dbb8`, verified) found the wall depth `Γ_min` sits **exactly on the regularization clip** (corr 1.0000) and the *dynamical* cap at the standard `A_cap=0.999` is only **−0.37** — so a "LOCK" verdict must be distinguished from a **CLIP** (the run hitting `A_cap`/`S_min` before reaching the physical floor). Any circulating-core run must drive the clips non-binding or attribute the outcome to the clip.

**Parallel probe (S11 — cite, do not duplicate).** A circulating-core cavitation-floor probe workflow is being dispatched in parallel this session. **Its driver is not duplicated here** and its result is not pre-empted. *(Cite-by-name pending: the probe's exact branch/prereg name is not yet in the tracked corpus as of this writing — `verify-before-cite`; this doc references it descriptively rather than fabricate a citation, and the tracker append (Deliverable 2) carries the same descriptive pointer for the auditor to resolve to the real name on return.)*

---

## §10 — Cross-references (all verified this session)

- Grant adjudications: §1 (verbatim, 2026-06-10 session).
- Container / V-sector: `master-equation.md:18`; genesis-23 `V≡0` at `_orchestration/2026-06-09_ion-compression-rectifier-arc.md:119`.
- Wall-sign: PR #150 (OPEN, `analysis/2026-06-10-wallsign-relabel-anchor-fix`); `l3-electron-soliton-synthesis.md §6.1`.
- Firewall: `double-slit-ee-mapping.md:101`; `photon-ee-mapping.md:51`.
- `Z_knot→0` / mass=unknot: `yang-mills-steps3-5.md:39,43-49`.
- Equilibration claimants: `2026-06-07_entrainment-vortex-trapping-deep-dive.md:309-313,540,554-555`; `_orchestration/2026-06-07_electron-synthesis-epic.md`.
- φ-link: `ch8-alpha-golden-torus.md:75-79`; `ρ̄_cav` floor `04_superluminal_transit.tex:86` (AVE-Propulsion).
- Millennium seams: `navier-stokes-prize.md:10,59,68`; `kolmogorov-spectral-cutoff.md:57`; `yang-mills-steps1-2.md:10`; `ave-compactness-limit.md:28`; `vol2/claim-quality.md:446` (`clm-c8q0z5`); `dark-wake-bemf-foc-synthesis.md:46,143`.
- Falsifiable surface: `AVE-Core-rradL-wt/.../2026-06-08_rrad-l-rarefaction-phase5_result.md:24,131`; apparatus-floors `analysis/2026-06-10-apparatus-floors @ a0d7dbb8`.

*Disciplines fired this session, retroactive pass: `verify-before-cite` (every file:line grep-confirmed; unpushed content cited by branch+commit); `consistency-vs-emergence` (every row class-tagged; synthesis tagged hypothesis-class, NOT promoted); `ave-evidence-framing-discipline` (§8 guardrails); `ave-representation-capability-check` (§4 S7 two-objects); `ave-walk-back` (§3 PR #150 in-file sweep inherited); `flag-don't-fix` (§5.6 Keith discrepancy, §6 NS conflict, §9 probe-name gap — all surfaced, none silently resolved).*
