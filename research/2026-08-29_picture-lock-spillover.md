# Spillover from the serial PR picture-lock (not #1020 rewrite)

**Purpose.** Walks and efforts that surface during the #1020…#1033 picture-lock but are **outside that PR’s rewrite scope**. Do not mix these into the #1020 walk record.

**Status: LANDED 2026-08-29** on `research/2026-08-26-overbraced-crystal-walk` (PR #1020). Working-pad copy remains gitignored at `.agents/handoffs/2026-08-29_picture-lock-spillover.md`.

**#1020 picture-lock stays** [`2026-08-29_overbraced-crystal-picture-lock.md`](2026-08-29_overbraced-crystal-picture-lock.md) (P0–P7 + mapping + ordinary flags + the 1:1 table). This file is everything that is **not** that PR’s rewrite.

---

## Grant status (2026-08-29)

- Mapping **makes sense** (epistemology).
- **Agrees** with the Kirchhoff reading below and with the audit holds: sign “AC reads a DC differential on a real medium”; **do not** sign “same scalar Kirchhoff mesh” or “\(\varepsilon_{11}\) is \(V\) on the \(L\)-edges.”
- Kirchhoff leaf **not edited** this session. Wording PR is S1, parked.
- P0 **SIGNED for #1020**; leftovers (2)(3) are spillover S11. P1/P2 sentence **SIGNED**. P3 **SIGNED** (dead as stated; no same-setup rerun). P5 instrument limit **SIGNED**. P6 **CLOSED for #1020** (S10). P7: analyze, do not pick — **CLOSED for #1020**; analysis is S10.

---

## Open spillover items

| ID | Item | Status | Home |
|---|---|---|---|
| S1 | Kirchhoff-method leaf: TKI pairing labels on \(V,I\) (equations stay) | PARKED — wording PR, not #1020. Grant agreed this is names, not Faraday/electrostatic mix-up. | [`2026-08-29-kirchhoff-pairing-labels`](../_orchestration/open-items/2026-08-29-kirchhoff-pairing-labels.md) |
| S2 | AC/DC gravity 1:1 as Kirchhoff/.OP/.AC | Epistemology signed (Grant). Full 1:1 **held** on H1–H6. | [`2026-08-29-acdc-gravity-circuit-map`](../_orchestration/open-items/2026-08-29-acdc-gravity-circuit-map.md); 1:1 table lives on the **picture-lock** Round 3 |
| S3 | Vocab lens: synonym vs new `def-` (theorem-thesaurus + register) | plan delta; not a #1020 rewrite | plan |
| S4 | SM/QED/GR leakage CI (warn vs fail) | Grant-gated epic | plan |
| S5 | over-braced `def-` (and self-stress / hyperstatic / knot vs `def-kn0t01`) | **Parked for later adjudication.** Collision list below. Not minted on #1020. | this file |
| S8 | P5 bench fact: scalar HB cannot hold Cosserat twist | **SIGNED** as instrument limit. “Therefore no knot” killed. Cosserat-wired HB later. | this file |
| S9 | Phase-space tank-state: `def-69f472` amend + coupling/bulk-emergence characterization | Sentence SIGNED. Vocab not minted. Derivation **not started** (prereg first). Gated on H1. | [`2026-08-29-phase-space-tank-state`](../_orchestration/open-items/2026-08-29-phase-space-tank-state.md) |
| S10 | Dual-arm analysis: \(\ker Y\) vs \(M\)-eigenmode (P6/P7) | **Closed as #1020 follow-up.** Analyze, do not pick. Drop Maxwell–Calladine weld. Not this HB code. | [`2026-08-29-ker-y-vs-m-eigenmode`](../_orchestration/open-items/2026-08-29-ker-y-vs-m-eigenmode.md) |
| S6 | Dielectric-Lagrangian “capacitive **edges** / inductive **nodes**” vs Kirchhoff nodes=\(C\), struts=\(L\) | not yet walked | this file |
| S11 | P0 leftovers: extra KVL loops vs A1 headroom; BH-host unsigned | PARKED — not #1020. Do not pick in the rewrite. | this file |
| S13 | #1020 Lens-4 ordinary flags | Walked 2026-08-29. Rewrite-BLOCKER: §9.1 keeps §2 live. FLAG: BOARD 0-PRs, chk3.py missing, EXTERNAL teaching, vocab:510 as CANON on a PROPOSED node. | picture-lock Lens 4 |

---

## S1 — Kirchhoff leaf (agreed)

**File:** [`kirchhoff-network-method.md`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md) (`clm-q39qct`).

**The leapfrog is ordinary LC, not a voltage mix-up.**

- \(I \leftarrow I + (\Delta t/L)(V_A-V_B)\) is Faraday: the voltage **across** the strut **is** \(L\,\mathrm{d}I/\mathrm{d}t\).
- \(V \leftarrow V + (\Delta t/C)\sum I\) is the capacitor at the node.

\(V_A-V_B\) is one KVL quantity: inductor voltage **and** the difference of the two capacitor voltages. They are coupled; that coupling *is* the circuit. This is **not** “induced voltage pretending to be a second electrostatic voltage.”

**What is wrong is the mechanical names.** Strut \(I\) is called “inductive flux **or lattice strain**”; node \(V\) is “voltage **or displacement**”; the Faraday step is titled “Edge Strain Update.” TKI (`def-1mpanl`) pins \(I\) = velocity, \(V\) = stress, \(Q\) = displacement. The leaf uses both analogies in the parentheticals.

**Fix shape:** wording PR. Keep the equations. Relabel parentheticals + the “Edge Strain Update” title. Rule 12 on `clm-q39qct` body (it repeats “edge-strain”). Not #1020.

**S6 (sister, unwalked):** `dielectric-lagrangian.md` stores energy in capacitive **edges** and inductive **nodes** — opposite \(C\)/\(L\) placement from this leaf.

---

## S2 — What is signed vs held

**Signed (Grant):** from inside this medium, you read DC only as an AC difference. Uniform DC can exist as medium state and remain unread. Gravity-as-interaction is a **differential** of that DC, read by AC probes.

**Not signed (holds):**

- **H1 (load-bearing).** Lossless series-\(L\) / shunt-\(C\) mesh is **equipotential at DC** (inductors short). A static \(\nabla V\) cannot live on those \(L\)-edges. DC prestress lives on A1 **bond-compliance** capacitors \(C_{\mathrm{eff}}=C_0/S\), which can hold DC voltage at zero current. Light is T2 on the TLs. “Same mesh as the Kirchhoff leaf” overclaims. Coupling is photoelastic (A1 grades T2 constitutives), not one voltage on one capacitor.
- **H2.** `clm-acdc07` “gravity \(= S(A)\)” vs Op19 linear-in-\(\varepsilon_{11}\) (Regime I kernel frozen, \(\Delta S\sim 10^{-10}\)). Two constitutive slots. Solar gravity is the Op19 slot, not the kernel Taylor series.
- **H3.** Light is T2 \(V_{\mathrm{inc}},V_{\mathrm{ref}}\), not the A1 varactor’s own .AC.
- **H4.** Matter has a **DC A1 store** at \(A=\sqrt{\alpha}\) plus a T2 winding. Gravity couples to the store. “Matter is AC” undersells mass.
- **H5.** \(\varepsilon_{11}\) as A1 Q-point is #1033 WALK-GRADE, not TKI-forced (stress vs strain).
- **H6.** A lossless TL needs no DC bias. P0 over-brace is varactor **headroom** (stay on the reactive arc), not generic line theory.

**Not minted** into `translation-circuit.md`. Full 1:1 table remains on the picture-lock until H1 is closed.

**P1 — signed.** Lattice is space; knot is tank-state winding; projected strain is AC readout.

---

## S5 — over-braced `def-` (parked; Grant 2026-08-29: track for later)

Do **not** mint on #1020. Collision senses to adjudicate later (KEEP-ALL until one is picked):

1. Trampoline / couple-stress \(\sigma^A\) — handed twist-lacing, inductive (`trampoline-analogy-primer`).
2. Vol 3 graph — “amorphous, over-braced” substrate graph.
3. Maxwell–Calladine extra-constraint count (driver is de-canonized diamond; live micropolar is isostatic).
4. Geometric lever (`LEVER_OVERBRACE` in code).
5. Pre-compressed strut (rest length past Euler).
6. Grant P0 — prestress / headroom so projected strain stays lossless (H6: varactor reactive arc, not TL bias).

Also parked here: **self-stress** (MC kernel vs writhe self-subtraction vs walk “knot = self-stress”); **hyperstatic** (gloss, 0 hits on main — do not mint unless Grant wants the civil name); **knot** vs SOLID `def-kn0t01` (phase-space portrait vs P1 projected-strain object).

---

## S11 — P0 leftovers (Grant 2026-08-29: spillover, not #1020)

**(2) Prestress as A1 compliance voltage vs extra KVL loops.** Two candidate circuit objects for “over-brace.” H1 already holds: DC does not live on the Kirchhoff \(L\)-edges. Adjudicate with S5 (senses 1 vs 6) later. Do not pick in the #1020 rewrite; the rewrite may name both as open, not as a signed identity.

**(3) BH-host / impedance-bubble.** Cosmology-scale **unsigned intuition**, not ontology. Keep unsigned. Do not mint. Do not put it in the walk as a mechanism.

---

## P2 note — Smith vs phase space (SIGNED sentence; vocab not minted)

Canon (`def-69f472`): phase space = \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) / Clifford-torus **phasor coordinates**, not real space.

