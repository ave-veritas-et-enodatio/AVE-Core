# α as boundary-energy partition — PRE-REGISTRATION (frozen, committed alone)

**Date:** 2026-06-11
**Branch:** `analysis/2026-06-11-r1-alpha-forward-check` (off `origin/main` @ `f6ffd98d`)
**Lane:** implementer. This doc is the **frozen prereg only** (Rule 11 / the v7 law: committed ALONE,
before any computation; every gate an EXECUTABLE assertion). The ANALYTIC and MEASURED arms run in a
**separate** Phase-2 commit. No number is computed here; no α comparison is loaded here.
**Owner-of-record for the framing:** vocabulary-unification audit §4(c) conclusion #13
(`research/2026-06-11_vocab-operator-unification-audit.md` on `origin/analysis/2026-06-11-vocab-operator-audit`),
which named this exact test a **prereg-CANDIDATE, not derived**. This doc is that owed prereg, with its
own version + verification chain (Rule 12).

**Discipline tags applied:** `ave-prereg` (corpus-grep done; the test is corpus-canonical-CANDIDATE, not
green-field), `verify-before-cite` (every anchor grepped this session — receipts in §0.1),
`ave-power-category-check` (the load-bearing quantity classified before any scaling — §1.2),
`phase-space-coordinate-check` (claim and measurement both in the longitudinal/reactive channel — §3.2),
`consistency-vs-emergence` (the match is class-gated on a live-fire α-input test — §6),
`ave-live-fire-derivation-provenance` (the FORWARD-FIRST / Minnaert protocol — §5), `substrate-native-check`
(channel-ledger, K4/Cosserat-native, not continuum-Helmholtz), `flag-don't-fix`, `coincidence-magnet
discipline` (the two-α trap — §0.2).

> **Status: PREREG — FROZEN. Not a result. Not canon.** Bins, tolerances, definitions, and gates below
> are committed BEFORE Phase-2 computation and are NOT to be re-opened post-hoc (the PARTITION-FREEZE LAW).

---

## §0.1 — Verified anchors (verify-before-cite, re-grepped this session)

| # | Anchor | Status | Verbatim / value |
|---|---|---|---|
| 1 | `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md:35` | **VERIFIED** | `\| Electron orbital \| $90^\circ$ \| $0$ W \| $m_e c^2 \cdot \alpha$ \| Quantized reactive shell \|` — the canonical reactive store the framing rests on |
| 2 | `src/ave/core/constants.py:133` | **VERIFIED** | `ALPHA: float = 7.2973525693e-3` (CODATA fine-structure constant — the comparison target) |
| 3 | `src/ave/core/constants.py:204-205` | **VERIFIED** | `ALPHA_COLD_INV = 4π³+π²+π ≈ 137.0363038`; `ALPHA_COLD = 1/ALPHA_COLD_INV ≈ 7.29352e-3` (the golden-torus GEOMETRIC α — the reconstruction trap, §0.2) |
| 4 | vocab-audit §4(c) conclusion #13 | **VERIFIED** | "α is the transformer turns-ratio² between the transverse content (primary) and the longitudinal boundary-layer mode (secondary), `E_boundary/E_content=α`. The forward test … is a prereg-CANDIDATE, not derived here." |
| 5 | banked MEASURED data — `s11_denovo_results.json` | **SHA-PINNED** | committing commit `570b50d7a560e54fb0c270a859e7e9c99c6e3968` on `origin/analysis/2026-06-11-s11-de-novo` (verified via `git log -1 -- src/scripts/vol_9_device/_output/s11_denovo_results.json`); fields `made_build.E_V_cons_{first,last}`, `made_build.H_cons_{first,last}` present |
| 6 | 2026-06-04 ¼-closure §5 gate law | **VERIFIED** | `research/2026-06-04_alpha-quarter-adversarial-rechallenge.md:54` — "over-determination is the **tell of a coincidence-magnet**, not robustness … evidence *only* if a route made a **discriminating secondary prediction** the others don't, **and the substrate confirmed THAT**." |
| 7 | #192 Nyquist closure (four kill grounds) | **VERIFIED** | `research/2026-06-11_nyquist-binding-route_CLOSED.md` §2 — IDENTITY (`c/ℓ_node=ω_C`) laundered as emergence; factor-π over-determination tell |

