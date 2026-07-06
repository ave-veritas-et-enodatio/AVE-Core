# EM keying ROUND 3 — the ε-side DC-mechanism: CHARGE-KEYED vs EXCURSION-KEYED — RESULT

**Date:** 2026-07-06 · **Lane:** implementer · **Branch:** `analysis/em-keying-round3-eps-dc-mechanism`
**FROZEN prereg (gated on):** `research/2026-07-06_em-keying-round3-eps-dc-mechanism_prereg_FROZEN.md`
(freeze commit `942c950b`, committed before any result — git ordering = freeze proof).
**Drivers (two files; sympy + numpy; ReconcileGate can-fire proven; constants imported):**
- `src/scripts/verify/em_keying_round3_mechanism.py` — the BLIND structural derivation (M0/M1/M2/M3
  + the four mandatory sub-answers). NO muonic/CREMA/#539/Table-I/PVLAS reference (hard firewall).
- `src/scripts/verify/em_keying_round3_comparison.py` — the FIREWALLED §9 comparison (muon vs the
  derived key), permitted to touch #539 ONLY here; consumes the #539 machinery by import.
**Tests:** `src/tests/test_em_keying_round3_eps_dc_mechanism.py` (8 fast-core gating + 2 engine_sim
standing falsifiers).

## ROUTED BIN: **[DERIVED: CHARGE-KEYED]** (with a UNIFORM-bias gauge-observability RIDER)

