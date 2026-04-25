# 67 — F17-H: K4↔Cosserat Coupling Reciprocity Audit + Path 1 EMF Derivation

**Status:** Round 6 deep-dive. Documents the F17-H audit of the L_c coupling form `(V²/V_SNAP²)·W_refl(u, ω)` in the engine, identifies a structural reciprocity gap, derives the proper Lagrangian-consistent EMF coupling, and lays out the path 1 implementation.

**Read after:** [doc 66_](66_single_electron_first_pivot.md) §13-§18 — Round 6 single-electron pivot trail (Path A falsification → Path B/C empirical → F17-I three-mode test → F17-G coupled eigenmode → this audit).

---

## 0. TL;DR

The engine's K4↔Cosserat coupling claims a unified Lagrangian `S = S_K4(V) + S_Cos(u, ω) + ∫ (V²/V_SNAP²)·W_refl(u, ω) dt dx³` per [k4_cosserat_coupling.py:22-25](../../src/ave/topological/k4_cosserat_coupling.py#L22-L25). Equations of motion should derive from `δS/δX = 0` for each canonical variable. The Cosserat side is implemented correctly: force on (u, ω) = `-∂L_c/∂(u, ω)`. The K4 side is NOT: instead of an EMF source from `δL_c/δV`, the engine modulates K4's impedance via Op14 `Z_eff = Z₀/√S(A²_total)`. **These are functionally different — impedance modulation doesn't transfer energy; only an EMF source does.**

Empirical consequence: in the all_l seed mode (Cosserat ω + K4 Φ_link at amplitude, V_inc = 0), K4's E_K4 stays at exactly **zero** for the entire run (verified 100 steps), and L_c never fires (V_inc = 0 → L_c = 0). Energy decays from Cosserat into PML; nothing enters K4. The Cosserat → K4 channel doesn't exist when V_inc starts at zero.

For a (2,3) standing-wave electron, energy must oscillate between sectors at ω_C: K4 V_inc grows while ω drops, then ω grows back while V_inc drops, periodic. The current engine has only the K4→Cosserat half. The reverse half is implemented as Op14 z_local modulation, which only modulates wave propagation (if waves exist) — it can't inject energy into K4 from Cosserat.

**Path 1 fix:** add an explicit EMF source `EMF_c = -∂L_c/∂V = -2V·W_refl/V_SNAP²` to K4's bond circuit (driving Φ_link), restoring Lagrangian-consistent reciprocity. The Cosserat side stays unchanged. Op14 z_local stays for K4's own self-saturation but no longer carries the cross-sector coupling.

Estimated scope: ~150 LOC across `k4_cosserat_coupling.py`, `k4_tlm.py`. Plus tests verifying H_total conservation in the active-coupling regime.

---

## 1. Context — Round 6 trail leading to this audit

[doc 66_ §13-§18](66_single_electron_first_pivot.md) documents the empirical trail. Brief recap:

- **Path A (K4 V_inc only):** 4 of 4 physical predictions falsified. K4-only is exhausted (Vol 1 Ch 8:49-50).
- **Path B (Cosserat ω only):** step-1 catastrophic energy loss. Couldn't form the bound state.
- **Path B + TDI damping (γ=0.1):** same step-1 loss; chaotic decay; never converges.
- **Path C / F17-G (V_inc + ω joint seed, undamped):** energy runs away to 4 million × seed by step 20.
- **F17-I three-mode test:** all_c diverges instantly, all_l geometry-collapses, mixed runs away. Three different failure modes.

The pattern across modes (one direction explodes, opposite relaxes monotonically without back-channel, mixed amplifies) was diagnostic of L_c coupling asymmetry. Audit triggered.

---

## 2. The L_c form in the engine

