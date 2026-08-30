# S9 — TANK-STATE CHART JOIN — FROZEN PRE-REGISTRATION

**Date:** 2026-08-30 · **Branch:** `analysis/2026-08-29-tank-state-h1-join` · **Base:** `origin/main` @ `a3f4fef7` (PR #1019)
**H1 close (this branch, already pushed):** [`research/2026-08-29_h1-dc-circuit-objects_WALK.md`](2026-08-29_h1-dc-circuit-objects_WALK.md) @ `48eead40`. Grant signed 2026-08-30 (photoelastic → EE-native lattice terms; then this prereg).
**Class:** CHARACTERIZATION / JOIN. **Mints no `clm-` / `def-` / `exp-` / spoke row.** Does not edit `kirchhoff-network-method.md`, `translation-circuit.md`, `CLAUDE.md`, or `def-69f472`. Does not rewrite PR #1020. Does not start PR #1021. Engine `src/ave` byte-untouched.
**Presentation state:** `[DO-NOT-MERGE]` until Grant/orchestrator review. Rule 11 binds every bin below. Rule 12 binds every later amendment.

**THIS DOCUMENT COMMITS ALONE AND PUSHES FIRST** (freeze-by-push). No characterization note, no driver, and no lane-produced number exists in the tree at its push. The characterization commits second, if at all.

**Not this lane:** Chern-as-knot; Maxwell–Calladine; pick of \(\ker Y\) vs \(M\) (S10); over-braced `def-` (S5); extra-KVL vs headroom (S11); canonical “ground” (R43); Smith-ℂP¹ un-park; \((2,1,1/2)\); a value of \(\mathcal{A}_g\) (R48); coinage “Q-point gravity”; `#1033` \(\varepsilon_{11}\) as Q-point as TKI-forced (H5 stays `[branch:#1033]` WALK). Uniform \(A\) unread. Bond \(L,C\leftrightarrow\mu,\varepsilon\) **graded** map unlicensed.

---

## §0 — Standard Vacuum Analysis header (SVA v0.2-pilot; all 11 rows)

1. **SECTOR / OWNERSHIP:** three **orthogonal** circuit objects on one K4/srs graph, KEEP-ALL from H1. **Object 1 (A1)** owns DC prestress: bond-compliance capacitor \(C_{\mathrm{eff}}=C_0/S\) (`CLAUDE.md:73`; `nonlinear-vacuum-capacitance.md:14,:26–28`). **Object 2 (EM-transverse photon port)** owns light’s traveling-wave chart \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) (`photon-ee-mapping.md:31–38,:69–71`; `z0-derivation.md:100–102`; `port-register.md:47` channel 1). **Object 3** is the lumped Faraday \(L\)-strut of a scalar Kirchhoff mesh — short at DC (`kirchhoff-network-method.md:18–19,:30–32`). A1 ⊥ T2 (`master-equation.md:20` — never wire the winding into the breather’s own \((V_{\mathrm{inc}},V_{\mathrm{ref}})\)). EE is operational, not ontological (`def-1mpanl` ANALOGY). **Cross-wiring check:** Object 1’s DC \(V_Q\) is not Object 2’s \(V_{\mathrm{inc}}\). Kirchhoff node \(C\) is not A1 \(C_{\mathrm{eff}}\). The two English uses of \(T_2\) (photon-port irrep vs charge/winding) stay KEEP-ALL (H3).
2. **REGIME / PHASE-STATE:** MODE = characterization of the tank-state chart and its coupling (no engine run). REGIME = sub-yield lossless-reactive interior (Axiom 3) plus the DC (`.OP`) limit of that network. PHASE-STATE = cold-reactive plus a DC bias point that is **gauge-relative** (`CLAUDE.md:75`: only spatial gradients of \(A\) are observable). Small-signal: linearization about \(A_0\). Large-signal / Regime IV / source-free electron finder: **out of scope**.
3. **CIRCUIT STATEMENT (before any framework word):** a lossless series-\(L\) mesh is equipotential at DC. Static \(\nabla V\) cannot live on those \(L\)-edges. DC voltage that can sit at zero current lives on a capacitor (Object 1). Light is the incident/reflected pair on a distributed lossless line (Object 2). **Coupling:** the DC Q-point of Object 1 grades the small-signal \(\varepsilon_{\mathrm{eff}}(A_0),\mu_{\mathrm{eff}}(A_0)\) seen by Object 2 — **varactor-biased GRIN** when both sectors co-scale (SYM: \(Z=Z_0\), \(\Gamma=0\)) / **varactor-biased impedance-gradient** when \(\varepsilon\) only (ASYM: \(Z\) moves, \(\Gamma\neq 0\)). **Not** one voltage on one capacitor. **Total-vs-slot:** the measurable is a port ratio or a port phase difference on Object 2, never a per-series-element share of Object 1’s DC.
4. **PLANE & PROJECTION:** every \(\Gamma\) or \(Z\) claim in this characterization is at the **photon-port TL reference plane** (Object 2; EM-transverse \(\varepsilon\)–\(\mu\) port, `z0-derivation.md:100–102`). SYM is shunt-and-series co-scale ⇒ \(Z\) invariant ⇒ \(\Gamma=0\) at that plane (`translation-circuit.md:117`; `CLAUDE.md:75` W6). ASYM is \(\varepsilon\)-only ⇒ \(Z_{\mathrm{eff}}=Z_0\sqrt{S_\mu/S_\varepsilon}\) (`operators.md:54` Op14 asymmetric form) ⇒ \(\Gamma\neq 0\). Smith \(\Gamma=V_{\mathrm{ref}}/V_{\mathrm{inc}}\) is the **T4 ratio disk**, not the state (`translation-phase-space.md:102`). No new \(\Gamma\)-sign is chosen; none is computed numerically on this freeze.
5. **CONSTITUTIVE PROVENANCE:** \(S(A)=\sqrt{1-A^2}\) **DERIVED-SHAPE**. Cold-lattice \(L_{\mathrm{cell}}=\mu_0\ell_{\mathrm{node}}\), \(C_{\mathrm{cell}}=\varepsilon_0\ell_{\mathrm{node}}\) **DERIVED** as photon-port consistency (`z0-derivation.md:109–112`). SYM/ASYM grading **DERIVED-SHAPE** (INVARIANT-S2 W6). \(\nu_{\mathrm{vac}}=2/7\) **IMPORTED** if Op19 is used (`operators.md:59`). Gravity constitutive slot **FORKED(H2):** `clm-acdc07` gravity \(=S(A)\) (`form-deriving-value-importing.md:284`; `claim-quality.md:1379`) vs Op19 \(n(r)=1+\nu_{\mathrm{vac}}\varepsilon_{11}\) (`operators.md:59`; `refractive-index-of-gravity.md:15`). Op16 \(c_{\mathrm{shear}}=c_0\sqrt{S}\) **BRACKETED** — FLAG-CEFF-CITE vacated (`operators.md:212–235`); do not cite as settled. Op14 matter-clock \(\omega_{\mathrm{local}}=\omega_{\mathrm{global}}\sqrt{S}=(1-A^2)^{1/4}\) **DERIVED-SHAPE** on its leaf (`op14-local-clock-modulation.md:11–19`). \(\mathcal{A}_g\) **UNVALUED** (R48) — unused. Graded bond \(L,C\leftrightarrow\mu,\varepsilon\) **UNLICENSED**. \(\varepsilon_{11}\) as A1 Q-point **BRACKETED(H5 / #1033 WALK)**.
6. **ENERGY LEDGER:** rim-only. Axiom 3: no “loss,” “dissipated,” “damped,” or “Joule” without a named boundary-crossing port. GRIN / impedance-gradient are **reactive constitutives**, not ports. Object 1 stores DC reactive energy (varactor headroom, H6); Object 2 is lossless traveling-wave exchange. Characterization introduces **no** new port.
7. **CALIBRATABILITY:** primary targets are **dimensionless**: \(\Gamma\), \(Z/Z_0\), \(n\) as a ratio, \(\omega_{\mathrm{local}}/\omega_{\mathrm{global}}\). Smith is already a ratio. No target requires an absolute \(\mathcal{A}_g\) or a unit bridge. Chart coordinates \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) are **phasor coordinates** (`def-69f472`), not a real-space length (A46 firewall; dimensional-provenance: do not attach \(\ell_{\mathrm{node}}\) to the chart).
8. **DISCRIMINATION CLASS:** **DC→AC coupling** for the join (A1 DC Q-point read out by Object 2’s AC chart). **Pure-AC** Maxwell recovery (\(S\to 1\), \(\Gamma=0\) on a matched line) is **consistency, not a chord** — a null there is expected, not a framework-level negative (`clm-acdc07` (iii)). SM/GR counterfactual: GR already has an optical metric / refractive gravity and a static potential whose gradient is the force; **SYM GRIN that recovers \(n-1=2GM/c^2r\) is PEER-with-GR / Class C**, not AVE-distinct. ASYM \(\Gamma\neq 0\) from ε-only load is the live DC→AC shape (vacuum-impedance-mirror class); this lane **does not** book it as a chord — it only names the coupling. Tautology filter: restating INVARIANT-S2 W6 as “the join” **DEMONSTRATES** the grading shape; it does not **adjudicate** a new constitutive. No chord is claimed on any outcome of this characterization.
9. **CERTIFICATION PLAN:** bins and gates frozen here, before any characterization prose exists beyond H1. **UNRUN ≠ PASSED.** This freeze has **no engine numbers** and **no driver**. Negative control named at §5: a model that places static \(\nabla V\) on Object 3, or identifies Object 1 with Object 2’s capacitor. Positive control: the three 2-ports remain exhibitable from the cited leaves without shared terminals.
10. **ADJUDICATION ROUTING:** §6. H2–H6 stay listed — this lane does not pick them. `def-69f472` amend is **later, not here** (no second `def-`). Smith-ℂP¹ stays **not un-parked** (open-item RE-OPENED 2026-08-25 for ontology; `translation-phase-space.md:29–32` still pointer-PARKED — currency collision, **ORTHOGONAL**, out of scope). Characterization licenses **no** KB edit on any outcome.
11. **NUMERICAL CONDITIONING:** no iterated map, no residual fit, no scan regex. Working precision N/A. Named cancellation if a later engine were to host the join: Object 1 DC vs Object 2 AC must not share a 2-port or the inductor shorts the prestress (H1 `:104`). **No engine on this freeze** (`engine-capability-map.md:51,:55`: Master-Equation FDTD has the A1 cage and no winding; VacuumEngine3D has `v_scalar_from_v_inc(V_inc)` and **no independent A1 field**). A paper join is not an engine demonstration.