> The ε-grade (transverse-T2 permittivity channel) nonlinearity keys on the **MEAN-SQUARE** of the
> instantaneous field amplitude at the cell — **DC-INCLUDED** (H1/CHARGE-KEYED). The
> variance/excursion member (H2) is **NOT forced** by the canonical network: all four candidate
> mechanisms (M0/M1/M2/M3) fail to deliver a lossless DC-block. The E-side "worked-keying" rescue
> (a Lenz-dual DC-blindness for the varactor) **does not exist in the canonical structure**. The
> round-2 `[SELECTED-NOT-DERIVED]` variance member is therefore **DERIVED-AGAINST**: the network
> selects the mean-square, not the variance.
>
> **RIDER (a real refinement, not a rescue):** a spatially-**UNIFORM** held DC bias self-cancels on
> READOUT — the A-state is **gauge-relative** (`CLAUDE.md` INVARIANT-S2:75, VERBATIM *"only spatial
> gradients of A across the substrate are physically observable, not absolute per-node values"*), so a
> uniform offset is unobservable (= the PHASE-ONLY north-star). This is Grant's Reading-A adaptation,
> **already canon at axiom level** — but it is an **OBSERVABILITY** statement (differential readout),
> NOT a claim that the local ledger is excursion-keyed. The local cell IS deficient under a uniform
> bias; you just cannot READ it without a gradient (a co-located wave-made ruler rides the same
> offset). A **NON-uniform** held field (a real bench fringe, an atomic Coulomb field) has a nonzero
> `∇A` and IS readable and DOES load.

## THE DERIVED KEYING STATEMENT (verbatim; sub-answer iii — EXACTNESS)

$$
\boxed{\;
S_\varepsilon\big[E(\cdot)\big] = \sqrt{1 - \mathcal{K}}, \qquad
\underbrace{\mathcal{K} \;=\; \big\langle A_V(t)^2 \big\rangle
   \;=\; \Big(\tfrac{V_0}{V_{yield}}\Big)^2 + \tfrac12\Big(\tfrac{V_1}{V_{yield}}\Big)^2}_{\textbf{MEAN-SQUARE — DC-included (H1/CHARGE-KEYED)}}
\;\;\ne\;\;
\underbrace{\operatorname{Var}_t(A_V) = \tfrac12\Big(\tfrac{V_1}{V_{yield}}\Big)^2}_{\text{variance (H2) — NOT what the network forces}}
\;}
$$

for a cell driven `V(t) = V_0 + V_1 cos(ωt)` (`V_0` = held DC baseline, `V_1` = AC excursion). At
leading (2nd) order the kernel deficit the varactor integrates is
`⟨1 − S(A_V)⟩ = ½⟨A_V²⟩ = ½(a_0² + a_1²/2)` — **EXACTLY the mean-square, not the variance** (sympy,
`m0_axiom_argument`; `mean_leading = a0**2/2 + a1**2/4 = ½·mean_square`). The two objects differ by the
DC baseline `a_0²`: the mean-square keeps it (charge), the variance subtracts it (excursion). **The
network keeps it.** This is exactly the object round-2 named at its crux (`⟨A_V²⟩/2` = mean-square,
`1−S(0.3)=0.046`) — round-3 derives WHY: no mechanism removes the DC baseline.

## THE SLOW-RAMP SETTLE-OUT ANSWER (verbatim; sub-answer i — Grant's falsifier)

> **PERSISTS (→ H1).** A field ramped up over seconds engages the cell during the ramp
> (`J_D = ε₀ dE/dt ≠ 0`, transient; cell response time `τ_relax = ℓ_node/c ≈ 1.288×10⁻²¹ s`), then
> settles. After settle `dE/dt = 0 → J_D = 0`, but the local ε-deficit `= 1 − S(E/E_yield)` depends
> **ONLY on the settled (held) amplitude**, NOT on the ramp rate — it **REMAINS**. The cell does **not
> forget a stress it is still under.** The elastic bookkeeping is explicit: the stress is parked as
> **charge in the saturating shunt capacitor** (`U = ½C V² = ½ε₀E²` per cell). A lossless "forget"
> would need either a soft zero-restoring mode (none exists — M3) or the `τ_relax` first-order
> relaxation — but the `τ_relax` hysteresis loop `∮S dr` is **dissipated** energy per cycle
> (`tau-relax-derivation.md`:24), so a lossless forget is **Ax3-forbidden**. Therefore the post-settle
> ε-shift persists: this is the H1/CHARGE-KEYED signature. (Under H2 the shift would decay to zero on
> settle; it does not, because there is nowhere lossless for the parked charge to go.)

## THE M0/M1/M2/M3 VERDICT TABLE (all four fail to deliver a lossless DC-block)

| Mechanism | Question | Derived verdict | Basis (canonical) |
|---|---|---|---|
| **M0** NULL | Is `A` axiom-defined on a static-capable variable ⟹ H1 forced? | **YES → H1.** The ε-kernel argument is `A_V=V/V_yield=|E|/E_yield`, a static-capable amplitude; the leading mean deficit is `½·mean-square` (DC-included); a held DC alone gives deficit `a_0²/2>0`. H2 would need an **axiom-level reinterpretation**, flagged — not a network trick. | `node-up`:104-106,:117-118; `axiom-register` Axiom-4:186 (`A`=local strain), :188 (forced L2 invariant on the dynamical phase-plane radius) |
| **M1** TOPOLOGY | Series-C DC-block on the ε path? | **NO — FALSIFIED by topology.** The ε-varactor is the **SHUNT** node capacitance (`C_cell=ε₀ℓ`, node-to-baseline), seeing the held V directly. The **only SERIES** reactance is the bond inductor `L_cell` — where the B-side Lenz DC-block lives. No ε-side series-C dual. | `device-circuit-models.md`:52; `per-dof-vacuum-node-circuit.md`:30-34; `relativistic-inductor.md` ("Why SPICE Cannot Exceed c") |
| **M2** MODE/LEDGER | Static energy on a linear spectator mode outside the kernel? | **NO — H2 ledger cannot close.** The held `½ε₀E²` sits **IN** the shunt varactor (the kernel-bearing ε element); one `(L,C)` pair per translation DOF, **no** linear spectator capacitance to park it on. `residual_on_linear_mode = 0`. | `per-dof-vacuum-node-circuit.md`:30-34 (one `(L_i,C_i)` per DOF) |
| **M3** SLIDE | Lossless quiescent slide preserving tangent stiffness? | **NO — FAILS losslessly.** The small-signal differential (tangent) capacitance under bias is `C_ss=C₀/S(A₀)³` (leading `+3/2 A₀²`) — it **CHANGES** under held bias; no lossless soft mode slides `A₀→0` while V is held; the only relaxation (`τ_relax` hysteresis) **dissipates** (Ax3-forbidden). | `device-circuit-models.md`:60 (`C_ss=C₀/S³` vs chord `C_eff=C₀/S`); `tau-relax`:24 |

**M2 and M3 are the same mechanism in two coordinates** (the fire order anticipated this): both ask
whether the held field-energy can be made invisible to the kernel. M2 asks it as *energy bookkeeping*
(is there a spectator mode? — no), M3 asks it as *tangent stiffness* (does a probe see a change? — yes,
`C₀/S³`). Both say the held field is genuinely IN the saturating element. Reconciled.

## THE DERIVATION CHAIN (blind; sympy; ReconcileGate can-fire proven)

**M0 — the local kernel integrates the MEAN-SQUARE (the load-bearing symbolic result).** For a cell at
instantaneous operating point `A_V(t) = a_0 + a_1 cos(ωt)`, the ε-kernel deficit `1 − S(A_V) = 1 −
√(1−A_V²)`. Cycle-averaging and expanding at leading (2nd) order in both amplitudes (sympy series in
`ε` after `a_i → ε a_i`): `⟨1−S⟩_lead = a_0²/2 + a_1²/4 = ½(a_0² + a_1²/2) = ½⟨A_V²⟩`. The mean-square
`⟨A_V²⟩ = a_0² + a_1²/2` keeps the DC baseline `a_0²`; the variance `Var_t = a_1²/2` drops it. The
kernel keeps it because it is a **local function of the instantaneous phase-plane radius** (the forced
L2 invariant, `axiom-register`:188) — it never subtracts a running mean. The DC-only deficit
(`a_1→0`) is `1−√(1−a_0²) = a_0²/2 + O(a_0⁴) > 0` for any `a_0>0`: **a held DC alone loads ε.**

**Counterfactual (the gate can fire — round-2 lesson, no `Var(cos)=½` tautology).** A hypothetical
variance-keyed kernel (subtract the cycle-mean before squaring) gives `½·Var_t`, which is **ZERO on a
held DC** (`a_1=0`). The canonical sqrt-kernel gives `1−√(1−a_0²) > 0` on the SAME held DC. **They
disagree** (`0.0202 ≠ 0` at `a_0=0.2`), so the mean-square verdict is a real property of the sqrt
kernel — had the network forced H2, this counterfactual would have matched the zero and the routing
would differ (`counterfactual_can_fire` in the driver).

**Frequency-independence (sub-answer iv, ReconcileGate).** `⟨A_V²⟩ = a_0² + a_1²/2` is amplitude,
frequency-INDEPENDENT. Numeric (numpy time-domain, an independent path) vs symbolic `a_0²+a_1²/2`
across `ω/ω_C ∈ {1e-3, 1e-2, 0.1, 0.5}`: `max_rel = 2.0×10⁻¹⁶`, `can_fire_proven = True`. Spread across
`ω` is `< 1e-9`. **No `(ω/ω_C)²` rate factor is smuggled back** — `𝒲_beat` stays dead (round-2 LEVEL-1
preserved).

**M1 — the topological asymmetry (confronting the fire-order asymmetry problem §0.2 head-on).** The
naive ε↔µ dual FAILS, and M1 shows exactly why in the network: the SERIES reactance is the **bond
inductor** (the µ-grade's element), whose keying variable (circulation `I_vac`) has a zero static limit
by Lenz (`node-up`:119-123,:364). The ε-grade's element is the **shunt capacitor** — it has no series
partner whose static limit vanishes. The asymmetry is TOPOLOGICAL: *series-inductive on the B-side,
shunt-capacitive on the E-side.* There is no ε-side series-C to "charge once and block." This is the
canonical-structure reason the B-side is `[WORKED-DERIVED]` and the E-side cannot be.

## THE DUAL S_B (Route C, consumed — the CANON-EXACT template; §7)

`S_µ = √(1 − A_I²)`, `A_I = |∮H·dℓ|_norm/I_max`, `I_max = ξ_topo·c ≈ 124.4 A`. Static B → `∂_tB=0` →
`I_vac=0` → `A_I=0` → `S_µ=1` **analytically exact** (`node-up`:364, `[WORKED-DERIVED]`). **The duality
FAILS on the E-side, and M1 says why:** the B-side DC-block is the SERIES inductor's zero static
circulation; the E-side has no series element, its varactor is SHUNT and sees the held V directly. So
the E-side is NOT the dual of the B-side — the asymmetry is real and topological, not an oversight. The
B-side is charge-blind because its keying variable (circulation) is dynamically sourced; the E-side is
charge-KEYED because its keying variable (node potential) is directly sourced. This is precisely the
"capacitor static limit is nonzero by definition of ε" that the fire order (§0.2) flagged.

## CONSISTENCY-VS-EMERGENCE CLASSIFICATION

**CONSISTENCY-class.** The routed CHARGE-KEYED verdict is a **consistency identity of the network
topology + the axiom-level kernel-argument definition** — the ε-varactor is what it is (a shunt element
keyed on the static-capable node potential), so it keys on the mean-square. Finding NO DC-block is a
consistency finding (the network simply lacks the ε-side series element). No new dimensionful number is
minted; the only constants used (`ω_C, ℓ_node, Z₀, E_yield`) are imported and appear only in the
slow-ramp timescale and dimensionless bands. The gauge-relativity rider is likewise a re-expression of
the canonical INVARIANT-S2 (the PHASE-ONLY north-star mechanized), not a new mechanism.

## KNIFE CHECKS (armed)

- **½/¼ derived-only:** the `½` in `½⟨A_V²⟩` is the leading-order coefficient of `1−√(1−A²)=A²/2` (sympy
  `mean_leading`), declared-derived; the `a_1²/2 = Var(cos)·a_1²` factor is the cosine variance identity,
  declared. No new `½`/`¼` asserted. The `3/2` in `C_ss` leading (`M3`) is the sympy expansion of
  `1/S³`, traced.
- **ω_C/9-class thresholds:** the derivation reproduces NO `9·ℓ_node` defeat-scale (a §9-comparison
  object); the charge-keyed verdict needs no cutoff — it just loads.
- **2/7, 9.7734, √8:** none appear in any ε-coefficient (all coefficients are `½`, `¼`, `3/2` from the
  sqrt-kernel expansion; sector-guard clean).
- **`a_0=0.3` spot-check disclosure (blindness honesty).** `held_dc_local_deficit_at_a0_0p3 = 0.046` in
  the driver is an ILLUSTRATIVE spot-check of the DC-only deficit formula `1−S(0.3)`, chosen to match
  round-2's crux number for continuity — NOT a tuning to any experimental value. The routing does not
  depend on it (it is a display of the formula at one point). Flagged here per the blindness rule.
- **Null-verdict liveness (trigger 10):** the §9 muon pipeline returns a nonzero finite shift
  (`1.52×10⁶ µeV`), proving the overshoot is physics, not a zero-for-everything bookkeeping.

## SECTOR HEADER + HOMONYM GUARD (honored)

- **ε-grade = transverse-T2 permittivity channel** (the varactor `C_eff=C₀/S(A_V)`, `A_V=V/V_yield`).
  **NOT** the A1 dilatation-MASS varactor (keyed on `V/V_snap`); **NOT** the mechanical Q-point sector;
  **NOT** an E-gradient's mechanical force on cells (the A1 momentum ledger — explicitly out of scope).
- **"A²" homonym** resolved: (i) Ax4 kernel arg, (ii) Letter `(E/E_c)²`, (iii) mechanical bond strain,
  (iv) round-1 `𝒯`, (v) round-2 `𝒲`, (vi) THIS round's `⟨A_V²⟩` mean-square vs `Var_t(A_V)` variance —
  named distinctly throughout.

## DISCIPLINE

- **Rule 11 honest closure:** no post-hoc criterion drops. The E-side rescue via a Lenz-dual DC-block is
  reported DEAD — the network forces the mean-square; one mechanism (the ε element is a shunt keyed on
  the static-capable node potential, with no lossless way to shed a held bias) explains all four
  verdicts. The variance member is DERIVED-AGAINST, not rescued.
- **Rule 12 substitution-not-retraction:** round 2's `[SELECTED-NOT-DERIVED]` is preserved (git); this
  is a NEW derivation with its own prereg + verification chain that RESOLVES the round-2 open member
  (toward charge), NOT a refill of round-2's slot.
- **flag-don't-fix:** the corpus R2 `node-up`:217 ("a static E loads ε") is CONFIRMED by this derivation
  at the local ledger (it DOES load) — no contradiction to surface there; the tension with #539 is
  resolved not by making the E-side DC-blind but by the **uniform-vs-non-uniform** distinction (§9): a
  uniform lab DC is gauge-hidden, a non-uniform atomic Coulomb field is not. See the CORPUS section.
- **substrate-adjudicates-forks:** the member fork (mean-square vs variance) is closed BY the network
  (M0/M1/M2/M3), not by fiat or by Table-I survival.
- **verify-before-cite:** every constant live-imported from `ave.core.constants` at worktree HEAD;
  #539 machinery + Route C reused by import; every KB cite grepped at HEAD `d70446ae`.
- Two independent code paths (sympy analytic + numpy time-domain) + ReconcileGate (can-fire proven,
  derived tolerance) + a live counterfactual; `make verify` green; 8 fast-core + 2 engine_sim tests.

---

## §9 POST-DERIVATION COMPARISON (FIREWALLED — written after the blind routing above)

> Per the prereg §9, [DERIVED: CHARGE-KEYED] ⟹ "the E-side rescue is dead; #539 [C-EXCLUDED] + the
> Letter's protective-cutoff reading stand as the complete story; say so plainly." Confirmed:

- **The muon LOADS under CHARGE-KEYING.** The muonic-H Coulomb field is static-in-TIME but has a large
  SPATIAL gradient (its `A_V(r)=E(r)/E_yield` spans ~2 decades across the atom, from ≈0.63 at 0.5 a_µ to
  ≈0.006 at 5 a_µ). Under the derived mean-square (charge) local ledger it loads: the #539 continuum
  interior-excluded bracket integral gives `1.52×10⁶ µeV`, overshooting the 2.3 µeV CREMA window by
  **~6.6×10⁵×** — reproducing **#539 [C-EXCLUDED]** (machinery consumed by import).
- **The uniform-bias gauge rider does NOT rescue the muon.** Gauge cancellation (`INVARIANT-S2`) applies
  ONLY to a spatially-uniform held bias; the muon's giant `∇A` is readable. So the rider explains why a
  UNIFORM lab DC E gives no readable shift (the PHASE-ONLY north-star) WITHOUT reviving the H2/variance
  member or rescuing the muon.
- **The round-2 conditional-PASS does NOT become derived.** It required the SELECTED variance member
  (static-in-time → blind). The network forces the mean-square (charge) member, so the muon (non-uniform
  Coulomb) loads and #539 [C-EXCLUDED] stands. **The Letter's protective hard-cutoff reading and #539
  [C-EXCLUDED] are the complete story.**

## CORPUS-STATE UPDATE (surfaced to the auditor lane — NOT landed here; NO edit to `manuscript/ave-kb/**`)

The auditor lane lands these; I surface the empirical finding (no supersession of node-up:217 is staged —
CHARGE-KEYED CONFIRMS it):

1. **`node-up-small-large-signal.md`:217-218 STANDS as-is** — "a static E is a real operating-point bias
   for the V-keyed varactor — it loads ε" is CONFIRMED by this derivation at the local cell ledger. The
   round-2 KEEP-BOTH R2′ (a WORKED-keyed / DC-blind variant) is **NOT admissible for the corpus**: the
   canonical network does not force it (M0/M1/M2/M3), and a lossless ε-side Lenz-dual DC-block **does not
   exist**. Recommend: DROP the round-2 "R2′ candidate" from the auditor queue as [DERIVED-AGAINST]; the
   legacy amplitude-keyed R2 is the derived answer.
2. **The reconciliation of R2 with #539** is the **uniform-vs-non-uniform** distinction, not a keying
   change: a spatially-UNIFORM held DC E is gauge-hidden (INVARIANT-S2 / claim-quality:1318, the
   PHASE-ONLY north-star — "every AVE-distinct observable is an AC reading of a DC gradient or topology");
   a NON-uniform held field (atomic Coulomb, a bench fringe) is readable and loads. This is a candidate
   additive note on the R2 leaf (a scoping clarification: "R2 loads on the local mean-square amplitude;
   a spatially-uniform held bias is gauge-unobservable, a gradient is not") — surfaced for Grant/auditor
   to land, NOT written here. It is a CONSISTENCY re-expression of INVARIANT-S2, not a new claim.
3. **The Letter** — its protective hard cutoff for the E-route on atomic scales is the correct reading
   under CHARGE-KEYING (the E-varactor loads on held amplitude; the cutoff scopes it away from atomic
   overshoot). No change recommended beyond noting the round-3 derivation as the substrate basis.
