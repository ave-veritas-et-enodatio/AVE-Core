# PRE-REG (FROZEN, Rule-11) — Stage-1.6 CP8-safe OPEN route: external moving Γ=−1 wall on Sector B

**Date:** 2026-06-16 · **Lane:** implementer · **Branch:** `analysis/2026-06-16-boundary-mqj-stage16-moving-wall-sectorB`
**Base:** `analysis/2026-06-16-boundary-mqj-stage15-alphafree-emergence` @ `be459b7e` (the α-free engine + generic photon seed + layer-c emergence probe).
**Inherited success criterion (FROZEN, unchanged):** `reconciliation-handoffs/2026-06-16_electron-existence-discrimination-prereg.md` §"Pre-registered success criterion" — the α-free winding-emergence lane (CP8 no plant, α-free, measure α-free Q, Z→0 necessary-not-sufficient). Reading m_e/e/ℏ/2 is NOT success (echo).
**Extends:** `research/2026-06-16_stage15-alphafree-winding-emergence_result.md` §0/§3/§4 (the Stage-1.5 (c) EMERGENCE-NEGATIVE + its named mechanism).

This prereg is banked **BEFORE** any Stage-1.6 measurement, freezing the bins, the
discriminator, and the new CP8-spatial-provenance gate. Per Rule 11: a clean
negative with a named mechanism is the discipline working — this prereg does NOT
license a rescue.

---

## §0 — The gated question (one hypothesis)

Stage-1.5 (c) proved an **internal SPECTATOR cage** cannot confine a *propagating*
photon: the A1 deep-saturated core is pure A1 dilatation = irrotational
(∇×∇V≡0, `engine-capability-map.md:57`), so the winding curl is structurally zero
there, and `f_V=0`, `coupling_work=0` because a propagating photon's curl never
co-locates with the compact cage core — it radiates out. This is a STRUCTURAL
null (adversarially confirmed), not a bug.

**THE HYPOTHESIS:** Can an EXTERNAL **moving Γ=−1 / Op17-bounded reflecting wall on
SECTOR B** (the photon's OWN sector — the Cosserat-ω sector, NOT Sector A where the
cage sits inert) confine the propagating photon so the energize-LOCK loop closes
(`coupling_work ≠ 0`, `f_V ≠ 0`) — **WITHOUT changing the seed?**

The ONLY change vs Stage-1.5 (c) is **adding the external wall on Sector B.** The
seed is the SAME generic transverse ω-photon, UNCHANGED (CP8-safety: re-seeding a
confined / co-located / pre-wound precursor would install the answer — the held-BC
C′ plant hazard).

---

## §1 — The build (3 changes, all bounded by CP8-safety + α-free)

1. **SAME generic transverse ω-photon seed, UNCHANGED.** `seed_cosserat_photon`
   (generic Gaussian helical wavepacket, amplitude 0.3, λ=6, the Stage-1.5 (c)
   config). `seed_bulk_blob` (sub-yield A1 mass) UNCHANGED. No planted (2,3), no
   pre-co-location, no pre-winding.
2. **An α-FREE moving Γ=−1 wall on Sector B.** Reuse the saturation-TIR
   moving-boundary precedent (`analysis/2026-06-06-saturation-tir-moving-boundary`,
   VERDICT (II): the moving Γ=−1 wall DID confine the Cosserat-ω photon, loc
   0.97→0.94, held vs both collapse and dispersion). Realized via
   `CosseratField3D(use_impedance_boundary=True, impedance_clamp_strength=K,
   impedance_implicit=True)` — the Op3 Γ=−1 node-clamp on the μ-side saturation
   front. **α-FREE ROUTING (load-bearing):** the precedent's `_impedance_gamma_field`
   routes through `KAPPA_CHIRAL_ELECTRON = α·κ̃_e` (α-bearing). We override it at the
   instance level to `kappa_chiral=0` (the symmetric/achromatic μ/ε limit), so the
   μ-side short is driven by the **GENERIC curvature saturation
   `A²_μ_base = κ²/ω_yield²`** (geometric, α-free) ONLY. Pre-build probe (this
   session): the α-free Γ_min=−0.084 ≈ the α-chiral Γ_min=−0.083 — the α-chiral
   term is an α-scale perturbation; the wall is geometric.