---

## §1 — The derivation target, stated precisely (ave-prereg Step 1)

**Characterize how the lattice tank-state chart \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) is modeled after H1, and how it couples** — A1 varactor Q-point grades photon-port constitutives as varactor-biased GRIN (SYM) / impedance-gradient (ASYM), not one voltage on one capacitor — **or** how bulk \(n\), \(Z\), clocks, and gravity-as-differential **emerge from that join**.

The gap is the **join that survives H1**, not a green-field ontology. Do not re-derive T0–T5, `clm-acdc07`, the Kirchhoff leapfrog, or Smith-ℂP¹.

**Signed sentence (Grant; do not mint a second `def-`):** phase space is the native **state-coordinate chart of the lattice tanks**, distinct from the graph that is space; Smith is a **ratio chart**, not the state. Amend `def-69f472` later.

---

## §1.5 — The physical picture, in plumber terms (ave-prereg Step 1.5)

- Every node is an LC tank on a graph that **is** space. The tank’s traveling-wave pair \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) **is** the light-sector state (Object 2). Smith \(\Gamma=V_{\mathrm{ref}}/V_{\mathrm{inc}}\) throws away overall amplitude and common phase — a ratio, not the state.
- A mass defect loads the **stretch** capacitors (Object 1). Those capacitors hold DC at zero current. The Faraday struts (Object 3) are shorts at DC; they cannot hold a static voltage drop. Putting gravity’s \(\nabla V\) on those struts was the H1 overclaim.
- Coupling is a **bias-point grade**, not a shared phasor: Object 1’s Q-point \(A_0\) is an **external parameter** of Object 2’s small-signal line (A1 ⊥ T2). Gradients of \(A_0\) make a matched GRIN (both \(\varepsilon\) and \(\mu\) move) or an impedance-gradient ( \(\varepsilon\) only). The materials word “photoelastic” is a spoke; it is **not** the hub name and it is **not** a \(p_{ijkl}\) to mint (`git grep photoelastic origin/main -- manuscript/ave-kb` → 0; `research/2026-07-31_anisotropy-observable_scoping.md:30,:657` — no measured \(p_{ijkl}\); `:893` kernel index is quadratic in \(A\), photoelasticity linear in strain — different expansions).
- Uniform load is unread. Gravity-as-interaction is a **differential** of that DC, read only as AC (`clm-acdc07` (i)).
- Light is Object 2’s chart, not the A1 varactor’s own `.AC` (H3). Matter still has a DC A1 store at \(A=\sqrt{\alpha}\) plus a T2 winding (H4; not closed here).

