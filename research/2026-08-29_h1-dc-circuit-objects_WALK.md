# H1 — three circuit objects, not one mesh (WALK-GRADE)

**Status:** WALK-GRADE close of hold **H1**. **Grant signed 2026-08-30** to proceed (photoelastic → EE-native lattice terms; then commit/push; then S9 prereg). Still no `translation-circuit.md` row, `def-`, or `clm-` on this lane — those wait a later mint, not the prereg.

**Class:** records / circuit-object identification. Consistency / organizing — not an emergence test (`consistency-vs-emergence`). Mints nothing. Does not edit `kirchhoff-network-method.md` (S1 is a parked wording PR). Does not rewrite PR #1020.

**Branch:** `analysis/2026-08-29-tank-state-h1-join` off `origin/main` @ `a3f4fef7`. Isolated worktree. **Not** `#1020` (`research/2026-08-26-overbraced-crystal-walk`) and **not** `#1033` (`research/2026-08-28-qpoint-constitutive`).

**Signed record cited from the #1020 ref, not applied here.** Pads landed 2026-08-29 as `9efcc8db`. `git branch --contains 9efcc8db` returns only `research/2026-08-26-overbraced-crystal-walk`. `gh pr view 1020` → `state: OPEN`, `mergedAt: null`. `gh pr view 1033` → `state: OPEN`, `[DO-NOT-MERGE]`. Tags: `[branch:#1020]`, `[branch:#1033]`.

---

## Sector / regime (declare first)

**SECTOR:** three **orthogonal** circuit objects on one K4/srs graph. A1 ⊥ T2 is already hub (`master-equation.md:20`). EE is operational, not ontological (`def-1mpanl` ANALOGY; Cosserat co-equal via TKI). No spoke-to-spoke weld.

**REGIME:** sub-yield lossless-reactive interior (Axiom 3) plus the DC (`.OP`) limit of that same lossless network. Not Regime IV. Not a source-free electron finder.

**COORDINATES:** this note is about **which 2-terminal element holds DC voltage**. Light’s state chart \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) is named only to keep it off the A1 capacitor (H3). Phase-space ontology is S9; `def-69f472` is not amended here.

---

## What H1 was holding `[branch:#1020]`

From `git show origin/research/2026-08-26-overbraced-crystal-walk:research/2026-08-29_picture-lock-spillover.md` S2 (not on this tree):

A lossless series-\(L\) / shunt-\(C\) mesh is **equipotential at DC** (inductors short). A static \(\nabla V\) cannot live on those \(L\)-edges. DC prestress lives on A1 **bond-compliance** capacitors \(C_{\mathrm{eff}}=C_0/S\), which can hold DC voltage at zero current. Light is T2 on the TLs. “Same mesh as the Kirchhoff leaf” overclaims. Coupling is A1 grading T2 constitutives — EE-native: **varactor-biased GRIN** (SYM) / **varactor-biased impedance-gradient** (ASYM) on the photon-port TL — **not** one voltage on one capacitor. (Spillover workshop word “photoelastic” is a materials spoke; retired as load-bearing.)

**Already signed (do not re-litigate):** from inside this medium, DC is read only as an AC difference. Uniform DC can exist unread. Gravity-as-interaction is a **differential** of that DC, read by AC probes (`clm-acdc07` (i); INVARIANT-S2: only gradients of \(A\) are observable).

**This note’s job:** grep-ground the three circuit objects and **close H1** without collapsing H2–H6 and without forcing a join of the three objects.

---

## Verdict

**H1 CLOSES.** The Round-3 1:1 table’s unsigned cells — “same scalar Kirchhoff mesh” and “\(\varepsilon_{11}\) is \(V\) on the \(L\)-edges” — stay **unsigned**, and they stay unsigned **because the Kirchhoff leaf’s own update already forbids a static \(\nabla V\) on the \(L\)-struts.** DC prestress has a different 2-port (A1 \(C_{\mathrm{eff}}\)). Light has a different 2-port (distributed TL, \(V_{\mathrm{inc}},V_{\mathrm{ref}}\)). Coupling is constitutive grading of the TL / photon-port parameters by the A1 operating point, not a single voltage on a single capacitor.

**KEEP-ALL** the three objects until a later join is forced. Identity-collapse probe (`ave-ee-first-mapping` trigger 7): they share English (“capacitance”, “voltage”, “\(L\)”) and they are **not** one bench element. A1 ⊥ T2 is the ratified grade split, not a new weld.

**No Grant question is required to close H1.** Residuals that look like questions are already owned by other holds / parked wording (listed below).

---

## The three objects (grep-grounded)

### Object 1 — A1 bond-compliance capacitor \(C_{\mathrm{eff}}=C_0/S\)