3. **The wall CO-MOVES with the cage front (GENERIC rule).** The wall position is
   the Γ-field itself, recomputed from the focusing ω-field every (sub-)step
   (`_freeze_clamp_weight` re-frozen per sub-step under `impedance_implicit`). It
   tracks the saturation threshold / cage-front location — NOT hand-placed where
   the answer is. Op17-bounded BC: `|Γ|→1 as A→1` (Checkpoint 10), realized as the
   reactive node-clamp `a_ω = −(K/I_ω)·relu(−Γ)·ω` (energy-storing via the exact
   `_rotate_clamp` LC rotation, NOT a bulk force; no |ω| blow-up).

---

## §2 — CP8-SPATIAL-PROVENANCE gate (NEW discipline — the auditor's flag)

The existing `seed_audit` gates TOPOLOGY (`t0_closes_23`, `non_circular`) but NOT
spatial configuration — and Stage-1.5 (c) proved **spatial co-location is the
load-bearing axis**. This prereg ADDS a spatial-provenance audit, REPORTED in the
result, with three prongs:

- **(a) seed-provenance:** confirm the seed is the SAME generic photon — no spatial
  plant in the seed (the photon is launched as a propagating wavepacket, not a
  pre-confined standing mode; `t0_closes_23=False` inherited from Stage-1.5).
- **(b) wall-provenance:** confirm the wall position is set by the GENERIC Γ-field
  rule (recomputed from the field each sub-step), not hand-placed at the answer.
  Report the wall-front location vs the photon density-peak over time — they must
  CO-EVOLVE under the generic rule, not be pinned.
- **(c) generic-offset sweep (THE plant discriminator):** vary the photon's launch
  position relative to the wall/cage center over a GENERIC range of offsets. If
  loop-closure works ONLY at one hand-tuned offset → a PLANT (fail). If it works
  across a generic range → EARNED. This gate decides whether a LOOP-CLOSES result
  is real or installed.

---

## §3 — Measurements (pre-committed)

- **`coupling_work` / `f_V` trajectory (THE gated number):** does the loop FIRE
  (`coupling_work ≠ 0`, `f_V` source live > 0% of steps) under the wall, vs Stage-1.5
  (c)'s spectator `f_V=0` / `coupling_work` flat? Recorded every sample.
- **photon confinement:** does the Sector-B Γ migrate to the rim (Z→0 / Γ→−1)?
  Localization (top-|ω|² within r≤6 of the density peak, PML-excluded), vs the
  no-wall control. Reactance pair |ω| (C-state) AND |ω̇| (L-state) every sample.
- **the winding:** does the (2,3) SELF-FORM once the photon is confined?
  `_measure_23` on the Cosserat ω phase-space (ω_x,ω_y) AND the bulk reactance
  (V,∂_tV), A46 phase-space coordinates, density-peak sampling, reliable contours.
- **α-free Q (ONLY if the loop closes):** does ~137 EMERGE untold? Joint-ledger
  guard: no resonator ⇒ nothing for Q to be (no α inserted either way).
- **full-H ledger** (passive, no pump): the coupled `total_hamiltonian()` + the
  Cosserat `impedance_hamiltonian()` (T + W_linear + V_clamp). |ω| bounded.
  Long-window persistence (≥10 Compton periods, default 12).

---

## §4 — Bins (FROZEN)

| Bin | Condition | Disposition |
|---|---|---|
| **LOOP-CLOSES** | wall confines the photon (Sector-B Γ→rim) AND `coupling_work ≠ 0` (energize-LOCK fires) AND the generic-offset sweep PASSES (not a plant) | (c) was a fixable mechanism-gap; the propagating route works WITH an external wall. THEN read emergence (did (2,3) self-form? did α-free Q emerge?) → **EMERGENCE-CANDIDATE** (orchestrator adjudicates chord/echo — implementer does NOT conclude). |
| **WALL-CONFINES-BUT-LOOP-INERT** | wall traps the photon (Sector-B Γ→−1) but `coupling_work` still =0 | the obstruction is DEEPER than confinement. Report precisely. |
| **WALL-ALSO-FAILS** | the moving wall CAN'T confine the propagating photon (radiates through/past) OR it pumps | the obstruction PROMOTES to a real substrate statement ("a free propagating massless precursor can't become a bound resonator even with an external wall"). Report precisely. |
| **PUMPS** | the wall isn't Op17-bounded (bulk force; \|ω\| blow-up, full-H climbs) | fix the BC, report. |

**Adjudication criteria are frozen.** No post-hoc dropping of a criterion to convert
a bin. A `coupling_work ≠ 0` that ONLY appears at a hand-tuned offset is a PLANT
(generic-offset-sweep FAIL) and does NOT qualify for LOOP-CLOSES — it routes to a
flagged plant, reported as such.