---

## §2 — Corpus state (ave-prereg Step 2)

**Corpus state: PARTIAL** — three objects + grading *shape* + AC-reads-DC-gradient are hub canon. **The join (chart modeling + bulk emergence from that split) is OPEN** on `origin/main`. H1 KEEP-ALL is **CLOSED** on this branch only (`48eead40`), not on main.

| Prior work | file:line (this worktree = `origin/main` for hub leaves) | Classification | Relation |
|---|---|---|---|
| H1 three-object close | `research/2026-08-29_h1-dc-circuit-objects_WALK.md` @ `48eead40` | **a** objects; join refused | SUPPORTS the split this prereg consumes |
| A1 \(C_{\mathrm{eff}}=C_0/S\) | `CLAUDE.md:73`; `nonlinear-vacuum-capacitance.md:14,:26–28` | **a** Object 1 | SUPPORTS grader ≠ graded |
| Photon I/Q on TL | `photon-ee-mapping.md:31–38,:69–71`; `z0-derivation.md:100–102,:115–124`; `port-register.md:47`; `def-b0nd01` | **a** Object 2 | SUPPORTS light = chart, not A1 `.AC` |
| Kirchhoff \(L\) short at DC | `kirchhoff-network-method.md:18–19,:30–32` | **a** Object 3 | CONTRADICTS one-mesh / \(\nabla V\) on \(L\)-edges |
| A1 ⊥ T2 | `master-equation.md:20` | **a** orthogonality | SUPPORTS A1 DC not a third T2 phasor |
| SYM GRIN / ASYM \(Z\)-move | `translation-circuit.md:117–118`; `CLAUDE.md:75` W6; `alpha-invariance-symmetric-gravity.md:15–22` | **a** coupling *shape* | SUPPORTS EE-native names; **c** for the named join |
| AC-reads-DC-gradient | `form-deriving-value-importing.md:292–297`; `translation-circuit.md:115–116`; `CLAUDE.md:75` gauge-relative \(A\) | **a** readout | SUPPORTS gravity-as-differential *readout*; does not pick H2 |
| T0–T5 ladder; T4 = ratio | `translation-phase-space.md:97–103,:113–119`; `def-69f472` (`vocabulary-register.md:161–164`, **ambiguous**, A46) | **a** chart vs ratio; **b** vocab | SUPPORTS signed sentence; do not amend `def-` here |
| Smith ontology | `_orchestration/open-items/2026-08-18-smith-chart-cp1-canonization.md:4,:43` RE-OPENED 2026-08-25; `translation-phase-space.md:29–32` still PARKED pointer | **d** ontology | ORTHOGONAL — do not un-park |
| Q-point name | `def-q1escn` (`vocabulary-register.md:491–494`) | **a** name | SUPPORTS DC grader; do not coin “Q-point gravity” |
| Gravity two slots (H2) | `clm-acdc07` `form-deriving-value-importing.md:284` / `claim-quality.md:1379` vs Op19 `operators.md:59` / `refractive-index-of-gravity.md:15` | **b** fork | REFINES — fork-record-both; do not pick |
| Clocks | Op14 leaf `:11–19`; Op16 FLAG-CEFF-CITE `operators.md:212–235` | **a** Op14; **a** Op16 vacated | SUPPORTS Op14; CONTRADICTS citing Op16 as settled |
| Photoelastic spoke | `git grep photoelastic origin/main -- manuscript/ave-kb` → **0**; `research/2026-07-31_anisotropy-observable_scoping.md:30,:657,:893` | **a** no \(p_{ijkl}\); **c** linear-vs-quadratic | CONTRADICTS materials noun as load-bearing; REFINES to GRIN / impedance-gradient |
| `:75` packs \(C_{\mathrm{eff}}\) into the T2 sentence | `CLAUDE.md:75` vs `:73` | **b** wording | REFINES — H1 reads `:73`; do not edit `CLAUDE.md` |
| Strain-on-\(I\) vs TKI | `kirchhoff-network-method.md:19` vs `def-1mpanl` / `translation-circuit.md:17–21` | **d** wording (S1) | ORTHOGONAL to the join; cite only |
| Engine split | `engine-capability-map.md:51,:55` | **d** instrument | SUPPORTS KEEP-ALL; no one-backend demonstration |
| Round-3 1:1 / spillover | `[branch:#1020]` only (`9efcc8db` not on this branch) | **d** | Cite as `[branch:#1020]`; do not rewrite |

