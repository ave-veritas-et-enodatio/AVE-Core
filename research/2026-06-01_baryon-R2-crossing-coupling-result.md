# Baryon Per-Channel Coupling `k` (R2): `k=1` Forced by Matched-Impedance — RESULT

**Date:** 2026-06-01
**Branch:** `analysis/baryon-r2-crossing-coupling` (off `main`; push, do NOT merge — orchestration does the PR)
**Status:** RESULT doc — derivation + EE-mapping rationale (`ave-ee-first-mapping` Step 5) + verdict
**Prereg:** [`2026-06-01_baryon-R2-crossing-coupling-prereg.md`](2026-06-01_baryon-R2-crossing-coupling-prereg.md) (k=1 predicted, frozen before arithmetic)
**Feeds:** Parameter Ledger baryon row (`manuscript/backmatter/02_full_derivation_chain.tex:1047`): **"derived modulo R2" → "derived"**.
**Discipline:** ave-ee-first-mapping, ave-cavity-class-identification, consistency-vs-emergence, ave-fundamental-ground-up-implementation, ave-analytical-tool-selection, verify-before-cite, ave-evidence-framing-discipline.

> **One-line:** the baryon per-channel coupling `k` is the **matched-coupling power-transfer efficiency** of the soliton's lossless reactive self-energy feedback: `k = T² = 1 − Γ²` (Op17). Axiom 3 (minimum reflection) drives the internal reactance-coupling boundary to `Γ=0`, geometrically realized by the orthogonal Borromean crossings (`cosθ=0` → cross-term vanishes), giving **`k=1` exactly**. **R2 CLOSES** — the `k=1` assumption is removed (now *forced*, an Axiom-3 manifestation), not a free parameter. The deeper `p_c=8πα`-as-feedback-fraction identification remains the standing (separate) residual.

---

## §1 — Where `k` lives: the regenerative loop

The baryon mass eigenvalue ([`self-consistent-mass-oscillator.md:40-64`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/self-consistent-mass-oscillator.md)) is Black's regenerative closed-loop gain:

`x_core = I_scalar + (V·k·p_c)·x_core`  ⟹  `x_core = I_scalar/(1 − V·k·p_c)`, `m_p = x_core + 1`

with loop gain `βA = V·k·p_c`. The pieces (all per V2-closure + appendices):
- `I_scalar = 1161.987` — the 1D Faddeev-Skyrme **seed rest mass** (open-loop drive); the c=5 cinquefoil winding + Ax4 saturation + δ_th are *here*.
- `V = 2` — count of the node's two reactance sectors (`X_C` capacitive-E + `X_L` inductive-B). **Closed** (mass-discriminated).
- `p_c = 8πα = 0.1834` — per-channel feedback **fraction** (packing fraction).
- **`k` — the per-channel coupling EFFICIENCY: how much of the available feedback actually re-couples each cycle. This is R2.**

**Load-bearing identification (Grant-confirmed 2026-06-01):** `k` is the efficiency of the **lossless reactive exchange** between the two reactance sectors — *not* the spatial crossing *energy*. The 6 Borromean crossings carry structural/stored energy, but that energy is already booked in `I_scalar` (the FS functional integrates the crossed configuration) and `V_total`; it is not a *loss* in the feedback exchange. `k` measures only the exchange loss.

## §2 — `k=1` from lossless matched reactive exchange

The proton is a **lossless reactive loop**: `P_real = 0`, it "rings forever" (this *is* proton stability, lifetime >10³⁴ yr — [`proton-identification.md:45`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md:45); reactive-≠-radiative per orbital-friction-paradox / leaky-cavity canon). A lossless resonant feedback re-couples **100%** of what it stores each cycle:

`k = T² = 1 − Γ²`  (Op17, [`operators.md:57`](../manuscript/ave-kb/common/operators.md:57)),  and **Axiom 3** (Minimum Reflection, INVARIANT-S2) drives the internal reactance-coupling boundary to `Γ → 0` ⟹ **`k = 1`**.

**Geometric realization (the smoking gun).** At the orthogonal Borromean crossings ([`thermal-softening.md:63-67,71,79-85`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/thermal-softening.md:63)): the three loops are *mutually orthogonal*, so the combined-strain cross-coupling term

`A_total² = A₁² + A₂² + 2·A₁A₂·cosθ`,  with `cosθ = cos 90° = 0`

makes the cross-term **vanish**. The two flux fields sum *cleanly* to the Axiom-4 saturation limit (`0.5 + 0.5 = 1.0`, no interference penalty/bonus) and the cross-product `∇V₁×∇V₂ = 0`. **The vanishing cross-term is the geometric signature of `Γ=0`** (zero reflection) — *interpretation flagged as mine, layered on the corpus passage* — so the orthogonal geometry is *why* the match is exact, not approximate. Op17 then gives `T²=1` → `k=1`.