---

## §5 — Discipline (apply, don't just name)

- **substrate-native-check Ckpt 8** (generic, no plant): seed UNCHANGED + the wall
  position is the generic Γ-field rule; the generic-offset sweep is the plant gate.
- **substrate-native-check Ckpt 10** (Op17-bounded BC, no bulk force): `|Γ|→1 as
  A→1`; the reactive node-clamp (energy-storing, exact LC rotation), NOT a bulk
  force; |ω| bounded.
- **full-Hamiltonian witness** (`total_hamiltonian()` / `impedance_hamiltonian()`,
  NOT sum(ω²)).
- **ave-apparatus-floor-attribution** (validate the moving-wall mechanism on a
  KNOWN photon FIRST — does the α-free wall confine a known case? — BEFORE trusting
  a null). Pre-build known-positive (this session): α-free wall (K=400) held a
  known photon loc 0.967→0.969 vs no-wall 0.967→0.679. The driver re-runs it as
  §0 of the measurement.
- **ave-conserved-vs-pumped** (energize-LOCK is a conserved exchange, not a pump;
  the ON-minus-OFF excess is the coupling-attributable ledger term).
- **α-FREE inherited** (no ALPHA / KAPPA_CHIRAL / V_yield=√α·V_snap in any update
  equation — grep-confirmed; route around the α-bearing `_impedance_gamma_field`
  default via the instance-level kappa_chiral=0 override, as Stage-1.5 routed
  around the α-bearing `VacuumEngine3D` paths).

---

## §6 — Figures (REAL data, not schematics; saved to `research/figures/`)

1. **moving-wall TDR** — wall position vs time + the photon reflection (nucleate /
   co-move / confine?).
2. **coupling_work / f_V trajectory** — does the loop fire, vs the (c) spectator
   f_V=0 (overlay the (c) flat-zero baseline).
3. **Sector-B Γ-plane locus** (Smith) — does the photon's Γ migrate center→rim
   under the wall? DUAL-SECTOR per the H3 wall-branch fork. **The terminal
   |Γ|²=1−α is marked as bake-(ii) echo, NOT emergence** (the 1−α gap is the
   universal Q-invariant radiative leak in `cvr_model.gamma_mag_sq_leak()`, not a
   self-emergence read).
4. **winding read** — does (2,3) self-form (w_tor, w_pol vs time)?
5. **apparatus-floor known-positive** — the α-free moving wall confining a known
   photon (the validity gate, vs no-wall dispersal).

---

## §7 — Scope guards (FROZEN)

- Do NOT change the seed (CP8-safety).
- Do NOT insert α.
- Do NOT read m_e/e/ℏ/2 as success (echo).
- Do NOT touch R10 remanence.
- Do NOT conclude chord/echo (orchestrator adjudicates).
- Do NOT merge (main is PROTECTED).
- Honest "WALL-CONFINES-BUT-LOOP-INERT, here's why" is a GOOD report; a forced
  emergence claim is NOT.

---

## 🔧 AMENDMENT A4 — APPARATUS SUBSTITUTION (Rule-12, NOT retraction) — 2026-06-16

> **Rule-12 apparatus-substitution.** This amendment is appended; the FROZEN body
> above (§0–§7, the 4 bins, the discriminator, the verdict-space) is UNCHANGED.
> Only the wall *mechanism* (the apparatus) is substituted. The bins and the
> adjudication criteria are PRESERVED. This is **not** a retraction (the hypothesis
> stands) and **not** a rescue (no criterion dropped, no post-hoc bin remap).

**Branch:** `analysis/2026-06-16-stage16-k4tlm-bounded-wall` (off the amendments
base `analysis/2026-06-16-stage16-rerun-amendments`, which already carries the
#273 amendments 1/2/3/5). **Source:** the #273 pre-flight `ww8x96sci`, GAP 3 (the
"Op17-bound" premise is false).

### What is substituted (the apparatus only)