**What is genuinely open and is this lane’s to close:** a **walk-grade characterization** of (i) the tank-state chart as Object 2’s coordinates with Object 1 as external grader, and (ii) how bulk \(n,Z\), clocks, and gravity-as-differential sit on that join **without** collapsing the three 2-ports. Not a new primitive. Not an engine run. Not a constitutive-slot pick (H2).

**Same-session research on this worktree:** only the H1 note. Picture-lock / spillover / S9 open-item live on `#1020`, not here.

---

## §3 — ANALYTIC EXPECTATIONS, frozen (ave-prereg Step 3.9; fork-record-BOTH)

This is a **characterization**, not a scaling-law magnitude run. **Step 3.5 dimensional analysis: N/A for new magnitudes.** Frozen identities below are the numbers the picture already has. No new OOM is predicted.

### §3.1 Modeling claim (WALK until the characterization lands)

**T2 chart \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) is the tank state** (rung T2). **A1 Q-point \(A_0\) is an external parameter** that grades Object 2’s constitutives, **not** a third phasor coordinate. Smith is T4 \(\Gamma=V_{\mathrm{ref}}/V_{\mathrm{inc}}\) (ratio). Gravity-as-interaction = \(\nabla A\) on the graph, AC-read. Fiber-bundle noun stays WALK if used at all.

