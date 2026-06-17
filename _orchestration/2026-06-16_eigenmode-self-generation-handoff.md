# Eigenmode Keystone — Lane Handoff v2: the BOUNDARY-OBSERVABLE (𝓜, 𝓠, 𝓙) test

**2026-06-16 · auditor → implementer handoff · SUPERSEDES the v1 "self-assembly of the (2,3)" framing below the line**
**Target:** the one open *physics* keystone — does the electron **exist** as a self-trapped object carrying the three boundary observables 𝓜=m_e, 𝓠=e, 𝓙=ℏ/2 (→ **chord**), or not (→ **echo**)?

---

## 0. Why v1 was wrong-framed (the category error)
v1 (and the whole prior arc — passive breather → NEGATIVE-A, held-BC → DISQUALIFY, genesis-23 → NEGATIVE) tested whether the **interior (2,3) field self-assembles / persists** on a multi-cell lattice. **Canon says that is a category error.** Per `boundary-observables-m-q-j.md` (clm-sjjvhf, Grant 2026-05-14): the interior of a Γ=−1 soliton is **causally disconnected, sub-Nyquist** (k≈6.36/ℓ_node ≫ k_max=0.577/ℓ_node), **phase-space** — *invisible*. *"Forcing a multi-cell propagating-eigenmode test on a bounded interior is a category error; the substrate-correct test measures integrated boundary observables (𝓜, 𝓠, 𝓙)."* So the prior NEGATIVE/DISQUALIFY results measured **invisible interior plumbing** — they are not echo evidence. The substrate-correct test has **never run**.

Two more v1 errors, now corrected (workflow `wbjjtt6o3`, file:line-verified):
- v1 said "use the coupled K4+Cosserat engine" and called the missing engine "the load-bearing gap." But the **engine-capability-map already encodes** that the cubic engines are achiral (`engine-capability-map.md:28,58`: *"a cubic grid is achiral and cannot carry it"* / *"Cubic ↮ chirality"*). v1 made a conflation the map does not.
- `k4_tlm.py`'s "native chirality via A/B twist" is **false** — the A/B swap is a centrosymmetric inversion (`h[mask_B]*=-1`), not handedness (corpus: "by fiat / non-sequitur").

## 1. Why the boundary test dissolves the "engine that doesn't exist"
The §4 substrate-complete engine (chiral srs + coupled stiffening+winding) genuinely **does not exist** (capability-map §4; srs `chiral_lattice.py` has topology but **no coupled V↔ω dynamics** — its "winding" is a *planted* ansatz; the coupled dynamics live on the **achiral** `VacuumEngine3D`/`CoupledK4Cosserat`). **But the existence keystone does not need it:**
- **𝓜, |𝓠|, |𝓙| magnitudes are achiral-OK on a rigid grid.** clm-3bwhad: fixed-`dx` rigid-grid engines are *"CORRECT for substrate-observability purposes — not a limitation, the right physics for boundary-only observability."*
- **The (2,3) topology is knot-theory-forced, independent of substrate chirality** (workflow Cluster D; vol2 torus-knot: coprimality+minimality). Substrate chirality only sets the **sign** (electron vs positron, spin ↑/↓).
- ∴ **chirality is NOT load-bearing for "does the electron exist."** It is a **secondary** question (is the sign *structural-from-srs* or an *injected decoration* — corpus permits the latter). **Parked.**

→ **The existence test runs on the EXISTING achiral coupled `VacuumEngine3D`.**

## 2. State of the tooling (verify before building)
`src/ave/core/boundary_invariants.py`:
- **`compute_M`** — IMPLEMENTED. ∫(n_grav−1)dV, n_grav=S^(−1/4). Ready (works on the scalar V field).
- **`compute_Q`, `compute_J`** — **FIRST-PASS PROXIES ONLY** (Q = local-max soliton count; J = winding proxy). The **rigorous** 𝓠=Link(∂Ω,**F**) and 𝓙=Wind(∂Ω) are **DEFERRED** and, per the docstring, *"require the full Cosserat-coupled engine (doc 113 §5.4)"* — F is the flux field derived from V via the Cosserat coupling. **This deferral is itself proof that nobody has measured boundary 𝓠/𝓙 on a soliton.** Implementing them IS the new build (small, well-scoped, on the existing coupled engine — NOT a new lattice).