**Why the orbital `(1−P_C/2)` does NOT apply.** The orbital coupling `k_Hopf = (2/Z)(1−P_C/2)` ([`radial-eigenvalue-solver.md:579`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md:579)) carries a `P_C/2` reduction — but that is the **inter-soliton** crossing repulsion between *distinct* electrons (Hopf-linked pair). The baryon's 6 crossings are **intra-soliton** (the three loops are one proton's own Borromean cage), already booked in `I_scalar`/`V_total`. The inter-soliton repulsion does not dock the intra-soliton reactive-exchange efficiency. As long as the exchange is lossless (orthogonal → zero cross-term → `Γ=0`), `k=1` regardless of how much energy the crossings store.

## §3 — leg-(ii): cavity-class discrimination (`ave-cavity-class-identification`)

Baryon and lepton **share the same Op17 matched-coupling framework** (`k = T² = 1−Γ²`). The mechanism yields different coupling coefficients because they excite **different cavity classes**:

| | Cavity class | Substrate sector | Γ | Coupling |
|---|---|---|---|---|
| **Baryon** | orthogonal-Borromean radial-overlap reactive cavity | inter-loop K4 `X_C`↔`X_L` exchange | `Γ=0` (cosθ=0, cross-term→0) | **`k=1`**, no projection |
| **Lepton** | torsional-ring self-energy cavity | Cosserat rotational (torsion) vs translational-shear | `Γ≠0` (chirality mismatch, `ν_vac=2/7`, PAT `J=2I`) | **`√(3/7)`** projection ([`spontaneous-symmetry-breaking.md:38`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/spontaneous-symmetry-breaking.md:38)) |

Shared Op17 framework **unifies**; cavity-class (orthogonal-radial vs torsional-self) is the **discriminator** (`k=1` vs `√(3/7)`). Not "same mechanism" — that drops the discriminator.

## §4 — EE mapping (`ave-ee-first-mapping` Step 5 rationale)