### §3.2 Coupling identities (SYM / ASYM) — DEMONSTRATED if recited, not a new derivation

| Load class | Frozen identity | Fireability |
|---|---|---|
| **SYM** (ε and μ co-scale) | \(Z/Z_0 = 1\), \(\Gamma = 0\) — varactor-biased **GRIN** | **ENTAILED** by INVARIANT-S2 W6 / `translation-circuit.md:117` if only restated. Honest verb: **DEMONSTRATED**. |
| **ASYM** (ε only, \(S_\mu=1\)) | \(Z_{\mathrm{eff}}/Z_0 = 1/\sqrt{S_\varepsilon}\), \(\Gamma \neq 0\) — varactor-biased **impedance-gradient** | **ENTAILED** by W6 / Op14 asymmetric form if only restated. Honest verb: **DEMONSTRATED**. |
| **Cold lattice** | \(L_{\mathrm{cell}}=\mu_0\ell_{\mathrm{node}}\), \(C_{\mathrm{cell}}=\varepsilon_0\ell_{\mathrm{node}}\) | **ENTAILED** identity (`z0-derivation.md:109–112`). Do not promote to a gravity constitutive. |

**What is FIREABLE** (the actual discriminator of this lane): whether a characterization of bulk \(n,Z\), clocks, and gravity-as-differential **can be written without** (i) sharing Object 1 and Object 3 terminals, (ii) adding \(A_0\) as a third T2 phasor, (iii) treating Smith as the state, or (iv) minting \(p_{ijkl}\).

