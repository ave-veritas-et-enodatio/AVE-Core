# G0 — the first substrate-complete (cross-firewall) engine is DOUBLE-COUNT-CLEAN — RESULT

> **STATUS: POSITIVE (architectural / structural result) — banked INDEPENDENT of the
> passive-eigenmode production outcome (Grant 2026-06-15).** The (b′) cross-firewall coupling
> (`crystal_engine` V-tank wall ⊗ Cosserat-ω winding) does **NOT** re-inflict the genesis-24
> `w_pol=0` double-count it was authorized eyes-open to risk. Smoke-gate agent `a048bd279cd6741d1`;
> the production driver (`analysis/2026-06-15-eigenmode-driver`) re-runs G0 as build-step-zero.
> Lane: `_orchestration/2026-06-15_passive-eigenmode-solve.md`; FROZEN prereg
> `research/2026-06-15_passive-eigenmode_prereg_FROZEN.md` §5 (G0 spec).

---

## 0. Headline

The minimal **Op14 cross-coupling** between the `crystal_engine` V-tank (A1 breathing wall) and the
**independent Cosserat-ω carrier** (the imposed (2,3) winding) is **double-count-clean**: the
winding stays on the ω-carrier (`w_pol` nonzero) with **zero leak** into the A1 `(V_inc,V_ref)`
breather phasor. This is the architectural pre-condition for the (b′) passive-eigenmode build, and
it is a **real result on its own** — it confirms that the **first substrate-complete engine** (the
exact object the `ave-loop-gap-harness-discipline` anti-loophole guard gates) can be wired **without
re-inflicting the failure mode it was built to avoid**.

---

## 1. The double-count hazard (what G0 guards)

The two-"3"s double-count (`master-equation.md:20`; the banked genesis-24/crystal failure): wiring the
Cosserat micro-rotation (2,3) **winding** into the A1 **breather phasor** `(V_inc,V_ref)` forces
`w_pol=0`, because `V_ref` is a **read-only projection** of the scalar `V`
(`k4_tlm.py:346`: `V_ref = 0.5·ΣV_inc − V_inc`), not an independent DOF. The fix (crystal-graft-v2,
`2026-06-09_crystal-graft-v2_result.md:42-48`): give the winding its **own** Cosserat-ω carrier so
`w_pol` CAN be nonzero. G0 tests that the (b′) coupling **preserves** this orthogonality.

---

## 2. Result — coupled run, N=48, R=10, r=4 (extractor-matched traveling-(2,3) plant)

| step | w_tor | w_pol | is_2_3 | **V_ref-leak (rel)** | \|V\|max |
|---:|---:|---:|:---:|---:|---:|
| 0 | 2 | 3 | True | **2.0e-16** | 0.815 |
| 10 | 2 | 3 | True | **4.3e-16** | 0.773 |
| 30 | 2 | 3 | True | **2.0e-16** | 0.555 |
| 50 | 2 | 3 | True | **3.9e-16** | 0.287 |
| 59 | 2 | 2 | False | **3.9e-16** | 0.213 |

- **`w_pol` never collapses to 0** (the genesis-24 signature is ABSENT). It holds at 3 for steps
  0–50; the step-59 drift to 2 is **NOT coupling-induced** — the **decoupled control (κ̃→0)** gives
  the identical late drift `(2,2)`, so it is free-evolution numerical relaxation of the unconfined
  ω-knot as `|V|` decays, independent of the coupling.
- **V_ref-leak ≤ 4.3e-16** at every checkpoint (tol 1e-10) — machine precision. The winding is
  **wholly absent** from the A1 breather phasor; reading `extract_2_3_omega_fast` **directly off the
  V-tank phasor** returns `(0,0)`, `is_2_3=False`. The winding lives **only** on `omega`.

---

## 3. How the coupling is wired (auditable / reusable)

- **Coupling:** `cross_sector_coupling.trilinear_buckle_forces(V, w, omega, g_wall, dx, kappa_tilde=κ̃)`
  (`cross_sector_coupling.py:110-139`, CrystalGraft-v4): `f_V = −κ̃ g (w·∇×ω)` onto the V-tank;
  `f_omega = −κ̃ ∇×(g V w)` onto the **independent** ω-carrier; **`f_w ≡ 0`**. `g_wall` =
  `crystal_engine._front_window()` — the saturation-front boundary shell (**Γ rendered as a BC, not
  a bulk term**, CP10). **Nothing is ever written to `(V_inc,V_ref)`.**
- **Coupling-binding declaration (`consistency-vs-emergence` / `ave-discrimination-check`):** the
  coupling imports `KAPPA_TILDE = 6/5` (`cross_sector_coupling.py:23`) — **α-FREE** (pure topology);
  `ALPHA` is imported only to *declare* it is NOT a coupling input.
- **Winding read:** `fast_winding_extractor.extract_2_3_omega_fast(omega, omega_dot, R, r, N)` — torus
  phasor coords on the ω-tank LC pair (A46 phase-space, not real-space).

---

## 4. Representation-capability flag (`ave-representation-capability-check`) — Grant-adjudicated

The brief-named seeder `initialize_electron_2_3_sector` writes a **z-flat rotor** (ω·ê_z≡0) →
`extract_2_3_omega_fast`'s toroidal projection is **structurally w_tor=0** (a G4 plant/read MISMATCH,
NOT a coupling collapse). That seeder is **corpus-DEPRECATED for the electron** — its own docstring
(`cosserat_field_3d.py:932-945`) flags the real-space (2,3) write as "misleading", valid for the
**proton 5₁/5₂**, and redirects to the unknot seeder. **Grant 2026-06-15: use the traveling-(2,3)**
(`planted_winding_field(traveling)` — the G4-certified carrier, `test_unified_quadrature_v7.py:142,153`),
which G0 used here. The electron is the **0₁ unknot** carrying the (2,3) as a phase-space winding
(`theory.md:16`); the production driver additionally **asserts the 0₁ unknot envelope** (the
third-time wrong-object guard).

---

## 5. Classification + scope (`consistency-vs-emergence`)

- **Class: STRUCTURAL / ENGINEERING (consistency).** G0 confirms the coupling **preserves** the
  A1⊥T2 orthogonality invariant — it is **not** an emergence/existence test of the electron.
- **Independent of the production physics.** Whether the passive winding-protected breather EXISTS
  (the keystone, F1/F2/F4 in the production driver) is a **separate** question; G0 stands regardless
  of that outcome.
- **What G0 does NOT show:** it does not show the hybrid mode is stable, high-Q, or that it exists —
  only that the cross-firewall coupling is double-count-clean. G0 is the orthogonality smoke-gate
  (build-step-zero), not the production discriminator.

---

## 6. Significance — the architectural precedent

This is the **first substrate-complete (cross-firewall) engine** in the program — the union of the
A1 stiffening-wall firewall (`crystal_engine`) and the Cosserat-chiral firewall (the ω-carrier),
which the harness discipline gates behind Grant sign-off. G0 establishes that the precedent
Grant authorized (eyes-open) **does not re-inflict the genesis-24 double-count** at its riskiest
seam. The coupling is reusable by the production driver and any future substrate-complete work — with
the standing caution (Grant) that future lanes will reach for this engine and **must not over-trust
it**: G0 certifies *orthogonality*, not *physics*.