## §0.2 — The two-α trap (coincidence-magnet discipline, declared up front)

`constants.py` carries **two** quantities near `7.29e-3`: CODATA `ALPHA = 7.2973525693e-3` (:133) and the
golden-torus geometric `ALPHA_COLD = 1/(4π³+π²+π) ≈ 7.29352e-3` (:204-205). They differ only at the **4th
significant digit** — far inside any forward energy-partition band. **A forward partition that lands near
7.29e-3 cannot, at forward-band precision, distinguish "matches CODATA α (emergence-candidate)" from
"reconstructs the golden-torus geometric α (the ¼-family)."** This is named here so it is not discovered
post-hoc. The comparison TARGET is **CODATA `ALPHA` (:133)**. The golden-torus `ALPHA_COLD` is the
reconstruction fingerprint the ANALYTIC arm is fenced against (§1.1 + §4.1).

---

## §1 — THE FENCE (runs FIRST, adversarial; the route does not run unless it clears)

**Per THE 2026-06-04 §5 GATE LAW: the fence check runs FIRST.** The E_boundary=α·mc² route must be shown
**ORTHOGONAL** to every closed α route, or — if it reconstructs one — STOP and report. The discriminating
distinction argued below: **this route MEASURES an energy ratio on an existing self-assembled object
(emergence-class evidence IF it lands without α in the inputs) — it does NOT DERIVE α from a geometric or
kinematic identification, as every closed route does.**

### §1.1 — Orthogonality vs each closed route (argued adversarially)

| Closed route | How it DERIVES α | Is E_boundary that move? | Verdict on this axis |
|---|---|---|---|
| **kinematic-bijection lift** | identifies a bijection between two geometric structures and reads α off the lift | No — the route measures a **conserved-energy ratio on a dynamical attractor**; no geometric structures are identified with each other | **ORTHOGONAL** (energy-partition measurement, not a geometric lift) |
| **¼-reconstruction family** (2026-06-04) | ≥6 geometric counts (Nyquist phasor-area, ½-cover, matched-Z, quarter-wave, KAM, parametric) all land ½²; §5 tell = over-determination = coincidence-magnet | MEASURED arm: No — a **single** energy ratio, claims no geometric fraction. ANALYTIC arm: **AT RISK** — deriving `E_boundary/E_content` from wall geometry could reduce to `1/(4π³+π²+π)` = golden-torus `ALPHA_COLD` (§0.2), which IS the ¼/golden-torus family | **PARTIAL** — measured orthogonal; analytic FENCED (bins ANALYTIC-BLOCKED if it reaches α only via the golden-torus geometric Q) |
| **Nyquist-binding route** (#192) | re-narrates the IDENTITY `c/ℓ_node=ω_C` as a sampling-rate readout (laundered as emergence; factor-π tell) | No — the route uses **no** `c/ℓ_node` identity, claims **no** sampling-rate readout, **relabels no** `{m_e,ℓ_node}` input scale. BUT must live-fire-check the engine's `E_V_cons/H_cons` is not a **disguised definitional identity** that forces the ratio (§5 forward-vs-fit / dead-input test) | **ORTHOGONAL** pending the live-fire identity check |
| **radiation-ladder reading** (α-flux scout) | counts radiation-ladder steps / flux quanta — a **P_real** radiated-flux story | No — by `ave-power-category-check` (§1.2) E_boundary and E_content are **both `Q_reactive` stores**; α is the **reactive transfer ratio between two stores**, with **zero radiated flux**. Different power category entirely | **ORTHOGONAL** (cleanest axis: `Q_reactive` store-partition vs `P_real` flux-ladder) |

### §1.2 — Power-category classification (ave-power-category-check, locked before scaling)

Load-bearing quantity: *the fraction of the converged soliton's total conserved energy stored in its
longitudinal V-sector (the standing-V boundary mode, the "3").*

- **Real-vs-Reactive:** **Q_reactive** — both stores are reactive (orbital-friction-paradox.md:35: electron
  orbital θ=90°, P_real=0, Q_reactive = m_ec²·α). α is the reactive transfer ratio, not a loss.
- **Propagating-vs-Bound:** **BOUND** (the standing-V of the Γ_bulk→−1 self-created wall).
- **On-shell-vs-Off-shell:** **ON-SHELL** (a real conserved-energy partition of a settled attractor).
- **Internal-tank-vs-External-matched:** **INTERNAL** (the object's own L↔C store partition; NOT a
  detector-coupling efficiency).
- **Substrate-mode-vs-Atomic:** **SUBSTRATE-MODE** (K4/Cosserat conserved energies; Z-independent).

Scaling-law implication: a **reactive internal store-partition** — measured directly from the conserved-
energy ledger, with **no α-power assembly** and **no radiative cross-section**. This is precisely the axis
that makes the route orthogonal to the P_real radiation-ladder.

### §1.3 — FENCE VERDICT: **PARTIAL**

- The **MEASURED arm** (forward `E_V_cons/H_cons` ratio on the de-novo MADE object, whose genesis does not
  inject α — to be **live-fire-confirmed** by the dead-input test, §5) is **ORTHOGONAL** to every closed
  route: an energy-partition MEASUREMENT on a self-assembled attractor, in the Q_reactive store category —
  not a geometric lift, not a sampling-rate identity-relabel, not a radiated-flux ladder, not a geometric
  count. It is in the SPIRIT of canon's Layer-8 acceptance test (measure a property of the self-assembled
  object, α nowhere in inputs), **not** the identity-laundering anti-pattern.