### §3.3 Bulk emergence — fork-record-BOTH (do not pick)

**\(Z\):** SYM \(Z=Z_0\) / ASYM \(Z\) moves — frozen as §3.2. **Ingredient-closed** on the hub.

**\(n\) / gravity constitutive (H2) — both branches frozen:**

- **SLOT-S:** gravity \(= S(A)\) operating-point field (`form-deriving-value-importing.md:284`). Index from kernel, not from Op19’s linear \(\varepsilon_{11}\).
- **SLOT-OP19:** \(n(r)=1+\nu_{\mathrm{vac}}\varepsilon_{11}\), \(\nu_{\mathrm{vac}}=2/7\) (`operators.md:59`); solar form \(n=1+2GM/c^2r\) (`refractive-index-of-gravity.md:15`).

The characterization **exhibits both slots as remaining H2**. Awarding one is **out of scope**. A prose paragraph that silently picks one **fails G-H2**.

**Clocks — both branches frozen; Op16 excluded:**

- **CLOCK-OP14:** \(\omega_{\mathrm{local}}/\omega_{\mathrm{global}}=\sqrt{S}=(1-A^2)^{1/4}\) (`op14-local-clock-modulation.md:19`). Shear matter-clock.
- **CLOCK-1 (slope-1 redshift):** PEER-with-GR if used as \(\omega_\infty=\omega_0\sqrt{1-A}\); the bias-propagation lane already tagged that arithmetic **ENTAILED** / tautology-adjacent. This lane does **not** re-run it.
- **CLOCK-OP16:** **do not cite.** FLAG-CEFF-CITE vacated.

**Gravity-as-differential readout:** uniform \(A\) unread; every AVE-distinct observable is an AC reading of a DC gradient or topology (`form-deriving-value-importing.md:292–297`). **ENTAILED** as readout principle. Not a constitutive pick.

### §3.4 Observable robustness ladder (Step 3.7(a))

**existence/class of the three-object join (PRIMARY, gating) → sign/shape (\(\Gamma=0\) vs \(\Gamma\neq 0\), SYM vs ASYM) → ratio (\(Z/Z_0\), \(\omega_{\mathrm{local}}/\omega_{\mathrm{global}}\)) → magnitude (\(n-1\), \(\mathcal{A}_g\), birefringence coefficient: SUPPLEMENTARY / out of scope / H2-gated).**

If magnitudes prove knob-ridden or slot-forked, **the class of the join still stands** and the lane reports the demotion rather than discovering it mid-arc.

### §3.5 Photoelastic translation (Grant 2026-08-30) — frozen vocabulary

| Materials spoke (retired as load-bearing) | EE-native lattice |
|---|---|
| photoelasticity / \(p_{ijkl}\) | A1 varactor Q-point grades \(\varepsilon_{\mathrm{eff}}(A_0),\mu_{\mathrm{eff}}(A_0)\) seen by the EM-transverse TL |
| birefringence from prestress | **ASYM** (ε-only): \(Z\) moves, \(\Gamma\neq 0\) — varactor-biased **impedance-gradient** |
| isotropic index, no reflection | **SYM** (ε and μ co-scale): \(Z=Z_0\), \(\Gamma=0\) — varactor-biased **GRIN** |

Do **not** mint a photoelastic tensor. Linear-in-strain vs kernel-\(A^2\) remains an anisotropy / H2 residual, not an S9 mint.

---

## §4 — FROZEN VERDICT GRAMMAR (Rule 11)

