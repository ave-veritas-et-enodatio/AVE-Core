# Engine re-route session trace + handoff (2026-06-24)

**Purpose:** a cohesive, traceable record of every redirection, result, and decision in the engine-reroute arc, plus the clear forward path. Read this to reconstruct the arc without replaying the transcript.
**Scope-lock:** all engine stages here are **CONSISTENCY-class** (mechanism / existence), NOT the α-free chord. The chord lives at the **bench** (forward predictions). `mass=A1 (PR#260)` is UNTOUCHED throughout; `Q=137` slot stays EMPTY.
**Discipline used throughout:** ground (scoping workflow) → Grant rules the forks → freeze pre-reg (SHA-pinned) → build + 3 refute-by-default auditors → synth → branch-only PR (Grant merges, never self-merge).

---

## 1. Trace table (the spine — stage → workflow → PR → verdict)

| Stage | Question | Scoping wf | Build wf | PR | Verdict |
|---|---|---|---|---|---|
| L0 | α-clean winding host | — | — | #405 ✅merged | CLEARED |
| **S1** | is the (2,3) winding a **separately-conserved DOF**? | `w8850pne0` | `waw44a1os` | #407 ✅merged | **PASS-WITH-FLAGS** (A1-sustains-rotation: asserted→derived; real-space ω, single-knot) |
| **S2** | does `H_couple` lock A1↔ω **conservatively, ω independent**? | `wfuwvaiev` | `wxmlb0q0k` | #409 ✅merged | **PASS-WITH-FLAGS** (forks: saturation-front intra-mechanical / splitting-OK; 2-mode-per-node model, NOT full PDE — flagged for S3) |
| **S3** | does winding+H_couple **PIN** the dispersing A1 core? | `wd0gg25yw` | `wpc5ip174` | #411 ⏳pending-merge | 🔴 **DISPERSE-FALSIFIED** (energy-certified, robust; the re-route's central mechanism is wrong) |
| **coupled eigensolve** | does the confined **coupled (mass+charge) eigenmode EXIST** + the V_yield/V_snap/m_e ladder | (emergence scoping `wue1k3pnb` served) | `w4v6abhxs` ⏳in-flight | (stacks on #411) | pending |
| docs: synthesis | electron-as-vacuum-state + figure | — | — | #408 ✅merged | — |
| docs: fwd-pred register + OA node | derived-vs-echo map + `clm-fofwr1` | — | `wue7w950l` | #410 ✅merged | — |
| docs: corpus hygiene | OA Phase-1 staleness + √α overclaim | — | — | #406 ✅merged | — |
| genesis/α bet | overshoot-rebound-lock + α-in-rupture-ratio | — | `wkp3xtzed` | (4th-echo, log owed) | 🔴 **REFUTED** (m_e-routed = construction; re-discovers √α; direction-inverted; re-opens falsified pump) |
| (B) emergence lane | eigenmode-existence as a free-scale sweep | `wue1k3pnb` | — | — | mostly-already-answered (fork-b); **PARKED** |

---

## 2. The redirections (what pivoted, and why)

1. **The re-route itself** (pre-session): Stage-2 falsified the bulk self-trap (A1-alone disperses on the native stencil; the Cartesian self-trap was a grid artifact). Localization re-routed to **boundary/topological**: the hypothesis that the **(2,3) winding + H_couple pins the dispersing A1 core**.
2. **S1→S2→S3 built that hypothesis up**, then **S3 falsified it**: the winding+coupling does NOT pin the mass. Energy-certified, robust, holds under 3 audits.
3. **S3 port-loading review (Grant-prompted) corrected an over-reach of mine:** I'd concluded "engine exhausted internally." Wrong — that conflated two things. The port analysis showed S3 only loaded the *conservative coupling* port; it never loaded the *confining* port (Γ=−1 reflection). And `fork-b` (2026-06-20) already shows a confined A1 eigenmode EXISTS. So: **the localizer is the cavity-eigenmode, NOT the winding** (the re-route mis-attributed localization to the winding). Localization is *identified*, not exhausted; what's twice-falsified is *dynamical self-formation from a seed* (Stage-2 + S3 — needs the cast, leans-falsified).
4. **The genesis/α bet** (Grant's overshoot→rebound→lock + α-in-the-rupture-ratio) was refuted as a 4th echo: the rupture threshold is m_e-routed (a construction, the α-circularity guard), it re-discovers the existing `V_yield=√α·V_snap`, it's direction-inverted vs the corpus (V_snap IS the rupture ceiling, not just-under), and the mechanism re-opens the leans-falsified pump.
5. **The calibration posture crystallized** (Grant-driven): the electron is the *ruler* (V_snap≡m_e c²/e, ℓ_node≡ℏ/m_e c — asserted, not derived), so every dimensionful value is a **structural echo**; chord-homes = m_e-free dimensionless ratios (mostly closed-neg) + forms + forward predictions. The chord-test = **form before calibration** = *did the substrate FORM the constraint (emergence/chord) or did we DECIDE it (impose/consistency)?* Dimensional-analysis theorem: ≥1 scale always survives (you cannot remove the last one).
6. **Planck route RETRACTED** (Grant's correction): the Planck scale is an *untested dimensional-analysis number*, G-dependent (AVE's G is the fitted/MIXED `ξ_machian`). Anchoring m_e to it trades a *measured* scale for a *worse, unmeasured* one — not a door. Conclusion sharpened: **the electron is the best-grounded scale there is; m_e-irreducible is the floor, no better anchor exists.**
7. **The pivot to the bench**: the engine's internal routes are characterized; the AVE-distinct chord lives in **forward predictions** (the parity channel), arrived at by the engine exhausting its internal mechanism-hunt, not by assertion.
8. **The current jump** (Grant): build the **coupled eigensolve** — the clean conservative-existence step S3 left untested — to settle whether the confined coupled (mass+charge) eigenmode exists AND to make the V_yield/V_snap/m_e ladder physical ("an engine that works, where we both understand how V_yield/V_snap relate to m_e").

---

## 3. Established contexts (the honest engine-arc map)

- **exists as a confined lossless eigenmode** — YES, A1-only (`fork-b`, 2026-06-20, GATE1 PASS, core_frac=1.0, ARM-B non-tautology). The coupled (mass+charge) version is what the eigensolve (`w4v6abhxs`) is now settling.
- **charge = a conserved (2,3) topological winding** — YES (S1 #407).
- **the conservative A1↔ω coupling** — YES (S2 #409), but validated on a 2-mode-per-node model (NOT a full PDE).
- **winding localizes the mass** — NO (S3 #411). The **cavity-eigenmode** localizes; the winding is charge, it rides along.
- **dynamical self-formation from a seed** — NO ×2 (Stage-2 + S3). The bound mode exists but a lossless seed can't relax into it → needs the one-time **cast** (formation, leans-falsified).
- **the scale** — FREE; `m_e` is the irreducible input (overdetermined: scale-invariant kernel + ℓ_node circular; fork-b ω diverges with L). No better anchor (Planck retracted).
- **genesis/α as a value-derivation** — REFUTED (4th echo).

Master-equation note: the S3 coupled PDE = the **master wave equation A1-sector** (`∂²V/∂t² = (c₀²/S(A))·∇²V`) ⊕ the **Cosserat ω sector** ⊕ **H_couple**. The bare master equation governs the mass grade alone (it disperses); the coupled object is the electron.

---

## 4. The forward path (clear, prioritized)

**IN FLIGHT:** the coupled eigensolve (`w4v6abhxs`) — existence of the confined coupled eigenmode + the physical V_yield/V_snap/m_e ladder (A* = where the mode binds = FORM; the dimensionful values = m_e-calibration; the two-camps resolution; the scale-free check). Honest priors: existence likely (fork-b found the A1 mode); scale-free expected (= m_e irreducible, honest closure, NOT a derivation of m_e).

**PENDING MERGE (Grant):** #411 (S3 DISPERSE); then the eigensolve PR (stacks on #411).

**THE PIVOT — the next REAL effort:** the engine's internal mechanism-hunt is essentially complete (existence yes, localizer=cavity, charge=winding, scale free, winding-pinning falsified). The AVE-distinct **chord is at the BENCH** — a bankable **forward prediction** in the **parity channel** (the cleanest zero-vs-nonzero divergence from QED): the field-free **optical-activity sign-flip** (`clm-fofwr1`) and/or the **co-vs-anti-handed |F| ratio** (unbuilt), and the **E-route birefringence** coefficient. Eventual experimental path = the **cRIO bench** (the C_eff(V) saturation-onset discriminator). Scope this the same way (ground→freeze→build) when Grant directs.

**OWED (one hygiene PR):** the **calibration-posture doc** (decide-vs-allow-to-form + form-before-calibration chord-test + irreducible-scale theorem, Planck-route-retracted) + the **genesis/α 4th-echo log** (against the standing α-register, NOT refilling the keystone-pump slot).

**PARKED (do not re-open without a specific new idea):** the **G/Planck scale route** (retracted — untested, G-fitted); the **(B) emergence dynamical-formation** (twice-falsified, needs the cast); the **z₀-from-K4** geometric scale route (closed-negative, z_eff→6).

---

## 5. Standing constraints (carried)

main PROTECTED / NEVER self-merge (Grant merges); fresh /tmp worktrees off origin/main; NO "build" in branch names; α-canonical-source (no ALPHA on a chord path); Q=137 slot EMPTY (gate `wmighcz1z`); spin-½ ≠ (2,3) (coordinate-category); genesis-24 guard (ω its own DOF, never ω:=grad(V)); chord = dimensionless-ratio / form / forward-prediction, NEVER a calibrated value; refute-by-default + symmetric-standard (hold AVE and SM to the same bar).