- The **ANALYTIC arm** carries a **named reconstruction hazard** against the ¼/golden-torus family: a wall-
  geometry derivation could collapse to `ALPHA_COLD = 1/(4π³+π²+π)` (§0.2). The prereg FENCES this: the
  analytic arm must reach the partition from the kernel `S(A)=√(1−A²)` + the Γ_bulk=−1 boundary condition's
  **standing-V energy** WITHOUT invoking the golden-torus geometric Q; **if it can only reach α via that
  count, it bins ANALYTIC-BLOCKED (reconstruction)**, and the route stands on the MEASURED arm alone.

**Because the MEASURED arm is orthogonal AND carries a discriminating secondary (§2), the route RUNS** —
with the analytic arm explicitly fenced. It is NOT a wholesale reconstruction (so not STOP); it is NOT
purely orthogonal (so not ORTHOGONAL). **PARTIAL** is the honest verdict.

---

## §2 — THE DISCRIMINATING SECONDARY (named, frozen)

Per the §5 gate law, a match is evidence **only** if the route makes a **discriminating secondary
prediction the closed routes do not**, and the substrate confirms THAT. The closed routes are all
single-identity derivations; **none makes a cross-object prediction.**

**FROZEN SECONDARY — cross-object-class partition invariance.** The route predicts that the boundary-energy
fraction is a **structural property of the soliton class**, hence **invariant across object classes built by
different recipes/scales**: the de-novo MADE rotation-column vs a planted-seed breather. **Same fraction →
structure (the turns-ratio is real); different fraction → build/scale accident (the single-object match is a
coincidence-magnet).** This is a prediction NO closed route makes and is independently checkable.

**Why this and not the alternatives (all three task candidates evaluated):**
- *Q-link (`E_boundary/E_total = 1/Q`):* **REJECTED as the secondary** — it is the reconstruction trap
  itself (canon `Q = α⁻¹ = 4π³+π²+π`, the golden-torus geometric count). Leaning on it would reconstruct
  the ¼-family, not discriminate against it.
- *drive-frequency independence:* strong physically (a transformer turns-ratio is excitation-independent)
  but **needs a new drive sweep** (a new sim) — disfavored under the banked-data-first rule.
- *cross-object-class invariance:* **strongest + closest to bankable** — it is the structure-vs-accident
  test the §5 law demands.

**Bankability honesty (flag-don't-fix):** the s11_denovo `planted` leg banks **probe-response only** (no
`E_V_cons`/`H_cons`); the v6 genesis JSONs at `main` bank **no** energy-partition fields (grep-verified
this session). So the secondary requires **ONE cheap re-extraction** of `E_V_cons + H_cons` on the second
object (the planted-seed genesis), using the **same conserved-energy accounting** the made_build leg already
uses — a small re-run, NOT a new physics sim. If that re-extraction is not cheaply available, the secondary
bins **SECONDARY-BLOCKED** and the primary match is downgraded to **single-object (coincidence-magnet-
unguarded)**.