| Bin | What it is | Fireable? |
|---|---|---|
| **A — JOIN-HOLDS** (expected) | Chart = Object 2 state; \(A_0\) = external grader; coupling = GRIN / impedance-gradient; Smith = ratio; gravity-as-interaction = AC-read \(\nabla A\); bulk \(n,Z\), clocks **exhibited as consequences or explicitly left on H2** without a third phasor or a shared 2-port. | **FIREABLE** as a *modeling* verdict. Sub-claims that only restate W6 / A1 ⊥ T2 are **ENTAILED** and must be verb’d **DEMONSTRATED**. |
| **B — A1-AS-PHASOR** | Characterization requires \(A_0\) as a third coordinate of the \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) chart. | **FIREABLE.** Contradicts H1 KEEP-ALL / `master-equation.md:20`. |
| **C — ONE-CAPACITOR / ONE-MESH** | Static \(\nabla V\) on Object 3, or Object 1 identified with Object 2’s / Kirchhoff’s \(C\), still “works.” | **FIREABLE.** Contradicts H1 close. Would walk H1 back, not silently absorb into A. |
| **D — SMITH-AS-STATE** | The ratio disk is treated as the tank state. | **FIREABLE** as vocab. Contradicts the signed sentence and T2→T4 quotient (`translation-phase-space.md:102`). |
| **E — BLOCKED** | Characterization cannot proceed without picking H2, valuing \(\mathcal{A}_g\), un-parking Smith-ℂP¹, minting a `def-`/`clm-`/spoke row, or editing Kirchhoff / `CLAUDE.md`. | **FIREABLE.** Route to Grant; do not pick. |

**Masquerade guard (Step 3.6, pre-armed):** Bin C and Bin D must not be absorbed into A via “persists” / “essentially the same mesh.” Primary rung is **existence of three 2-ports**.

**No framework-level negative** from a pure-AC matched-line null.

---

## §5 — Certification: gates, controls, liveness (frozen; UNRUN ≠ PASSED)

**Positive control (Step 3.8(a)):** the characterization can point at three distinct 2-ports in the cited leaves (Object 1 capacitor holds DC; Object 2 TL carries \((V_{\mathrm{inc}},V_{\mathrm{ref}})\); Object 3 \(L\) ⇒ \(V_A=V_B\) at DC) **without identifying their terminals**. H1 already ran this exhibit; the characterization must **preserve** it.

**Negative control:** a paragraph that places static \(\nabla V\) on the \(L\)-struts, or that sets Object 1’s DC \(V_Q =\) Object 2’s \(V_{\mathrm{inc}}\). That paragraph is a **fail of G-PORTS**, not a Bin-A success.

**Structural-degeneracy (Step 3.8(b)):** \(\Gamma=0\) on SYM is **forced** by \(Z=Z_0\), not evidence that “reflection vanished empirically.” Report it as identity, not as a measured null.

| Gate | Frozen criterion |
|---|---|
| **G-PORTS** | Three 2-ports remain distinct. Shared terminals ⇒ Bin C, not A. |
| **G-CHART** | \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) named as T2 state; Smith named as T4 ratio. Collapse ⇒ Bin D. \(A_0\) as third phasor ⇒ Bin B. |
| **G-H2** | Both gravity slots named; neither picked. Silent pick ⇒ fail, route Grant. |
| **G-OP16** | Op16 formula / vol-2 receipts not cited as supporting. Op14 leaf may be cited. |
| **G-AGFREE** | \(\mathcal{A}_g\) unvalued, unused. |
| **G-R43** | No canonical “ground.” |
| **G-PHOTO** | Coupling named GRIN / impedance-gradient. No \(p_{ijkl}\) mint. “Photoelastic” only as retired spoke. |
| **G-MINT** | Diff against this freeze adds no `clm-`/`def-`/`translation-circuit.md` row / Kirchhoff / `CLAUDE.md` / `def-69f472` body edit. |
| **G-ENGINE** | `git diff --stat a3f4fef7..HEAD -- src/` stays EMPTY at every commit of this lane. |
| **G-BRANCH** | `#1020` / `#1033` files cited only via `git show` + `[branch:#…]`. `9efcc8db` is not on this branch. |
| **G-ECHO** | No chord; SYM→GR \(n\) is Class C / PEER-with-GR if recited. `clm-acdc07` (iii) honored. |
| **G-AX3** | No loss word without a named port. |
| **G-Holds** | H2–H6 remain listed; H3–H6 not closed by assertion. |