**Hub cell:** longitudinal stretch reactance \(1/k_a\). EE operational name: metric varactor. Holds DC voltage at zero current (capacitor = open at \(\omega=0\)).

Canon:

- `manuscript/ave-kb/CLAUDE.md:73` (INVARIANT-S2 Axiom 4 sector split, Grant-ratified 2026-06-15): \(C_{\mathrm{eff}}=C_0/S\) (↑) is the **longitudinal-A1 bond compliance**; the transverse-T2 permittivity \(\varepsilon_{\mathrm{eff}}=\varepsilon_0 S\) (↓) is a **distinct** object. They are **orthogonal reactances** (A1 ⊥ T2) that share the EE name “capacitance”.
- `nonlinear-vacuum-capacitance.md:14` restates the same split, then `:26–28`:

$$
C_{\mathrm{eff}}(V)=\frac{C_0}{S(V)},\qquad S(V)=\sqrt{1-(V/V_{\mathrm{snap}})^2}.
$$

- Knee is \(V_{\mathrm{snap}}\approx 511\,\mathrm{kV}\) on this object, not \(V_{\mathrm{yield}}\) (`nonlinear-vacuum-capacitance.md:16–18`; `def-vyvsn1`). Electron A1-core at \(A=\sqrt{\alpha}\) is **sub-saturated** on this capacitor (H4 lists that store; this note does not close H4).
- `def-q1escn`: Q-point **name** for the saturation-state \(A\) as DC bias. R43: never canonical “ground.” Clause Q is DC reference-fixing, not AC phase-normalization. **This note does not coin “Q-point gravity.”** H5 (\(\varepsilon_{11}\) as A1 Q-point) stays `[branch:#1033]` WALK-GRADE.

DC voltage on this 2-port is the prestress / headroom store (H6: varactor reactive-arc headroom, not a TL bias requirement).

### Object 2 — T2 / photon-port transmission line \((V_{\mathrm{inc}},V_{\mathrm{ref}})\)

**Hub cell:** distributed lossless bond as MODEL-OF a single-mode TL (`def-b0nd01`). Light is the traveling-wave state on that line.

Canon:

- `photon-ee-mapping.md:31` — free photon: sector \(T_2\) only, \(\Gamma=0\), matched \(Z_0\), no core.
- `photon-ee-mapping.md:69–71` — on each TL bond, \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) **are** the photon’s I/Q:

$$
E\sim(V_{\mathrm{inc}}+V_{\mathrm{ref}}),\qquad B\sim(V_{\mathrm{inc}}-V_{\mathrm{ref}})/Z.
$$

- `z0-derivation.md:100–102` — the bond-as-distributed-TL section is the **EM-transverse / \(\varepsilon\)–\(\mu\) photon port**, cold lattice \(S(A)=1\), lossless-reactive. Explicit fence: **not** the T2/charge sector and **not** the A1 mass store. Consistency class; no new \(Z_0\) or \(c_0\).
- `port-register.md:47` channel 1: EM-transverse photon, irrep \(T_2\), \(Z_{\mathrm{EM}}=Z_0\).

**KEEP-ALL** the two \(T_2\) English uses (photon-port irrep vs charge/winding “3”). H1 does not pick them. H3 stays listed: light is this object’s \((V_{\mathrm{inc}},V_{\mathrm{ref}})\), not the A1 varactor’s own `.AC`.

**Bond \(L,C\leftrightarrow\mu,\varepsilon\) graded map is unlicensed** (`[branch:#1033]`; kickoff). The **cold-lattice** per-cell pair \(L_{\mathrm{cell}}=\mu_0\ell_{\mathrm{node}}\), \(C_{\mathrm{cell}}=\varepsilon_0\ell_{\mathrm{node}}\) already sits on main at `z0-derivation.md:16–20,:109–112` as a photon-port consistency identity. H1 does not promote that identity into a gravity constitutive, and does not value \(\mathcal{A}_g\).

### Object 3 — Kirchhoff \(L\)-strut (lumped series-\(L\) of a scalar LC mesh)

**Hub cell:** Faraday inductor on a graph edge. At DC it is a **short**.

Canon (equations stay; names are S1):

- `kirchhoff-network-method.md:18–19`: nodes \(=\) capacitors storing \(V_i\); struts \(=\) inductors carrying \(I_{ij}\).
- `kirchhoff-network-method.md:30–32`:

$$
I_{\mathrm{new}}=I_{\mathrm{old}}+\frac{\Delta t}{L}(V_A-V_B).
$$

At DC, \(\mathrm{d}I/\mathrm{d}t=0\) \(\Rightarrow\) \(V_A=V_B\). Every pair of nodes joined by an \(L\)-strut is **equipotential**. A static \(\nabla V\) **cannot** live on those edges.