**Grant-signed sentence (2026-08-29):** Phase space is the native **state-coordinate chart of the lattice tanks**, distinct from the graph that is physical space. Smith is a **ratio chart** of that state, not the state itself.

Amend `def-69f472` on a vocab PR (not #1020, not #1033). Keep the A46 size-leak flag. Do not mint a second `def-`. Fiber-bundle noun stays WALK (`translation-phase-space.md` §3.2). Smith-as-ontology stays Grant-gated.

Smith chart is a **ratio**: \(\Gamma = V_{\mathrm{ref}}/V_{\mathrm{inc}}\) (rung T4). Overall amplitude and common phase drop out. “All quadrants” is closer to the **I/Q plane** than to the passive Smith disk.

---

## S8 — P5 (SIGNED)

1. **Signed:** the #1020 HB code is stretch/A1-only; Cosserat \(\gamma_c\) (flywheel mutual-\(L\)) is unwired. That code cannot hold a twist.
2. Do **not** promote “therefore the knot cannot exist.”
3. On a later #1020 wording pass: remaining live content is Grant’s spiderweb/over-brace metaphor, not an HB selector (P4 killed Chern).
4. A Cosserat-wired HB is a **new effort**, not this PR.

---

## S9 — model the tank-state chart and its couplings (Grant: next theory step)

**Do not derive this session.** Prereg before any characterization.

**Signed target:** how the tank-state chart is modeled, and how it couples to the vacuum and to matter / light / gravity — or how bulk properties emerge from it.

**Already on the shelf (do not re-derive as new):** `translation-phase-space.md` ladder T0–T5; `clm-acdc07`; Round-3 1:1 table; H1–H6; photon-ee-mapping; `bond-lc-constitutive-grading.md`; INVARIANT-S2 SYM/ASYM.

**The actual gap:** the **join that survives H1** — A1 Q-point grades T2 constitutives (photoelastic), not one voltage on one capacitor; bulk \(n\), \(Z\), clocks, gravity-as-differential from that split.

---

## S10 — P6/P7 follow-up (analyze, do not pick)

1. Drop Maxwell–Calladine as the knot’s identity. Do not mint.
2. Analyze **both** arms: (i) \(\ker Y\) DC loop current; (ii) \(M\)-eigenmode at \(\theta\).
3. Clause Q is a lens on the DC arm, not a verdict. Never “ground.”
4. Split the \(\omega\) glyph before any compute.
5. This HB code is the wrong instrument for either arm as a Cosserat object (S8).
6. Self-stress `def-` stays in S5.

---

## Round log

- **2026-08-29 open:** tracker distinct from the per-PR picture-lock. Kirchhoff leaf not edited. Mapping not minted into the spoke.
- **2026-08-29 later:** Grant: park over-braced `def-` for later (S5 list). P4 agreed killed. P5 plan = S8. P2 Smith/quadrants recorded unsigned, not a P1 close.
- **2026-08-29 P1←P2:** proposed close — lattice is space; phase space is tank-state coordinates. P3: stretch-only ≠ voltage synonym; HB \(A\) sweep ≠ SYM \(L{+}C\). P7: Q2 restatable, not a compute green light.
- **2026-08-29 ordinary flags:** Lens 4 walked. Rewrite-BLOCKER is §9.1 “§2 not wrong.” BOARD.md 0-PRs FLAG.
- **2026-08-29 pads landed:** tracked copies on PR #1020. `BOARD.md` not regenerated (Lens 4 FLAG).
