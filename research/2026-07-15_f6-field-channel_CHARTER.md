# F6 field channel — irreversible ε→T2 / fluctuation sink — CHARTER

**Date:** 2026-07-15 · **Class:** charter (discriminator BEFORE any driver) — remanence-charter pattern. · **Status:** ★ **GRANT-GO'd 2026-07-15** (in-chat: "2. proceed") — charter accepted; freeze prereg then driver. · **Priority:** hardware-ratings-map R7 / §3 item 1 (Priority 1).

**What this is NOT.** This is **not** a redo of the F6 **tier-1 two-reservoir ODE ledger** (`research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md`, driver MERGED #674, §5.4 ★RULED BOTH). Tier-1 already banks FORM-EXISTENCE of the occupancy-slaved chord as a *homogeneous bookkeeping* object and WRONG-INSTRUMENT closure for late homogeneous averages. **This charter addresses the still-UNBUILT engine capability:** a BOUNDED, Ax3-legal, norm-preserving **field-level** irreversible ε→T2 channel — the missing fluctuation / entropy sink that (a) the DE chord needs as realized substrate physics and (b) the lattice thermometer needs after PR #707.

**Sector header (mandatory).** MODE: local lattice field dynamics with a one-way transfer into a mode-count sink — **not** a global ODE ledger, **not** an `a(t)` Friedmann evolver. REGIME: sub-yield to moderately saturated; reversible Cosserat/K4 interior preserved. PHASE-STATE: coherent bound / coherent radiating / incoherent bath. SECTOR: A-class continuous drainage into T2 (entropic), **not** A1 dilatation-mass, **not** Cosserat-winding genesis, **not** friction on a soliton's own energy.

**Register:** AVE substrate + EE peer-check labels only (Nyquist / FDT as translation after CHANNEL-BOUNDED — **not** design targets). **Not** ΛCDM Λ-as-ontology, **not** QED zero-point as imported ontology, **not** the detonating `photon_deplete=True` indefinite-Hamiltonian attempt, **not** pre-named “matched-termination Re(Z) absorb” (Grant 2026-07-15: forbidden as the plan; see `2026-07-15_f6-mode-count-door_CHARTER.md`).

---

## 0 · One-paragraph charter

The reversible engine as built is **athermal**: PR #707 showed relative-phase diffusion under a bath is an **additive artifact**; isolated Op14 dephasing is **bounded** (Ax3-forced). QED loops and a diffusion-rate thermometer both need fluctuations + a sink. Cosmology's F6 chord needs a **bounded norm-preserving ε→T2 depletion** that does not detonate (`dark-energy-latent-heat-definition.md`:152–157 gate 1). This charter freezes the discriminator for that **field channel**: introduce an Ax3-legal one-way transfer of energy from a local ε-store into a high-mode-count T2 bath (irreversibility from mode-count, not friction), with hard detectors for (i) no indefinite Hamiltonian, (ii) bias≠release, (iii) electron-no-drain, (iv) reversible interior conserved when the channel is OFF. Tier-1 ledger results stand; this is the capability they assumed as an ODE premise.

---

## 1 · Why now (receipts)

| Motivation | Receipt | Role |
|---|---|---|
| **DE-tracks-matter chord** | `dark-energy-latent-heat-definition.md` §5; engine-capability-map F6 rows; tier-1 #674 | Form exists in ledger; **field realization UNBUILT**; prior `photon_deplete=True` detonates |
| **Lattice thermometer** | PR #707 `ADDITIVE-ARTIFACT`; `thermal-phase-registers.md` ★#1 DEMOTED / RE-GATED | Lossless kernel ⇒ only bounded reversible dephasing; diffusion-**rate** needs irreversibility |
| **QED loops** | Ratings-map §1; #693 spectator medium | #693 is a *separate* no-log result from #707’s no-sink; ℏ=FD **UNBANKED** (FORM not derived) |
| **Hardware row R7** | `_orchestration/2026-07-15_hardware-ratings-map.md` | REFUSED as-built → missing spec page = this channel |

Docket Entry 14 convergence note: DE + thermometer independently point at the same unbuilt primitive.

---

## 2 · Physical picture (ruling-grade inputs — inherited, not re-derived)

Four-element map (Grant-walked 2026-07-13; same as tier-1):

| Element | Identity |
|---|---|
| **Source** | local ε / ρ_latent-class store (static-sector held energy) |
| **Destination** | T2 bath (huge mode-count; irreversibility from mode-count) |
| **Transducer** | mass envelope / off-line↔on-line door (implementation choice = frozen bin, not fiat) |
| **Door** | one-way transfer; Ax3-compliant (`dS>0` into bath, not friction loss) |

**Hard prior negative:** any continuous transfer that makes the Hamiltonian indefinite (the `photon_deplete=True` detonation) is a **kill** of that implementation class — not a retune. Prefer event-gated / entropic-bookkeeping forms that keep the reactive interior positive-definite. **Do not** pre-name “matched-termination Re(Z) absorb” as the plan (Ax3 retirement knife; Grant 2026-07-15 — next discriminator: `2026-07-15_f6-mode-count-door_CHARTER.md`).

---

## 3 · Scope fence

**IN scope (this charter):**
- One local or lattice-window field implementation of ε→T2 transfer.
- Frozen bins: BOUNDED-PASS / DETONATE-FAIL / BIAS-MOVED-FAIL / ELECTRON-DRAIN-FAIL / NO-TRANSFER-NULL.
- Mandatory ON/OFF control; energy ledger `ΔE_ε + ΔE_T2 ≈ 0` (conservation within tol).
- Mechanism control proving the sink is **not** additive numerical dissipation.

**OUT of scope (explicit):**
- Re-running or amending the tier-1 homogeneous ODE ledger (#674 stands).
- Spatial DESI/Euclid cross-correlation (downstream of a working channel).
- Deriving κ / magnitude from `{ℓ_node,α,G}` (chord vs echo — gate for later).
- QED loop summation or ℏ value (ℏ=FD **UNBANKED** — FORM not derived; not a successor workstream of this charter).
- Pre-naming matched-termination Re(Z) absorb as the next door (Grant-forbidden; see mode-count door charter).
- F1 ordering fix (orthogonal engine hygiene; ratings-map Priority sequencing keeps F1 before census S2, not before this charter).

---

## 4 · Frozen bins (pre-driver; do not retune)

| Bin | Name | Fire condition (sketch) |
|---|---|---|
| **(i)** | **CHANNEL-BOUNDED** | Transfer ON: energy leaves ε-store into bath; Hamiltonian eigenvalues / energy norm stay bounded for full run; OFF recovers reversible Ax3 behavior |
| **(ii)** | **DETONATE** | Any indefinite / runaway / NaN / energy blow-up under ON (repeats `photon_deplete` class) → **implementation killed** |
| **(iii)** | **BIAS-MOVED** | Operating-point bias / electron rest quantities move under ON vs OFF beyond tol → fails bias≠release |
| **(iv)** | **ELECTRON-DRAIN** | Bound soliton self-energy drains under ON without bath coupling intent → fails electron-no-drain |
| **(v)** | **NULL** | ON indistinguishable from OFF (no transfer) → channel not implemented |

Decision rule: **(ii)/(iii)/(iv) fail closed**; only **(i)** licenses a follow-on prereg for thermometer re-fire and/or spatial F6 chord. **(v)** = build incomplete, not physics.

---

## 5 · Fool-modes (name before fire)

1. **Additive sponge / PML leakage** misread as T2 sink — require interior-only bath bookkeeping + OFF control.
2. **Numerical damping** in the integrator — require exact-arithmetic or double-precision ledger with known reversible baseline.
3. **Renaming friction as entropic transfer** — require bath mode-count / phase-space volume increase, not soliton Q-drop alone.
4. **Retuning after detonation** — Rule 11: kill the implementation class; do not soften bins.
5. **Quietly amending tier-1** — KEEP-BOTH; this channel does not reopen §5.4.

---

## 6 · Successor gates (registered, not this charter)

After **(i) CHANNEL-BOUNDED**:
1. Re-fire two-tank / thermometer with channel ON (mechanism-gated criterion from #707).
2. Loop-ledger charter (ratings-map §3 item 2) — which diagram classes become fireable — **separate** from any ℏ=FD claim (unbanked).
3. Spatial F6 chord / DESI–Euclid discriminator (engine-capability-map relocation).
4. Next in-Hamiltonian door after rung-2 kill: [`2026-07-15_f6-mode-count-door_CHARTER.md`](2026-07-15_f6-mode-count-door_CHARTER.md).

---

## 7 · Deliverables for the driver lane (after this charter reviews)

- Frozen prereg sibling (`…_prereg_FROZEN.md`) by push **before** any driver.
- Minimal harness on an existing reversible platform (prefer native K4 or VacuumEngine3D; no new genesis_v{N}).
- ON/OFF + detonation + bias + electron-no-drain detectors wired as first-class asserts.
- RESULT with Rule-11 honesty if bins fail.

---

*Charter only. Nothing here canonizes a value. Tier-1 #674 KEEP-BOTH. Grant reviews before driver.*
