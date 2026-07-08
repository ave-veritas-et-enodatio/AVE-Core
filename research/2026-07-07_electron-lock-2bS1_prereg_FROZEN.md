# PRE-REGISTRATION (FROZEN) — Electron-lock 2b-Stage-1: the BINDING test as a parallel coupling-mode sweep

**Date:** 2026-07-07 · **Lane:** implementer · **Arc:** `analysis/electron-lock-2bS1-fill`
**Branch:** `analysis/electron-lock-2bS1-fill` (throwaway worktree off `origin/analysis/electron-equivalent-circuit`, #569 ref `5a7c78cc`).
**Nature:** **PRE-REGISTRATION — FROZEN BEFORE RESULTS.** This document is committed
*before* the harness and any run (the freeze commit precedes the harness/run commits).
It states the model, the metrics, the thresholds, the bins, and the adjudication rule.
It contains **no result numbers.** The result lands in a separate
`…_RESULT.md` that this prereg governs.

**Predecessors (READ + cited, verify-before-cite this session):**
- `research/2026-07-07_electron-equivalent-circuit.md` (#569) — the frozen equivalent
  circuit this harness extends (two coupled saturating LC tanks + M(V_A1) + Γ=−1 wall).
- `research/2026-07-07_electron-lock_design-note.md` (#568) — the topology walk;
  the §4 modeling fork; the §9 slow/fast-vs-co-equal gut-check (Grant's framing call).
- `research/2026-06-09_reflection-genesis-23-self-assembly_result.md` — GAP-1: a lone
  transverse photon **never energizes** the V-sector (`max|V_inc|=0`); the ω→V channels
  are geometric-multiplicative (0→0) or `∝V_inc` (cannot bootstrap from zero). GAP-2: no
  stable confining window.
- `research/2026-06-09_genesis-24-saturated-seed_result.md` — the ω→V source, once seeded,
  is a **secular pump not a lock** (`+2` bug; `−2` Lenz bounded but does **not close**);
  the (2,3) winder primitive is structurally absent (poloidal q=3 never enters; toroidal
  "2" sub-gate). Pump FALSIFIED for lock.
- `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` — mass = **zero-drive
  persistence** (anhysteretic kernel `S=√(1−A²)`, zero loop area); **reactive storage under
  drive is not mass**; pump-detonation is fool-mode #6.

---

## §0 — THE ONE QUESTION (frozen)

> **Does a coupling mode make the empty CAPACITIVE "3" (V-sector / q-tank) POPULATE from
> the ringing INDUCTIVE "2" (Cosserat / d-tank) and SELF-SUSTAIN at ZERO external drive?**

This is the specific gap that failed 5 ways (genesis-23 GAP-1/GAP-2, genesis-24 pump ×2,
CW-pump structural). None of the 5 prior failures used an **internal reactive fill between
two tanks tuned to the (2,3) ratio at zero drive** — they used a lone photon (no source), a
V-seed + EMF reciprocal (a pump), or a CW external drive. So this is **not a foreseeable
re-run either way.**

## §0a — SCOPE (frozen, stated explicitly up front)

1. **FILLING / BINDING test — NOT selection.** The two tanks are **tuned by construction**
   to the (2,3) ratio (`ω_q/ω_d = 3/2`). Whether (2,3) is *selected over 1:1* is the
   **deferred topological question** (Stage-1 minimal returned `[DOMINATED]`: bare
   two-oscillator dynamics prefer a 1:1 lock; (2,3)-selection is topological, not bare-dynamical).
   This prereg does **not** test selection-over-1:1. It tests whether, *given* the (2,3) tuning,
   the "3" fills and self-sustains.
2. **Reduced-order EQUIVALENT-CIRCUIT register — NOT the 3D lattice.** This extends the
   #569 lumped equivalent circuit (a 2-tank ODE model), not `VacuumEngine3D`. A positive
   here is *necessary-not-sufficient* (needs Stage-2 lattice confirmation); a negative here
   is informative (the most favorable reduced case cannot fill ⇒ the reactive candidate is in
   trouble).
3. **The (2,3) fill is a MEASURED output**, never planted. The seed is inductive current in
   the **d-tank only**; the q-tank starts identically empty (`V_q=I_q=0`). Any q-energy is
   read out from the evolved state (energy-in-the-q-tank + phase-space winding), never seeded.

## §1 — Skill-selection plan (60-sec, pre-harness)

- `substrate-native-check` — §2 walk (K4 / Cosserat / Op14 / phase-space-vs-real-space)
  BEFORE the ODEs. The reduced model must carry the *substrate* reactances (saturating
  `L/S`, collapse `C·S`, divergent `C/S`), not a generic Duffing pair.
- `pre-test-physics-check` — one plumber-physical question surfaced to Grant (§9).
- `phase-space-coordinate-check` (A46) — the (2,3) is a **phase-space** winding on the
  Clifford torus (d,q Park quadratures), NOT a real-space knot. All winding/lock metrics are
  measured in the (V,I) phase plane of each tank — matching coordinates.
- `consistency-vs-emergence` — the component VALUES are consistency-class (datasheet
  imports); the FILL/SUSTAIN/SELECT verdict is the emergence-class output and is firewalled
  (§4): topological / dynamical / scale-invariant, never m_e- or α-tuned.
- `verify-before-cite` — every canon cite greped/opened this session (predecessors above).

## §2 — Substrate-native walk (checkpoints, frozen before code)

- **K4 / bond-pair LC tank.** The base cell is the K4-bond LC tank: `L_cell=μ₀ℓ_node`,
  `C_cell=ε₀ℓ_node`, `Z₀=√(L/C)=376.73 Ω`, `ω_cell=1/√(LC)=OMEGA_C`. Values from
  `ave.core.constants` (no hard-coding). z=3 K4 strut count is not flipped.
- **Cosserat "2" (d-axis, inductive).** The winding that rings/forms is the Cosserat
  micro-rotation, carried by the **saturating inductor** `L_d = L_cell/S(I_d/I_max)`,
  `I_max = XI_TOPO·C_0 ≈ 124.384 A` (μ-grade circulation threshold, `fdtd_3d.I_MAX_MU`).
- **V-sector "3" (q-axis, capacitive).** The empty fibre is the T2 dielectric **collapse
  cap** `C_q = C₀·S(V_q/V_yield)`, keyed `V_YIELD=√α·V_snap` (charge sector). This is the
  Op14 varactor `C_eff(V/V_yield)` (T2 sector). Fill target.
- **Op14 / Ax4 kernel.** The ONLY nonlinearity is `S(A)=√(1−A²)`
  (`ave.axioms.scale_invariant.saturation_factor`). Load-bearing: it makes each tank's
  frequency amplitude-dependent, which is what permits (or denies) an internal n:m resonance.
  The saturating inductor's flux law integrates to a pendulum (sine) constitutive; the
  collapse cap to a `(V_y²/3)(1−S³)` energy — both **anhysteretic** (zero loop area,
  conservative), so the system is Hamiltonian at zero drive (doctrine §1).
- **A1 ⊥ T2 sector keying (never crossed).** A1 metric varactor `C₀/S` keyed `V_snap`
  (mass/DC bias); T2 dielectric `C₀·S` keyed `V_yield` (charge/AC). The A1 bias is a static
  operating-point parameter (zero-drive), NOT a dynamical DOF here.
- **Phase-space vs real-space.** The (2,3) is measured in the phase plane of the (d,q)
  quadratures (Clifford-torus winding), NOT a real-space trefoil (electron = 0₁ unknot in
  real space). All lock metrics live in phase space (A46).
- **Homonym guard.** The winding-"2" (`n_d=2`, topological d-axis winding) ≠ the
  2×-per-cycle L↔C reactive exchange within a tank. "the 2" always means the winding.

## §3 — The frozen model (equivalent-circuit ODEs, zero external drive)

Two nonlinear LC tanks in `(V, I)` state, integrated at **zero external drive** (no source).
Non-dimensionalized to `ω_d=1`, impedance in units of `Z₀`; the datasheet-scaled run (§7) is
a scale-invariance control. Both tanks carry the substrate reactances:

- **d-tank ("2", Cosserat inductive, SEEDED):**
  `C_d = C_cell` (cold linear); `L_d = L_cell/S(I_d/I_max)` (saturating inductor).
  `dV_d/dt = −I_d/C_d(V_d)`; `dI_d/dt = [V_d − ∂E_c/∂flux_d]/L_d(I_d)`.
- **q-tank ("3", V-sector capacitive, EMPTY fill-target):**
  `C_q = C₀·S(V_q/V_yield)` (collapse cap); `L_q = L_cell/S(I_q/I_max)` (saturating inductor).
  `dV_q/dt = −I_q/C_q(V_q)`; `dI_q/dt = [V_q − ∂E_c/∂flux_q]/L_q(I_q)`.
- **Tuning to (2,3):** the q-tank base reactance is scaled so `ω_q/ω_d = 3/2` at small
  amplitude (a dimensionless tuning, scale-free). The (2,3) torus: d winds 2×, q winds 3× per
  common period `T_common = 2·T_d = 3·T_q`.
- **Seed:** `I_d(0)=seed_frac·I_max`, `V_d(0)=0` (pure inductive seed — the "2" rings);
  `V_q(0)=I_q(0)=0` (empty "3"). `seed_frac=0.30` (sub-saturated `A_d=0.30`, `S≈0.954` —
  nonlinearity active, no rupture).
- **Coupling** enters ONLY the flux/current equations (inductive channel) for `mutual_M` and
  `co_equal`; the voltage/charge channel for `coupling_varactor`. All three couplings are
  derived from a **coupling energy `E_c`** so the total `H=E_d+E_q+E_c` is conserved by
  construction (Ax3-lossless; H-drift is then a pure numerical/pump diagnostic).

### The three PARALLEL ARMS (§9 hierarchy fork — the substrate adjudicates)

Let `a_d=I_d/I_max`, `a_q=I_q/I_max`; `E_scale=½·L_cell·I_max²` (a tank-energy unit).

- **`mutual_M`** — bias-set constant mutual inductance (A1 **slow-bias** / T2 **fast-signal**
  hierarchy; #569 chosen fork (a)). Coupling energy **bilinear** in the currents:
  `E_c = κ·E_scale·a_d·a_q`, with `κ = κ0` set by the *static* A1 bias `V_A1/V_snap`. Because
  `V_A1` is a DC operating point, `κ` is constant on the fast timescale ⇒ a linearized
  1:1-resonant coupler. Keeps the two voltage nodes galvanically independent (mutual flux).
- **`co_equal`** — two **co-equal** nonlinear oscillators, symmetric nonlinear coupling, **no
  bias/signal hierarchy** (#568 §9 gut-check alternative). Same inductive/flux channel but the
  coupling retains its **intrinsic nonlinearity** (the `A₁·|T₂|²` amplitude² dependence, made
  symmetric): `E_c = κ·E_scale·a_d·a_q·[1 + g·(a_d²+a_q²)]`, `g=g0>0`. The cubic term supplies
  the sum/difference frequencies that can bridge the 3:2 detuning. Symmetric under d↔q; no
  external bias controls it. Setting `g=0` recovers `mutual_M` exactly (nested arms).
- **`coupling_varactor`** — the bridging-cap realization; a **CONTROL** that co-keys the tanks
  by construction: `E_c = ½·C_c·(V_d−V_q)²` (a shared capacitance bridging the two voltage
  nodes). It ties `V_q` to `V_d` (capacitive divider). **It SHOULD trip the tautology guard**
  (§6). If it "fills" trivially, that CONFIRMS the detector works — bin `[TAUTOLOGY]`, not a win.

**Coupling strengths (dimensionless, frozen):** `κ0 = 0.15`, `g0 = 4.0`, `C_c = 0.30·C_q0`.
These are engineering choices tagged as such (§4): chosen to sit in the KAM/resonant-island
regime (weak enough that off-resonant configs do NOT trivially mix, strong enough that an
on-resonance fill is visible within the window). They are **scale-invariant** and carry **no
m_e / α content**. The verdict is required to be invariant to their exact values within a
stated neighborhood (§7 robustness), and the substrate — not these numbers — decides the bin.

## §4 — FIREWALL (mechanical exclusion — load-bearing)

- **LEGITIMATE (consistency-class): the component VALUES.** `L_cell, C_cell, Z₀, I_max,
  V_snap, V_yield, ω_cell` from `ave.core.constants` (+ `fdtd_3d.I_MAX_MU`) — the datasheet
  model's own numbers. No value hard-coded.
- **FORBIDDEN (emergence-class OUTPUT): the FILL/SUSTAIN/SELECT verdict.** The routed bin
  must be **topological / dynamical / scale-invariant**, never tuned to, seeded from, or
  checked against `m_e` or any mass ratio. The verdict depends only on the dimensionless
  `(ratio, κ0, g0, seed_frac, C_c/C_q0)` — none m_e-derived.
- **α and Q=1/α EXCLUDED from the outcome.** `ALPHA` / `ALPHA_COLD_INV` must not appear in
  the harness outcome logic. (`V_yield=√α·V_snap` carries an α-echo in its *magnitude*; the
  verdict must be invariant to that magnitude — demonstrated by the §7 scale-invariance
  control. The magnitude never reaches the bin.) Enforced by a **tokenize/AST firewall scan**
  asserting no `ALPHA`/`M_E`/`m_e` token on the outcome path.
- **Scale-invariance control (the firewall demonstration):** the 3:2 config is run at TWO
  absolute scales (normalized `ω_d=1` AND datasheet-scaled `ω_d=ω_cell·<ratio>`); the routed
  bin MUST be identical. A bin that changes with absolute scale FAILS the firewall.

## §5 — The DOUBLE-COUNT LANDMINE (the owed check — handled explicitly)

`M(V_A1)` risks the genesis-24 double-count: the flag-gated Lagrangian-EMF reciprocal
(`k4_cosserat_coupling.py:223`, `use_lagrangian_emf_coupling=False` by default) is off
*precisely because* on small-amplitude mixed-mode it **double-counts the Op14 varactor
`C_eff(V)`** (both signs diverge). My q-tank cap **is** that Op14 varactor
(`C_q=C₀·S(V_q/V_yield)`). Handling:

- **`mutual_M` / `co_equal` couple through the INDUCTIVE flux channel** (`E_c` depends on the
  currents `a_d, a_q`), which is **orthogonal** to the q-tank's capacitive reactance
  `C_q(V_q)`. The Op14 collapse cap is carried **once**, by `C_q`, computed **solely from
  `V_q`** and never from the coupling. I add **NO** `∝V_inc` EMF term (the exact term that
  double-counts). This is asserted in the harness: a reconcile-gate checks the q-tank
  capacitive energy recomputes from `V_q` alone, independent of `E_c`.
- **`coupling_varactor`** uses a **separate** linear bridging cap `C_c` (distinct element,
  distinct charge) — it does not re-inject `C_q`'s collapse charge. It is a control anyway.
- **Verdict tag:** because the coupling is a pure inductive mutual (not a V-dependent reactive
  re-injection), the arms are **NOT** double-count-suspect. If any arm's implementation is
  found to re-touch `C_q` through `E_c`, that arm's result is FLAGGED `double-count-suspect`
  and NOT read as a win.

## §6 — Metrics (frozen definitions) + anti-tautology guards

Energies (closed-form, for the H-ledger): saturating inductor `U_L=L_cell·I_max²·(1−S(I))`;
linear cap `U_C=½C_cell·V²`; collapse cap `U_C=C₀·(V_yield²/3)·(1−S(V_q)³)`. `E_d=U_{C,d}+U_{L,d}`,
`E_q=U_{C,q}+U_{L,q}`, `H=E_d+E_q+E_c`. Normalize by `H(0)`.

Recording window `[0, t_max]`, `t_max = 120·T_common` (240 d-cycles); back-half = last 50%.

1. **FILL** — `fill_max = max_t E_q/H(0)`; `fill_mean = ⟨E_q/H(0)⟩` over the back-half.
2. **SUSTAIN** — `fill_min = min_t (E_q/H(0))` over the back-half (does q ever empty back to
   ~0?); `H_drift = max_t|H(t)−H(0)|/H(0)` (the conservation/detonation ledger).
3. **LOCK (phase-space (2,3) readout, A46)** — instantaneous phase `θ_i=atan2(I_i/I_max,
   V_i·C_scale)`; the resonant combination `ψ = 3·θ_d − 2·θ_q` (constant on a (2,3) torus).
   `lock_drift = |ψ(t_end_backhalf) − ψ(t_start_backhalf)|` (wrapped-unwrapped). Also the
   per-tank winding numbers `(w_d, w_q)` from the unwrapped phase over one back-half segment,
   and their ratio → should read (2,3).
4. **CAN-FIRE / SELECTIVITY** — a **golden-ratio** config (`ω_q/ω_d = φ = (1+√5)/2`,
   maximally irrational) is run identically. It must **NOT** route `[FILLS-AND-SUSTAINS]`
   (KAM torus: the empty q stays empty / borrows-and-returns, no phase lock). If it also
   sustains, the test is vacuous for that arm — reported honestly.
5. **INDEPENDENCE guard (anti-tautology)** — `div_corr` = correlation of `V_q(t)` with the
   instantaneous capacitive-divider image `V_d(t)·C_c/(C_c+C_q0)` over the window; and
   `t_fill` = the earliest time `E_q/H(0)` crosses `FILL_THRESH`. A co-keyed (divider) fill
   tracks `V_d` near-instantaneously (`div_corr→1`) and fills within the first fraction of a
   d-cycle (`t_fill ≪ T_common`) *regardless of ratio* — that is the tautology signature.

## §7 — Thresholds + BINS (frozen BEFORE any run)

**Thresholds (dimensionless, m_e-free, α-free):**
- `FILL_THRESH = 0.05` (q holds ≥5% of total energy — a substantial populate from ~0).
- `SUSTAIN_THRESH = 0.01` (q back-half minimum ≥1% — it does not empty back to zero).
- `H_GATE = 0.02` (H-drift <2% over the window — conservative, not detonating).
- `LOCK_GATE`: `lock_drift < π` over the back-half (phase-locked, ψ not secularly advancing).
- `TAUT_CORR = 0.9` (`div_corr>0.9` ⇒ divider co-keying); `TAUT_FAST = 0.25·T_common`
  (`t_fill < TAUT_FAST` ⇒ instantaneous fill).

**BINS (per arm, evaluated at the 3:2 config):**
- **`[FILLS-AND-SUSTAINS]`** — `fill_mean ≥ FILL_THRESH` AND `fill_min ≥ SUSTAIN_THRESH` AND
  `H_drift < H_GATE` AND `lock_drift < LOCK_GATE` AND independence-guard PASSES (`div_corr <
  TAUT_CORR` or coupling is inductive) AND can-fire HOLDS (golden does NOT sustain).
- **`[FILLS-BUT-DECAYS]`** — `fill_max ≥ FILL_THRESH` but `fill_min < SUSTAIN_THRESH` (q
  populates then empties back — reactive borrow/return storage, NOT mass).
- **`[DOESN'T-FILL]`** — `fill_max < FILL_THRESH` (the "3" stays empty — the 5-failure outcome).
- **`[TAUTOLOGY]`** — independence guard TRIPS (`div_corr > TAUT_CORR` AND `t_fill <
  TAUT_FAST`) OR can-fire is vacuous (golden ALSO routes fills-and-sustains via a
  non-selective mechanism). For `coupling_varactor` this is the *expected, detector-confirming*
  outcome.

**Robustness (freeze):** the 3:2 bin is re-checked at `κ0×{0.7,1.4}` and `seed_frac∈{0.2,0.4}`;
a bin that flips under a ±40% coupling nudge is downgraded to a qualified verdict (reported,
not headlined).

## §8 — ADJUDICATION (the substrate decides the fork — report honestly, do NOT rationalize)

Read the per-arm bins and route the hierarchy verdict:
- `mutual_M` [FILLS-AND-SUSTAINS] AND `co_equal` NOT → **bias-hierarchy real** (the linearized
  slow-bias coupling suffices; the varactor framing wins).
- `co_equal` [FILLS-AND-SUSTAINS] AND `mutual_M` NOT → **two-mode resonance** (the full
  nonlinear co-equal coupling is required; the bias-hierarchy framing is the wrong idealization).
- **Both** → both couplings work (the fill is robust to the framing).
- **NEITHER** → **the reactive-pump candidate is DEAD**; the "3" needs a **non-reactive**
  mechanism. A cheap, important NEGATIVE — the gap says no to us too. State it plainly; do NOT
  debug toward a rescue (Rule 11). Retract via Rule 12 if a live hypothesis is falsified; do
  not refill the slot (Rule 12 / A47 v11b).
- `coupling_varactor` is a **control**: its expected route is `[TAUTOLOGY]`. If it instead
  routes `[DOESN'T-FILL]`, the tautology detector is under-powered — flag it.

## §9 — Pre-stated expectation + pre-test-physics question (Grant)

**Pre-stated expectation:** genuinely uncertain — this is the make-or-break. The 5 prior
failures used a lone photon (no source), a V-seed+EMF (a pump), or a CW external drive; **none
used this internal-reactive-fill at (2,3) tuning, zero drive.** So it is not a foreseeable
re-run either way. If forced to a prior: `mutual_M` (bilinear, a 1:1-resonant coupler) is
*expected* to struggle at the 3:2 detuning (borrow/return); `co_equal`'s cubic term is the
one with a mechanism to bridge 3:2 — but whether a conservative reactive coupling forms a
*persistent* (2,3) partition (vs KAM quasi-periodicity) is exactly what the substrate will
decide. Both-fail (candidate dead) is a live, respectable outcome.

**pre-test-physics-check — one plumber-physical question surfaced to Grant:** in a genuinely
**lossless** (anhysteretic, zero-drive) two-tank circuit, "self-sustain" cannot mean "energy
persists" (energy is conserved, so *everything* persists trivially). The mass-analogue
discriminator I have frozen is **partition persistence**: does the q-tank hold a *stable
nonzero share* (a phase-locked (2,3) bound partition), as opposed to periodically returning
all its energy to the d-tank (reactive borrow/return = not mass)? Is that the right reading of
"zero-drive persistence" for a lossless tank, or does the mass-analogue require a *dissipative*
`B_r`-at-`H=0` remanence that a conservative circuit structurally cannot show — in which case
the equivalent-circuit register can at best route `[FILLS-BUT-DECAYS]` and the real test must
add the Level-2 `τ_relax` memristive kernel (doctrine §6)? Surfaced BEFORE freezing the bins;
the frozen bins treat partition-persistence as the operative discriminator and flag the
dissipation question as the scope boundary.

## §10 — Discipline that rides every arm (frozen)

- **FIREWALL** (§4) + tokenize/AST scan (no `ALPHA`/`M_E` on the outcome path) + scale-invariance control.
- **DOUBLE-COUNT** (§5) handled: inductive coupling orthogonal to `C_q(V)`; reconcile-gate on the q-cap energy.
- **ANTI-TAUTOLOGY** (§6): q-fill is a measured output; the can-fire (golden) must actually
  fire; a config that does NOT fill is demonstrated.
- **SECTOR:** A1↔V_snap, T2↔V_yield never crossed. **HOMONYM:** winding-"2" ≠ 2×-per-cycle exchange.
- **ReconcileGate + can-fire self-test** on the load-bearing recomputations (q-cap energy;
  H-ledger independent recompute).
- **RUN MANAGEMENT:** integrations are short (O(10⁴) steps, milliseconds); no background polling needed.
- **FIGURE:** house-WHITE (`ave.viz.style.apply`).

**Files:** this prereg (freeze first) → `…_RESULT.md` +
`src/ave/solvers/electron_lock_2bS1.py` (harness) +
`src/scripts/verify/electron_lock_2bS1.py` (driver) +
`src/tests/test_electron_lock_2bS1.py` (tests + standing falsifiers).
