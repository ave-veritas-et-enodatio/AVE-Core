[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Term-selection discipline for the loss/irreversibility vocabulary: which of two physically distinct moments a 'remanence / irreversible / plastic / latch / dissipates / frozen' word refers to — PRODUCT (persistence of a latched state, LOSSLESS per canon) vs TRANSITION (the crossing arrow, licensed only from counting). References existing axioms, canon leaves, the 2026-07-17 dissipation audit, and the remanence-R10 charter; originates no new physical claim and mints no clm-."
path-stable: "the canonical PRODUCT/TRANSITION discipline leaf; companion to substrate-native-terminology.md (the EE-native leak-check) and vocabulary-register.md (per-term def- adjudications) — this leaf carves the two loss-moments and gives the which-moment declaration rule"
-->

# Retention vs Transition — the PRODUCT / TRANSITION split

This is a **definitional / no-claim** leaf. It introduces no new physical result. It records a term-selection discipline: the corpus uses one vocabulary — *irreversible, remanence, plastic, latch, dissipates, frozen, erased* — for **two physically distinct moments**, and load-bearing prose must declare which one it means. Ratified as corpus discipline by Grant (in-chat, 2026-07-17); the evidence base is the Regime-IV dissipation audit `research/2026-07-17_regime-iv-dissipation-audit.md` (workflow `wf_3f83fc66-6f5`; 126 items). Companion to the [EE-native leak-check](substrate-native-terminology.md) (which scopes borrowed words by *regime*); this leaf carves them by *moment*.

## The split

- **PRODUCT — persistence of a latched state.** Does a state survive with the **drive off**? A winding integer, the charge on a `$\Gamma=-1$` cavity, a retained order parameter. Under canon this is **LOSSLESS** and needs **no maintenance resistor** — it is a *consistency-class* read of the wall, never an emergence chord.
- **TRANSITION — irreversibility of the crossing.** Is the *act of crossing* the threshold arrow-of-time-bearing? An arrow here is **licensed only from counting** (below) — **never** from a valve/diode/`Re(Z)` friction.

The two are independent questions. A state can persist losslessly (PRODUCT lossless) even if its *formation* crossing carried an arrow (TRANSITION), and vice versa. Conflating them is the failure mode the split names.

## The two-reason trap — both latches are lossless

The electron is held by **two independent reasons**, and neither is a dissipation:

- **Charge is latched by topology.** "Two-reason trap: topological (the loop cannot untangle) + impedance — both independently prevent decay" (`electron-identification.md:97`). The topological reason is the `$(2,3)$` phase-space winding integer / the `$0_1$` unknot — a conserved *label*, not an energy that leaks.
- **Mass is latched by the `$\Gamma=-1$` wall.** A `$\Gamma\to-1$` confined reactive mode on a lossless (Axiom-3) substrate "has **no loss channel** in the intrinsic (EM-port-CLOSED) eigenframe ... `Q\to\infty` ⇒ infinite lifetime ⇒ **the electron PERSISTS in an ideal vacuum**" (`resonant-lc-solitons.md:104`); this "**partly follows from the lossless axiom itself**" (`:108`). The `$A_1$` dilatation-mass "3" and the `$T_2$` winding "3" are **orthogonal** (`master-equation.md:20`) — two objects, two latches, both lossless.

So the PRODUCT moment for the electron is doubly lossless: topology holds the charge, the reactive wall holds the mass, and **neither requires a resistor to maintain**.

## The crossing-arrow license — counting only, never a valve

An arrow at the TRANSITION moment is admissible **only** from counting:

- **mode-spreading** with reconvergence ≈ 0 — "energy dispersed across many incommensurate `$\omega_m$` with no return path on relevant timescales ... NOT a smuggled friction" (`research/2026-07-16_f6-bath-meter_CHARTER.md:57`); or
- **the energy-conserving click** — the X40 ring-closure transient (`research/2026-07-10_x40-ring-closure-transient_result.md`).

Tier-1 canon states the prohibition flat: "the arrow comes from **mode-count or a click, never a valve**" (`research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md:256`). Inserting a `Re(Z)` / diode / rectifier to *manufacture* the arrow is the forbidden move.

## MODE-vs-SYSTEM loss — the generalization (Op3 worked example)

The subtle trap the audit surfaced: **loss from a MODE ≠ loss from the SYSTEM.**

- **LOSS-FROM-A-MODE** — energy redistributed *across modes* (an arrow by counting). The mode empties; the system conserves power.
- **LOSS-FROM-THE-SYSTEM** — a genuine `Re(Z)` sink; total energy actually decreases.

**Worked example — Op3.** The KB leaf reads Op3 as a system-loss: "`$A_1$` **loses energy monotonically**" / "dissipates energy **asymmetrically**" (`k4-port-irrep-decomposition.md:28,:109`). But the **code** that implements Op3 is unitary: "Unitary: `V_inc_A[k] = Γ * V_ref_A[k] + T * V_ref_B[k]` ... `T = sqrt(1 - Γ²)` ... **Conserves total power**" (`src/ave/core/k4_tlm.py:396-398`). A lossless reactive scatter (`$|\Gamma|^2+|T|^2=1$`) cannot dissipate. The **candidate resolution** (routed, pending the operator-physics adjudication) is **common-mode rejection**: `$A_1$` (the common mode) destructively interferes with neighbours and empties *its mode*, while the **system** conserves power — which would make it LOSS-FROM-A-MODE, not from the system. The code's unitarity is verified fact; which reading of the *leaf wording* wins is the routed question. (This item is FLAGGED on the leaf itself, routed to the operator-physics lane; see the audit §F4 and `k4-port-irrep-decomposition.md` bottom flag.)

> **🟢 RULED (2026-07-19, Grant in-chat — the candidate resolution above is PROMOTED to RULED; the "candidate/routed" wording is preserved unedited above per Rule-12).** Grant ruled the Op3 worked example (verbatim, normalized: "*mode loss should jot equal system loss, its trasnduction right?*" [sic]; docket RULING 21, `_orchestration/2026-07-10_rulings-docket.md`): Op3's $A_1$ behaviour is **LOSSLESS TRANSDUCTION** — the common-mode-rejection / **LOSS-FROM-A-MODE** reading is the ruled one, **not** LOSS-FROM-THE-SYSTEM. **Mode-projection loss ≠ system loss.** The code receipt stands (`src/ave/core/k4_tlm.py:396-398`, unitary, "Conserves total power"); the `k4-port-irrep-decomposition.md` bottom flag now carries a dated RESOLUTION addendum and its `:28`/`:111`/`:113` prose is corrected to transduction wording (the §4 sentences moved from the pre-insertion `:109`/`:111` down to `:111`/`:113` under the RULING-21 D1 block; the preserved worked-example body at line 45 above still cites the pre-insertion `:109` and is left unedited per Rule-12). This is the canonical worked example of the **MODE-loss** row in the §"Regime scoping" table below (`requires_R = no`, the system conserves).

## The application rule

> **Any load-bearing use of *remanence / irreversible / plastic / latch / dissipates / frozen / erased* must declare WHICH moment it refers to: PRODUCT (product-persistence) or TRANSITION (transition-arrow).** If PRODUCT, the default reading is **lossless** — do not attach a maintenance resistor. If TRANSITION, the arrow must be sourced from **counting** (mode-spread / click), not a valve. If a mode-decay is invoked, declare whether it is **loss-from-a-mode** (redistribution, Ax3-legal) or **loss-from-the-system** (needs a genuine `Re(Z)`).

## Regime scoping

| moment | regime where it is clean | licensed source | `requires_R`? |
|---|---|---|---|
| **PRODUCT** (persistence) | any regime, drive-off | topology (winding integer) or the `$\Gamma=-1$` reactive wall | **no** (lossless per Ax3) |
| **TRANSITION** (crossing arrow) | at/across the yield threshold | mode-spread (reconvergence ≈ 0) or the energy-conserving click | **no valve**; counting only |
| **MODE-loss** (redistribution) | sub-yield reactive, multi-port | destructive interference / common-mode rejection | **no** (system conserves) |
| **SYSTEM-loss** (genuine sink) | matched radiative/detector PORT | `$R_{rad}\equiv Z_0$` or `$Z_{det}$` (a real port) | **port-only** (Ax3-legal) |
| **near-yield loop** (contested) | at/above-yield crossing | the OPEN yield fork — substrate decides | **fork-gated** (see below) |

The last row is the **open yield-fork** (finite-area memristive loop vs zero-area saturating reactance): Grant leans reversible; the fork stays OPEN; resolution is by the registered discriminators (audit §5). Do not bank it either way in load-bearing prose.

## Cross-references

- The EE-native leak-check (regime-scoped word selection): [`substrate-native-terminology.md`](substrate-native-terminology.md).
- Per-term `def-` adjudications: [`vocabulary-register.md`](vocabulary-register.md).
- The evidence base (126-item audit + fork record): `research/2026-07-17_regime-iv-dissipation-audit.md`.
- The split precedent ("the retained order parameter, not the crossing loss, is what must survive drive-off"): `research/2026-07-12_remanence-r10-fixed-n_CHARTER.md:108`.
- The engine-incapability context (retention = the open R10 remanence gap; every attempt so far is an IMPOSED-LATCH): [`engine-capability-map.md`](engine-capability-map.md) §3.3 (Anhysteretic ↮ loop).