**Zero-cost companion check (fully banked, registered alongside):** *convergence-stationarity* — the fraction
`E_V_cons_first/H_cons_first` vs `E_V_cons_last/H_cons_last`. A real structural fraction is **stationary**
across the settle window while the absolute energies move (E_V 11.70→12.91, H 29203→24612); a transient
snapshot is not. Computable from the four banked scalars at zero cost.

---

## §3 — THE PARTITION-FREEZE (one definition frozen, others as robustness arms)

### §3.1 — The three canonical candidate definitions (per the PARTITION-FREEZE LAW)

- **(a) longitudinal-mode projection** — E_boundary = the standing-V / longitudinal-channel share of the
  converged object's total conserved energy, per the channel-ledger decomposition.
- **(b) spatial interface band** — cells within the canonical interface width ℓ_c of the saturation boundary.
- **(c) reactive/oscillatory share** — per the reactance-pair (C-state / L-state) decomposition.

### §3.2 — FROZEN: definition **(a)**, the longitudinal-mode projection

**Frozen on canon grounds (NOT on proximity to α):**
1. vocab-audit §4(c) identifies E_boundary as "the standing **longitudinal V** of the soliton wall (the
   '3', **Z_bulk channel**)"; the three-impedance law §4(a) makes the **bulk-longitudinal** channel the
   boundary-forming channel (`Γ_bulk→−1` sonic-horizon reflector).
2. The engine's `E_V_cons` **is** the conserved longitudinal V-sector energy — the matching coordinate
   (`phase-space-coordinate-check`: claim in the longitudinal/reactive channel, measurement in `E_V_cons`,
   the longitudinal channel → **MATCHING**, not a real-space-Cartesian mismatch).
3. **(a) is the only candidate the banked data supports forward with zero new sim** (`E_V_cons` and `H_cons`
   are both banked scalars) — satisfies FORWARD-FIRST.

**FROZEN PRIMARY ratio:**
```
r  ≡  E_boundary / E_total  =  E_V_cons_last / H_cons_last
```
(longitudinal share of total conserved energy, evaluated at convergence).

> **Honesty note (forward-first integrity):** the scalar values `E_V_cons_last ≈ 12.91`, `H_cons_last ≈
> 24612` were **visible during JSON-structure inventory**; the ratio `r` and its α-comparison were **not**
> computed. The definition is frozen on the canon grounds (1)-(3) above, **not** on number-proximity to α.
> Disclosed so the freeze cannot be mistaken for number-chasing.

### §3.3 — The robustness arms (pre-registered; NOT post-hoc selection)

| Arm | Definition | Banked? | Pre-registered status |
|---|---|---|---|
| **(a2)** | `r2 = E_V_cons / (H_cons − E_V_cons)` — the literal §4(c) `E_boundary/E_content` (longitudinal / complement) | YES | runs; `r2 ≈ r` for `r≪1` |
| **(a3)** | `r3 = E_V_cons / (H_cons − E_bulk_decoupled)` — excludes the canon-flagged decoupled-bulk reservoir (`bulk_sector_unstable_free_evolution=True`, `bulk_decoupled_from_V_proof`) | field NOT obviously banked | **likely ANALYTIC-BLOCKED** — and excluding a reservoir to hit α is coincidence-magnet-adjacent; only justified by the bulk_decoupled flag, NEVER by α-proximity |
| **(b)** | spatial interface band within ℓ_c of the snap boundary | NO (no per-cell fields; `pocket_cells=0`) | **VOID** — SHELL-NEVER-FORMS on this object; no interface band exists to integrate |
| **(c)** | reactive/oscillatory share per the reactance-pair | NO (ringdown banks w_est/Q, not an energy split) | **ANALYTIC-BLOCKED** on banked data — needs C-state/L-state pair re-analysis |

