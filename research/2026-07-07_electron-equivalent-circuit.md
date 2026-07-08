# Electron Equivalent Circuit — Frozen Model Definition (round-2b lock test)

**Date:** 2026-07-07
**Arc:** `analysis/electron-equivalent-circuit`
**Nature:** **DESIGN ARTIFACT / HYPOTHESIS-CLASS.** This is the *frozen model
definition* — the equivalent circuit that round-2b ("B") **will** simulate — in
the Vol 9 device-datasheet register. It is **NOT a run and NOT a result.** Every
statement is of the form *"the circuit B will simulate is X"* or *"the design
rationale for element Y is Z"* — never *"the electron is this circuit"* and never
*"X was measured."* Nothing here has been run except the base-tank
well-formedness sanity check (§8). It comes back to Grant for review **before any
2b simulation.**

**Predecessor context.** This artifact formalizes the topology walked in the
electron-lock design-rationale note (`research/2026-07-07_electron-lock_design-note.md`,
PR #568, DO-NOT-MERGE). The topology is **FROZEN from that Grant-walk**; this
document formalizes it into a component table, a physical-mapping table, and a
SPICE netlist. It does **not** redesign the physics. The Stage-1 minimal result
(`electron-lock-stage1`, verdict **[DOMINATED]** — bare two-oscillator dynamics
prefers a 1:1 lock, so (2,3)-selection is *topological*, not bare-dynamical) is
the load-bearing input that shapes the flags in §9.

---

## FIREWALL (mechanical exclusion — load-bearing)

<!-- FIREWALL SECTION -->

## §0 — Canon anchors (verified verbatim, two-method)

<!-- CANON ANCHORS SECTION -->

## §1 — The equivalent circuit (ASCII schematic)

<!-- SCHEMATIC SECTION -->

## §2 — Component table

<!-- COMPONENT TABLE SECTION -->

## §3 — Physical-mapping table (circuit element ↔ physics)

<!-- MAPPING TABLE SECTION -->

## §4 — The parametric-coupling element (MODELING FORK — flag for Grant)

<!-- FORK SECTION -->

## §5 — The Γ=−1 confinement wall

<!-- WALL SECTION -->

## §6 — Homonym guard + sector discipline

<!-- HOMONYM SECTION -->

## §7 — The netlist

<!-- NETLIST SECTION -->

## §8 — Sanity check (base-tank resonance + well-formedness ONLY)

<!-- SANITY SECTION -->

## §9 — Flags for Grant (three)

<!-- FLAGS SECTION -->

---

**Closing register reminder.** Nothing above is a result. This is the frozen
model definition — the circuit B *will* simulate — plus a base-tank
well-formedness sanity check. The (2,3)-selection and ⟨N⟩ outputs the eventual
2b run must produce are firewalled per the §FIREWALL: topological / dynamical /
scale-invariant, never tuned to m_e, and α / Q=1/α excluded from any selection
claim. This artifact lands *model definition only.*