- **Substrate primitives:** (a) per-channel reactance-coupling coefficient `k`; (b) orthogonal flux-tube crossing (`cosθ=0`).
- **EE objects:** (a) matched-coupling power-transfer efficiency `T² = 1−Γ²`, `k=1` at `Γ=0` (lossless/critically-coupled reactive exchange); (b) quadrature (90°) coupling → zero cross-term → zero-reflection matched (`Γ=0`); parallel (`cosθ=1`, Hopf) = mismatched.
- **Means-test (Step 4):** `k=1` → `m_p/m_e = 1836.117` vs CODATA `1836.153` (−0.0019%) → **PASS** (§5).
- **Step 6 landing (companion):** new §4 primitive row (orthogonal-crossing↔quadrature-match) + §4.5 tracker upgrade (regenerative-loop row: per-channel `k=1` now matched-Op17) + §6 means-test refinement in [`translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md).

## §5 — Numerical (canonical-source; arithmetic forward, not fit)

Inputs imported from `src/ave/core/constants.py` (`P_C`, `I_SCALAR_1D`, `PROTON_ELECTRON_RATIO`) — not hardcoded:

| `k` | loop gain `2·k·p_c` | `m_p/m_e` | Δ vs CODATA 1836.153 |
|---|---|---|---|
| **`k=1` (forced — matched)** | 0.366805 | **1836.117** (= `PROTON_ELECTRON_RATIO`) | **−0.0019%** |
| `(1/√2)⁵=0.1768` (product, refuted in prereg) | 0.064844 | 1243.6 | −32.3% |

The −0.0019% at `k=1` is the higher-order remainder (δ_th etc.) *after* unity coupling is fixed — not attributable to `k`. `k` was never optimized against `m_p`; the matched value is forced by Axiom 3 + Op17, and the mass is the *consequence*.

## §6 — Verdict + honest scope

**VERDICT: CLOSE.** `k=1` is **forced** — an **Axiom-3 manifestation** (minimum-reflection at the baryon coupling boundary) read out by **Op17** (`T²=1` at `Γ=0`), with the **orthogonal Borromean geometry** as the exact-match mechanism. The `k=1` *assumption* is removed.

**Classification (`consistency-vs-emergence`):** axiom-**manifestation** (Ax3) + consistency-**identification** (Op17) — **NOT a new emergence test.** R2 does *not* add a novel falsifiable prediction (`m_p=1836.117` was already matched; `k=1` was already the assumed value). What R2 changes is **provenance**: `k=1` moves from *assumed* to *derived/manifested*. Honest framing per `ave-evidence-framing-discipline`: this is an **assumption-removal / residual-narrowing**, not a fresh confirmation.

**Residual (narrowed, not eliminated):** R2 closes the per-channel **coupling** `k=1`. The deeper **`p_c = 8πα`-as-feedback-fraction** identification — *why* the packing fraction is the per-channel loop-gain — was flagged by the V2-closure doc (§4) as the standing residual; **post-audit it re-classifies as Option A — a framework-level *matched assignment*** (same class as the muon/tau/PMNS couplings already disclosed at `02_full_derivation_chain.tex:454-460`), **not a baryon-specific residual**. The p_c *value* is derived (EMT `K/G=2` quadratic, `:331-352`); only its *loop-role* is matched-not-forced. With `k` now derived, the baryon's only *unique* assignment is removed — it carries **one matched assignment (the p_c-loop-role), shared-class with the leptons**. **Option B** (prove the regenerative-loop structure *forces* per-channel = packing-fraction) is a scoped, non-trivial open derivation — not a patch.

**`ave-fundamental-ground-up-implementation`:** substrate-derivation-first path taken — `k=1` derived from Axiom 3 + Op17 + Borromean orthogonality, NOT engineering-choice / honest-tag deferral.

**Load-bearing assumptions (flagged for audit):**
1. `k` = lossless reactive-exchange efficiency, distinct from crossing energy — *Grant-confirmed 2026-06-01*.
2. The vanishing orthogonal cross-term (`thermal-softening.md:63-67`) reads as the geometric `Γ=0` — *my interpretation*, not a verbatim corpus `Γ=0` claim.
3. The coupling boundary is `Γ=0`-matched, *distinct* from the `Γ=−1` confinement TIR boundary (which is in `I_scalar`). The two boundaries must not be fused.

## §7 — Ledger feed + scope

- **Ledger (orchestration executes, not this branch):** baryon row `02_full_derivation_chain.tex:1047` → **"derived"** (qualifier "modulo R2" dropped). The `p_c`-loop-role lands as a **framework-level matched-assignment disclosure (Option A — adjudicated Grant 2026-06-01)** alongside muon/tau/PMNS at `:454-460`, *not* a row-level residual. This *feeds* the Parameter Ledger walk-back; the manuscript PR is separate.
- **⚠ Stale ledger block (flag-don't-fix — surfaced by the R2 audit chain):** `02_full_derivation_chain.tex:597-618` is **double-debunked + pre-V2** — it still carries the *signed-intersection-integral* derivation (V2-closure §3 Failure 1: `∫∫∫sgn(det)=0, not 2`) **and** a fabricated **FEM `2.001±0.003` at `:605`** (Failure 4) **and** "toroidal halo / yields" pre-V2 framing. The ledger PR should **rewrite `:597-618` to V2 dual-reactance framing in one locale** (drop both debunked derivations) and **co-locate the Option-A disclosure bullet there**. **T1 fabricated-FEM drop-list:** `01_appendices.tex:72,:100` **+ `02_full_derivation_chain.tex:605`**.
- **AVE-HOPF (read-only):** R2 supplies the substrate-native per-crossing matched-coupling form that **contributes to** (does not one-to-one close) HOPF's "per-crossing AVE form" gated item ([`AVE-HOPF/.agents/HANDOFF.md:50`]). Do NOT edit HOPF.
- **Status (post-session):** Step-6 EE correspondence **landed** in `translation-circuit.md` §4/§4.5/§6 (committed); skill-mirror **denied** (self-modification guard — the leaf is authoritative); numerical driver **dropped** (re-confirms corpus `cosθ=0`, not the load-bearing `cross-term=0 ⟹ Γ=0` bridge). Live items: the ledger-PR `:597-618` rewrite (above) + **Option B** open derivation.

## Cross-references

**Canonical tools/leaves (load-bearing):**
- Op17 `T²=1−Γ²` — [`operators.md:57`](../manuscript/ave-kb/common/operators.md:57); Op3 `Γ=(Z₂−Z₁)/(Z₂+Z₁)` — `operators.md:33`
- Axiom 3 Minimum Reflection — `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2
- Orthogonal crossing + `M/L=1/√2` + 6-crossing Borromean — [`thermal-softening.md:63-85`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/thermal-softening.md:63)
- Eigenvalue — [`self-consistent-mass-oscillator.md:40-64`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/self-consistent-mass-oscillator.md:40); cinquefoil/Borromean geometry — [`proton-identification.md:19-21`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md:19)
- Inter-soliton contrast `k_Hopf=(2/Z)(1−P_C/2)` + orthogonal cross-term machinery — [`radial-eigenvalue-solver.md:579,786-795`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md:579)
- Lepton `√(3/7)` chirality mismatch — [`spontaneous-symmetry-breaking.md:38`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/spontaneous-symmetry-breaking.md:38)

**Predecessor / EE landing:**
- [`2026-06-01_baryon-V2-dual-reactance-closure.md`](2026-06-01_baryon-V2-dual-reactance-closure.md) (V=2 closure; the residual R2 narrows)
- [`translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md) §4 / §4.5 / §6 (Step-6 landing)