**Pre-registered spread finding:** on this banked object the robustness spread is **under-evaluable** — only
(a)/(a2) run on banked data; (b) is VOID (SHELL-NEVER-FORMS) and (c)/(a3) are ANALYTIC-BLOCKED. **This
limitation is itself a result** and feeds the DEFINITION-SPREAD / ANALYTIC-BLOCKED bins (§4).

---

## §4 — THE TWO ARMS

### §4.1 — ANALYTIC arm (α NOWHERE in inputs — derivation PLAN, not derived here)

**Plan:** derive E_boundary from the canonical soliton structure — the standing-V / latent share from the
Axiom-4 kernel `S(A)=√(1−A²)` plus the `Γ_bulk=−1` boundary condition at the saturated-core wall — and the
total conserved energy from the same kernel, with **α absent from every input** (K4 lattice primitives +
Axiom-4 saturation only). **Fence (§1.1):** if the only route to the partition's value is the golden-torus
geometric Q `= 4π³+π²+π` (i.e. it equals `ALPHA_COLD`, not an independent wall-energy integral), the arm
bins **ANALYTIC-BLOCKED (reconstruction)** — it has re-derived the ¼/golden-torus family, not an orthogonal
energy partition. Class: **emergence-target** only if parameter-free AND not the golden-torus count.

### §4.2 — MEASURED arm (banked, SHA-pinned; re-analysis scope stated)