**Gate-floor (Step 3.7(b)):** no noise-limited cells; no numerical gates.

---

## §6 — Adjudication routing + falsifiers (frozen)

- **F1 (my framing is wrong — Bin C).** If the only consistent model of bulk \(n,Z\) / clocks / gravity-as-differential **requires** a static \(\nabla V\) on Object 3 or one shared capacitor, H1 does not survive contact with S9. Report **C**, stop to Grant. Do not “fix” Kirchhoff on this lane.
- **F2 (Bin B).** If \(A_0\) must sit on the same chart as \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) as a third phasor, A1 ⊥ T2 was mis-applied. Report **B**, stop.
- **F3 (Bin D).** If the characterization cannot state the tank state without the Smith disk, the signed sentence fails. Report **D**. Do not un-park ℂP¹ to rescue it.
- **F4 (Bin E / G-H2).** If the join cannot be written without picking SLOT-S vs SLOT-OP19, that is **H2 still holding**, not a license to pick. Report **E**.
- **F5 (photoelastic residual).** If the characterization needs a rank-4 \(p_{ijkl}\) as a new hub object, G-PHOTO fails. The 2026-07-31 linear-vs-quadratic residual stays on the anisotropy shelf.

**Routing on A:** a walk-grade join note on this branch; **proposed** `def-69f472` amendment text **not landed**; **proposed** `translation-circuit.md` wording **not landed** (Grant mint later). H2–H6 listed unchanged.

**The lane’s fence on itself:** no KB edit, no register edit, no solidity move, no Kirchhoff edit, no `#1020` rewrite, no engine edit, on any outcome.

**H2–H6 remainder (unchanged from H1):**

| Hold | Remainder |
|---|---|
| **H2** | `clm-acdc07` \(S(A)\) vs Op19 linear-in-\(\varepsilon_{11}\) |
| **H3** | Light is T2 \((V_{\mathrm{inc}},V_{\mathrm{ref}})\), not A1 `.AC` |
| **H4** | Matter DC A1 store at \(A=\sqrt{\alpha}\) plus T2 winding |
| **H5** | \(\varepsilon_{11}\) as A1 Q-point is `#1033` WALK, not TKI-forced |
| **H6** | Lossless TL needs no DC bias; P0 over-brace is varactor headroom; extra-KVL is S11 |

---

## §7 — What the characterization may write (scope fence)

**In:** a WALK-GRADE note that (1) models the tank-state chart as Object 2 coordinates on the graph that is space, (2) treats \(A_0\) as grader, (3) names coupling GRIN / impedance-gradient, (4) exhibits bulk \(n,Z\) / clocks / gravity-as-differential as **consequences or as H2-forked**, (5) keeps Smith as T4.

**Out:** derivation of a new constitutive; engine run; spoke row; second `def-`; Chern/Calladine/\(\ker Y\); \(\mathcal{A}_g\); Q-point gravity; Smith-ℂP¹ ontology.

**Class of the work:** **C — consistency / organizing** for re-assembly of hub identities; the OPEN piece is the **join paragraph**. Not D (no new primitive, no engine). Not a mint.

---

> **Freeze provenance.** SVA v0.2-pilot §0 filled, all 11 rows. Corpus-grep 2026-08-30 (AVE-Core hub + sibling mirrors as KB echoes, not independent join content). Hub cites byte-checked on this worktree against `origin/main` leaves. H1 @ `48eead40` already on `origin/analysis/2026-08-29-tank-state-h1-join` before this file existed. **This document commits ALONE and pushes FIRST;** characterization, if any, commits second. `[DO-NOT-MERGE]`.
