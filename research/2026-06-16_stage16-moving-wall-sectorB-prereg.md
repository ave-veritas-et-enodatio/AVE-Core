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