**Primary:** `r = E_V_cons_last / H_cons_last` from `s11_denovo_results.json.made_build`, SHA-pinned at
commit `570b50d7…` (§0.1 #5). Forward, banked, zero new sim.
**Secondary (cross-object):** requires one cheap `E_V_cons+H_cons` re-extraction on the planted-seed object
(§2). **Robustness arms:** (a2) banked; (a3)/(b)/(c) blocked/void per §3.3.
**α-input gate (consistency-vs-emergence, §6):** the de-novo object's genesis must be **live-fire-checked**
for α as a load-bearing input (dead-input test). NOTE the v6 **phasor** object carries `gamma_target_for_alpha`
/ `comparison_only_alpha` (α IS referenced in THAT object's inputs → consistency-class); the de-novo MADE
object's α-dependence is the live-fire question that sets the class of any match.

---

## §5 — FORWARD-FIRST protocol (the Minnaert / live-fire-provenance pattern)

Phase-2 driver MUST, in this order, with the **α comparison loading LAST**:
1. compute + **PRINT** the ANALYTIC number (§4.1) — or print `ANALYTIC-BLOCKED: <named missing primitive>`;
2. compute + **PRINT** the MEASURED partition `r` (and `r2`, stationarity, secondary if available) — all
   **before** α is referenced;
3. **THEN** load CODATA `ALPHA` (constants.py:133) and compute `r/α`;
4. **dead-input test** (`ave-live-fire-derivation-provenance` Step 3): vary the genesis α-input ×{1, 1e6} —
   if `r` is unchanged, α is a DEAD input to the object → a match is emergence-candidate; if `r` moves with
   α, the match is consistency-class (α laundered through the inputs);
5. **forward-vs-fit test** (Step 4): confirm no α-target sits in the energy-accounting loop (no
   `comparison_only_alpha`-style field feeds `E_V_cons` or `H_cons`).

---

## §6 — consistency-vs-emergence tag (pre-committed)

- **MATCHES-α with α a DEAD genesis input + analytic arm parameter-free (not golden-torus) →** *emergence-
  class* (and must still clear the §1 fence, which it does as PARTIAL/measured-orthogonal).
- **MATCHES-α with α LIVE in the genesis inputs, OR analytic arm = golden-torus count →** *consistency-class*
  (α is CODATA-anchored through the inputs / the geometric Q is re-narrated). The honest default until the
  dead-input test says otherwise.
- The vocab-audit §4(c) already pre-classifies: "A forward pass is **consistency-class** (α is CODATA-
  anchored at the inputs); only a parameter-free derivation of the turns-ratio from the wall geometry would
  be emergence-class — and that must clear the §5 reconstruction-stop fence first."

---

## §7 — FROZEN BINS (ordered) + EXECUTABLE GATES

Tolerance (frozen BEFORE computation): forward energy-partition band **`MATCH ⟺ |r/α − 1| ≤ 0.25`**
(coarse forward band; honest, not a tight fit), with a **TIGHT sub-flag at `≤ 0.05`**. `α = ALPHA` (CODATA,
constants.py:133).

Ordered bins:
1. **MATCHES-α** — `|r/α − 1| ≤ 0.25`, surviving (a2), the convergence-stationarity companion, AND the
   coincidence-magnet/two-α check (§0.2). Class per §6.
2. **DIFFERENT-RATIO** — `|r/α − 1| > 0.25`. Report `X = r/α` and what `r` physically is (e.g. if
   `r ≈ E_V_cons/H_cons` lands ≈14× below α because `H_cons` carries the decoupled-bulk reservoir, that is
   the finding: the longitudinal share of *total* conserved energy is **not** α at this definition).
3. **DEFINITION-SPREAD** — (a), (a2), and any runnable arm disagree wildly → **UNDERDETERMINED**.
4. **ANALYTIC-BLOCKED** — the analytic arm's missing primitive named (e.g. "the standing-V wall-energy
   integral is only reachable via the golden-torus geometric Q → reconstruction → blocked"), and/or arms
   (a3)/(b)/(c) blocked per §3.3.

**Executable gate assertions (frozen — Phase-2 must implement these verbatim):**
```python
import json
from ave.core.constants import ALPHA  # 7.2973525693e-3, constants.py:133
ALPHA_COLD = 1.0/(4*3.141592653589793**3 + 3.141592653589793**2 + 3.141592653589793)  # golden-torus trap

d = json.load(open(".../s11_denovo_results.json"))          # SHA-pin 570b50d7…
mb = d["made_build"]
r        = mb["E_V_cons_last"]  / mb["H_cons_last"]          # FROZEN primary (a)
r2       = mb["E_V_cons_last"]  / (mb["H_cons_last"] - mb["E_V_cons_last"])  # arm (a2)
r_first  = mb["E_V_cons_first"] / mb["H_cons_first"]         # stationarity companion
stationary = abs(r/r_first - 1.0) <= 0.10                    # frozen 10% stationarity band

# FORWARD-FIRST: print r, r2, r_first, stationary BEFORE the next two lines (the Minnaert order, §5)
match      = abs(r/ALPHA - 1.0) <= 0.25                      # bin 1 gate
tight      = abs(r/ALPHA - 1.0) <= 0.05                      # tight sub-flag
two_alpha_indistinct = abs(ALPHA/ALPHA_COLD - 1.0) < 0.25    # True → cannot separate emergence from golden-torus reconstruction at this band

assert (b is VOID) , "arm (b): pocket_cells==0 ⇒ SHELL-NEVER-FORMS ⇒ no interface band"  # mb["pocket_cells"]==0
# bin = MATCHES-α if match and stationary and secondary_invariant and not two_alpha_indistinct-unguarded
#       else DIFFERENT-RATIO (report r/ALPHA) / DEFINITION-SPREAD / ANALYTIC-BLOCKED  (ordered, §7)
```

---

## §8 — Step-3.5 dimensional / magnitude pre-registration (ave-prereg v1.1)

`r` is **dimensionless** (energy/energy). Expected magnitude = α = 7.297e-3 (sub-percent). Forward band
[0.75α, 1.25α] = **[5.47e-3, 9.12e-3]**. **Pre-registered most-likely outcome (transparent, per the §3.2
glimpse-disclosure):** the share-of-TOTAL reading (a) is `r ~ E_V_cons/H_cons` with `E_V_cons ~ O(10)` and
`H_cons ~ O(10^4)`, so `r ~ O(5e-4)` — **~14× BELOW α → DIFFERENT-RATIO is the a-priori most probable bin**,
unless `E_total` should exclude the canon-flagged **decoupled-bulk reservoir** (`bulk_sector_unstable_free_
evolution=True`). Excluding that reservoir (arm a3) is the ONLY physically-motivated path toward α — and it
is **fenced**: justified only by the bulk_decoupled flag, NEVER by α-proximity. This pre-registration means
a DIFFERENT-RATIO outcome is the expected honest result, not a surprise, and an α-match would require the
fenced (a3) reservoir-exclusion to both run AND be independently justified.