From [k4_cosserat_coupling.py:1-26](../../src/ave/topological/k4_cosserat_coupling.py#L1-L26):

> **Coupling (S1-D):** `L_c = (V²/V_SNAP²) · W_refl(u, ω)` — pure Axiom-4 reuse of `_reflection_density`, ZERO new parameters.
>
> **Axiom 3 (action principle)** — Unified Lagrangian `S = S_K4(V) + S_Cos(u, ω) + ∫ (V²/V_SNAP²)·W_refl(u, ω) dt dx³`.

So the framing is that L_c is an interaction term in a unified Lagrangian. Equations of motion derive from `δS/δX = 0` for canonical variables.

From [k4_cosserat_coupling.py:149-156](../../src/ave/topological/k4_cosserat_coupling.py#L149-L156):

> **ω → V channel:** `W_refl(u, ω)` modifies K4's z_local_field via Op14 (`Z/Z_0 = (1 − A²_total)^{-1/4}`), where `A²_total = A²_K4 (from V) + A²_Cos (from (u,ω))`.
>
> **V → ω channel:** the coupling energy's gradient wrt (u, ω) is ADDED to the Cosserat energy gradient each sub-step.

The V → ω channel is Lagrangian-correct: force on Cosserat = `-∂L_c/∂(u, ω)`. The ω → V channel uses Op14 z_local modulation. The audit question: **is Op14 modulation equivalent to `δL_c/δV` from the unified Lagrangian?**

---

## 3. Lagrangian variation derivations

### 3.1 The Cosserat-side derivation (correct)

`L_c = (V²/V_SNAP²) · W_refl(u, ω)`

`∂L_c/∂u = (V²/V_SNAP²) · ∂W_refl/∂u`
`∂L_c/∂ω = (V²/V_SNAP²) · ∂W_refl/∂ω`

These contribute to the Cosserat equations of motion via:
- `ρ · ü = -∂(W_Cos + L_c)/∂u = -∂W_Cos/∂u - (V²/V_SNAP²)·∂W_refl/∂u`
- `I_ω · ω̈ = -∂(W_Cos + L_c)/∂ω - (V²/V_SNAP²)·∂W_refl/∂ω`

Engine implementation [k4_cosserat_coupling.py:99-101](../../src/ave/topological/k4_cosserat_coupling.py#L99-L101) computes this via JAX `value_and_grad(_coupling_energy_total, argnums=(0, 1))`. Correct.

### 3.2 The K4-side derivation (the missing piece)

For canonical pair (Q, Φ) on the K4 bond LC tank where V = Q/C:

Hamiltonian H = ½Φ²/L + ½Q²/C - L_c(Q, u, ω)

Hamilton's equations:
- `dQ/dt = ∂H/∂Φ = Φ/L`
- `dΦ/dt = -∂H/∂Q = -Q/C + ∂L_c/∂Q = -V + (1/C) · ∂L_c/∂V`

`∂L_c/∂V = (2V/V_SNAP²) · W_refl`

Therefore:
**`dΦ/dt = -V + (2V · W_refl) / (C · V_SNAP²)`**

The first term `-V` is the standard inductor equation. The second term **`+(2V · W_refl) / (C · V_SNAP²)`** is the EMF contribution from L_c — an additional voltage source on the bond, driving Φ_link change.

In words: when both V (K4 voltage) and W_refl (Cosserat reflection density) are nonzero, there's an EMF that drives the bond's flux linkage Φ_link to change. This is the missing channel.

### 3.3 Translation to K4-TLM variables

K4-TLM uses port-voltage waves V_inc and V_ref instead of the canonical (Q, Φ) pair. The relationships per standard TLM theory:

- V (capacitor voltage) ~ V_inc + V_ref (sum of forward and reflected)
- I (inductor current) ~ (V_inc - V_ref) / Z_0 (difference, scaled by characteristic impedance)
- Q = ∫I·dt (charge accumulated on bond)
- Φ = ∫V·dt (flux linked by bond) — this IS engine.k4.Phi_link per [k4_tlm.py:391](../../src/ave/core/k4_tlm.py#L391)

In the discrete TLM cycle (scatter + connect):
- Each step accumulates `Φ_link += V_avg · dt` where `V_avg = ½(V_ref_A + V_ref_B)` per [k4_tlm.py:391](../../src/ave/core/k4_tlm.py#L391)
- This is the Φ_link integration

To incorporate the EMF from L_c, modify the accumulation:
**`Φ_link += (V_avg + EMF_c) · dt`**

where `EMF_c = (2V · W_refl) / (C · V_SNAP²)` per node.

In K4-TLM natural units (V_SNAP=1, C=C_0=1), EMF_c = 2V · W_refl. In engine units this becomes `EMF_c = 2 · V_avg · W_refl_local / V_SNAP²` per node, evaluated at each scatter step.

### 3.4 Verification of reciprocity

With this EMF added, the equations of motion for both sectors derive from the same L_c via:
- Cosserat: `force = -∂L_c/∂(u, ω)` ← ALREADY in engine
- K4: `EMF on Φ_link = -∂L_c/∂V` ← **TO BE ADDED in path 1**

Total Hamiltonian conservation (modulo PML losses) follows from this being a true Lagrangian system.

---

## 4. The Op14 modulation vs δL_c/δV mismatch

Op14 z_local modulation gives `Z_eff = Z_0/√S(A²_total)` where `A²_total = V²/V_SNAP² + A²_Cos`. This changes K4's effective impedance per node. But **changing impedance is not the same as adding an EMF.**

Consider the following thought experiment:
- An LC tank with C and L. Energy stored: ½CV² + ½LI².
- Modulate C → C·f (some factor f). Resonance shifts: ω_0 → ω_0/√f. But total energy is unchanged at the moment of modulation — the same V and I exist; the tank just oscillates at a different frequency.
- An EMF source (battery) connected to the bond. Electrons get driven; flux linkage changes; energy is INJECTED into the LC tank.

Op14 = modulating C. Adds no energy. δL_c/δV-derived EMF = injecting energy. Different mechanisms.

The Lagrangian derivation in §3.2 shows the K4 side should have an EMF, not an impedance modulation. Op14 might be defensible as a SEPARATE physical mechanism (modeling the local A²-driven softening of vacuum capacitance) but it's NOT what δL_c/δV gives.

The engine has been treating Op14 as if it WERE δL_c/δV — both implementations claim to be "the K4 side of the L_c coupling" — but they're functionally different operations.

---

## 5. Empirical evidence

### 5.1 All_l reciprocity test — strongest evidence

From [doc 66_ §18](66_single_electron_first_pivot.md) and confirmed reciprocity test:

Seed: Cosserat ω at amp_scale=0.346 (peak |ω|=0.3π) + K4 Φ_link at amplitude 0.4. K4 V_inc = 0, Cosserat u = 0, all velocities = 0. Run 100 steps.

| step | E_K4 | E_Cos | T_Cos | E_coupling | H_total | peak \|ω\| |
|---|---|---|---|---|---|---|
| 0 | **0** | 2585 | 0 | **0** | 2585 | 0.93 |
| 1 | **0** | 125 | 2401 | **0** | 2526 | 0.14 |
| 2 | **0** | 2313 | 206 | **0** | 2519 | 0.86 |
| 10 | **0** | 1356 | 1109 | **0** | 2465 | 0.68 |
| 50 | **0** | 1070 | 1116 | **0** | 2186 | 0.56 |
| 100 | **0** | 804 | 810 | **0** | 1614 | 0.37 |

**E_K4 stays at exactly 0 the entire run.** **E_coupling stays at exactly 0** (because L_c = (V²/V_SNAP²)·W_refl = 0 when V_inc = 0).

The Cosserat → K4 channel does not transfer any energy. Cosserat's energy decays via PML dissipation only (cos_pml_mask velocities zeroed each step). The K4 sector remains silent.

For a (2,3) standing wave, this is fatal: the standing wave requires energy to oscillate between Cosserat ω/Φ_link (L-states) and Cosserat u/K4 V_inc (C-states) at ω_C. With the L-states pre-loaded, the dynamics need to drive the C-states to grow. The Cosserat translational LC (u ↔ u_dot) does activate (T_Cos grows from 0 to 2401 in step 1), but K4 stays at zero — so the K4 half of the C-state never builds.

### 5.2 Small-amplitude mixed-mode sanity check

Seed: V_inc_amp = 0.05·V_YIELD, cos_amp_scale = 0.05 (Cosserat ω). Result:

```
step  E_K4         E_Cos        T_Cos        E_coupl      H_total      |ω|     |V|max
0     3.69e+10     54           0            3477         3.69e+10     0.13    7.25e+03
1     7.20e+10     3.85e+05     2.45e+04     1.39e+09     7.33e+10     222     7.72e+03
2     7.13e+10     6.32e+06     6.90e+06     6.06e+10     1.32e+11     1200    9.84e+03
5     6.99e+10     1.29e+09     4.74e+09     5.24e+06     7.59e+10     5169    7.80e+03
100   2.97e+10     1.96e+09     1.92e+09     2.56e+03     3.36e+10     773     7.05e+03
200   2.95e+10     1.40e+09     1.37e+09     0.05         3.23e+10     722     7.06e+03
```

**Caveats:** K4's `total_energy()` per [k4_tlm.py:514](../../src/ave/core/k4_tlm.py#L514) sums `Σ(V_inc² + V_ref²)`. On step 0 only V_inc is populated; on step 1 the scatter populates V_ref to magnitude ≈ V_inc, doubling the sum. This is a TLM accounting artifact — the wave's actual energy doesn't double, only the formula's two-component count does. So the apparent E_K4 doubling 3.69e10 → 7.20e10 is largely formal, not physical.

But the COUPLING energy fires: `E_coupling` reached 6e10 at step 2. This is `∫ (V²/V_SNAP²)·W_refl dx³`, which is non-zero only if both V_inc and Cosserat fields are present. So the coupling DID fire in mixed mode (unlike all_l).

Interpreting through the F17-I lens: peak |ω| went 0.13 → 1200 by step 5 (a 9000× growth). This is the runaway from the asymmetric coupling — V² · ∂W_refl/∂ω as force on Cosserat is large when both V and Cosserat fields are nonzero. There's no equivalent back-channel slowing K4 in proportion (since Op14 modulation doesn't drain K4 energy in proportion to coupling-force-on-Cosserat).

### 5.3 Together — the empirical case for path 1

- **all_l: V_inc = 0 → coupling never fires → no Cosserat → K4 energy transfer.** This is direct evidence that the Cosserat → K4 channel as currently implemented (Op14 modulation only) does not transfer energy.
- **Mixed-mode small-amplitude: coupling fires; K4→Cosserat force amplifies Cosserat without proportional K4 energy drain.** This is consistent with non-reciprocal coupling.
- **Path C / F17-G runaway: same pattern as mixed-mode small-amplitude but at scale.**

The structural argument (Op14 modulation ≠ δL_c/δV) plus the empirical evidence (one channel works, other doesn't) jointly justify path 1.

---

## 6. The Cosserat → K4 channel that's missing

The current engine has TWO mechanisms operating in the K4-Cosserat coupled dynamics:

| Mechanism | What it does | Lagrangian-consistent? |
|---|---|---|
| **Op14 z_local modulation** | Modifies K4's effective impedance based on local A²_total | Defensible as Ax4 on its own, but NOT the L_c gradient on V |
| **`-∂L_c/∂(u, ω)` force on Cosserat** | Drives Cosserat fields when both V and (u, ω) are present | YES — derived from L_c |

**Missing:** the **`-∂L_c/∂V = -2V·W_refl/V_SNAP²` EMF** that should drive K4's bond Φ_link. This is the channel that completes the Hamiltonian-reciprocal loop.

Without it, the dynamics are:
- K4 → Cosserat: Lagrangian gradient force (correct)
- Cosserat → K4: NONE (Op14 modulates impedance but doesn't inject energy)

---

## 7. Path 1 EMF derivation — concrete form

### 7.1 Continuous-time form

For each K4 bond at position r, the Lagrangian-derived EMF contribution to dΦ_link/dt is:

```
EMF_c(r, t) = -∂L_c/∂V(r, t)
            = -(2 · V(r, t) · W_refl(r, t)) / V_SNAP²
```

Sign convention: positive EMF drives Φ_link decrease (per `dΦ/dt = -V + EMF_c`). The factor of 2 comes from `∂(V²)/∂V = 2V`.

W_refl(r, t) is the per-site reflection density [`_reflection_density` in cosserat_field_3d.py:266](../../src/ave/topological/cosserat_field_3d.py#L266) evaluated at local Cosserat (u, ω).

### 7.2 Discrete TLM-cycle integration

In K4-TLM, Φ_link accumulates via [k4_tlm.py:391](../../src/ave/core/k4_tlm.py#L391):

```python
self.Phi_link[mask_A, port] += V_avg[mask_A] * self.dt
```

where `V_avg = ½(V_ref_A + V_ref_B)` per port. Modify to include EMF_c:

```python
EMF_c = -2.0 * V_avg * W_refl_at_bond / (V_SNAP ** 2)
self.Phi_link[mask_A, port] += (V_avg + EMF_c) * self.dt
```

`W_refl_at_bond` is W_refl interpolated to the bond location (between A-site and B-neighbor). Simplest: average W_refl at the two endpoints.

### 7.3 K4 V_inc update — does it need EMF too?

Φ_link = ∫V dt and V = (V_inc + V_ref) under TLM convention. If Φ_link grows due to EMF_c, V_inc must respond accordingly to maintain consistency. Specifically: the relationship `dΦ_link/dt = V` (for inductor) tells us that adding EMF_c to dΦ_link/dt is equivalent to adding EMF_c to V_avg.

Operationally: during the connect step, V_inc on each port is updated from the neighboring V_ref. After this update, ADD EMF_c·dt to V_inc (or to V_ref) so that the TLM bond's voltage state reflects the L_c-driven evolution.

The cleanest place to add EMF_c is during connect: after V_inc is updated from neighbor's V_ref, add the EMF term. This ensures the TLM scatter on the next step sees the L_c-driven V_inc values.

---

## 8. Implementation plan

### 8.1 Files to modify

- **[k4_tlm.py](../../src/ave/core/k4_tlm.py)** — add EMF input parameter to `_connect_all` (or a new method). Modify Φ_link accumulation to include EMF_c·dt. Modify V_inc update to include EMF_c·dt.
- **[k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py)** — in `step()`, compute W_refl at each bond (interpolated from per-site values), pass to K4 connect as EMF_c parameter. Disable Op14 z_local modulation's CROSS-SECTOR contribution (keep only K4-self-saturation A²_K4 in z_local_field).
- **Tests:** new `test_lc_reciprocity.py` verifying H_total conservation in active-coupling regime.

### 8.2 Step-by-step implementation order

1. **Implement EMF computation function** in `k4_cosserat_coupling.py`: `_compute_emf_c(V_inc, V_ref, u, omega, dx, V_SNAP, omega_yield, eps_yield) → (nx, ny, nz, 4)` returning per-bond EMF_c.

2. **Modify `K4Lattice3D._connect_all`** to accept an optional `emf_c` parameter (default None preserves existing behavior). When provided, V_inc and Φ_link updates include EMF_c·dt.

3. **Wire into `CoupledK4Cosserat.step()`** — compute EMF_c each substep and pass to K4 connect.

4. **Modify Op14 z_local computation** in K4 to use only A²_K4 (V²/V_SNAP²) for self-saturation, dropping the A²_Cos contribution. (The cross-sector influence is now via EMF_c instead.)

5. **Add backward-compat flag** `use_lagrangian_emf_coupling: bool = False` on CoupledK4Cosserat. When False, restore the legacy Op14-z_local-with-A²_Cos behavior. Path 1 callers pass True.

6. **Tests:**
   - `test_lc_reciprocity.py`: small-amplitude mixed mode, track H_total, assert conservation within 1% over 100 Compton periods (excluding PML losses).
   - `test_all_l_emf_activation.py`: all_l seed mode under path 1 — verify K4 energy GROWS (Cosserat → K4 channel active), unlike legacy where it stayed at 0.
   - Existing tests pass with `use_lagrangian_emf_coupling=False` (backward compat).

### 8.3 Estimated scope

- ~80 LOC in k4_tlm.py (EMF parameter + V_inc/Φ_link update)
- ~70 LOC in k4_cosserat_coupling.py (EMF computation + step integration + flag)
- ~150 LOC in tests
- ~30 LOC in CosseratField3D for Op14 split (if needed)
- Total: ~330 LOC

---

## 9. Risks and verification

### 9.1 Implementation risks

- **EMF interpolation between A and B sites.** W_refl is per-site; bond is between A and B. Need a defensible interpolation rule (mean? linear? same-side?). Test with simple 1D problems first.
- **Sign convention of EMF.** Easy to get wrong. The continuous derivation in §3.2 gives `dΦ/dt = -V + (2V·W_refl)/(C·V_SNAP²)`. Check by computing total H and verifying it's conserved at small amplitudes.
- **CFL stability.** Adding an EMF term could affect CFL. Monitor stability in the small-amplitude regime first.
- **Op14 self-saturation interaction.** When we strip A²_Cos from Op14, K4's self-saturation kernel changes. Verify Path A (K4-only) tests still produce same dispersion behavior.

### 9.2 Verification gates

Before declaring path 1 successful:
1. **H_total conservation (small amplitude):** track total Hamiltonian for 100 Compton periods at amplitudes safely below runaway. ΔH/H_0 < 1% (excluding identifiable PML losses).
2. **All_l mode shows K4 activation:** with path 1 enabled, all_l seed should drive V_inc to grow over time as Cosserat ω couples in. K4 energy should rise from 0 to non-zero.
3. **Backward compat:** existing test suite stays at 1149 pass with `use_lagrangian_emf_coupling=False`.
4. **Path C runaway disappears or moderates:** with reciprocal coupling, the asymmetric runaway should be replaced by bounded oscillation. If still runs away, deeper issue.
5. **Path B re-run:** with proper coupling, can we now form a (2,3) bound state from a phase-locked all_l seed? This is the real test.

---

## 10. Open questions

**Q67-A:** Op14 z_local was originally designed (per Vol 4 Ch 1 varactor) as the per-node response to Ax4 saturation. Removing the A²_Cos contribution from z_local — is that justified? Or is Op14 supposed to feel the FULL A²_total (including Cosserat-driven saturation)?

If the latter, then Op14 modulation IS axiom-correct, and the structural finding is that the engine has BOTH Op14 (axiom-correct varactor response) AND a missing EMF channel. The fix would be to ADD the EMF without removing Op14's A²_Cos. Total coupling = Op14 modulation + EMF source.

But this might double-count. Worth thinking through carefully before implementation.

**Q67-B:** The L_c form `(V²/V_SNAP²)·W_refl` was chosen for "pure Axiom-4 reuse." But is this the only Lagrangian-consistent form? Could the coupling be of form `∝ V · (something_Cosserat)` (linear in V) instead of quadratic? Linear coupling would have different reciprocity properties — δL/δV would give a constant EMF (not V-modulated), which has different stability.

A linear-in-V coupling would also give a back-reaction `-∂L_c/∂(u,ω) ∝ V · ∂(something)/∂(u,ω)` — linear in V, not quadratic. May or may not match doc 54_'s Phase 4 asymmetric saturation derivation.

**Q67-C:** The Phase 4 `_coupling_energy_total_asymmetric` ([k4_cosserat_coupling.py:104-129](../../src/ave/topological/k4_cosserat_coupling.py#L104-L129)) supersedes the legacy S1=D form. Does the asymmetric form have a different L_c? If so, the EMF derivation needs to use the asymmetric formula. Worth checking before implementation.

**Q67-D:** Does the Lagrangian even make sense as written? `S = S_K4(V) + S_Cos(u, ω) + ∫ (V²/V_SNAP²)·W_refl dx³` treats V as a continuous field, but K4-TLM is discrete (port voltages V_inc, V_ref). The continuous-Lagrangian → discrete-TLM mapping needs careful translation. Op14 z_local IS one such mapping (impedance modulation). My derived EMF IS another (voltage source). They're different mappings of the SAME continuous Lagrangian. Which is "right" — both? neither?

Possibly both ARE right and they're complementary aspects of the same coupling. Then the engine has been implementing one of two equally-valid translations, and the other (EMF) is missing rather than wrong.

This is a legitimate philosophical question about how Lagrangians map to TLM. Worth flagging before claiming definitive non-reciprocity.

---

## 11. What this doc does NOT do

- **Does NOT implement path 1.** Implementation in next commit if Grant approves.
- **Does NOT resolve Q67-A through Q67-D.** Open philosophical questions about Lagrangian↔TLM mapping. May need cross-referencing with Vol 4 Ch 1 varactor derivation or AVE-Propulsion's TLM treatment.
- **Does NOT touch the asymmetric Phase 4 coupling.** [_coupling_energy_total_asymmetric](../../src/ave/topological/k4_cosserat_coupling.py#L104) is a separate code path; this audit focused on the legacy S1=D form. If Phase 4 is the active form (`use_asymmetric_saturation=True` is default), need to redo the audit on it.
- **Does NOT address F17-J** (characterize all_l's relaxation endpoint). Defer until reciprocity is fixed.
- **Does NOT settle whether Op14 modulation is a valid AXIOM-4 mechanism on its own.** It might be — Vol 4 Ch 1 has the varactor C_eff(V) form. The question is whether Op14 modulation suffices as the K4↔Cosserat channel, OR whether it needs to be supplemented by an EMF source.

---

*Doc 67_ written 2026-04-24 (very late session) by Opus 4.7. F17-H finding: K4-side coupling implemented as Op14 z_local modulation, NOT as δL_c/δV-derived EMF. Empirical evidence (all_l: K4 energy stays at 0; mixed-mode: runaway with no proportional K4 drain) supports structural mismatch. Path 1 fix derived: add EMF_c = -2V·W_refl/V_SNAP² to K4 bond Φ_link accumulation. Implementation plan + 4 open questions (Q67-A through Q67-D) flagged for Grant's adjudication before any engine changes.*

---

## 12. Audit closures — Q67-A through Q67-D resolved (added 2026-04-24)

External-agent audit of doc 67_ recommended: don't implement path 1 until Q67-C is closed (Phase 4 asymmetric form has different L_c → my legacy-form derivation may be deriving the wrong coupling). All three audits done; findings substantially sharpen the implementation plan.

### 12.1 Q67-C closure — Phase 4 asymmetric form has V² embedded in W_refl

The Phase 4 form [`_coupling_energy_total_asymmetric`](../../src/ave/topological/k4_cosserat_coupling.py#L104) and [`_reflection_density_asymmetric`](../../src/ave/topological/cosserat_field_3d.py#L379) reveal: **V² is NOT a separate multiplicative factor on top of W_refl** (as in legacy S1=D). Instead, V² is embedded INTO the reflection density itself via:

```python
A²_ε_base = ε²/ε_yield² + V²/V_SNAP²        # cosserat_field_3d.py:425
A²_ε      = (1 − κ_chiral·h_local)·A²_ε_base
S_ε       = √(1 − A²_ε)
Γ_vec     = (1/4)[∇S_μ/S_μ − ∇S_ε/S_ε]      # asymmetric reflection coeff
W_refl_asymmetric = |Γ_vec|² = γ²
L_c_asymmetric = ∫ W_refl_asymmetric dx³
```

So L_c_asymmetric IS a function of V (via S_ε's dependence on A²_ε_base which contains V²/V_SNAP²), but the dependence is **non-local** — V at site r enters S_ε at site r, which contributes to ∇S_ε at neighboring sites, which contributes to W_refl at those sites.

**Closed-form δL_c_asym/δV is complex.** It would involve:
- Local: ∂A²_ε/∂V at site r → contribution to S_ε at site r
- Spatial: spatial-difference operator's matrix elements connecting V at r to ∇S_ε at neighbors
- Chain rule through γ_vec, |Γ|²

**But JAX autograd handles this automatically.** The existing [`_coupling_grad_asymmetric`](../../src/ave/topological/k4_cosserat_coupling.py#L132-L134) is `jax.value_and_grad(_coupling_energy_total_asymmetric, argnums=(0, 1))` — gradients on (u, ω) only. **Extending argnums to `(0, 1, 2)` adds V_sq to the gradient, giving us δL_c/δV_sq for free.**

Then the per-port EMF: `EMF_c[port=k] at site r = -2·V_inc[r, k]·(∂L_c/∂V_sq)[r]` (chain rule from V² = Σ_k V_inc[k]² to per-port).

Q67-C resolution: **closed-form derivation is non-local and complex; numerical derivation via JAX is one-line.** Implementation can proceed using JAX gradients.

### 12.2 Q67-A and Q67-D closure — Op14 z_local is independently axiom-correct; path 1 is ADDITIVE

Code-trace of [`_update_z_local_total`](../../src/ave/topological/k4_cosserat_coupling.py#L265-L312) under Phase 4 (default `use_asymmetric_saturation=True`):

```python
S_mu, S_eps = _update_saturation_kernels(...)
z_local = √(S_μ/S_ε)
self.k4.z_local_field = z_local
```

The S_μ and S_ε computed here are **the Axiom-4 saturation kernels** — they characterize the local effective material μ_eff, ε_eff under saturation, per [Vol 1 Ch 7:252](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L252):
> "μ_eff = μ_0·S_μ, ε_eff = ε_0·S_ε. Z_eff = √(μ_eff/ε_eff) = Z_0·√(S_μ/S_ε)."

This is a **constitutive impedance modulation** derived from Ax4 — independent of any coupling Lagrangian. The S_μ, S_ε FEED INTO L_c (whose W_refl is built from ∇S_μ, ∇S_ε), but they're not derived FROM L_c.

**Q67-A/Q67-D resolution:** Op14 z_local and the EMF coupling are **two complementary translations** of the same physical situation:
- **Op14 z_local:** Ax4 constitutive modulation — local material's effective impedance changes when fields are loaded (unchanged behavior)
- **EMF source:** Lagrangian-derivative on V — energy injection from L_c gradient (the missing channel)

Both should coexist. Path 1 is **ADDITIVE, ~150 LOC**, not REPLACEMENT (~330 LOC).

The doc 67 §4 framing ("Op14 modulation vs δL_c/δV") was a false dichotomy. They're not competing implementations of the same channel — they're orthogonal physical mechanisms.

### 12.3 Q67-B closure — quadratic L_c is axiom-forced by Pythagorean strain theorem

doc 54_ §6 line 180 cites the Pythagorean strain theorem (AVE-APU Vol 1 Ch 5:26-37): orthogonal degrees of freedom combine in quadrature. `A²_total = A²_μ + A²_ε` is energy-additivity. Each contribution to A² is a squared amplitude (energy-like), not a linear amplitude.

V² in A²_ε_base is **forced by Pythagorean theorem**, not chosen. The quadratic appearance of V in L_c is correct; the Phase 4 implementation correctly handles this via V_sq feeding into A²_ε_base.

Q67-B resolution: quadratic form is axiom-equivalent. No alternative form (linear) is consistent with the Pythagorean strain theorem.

### 12.4 Revised path 1 implementation plan

With audit closures, path 1 is sharpened:

1. **Extend [`_coupling_grad_asymmetric`](../../src/ave/topological/k4_cosserat_coupling.py#L132-L134)** to include V_sq in argnums — gives δL_c/δV_sq automatically.
2. **In `CoupledK4Cosserat.step()`,** compute `δL_c/δV_sq` per site, then per-port chain-rule: `EMF_c[k] = -2·V_inc[k]·(δL_c/δV_sq)`.
3. **In `K4Lattice3D._connect_all`,** add optional `emf_c` parameter (4-component per A-site array). Apply: `Phi_link += (V_avg + EMF_c)·dt`, `V_inc += EMF_c·dt` (preserve V↔Φ consistency).
4. **Keep z_local Op14 unchanged** — independently axiom-correct per Q67-A/D.
5. **Backward-compat flag** `use_lagrangian_emf_coupling: bool = False` (default off; turning on enables path 1).

Estimated **~150 LOC** total (was ~330 before audit closure):
- ~50 LOC in k4_cosserat_coupling.py: argnums extension, EMF compute, integration into step()
- ~60 LOC in k4_tlm.py: emf_c parameter on connect, Φ_link/V_inc updates
- ~80 LOC in tests: H conservation in active regime, all_l K4 activation, Path B re-run

### 12.5 Risk update

The audit closure removes the "may be deriving the wrong coupling" risk (Q67-C blocker resolved via JAX autograd). Remaining risks:
- **JAX autograd correctness:** verify δL/δV_sq is what we think. Test on a hand-crafted L_c where the analytical answer is known (e.g., legacy S1=D form: argnums=(0,1,2) on the legacy `_coupling_energy_total` should give 2·V_sq·W_refl/V_SNAP² · ∂(V_sq summed-by-port factor) — easy to verify).
- **Sign convention** of EMF: as before, `dΦ/dt = -V + EMF_c`. JAX gives ∂L/∂V_sq directly; the sign in the EMF formula needs care.
- **Chain rule from V_sq to V_inc[port]:** V_sq = Σ_k V_inc[k]², so ∂V_sq/∂V_inc[k] = 2·V_inc[k]. Therefore EMF on port k: `EMF_c[k] = -(δL/δV_sq)·2·V_inc[k]`.

### 12.6 Implementation gating

All three audits resolved. Implementation can proceed if Grant approves. Recommended next step: extend `_coupling_grad_asymmetric` argnums and verify EMF computation against the legacy form's known closed-form result as a sanity check before integrating into the engine.

---

*§12 added 2026-04-24 after external-agent audit recommendations. Q67-A/D collapsed (Op14 axiom-correct independently → additive coupling, not replacement). Q67-B closed (quadratic forced by Pythagorean theorem). Q67-C closed (asymmetric L_c has non-local V dependence; JAX autograd handles it). Path 1 implementation scope reduced from ~330 to ~150 LOC. Manual r8.3 patch can be drafted referencing this audit closure.*
