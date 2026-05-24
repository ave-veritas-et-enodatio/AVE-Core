# Item 3 (Chirality Projection Sub-Theorem) — Focused Plan

**Status:** PLAN. Item 3 of [`L3_PHASE3_NEXT_STEPS_PLAN_20260421.md`](../../.agents/handoffs/L3_PHASE3_NEXT_STEPS_PLAN_20260421.md).
Following the same posture that worked for Theorem 3.1: research the
corpus first (~80% of the work is already documented), then derive
the missing bridge.

---

## §1 Context

The (2,3) torus knot embedded on K4 has a definite handedness that
distinguishes electron from positron. The electron's macroscopic
chirality observable (per AVE-HOPF antenna prediction) is
`Δf/f = α·pq/(p+q)`, which for (2,3) gives `α·6/5 = 1.2α ≈ 8.76×10⁻³`.
Per [`research/L3_electron_soliton/10_chirality_accounting_narrative.md:56-85`](10_chirality_accounting_narrative.md#L56),
chirality is sign/phase convention on cross-couplings (orthogonal to
scalar Q-factor); same Z₀ and α⁻¹ for electron and positron, opposite
sign of one specific coupling.

**Goal:** Derive the explicit projection formula by which K4
node-scale right-handedness (`det[p₀, p₁, p₂] = +4` on A-sublattice
ports) accumulates along the closed (2,3) torus-knot path to produce
the empirical `α·pq/(p+q)` macroscopic chirality factor.

---

## §2 What's already in the corpus

### §2.1 The DIRECT precedent — delta-CP path-accumulation (KB)

[`manuscript/ave-kb/vol2/particle-physics/ch03-neutrino-sector/delta-cp-violation.md:7-19`](../../manuscript/ave-kb/vol2/particle-physics/ch03-neutrino-sector/delta-cp-violation.md#L7):

> "The CP-violating phase accumulates three contributions as the
> torsional mode propagates through the chiral K4 lattice:
>
>     δ_CP = (1 + 1/3 + 1/45)π = 61π/45
>
> - π: base phase (unknot half-turn)
> - π/3: one K4 bond's share of structural chirality. Because the
>   lattice is 3-connected, each bond carries 1/3 of total chiral phase
> - π/45: junction coupling phase"

**This is the path-accumulation pattern.** Per-bond chirality
contribution = (lattice connectivity)⁻¹ × (one full chiral cycle).
For K4 with 4-port connectivity, each bond carries 1/4 of total
chirality; sum over the (p,q) torus knot's bonds gives the path
chirality. The harmonic mean `pq/(p+q)` should fall out of
counting bonds along the (p,q) winding.

### §2.2 The phase-closure quantization

[`manuscript/ave-kb/vol2/nuclear-field/ch12-millennium-prizes/hodge-conjecture.md:16-46`](../../manuscript/ave-kb/vol2/nuclear-field/ch12-millennium-prizes/hodge-conjecture.md#L16):

> "For a standing wave to persist on a closed toroidal path, the
> accumulated phase over one complete circuit must return to its
> starting value: ∮_torus k·dl = 2πq, q ∈ ℤ"

Closed-path quantization. Selects integer windings; the (2,3)
satisfies this. The electron's chirality sign comes from which side
of the integer-winding identity is locked in.

### §2.3 The chirality-as-sign-convention principle

[`research/L3_electron_soliton/10_chirality_accounting_narrative.md:56-85`](10_chirality_accounting_narrative.md#L56):

> "Impedance Z = effort/flow magnitude (scalar). Chirality =
> sign/phase convention on cross-couplings... The electron as (2,3)
> soliton locks into ONE sign of coupling convention. Same Z₀, same
> Q-factor, same α⁻¹ — opposite handedness."

Critical foundational principle: chirality enters as a SIGN on the
ε_{ijk} cross-coupling terms (Levi-Civita in the Cosserat constitutive
tensor). NOT a separate impedance.

### §2.4 Universal chiral coupling 8πα

[`manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/chiral-factor.md:4-38`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/chiral-factor.md#L4):

> "p_c = 8π... For (p,q) torus knot, the chiral factor
> χ_knot = α × pq/(p+q)."

Statement of the formula at operator level. The `8π` is the
universal Cosserat packing-fraction factor; `α` is the saturation
limit; `pq/(p+q)` is the knot-specific geometric factor.

### §2.5 K4-TLM native chirality

[`manuscript/ave-kb/vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md:49,63`](../../manuscript/ave-kb/vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md#L49):

> "Native helicity density emergence matching α·pq/(p+q)... The
> native lattice directly confirms the fundamental isomorphism of
> Axiom 2 without employing arbitrary mathematical R(θ) modifiers."

Stated as numerically observed in K4-TLM simulation, no separate
derivation.

### §2.6 Engine infrastructure (all building blocks present)

| Component | File | What it does |
|---|---|---|
| `_hopf_density` | [`cosserat_field_3d.py:202-204`](../../src/ave/topological/cosserat_field_3d.py#L202) | FFT-based `½A·B` Chern-Simons density |
| Sign-tracked ε_{ijk} | [`cosserat_field_3d.py:72-83`](../../src/ave/topological/cosserat_field_3d.py#L72) | Cosserat strain with explicit ± signs |
| `harmonic_mean_winding(p,q)` | [`AVE-HOPF/scripts/beltrami_hopf_coil.py:43-44`](../../../AVE-HOPF/scripts/beltrami_hopf_coil.py#L43) | Returns `p*q/(p+q)` |
| `self_linking_number(p,q)` | [`beltrami_hopf_coil.py:47-49`](../../../AVE-HOPF/scripts/beltrami_hopf_coil.py#L47) | `pq − p − q` (Seifert framing) |
| `crossing_number(p,q)` | [`beltrami_hopf_coil.py:52-53`](../../../AVE-HOPF/scripts/beltrami_hopf_coil.py#L52) | `min(p(q−1), q(p−1))` |
| Port-tangent projection | [`tlm_electron_soliton_eigenmode.py:39-80`](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py#L39) | (2,3) knot tangent → tetrahedral port weighting |
| Phase advance per node | [`entanglement_thread.py:54-60`](../../src/ave/topological/entanglement_thread.py#L54) | `δφ = 2π/N` along thread |

---

## §3 What's missing — the bridge derivation

The corpus has the per-bond accumulation principle (delta-CP §2.1)
and the macroscopic formula (§2.4-2.5), but no explicit derivation
chain showing how the per-bond accumulation on a (p,q) torus knot
embedded on K4 produces specifically `pq/(p+q)`.

**Three sub-questions to close:**

1. **Why harmonic mean (not arithmetic, not geometric)?** The agent
   research surfaced this as the load-bearing physics gap. The
   harmonic mean appears in several places (chirality factor,
   parallel resistor combination, lens-formula, etc.), each with a
   specific physical origin. Which origin applies here?

2. **How does K4 connectivity enter?** Delta-CP uses 1/3 because K4
   is 3-connected at neutrino-sector scale. For the electron's (2,3)
   embedding, what's the effective connectivity factor?

3. **What's the explicit per-bond chirality contribution?** Each K4
   port has a definite chirality (right-handed tetrahedron). When a
   wave traverses N_bonds along the (p,q) knot, what's the
   accumulated phase, and how does it equal `α·pq/(p+q)`?

---

## §4 Derivation strategy

Two derivation paths, in increasing rigor:

### §4.1 Path A — Geometric counting (electron-plumber shortcut)

For a (p,q) torus knot:
- Total knot length = `L = ∮ |dl|` (along parametrized path)
- For unit-radius torus knot at Golden Torus, `L ∝ √(p² + q²)` to
  leading order (Pythagorean approximation)
- Number of K4 bonds traversed `N_bonds ≈ L / ℓ_node = L`
- Per-bond chirality contribution `χ_bond = 1/N_per_cycle` where
  `N_per_cycle` is the number of bonds in one chirality-return cycle
- Total chirality per cycle around the knot: `χ_total = N_bonds × χ_bond`

For the harmonic mean to emerge:
`pq/(p+q)` is the **harmonic mean** = `2/(1/p + 1/q)` divided by 2.
Equivalently `(1/p + 1/q)⁻¹`. This is the parallel-resistor /
parallel-impedance pattern.

**Hypothesis (to verify):** the (p,q) torus knot has TWO independent
winding directions (toroidal `p` and poloidal `q`), each carrying
its own chirality channel. The two channels combine in PARALLEL
(both leak through the same TIR boundary), giving:
```
1/χ_total = 1/χ_p + 1/χ_q = 1/(α·p) + 1/(α·q) = (p + q)/(α·pq)
χ_total = α·pq/(p+q)
```

This is the parallel-loss interpretation — analogous to two
resistors in parallel, the slower-leaking channel dominates and
gives the harmonic mean. Same physics as parallel-Q combinations.

### §4.2 Path B — Explicit path integral (rigorous)

1. Parametrize the (p,q) torus knot path on K4: `r(t) = ((R + r cos qt) cos pt, …)`
2. Discretize into K4 bonds: identify which bonds the path traverses
3. At each bond, compute the chirality contribution from the local
   tetrahedral handedness × the path's tangent projection
4. Sum over the closed path:
   ```
   χ_path = (1/N_cycle) ∮ p_node × t_path · n̂_normal ds
   ```
   where `p_node` is the K4 port basis at each node and `t_path` is
   the tangent.
5. Show this evaluates to `α·pq/(p+q)` for any (p,q) torus knot.

Path B is more rigorous but Path A's derivation may be enough if
the parallel-channel interpretation holds.

---

## §5 Concrete steps to execute

1. **Verify the parallel-channel hypothesis (§4.1) numerically** —
   write `src/scripts/vol_1_foundations/chirality_projection.py` that:
   - Computes `α·pq/(p+q)` for several (p,q): (2,3), (2,5), (3,5), (3,7), (3,11)
   - Computes `χ_p + χ_q`-style parallel combinations and compares
   - Verifies the harmonic mean structure
   - Cross-checks against AVE-HOPF table at
     [`AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex:72-82`](../../../AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex#L72)

2. **Per-bond chirality check** — for the (2,3) winding at Golden
   Torus, count K4 bonds traversed and verify per-bond accumulation
   gives the expected total. Use existing port-tangent projection
   from `tlm_electron_soliton_eigenmode.py` for the bond-counting.

3. **Sub-theorem doc** at
   `research/L3_electron_soliton/20_chirality_projection_sub_theorem.md`
   with structure:
   - §1 Statement (the projection formula)
   - §2 Corpus precedents (delta-CP, chiral factor, K4-TLM native)
   - §3 Path A derivation (parallel channels → harmonic mean)
   - §4 Path B derivation (explicit path integral on K4) — if needed
   - §5 Verification (numerical check on multiple (p,q))
   - §6 Connection to electron/positron distinction
   - §7 Implications for Item 2 (TLM port chirality-signed Y-matrix)

4. **Optional Op23 candidate** — if the parallel-channel pattern
   generalizes beyond chirality (e.g., to other multi-channel
   couplings), propose a new universal operator `Op23 (Multi-Channel
   Coupling Combination)` that formalizes harmonic-mean combinations
   for parallel coupling.

---

## §6 Critical files to reference

- [`manuscript/ave-kb/vol2/particle-physics/ch03-neutrino-sector/delta-cp-violation.md`](../../manuscript/ave-kb/vol2/particle-physics/ch03-neutrino-sector/delta-cp-violation.md)
- [`manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/chiral-factor.md`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/chiral-factor.md)
- [`manuscript/ave-kb/vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md`](../../manuscript/ave-kb/vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md)
- [`AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex`](../../../AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex)
- [`AVE-HOPF/scripts/beltrami_hopf_coil.py`](../../../AVE-HOPF/scripts/beltrami_hopf_coil.py)
- [`research/L3_electron_soliton/10_chirality_accounting_narrative.md`](10_chirality_accounting_narrative.md)
- [`research/L3_electron_soliton/13_hopf_self_inductance.md`](13_hopf_self_inductance.md)

---

## §7 Verification criteria

- For (2,3): `pq/(p+q) = 6/5 = 1.200` (matches AVE-HOPF row 1) ✓
- For (2,5): `10/7 ≈ 1.429` (matches AVE-HOPF row 2) ✓
- For (3,5): `15/8 = 1.875` (matches AVE-HOPF row 3) ✓
- For trivial unknot (p=1, q=0): `0/1 = 0` (no chirality) ✓
- For symmetric (p=q): `p²/2p = p/2` (half the winding, plausible) ✓
- For (p,q) and (q,p): same value (knot/mirror symmetry preserved) ✓

If Path A's parallel-channel interpretation reproduces all rows of
AVE-HOPF table 1 and gives sensible limits, the derivation is closed.

---

## §8 Effort estimate

**~1 day** (revised down from 2-3 days, per Grant's "estimates are way
off" rule and the abundance of corpus precedent).

Breakdown:
- Numerical verification script: 30 min
- Path A derivation write-up: 2 hours
- Path B derivation (if needed): 2-4 hours
- Sub-theorem doc: 2 hours
- Sanity checks + integration with Theorem 3.1: 1 hour

If Path A fails to reproduce all AVE-HOPF rows, fall back to Path B
(explicit path integral) — adds ~half a day.

---

## §9 Judgment calls to flag

1. **Path A vs Path B priority.** Path A is shorter and more
   electron-plumber-style; Path B is more rigorous. Recommendation:
   start Path A, fall back to Path B if needed.

2. **Op23 vs informal generalization.** If parallel-channel
   harmonic-mean combination generalizes beyond chirality (e.g., to
   other multi-channel impedances), propose Op23. If chirality-
   specific, document as part of the sub-theorem only.
   Recommendation: defer Op23 unless other use cases surface.

3. **What about (p,q) where gcd(p,q) ≠ 1?** Non-coprime windings
   produce composite knots, not simple torus knots. The harmonic
   mean formula may need adjustment for the composite case.
   Recommendation: derive for coprime case (electron is (2,3) =
   coprime); flag composite case as open.

4. **Connection to neutrino-sector chirality.** Delta-CP also uses
   K4 connectivity but produces 61π/45 not pq/(p+q). The two
   formulas relate via different projections (one on the unknot,
   one on the (2,3) torus knot). Worth showing explicitly that the
   derivation reduces to delta-CP for the neutrino case.
   Recommendation: include in §6 of the sub-theorem doc.

---

## §10 What this plan does NOT include

- Implementing chirality-signed Y-matrix in L3 TLM (that's Item 2)
- Full path integral over arbitrary embeddings on K4 (only the
  (p,q) torus knot family)
- Composite knots (gcd(p,q) > 1)
- Higher-order Vassiliev invariants beyond Hopf
- Connection to neutrino δ_CP composite structure (mentioned but
  not derived)