- `z0-derivation.md:115–124`: that same lumped series-\(L\) / shunt-\(C\) section is the \(\omega\tau\ll 1\) limit of the **photon-port** distributed line. At \(\theta=\omega\tau=0\), \(\sin\theta=0\), \(\cos\theta=1\), so \(\mathrm{ABCD}_{\mathrm{line}}=\mathrm{ABCD}_{\mathrm{lump}}=I_2\): zero electrical length, no series voltage drop. H6 is the same fact from the other side: a lossless TL **needs no DC bias** to propagate.

**Pairing collision (cite only; S1 owns the wording).** `kirchhoff-network-method.md:19` writes strut current as “inductive flux **or physical lattice strain**.” `def-1mpanl` (Grant 2026-07-21) pins the **impedance** analogy: stress \(\leftrightarrow\) voltage, velocity \(\leftrightarrow\) current (`translation-circuit.md:17–21`). Strain-on-\(I\) is the **mobility** pairing. Round 3 `[branch:#1020]` already named this collision. This note does not relabel the leaf.

**Do not identify Object 3 with Object 1.** If the A1 compliance capacitor and the Kirchhoff \(L\) shared the same two terminals, the inductor would short the capacitor at DC and Object 1 could not hold prestress. They do not share a 2-port: A1 ⊥ T2 (`master-equation.md:20` — never wire the winding into the breather’s own \((V_{\mathrm{inc}},V_{\mathrm{ref}})\)). The scalar Kirchhoff mesh is a **one-sector lumped model**. “Same mesh as the Kirchhoff leaf” is the overclaim H1 was holding.

**Do not identify Kirchhoff node \(C\) with A1 \(C_{\mathrm{eff}}\).** Node \(C\) in the Kirchhoff leapfrog (`kirchhoff-network-method.md:40–41`) is the shunt \(C\) of the lumped LC pair (Object 3’s partner). A1 \(C_{\mathrm{eff}}\) is Object 1. Same EE word; orthogonal reactances (`CLAUDE.md:73`).

---

## Coupling that survives H1 (not a mint)

**Already on the hub, not a new row:** a spatial gradient of the A1 operating point \(A_0\) modulates the small-signal parameters seen by Object 2.

`CLAUDE.md:75`: the tank state \(A\) is **gauge-relative**; only spatial gradients are observable. Small-signal transverse propagation through a region at \(A_0\) sees modulated \(\varepsilon_{\mathrm{eff}}=\varepsilon_0 S(A_0)\), \(\mu_{\mathrm{eff}}=\mu_0 S(A_0)\). SYM: both sectors scale, \(Z=Z_0\), \(\Gamma=0\). ASYM: \(\varepsilon\) only, \(Z\) moves (`translation-circuit.md:117–118`; `CLAUDE.md:75` W6).

That is A1 **grading** the photon-port small-signal constitutives. **EE-native lattice term (Grant 2026-08-30: translate; do not leave the materials spoke as the name):**

| Materials spoke (retired as load-bearing) | Hub / EE-native lattice |
|---|---|
| photoelasticity / strain-optic \(p_{ijkl}\) | DC Q-point of the A1 varactor grades \(\varepsilon_{\mathrm{eff}}(A_0)\), \(\mu_{\mathrm{eff}}(A_0)\) seen by the EM-transverse TL |
| birefringence from prestress | **ASYM** (ε-only): \(Z\) moves, \(\Gamma\neq 0\) — varactor-biased **impedance-gradient** |
| isotropic index shift, no reflection | **SYM** (ε and μ co-scale): \(Z=Z_0\), \(\Gamma=0\) — varactor-biased **GRIN** (matched line) |

Do **not** mint a photoelastic tensor. `grep photoelastic manuscript/ave-kb` from this worktree returned **0** hits; the 2026-07-31 anisotropy scoping already recorded that the corpus has no measured \(p_{ijkl}\). The live hub cell is INVARIANT-S2 SYM/ASYM + Op14/Op16, already EE (`translation-circuit.md:112–118`: Q-point, common-mode, differential, SYM, ASYM). Bond \(L,C\leftrightarrow\mu,\varepsilon\) stays unlicensed.

**Not** “one voltage on one capacitor”: Object 1’s DC \(V_Q\) is not Object 2’s \(V_{\mathrm{inc}}\). Object 2’s AC is the readout (`clm-acdc07` (i)):

`form-deriving-value-importing.md:292–297`: **all measurement is AC.** A uniform DC bias is gauge-relative and self-cancels. Every AVE-distinct observable is an AC reading of a DC **gradient or topology**.

`translation-circuit.md:115–116`: uniform field \(\leftrightarrow\) common-mode bias; field gradient \(\leftrightarrow\) differential bias. Two **registers** of “common-mode” (readout-level unreadability vs coupling-level WEP-CMRR) stay KEEP-ALL (`def-cmdiff` on main). This note does not collapse them.

