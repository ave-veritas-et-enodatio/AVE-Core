# Q-POINT CONSTITUTIVE MAP — PRE-REGISTRATION (FROZEN)

**Date:** 2026-08-28 · **Branch:** `research/2026-08-28-qpoint-constitutive` · **Base:** `origin/main` @ `a3f4fef7`
**Lane:** orchestrator-authored derivation. Grant signed the lattice picture in-session 2026-08-28 (vertices unmoved; ε₁₁ = DC Q-point; observed matter/waves are AC). This document freezes that picture and the first derivation target. **Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; edits no KB leaf, register, ledger, or ruling; changes no solidity.**
**This document commits ALONE and pushes FIRST (freeze-by-push), before any derivation content, driver code, or lane-produced number exists on this branch.**

**Unmerged prior (cited, not stacked).** Open PRs #1028 (PPN-tensor, `50cb25c7`) and #1029 (two-knob repair, `849f6a97`) diagnosed Gordon γ = 0 and posed `(c_eff, Ω)` as two knobs; L3 reported the constitutive map does not exist. This lane continues that question from **main**, with a signed ontology. It does **not** restack those branches (their headlines overclaim relative to their own caveats; #1032 is BLOCKED). It does **not** plant `(a_1,b_1,b_2) = (2,1,½)`.

---

## 🔒 FREEZE STATEMENT

This document is the frozen prereg. Rule 11 binds from the push: no bin, tolerance, edge, or label below may be edited, widened, or re-labelled after derivation content lands. A post-push change is a Rule-12 dated amendment.

---

