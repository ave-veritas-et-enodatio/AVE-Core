# Crystal-Graft v4 — the photon's helicity IS the winding? (RESULT)

**Date:** 2026-06-10 · **Branch:** `analysis/2026-06-10-graft-v4-photon-helicity` · **Lane:** implementer
**Prereg (FROZEN):** [`2026-06-10_graft-v4-photon-helicity_prereg.md`](2026-06-10_graft-v4-photon-helicity_prereg.md)
**Engine:** [`src/ave/core/crystal_graft_v4.py`](../src/ave/core/crystal_graft_v4.py) ·
**Driver:** [`src/scripts/vol_1_foundations/crystal_graft_v4_run.py`](../src/scripts/vol_1_foundations/crystal_graft_v4_run.py) ·
**CI gate (hardened):** [`src/tests/test_graft_v4_alpha_free.py`](../src/tests/test_graft_v4_alpha_free.py) ·
**Results:** `crystal_graft_v4_results.json` · N held FIXED at **72**; lock_eta **0.05**; n_steps **1200**.

## VERDICT — C (the conservation hypothesis is FALSIFIED; CHANGE 1's provenance LANDS; the lock saturates magnitude but a STOP gate fires)

> **Grant's twist question (recorded verbatim in the prereg §0): "is the poloidal '3' the photon's own
> conserved twist — confinement CONVERTS the photon's helicity into the winding?" The answer in this engine
> is NO.** The photon keeps **~100 %** of its helicity (RH residual `−291.2` of input `−291.4`); only **~2 %**
> ends up as the trapped winding (`H_bel = −6.0`). The photon's spin does NOT become the electron's spin here —
> it stays in the photon. This is a clean negative with a NAMED mechanism (§6, ave-conserved-vs-pumped): the
> conversion REQUIRES the photon to deplete into the winding, and the ONLY coupling that depletes is an
> INDEFINITE-Hamiltonian PUMP that detonates (the `deplete_RH` arm: `H_bel −4107`, `H_photon −13446`); the
> bounded coupling that is numerically stable does NOT transfer the conserved helicity (the photon is a
> non-depleting chiral director). **A false A was avoided** — and three real v3 repairs landed (below).

