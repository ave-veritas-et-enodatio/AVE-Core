# The gravity-sector linearity audit — the license map (2026-08-11)

**Prereg-file**: [lane brief](_orchestration/2026-08-10_gravity-linearity-audit-brief.md)
**Prereg-commit**: `8a9f485f`
*(This is a **verify-not-derive records lane**: it runs no experiment, so it has no prereg of its own.
The frozen object is the **lane brief**, which fixed the goal, the verdict grammar
`LICENSED / UNLICENSED / AMBIGUOUS`, the prior-art consumption list, and the fences **before** any
site was read. The one object frozen by this document is the **site list (§2)**, frozen before
classification per the brief's own fence — see §2.)*

**Lane brief:** [`_orchestration/2026-08-10_gravity-linearity-audit-brief.md`](../_orchestration/2026-08-10_gravity-linearity-audit-brief.md)
**Class:** records / read-only adjudication. **Verify-not-derive.** No repair, no new coupling, no
edit to any KB leaf, register, ruling, axiom file, or manuscript file. **Mints nothing.**
**Base:** `origin/main` @ `a23a044b`.

> **⚑ HEADLINE.** The linearity is **LICENSED at every GR-exact observable, by ONE structure** —
> the linear constitutive projection `n − 1 = ν_vac·(channel strain)` (Op19) applied to the solution
> of a **linear** elliptic equation with a **constant** modulus. The Ax4 kernel appears **nowhere** in
> that chain. The kernel's licensed role is separate and second-order: it grades the *modulus*, and
> canon states the split in its own words at `white-dwarf-gravitational-predictions.md`:44–54
> (*"For Standard General Relativity, S = 1"*). **So the two "laws" are not competitors for one
> observable — they are two roles, and `√S` is a collided symbol.**
>
> **That verdict holds for lensing, Shapiro, perihelion, and the static force chain. It does NOT
> hold for the local clock.** The clock is a genuine **STUCK-POINT** (§7): canon carries **three**
> mutually exclusive clocks, **two Grant rulings** ride on the one the merged #951 lemma
> weak-field-falsifies, and the channel discipline canon used to resolve the adjacent two-radii item
> points *at* that same falsified one. Corpus license cannot settle it. **No winner is picked here.**

---

## §0 — Standard Vacuum Analysis header (SVA v0.2-pilot)

 1. **SECTOR / OWNERSHIP:** three channels carry gravity-sector observables and canon rules them
    distinct (`lattice-extreme-bh-rationality.md`:96–97): **EM/transverse** (strain measure
    `n − 1 = 2GM/c²r`; `Z_EM = Z₀`, `Γ_EM = 0`, matched) / **shear+bulk** (strain measure
    `ε₁₁ = 7GM/c²r`; `Γ = −1` at `r_sat`) / **A1-dilatation** (the mass/source channel). The audit's
    live cross-wiring risk is the **clock**: which channel owns an atom's proper tick. **Not resolved
    here — routed (§7).**
 2. **REGIME / PHASE-STATE:** static, cold, weak-field (`A ≪ 1`) for every GR-exact site audited;
    Regime I throughout (`einstein-field-equation.md`:92–97, all GW sources `A ~ 10⁻²²`).
    Strong-field (`A → 1`) sites are named where they appear but are **not** the audit's target.
    ★ The collision is **regime-hidden**: the kernel clock is operative only in the strong-field
    engine, the lapse only in the weak-field observable chain. They have never been evaluated in the
    same regime — except at one site, and that site's arithmetic fails (§5, F-4).
 3. **CIRCUIT STATEMENT:** the observable in each case is a **total** propagation or tick ratio
    between two reference planes (source at `r`, observer at `∞`) — not a series slot. Every verdict
    below is stated on the total.
 4. **PLANE & PROJECTION:** no signed `Γ` claim is made or adjudicated here. Where a cited site
    makes one (`Γ_EM = 0`, `Γ_shear = −1`), it is quoted, not re-derived.
 5. **CONSTITUTIVE PROVENANCE:** the audit's whole subject. Per-site column in §3.
 6. **ENERGY LEDGER:** no port crossing is claimed; no loss word is used. Reactive throughout.
 7. **CALIBRATABILITY:** targets are dimensionless ratios (`δn`, `z`, `δ_light/(GM/bc²)`).
 8. **DISCRIMINATION CLASS:** DC-internal (corpus-coherence). **No AVE-distinct claim is made or
    tested by this lane.** Canon's own labels (consistency-class / GR-import) are carried forward,
    not re-litigated.
 9. **CERTIFICATION PLAN:** the site list was **frozen (§2) before any site was classified (§3)**.
    Two-method receipts on every number (§6), engines named.
10. **ADJUDICATION ROUTING:** §7 (the one Grant question) and §8 (routed items, none actioned).
11. **NUMERICAL CONDITIONING:** the only conditioning hazard is the `(1+z)` vs `z` prefactor at
    `z ~ 10⁻⁴` (§5, F-4); handled by carrying the exact expression and cross-checking in
    `Decimal(prec=40)`.

---

## §1 — Prior art consumed (the brief's mandatory list, dispositions)

| Prior art | Status at HEAD | Disposition here |
|---|---|---|
| **PPN coherence audit** (PR #91, `research/2026-06-05_gravity-ppn-coherence-result.md`) | merged | **Seeds the frozen list.** Its S1–S4 are sites 1, 4, 6, 5 below. It settled COEFFICIENT coherence *while assuming the linear form* — that assumption is this lane's subject, and it is **vindicated as licensed** (§4). |
| **W1 / W2 walk-backs** (PR #90, `temporal-spatial-lattice-decomposition.md`:26,:28) | applied at HEAD | **Not re-litigated.** Post-relabel statements classified. ★ **W2's ruled content is the slope-2-vs-slope-1 disambiguation only**; its descriptive phrases *"= √S"* and *"the c_shear clock"* are **unruled baggage inside a ruling about something else** (§7). |
| **graded-network quadratic row** (`graded-network-response.md`:147, provenance `b56ee5df` 2026-06-22; ASYM `−¼A²` older, `vacuum-impedance-mirror.md`:122) | live | Site 9. Licenses **only** `δn ∝ +¼A²`, and labels that row *"gravity-class"* — the collision in the **index** register. |
| **ALREADY-FLAGGED linear-vs-quadratic tension** (`research/2026-07-31_anisotropy-observable_scoping.md`:893) | live | **Cited and sharpened, not re-discovered.** Verbatim there: *"photoelasticity is linear in strain while the kernel's index shift is quadratic in amplitude — the two are not the same expansion."* That site also fixes `A ≡ ε₁₁` numerically (§6, R7). |
| **failed kernel-mechanism attempt** (PR #92, two-reactance factor-2 NOT-FORCED) | merged | Consumed as a **prior negative**: the kernel route to the factor was tried and did not force. Not retried here. |
| **`trampoline-framework.md`:113** `k_eff = k₀(1 + βu₀ + O(u₀²))` | live | Site 12. The **operating-offset** structure (Arm-1). Verdict: **licensed as a structure, NOT instantiated for gravity** (§4.3). |
| **#951 `S^p` lemma + TWO-CLOCKS finding** | ⚑ **status changed after the brief froze — PR #951 is now MERGED, titled `[REVIEW: CLEARED]`** | The brief instructed *"consume as PROVISIONAL, tagged."* It is no longer provisional. **Consumed as merged canon-adjacent record**, and the tag is dropped with this note. Its lemma is load-bearing below and is **independently re-derived** at §6 R1–R2. |

---

## §2 — THE FROZEN SITE LIST (frozen before classification; 14 sites)

Enumerated by two independent grep methods (§6, R9) plus the PPN seed list. Ordered by role, not
by verdict. **No site was added after classification began.**

| # | Site | What it states (role) |
|---|---|---|
| 1 | `common_equations/eq_gravity_derived.tex`:50–56 + `temporal-spatial-lattice-decomposition.md`:14–19 | the two-index decomposition (PPN **S1**) |
| 2 | `gordon-optical-metric.md`:20–28 | the **linear** elliptic core, constant modulus `c⁴/7G` |
| 3 | `refractive-index-of-gravity.md`:10–18 | `n = 1 + (2/7)(7GM/c²r)`; Gordon identification |
| 4 | `02_general_relativity_and_gravity.tex`:185–206 + `double-deflection.md`:28 | the deflection derivation (PPN **S2**) |
| 5 | `translation-gravity.md`:23 + `02_general_relativity…tex`:137 | Gordon-form lensing index (PPN **S4**) |
| 6 | `14_macroscopic_orbital_mechanics.tex`:66–77 (+ warningbox :70–72) | perihelion (PPN **S3**) |
| 7 | `operators.md`:59 (**Op19**) | `n(r) = 1 + ν_vac·ε₁₁` — CANONICAL operator |
| 8 | `saturating-modulus-and-backreaction.md`:42, :50–53, :64 | kernel on the **modulus**; weak-field recovery |
| 9 | `graded-network-response.md`:147, :153–155 | SYM co-grade "gravity-class": `n = 1/√S`, `δn ≈ +¼A²` |
| 10 | `saturating-modulus-and-backreaction.md`:128 (+ `:126–130` SUBTRACT ruling) | **kernel clock** `ω_local = ω√S` |
| 11 | `temporal-spatial-lattice-decomposition.md`:24, :28 (W2) | **lapse clock** `√g₀₀ = √S ≈ 1 − GM/c²r` |
| 12 | `trampoline-framework.md`:113 | operating-offset linear response (Arm-1 structure) |
| 13 | `white-dwarf-gravitational-predictions.md`:42–57, :61–70 | the **only** site combining both, with numbers |
| 14 | `eq_axiom_4.tex`:10, :24, :56–59 + `einstein-field-equation.md`:49 | the routed `ε₁₁ = 1` two-radii item |

**Engine sites (operative code, carried as receipts not as separate rows):**
`src/ave/gravity/backreaction.py`:14–17, :237–252 (kernel clock, X44) and :646–678 (linear Op19);
`src/ave/gravity/gw_propagation.py`:84–117 (linear/GR index), :270–294 (kernel shear speed);
`src/ave/core/universal_operators.py`:1100 (`1.0 + nu_vac * epsilon_11`).

---

## §3 — THE LICENSE MAP (per site: where linearity enters, and its license)

Grammar (fixed by the brief, not by this lane) — **LICENSED**(name the structure) / **UNLICENSED** / **AMBIGUOUS**(both readings
possible — both quoted).

### §3.1 — The GR-exact observable chain

| # | Where linearity enters (file:line) | Verdict | The license, named |
|---|---|---|---|
| **2** | `gordon-optical-metric.md`:25 — `-\left(\frac{c^{4}}{7G}\right)\nabla^{2}\epsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)` | **LICENSED** | **Linear Poisson with a CONSTANT modulus.** The modulus `c⁴/7G` carries no `A`-dependence and no kernel. `ε₁₁ = 7GM/c²r` is the Green's-function solution of a linear PDE (`:28`). Linearity here is not a coupling *choice* — it is the equation's own form. **This is the root of the whole chain.** |
| **3** | `refractive-index-of-gravity.md`:10 — *"Substituting the trace-reversed tensor boundary (`ν_vac = 2/7`) and the radial strain field yields"* `n(r) = 1 + (2/7)(7GM/c²r)` | **LICENSED** | **Op19 constitutive projection** (site 7). Arithmetic substitution of `ε₁₁` into a linear relation. |
| **7** | `operators.md`:59 (**Op19**) — `n(r) = 1 + \nu_{vac}\cdot\varepsilon_{11}`, status **CANONICAL** | **LICENSED** | **Poisson-ratio kinematics.** `ν_vac = 2/7` is declared at the site as *"Poisson ratio: 2 compliance / 7 total modes"* — a **kinematic ratio** (transverse strain per longitudinal strain), not a modulus. Kinematic ratios are linear by construction; the kernel grades *moduli*, not kinematics. **This is why Op19 and Ax4 are not in conflict — they answer different questions** (§4.1). |
| **4** | `double-deflection.md`:28 — `n_{\perp} = 1 + \nu_{vac}\,\chi_{vol} = 1 + \tfrac{2}{7}\chi_{vol}` | **LICENSED** | Op19, applied to the **transverse Cosserat** channel. Same structure as #3, different channel. |
| **1** | `eq_gravity_derived.tex`:53 / `temporal-spatial…md`:18 — `n_{temporal} = 1 + \tfrac{2}{7}\varepsilon_{11}` | **LICENSED** | Op19 again. (The `(9/7)` companion at `:19` is a **bookkeeping sum** `n_t + ε₁₁`, per PPN result `:92`; it is linear for the same reason and its deflection attribution was already corrected by W1.) |
| **5** | `translation-gravity.md`:23 — `n(r) = (1+r_s/2r)³/(1−r_s/2r)` | **LICENSED (by IMPORT, declared)** | The **full GR isotropic optical index**, imported whole. Not derived from the kernel; not claimed to be. |
| **6** | `14_macroscopic_orbital_mechanics.tex`:67 — `V_{tidal} = -\frac{GM}{r}(1 + \frac{3GM}{c^2 r})` | **LICENSED (by IMPORT, declared *in situ*)** | The warningbox at `:70–72` states it verbatim: *"The relativistic coefficient 3 … is General Relativity's effective-potential correction … here adopted as a static potential. It is therefore a consistency-class re-statement (AVE = GR at O(GM/c²r), no AVE-distinct observable), not an independent AVE derivation."* **Exemplary honesty — the license is written at the site.** |
| **8** | `saturating-modulus-and-backreaction.md`:64 — *"In the weak field (`r≫r_sat`: `A→0`, `S→1`, `D→1`) the correction **vanishes** and the linear GR core is reproduced identically (**consistency**)"* | **LICENSED** | **The kernel's own weak-field limit.** This site does not *compete* with the linear chain — it explicitly **defers** to it. Ax4's `:13` says the same: `A = 0 ⇒ S = 1` (*"linear regime: … Newtonian gravity recovered"*). |

**The static force chain** (`F/F_Newton = (1−r_s/r)^{−1/2}`, #951 D2) is not a separate license: #951
adjudicated it **MERGED** as `REPRODUCES-WITH-IMPORT(κ = c⁴/7G, ν_vac = 2/7 — both GR-imported)`,
*"DEMONSTRATED, not DERIVED. PEER-with-GR. No chord."* Carried, not re-opened.

### §3.2 — The kernel sites

| # | Site | Verdict | Reading |
|---|---|---|---|
| **8** | `backreaction.md`:50–53 — `-\nabla\cdot[(c^4/7G)D(A)\nabla\varepsilon_{11}] = 4\pi T_{00}`, `D = 1/S` | **LICENSED** | Kernel on the **MODULUS**. Correct role, correct place, self-limiting to `O(A²)`. No conflict. |
| **9** | `graded-network-response.md`:147 — SYM co-grade row labelled **"gravity-class"**, `n = 1/\sqrt{S}`, `\delta n\approx+\tfrac14 A^2` | **UNLICENSED as a gravity index** | The row is licensed as a **graded-network** result; the *"gravity-class"* label is what fails. It gives `δn ∝ A²` where the entire chain above gives `δn = ν_vac·ε₁₁`. Quadratic ≠ linear **at every normalization** (§6 R6). The brief's fence is exact: this leaf *"licenses only `δn ∝ +¼A²`"* — and that is not the gravitational index. **Adjacent live flag already on record**: `2026-07-31_anisotropy…:893`. |
| **10** | `backreaction.md`:128 — `\omega_{\text{local}}=\omega\sqrt{S}` | **AMBIGUOUS → STUCK-POINT** | See §7. Both readings quoted there. **Not resolved.** |
| **11** | `temporal-spatial…md`:24 — `\sqrt{g_{00}} = \sqrt{S} \approx 1 - GM/(c^2 r)` | **AMBIGUOUS (symbol) / LICENSED (value)** | The **value** `1 − GM/c²r` is licensed (GR lapse, ratified by W2). The **symbol** `√S` is not: for the printed value to hold, `S` must be `1 − r_s/r` (#951's finding, re-derived §6 R1), which is **not** Ax4's `S = √(1−A²)`. One symbol, two functions. |
| **13** | `white-dwarf…md`:44 — `\frac{\omega_{\text{local}}}{\omega_\infty} = \frac{1}{n(R)\cdot S(\varepsilon_{11})}` | **LICENSED as the two-factor structure; three internal defects** | ★ **The keystone.** This is canon's own statement that the clock is **lapse × kernel**, with `:54` making the split explicit: *"For Standard General Relativity, `S = 1`."* The structure is the resolution the rest of the corpus lacks. Its execution has three defects (§5). |
| **12** | `trampoline-framework.md`:113 — `k_{\text{eff}}(u_0) = k_0\cdot(1 + \beta u_0 + O(u_0^2))` | **LICENSED as a structure; NOT instantiated for gravity** | See §4.3. |

### §3.3 — Site 14: the routed `ε₁₁ = 1` two-radii item — **RESOLVED by existing canon**

The brief folded this in as *"adjacent, verify and include."* **It is already resolved, and the
resolution is ratified canon that three sites have not propagated.**

`lattice-extreme-bh-rationality.md`:92 (clm-ir8h78), verbatim:

> *"The horizon radius appears in the corpus as **both** 2GM/c² and 7GM/c². These are **two different
> boundaries in two channels**, not a contradiction — resolved by the three-impedance-law channel
> discipline"*

with the ruling table at `:96–97`:

| radius | the quantity that reaches 1 | channel |
|---|---|---|
| `r_s = 2GM/c²` | **`n − 1 = 2GM/(c²r) = 1`** | EM / transverse |
| `r_sat = 7GM/c² = 3.5 r_s` | **`ε₁₁ = 7GM/(c²r) = 1`** | shear + bulk |

**Therefore `ε₁₁ ≠ 1` at `r_s`; `ε₁₁ = 3.5` there** (§6 R3). Three sites still carry the
pre-reconciliation conflation:

| Site | Verbatim | Defect |
|---|---|---|
| `eq_axiom_4.tex`:24 | *"BH event horizon `\varepsilon_{11}(r) = 1` matches Schwarzschild `r_s = 2GM/c^2` **exactly**"* | Names the **shear** variable at the **EM** radius. The quantity that equals 1 at `r_s` is `n−1`, not `ε₁₁`. Listed as one of the axiom's **three validated zero-free-parameter anchors** (`:21`). |
| `eq_axiom_4.tex`:56–59 | *"Gravity: Near a massive defect, `\varepsilon_{11} \to 1` → shear modulus `G_{shear} \to 0` … → event horizon = dielectric rupture"* | The mechanism (`ε₁₁ → 1` ⇒ shear rupture) is **right and is the `r_sat` row**; calling the result *"event horizon"* re-attaches it to `r_s`. Also *"dielectric rupture"* is the channel mislabel `lattice-extreme…:99` already corrects elsewhere: *"the EM channel is matched, `Γ_EM = 0`, under SYM gravity; it does **not** rupture."* |
| `einstein-field-equation.md`:49 | *"The Schwarzschild radius `r_s = 2GM/c^2` marks the point where `n(r) \to \infty` and the local strain reaches the Axiom 4 saturation limit (`S \to 0`)"* | Two true clauses joined by a false *"and"*: `n → ∞` at `r_s` (EM, true) but `S → 0` at `r_sat = 3.5 r_s` (shear, true) — **not the same point.** |

**And the missing factor is exactly the one #951 named:** `r_s/r = ν_vac·ε₁₁ = (2/7)ε₁₁` (§6 R3).
`eq_axiom_4.tex`:10's own dialect list — *"`r_s/r` (gravitational metric strain)"* — is **consistent
with the EM row** and therefore **inconsistent with `:24`/`:56` fourteen lines later, inside the same
file.**

> **Class: PROPAGATION GAP, not open physics.** The physics was settled 2026-06-14 (the dated fix at
> `lattice-extreme…`:99). **Verdict deliverable; no Grant question needed on this item.** Routed §8.

---

## §4 — ONE structure or several? And what the map does to the four-arm fork

### §4.1 — The licenses reduce to ONE structure, plus a declared import

Eight of the nine licensed sites in §3.1 are **the same structure wearing different channel labels**:

> **`observable − 1 = ν_vac × (channel strain)`, with the strain the solution of a LINEAR elliptic
> equation of CONSTANT modulus.**

`n_temporal`, `n_⊥`, `n_spatial`, the Gordon index, the engine's `universal_refractive_index`
(`universal_operators.py`:1100, `return 1.0 + nu_vac * epsilon_11`) — one relation, five prints.
Sites 5 and 6 add a second, **declared** license: **direct GR import**, labelled as such *in situ*.

**So: ONE derived structure (Op19 on a linear Poisson field) + ONE declared import. Not several.**

**Why it does not collide with Axiom 4** — and this is the load-bearing distinction the whole
collision has been hiding behind:

| | grades what | linear or not |
|---|---|---|
| **Ax4 kernel `S(A)`** | the **MODULUS** — how much strain a given stress produces (`eq_axiom_4.tex`:5, *"The substrate's **bulk response** to local strain"*; `backreaction.md`:50, `D(A)` multiplying the elliptic operator) | nonlinear, flat at the origin |
| **Op19 `ν_vac`** | a **KINEMATIC RATIO** — declared at `operators.md`:59 as *"Poisson ratio: 2 compliance / 7 total modes"*: transverse strain per longitudinal strain, a mode-count | linear by construction |

A Poisson ratio is not a modulus. **The strain responds nonlinearly to stress; the index responds
linearly to strain.** Both can be true at once, and canon's own engine implements exactly that:
`gw_propagation.py` puts the kernel in `bulk_stiffness_D` and `shear_wave_speed` and puts **no
kernel at all** in `refractive_index` (`:84–117`) — matching `backreaction.md`:62's
*"EM matched: `Z_EM=Z_0`, `Γ_EM=0` — `refractive_index()` is untouched (guard-tested spectator)."*

> ⚠ **UN-AUDITED INFERENCE, tagged.** The *"Poisson ratio ⇒ kinematic ⇒ legitimately linear"* step is
> **this lane's reading**, not a corpus statement. What canon states is the phrase at `operators.md`:59
> and the operative code split. A reviewer should attack this step first — it is the hinge of §4.2.

### §4.2 — What this does to the four-arm fork

Fork of record: `research/2026-08-06_rotation-substance-ontology_framing-note.md`:247–259 (⚑ the file
marks §11 UN-AUDITED; quoted as the frozen fork statement, not as a verified claim).

| Arm | Framing-note text (abridged, verbatim fragments) | What this map does to it |
|---|---|---|
| **1 — PRE-TENSION** | *"the vacuum idles at a finite scalar operating offset A₀ (linear small-signal coupling for free)"* | **NOT MOOTED, but DEMOTED from necessary to contingent.** The index/observable chain does not need it (§4.1). It is needed **only** if the clock must be kernel-rooted — i.e. only on one branch of §7. **Its charter should be re-scoped accordingly before the pre-tension lane runs.** |
| **2 — KINEMATIC/GEOMETRIC** | *"waves riding DISPLACED geometry couple linearly in u₀ by pure kinematics, kernel-free (the arm the constitutive-thinking habit missed)"* | ★ **SELECTED — and it is not a hypothesis.** Op19 **is** this arm, at **CANONICAL** status, already carrying the entire GR-exact chain. The arm the walk thought was missed is the one canon has been running on all along. |
| **3 — EXTRA-KERNEL LINEAR CHANNEL** | *"last resort; the add-a-field reflex flagged"* | **MOOTED for the observable chain.** No new field is needed: the linear channel exists and is Op19. (Not mooted for the clock, where it remains a last resort.) |
| **4 — CANON-INCONSISTENT** | *"the lemma may have EXPOSED a standing unlicensed linearity, not opened a fork"* | **FIRES — but narrowly, and with the polarity reversed.** The linearity is **licensed**; what is unlicensed is the **quadratic** intrusion into gravity-labelled sites (site 9's *"gravity-class"* row) and the **collided `√S` symbol** at sites 10/11. The exposure is real, and it is **on the kernel side, not the linear side.** |

**Net:** the fork was posed as *"what licenses the linearity?"* The map answers that (Arm 2, already
canonical) and re-poses the live question as: ***what licenses the clock?*** — §7.

### §4.3 — Arm-1's structure at site 12 (verified, not endorsed)

`trampoline-framework.md`:113 does license a linear-in-offset response —
`k_eff(u₀) = k₀(1 + βu₀ + O(u₀²))`, *"the standard pre-stress correction"* — and canon already runs
pre-tension into gravity: `:114`, *"Newton's `G` derives from `T_EM`"*, `G = c⁴/(7ξT_EM)` with
`T_EM ∝ u₀`. **But that is `G`'s magnitude, not the strain-coupling's slope.** The gravity chain's
linear coupling is **not** instantiated at any operating offset anywhere in the corpus.

**Two-method receipt that it is OWED, not held:** (a) grep — no site expands any gravity observable
about `A₀ ≠ 0`; (b) the pre-tension brief's own charter item 2
(`_orchestration/2026-08-10_pretension-brief.md`:12–14) reads *"show the small-signal slope at A₀
supplies the gravity sector's linear-in-ε₁₁ coupling with the RIGHT magnitude"* — **stated as work to
be done.** A held license would leave that charter with nothing to derive.

> **Fence honoured.** Deriving `A₀`, or the slope at `A₀`, is the pre-tension lane's charter. This lane
> states only that the structure exists at site 12 and is **not instantiated** for gravity. **No `A₀`
> value is proposed here, and no arithmetic toward one was performed.**

---

## §5 — Site 13, the keystone: right structure, three defects in execution

`white-dwarf-gravitational-predictions.md` is the **only** place in the corpus that puts the lapse and
the kernel in one expression, applies it in the **weak field**, and compares to **data**. It is
therefore the single most load-bearing site for the collision — and all three of its defects push the
kernel's apparent contribution around by orders of magnitude. All numbers §6, three engines.

**F-1 — `:44` uses the slope-2 index as a local clock, against W2.** The site writes
`ω_local/ω_∞ = 1/(n(R)·S)` with `n(R) = 1 + 2GM/(c²R)`. W2 (2026-06-05, Grant-adjudicated) ruled that
form to be the **bulk/coordinate-time propagation index**, and the local clock to be the slope-1
`√g₀₀`. `:51`'s resultbox then quietly uses the **slope-1** form, `1/\sqrt{1-2GM/(c^2R)}`.
**`:44` and `:51` differ by a factor 2 in the redshift** (§6 R5). This is a **post-W2 un-propagated
site** — W1/W2 landed in `vol3/gravity/ch01`; ch20 was not swept.

**F-2 — `:56`'s correction formula drops a factor `(1+z)/z ≈ 3857`.** The site states
`δz = z_GR·(1/S − 1)`. Exactly, `δz = (1+z_GR)·(1/S − 1)`. Since `z_GR ≈ 2.59×10⁻⁴`, the stated form
understates the kernel's own contribution by **3857×** (§6 R4b).

**F-3 — the Sirius B table `:67,:70` matches neither its own text nor its own formula.** Three numbers
for one quantity:

| source | `δv` (km/s) | |
|---|---|---|
| `:56` formula as written | **0.000128** | wrong by F-2 |
| correct, at the leaf's own `A = ε₁₁` (`:27`) | **0.493785** | 3 engines agree |
| the table at `:67`/`:70` | **0.05** | matches neither |

**F-4 — and the table's number is closest to the *other* normalization.** Under
`A = r_s/r` — `eq_axiom_4.tex`:10's declared gravitational dialect — the correction is **0.0403 km/s**,
within ~24% of the tabled 0.05, versus **9.9×** off the leaf's own `ε₁₁` normalization. *(Stated as a
proximity observation. The lane did **not** establish the table's provenance and does **not** assert
the table was computed that way.)*

> **Why F-4 matters beyond arithmetic.** The `ε₁₁`-vs-`r_s/r` ambiguity is the **same** `ν_vac = 2/7`
> gap as site 14 (§3.3) — and here it is not a labelling slip in an axiom file, it is **a factor 12 in
> a number compared against a measurement.** The two-radii item and the white-dwarf number are one
> defect at two altitudes.

**What survives F-1…F-4.** The **structure** at `:44` + `:54` — clock = lapse × kernel, with
*"For Standard General Relativity, `S = 1`"* — is untouched by all four and is the resolution shape
§3 relies on. **The numbers do not survive.** Under the leaf's own normalization the kernel term is
0.494 km/s against an observed (obs−GR) residual of +2.90 km/s (`:68`) — **17% of the residual, not
the ~2% the table implies.** ⚠ **That is a live, unclaimed empirical exposure**: whether it helps or
hurts depends on the §7 answer, and this lane takes no position on it.

---

## §6 — Receipts

**Driver:** [`research/drivers/gravity_linearity_audit_number_check.py`](drivers/gravity_linearity_audit_number_check.py) —
**30 checks, all GREEN.** Engines: **A** = python `math` floats, **B** = sympy 1.14.0 exact/series,
**C** = `decimal.Decimal` at 40 digits (headline delta only, third engine).

| Receipt | Result | Consumes |
|---|---|---|
| **R1** | `√S(A) = 1 − A²/4`; `√(1−A) = 1 − A/2 − A²/8`; slopes at the origin `0` and `−1/2` | §3.2, §7 |
| **R2** | `d/dA f(S(A))|₀ = 0` for **symbolic** `f` — independent re-derivation of the merged #951 lemma at its widened `C¹` scope | §1, §7 |
| **R3** | `r_s/r = (2/7)ε₁₁`; `r_sat/r_s = 3.5`; **`ε₁₁ = 3.5` at `r_s`** | §3.3 |
| **R4** | Sirius B: `ε₁₁ = 1.815×10⁻³` ✓`:32`; `v_GR = 77.75` ✓`:66`; `δv` = **0.493785** (`A=ε₁₁`) / **0.040309** (`A=r_s/r`) / **0.000128** (`:56` as written); dropped factor **3856.8**; kernel term = **17.0%** of the `:68` residual. **Engine C agrees to 6 d.p.** | §5 |
| **R5** | `:44` → `z = 2p` (slope 2); `:51` → `z = p` (slope 1) | §5 F-1 |
| **R6** | `1/√S = 1 + A²/4`; leading power of `ε₁₁` is **2** under **both** normalizations | §3.2 site 9 |
| **R7** | solar limb `7GM/c²R_☉ = 1.4861×10⁻⁵` ✓`:893`'s `1.486e-5`; `A² = 2.209×10⁻¹⁰` ✓ its `2.21e-10` — **that site's `A` is `ε₁₁`** | §1 |
| **R8** | the three clocks' leading terms: **`ε₁₁²/4`** (kernel) / **`ε₁₁/7`** (lapse) / **`2ε₁₁/7`** (index); kernel/lapse at Sirius B = **0.3%** | §7 |
| **R9** | `d ln W/dA|_{A₀} = A₀/(2(A₀²−1)) → −A₀/2` — nonzero for `A₀ ≠ 0`. **Structure only; no `A₀` value proposed** | §4.3 |

**Constant provenance.** `c`, `G`, `M_SUN` are **imported** from `src/ave/core/constants.py`, never
hard-coded — the repo's EFT gate caught a first cut that inlined them, exactly as it did for #951.
`R_☉` has no canonical entry and is declared **ENG-CHOICE at its use site** (IAU nominal, R7 only).
Sirius B's `M/M_☉ = 1.018` and `R = 5800 km` are the **leaf's own** inputs (`:32`), quoted not chosen.
*(The canonical `M_SUN = 1.989×10³⁰` shifts the §5 deltas in the 5th significant figure versus a
CODATA-style literal; the doc carries the canonical-source values.)*

**R9-completeness (the frozen site list).** Two independent grep patterns, per the
grep-false-negative discipline: (1) literal `1 + 2GM`-class / `\tfrac{2}{7}` forms across
`manuscript/`; (2) the `nu_vac`-projection pattern across `manuscript/` **and** `src/ave/`. Method 2
surfaced three sites method 1 missed (`double-deflection.md`:28, `transverse-refractive-index.md`,
`universal_operators.py`:1100) — **all three are the same Op19 structure**, changing no verdict.
Seeded additionally by the PPN audit's S1–S4. ⚠ **Completeness is curation, not a gate**: the list
is frozen and enumerated, but no machine check asserts it is exhaustive.

**Quote receipts.** Every verbatim span in §3–§5 was read from the worktree at `a23a044b`, not from
a summary. The `√S` collision and the `eq_axiom_4` `ν_vac` gap were **independently found here**
before #951's body was read, then reconciled against it — they agree.

---

## §7 — ⚑ STUCK-POINT — the clock. Corpus license cannot settle it.

**Everything above resolved. This did not.** Per the brief: *"If the two-laws collision cannot be
settled by corpus license alone, that is a STUCK-POINT for Grant — not a coin flip, not a
'recommended reading.'"* **No reading is recommended below.**

### (1) The blocker, exact

Canon holds **three mutually exclusive local clocks**, and their leading terms differ in **power**,
not coefficient (R8):

| clock | site | leading deficit |
|---|---|---|
| **kernel** `ω_local = ω√S` | `saturating-modulus-and-backreaction.md`:128 · `op14-local-clock-modulation.md`:20 (`τ = τ₀/(1−A²)^{1/4}`) · `backreaction.py`:17,:252 | **`ε₁₁²/4`** |
| **lapse** `√g₀₀` | `temporal-spatial-lattice-decomposition.md`:24 · W2 `:28` | **`ε₁₁/7`** |
| **index** `ω/n` | Op19 route · `op14-local-clock-modulation.md`:11 (*"`τ_local = n(r)·τ_unstrained`"*) | **`2ε₁₁/7`** |

**W2 ruled between the second and third only.** The kernel clock was **not on that ballot** — it has
no linear term to compare (R1c, R2). Nothing in canon has ever ruled kernel-vs-lapse.

**And the kernel clock is not a dead branch — it is load-bearing at three live sites:**

- **Grant ruling 2026-06-29 (SUBTRACT)**, whose stated substrate-native reason is `:126–130`:
  *"the local clock `ω_local = ω√S` down-regulates; since `E = ħω` and `m = E/c²`, matter in the well
  weighs less (the mass defect)."*
- **Grant ruling 2026-07-12 (X44, Komar/redshift weight)**, live in operative code —
  `backreaction.py`:14–17: *"`T₀₀^src = T₀₀^matter · √S(A)`  # local clock `ω√S`"*.
- **The Stage-4 peel target**, `backreaction.md`:174–176: *"AVE's `√S` can peel from GR's
  `√(1−r_s/r)`"* — the exposed consumer #951 already named.

The merged #951 lemma says the kernel clock has **no first-order effect at all** — *"not a wrong
coefficient, an absent power."* R8f puts it at **0.3%** of the lapse clock at Sirius B. So the
mechanism two Grant rulings stand on cannot produce the effect they invoke it to explain, at leading
order. **The rulings' verdicts may well survive on other grounds — SUBTRACT is confirmed by every
bound orbit — but their stated mechanism does not.** That is a physics question, not a bookkeeping one.

### (2) What I tried — two attempts, both failed

**Attempt 1 — adopt canon's own two-factor structure** (`white-dwarf…md`:44,:54: clock = lapse ×
kernel, *"For Standard General Relativity, `S = 1`"*). **FAILED: the product is asserted at exactly one
site and contradicted at two.** `op14-local-clock-modulation.md`:74 derives the clock from the
wave-crossing time — *"a wave needs `τ = ℓ/c_eff` to cross a cell"* — which yields the **kernel alone,
no lapse factor**; `backreaction.py`'s Komar source likewise weights by `√S` alone. **No site derives
the product**, and the one site that prints it fails its own arithmetic three ways (§5).

**Attempt 2 — apply the channel-split discipline that resolved the adjacent two-radii item**
(clm-ir8h78, §3.3). **FAILED — it points the wrong way.** That discipline assigns each observable the
strain measure of *its own channel*. An atom is matter: **shear + bulk**, whose measure is `ε₁₁` and
whose grading is the kernel ⇒ **quadratic redshift**, empirically dead. The **EM** channel, whose
response is linear, is the *messenger*, not the emitter — and canon insists it is a matched spectator
(`Γ_EM = 0`, `refractive_index()` *"untouched"*). So canon's own most successful reconciliation
tool, applied here, **selects the branch observation rules out.**

**Two attempts, cap reached. Stopping.**

### (3) The ONE physical question

> **An atom sitting on a white dwarf's surface is an LC tank in a vacuum that has been squeezed.
> Its tick slows. Which knob actually moved?**
>
> **(a) The tank's own `L` and `C` changed** — the medium around it saturated, so its component
> values shifted. That is the kernel, and a saturation curve is *flat at small drive*: squeeze it a
> little and almost nothing happens (`ε₁₁²`).
>
> **(b) The tank didn't change at all — its DC rail did.** It is sitting further down a graded
> supply, and a tank biased off its rest point de-tunes *linearly* with the offset (`ε₁₁`).
>
> **Is the gravitational clock a MODULUS effect or a BIAS-POINT effect?**

Everything else in this map follows from the answer, and nothing in the corpus answers it.

### (4) Candidate readings — one line each, none endorsed

- **R-A — LAPSE.** The kernel is modulus-only; `:128` and the X44 weight are sector mis-assignments. *Cost:* two rulings lose their stated mechanism, the Stage-4 peel target loses content, and the linear coupling stays **GR-imported with the substrate derivation OWED**.
- **R-B — KERNEL.** Then the observed linear redshift is unexplained at leading order, and only a nonzero `A₀` restores it (R9). *Cost:* the pre-tension lane goes from contingent to **make-or-break**, and its charter item 2 becomes the gate on the whole gravity sector.
- **R-C — BOTH, as `white-dwarf…md`:44 prints.** Two physically distinct effects that multiply. *Cost:* the product needs a derivation nobody has written, and `op14…`:74 must be re-scoped — it currently claims the whole clock.
- **R-D — the question is malformed.** *"The clock"* is not one object; a matter clock and an EM clock are different observables. *Cost:* W2's bulk-vs-local carve needs a **third row**, and every *"the local clock"* site in the corpus needs a channel subscript.

**This lane picks none of them and edits nothing.**

---

## §8 — Routed, not actioned (no propagation performed by this lane)

| # | Item | Class | Route |
|---|---|---|---|
| **1** | `eq_axiom_4.tex`:24, `:56–59`, `einstein-field-equation.md`:49 — `ε₁₁ = 1` at `r_s` | **propagation gap** (physics settled 2026-06-14 at `lattice-extreme…`:99) | auditor lane. ⚠ `:24` is one of Axiom 4's **three validated zero-free-parameter anchors** — the anchor count is downstream of the fix. |
| **2** | `white-dwarf…md` F-1…F-4 (§5) | **arithmetic + un-propagated W2** | auditor lane; `clm-at7x0y` solidity is downstream. Blocked on nothing. |
| **3** | `graded-network-response.md`:147 *"gravity-class"* label | **mislabel** — the row's physics is fine, its gravity attribution is not | auditor lane; adjacent to the live `:893` flag. |
| **4** | `operators.md`:56 — *"`c·√(1−A²)` ≡ Schwarzschild `c·√(1−r_s/r)`"* | **a fourth face of the collision** | ⚑ **do not action separately.** The cell is **already VACATED** (FLAG-CEFF-CITE, 2026-08-07, ROUTED-NOT-RULED). §8 there flags the *exponent* disagreement; it does **not** flag that no power of `S` can equal `√(1−r_s/r)` at first order. **This lane adds that second, orthogonal defect to the existing flag.** |
| **5** | Arm-1 charter re-scope (§4.2) | **brief amendment** | `_orchestration/2026-08-10_pretension-brief.md` — its necessity is contingent on §7. Worth reading before that lane runs. |
| **6** | The §7 clock question | **Grant** | This report. |
| **7** | `verify-frozen-provenance.py`:210–214 — a `Prereg-file:` path beginning with `_` **silently fails to resolve** when backtick- or emphasis-wrapped | **gate defect** (hit live by this lane) | tooling. The optional emphasis group `(?:[*_\`]{1,3})?` is greedy over `{*, _, \`}`, so `` `_orchestration/…` `` is captured as `orchestration/…`, which resolves nowhere — and the doc is then reported as *"carries Frozen label(s) but no prereg resolves"*, i.e. **the wrong diagnosis**. Every brief under `_orchestration/` is affected. Worked around here with the link form; **not fixed** (out of lane scope). |

**Explicitly NOT done by this lane:** no leaf/axiom/register/ruling/manuscript edit; no solidity
moved; no claim-id minted; no `A₀` derived or estimated; no winner picked on §7; no re-litigation of
W1/W2, PR #90/#91/#92, #951, or FLAG-CEFF-CITE; no position taken on whether the 17%-of-residual
exposure (§5) helps or hurts.
