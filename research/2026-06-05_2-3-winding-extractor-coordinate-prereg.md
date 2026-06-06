# (2,3)-Winding Extractor — Coordinate Fix + Validation Gate (PREREG, FROZEN)

**Date:** 2026-06-05
**Branch:** `analysis/2026-06-05-2-3-winding-extractor` (off `origin/main` @ `c1d7390f`, isolated worktree `AVE-Core-2-3-wt`)
**Status:** PREREG FROZEN — implementor build pending. Session type: orchestration (Grant in-session).
**Predecessor:** [`2026-06-04_full-electron-option-B-discrete-emergence-result.md`](2026-06-04_full-electron-option-B-discrete-emergence-result.md) — auditor item **#1 (BLOCKING)** + **#5**.

---

## §0 Scope-fence — what this is NOT (read first)

This prereg deliberately does **NOT** re-open two closed questions. Stating them so the work cannot drift into a re-tread:

- ❌ **"Does the substrate dynamically SELECT R·r=¼ / the unit?"** — CLOSED, twice-falsified, **anti-pattern-marked** ([`2026-06-04_alpha-quarter-adversarial-rechallenge.md:7`](2026-06-04_alpha-quarter-adversarial-rechallenge.md): *"not reconstructed a third time … falsified twice … No new R·r=¼-selection test is warranted."*). We run **no** R·r-selection / α-lift test.
- ❌ **"Does a transverse photon NUCLEATE the (2,3) from scratch?"** — CLOSED, refuted on retention (Arm A 1.7% ≈ baseline 1.6% ≪ imposed C 91.4%) + the ω≡0 fixed point. The (2,3) must be **seeded**; we take that as given.

**What IS open (this prereg):** the prior run's own **auditor #1 (BLOCKING)** — the (2,3)-winding **extractor is unvalidated**: it *failed to recover the Arm-C known-imposed (2,3)* (read `(8,0)`, `c=16`, spatial-ring `(0,0)` on a bond where the (2,3) was *planted*). "An extractor that cannot see a known-imposed (2,3) cannot certify its absence." Until it recovers a known signal, **no (2,3)-presence/absence/geometry claim is load-bearing.** This is a **measurement-tool validation + structural characterization**, not an emergence or α claim.

---

## §1 The diagnosis — why the prior extractor is blind (the coordinate error)

The prior extractor (`r10_…_2_3_emergence.py:phasor_temporal_winding`) set `θ₁ = phasor angle of port 1`, `θ₂ = phasor angle of port 2`, and took `(n₁, n₂)` from their windings. Two facts collapse it:

1. **A port's `(V_inc, V_ref)` phasor angle IS its capacitive↔inductive angle.** Transmission-line identity: `V = V_inc + V_ref`, `Z₀I = V_inc − V_ref`, so `(V_inc, V_ref)` is a 45° rotation of `(V, Z₀I) = (C-state, L-state)`. The driver names it: `C-state(V_inc) ⟷ L-state(Phi_link)`.
2. **Two ports of one bond ring at the same LC frequency.** So `θ₁` and `θ₂` wind at the *same rate* → the ratio is structurally **~1:1, never (2,3)**. The extractor paired the **C↔L angle with itself across ports**, and never used the second required axis.

**The (2,3) is a *pair of distinct windings* on the Clifford torus** ([`06_winding_index_projection.md` §3–4](_archive/L3_electron_soliton/06_winding_index_projection.md)):
- **w₁ = 2** — winding of the field **direction** `n̂` (the S² base; the polarization/E-field direction). A **spatial-direction** winding.
- **w₂ = 3** — the **U(1) fibre-phase** winding (the complex-amplitude oscillation phase ≈ the **C↔L / LC-slosh** angle). *(The fibre↔C↔L identification is the one mapping to PIN, not assume — Grant 2026-06-05.)*

So the (2,3) lives in **(n̂-direction winding, C↔L/U(1)-fibre-phase winding)** — and the prior extractor lived in **(C↔L-phase, C↔L-phase)**. Wrong axes. That is the whole bug.

---

## §2 The target coordinate (the fix)

A coordinate-correct extractor reads, at the trap bond / bond-pair, over the post-trap window:

- **Axis "2" (base):** the winding of the **field-direction** `n̂` — the Cosserat/`(V_inc,V_ref)`-derived polarization-direction unit vector. (NOT a port phasor angle.)
- **Axis "3" (fibre):** the **U(1) internal phase** — the LC/C↔L slosh phase, built from the **C-state `V_inc`** vs the **L-state `Phi_link`** (the axis the prior extractor *ignored*; `phi_traj` was an unused optional arg).
- **Native invariant:** the scalar **crossing count `c`** of the closed phase-space curve in the *correct* plane (corpus-native per `06_winding` post-note: electron `c = 3`).

---

## §3 Pre-registration (expect · why · discriminator)

**Expect:** the coordinate-correct extractor **recovers the Arm-C known-imposed (2,3)** — `c = 3` (or `(w₁,w₂)=(2,3)`) on the imposed-control bond — where the old one read garbage. **Why:** the imposed (2,3) is *present by construction* in Arm C; an extractor in the right plane must see it. **If it still cannot** → either the imposed ansatz does not actually plant a (2,3) in this coordinate (a deeper corpus problem, escalate) OR the fibre↔C↔L mapping (§1) is wrong (re-derive before any characterization).

**Discriminator (single-bond vs bond-pair — the pair question):** with a *validated* extractor, read where axis "2" (the n̂-direction winding) closes:
- **single-bond / midpoint** (Grant): the "2" closes on **one bond's** internal structure (≈1 ℓ_node span, crossing at the bond midpoint).
- **bond-pair / node-centred** (corpus `l3:30`): the "2" closes across the **bond-pair span** (≈2 ℓ_node, crossing at a saturated node).
These predict a *different real-space extent* of the n̂-direction winding's closure (≈1 vs ≈2 ℓ_node) — a measurable difference, **not** an α-selection.

---

## §4 PASS bars (substrate-derived; the validation gate is the anti-fit guard)

| Bar | Criterion | Discipline |
|---|---|---|
| **V0 — VALIDATION GATE (blocking)** | New extractor recovers Arm-C imposed (2,3): `c=3` (±0) OR `(w₁,w₂)=(2,3)` on the imposed-control bond, where the legacy extractor read `(8,0)/c=16`. | ave-driver-script-honesty: recover a KNOWN signal before any claim. No gate → no characterization. |
| **V1 — null on absence** | Extractor reads NO (2,3) (`c≠3`, ratio≠2:3) on the Arm-B matched baseline (no imposed winding). | discrimination-check: it must distinguish present vs absent. |
| **C1 — single/pair read** | On the validated Arm-C bound state, the n̂-direction "2" closes at ≈1 ℓ_node (single-bond) OR ≈2 ℓ_node (bond-pair); report which, with the span. | phase-space-coordinate-check; structural identification only. |
| **C2 — honest non-result** | If V0 fails, report INCONCLUSIVE + escalate (ansatz or fibre-mapping); do NOT report a single/pair verdict on an unvalidated tool. | evidence-framing. |

---

## §5 Skill discipline (applied)

`ave-prereg` (prior-work grounding: the two closed results + the blocking auditor item) · `phase-space-coordinate-check` (THE load-bearing skill — axes = direction + fibre, not port-vs-port) · `substrate-native-check` CP8 (characterize the *seeded* Arm-C state, plant nothing fresh) · `ave-canonical-source` (`ALPHA` etc. from `ave.core.constants`) · `ave-driver-script-honesty` (V0 known-signal gate = anti-fit) · `consistency-vs-emergence` (this is tool-validation [consistency] + structural-ID, NOT emergence, NOT α-derivation) · `ave-evidence-framing-discipline` (V0-fail ⇒ INCONCLUSIVE, no overclaim).

---

## §6 Deliverables

1. New extractor (module or driver section) in the (n̂-direction, C↔L/fibre-phase) coordinate.
2. Validation run against the Arm-C imposed control (load `*_capture.npz` if it carries `V_inc/V_ref/Phi_link/n̂` at the trap bond; else re-run Arm C — deterministic, ~3 min).
3. Result doc: V0/V1 gate outcome → (only if V0 passes) C1 single-vs-bond-pair read.
4. Brief updated with outcome; reviewed PR to `main`.