## §0 — Standard Vacuum Analysis header (SVA v0.2-pilot; all 11 rows)

 1. **SECTOR / OWNERSHIP:** Source of the held grade = **A1 dilatation** (mass accounting). Observables are **AC readouts** of that DC grade: (i) hop delay / `c_eff` of the gapless T2/EM channel, (ii) local tank clock `Ω` of a gapped packet. **Not** Cosserat (2,3) winding, not charge, not spin. A1 ⊥ T2 fence active: the A1 sector appears only as the **bias**, never as a propagating EM mode. Geometric bound response `u_0` (clause G) is **in the sector but unused** (R48, `𝒜_g` UNVALUED).
 2. **REGIME / PHASE-STATE:** Crystalline, **cold**, sub-yield, lossless-reactive. Weak-field gravity: `ε₁₁ ∼ 10⁻⁸–10⁻⁵`. Op14 saturation kernel **inactive** at linear order (even in `A`; see §4). No `Γ = −1` wall. MODE: analytic constitutive inventory; no engine run in this freeze.
 3. **CIRCUIT STATEMENT (before any framework word):** A lossless LC ladder with a shunt stiffness, graph frozen (no vertex translation in an embedding). Hold a DC bias on the A1 tanks. Small-signal: series `L` and shunt `C` of the hop, plus a gap stiffness `S`. Read `c_eff² = 1/(LC)` and `Ω² = S/C`. Gravity-class loading is **impedance-matched** (`Z = √(L/C)` pinned). Question: which of `{L, C, S}` can be functions of `ε₁₁` without moving vertices and without breaking the match.
 4. **PLANE & PROJECTION:** No signed `Γ` is a verdict observable. Achromatic `Γ_EM = 0` is an **Ax3 constraint** on the map, not a result. Irrep projections (`1/7` isotropic vs `2/7` transverse) are named as **readout channels** of one bias, not as two fields.
 5. **CONSTITUTIVE PROVENANCE:** `ε₁₁ = 7GM/c²r` — **IMPORTED** (Poisson / `gordon-optical-metric.md`:33). `ν_vac = 2/7` — **GR-IMPORTED** via `K = 2G` (#261). Op19 `n = 1 + ν_vac·ε₁₁` — **CANONICAL formula, coefficient imported**. Ax4 `S(A) = √(1−A²)` — **SHAPE-DERIVED**, even, quadratic-leading. `Z = Z_0` under SYM — **Ax3 + INVARIANT-S2**, entailed. `𝒜_g` — **UNVALUED-RATIFIED** (R48). `(a_1,b_1,b_2) = (2,1,½)` — **not an input and not a target**.
 6. **ENERGY LEDGER:** Lossless-reactive. Bias energy of the A1 rail is **out of scope** (bound-constitutive item (iii) is a different lane). This lane grades **small-signal parameters**, not the mass ledger.
 7. **CALIBRATABILITY:** Verdicts are structural (which objects can be independent functions of `ε₁₁`). Dimensionless ratios only. No new dimensional constant. Solar-limb / Mercury amplitudes in §4 are **scale-setting**, not targets to fit.
 8. **DISCRIMINATION CLASS:** **DC→AC coupling** (DC Q-point read by AC hop-delay and AC clock). Recovering GR PPN from imported `ν_vac` and Newton would be **Class C** (consistency), not emergence — and is **not** a success criterion of this freeze. SM/GR counterfactual: a metric with `g_{ij} = δ_{ij}` **must** give `γ = 0`; that diagnosis is already derived (#1028) and is **not** re-litigated. AVE-distinct content, if any, is whether the substrate **forces a second constitutive function** (the gap `S(ε₁₁)`) that a Gordon scalar cannot express.
 9. **CERTIFICATION PLAN:** Gates in §7. UNRUN ≠ PASSED. Phase-1 is analytic (sympy identities + tagged provenance). No `src/ave` run corroborates anything. Negative control: the Gordon identity (`a_1 = b_1`, `b_2 = a_1²`) must reappear whenever the map is one scalar index. Positive control: the WKB split `c_eff² = 1/(LC)`, `Ω² = S/C` is algebraically two functions when `S` is independent of `LC` — that identity is **already derived** on unmerged #1029; this lane does not re-derive it; it asks whether the **substrate assigns** `S(ε₁₁)` independently.
10. **ADJUDICATION ROUTING:** Forks F1–F3 (below) route to **Grant**. The lane reports a four-tuple, no aggregation, no solidity move. PR opens `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.
11. **NUMERICAL CONDITIONING:** Phase-1: sympy exact + float cross-check of the §4 amplitudes only. Dynamic range: `ε₁₁ ∼ 10⁻⁸` vs `1`; no cancellation at this order. No iterated map. No RNG.

---

## §1 — Signed ontology (Grant, 2026-08-28) — LOCKED

These are session-signed, not derived here. A derivation that violates them is aborted, not “repaired.”

1. **The lattice is the space.** There is no embedding `ℝ³` the bricks fly through. A node is a graph vertex with six Cosserat DOFs plus operating point `A`.
2. **Observed matter and light are AC** on that net (traveling / standing waves). All measurement is AC (`clm-acdc07`).
3. **`ε₁₁` is the DC Q-point** of the A1 tank at that vertex — allowed AC swing / varactor bias — **not** “we grabbed this node and slid it.”
4. **Uniform `A` is gauge-relative.** Only spatial gradients of `A` / `ε₁₁` are readable (`CLAUDE.md` INVARIANT-S2 operating-point clause, `:75`).
5. **Vertices stay put** for this lane. Bound response `u_0 = −𝒜_g ∇ε₁₁` is a second layer, **unvalued** (R48). Geometric `θ = ∇·u` is **not consumed**.
6. **Relative frame down-regulates** via the local LC cell (`Ω`, `c_eff`, `Z`) without vertices leaving the graph.

**Naming correction, frozen as a fork not a silent rewrite.** Session language “micropolar rotation → inductance, bonds → capacitance” is **half-right**:

- Microrotation → inductive **flywheel** (`dual-reactance-storage-taxonomy.md`:71–73; `translation-circuit.md`:100).
- Translation / bond-stretch → capacitive (`translation-circuit.md`:99, `:103`).
- The **bond** is a distributed TL (`L'` and `C'`), not a capacitor alone (`translation-circuit.md`:98).

**SYM constraint (entailed, not a branch).** Gravity-class loading is symmetric: `μ` and `ε` co-scale, `Z = Z_0`, `Γ_EM = 0` (`achromatic-impedance-matching.md`:20–28; `alpha-invariance-symmetric-gravity.md`:15–21). Independent grading of **TL series `L` vs TL shunt `C`** would change `Z` and is the **ASYM** channel (static-E, Meissner-asymmetric, `CLAUDE.md`:75). That is **not** gravity. So “split micropolar `L` vs bond `C` on the EM hop” is **not fireable** under the signed + canonical loading class.

**What remains fireable (this lane’s actual target):** under a frozen graph and `L/C` pinned, the two medium-native knobs are the **product** `LC` (sets `c_eff`) and the **gap** `Ω² = S/C`, where `S` is the Cosserat / shunt stiffness that no impedance theorem constrains. Session “micropolar inductance” maps onto **`S`**, not onto the TL series `L`. Independent `L` vs `C` of the EM hop is closed. Independent **`S` vs `LC`** is the open question (#1029 L1 vs L3).

---

## §2 — Derivation target (one sentence)

**Derive — or honestly report NOT-DERIVABLE — the constitutive map `ε₁₁ ↦ (L, C, S)` of a loaded K4/srs cell with vertices unmoved, `Z` pinned, and no GR `(β, γ)` imported as the answer; then read off which of `{c_eff(ε₁₁), Ω(ε₁₁)}` are independent AC channels.**

---

## §3 — Corpus state

**Corpus-grep (2026-08-28, `ave-corpus-grep` across staging + archive):** **no closed `ε₁₁ → (L, C)` map on any searched HEAD.** Closest prior is unmerged #1028/#1029.

| Finding | Home | Class | Relation to signed picture |
|---|---|---|---|
| Gordon `g_{ij} = δ_{ij}` ⇒ metric-read `γ = 0` | `gordon-optical-metric.md`:17; #1028 | (a) closed diagnosis | SUPPORTS “do not take Gordon as the answer” |
| One scalar index fuses speed and clock | #1029 §0; ponderomotive `:14`+`:19` | (a) closed diagnosis | SUPPORTS two-slot language |
| `c_eff² = 1/(LC)`, `Ω² = S/C`; `Z` pins `L/C` only | #1029 Step 1 | (b) partial | SUPPORTS / REFINES: knobs are `(LC, S)`, not TL `L` vs `C` |
| `(2,1,½)` not forced; `a_1` GR-imported, `b_1` Newton, `b_2` asserted | #1029 open-item `two-knob-constitutive-forcing` | (c) | **CONTRADICTS** treating that triple as a derivation target |
| Rank-4 `p_{ijkl}` never named | `2026-07-31_anisotropy-observable_scoping.md`:657 (F-B4) | (c) missing object | SUPPORTS “the linear map is missing” |
| Ax4 kernel even ⇒ `O(A²)` at limb `∼ 10⁻¹⁰` vs Op19 linear `O(ε₁₁)` | #1029 §9.4.1; `nonlinear-vacuum-capacitance.md`:33–34 | (c) | **CONTRADICTS** “linear response of `(L,C)` from the kernel” |
| `1/7` is `θ/3` | `one-seventh-impedance-projection.md`:13 | (c) | TENSION with “`θ` unused” — Fork F3 |
| Op14 clock `ω_local = ω √S` | `op14-local-clock-modulation.md`:19 | (c) | SUPPORTS clock-as-`S(A)`; keyed on saturation `A`, not linear `ε₁₁` |
| Two speeds `c_EM = c_0/S`, `c_shear = c_0 √S` | `CLAUDE.md`:79–80 | (c) | SUPPORTS two speeds; **not** automatically two PPN knobs |
| `C_eff = C_0/S` A1 compliance | `nonlinear-vacuum-capacitance.md`:27 | (c) | SUPPORTS C(Q-point); electrical `V/V_snap`, not `ε₁₁`; Taylor **quadratic** |
| `𝒜_g` UNVALUED | `eq_axiom_5.tex`:96 | (c) | SUPPORTS leaving `u_0` unused |

**Not on main:** the two-knob result doc, the PPN-tensor result doc, the `two-knob-constitutive-forcing` open-item. This prereg may cite them by PR/commit. It does not copy their repair arithmetic.

---

## §4 — Dimensional analysis (Step 3.5)

Primitives from `src/ave/core/constants.py`:

| Symbol | Value | Cite |
|---|---|---|
| `G` | `6.67430e-11` m³ kg⁻¹ s⁻² | `:188` |
| `C_0` | `299792458.0` m s⁻¹ | `:110` |
| `M_SUN` | `1.989e30` kg | `:132` |
| `R_SUN` | `6.957e8` m | **ENG-CHOICE** IAU 2015 (`gravity_sign_freq_modulation.py`:46); **not** in `constants.py` |
| Mercury `a` | `5.79e10` m | **ENG-CHOICE** astronomical datum |

`GM_⊙/c² = 1.477063×10³ m`.

`ε₁₁(r) = 7GM/c²r` (`gordon-optical-metric.md`:33):

| Locus | `r` | `ε₁₁` | `U = GM/c²r` |
|---|---|---|---|
| solar limb | `R_SUN` | `1.486193×10⁻⁵` | `2.123132×10⁻⁶` |
| Mercury semi-major | `5.79e10` m | `1.785741×10⁻⁷` | `2.551059×10⁻⁸` |

**Kernel vs linear coupling (power-counting, frozen):**

- Ax4: `S(A) = √(1−A²) = 1 − A²/2 − ⋯`. If `A ∼ ε₁₁` (no yield denominator), leading correction at the limb is `ε₁₁²/2 = 1.104×10⁻¹⁰`.
- Op19: `n − 1 = ν_vac ε₁₁ = (2/7)ε₁₁ = 4.246×10⁻⁶` at the limb (same order as `2U = 4.246×10⁻⁶`).
- Solar-limb deflection is `O(10⁻⁵)` rad. Kernel-only is **∼ 10⁴ too small**. The `O(m)` gravitational sector **cannot** be the even kernel. It requires a **linear-in-`ε₁₁` coupling that is not Ax4**. The only named such object is Op19, whose `ν_vac` is a **strain-per-strain** ratio used as strain-per-index (`operators.md`:59). That conversion in a real medium is `p_{ijkl}`, which F-B4 records as **unnamed**.

PONDER-05 (`V_DC/V_y = 0.687`, `A_0` appreciable) is a **material** analog of the kernel **shape**, not a solar-gravity operating point (per-node vacuum `A_0` at 30 kV is `10⁻⁷–10⁻¹⁰`, `CLAUDE.md`:75). Sanity: solar `ε₁₁` sits in the **linear-index / quadratic-kernel** split, not in the varactor-knee band.

---

## §5 — Forks (record both; Grant-routed)

Default shape: freeze **both** branches; do not pick by fiat.

**F1 — Is `Ω` a free function of `ε₁₁`, or a second projection of the same tensor as `c_eff`?**
- **F1-free:** `Ω² = S/C` with Cosserat `S` independent of the EM `LC` product (two-knob L1). Analytic expectation: a Z-matched medium can still have `a_1 ≠ b_1`.
- **F1-projection:** bound mode is a cavity of the **same** graded tensor (two-knob L3/reconciliation). Analytic expectation: `a_1` and `b_1` are locked up to irrep projection (`1/7` vs `2/7`); Gordon-family `γ = 0` for a scalar readout **survives**.

**F2 — What is the linear `ε₁₁ →` index map?**
- **F2-Op19:** use the canonical formula and **tag `ν_vac` IMPORTED**. Analytic expectation: numbers can be written; they are Class C; nothing is forced.
- **F2-photoelastic:** the map is a rank-4 `p_{ijkl}` that this corpus has never named. Analytic expectation: Phase-1 reports **NOT-DERIVABLE(missing `p_{ijkl}`)** unless a substrate identity produces the tensor.

**F3 — What is the `1/7`?**
- **F3-θ:** canon’s leaf is `θ/3` with `θ = 3/7 ε₁₁` (`one-seventh-impedance-projection.md`:13). Consuming it **uses geometric dilatation**, against locked item 5 unless re-derived as a **bias projection that does not need `u`**.
- **F3-clock:** two-knob §4.2 re-reading: `1/7` was always the **clock** grading. Analytic expectation: `b_1` from `1/7`, `a_1` from a different irrep; still not `(2,1,½)` without further imports.

**Entailed (not a fork):** under gravity-class SYM, TL `L/C` is invariant. A “maybe gravity grades `L` and `C` independently” branch is **not fireable** without an explicit Ax3 exception, which this lane does not take.

---

## §6 — Discriminating outcomes (Phase-1 analytic)

**Primary rung (robustness ladder):** **existence** — does the substrate assign a second constitutive function `S(ε₁₁)` independent of `LC(ε₁₁)`? Magnitudes / PPN exponents are supplementary and **cannot** promote a consistency fit to a derivation.

Sector: DC→AC. A null here is **not** a framework-level axiom kill; it is “the O(m) map is still missing.”

| Outcome | What | Class | Interpretation |
|---|---|---|---|
| **A (likely)** | Inventory closes: SYM pins `L/C`; kernel cannot source `O(m)`; Op19 is the only linear object and does not force `(a_1,b_1)`; F1 stays open | NOT-DERIVABLE(missing linear constitutive) + honest fork table | The signed picture stands; the map is not in the axioms; #1029’s caveat is confirmed from main |
| **B** | A substrate identity (Ax1 connectivity + Ax3 + Cosserat gap) **forces** `S(ε₁₁)` independent of `LC` with a **derived** leading exponent, no GR import | DERIVED (exponents tagged) | Still Class C if the exponent equals a GR-imported `ν_vac` chain; say so |
| **C (null)** | The only consistent Z-matched frozen-graph map is one scalar → Gordon family, `γ = 0` for matter geodesics | NOT-DERIVABLE(one-knob) | Matches #1028 matter sector; optics remains Snell / `n_⊥`, not Gordon `g_{ij}` |
| **Abort** | Any step slides vertices, consumes unvalued `𝒜_g` as a length, or plants `(2,1,½)` as “derived” | STOP | Ontology or honesty violation |

**Falsifier of the signed picture (not of GR):** a derivation that **requires** embedding-space node motion to get a spatial PPN slot, after F1-projection and irrep projection have been exhausted. That would reopen locked item 5 and route to Grant — it is not licence to slide nodes in this lane.

**SM counterfactual:** GR already has `γ = 1`, `β = 1` as metric structure. Recovering those numbers from imported `ν_vac · 7` and Newton is **peer-with-GR**, not AVE-distinct. The AVE-distinct claim, if it ever exists, is a **forced second function** `S(ε₁₁)` that Gordon cannot write. Phase-1 does not claim that.

---

## §7 — Gates (frozen; UNRUN ≠ PASSED)

| Gate | Content | Pass |
|---|---|---|
| G-ONT | Every derivation step names whether it grades `L`, `C`, or `S`, and never treats `ε₁₁` as a vertex displacement | structural |
| G-SYM | No step grades TL `L` and TL `C` independently | structural |
| G-EVEN | Any kernel-sourced index shift is shown `O(ε₁₁²)` (or `O(A²)`) and is **not** used as an `O(m)` PPN input | algebraic |
| G-IMPORT | Every `2/7`, `7`, `κ = c⁴/7G`, `a_1 = 2` is tagged IMPORTED | provenance |
| G-GORDON | If the map is one scalar, the Gordon identity `a_1 = b_1`, `b_2 = a_1²` is reproduced (negative control) | algebraic |
| G-NO-PLANT | Result text does not call `(2,1,½)` derived | honesty |
| G-AG | `𝒜_g` is not assigned a length | R48 |

**Positive control (analytic):** WKB identity with independent `S` produces two knobs. **Negative control:** `S ∝ C · (LC)^{-1}` (or any lock `Ω ∝ c_eff`) recovers one knob / Gordon.

**Liveness:** Phase-1 has no engine null to book. G-GORDON is the instrument check that the one-knob pipeline still sees `γ = 0`.

**Discreteness:** N/A (no engine). If a later freeze adds a lattice, discreteness vs integrator is declared there.

---

## §8 — Out of scope

- Merging or headline-patching #1028 / #1029 / #1032.
- Valuing `𝒜_g`; moving nodes; photoelastic lab protocol.
- SN1987A / neutrino channel (already posed on #1029; independent of this freeze).
- Preferred-frame `α_1, α_2, α_3` (two-knob L2).
- Any claim that AVE “has GR at `O(m)`.”

---

## §9 — PREREG paragraph (skill Step 3)

```
PREREG (target: constitutive map ε₁₁ ↦ (L, C, S) on a frozen graph, Z pinned):
  Corpus state: OPEN — diagnosis of one-knob Gordon closed on unmerged #1028/#1029;
    map itself missing (F-B4; L3); kernel even so O(m) is not Ax4.
  Prior work cited: gordon-optical-metric.md:17,:33; operators.md:59;
    one-seventh-impedance-projection.md:13; achromatic-impedance-matching.md:20-28;
    nonlinear-vacuum-capacitance.md:27,:33; op14-local-clock-modulation.md:19;
    eq_axiom_5.tex:75-96; CLAUDE.md:75,:79-80; translation-circuit.md:98-104;
    2026-07-31_anisotropy-observable_scoping.md:657; PRs #1028/#1029.
  My prediction: Outcome A — SYM + frozen vertices leave (LC product) and (S/C)
    as the only candidate pair; the linear map is not in the axioms;
    (2,1,½) stays unforced.
  Why: Ax3 pins L/C; Ax4 is even; Op19's ν_vac is imported strain-per-strain;
    Cosserat S is the only object impedance matching does not constrain.
  Discriminating outcomes: A / B / C / Abort as §6 (DC→AC; no framework-level
    axiom kill on a null).
  Falsifier: a step that needs embedding node motion after F1-projection and
    irrep projection are exhausted — route to Grant, do not slide nodes.
```

---

## Rule-12 amendment A1 (2026-08-28) — KB + vocab landing; Grant's linear-regime question

**Does not edit any frozen bin, tolerance, edge, or §6 label.** The freeze header's "edits no KB" was true at freeze-by-push (`2704bc79`). This amendment records the documentation Grant asked for after the freeze.

**Answer (locked as restatement of canon, not a new derivation):** hop $L$ and $C$ **do not scale linearly in strain from Axiom 4.** Three senses (`def-ln3str`):

- **K (kernel):** $S(r)$ is even. Regime I ($r<\sqrt{2\alpha}$) freezes hop $L,C$ from Ax4. Solar $\varepsilon_{11}=1.486\times10^{-5}$ is deep Regime I. Kernel $\delta L/L$ at the limb is $O(10^{-10})$.
- **P (Op19):** $n=1+\nu_{\mathrm{vac}}\varepsilon_{11}$ is linear in $\varepsilon_{11}$ at leading order, still inside Regime I, **different expansion**. Coefficient imported.
- **Z (SYM):** $L\propto C$ at every gravity-class strain ($Z$ pinned). Not linear-in-strain.

**KB home:** `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/hop-lc-constitutive-grading.md` (no-claim, WALK). Vocabulary: rider on `def-q1escn` (gravity-scope Q-point, not node-slide); new `def-ln3str` (ambiguous disambiguation, not a coinage). Phase-1 constitutive derivation is **not** started by this amendment. Forks F1–F3 stay Grant-routed.

---

## Rule-12 amendment A2 (2026-08-28) — option-1 audit fence; does not edit A1 body

**Does not edit any frozen bin, tolerance, edge, or §6 label.** Grant greenlit option 1 of the hop-lc documentation audit (same PR). A1's K-bullet "Kernel $\delta L/L$ at the limb is $O(10^{-10})$" is **superseded as identification**: the pointer is kernel $\Delta S\approx\varepsilon_{11}^2/2\sim10^{-10}$ at the solar limb (`domain-catalog.md`:47, :50), **not** a derived hop $\delta L/L$. A1's "freezes hop $L,C$ from Ax4" is **superseded** as SYM-table column I frozen. Hop TL $L,C$ co-scale with $n$ remains an **unlicensed** bond-TL identification (Phase-1); achromatic matching licenses $\mu,\varepsilon$ only. Leaf writes Cosserat / gap shunt as $S_\gamma$ so it is not the kernel $S(r)$; the freeze body's $S$ in $\Omega^2=S/C$ is that shunt (Fork F1). Dropped: "kernel-linear"; uncited Mercury $\sim10^{-7}$; unlabeled $O(m)$. INVARIANT-S2 `:75` **not** touched. WD `:46` / Mercury-II-Yield **not** swept.

---

## Rule-12 amendment A3 (2026-08-28) — "hop" was TLM slang for the bond; does not edit freeze body, A1, or A2

**Does not edit any frozen bin, tolerance, edge, or §6 label.** Grant asked for the registered noun. Freeze §0 row 3 "series `L` and shunt `C` of the hop" and the later "EM hop" meant the **bond** (`def-b0nd01`) TL pair (`translation-circuit.md`:98). Live KB writes **bond TL** $L',C'$. The 2026-08-28 filename `hop-lc-constitutive-grading.md` is a Rule-12 stub; live path is `bond-lc-constitutive-grading.md`. `def-ln3str` **id unchanged**; surface form is now "linear (bond TL $L,C$ vs strain)". "Hop" stays in freeze/A1/A2 as historical wording. Does **not** start Phase-1. Does **not** touch hopping unknot or mechanical→EM hop (different objects). Sibling PRs #1028–#1032 **not** edited.

---

## Rule-12 amendment A4 (2026-09-06) — channel scope of the A2 fence; APPENDED, edits no frozen body, A1, A2 or A3

**Does not edit any frozen bin, tolerance, edge, or §6 label, and does not touch a byte of the freeze body, A1, A2 or A3.** A2's fence — *"Hop TL `L,C` co-scale with `n` remains an **unlicensed** bond-TL identification (Phase-1); achromatic matching licenses `μ,ε` only"* (`:224`) — is **right for the whole three-channel bond and wrong by omission for the channel this freeze's own §0 names**.

- **§0 row 1 (`:19`) names the channel:** *"hop delay / `c_eff` of the **gapless T2/EM channel**."* §1 `:50`/`:52` repeat it as "the EM hop"; A3 (`:230`) rewrites "hop" to the bond (`def-b0nd01`).
- **On that channel the identification is canon's own Class-A identity, not a Phase-1 open item:** `translation-circuit.md` §10.1 tabulates `L = μ₀` (*"series line inductance / inertia"*) at `:811` and `C = ε₀` (*"shunt line capacitance / compliance"*) at `:812`, both graded **A identity (§1)**; the rendered mirror is `docs/glossary.md:96`.
- **The refusal survives for the whole bond**, because a bond is not one line: three wired reactance channels `Z_EM` / `Z_shear` / `Z_bulk` (`def-gv1net`, `vocabulary-register.md:715-726`; `three-channel-impedances.md:20-22`), of which only `Z_EM ≡ Z_0` is electrical — `Z_shear` and `Z_bulk` are mechanical/acoustic and not in `Z_0` units (`resonant-lc-solitons.md:133`). There is no single `(L,C)` for "the bond" to identify with `μ,ε`.

**Applied on the branch (KB side, this is a scoping repair and no ruling):** every live fence site now carries the channel qualifier — `bond-lc-constitutive-grading.md` new §2.1 plus §2 / Sense P / Sense Z / §4; `translation-circuit.md:117`; `vocabulary-register.md` `def-ln3str` adjudicated-meaning, the (P) and (Z) flag bullets, and the verification field; `regime-equation-sets.md:27`; `docs/glossary.md:109` and `:110`. **Sense Z is now stated conditionally exactly as Sense P is** — its earlier unconditional "definitional once `Z=√(L/C)` is pinned" carried the same identification it was refusing elsewhere.

**Provenance of the fence, recorded because it was a same-day inversion.** `d1b55e87` (22:38) read *"so hop `L` and `C` **co-scale with `n`**"* — unconditional. `f943a034` (23:50) inverted it to the unqualified refusal, in the same commit that added A2 and A3. The flip **is** disclosed, by A2 itself; what does **not** exist anywhere in the tree is the **charter or the verdict** of the "hop-lc documentation audit" A2 credits — *"Grant greenlit option 1"* is **author-stated**, with no docket entry, no record doc, and no reviewer. Treat A2's fence as author-stated, and this amendment likewise.

**Forks F1–F3 stay Grant-routed. No solidity moves. Phase-1 is still not started.** This lane remains **UNAUDITED** — an adversarial pass is owed on the repaired scope, not only on the original fence.

---

## Rule-12 amendment A5 (2026-09-06) — CLASS 1 status-word demotion; APPENDED, the frozen body is byte-untouched

**This amendment edits nothing.** Two Class-1 sites sit inside the frozen body and are therefore **byte-untouchable**; they ride this dated note instead:

| Site | Frozen wording (unchanged, quoted) | How to read it |
|---|---|---|
| `:4` | *"Grant signed the lattice picture in-session 2026-08-28 (vertices unmoved; ε₁₁ = DC Q-point; observed matter/waves are AC)."* | **Grant-agreed (chat), WALK-GRADE, UNAUDITED.** The receipt is session agreement; the reasoning is not recorded, and no adversarial pass has run on this lane. |
| `:33` | *"## §1 — Signed ontology (Grant, 2026-08-28) — LOCKED"* | **Session-agreed ontology (Grant, chat).** "LOCKED" is this lane's own abort-condition — a derivation violating §1 is aborted (`:35`) — **not** a canon ratification, and not a docket ruling. |

**Why the demotion.** Grant ratified the convention 2026-09-03, verbatim: *"signed meaning passed adversarial pass plus physical/logical review with me."* This lane holds the second half only, and holds it as chat agreement. Neither receipt for the first half exists: there is no adversarial review of this branch, and no docket entry for it.

**The agreement is not withdrawn or weakened** — §1's six items remain exactly what Grant said in session, and the freeze's own honest framing at `:35` (*"These are session-signed, not derived here"*) already said so. Only the grading word moves.

**Propagated on the KB side** (live text, editable, so edited rather than noted):

- `bond-lc-constitutive-grading.md:5` — frontmatter `no-claim` "(Grant-signed 2026-08-28)" → "(Grant-agreed in chat 2026-08-28; no adversarial pass has run)", leaf tagged WALK-GRADE, **UNAUDITED**.
- `bond-lc-constitutive-grading.md:11` — "Grant signed the lattice picture" → "Grant **agreed the lattice picture in chat**", with the 2026-09-03 convention quoted and the missing receipt named.
- `bond-lc-constitutive-grading.md:17` — "§1 — Signed ontology" → "§1 — **Session-agreed** ontology (Grant, chat …; WALK-GRADE, UNAUDITED)".
- `bond-lc-constitutive-grading.md:26` — the paragraph re-reading Grant's session phrase *"micropolar inductance"* as \(S_\gamma\) was the **orchestrator's** correction of Grant's words, sitting under a heading carrying Grant's signature. It is lifted into its own **"Naming correction (orchestrator; Fork F1 — not Grant's wording, not ratified)"** block. This freeze already kept it separate at `:44`; the leaf had collapsed it.
- `vocabulary-register.md` `def-q1escn` — the **"★ GRAVITY-SCOPE RIDER (2026-08-28, Grant-signed picture, PR #1033)"** was appended into the **`verification`** field of a **SOLID** node, a field the register defines at its own `:61` as *"the verify-before-cite result for this entry."* A session picture cannot occupy that slot. The rider is **tagged inside** the field with an explicit NOT-A-VERIFICATION-RESULT delimiter (`⟦BEGIN/END TAGGED NON-VERIFICATION BLOCK⟧`) rather than moved to a bullet of its own — the register is anchored by line number by an external gate fixture (`research/drivers/iomega_law_number_check.py` cites `vocabulary-register.md:526`), so the repair is kept **line-count-neutral** and no other lane's gate is touched. Regraded **RESTATEMENT (def-q1escn R43 × `domain-catalog.md`:45-47 / `clm-82dxbj` solidity 0.63, input-only × `CLAUDE.md`:75), WALK-assembled, UNAUDITED, no ruling**, and the **Axiom-5 noun seam** it inherits is recorded rather than glossed: clause **G**'s object is *the bias* ε₁₁ (`eq_axiom_5.tex`:73) and clause **Q**'s is *the Q-point* (`:82`-`:87`); the register lists them as separate canonical nouns (`translation-circuit.md`:1107-1108). The rider's unqualified *"this **same noun**"* fused them. **Unadjudicated; recorded, not resolved.** R43 licenses the name only.

**No finding is removed by any of the above, and no solidity moves.** Forks F1–F3 stay Grant-routed. An adversarial pass on this lane is still owed.

---

## Rule-12 amendment A6 (2026-09-06) — CLASS 4: the mint receipt, measured; APPENDED, the frozen body is byte-untouched

**This amendment edits nothing.** The freeze header at `:4` states, and still states byte-for-byte:

> **Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; edits no KB leaf, register, ledger, or ruling; changes no solidity.**

**That receipt is false at the branch tip, and this is the measurement.** Counted by re-running the derived index and diffing `manuscript/ave-kb/.index/claims.jsonl` against `origin/main`:

| Prefix | Minted on this branch | Ids |
|---|---|---|
| `def-` | **1** | `def-ln3str` — *linear (bond TL $L$, $C$ vs strain)*, `node_type: definition`, **`status: ambiguous`**, `open_ambiguity: true`, canonical path `common/vocabulary-register.md` |
| `clm-` | 0 | — |
| `exp-` | 0 | — |
| `sup-` | 0 | — |
| `ilk-` | 0 | — |

Zero ids are removed or re-graded; `claims.jsonl` is `+1 / -0`, and no other file under `.index/` changes. **Method:** `make refresh-kb-metadata`, then `git diff origin/main...HEAD -- manuscript/ave-kb/.index/` parsed per JSON line. **Blind spot:** this counts what the *materialized index* holds; a register bullet the emitter does not parse would not appear (the emitter reads five required fields per INVARIANT-S12 and ignores additional bullets, `vocabulary-register.md`:62).

**This is a PR-body silence, not a covert mint.** The header's `:4` wording is a **freeze-time** statement, true at `2704bc79` when the prereg pushed alone. The mint is **already disclosed** by amendment **A1** (`:218`), verbatim: *"Vocabulary: rider on `def-q1escn` (gravity-scope Q-point, not node-slide); new `def-ln3str` (ambiguous disambiguation, not a coinage)."* A1 also already supersedes the header's "edits no KB" clause on the same grounds (`:210`). And the node minted is a **permitted restatement node** — `status: ambiguous` is the register's own value for *"≥2 corpus meanings, no locked sense, canon gated"* (`vocabulary-register.md`:57); it locks no meaning, adds no physics, and originates no `clm-`.

**Read the `:4` header, therefore, as:** *mints no `clm-`/`exp-`/`sup-`/`ilk-`; mints exactly one `def-` — `def-ln3str`, `status: ambiguous`, disclosed by A1; edits KB leaf/register per A1 and A3; changes no solidity.* The last clause is unchanged and holds: `make refresh-kb-metadata` reports **0** solidity lines rewritten.

The PR body is corrected in the same round to say the same thing, so the disclosure does not live only inside the frozen document.
