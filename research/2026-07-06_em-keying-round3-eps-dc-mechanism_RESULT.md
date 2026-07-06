# EM keying ROUND 3 — the ε-side DC-mechanism: CHARGE-KEYED vs EXCURSION-KEYED — RESULT

**Date:** 2026-07-06 · **Lane:** implementer · **Branch:** `analysis/em-keying-round3-eps-dc-mechanism`
**FROZEN prereg (gated on):** `research/2026-07-06_em-keying-round3-eps-dc-mechanism_prereg_FROZEN.md`
(freeze commit `942c950b`, committed before any result — git ordering = freeze proof).
**Drivers (two files; sympy + numpy; four ReconcileGates can-fire proven; constants imported):**
- `src/scripts/verify/em_keying_round3_mechanism.py` — the BLIND structural derivation. M0 (sympy
  mean-square), M1 (two-topology TIME-DOMAIN DC-response, COMPUTED), M2 (two-route energy ledger,
  COMPUTED), M3 (T2-sector tangent + a lattice-level zero-mode rigidity check) + the four mandatory
  sub-answers (slow-ramp is a REAL time-domain integration at 4 ramp rates). NO muonic/CREMA/#539/
  Table-I/PVLAS reference (hard firewall).
- `src/scripts/verify/em_keying_round3_comparison.py` — the FIREWALLED §9 comparison (muon vs the
  derived key), permitted to touch #539 ONLY here; consumes the #539 machinery by import.
**Tests:** `src/tests/test_em_keying_round3_eps_dc_mechanism.py` (9 fast-core gating asserting COMPUTED
outputs + 2 engine_sim standing falsifiers; the second falsifier is keyed to the M1 two-topology
DC-response, replacing a prior fixed identity — 11 total).

## ROUTED BIN: **[DERIVED: CHARGE-KEYED]** (single-cell + lattice-rigid; with a UNIFORM-bias gauge-observability RIDER)