The §1.3 / §5 Op17-bounded wall was specified as the reactive node-clamp
`a_ω = −(K/I_ω)·relu(−Γ)·ω`, integrated by the exact LC rotation `_rotate_clamp`
(`cosserat_field_3d.py:1760`), with the FROZEN claim "|ω| bounded" / "no |ω|
blow-up." **That premise is FALSE.** `_rotate_clamp` integrates the harmonic
node-clamp `ω̈ = −Ω₀²ω` EXACTLY, but `Ω₀ = √((K/I_ω)·relu(−Γ))` is a *stiffening
spring* with **no |ω| ceiling**: as the saturation front sharpens (`relu(−Γ)→1`)
it stores unbounded reactive energy, so the wall **forms (Γ→−0.994) AND pumps
(H climbs 4.3×10⁶) together** (#273 banked data; reproduced this branch at the
operating point: `|ω|max→20918`, `H_minus_Vclamp` peak-rise `+7.4×10⁶`). A spring
is a **bulk restoring force** — `substrate-native-check` Checkpoint-10 says render
confinement as a **boundary reflection** (`R = Γ² ≤ 1`), NOT a bulk force (singular
at the wall, detonates). The amend-4 `K_wall` sweep confirms the gap is unfixable
by value: **no K** separates pump-suppression from confinement-loss (verdict
`AMBIGUOUS-pending-stable-BC`) — because no *value* of a no-ceiling clamp can add
a ceiling.

**Substituted apparatus:** the **K4-TLM Op3 unitary-scatter reflector**
(`k4_tlm.py:402-423`, `V_inc = Γ·V_ref_A + T·V_ref_B`, `Γ²+T²=1`, `|Γ|≤1`)
adapted to the Cosserat `(ω, ω̇/Ω₀)` reactance pair (`_unitary_scatter`,
`cosserat_field_3d.py`). At the wall cells the incident/reflected d'Alembert
characteristic amplitudes are rotated through the **orthogonal** `[[Γ_w,T_w],
[T_w,−Γ_w]]` (`Γ_w = relu(−Γ) ∈ [0,1]`, `T_w = √(1−Γ_w²)`). Orthogonality
preserves the reactance-pair norm `½(ω²+ω̇²/Ω₀²)` EXACTLY and maps `|output|=
|input|` — so the wall **cannot inject energy (no pump)** and `|ω|` is bounded by
the incident amplitude **by construction (no blow-up)**. At the μ-short
`Γ_w→1,T_w→0` the wave reflects with the corpus `Γ=−1` inversion
(`electron-identification.md:24` property-3 TIR cavity: "a perfect TIR mirror at
the wave's location, trapping it as a standing wave"; `:25` "only the boundary
condition flips from impedance-matched Γ=0 to TIR Γ=−1"); at matched/open
`Γ_w→0,T_w→1` the pair
free-streams (bulk wave unchanged). This is the CP10-correct boundary rendering
of the SAME physical wall the frozen prereg specified — it bounds `|ω|` *without*
suppressing the reactive sector-to-sector exchange the loop test measures
(resolving the posable-vs-meaningful catch-22).

### What is PRESERVED (unchanged)

- **The 4 FROZEN bins** (§4): `LOOP-CLOSES / WALL-CONFINES-BUT-LOOP-INERT /
  WALL-ALSO-FAILS / PUMPS`. Verdict-space unchanged.
- **All adjudication criteria** (§4 + #273 amendments 2/3/5): two-sided fire
  (`fV_live_max>0` AND `f_omega_alive_max>0` on alive), the H-ledger bin gate
  (`coupling_hamiltonian_full` flat/decaying, V_clamp held separable), the
  conserved-redistribution gate, the generic-offset plant discriminator, the
  known-null meter. None dropped, none relaxed.
- **The seed** (§1.1, CP8-safe, α-free), **the success criterion** (inherited),
  **the scope guards** (§7).

### Rationale for substitution-not-retraction

The §0 hypothesis ("can an external moving Γ=−1 / Op17-bounded wall on Sector B
confine the photon so the loop closes") is UNCHANGED — only the realization of
"Op17-bounded" is corrected from a (falsely-bounded) bulk node-clamp to a
(genuinely-bounded) boundary scatter. The frozen-clamp run is RETAINED in the
driver as the **motivating diagnostic** (it lands `PUMPS` / `AMBIGUOUS`, which is
*why* the unitary wall is needed). Per Rule-12: the apparatus that cannot test the
hypothesis honestly is replaced; the hypothesis, bins, and criteria are preserved
so the verdict remains comparable to the frozen verdict-space.

### Note (non-physics): dx normalization

Side-rider (does not alter the object, only the sampling): the engine + driver
`dx` defaults are normalized `0.5 → ℓ_node = 1.0` (the §1 stale comment
`boundary_mqj_selftrap_zwall_gate.py:94` "dx=ℓ_node" was FALSE with `KP_DX=0.5`).
`dx=0.5` was 2× *oversampling* (Phase-20 scoped credit), not a sub-Nyquist fiction
— the result doc reports both so the verdict is not dx-dependent.