**INVARIANT-S2 wording collision (not a Grant-blocker; not edited here).** `:75` still lists \(C_{\mathrm{eff}}=C_0/S(A_0)\) in the same small-signal-transverse sentence as \(\varepsilon_{\mathrm{eff}}\) and \(\mu_{\mathrm{eff}}\). `:73` already split that \(C_{\mathrm{eff}}\) onto A1. H1 reads `:73` as load-bearing and leaves the `:75` parenthetical as S1-adjacent wording debt. Do not “fix” `CLAUDE.md` on this lane.

---

## What this does **not** close (H2–H6 stay listed)

| Hold | One-line remainder | Why H1 does not eat it |
|---|---|---|
| **H2** | `clm-acdc07` gravity \(=S(A)\) vs Op19 linear-in-\(\varepsilon_{11}\) (Regime I kernel frozen). Two constitutive slots. | H1 only places DC voltage off the \(L\)-edges. It does not pick the gravity constitutive slot. |
| **H3** | Light is T2 \((V_{\mathrm{inc}},V_{\mathrm{ref}})\), not the A1 varactor’s own `.AC`. | Named as Object 2. Not re-derived. |
| **H4** | Matter has a **DC A1 store** at \(A=\sqrt{\alpha}\) plus a T2 winding. Gravity couples to the store. | Object 1 + `master-equation.md:20` two-“3”s. Mass-as-AC undersells; not closed here. |
| **H5** | \(\varepsilon_{11}\) as A1 Q-point is `#1033` WALK-GRADE, not TKI-forced (stress vs strain). | Do not coin “Q-point gravity.” Do not value \(\mathcal{A}_g\). |
| **H6** | Lossless TL needs no DC bias. P0 over-brace is varactor **headroom**, not generic line theory. | Object 2 / Object 3 at \(\theta=0\). Extra-KVL vs headroom remains S11. |

**S9 prereg** follows this close (Grant 2026-08-30). The gap is the **join that survives this close** (A1 Q-point grades photon-port constitutives as varactor-biased GRIN / impedance-gradient; bulk \(n,Z\), clocks, gravity-as-differential), not a green-field ontology. Signed sentence (do not mint a second `def-`): phase space is the native state-coordinate chart of the lattice tanks, distinct from the graph that is space; Smith is a ratio chart, not the state. Amend `def-69f472` later. Smith-ℂP¹ stays parked.

---

## Hard stops honored

- No Chern/Berry-as-knot; no Maxwell–Calladine weld; no “therefore no knot.”
- No pick of \(\ker Y\) vs \(M\)-eigenmode (S10).
- No over-braced `def-` (S5 KEEP-ALL). No pick of extra-KVL vs A1 headroom (S11).
- R43: no canonical “ground.”
- Uniform \(A\) unread; only gradients.
- Vertices stay put. No \((2,1,1/2)\). No \(\mathcal{A}_g\) value.
- `#1020` walk not rewritten. `kirchhoff-network-method.md` not edited. No `translation-circuit.md` rows.

---

## Shelf inventory (read; not re-derived)

| Item | Use here |
|---|---|
| `translation-phase-space.md` T0–T5 | Chart vs graph vs Smith-ratio already laddered. S9 consumes; H1 does not retread. |
| `form-deriving-value-importing.md` `clm-acdc07` | Measurement principle cited; gravity-slot remains H2. |
| `translation-circuit.md:112–119` | Q-point / common-mode / differential / SYM / ASYM **read, no rows added**. |
| INVARIANT-S2 SYM/ASYM | Coupling shape. |
| `def-q1escn`, `def-69f472`, `def-1mpanl`, `def-kn0t01`, `def-b0nd01` | Names only. |
| `photon-ee-mapping.md` | Object 2. |
| Round-3 1:1 table `[branch:#1020]` | Epistemology signed; full 1:1 held until this close **and** Grant sign. |

---

## Classification (this document)

| Class | Why |
|---|---|
| **C — consistency / organizing** | DC short of a lossless inductor, capacitor-holds-DC, and A1 ⊥ T2 are already corpus. H1 is the **join refusal**: do not put a static \(\nabla V\) on Object 3 and call it gravity. |
| **Not D** | No new primitive, no engine run. |
| **Not a mint** | No `def-`, no `clm-`, no spoke row. |

---

## Grant sign line

**Signed 2026-08-30:** close stands; translate photoelastic to EE-native lattice terms (done above); commit/push this note; then write the S9 prereg on this branch. How to **model** the tank-state chart \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) and how it couples, or how bulk \(n,Z\), clocks, and gravity-as-differential emerge from the join that survives H1.