## 3. The test — three steps
1. **Self-trap a COUPLED Γ=−1 region** (CP8 emergence: seed the precursor — a transverse-T₂ excitation near ω_C — and let the moving-Γ=−1 boundary form it; **do NOT plant**). This needs the **stiff-wall integrator** resolved (see §4 — the one real upstream gap).
2. **Implement rigorous 𝓠=Link(∂Ω,F) + 𝓙=Wind(∂Ω)** on `CoupledK4Cosserat` (doc-113-§5.4 deferred work; F = Cosserat flux from V). Energy-ledger via the existing `k4_cosserat_coupling.py` `total_hamiltonian()`.
3. **Measure (𝓜, 𝓠, 𝓙)** over the level-set boundary ∂Ω of the self-trapped region. **Existence verdict = does (𝓜, |𝓠|, |𝓙|) → (m_e, e, ℏ/2)?**

## 4. The one real upstream gap (your "no pump")
The self-trap must form on the *coupled* engine. genesis-23 found it "doesn't port" (GAP-2): soft wall under-engages, hard wall the |ω| diverges. **But there is no physical pump** — the substrate is lossless-reactive (Ax 3); a self-consistent self-trap conserves energy. The |ω|→1144 is an **artifact** (explicit integrator unstable on the stiff Γ=−1 wall). **So GAP-2 is the stiff-wall integrator**: use an implicit/symplectic stiff solver and verify the moving-Γ=−1 self-trap engages with the total Hamiltonian **bounded**. This is the gate before the boundary read; it is cheap and decisive.

## 5. Disciplines (applied)
- **clm-sjjvhf** — boundary-not-interior (THE reframe). **clm-3bwhad** — rigid grid is correct for boundary observability.
- **`phase-space-coordinate-check`** — the (2,3) is a phase-space winding *label*; measure the **boundary integer** (𝓠, 𝓙), not the interior real-space field.
- **`substrate-native-check`** — CP8 (seed precursor, don't plant); CP10 (Γ=−1 as a moving reflective **boundary**, not a bulk energy term — validated 0.94 vs 0.26).
- **`ave-conserved-vs-pumped`** — energy-ledger first via `total_hamiltonian()`; "pump" = artifact, not physics; energize-and-lock once.
- **`ave-prereg`** — do NOT re-run the interior-field tests (category error); the ledger is `boundary-observables-m-q-j.md` + genesis-23 + held-BC.
- **`ave-canonical-source`** — import m_e, e, ℏ, ω_C(=C_0/L_NODE), V_yield from `constants.py`.

## 6. Outcomes
- **POSITIVE** — a SEEDED-not-planted self-trap yields (𝓜, |𝓠|, |𝓙|) = (m_e, e, ℏ/2) → the electron exists as a boundary-observable object → **CHORD**. (Sign/handedness then a secondary, separate study.)
- **NEGATIVE** — no self-trap forms (even with a stable integrator), or the boundary integrals miss (m_e, e, ℏ/2) → **ECHO**, cheap-close.
- Adversarial-verify panel on the verdict before it counts.

## 7. Flag-don't-fix opens for Grant
- **GAP-2 = stiff-wall integrator** (physical vs numerical) — your call confirmed the |ω| growth is artifact; the implicit-solver run settles it.
- **Chiral-sign source** — structural-from-srs (the §4 engine, doesn't exist) vs injected decoration (corpus-permitted). Secondary; not needed for existence.
- **Proxy vs rigorous 𝓠/𝓙** — does the verdict need the rigorous Link/Wind, or does compute_M + a sharpened proxy suffice for a first cut?

## First steps (before code)
1. `ave-prereg`: grep `boundary-observables-m-q-j.md`, genesis-23, doc-113-§5.4, and the `boundary_invariants.py` deferral.
2. `pre-test-physics-check`: surface the precursor ontology + the stiff-solver choice to Grant.
3. Pre-register: the stiff-wall-integrator gate + the (𝓜,𝓠,𝓙)→(m_e,e,ℏ/2) discriminator, bins frozen, Rule-11 commit-before-run.
4. Branch off `main`; do NOT inherit `held_bc_winding.py`; build on `VacuumEngine3D`/`CoupledK4Cosserat` + `BoundaryInvariants`.

---
---

## [v1 — SUPERSEDED 2026-06-16: interior-(2,3)-self-assembly framing = the category error clm-sjjvhf names. Retained per Rule 12 for the audit trail; do NOT execute. The validated-state facts in it (verdict-II moving-Γ=−1 self-trap, the "2", charge=helicity) remain correct and are reused above.]

The v1 brief tasked the lane with self-assembling the longitudinal "3" / V-sector fibre in a "coupled K4+Cosserat engine" under a moving Γ=−1 boundary. That engine does not exist (capability-map §4), the test measured invisible interior structure (clm-sjjvhf), and the missing-coupling-operator framing was wrong (the electron-scale operator exists; the planetary one was mis-imported). Superseded by the boundary-observable test above.