**What v4 DID land (genuine progress over v3's two fatal lenses):**
1. **CHANGE 1 χ-FROM-PHOTON kills the template — the v3 byte-identical failure is now IMPOSSIBLE.** The
   `no_photon` arm is null **BY PHYSICS** (`H_bel = +0.0`, `E_ω = 0`, winding `(0,0)`, reliability `(0,0)`) —
   it differs from signal by construction (the source literally contains `w`). The charge SIGN traces the
   photon helicity and FLIPS RH↔LH (`H_bel`: RH `−6.0` / LH `+6.0`), with **NO dialed χ anywhere**. The
   zero-helicity (linear) photon gives null winding + null charge (`H_bel −0.0`, `(0,0)`).
2. **CHANGE 2 the LOCK preserves a planted knot** (the v3-killer): a planted (2,3) at a resolvable scale
   survives 500+ live steps with source ON + lock ON, reading back **(2,3)** (v3 destroyed it → (2,1)).
3. **The resolution gate + the falsifiable independence gate both PASS** (v3's were VOID/unfalsifiable).

| Quantity | Result | Bar | Pass |
|---|---|---|---|
| SMOKE-1 LOCK preserves planted (2,3) | `(2,3)→(2,3)` is_2_3=True, source+lock ON, 600 steps | survives | ✅ |
| SMOKE-2 independence + POSITIVE control | real arm robust `(2,2)==(2,2)`; **SLAVED ω:=F(V) flagged False** `(0,0)≠(1,0)` | reachable-False PROVEN | ✅ |
| SMOKE-3 RESOLUTION gate | de-novo torus R=9.02 **r=3.61 cells**; plant-at-de-novo-scale reads **(2,3)** rel (0.75,0.93) | r≳3 + reads (2,3) | ✅ |
| **SMOKE-4 SATURATION (STOP gate)** | `\|L_ω\|` doubling ratio RH **5.03** / χ-null **3.97** / live-wall **5.19** (η-invariant; bounded but not flat) | ratio ≤ 1.3 | ❌ |
| **HELICITY LEDGER closes (RH)** | trapped **−2 %**, residual **−100 %**, radiated +2 % (photon keeps its helicity) | trapped ≈ input | ❌ |
| sign provenance traces photon + flips | `H_bel` RH `−6.0` / LH `+6.0`; sign-traces ✅ flips ✅ | flips with χ | ✅ |
| no-photon NULL BY PHYSICS | `H_bel +0.0`, `E_ω 0`, `(0,0)` rel `(0,0)` | null, differs from signal | ✅ |
| zero-helicity arm null winding+charge | `H_bel −0.0`, `(0,0)`; deposits `E_w=28.1` (=½ RH 56.3 — see §3) | null winding/charge | ✅ |
| de-novo (2,3) closes (w_pol≈3) | RH/LH `(4,0)`, **w_pol≡0** at resolved scale | (2,3) | ❌ |
| α-import CI (hardened: Import+attr+CODATA+driver+runtime) | 7 passed; ALPHA_COLD_INV/PHI/RR never in engine state | green | ✅ |

## §1 — The two physics changes AS BUILT (and the two findings that reshaped them)

**CHANGE 1 — χ-from-photon (the live photon `w` IS the buckle director).** A circularly-polarised photon is a
force-free Beltrami field (`∇×w=±k·w`, A∥B) — the SAME A∥B object v3 dialed, now PHYSICALLY the photon's. The
mechanism is verified: `ω∝∇×(gVw)∝∇×w`, then `∇×ω∝w`, so `H_bel=∫ω·(∇×ω)∝∫(∇×w)·w` = the photon's own helicity
density. **FINDING 1 (frozen in prereg §1.1):** the full trilinear coupling (with the `f_w` photon-depletion
back-reaction) conserves the continuum energy but is an INDEFINITE Hamiltonian — it DETONATES (the `deplete_RH`
arm: `H_bel −4107`, `H_photon −13446`, `max|ω| 1.06` vs the stable arm's `0.05`). So the operative engine drops
`f_w` (`photon_deplete=False`): the photon is a BOUNDED chiral director. This is the crux of the C — see §6.

**CHANGE 2 — the LOCK.** **FINDING 2 (the load-bearing v4 lesson):** the literal Woltjer flow
`∂_tω=η(λ∇×ω−∇×∇×ω)` DETONATES in central-difference discretisation (curl-of-curl Nyquist null space —
`H_bel 9.5→4.9e5` in 300 steps); and a plain velocity damp drives `π_ω→0` and **KILLS the LC quadrature that
IS the poloidal winding** (verified planted (2,3)→(2,1) collapse). The poloidal "3" lives in the LOCAL `(ω,π_ω)`
LC reactance; the runaway is a GLOBAL rigid rotation — SEPARABLE. The lock therefore removes only the rigid-body
rotation `π_ω ← π_ω − η·(Ω×r)` (`Ω=I⁻¹L_ω`), contracting `L_ω←(1−η)L_ω` while leaving the local LC quadrature
intact. This **preserves the planted knot** (SMOKE-1 ✅).

## §2 — The HEADLINE: the helicity ledger does NOT close (the conservation hypothesis is falsified)

| arm | `H_photon(0)` | `H_bel` trapped | `H_photon` residual | radiated (deficit) | trapped/input |
|---|---|---|---|---|---|
| RH (photon hel +1) | `−291.4` | `−6.0` | `−291.2` | `+5.8` | **−2 %** |
| LH (photon hel −1) | `+291.4` | `+6.0` | `+291.2` | `−5.8` | **+2 %** |
| ZERO (linear) | `+0.0` | `−0.0` | `+0.0` | `0` | — |
| no_photon | `+0.0` | `+0.0` | `+0.0` | `0` | — |

The TOTAL helicity ledger BALANCES (radiated ≈ 2 %, i.e. `input ≈ trapped + residual`), but the photon's
helicity does **NOT survive as the winding**: the residual is **~100 %** (the photon keeps its helicity) and
only **~2 %** is trapped. "The electron's spin IS the photon's spin, trapped" is FALSE in this engine — the
photon's spin stays the photon's. Per the frozen bins (prereg §4) this is **C** ("trapped H_bel ≁ photon's").

## §3 — What CHANGE 1 landed (the v3 fatal-lens repair — real, clean, reportable)

- **no-photon null BY PHYSICS** (the v3 demotion's FATAL lens 1, eliminated). v3's `no_photon` arm was
  byte-for-byte identical to signal (χ was a source input). v4's source IS the photon `w`, so no-photon ⇒
  `w=0 ⇒ f_ω≡0 ⇒ ω=0`: `H_bel +0.0`, `E_ω 0`, winding `(0,0)`, reliability `(0,0)`. **Truly null, by physics.**
- **sign provenance + flip:** `H_bel` RH `−6.0`, LH `+6.0` — sign traces the photon helicity and flips RH↔LH.
  No dialed χ exists in the engine (hardened α/dial CI). This is **charge=helicity-SIGN carried FROM the photon**
  (v3 only carried it from an imposed template).
- **zero-helicity (linear-pol) control:** null winding `(0,0)` + null charge `H_bel −0.0` while the photon is
  present. **Honest caveat (`zero_energy_comparable=False`):** the linear photon deposits `E_w=28.1` = **exactly
  ½** the circular photon's `56.3` at equal amplitude (one transverse component vs two) — so "comparable energy"
  fails my ±30 % quantifier by construction, NOT because the linear photon is inert. The physics holds (energy
  present, helicity zero ⇒ no winding/charge); the quantifier is a polarisation-energy convention.

## §4 — The lock saturates |L_ω| MAGNITUDE but the doubling-RATIO STOP gate fires

`|L_ω|` is BOUNDED and SMALL (RH `2.09`; at stronger η it shrinks to `0.14`) — there is NO v3-style unbounded
`t^0.43` pump. But the **doubling-ratio gate FAILS**: RH `5.03`, χ-null `3.97`, live-wall `5.19`, lock-OFF `3.69`
(all ≫ 1.3). **The ratio is η-INVARIANT** (5.27→5.48→5.60→5.65 as η 0.1→0.5): the rigid-rotation lock rescales
the `|L_ω|` magnitude (∝1/η) but the 4L/L ratio is set by a LATE-TIME transient `|L_ω|` excursion (the photon's
wall-interaction timescale), which is NOT a steady rigid rotation the lock can null. Per Rule 11 I did NOT move
the frozen tolerance to convert ❌→✅; the gate fires, and (with the ledger non-closure) caps the verdict at C.
*(η=0.05 was frozen on a pre-final config; re-tuning was tested and does NOT change the ratio — kept frozen.)*

## §5 — De-novo (2,3): the poloidal "3" still does not self-assemble (w_pol ≡ 0)

At the RESOLVED de-novo scale (R=9.02, r=3.61 cells — resolution gate ✅, so this is NOT the v3 unresolvable
artifact) the photon-sourced ω reads `(w_tor, w_pol) = (4, 0)` (RH and LH). `w_tor=4` is the ABC/photon spatial
frequency on the major contour (a real winding of the deposited ω, not a topological toroidal-2); **`w_pol≡0`**
— no poloidal fibre. Same residual as v3, now confirmed at a RESOLVABLE scale (the v3 read was VOID below the
resolution floor). The poloidal "3" does not geometry-select from a photon-director source.

## §6 — The named mechanism (ave-conserved-vs-pumped, topology edition) — WHY it is C

The conservation-genesis Grant adjudicated REQUIRES the photon to DEPLETE its helicity 1:1 into the winding
(energize + lock a conserved invariant). In this elastodynamic substrate that depletion is the back-reaction
`f_w=−κ̃gV(∇×ω)`. But the full trilinear coupling `H=κ̃∫gV[w·(∇×ω)]` is linear in each of `V,w,ω` ⇒ **INDEFINITE
(unbounded below)** ⇒ the discrete dynamics PUMP and DETONATE (the `deplete_RH` arm). The lock cannot arrest an
indefinite-Hamiltonian runaway. The ONLY stable rendering drops `f_w` — and then the photon is a **non-depleting
chiral director**: it imprints a small chiral ω (`H_bel −6`, sign-traced) but transfers ~none of its `−291`
helicity. **So: the coupling that would CONSERVE-AND-TRANSFER the helicity is a pump; the coupling that is a
stable lock does not transfer it.** A bounded, depleting, helicity-conserving photon→winding conversion is NOT
realized by this director-buckle family. That is the localized residual — and the honest C.

## §7 — Gates / controls (all green except the two that define the C)

- **POSITIVE CONTROL (the v3 auto-VOID fix):** the SLAVED arm `ω:=∇V`-family is FLAGGED False by the SAME
  independence gate (`(0,0)` ref vs `(1,0)` pert — winding not robust ⇒ gate returns False). Reachable-False
  PROVEN; the gate is falsifiable (v3's could not fail).
- **JSON hygiene (prereg-mandated):** `control_null_by_physics` redefined = no-photon differs from signal AND
  reads `(0,0)` (True, genuinely); saturation field is `saturates` per-arm with the ratio + tolerance recorded
  (no misleading `frozen_subsecular`); a measured `read_t0` winding-null artifact is recorded in SMOKE-1.
- **α CI HARDENED:** AST `ast.Import` + attribute access + bare-CODATA-literal scan over the engine CHAIN
  **and the DRIVER**, plus a RUNTIME assertion that `ALPHA_COLD_INV`/`PHI`/`RR_GOLDEN_TORUS`/`R_I`/`V_YIELD`/`P_C`
  never enter engine STATE — **7 passed**. κ̃=6/5, V_yield≡1, c-speeds from ν_vac=2/7, lock_eta=0.05 — all α-free.
- **EMF reciprocal:** default-OFF (`converter_on=False` inherited); v4 uses ONLY the photon-director buckle +
  lock — its conservative-vs-pump contradiction (Vol-9) is untouched here.

## §8 — Honest closure (Rule 11 / substitution-not-retraction)

This is a **clean Outcome C** with a named mechanism, and a real advance over v3 on the two fatal lenses (the
photon is now coupled — no-photon null by physics; the lock is built — planted knot survives; both gates are
falsifiable; the de-novo scale is resolvable). **No debug-toward-A:** the frozen A/B/C bins were applied to the
data; B's defining condition (the helicity ledger closes) is NOT met (2 % trapped), so B was NOT claimed despite
the clean sign-provenance; the saturation STOP gate fired and I did NOT relax the frozen tolerance; α is not
invoked (no real (2,3) hosts). **Substitution-not-retraction (Rule 12):** the slot is not refilled with a new
hypothesis — the named residual (§6: depletion is a pump, the bounded coupling doesn't transfer helicity) is the
honest new boundary, surfaced for Grant, not auto-pivoted (Rule 16 / A44: this is an engine coupling-family gap,
not a missing axiom).

**Skills fired:** `substrate-native-check` (CP8 precursor-only de-novo, planted-(2,3) labeled carrier-gate; CP9
the director is the LIVE evolved photon not a frozen template, the lock is dynamical; CP10 boundary-localized
buckle); `ave-conserved-vs-pumped` (THE framing — the depletion term is the pump, the bounded coupling is the
lock-that-doesn't-transfer; the f_w detonation arm names it); `ave-fundamental-ground-up-implementation` (derived
H_couple's form, rejected the brief's literal `ω·∇×ω` candidate which gives no photon coupling); `ave-
representation-capability-check` (the resolution gate r=3.61 cells, instrument-side, PASSED — so w_pol=0 is now
PHYSICAL not representation-limited, unlike v3); `phase-space-coordinate-check` ((2,3) read in the ω reactance
pair; the poloidal "3" IS the LC quadrature — the load-bearing lock lesson); `ave-canonical-source` /
`ave-driver-script-honesty` (every number from the EVOLVED field; the f_w detonation + zero-energy-½ + ratio-
η-invariance + lockOFF≈lockON all surfaced, not buried); `ave-regime-phase-state-check` (the lock saturates
MAGNITUDE — bounded — the ratio-gate failure is a transient, distinguished from a true pump); `verify-before-cite`
(v3 demotion lenses, extractor resolution floor, Beltrami/CP grounding all re-greped this session); `flag-don't-
fix` (§6 mechanism + the saturation η-invariance + the zero-energy convention surfaced for Grant).

**Figures** (`src/scripts/vol_1_foundations/`, data-derived captions):
- `crystal_graft_v4_fig1_ledger.png` — the helicity ledger (input vs trapped per arm; no-photon null by physics;
  RH closure trapped −2 % / residual −100 %); the operative `|L_ω|(t)`.
- `crystal_graft_v4_fig2_winding_saturation.png` — ω winding per arm (all `w_pol=0`); `|L_ω|` across doublings
  (lock-ON bounded-but-not-flat vs lock-OFF vs the ∝t line).

## §9 — Corpus-state updates queued (implementer SURFACES; auditor LANDS)

- **The v3 result's two fatal lenses are REPAIRED, the residual MOVES one level deeper.** v3's "photon
  decoupled / lock unbuilt" become "photon coupled (null-by-physics, sign-traced) / lock built (knot survives,
  |L_ω| bounded)"; the NEW boundary is **§6: the photon→winding helicity TRANSFER cannot be both bounded and
  conserving in the director-buckle family** (depletion ⇒ indefinite pump; bounded ⇒ no transfer). Auditor to
  decide whether to annotate `2026-06-09_crystal-graft-v3_result.md`.
- **No new axiom drafted** (A44 / Rule 16): this is an engine coupling-family limitation, surfaced for Grant —
  the open question is whether a BOUNDED, helicity-TRANSFERRING photon↔winding coupling exists (e.g. an
  orthogonal field-space rotation à la the crystal_engine converter, rather than a trilinear potential).
- **The poloidal "3" = the LC quadrature** (§4 lesson) is the load-bearing structural surface for any next
  build: any lock must saturate the GLOBAL |L_ω| WITHOUT bleeding the LOCAL LC reactance, or the winding dies.
