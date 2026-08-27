---
id: virtual-neutral-register-move
title: "ROUTED TO GRANT — move the electron row from boundary register 1 (AMPLITUDE LEVEL-SET) to register 4 (BALANCE LOCUS)?"
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-26
source: research/2026-08-26_virtual-neutral-boundary-arc_RECORD.md
anchor: "move a row between two registers canon already defines"
---

**The proposal in one line.** `boundary-observables-m-q-j.md`:56-63 files the
electron under boundary **register 1 — AMPLITUDE LEVEL-SET**. This proposes
moving it to **register 4 — BALANCE LOCUS**: the boundary is where the Wye
node's phasor sum cancels (`Σ_j Y_j V_j^inc = 0`), not where a scalar
amplitude crosses a threshold.

**★ IT DOES NOT SUPERSEDE `def-vyvsn1`. Only Grant rules that.** `def-vyvsn1`
is SOLID and is the only SOLID electron-wall statement in the corpus. Nothing
is edited, demoted, or re-graded by this item.

**Why it is a move and not a mint.** Both registers already exist in canon, so
the proposal uses a category canon already defines rather than minting one.

> ⚑ **[OPEN] — corrected 2026-08-27.** An earlier version of this item added
> that `vocabulary-register.md`:404 (`def-anat3s`) *"already banks the conjecture
> the move would discharge"* — surface (ii), the balance shell, *"CONJECTURED ≡
> wall per Ruling 6"*. **That performed the weld caution 2 below forbids.**
> `def-anat3s`'s surface (ii) is the **real-space** `σ`-balance object: the
> def-node's `axis:` is `spatial-Brillouin` (`:405`), its `dimension/type:` is
> `length (L) — three distinct radial loci` (`:406`), and its balance-shell
> anchor is `hollow-vortex-binding.md`:49,:133 (`:411`) — the same citation
> caution 2 gives for the pressure-balance column. **Whether that surface is the
> same surface as the port-space phasor balance is exactly what is
> under-determined, and neither this item nor the record takes a position on
> it.** The register move therefore does **not** discharge `def-anat3s`'s
> surface-(ii) conjecture.

**What is measured, and what it costs the incumbent.** On the shipped operator
(`src/ave/solvers/vacuum_varactor_scatter.py`), reproduced in the record:

- A **uniformly saturated shell reflects EXACTLY like cold vacuum** (`Γ = −1/3`
  on every port, difference `0.000e+00`) — the mirror is the *gradient* at the
  shell edge, never the saturation level.
- `Σ_i S_ii = 2 − z` **exactly**, so at `z=3` driving one port to `Γ=−1` forces
  the other two to sum to `0`. **`Γ=−1` on all three ports is arithmetically
  unreachable by saturation.**
- On canon's own bulk route at `def-vyvsn1`'s own A1 operating point `A=√α`:
  **`Γ_bulk = −9.155133e-04`** — a 0.09% reflection.

**★ AND THE TWO CAUTIONS, WHICH ARE NOT OPTIONAL READING.**

1. **A local `−1` is NOT confinement.** Balance is codimension-1 *per node*, so
   balanced nodes are **cheap, not special** — the `−1` eigenspace is present at
   **every node of empty cold vacuum**, where nothing is confined. The electron
   would have to be a **closed surface of simultaneously balanced nodes**, which
   is a property of the composed map `M = C · blockdiag(S)`. **The corpus DOES
   compute `M`** (`assemble_varactor_scattering`,
   `src/ave/solvers/vacuum_varactor_scatter.py`:225; leaf
   `vol4/circuit-theory/ch1-vacuum-circuit-analysis/vacuum-varactor-scatter-operator.md`:76-78)
   — **what no leaf computes is `M`'s SPECTRUM on a closed surface**; the only
   shipped eigenvalue read is the local-node one
   (`src/scripts/vol_4_engineering/vacuum_varactor_scatter_figures.py`:242).
   *(Corrected 2026-08-27: this item previously said the corpus does not compute
   `M` at all, which was false — see the ⚑ in record §3 CAUTION 1.)* The register
   move buys a *relocated question*, not an answer.
2. **Register 4 is ambiguous as written.** Its own gloss
   (`boundary-observables-m-q-j.md`:61) illustrates BALANCE LOCUS with the
   **hollow-vortex balance shell** — a *real-space pressure* balance of two
   opposed scalars (`σ/R` vs `Γ²/R³`, `hollow-vortex-binding.md`:49). The
   virtual neutral is a **port-space phasor** balance. **Different objects; do
   not weld them.** The move is under-determined until register 4 is split or
   unified.

**What must clear before Grant should be asked to rule.**

- **Upstream blocker:** the canon-vs-canon tension over *which sector owns the
  confinement surface* (record §7.3) — `device-circuit-models.md`:165 says A1;
  `def-vyvsn1` + `pair-production-axiom-derivation.md`:102 say T2 at
  `V_yield`. *Which sector owns the wall* must settle before *which register
  the wall belongs to* is meaningful. Tracked separately as
  `2026-08-26-device-circuit-models-165-correction.md`.
- **The standing fence:** `proton-identification.md`:161-165 (2026-08-23)
  already refutes neutrality arguments built on the virtual neutral — *"no
  neutrality/minimum-N argument may be built on it (both uses adversarially
  refuted)"*. The lepton-sector version inherits that burden. Kill condition
  **K8** of the record fires if the same refutation lands here.
- **The audit charter** — record §10, twelve numbered claims A1–A12 with attack
  instructions, and §11, nine kill conditions written so they can fire.

**Honest framing.** This is **peer-with-standard-EE, not an AVE-distinct
chord** — substituting a nodal/symmetry plane for a PEC wall is bread-and-butter
EM cavity practice. The content on offer is **ontological**, and the arc buys
organizing power plus exact negative constraints, and **zero positive
predictions**.
