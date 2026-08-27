---
id: device-circuit-models-165-correction
title: "CORRECTION — device-circuit-models.md:165 ASSERTS the A1 wall; it does not prohibit it"
status: OPEN
owner: lane
opened: 2026-08-26
source: research/2026-08-26_virtual-neutral-boundary-arc_RECORD.md
anchor: "does NOT argue against the A1/bulk wall. It ASSERTS it"
---

**The correction, in one line.**
`manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md`:165
**asserts** that the confinement surface is the A1 mass wall. It is **not** a
prohibition against the A1/bulk wall, and **any document that inherited the
earlier "prohibition" framing is wrong and must be corrected.**

**What the line actually says**, verbatim:

> *"**Two coincident `Γ=−1` walls — do NOT re-collide.** The confinement
> surface is the **A1 MASS wall** (`Z_bulk→0`, the impedance-short `Γ=−1` of
> the Pauli/TIR derivation). It is numerically coincident with — but a
> **DISTINCT object** from — the **`Γ_spinor = −1`** topological `2π→4π`
> stability wall of the T2 micro-rotation sector … Reading the two `−1`'s as
> one wall would wire the cage into the charge-winding and break the two-"3"s
> orthogonality."*

**The misreading and the fix.** The guard sentence warns against **colliding**
the A1 mass wall with the `Γ_spinor` T2 wall. It argues **on the A1 side**.
Reading it as "`:165` forbids the A1 wall" inverts its position.

**★ And correcting it exposes a live canon-vs-canon tension** that the
misreading concealed — this is the substantive half of the item:

| site | who owns the confinement surface |
|---|---|
| `device-circuit-models.md`:165 | *"The confinement surface **is the A1 MASS wall**"* |
| `common/vocabulary-register.md`:751 (`def-vyvsn1`, **SOLID**) | `V_yield` = the *"transverse Cosserat (`T_2`) self-trap wall … the single-electron confining `Γ=−1` TIR cavity self-creates here"*; and *"**The A1 mass channel does NOT saturate at `V_yield`**"* |
| `vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md`:102 | *"a single electron's confining `Γ = −1` wall is **already here**"* — at `V_yield`, the **T2** threshold |

**A number on the A1 side** (measured on the shipped operator, reproduced in
the record §2.5): at `def-vyvsn1`'s own A1 operating point `A = √α = 0.0854`,
`S = 0.996345`, `Z_eff = √S = 0.998171`, and **`Γ_bulk = −9.155133e-04`** — a
0.09% reflection. Canon itself already states the physics behind that number
(`vocabulary-register.md`:757: the A1 core is *"sub-saturated (`S(√α) =
√(1−α) ≈ 0.996`), which is why the mass channel does not run away"*). So the
A1 branch **cannot** be a mirror at the amplitude canon assigns the A1 core.

**Related gate observation** (record §2.5.1): the T3.3 acceptance gate
(`sup-1ecv2m`, `electron-bound-resonator-coverage.md`:226) records *"literal
`−1` unreachable"* and passes on a `−0.25` crossing — but probes at `A=0.95`
(`Γ=−0.283`) and `A=0.99` (`Γ=−0.454`), amplitudes the electron's own A1 core
never reaches. Both values were reproduced here and match canon exactly.

**Scope — what this item is and is not.**

- **IS:** (a) a Rule-12 correction of the reading of `:165`; (b) a sweep for
  downstream inheritors of the misreading; (c) registration of the sector-
  ownership tension so it is adjudicated rather than absorbed.
- **IS NOT:** an adjudication of that tension, an edit to `def-vyvsn1`, or a
  claim that there is no electron wall. The arc never computes the **T2**
  channel — the one `def-vyvsn1` actually assigns the wall to.

**Work to do.**

1. Read `device-circuit-models.md`:163-167 end to end and confirm the guard
   sentence's target. (Kill condition **K6** of the record fires if `:165`
   does not assert the A1 wall on a full reading.)
2. Sweep for documents inheriting the "prohibition" framing. Per the
   grep-completeness rule: cross-check any "N sites / none found" result with a
   second method, and **report the method, not the corpus**.
3. Route the sector-ownership tension (A1 vs T2 ownership of the confinement
   surface) for adjudication. It is **upstream** of
   `2026-08-26-virtual-neutral-register-move.md` — which sector owns the wall
   must settle before which register the wall belongs to is meaningful.
4. Decide whether T3.3 should be re-run at `A = √α`, or whether its probe
   amplitudes are a deliberate scope choice with a stated rationale (audit item
   **A10**).