> The ε-grade (transverse-T2 permittivity channel) nonlinearity keys on the **MEAN-SQUARE** of the
> instantaneous field amplitude at the cell — **DC-INCLUDED** (H1/CHARGE-KEYED), **at leading (2nd)
> order** (the `⟨1−S⟩ = ½⟨A_V²⟩` identity is 2nd-order; a Jensen gap opens at `O(A⁴)`, DC baseline
> retained either way). The variance/excursion member (H2) is **NOT forced** by the canonical network:
> all four candidate mechanisms (M0/M1/M2/M3) fail to deliver a lossless DC-block, and the lattice-level
> zero-mode question is **settled CLOSED (rigid)** — the K4 translational (E-coupled) sector carries
> shear stiffness `k_s>0`, so no floppy zero-mode absorbs a held strain (`k4-bloch-dispersion-quartic`:58).
> The E-side "worked-keying" rescue (a Lenz-dual DC-blindness for the varactor) **does not exist in the
> canonical structure**. The round-2 `[SELECTED-NOT-DERIVED]` variance member is therefore
> **DERIVED-AGAINST**: the network selects the mean-square, not the variance.
>
> **RIDER (CANON-CONSISTENT, NOT DERIVED-HERE — a real refinement, not a rescue):** a spatially-**UNIFORM**
> held DC bias self-cancels on READOUT — the A-state is **gauge-relative** (`manuscript/ave-kb/CLAUDE.md`
> INVARIANT-S2:75, VERBATIM *"only spatial gradients of A across the substrate are physically observable, not absolute
> per-node values"*), so a uniform offset is unobservable (= the PHASE-ONLY north-star, `claim-quality.md`
> :1318 VERBATIM *"All measurement is AC — a uniform DC bias is gauge-relative and self-cancels (= relativity …)."*).
> This is a **re-statement of the canonical INVARIANT-S2 applied to the asymmetric ε-only load**, NOT a
> fresh derivation on this branch. It is not a stretch: `manuscript/ave-kb/CLAUDE.md`:75 already scopes the static-E-only
> (asymmetric) case verbatim — *"A **static-E-only drive is ASYMMETRIC** … it loads the $\varepsilon$ /
> capacitive sector only ($S_\varepsilon < 1$, $S_\mu = 1$)"* — so the ε-only load is canon-covered.
> It is an **OBSERVABILITY** statement (differential readout), NOT a claim that the local ledger is
> excursion-keyed. The local cell IS deficient under a uniform bias (charge-keyed); you just cannot READ
> it without a gradient (a co-located wave-made ruler rides the same offset). A **NON-uniform** held field
> (a real bench fringe, an atomic Coulomb field) has a nonzero `∇A` and IS readable and DOES load.
>
> **The discriminating readout (finding [16] — the rider is falsifiable, not metaphysics).** "Uniformly
> loaded but gauge-hidden vs not loaded" is distinguished in canon by the **Op14 Meissner-asymmetric
> impedance mirror**: a static-E-only load gives `Z_eff = Z_0·√(S_μ/S_ε)` with `S_ε<1, S_μ=1`, so `Z`
> changes and a boundary **reflects (`Γ≠0`)** — the vacuum-impedance-mirror bench mechanism
> (`manuscript/ave-kb/CLAUDE.md`:75 VERBATIM *"$Z$ **changes**, so the boundary reflects ($\Gamma \neq 0$): this is the
> vacuum-impedance-mirror bench mechanism (Vol 4 Ch 11)"*; `operators.md`:54 canonical asymmetric form).
> A truly UNIFORM load reflects nowhere it can be read differentially; a NON-uniform (gradient) load
> presents an impedance step that DOES reflect. That reflection `Γ≠0` at an ε-gradient boundary is the
> readable observable node-up:217 calls *"shifts $n$"* — differential by principle.

## THE DERIVED KEYING STATEMENT (verbatim; sub-answer iii — EXACTNESS)

$$
\boxed{\;
\big\langle 1 - S_\varepsilon(A_V)\big\rangle \;\stackrel{O(A^2)}{=}\; \tfrac12\,\mathcal{K}, \qquad
\underbrace{\mathcal{K} \;=\; \big\langle A_V(t)^2 \big\rangle
   \;=\; \Big(\tfrac{V_0}{V_{yield}}\Big)^2 + \tfrac12\Big(\tfrac{V_1}{V_{yield}}\Big)^2}_{\textbf{MEAN-SQUARE — DC-included (H1/CHARGE-KEYED), AT LEADING (2nd) ORDER}}
\;\;\ne\;\;
\underbrace{\operatorname{Var}_t(A_V) = \tfrac12\Big(\tfrac{V_1}{V_{yield}}\Big)^2}_{\text{variance (H2) — NOT what the network forces}}
\;}
$$

for a cell driven `V(t) = V_0 + V_1 cos(ωt)` (`V_0` = held DC baseline, `V_1` = AC excursion). At
leading (2nd) order the kernel deficit the varactor integrates is
`⟨1 − S(A_V)⟩ = ½⟨A_V²⟩ = ½(a_0² + a_1²/2)` — **exactly the mean-square, NOT the variance, AT LEADING
(2nd) ORDER** (sympy, `m0_axiom_argument`; `mean_leading = a0²/2 + a1²/4 = ½·mean_square`). This is a
LEADING-order equality: at `O(A⁴)` a Jensen gap opens between `⟨1−S⟩` and `½⟨A_V²⟩` (the sqrt kernel is
concave), but both objects keep the DC baseline `a_0²`, so the H1-vs-H2 routing is unchanged by the
higher-order gap — only the *exact* `½⟨A_V²⟩` identity is 2nd-order. The two objects differ by the DC
baseline `a_0²`: the mean-square keeps it (charge), the variance subtracts it (excursion). **The network
keeps it.** This is exactly the object round-2 named at its crux (`⟨A_V²⟩/2` = mean-square,
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
| **M0** NULL | Is `A` axiom-defined on a static-capable variable ⟹ H1 forced? | **YES → H1.** The ε-kernel argument is `A_V=V/V_yield=|E|/E_yield`, a static-capable amplitude; the leading (2nd-order) mean deficit is `½·mean-square` (DC-included); a held DC alone gives deficit `a_0²/2>0`. H2 would need an **axiom-level reinterpretation**, flagged — not a network trick. | `node-up`:104-106,:117-118; `axiom-register` Axiom-4:186 (verbatim *"local strain $A$ (normalized to the bandwidth limit $A_{yield}$)"*), :188 (forced L2 invariant on the dynamical phase-plane radius) |
| **M1** TOPOLOGY | Series-C DC-block on the ε path? | **NO — FALSIFIED by topology (COMPUTED, two-topology).** The canonical **series-L-bond / shunt-C-node** unit passes the held DC to the varactor node (`V_node→V₀`, integrated); a **series-C-blocked** counterfactual relaxes it to zero (`V_node→0`) — they genuinely differ, so there is no ε-side DC-block. The **only SERIES** reactance is the bond inductor `L_cell` (a DC short) — where the B-side Lenz DC-block lives. Gate reconciles the canonical settled node voltage against the LC-ladder DC relation. | `graded-network-response.md`:50 (*"series $L$ per bond, shunt $C$ per node"*); :53 Resultbox (*"LC-ladder dispersion (lossless KCL/KVL, series-$L$ bond, shunt-$C$ node)"*); `z0-derivation.md`:133-136 (*"$C_{cell}=ε₀ℓ_{node}$ **is** the bond segment's own shunt capacitance … the repeated series-$L$ / shunt-$C$ unit"*); `relativistic-inductor.md`:30 ("Why SPICE Cannot Exceed $c$") |
| **M2** MODE/LEDGER | Static energy on a linear spectator mode outside the kernel? | **NO — H2 ledger cannot close (COMPUTED, two-route).** The held-field energy on the saturating shunt varactor, computed by **two independent routes** (charge-path element-energy sum vs constitutive Legendre co-energy), reconciles with **zero residual** — fully accounted IN the kernel-bearing ε element; one `(L,C)` pair per translation DOF, **no** linear spectator capacitance to park it on. Gate proven can-fire on a broken constitutive. | `per-dof-vacuum-node-circuit.md`:30-34 (per-DOF reactive pair, one `(L_i,C_i)` per translation DOF); `graded-network-response.md`:50/:53; `z0-derivation.md`:133-136 (single-ontology shunt-C, no separate node admittance) |
| **M3** SLIDE | Lossless quiescent slide preserving tangent stiffness? | **NO — FAILS losslessly (T2 sector, sign-corrected).** In the **transverse-T2 permittivity** direction the tangent capacitance under bias is `C_ss=C₀·S(A₀)` (leading `1 − ½A₀²`, **sign DOWN**) — it **CHANGES** under held bias; no lossless soft mode slides `A₀→0` while V is held; the only relaxation (`τ_relax` hysteresis) **dissipates** (Ax3-forbidden). The A1 `C₀/S³` (`+3/2 A₀²`) is the OUT-OF-SCOPE `V/V_snap` varactor. | `manuscript/ave-kb/CLAUDE.md`:73 (T2 direction: `ε_eff=ε₀S`, `C_diel∝S`); `tau-relax`:24. *(A1 `C_ss=C₀/S³` at `device-circuit-models.md`:60 is the `V/V_snap` sector — cross-sector borrow REMOVED; ERRATA §.)* |

**M2 and M3 are the same mechanism in two coordinates** (the fire order anticipated this): both ask
whether the held field-energy can be made invisible to the kernel. M2 asks it as *energy bookkeeping*
(is there a spectator mode? — no, two-route ledger closes with zero residual), M3 asks it as *tangent
stiffness* (does a probe see a change? — yes: T2 `C_ss=C₀·S(A₀)`, leading `1−½A₀²`). Both say the held
field is genuinely IN the saturating element. Reconciled.

**M3 at LATTICE level (finding [5] — settled CLOSED, rigid).** The single-cell M3 leaves open whether
a lattice zero-mode could losslessly absorb a held strain. Canon settles it cleanly: the K4 Bloch
dynamical matrix uses the RANK-2 bond tensor with axial `k_a` **and** transverse/shear `k_s`, and
`k4-bloch-dispersion-quartic.md`:58 states verbatim *"A pure central-force model ($k_s=0$) would carry
soft transverse-acoustic branches; the general-force-constant tensor restores all three linear acoustic
branches."* So a floppy (zero-frequency) transverse mode is the `k_s=0` **pure-central-force pathology**;
the canonical substrate carries `k_s>0` and is **rigid** in the translational (E-coupled) sector at the
cold small-A operating point (loaded-cold `C₄₄=0.177`, `electron-bh-isomorphism.md`:38). The near-yield
`A→1` floppiness (`C₄₄→4×10⁻⁵`, ibid.) is an **absolute-scale** collapse at the yield wall, NOT this
round's cold small-A regime. Verified numerically (driver `m3_lattice_zero_mode_from_canon`): the
transverse-acoustic branch speed is nonzero for `k_s>0` (rigid) and collapses to zero only for the
`k_s=0` pathology. **The single-cell M3 kill EXTENDS to the lattice.** This is the one place the
excursion-keyed alternative could have lived — it needed a floppy lattice zero-mode; there is none.

## THE DERIVATION CHAIN (blind; sympy; ReconcileGate can-fire proven)

**M0 — the local kernel integrates the MEAN-SQUARE (the load-bearing symbolic result).** For a cell at
instantaneous operating point `A_V(t) = a_0 + a_1 cos(ωt)`, the ε-kernel deficit `1 − S(A_V) = 1 −
√(1−A_V²)`. Cycle-averaging and expanding at leading (2nd) order in both amplitudes (sympy series in
`ε` after `a_i → ε a_i`): `⟨1−S⟩_lead = a_0²/2 + a_1²/4 = ½(a_0² + a_1²/2) = ½⟨A_V²⟩` (a LEADING-order
equality; the exact `⟨1−S⟩` and `½⟨A_V²⟩` differ at `O(A⁴)` by a Jensen gap, both keeping the DC
baseline, so the routing is unchanged). The mean-square
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

**M1 — the topological asymmetry, COMPUTED as a two-topology DC-response (confronting the fire-order
asymmetry problem §0.2 head-on).** The naive ε↔µ dual FAILS, and M1 shows exactly why by building BOTH
cell topologies as actual time-domain models: (a) the canonical **series-L-bond / shunt-C-node** unit
(`graded-network-response.md`:50 *"series $L$ per bond, shunt $C$ per node"*; :53 Resultbox; and
`z0-derivation.md`:133-136 *"$C_{cell}=ε₀ℓ_{node}$ **is** the bond segment's own shunt capacitance …
the repeated series-$L$ / shunt-$C$ unit"*), and (b) a counterfactual with a **series blocking
capacitor** inserted on the E-signal path. Integrating both under a held DC: the canonical unit passes
the held voltage to the varactor node (`V_node→V₀`, the series-L is a DC short), while the counterfactual
series-C relaxes the node to zero (`V_node→0`, charge-once-block). They **genuinely differ** — so the
canonical structure has NO ε-side series-C DC-block (a ReconcileGate reconciles the canonical settled
node voltage against the LC-ladder DC relation, proven can-fire). The SERIES reactance is the **bond
inductor** (the µ-grade's element), whose keying variable (circulation `I_vac`) has a zero static limit
by Lenz (`node-up`:119-123,:364); the ε-grade's element is the **shunt capacitor** with no such series
partner. The asymmetry is TOPOLOGICAL: *series-inductive on the B-side, shunt-capacitive on the E-side.*
This is the canonical-structure reason the B-side is `[WORKED-DERIVED]` and the E-side cannot be.

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
  declared. No new `½`/`¼` asserted. The `½` in the T2 `C_ss=C₀·S` leading (`1−½A₀²`, `M3`) is the sympy
  expansion of `S=√(1−A₀²)`, traced (the A1 `+3/2` from `1/S³` is the OUT-OF-SCOPE `V/V_snap` sector,
  not used in this round's routing).
- **ω_C/9-class thresholds:** the derivation reproduces NO `9·ℓ_node` defeat-scale (a §9-comparison
  object); the charge-keyed verdict needs no cutoff — it just loads.
- **2/7, 9.7734, √8:** none appear in any ε-coefficient (the T2 coefficients are `½`, `¼` from the
  sqrt-kernel expansion; sector-guard clean).
- **`a_0=0.3` spot-check disclosure (blindness honesty).** `held_dc_local_deficit_at_a0_0p3 = 0.046` in
  the driver is an ILLUSTRATIVE spot-check of the DC-only deficit formula `1−S(0.3)`, chosen to match
  round-2's crux number for continuity — NOT a tuning to any experimental value. The routing does not
  depend on it (it is a display of the formula at one point). Flagged here per the blindness rule.
- **Null-verdict liveness (trigger 10):** the blind derivation's gates are proven can-fire on
  synthetic-discrepancy inputs (M1 two-topology, M2 two-route, slow-ramp, frequency-independence); the
  positive-control liveness of the §9 muon pipeline is recorded BELOW the firewall (§9), not here.

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
- **flag-don't-fix:** the corpus R2 `node-up`:217 (full verbatim: *"A static $\mathbf E$ is a real
  operating-point bias for the $V$-keyed varactor — it loads $\varepsilon$ and shifts $n$"*) is CONFIRMED
  by this derivation at the local ledger (it DOES load). The dropped clause **"and shifts $n$"** is exactly
  the readable observable the uniform-bias rider argues is gauge-hidden for *uniform* loads — see the
  RIDER-OBSERVABILITY flag below, which confronts it head-on rather than eliding it. (Any comparison to a
  specific experimental result is deferred to the firewalled §9.)
- **RIDER-OBSERVABILITY (flag, confronted not elided):** node-up:217's *"shifts $n$"* is a REAL readable
  index shift **for a NON-uniform held E** (the shift is a gradient of `S(A)`, and `∇A` is the observable,
  `manuscript/ave-kb/CLAUDE.md`:75). For a **spatially-uniform** held E the local `n` shifts *identically everywhere*, so a
  co-located wave-made ruler rides the same offset and the shift is gauge-unobservable (`manuscript/ave-kb/CLAUDE.md`:75
  INVARIANT-S2). This is NOT a contradiction with the local charge-keyed ledger (the cell IS loaded); it
  is the uniform-vs-gradient observability split. The discriminating readout that makes this falsifiable
  (not metaphysics) is named in the RIDER box below.
- **CLUSTER-B CAPACITANCE-TENSION (flag-don't-fix — surfaced for Grant, NOT resolved here):** the corpus
  carries a live symbol-sharing tension in the `C_eff=C₀/S` assignment. `node-up-small-large-signal.md`:104
  (Resultbox) and :360 (status table) label **`C_eff(V)=C₀/S(A_V)`, `A_V=V/V_yield`** as the
  **"ε-grade: VARACTOR, keyed on VOLTAGE"** — verbatim :104: *"$C_{eff}(V) = \frac{C_0}{S(A_V)}, \quad
  A_V = \frac{V}{V_{yield}}$ … $\varepsilon$-grade: VARACTOR, keyed on VOLTAGE"*. But `manuscript/ave-kb/CLAUDE.md`:73
  (Grant-ratified sector split, 2026-06-15) assigns **`C_eff=C₀/S` (↑) to the longitudinal-A1 bond
  compliance** and **`ε_eff=ε₀·S` (↓, `C_diel∝S`) to the transverse-T2 permittivity** — verbatim :73:
  *"$C_{eff}=C_0/S$ (↑) is the **longitudinal-A1 bond compliance** … a DISTINCT object from the
  **transverse-T2 permittivity** $\varepsilon_{eff}=\varepsilon_0 S$ (↓; the LCR-measured cell capacitance
  $C_{diel}=\varepsilon_{eff}A/d\propto S$ …)"*. So node-up calls `C₀/S(A_V=V/V_yield)` the ε-grade
  varactor, while CLAUDE.md reserves `C₀/S` for A1 and gives T2 the `C_diel∝S` form. This round derived M3
  in the **CLAUDE.md T2 direction** (`C_diel=C₀·S`), which is why the M3 sign flipped from the round-3
  prereg's A1-borrowed `C₀/S³`. **Surfaced for Grant's adjudication; not resolved here** (per lane
  discipline — this is a corpus-consistency call, not an engine bug).
- **substrate-adjudicates-forks:** the member fork (mean-square vs variance) is closed BY the network
  (M0/M1/M2/M3 + the lattice-level rigidity check), not by fiat or by Table-I survival.
- **verify-before-cite:** every constant live-imported from `ave.core.constants` at worktree HEAD; Route C
  reused by import; every KB cite re-grepped verbatim at branch tip (M1/M2 anchors corrected this round —
  see ERRATA). The firewalled §9 machinery is imported only below the firewall.
- Two independent code paths (sympy analytic + numpy time-domain) + four ReconcileGates (M1 two-topology,
  M2 two-route, slow-ramp, frequency-independence — all can-fire proven; tolerances are engineering
  choices scaled to the numeric method, honestly tagged per prereg ERRATA-5, NOT canonically derived) + a
  live counterfactual; `make verify` green; **9 fast-core + 2 engine_sim tests = 11 total** (up from 8+2:
  the fast-core grew by the M1 two-topology, M2 two-route, M3 lattice-rigidity, and slow-ramp COMPUTED
  gates; the second engine_sim falsifier is now keyed to the M1 two-topology DC-response, replacing a
  prior fixed identity).

---

## §9 POST-DERIVATION COMPARISON (FIREWALLED — written after the blind routing above)

> Per the prereg §9, [DERIVED: CHARGE-KEYED] ⟹ "the E-side rescue is dead; #539 [C-EXCLUDED] + the
> Letter's protective-cutoff reading stand as the complete story; say so plainly." Confirmed:

- **The muon LOADS under CHARGE-KEYING.** The muonic-H Coulomb field is static-in-TIME but has a spatial
  gradient. Under the derived mean-square (charge) local ledger it loads: the #539 continuum
  interior-excluded bracket integral gives `1.52×10⁶ µeV`, overshooting the 2.3 µeV CREMA window by
  **~6.6×10⁵×** — reproducing **#539 [C-EXCLUDED]** (machinery consumed by import).
- **Muon non-uniformity, quantified properly (finding [18] — the gradient scale vs the node pitch).** The
  relevant non-uniformity measure is the LOCAL GRADIENT SCALE `L_grad = A_V/|∇A_V| = r/2` (for a `1/r²`
  Coulomb field), compared to `ℓ_node = 386 fm`, NOT a raw amplitude span. This is honest about where the
  gradient is lattice-resolvable:
  - at `r = 0.5 a_µ = 142 fm` (`0.37 ℓ_node`): `A_V ≈ 0.63`, `L_grad = 71 fm = 0.18 ℓ_node` — **the field
    varies faster than one node pitch; the inner sample point sits INSIDE a single node pitch** (`0.37
    ℓ_node < ℓ_node`). This is precisely the interior the #539 continuum arm **excludes** — the continuum
    `∇A` is not lattice-meaningful there, and no sub-node "gradient" claim is made. Handled honestly: the
    interior is excluded, not counted as readable gradient.
  - at `r = 2 a_µ = 569 fm` (`1.48 ℓ_node`): `L_grad = 285 fm = 0.74 ℓ_node`; at `r = 5 a_µ`: `L_grad =
    712 fm = 1.84 ℓ_node`. **Outside the interior the gradient scale reaches ~1–2 node pitches**, where
    `∇A` IS lattice-resolvable and the field is genuinely non-uniform (multi-cell). This is the region
    that carries the readable load and drives the overshoot.
  So the muon's non-uniformity is REAL but only in the interior-excluded-outward region; the amplitude
  "~2 decades" figure is replaced by the gradient-scale statement, and the inner point inside one node
  pitch is flagged and handled by interior exclusion (consistent with #539's most-forgiving arm).
- **The uniform-bias gauge rider does NOT rescue the muon.** Gauge cancellation (`INVARIANT-S2`) applies
  ONLY to a spatially-uniform held bias; the muon's `∇A` (gradient scale ~1–2 `ℓ_node` outside the
  interior) is readable — the Op14 Meissner-asymmetric impedance step `Γ≠0` is present. So the rider
  explains why a UNIFORM lab DC E gives no readable shift (the PHASE-ONLY north-star) WITHOUT reviving the
  H2/variance member or rescuing the muon.
- **The round-2 conditional-PASS does NOT become derived.** It required the SELECTED variance member
  (static-in-time → blind). The network forces the mean-square (charge) member, so the muon (non-uniform
  Coulomb) loads and #539 [C-EXCLUDED] stands. **The Letter's protective hard-cutoff reading and #539
  [C-EXCLUDED] are the complete story.**
- **Null-verdict liveness (trigger 10, recorded BELOW the firewall).** The §9 muon pipeline returns a
  nonzero finite shift (`1.52×10⁶ µeV`), proving the overshoot is physics, not a zero-for-everything
  bookkeeping. (Moved here from the blind KNIFE-CHECKS section per finding [9]: no muon/#539 comparison
  quantity appears above the §9 firewall header.)

## CORPUS-STATE UPDATE (surfaced to the auditor lane — NOT landed here; NO edit to `manuscript/ave-kb/**`)

The auditor lane lands these; I surface the empirical finding (no supersession of node-up:217 is staged —
CHARGE-KEYED CONFIRMS it):

1. **`node-up-small-large-signal.md`:217-218 STANDS as-is** — VERBATIM :217: *"A static $\mathbf E$ is a
   real operating-point bias for the $V$-keyed varactor — it loads $\varepsilon$ **and shifts $n$**"* — is
   CONFIRMED by this derivation at the local cell ledger. The **"and shifts $n$"** clause is retained here
   in full: it is the readable index shift, which for a NON-uniform held E is a gradient of `S(A)` (`∇A`
   observable) and is the very observable the uniform-bias rider scopes as gauge-hidden ONLY for a uniform
   load. The round-2 KEEP-BOTH R2′ (a WORKED-keyed / DC-blind variant) is **NOT admissible for the
   corpus**: the canonical network does not force it (M0/M1/M2/M3 + lattice-rigid), and a lossless ε-side
   Lenz-dual DC-block **does not exist**. Recommend: DROP the round-2 "R2′ candidate" from the auditor
   queue as [DERIVED-AGAINST]; the legacy amplitude-keyed R2 is the derived answer.
2. **The reconciliation of R2 with #539** is the **uniform-vs-non-uniform** distinction, not a keying
   change: a spatially-UNIFORM held DC E is gauge-hidden (INVARIANT-S2 / `claim-quality.md`:1318, the
   PHASE-ONLY north-star — VERBATIM *"Every AVE-distinct observable is an AC reading of a DC gradient or
   topology — differential BY PRINCIPLE, not by experimental limitation (the PHASE-ONLY north-star,
   mechanized)."*); a NON-uniform held field (atomic Coulomb, a bench fringe) is readable and loads. This
   is a candidate additive note on the R2 leaf (a scoping clarification: "R2 loads on the local
   mean-square amplitude at leading order; a spatially-uniform held bias is gauge-unobservable, a gradient
   is not — the discriminating readout is the Op14 Meissner-asymmetric impedance mirror `Γ≠0`") — surfaced
   for Grant/auditor to land, NOT written here. It is a CONSISTENCY re-expression of INVARIANT-S2, not a
   new claim.
3. **The Letter** — its protective hard cutoff for the E-route on atomic scales is the correct reading
   under CHARGE-KEYING (the E-varactor loads on held amplitude; the cutoff scopes it away from atomic
   overshoot). No change recommended beyond noting the round-3 derivation as the substrate basis.
