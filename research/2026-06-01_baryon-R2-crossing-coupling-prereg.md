# Baryon Per-Channel Coupling `k` (R2): Is `k=1` Forced by Impedance Match? — PRE-REGISTRATION

**Date:** 2026-06-01
**Branch:** `analysis/baryon-r2-crossing-coupling` (off `main`; push, do NOT merge — orchestration does the PR)
**Type:** Theoretical-physics derivation pre-registration — **frozen BEFORE any arithmetic** (the forced-vs-fit integrity depends on this)
**Feeds:** Parameter Ledger walk-back — decides the canonical ledger baryon row (`manuscript/backmatter/02_full_derivation_chain.tex:1047`) reads **"derived"** vs **"derived modulo R2"**.
**Origin:** 2026-06-01 V=2 dual-reactance closure; kickoff brief `_orchestration/2026-06-01_baryon-r2-crossing-coupling-brief.md`.
**Discipline applied:** ave-prereg, ave-ee-first-mapping, ave-canonical-leaf-pull, ave-analytical-tool-selection, pre-test-physics-check, consistency-vs-emergence, ave-fundamental-ground-up-implementation, ave-driver-script-honesty, ave-canonical-source, verify-before-cite, ave-evidence-framing-discipline. (substrate-native-check + ave-cavity-class-identification fire at derivation/leg-(ii).)

> **One-line prediction (frozen):** the baryon per-channel coupling `k` — the coefficient on `p_c` in the mass-eigenvalue loop gain `V·k·p_c` — is **exactly 1**, FORCED by Axiom-3 minimum-reflection driving the soliton's internal reactance-coupling boundary to `Γ→0`, where Op17 `T² = 1 − Γ² = 1` gives unity coupling. It is **not** a turns-ratio product.

---

## §1 — Framing (adjudicated — Grant 2026-06-01)

Grant collapsed the cascade-vs-match fork to the **impedance-match picture** after the full substrate-native painting. Locked framing:

1. **`k=1` is an impedance MATCH (Op17 `Γ=0`), not a turns-ratio product.** The literal product reading is a category error (coupling-coefficient `M/L=0.707` ≠ net power transmission `T²`); it is refuted on arrival (§5).
2. **Two crossing-roles, kept distinct:** the **6 Borromean linking-crossings** (each a transformer, `M/L = exp(−d²/4σ²) = 1/√2`) are the *coupling network* that governs `k`; the **c=5 cinquefoil winding** is the *confinement* (`r_opt = κ_FS/c = 8π/5`), already inside `I_scalar`. The brief's "(2,c) crossings inside `V·p_c`" conflated these — resolved: `k` lives in the Borromean linking network, `c=5` lives in `I_scalar`.
3. **leg-(ii) (why baryon ≠ lepton):** the baryon's 3 mutually-orthogonal Borromean loops couple as a **pure radial cross-sectional flux overlap** (no torsional twist) → matchable to `Γ=0` → `k=1`. The lepton is a **torsional ring self-energy** with a chirality mismatch (`ν_vac = 2/7`, PAT `J=2I`) → irreducible `Γ≠0` → the `√(3/7)` projection. Same Op17 coupling, two cavity classes.
4. **Why `Γ→0` is not assumed but forced:** Axiom 3 (Minimum Reflection) — the substrate minimizes `|Γ|²` at every internal impedance boundary. A stable standing soliton therefore self-matches its internal reactance-coupling boundary; proton stability ⇔ reactive loop that never dissipates (`P_real=0`, "rings forever").

## §2 — Corpus state: OPEN (reinvention-check clean)

Cross-repo `ave-corpus-grep` (this session) confirmed **no leaf derives the baryon per-channel `k` from a crossing structure** — R2 is genuinely open, not a re-derivation. All structural ingredients exist:

- Master eq `m_p = I_scalar/(1 − 𝒱·p_c) + 1` — `manuscript/backmatter/01_appendices.tex:97`; `M/L = 1/√2` at crossing — `:98`.
- `V=2` = reactance-sector count (X_C + X_L), mass-discriminated — `research/2026-06-01_baryon-V2-dual-reactance-closure.md` §1–2.
- Borromean 6 crossings (3 orthogonal loops × 2) — `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/thermal-softening.md:71`; cinquefoil c=5 + `r_opt=8π/5` — `proton-identification.md:19,21,63`.
- Closest different-scope cascade (NUCLEAR inter-nucleon, additive `c·π/2`, NOT this) — `vol6/framework/computational-mass-defect/mutual-coupling-constant.md:49`.

## §3 — Canonical tools + leaves pulled (load-bearing)

**Analytical tools (§1 Coupling + Class-10 Topology, per toolkit index):**
- **Op17** `T² = 1 − Γ²` — `operators.md:57` — the matched-coupling readout: **`k = T²`**.
- **Op3** `Γ = (Z₂−Z₁)/(Z₂+Z₁)` — `operators.md:33` — the loop↔loop / core↔halo mismatch.
- **Op14** cross-sector trading (Cosserat-B ↔ K4-inductive-E, ρ=−0.990) — the `V=2` `X_L↔X_C` trade the loop runs each cycle.
- **Axiom 3** minimum reflection — `ave-kb/CLAUDE.md` INVARIANT-S2 — forces `Γ→0` at internal boundaries (the reason `k=1` is forced, not assumed).
- **Topology Class-10** (scattered): Faddeev-Skyrme c-partition `03_geometric_inevitability.tex:316`; Vakulenko-Kapitanski + Q_H `01_appendices.tex:213`; bulk form `Δf/f = α·pq/(p+q)` (for (2,5): `α·10/7`) — to check whether the matched coupling is topologically quantized.

**Contrast / alternative leaves:**
- Lepton `√(3/7)` chirality-mismatch (leg-(ii) contrast) — `spontaneous-symmetry-breaking.md:38`.
- Orbital subtractive analog `k_pair = (2/Z)(1 − P_C/2)`, `P_C/2 ← Hopf c=2` (the only existing crossing-cascade form; kept as the (C) fallback) — `radial-eigenvalue-solver.md:579`.

## §4 — Prediction + mechanism

**Prediction: `k = 1` exactly.**

**Mechanism (the chain the derivation must instantiate):** the 6-crossing orthogonal-Borromean network (per-crossing `M/L=1/√2`) presents an internal reactance-coupling boundary. Axiom 3 drives that boundary to minimum reflection `Γ→0`. At `Γ=0`, Op17 gives `T²=1`, i.e. the per-channel feedback couples with unity efficiency → `k=1` → the loop gain is **bare** `V·p_c = 2·8πα`. The orthogonal (non-torsional) loop geometry is what makes `Γ=0` *reachable* (vs the lepton's chirality-locked `Γ≠0`).

## §5 — Numerical analysis (Step 3.5) — frozen pre-arithmetic

Inputs (driver MUST import from `src/ave/core/constants.py`, not hardcode — `ave-canonical-source`): `P_C = 8πα = 0.18340247`, `I_SCALAR_1D = 1161.9870305`, `V = 2`.

| `k` (hypothesis) | loop gain `V·k·p_c` | `m_p/m_e = I_scalar/(1−V·k·p_c)+1` | Δ vs CODATA 1836.152673 |
|---|---|---|---|
| **`k=1` (predicted — match)** | 0.366805 | **1836.117** (= `PROTON_ELECTRON_RATIO` exactly) | **−0.0019%** |
| `k=(1/√2)⁵=0.17678` (product, c=5) | 0.064844 | 1243.6 | −32.3% |
| `k=(1/√2)⁶=0.125` (product, c=6) | 0.045851 | 1218.8 | −33.6% |

The −0.0019% residual at `k=1` is the higher-order remainder (δ_th, etc.) **after** the integer count + unity coupling are fixed — NOT attributable to `k`. The product readings crater the mass by ~32% → the cascade-product picture is pre-registered as **refuted**.

## §6 — Discriminating outcomes

- **CLOSE (predicted):** the Borromean network provably has a `Γ=0` matched operating point AND the loop-gain coefficient there is **exactly 1** → R2 closes; ledger baryon row → **"derived"**.
- **REFINE:** the network matches but the coefficient is self-consistently **≠1** → `m_p` shifts; report the new value vs CODATA 1836.153; ledger row → "derived (k=⟨value⟩)".
- **STAYS-RESIDUAL:** no internal-boundary match forces unity (e.g. Axiom 3 pins the boundary to `Γ=−1` open-circuit, not `Γ=0`) → `k=1` remains an honest assumption; ledger row → **"derived modulo R2 (k=1 assumed, pending closure)"**.

## §7 — Falsifier

The match-picture is **wrong** if: (a) the soliton's internal reactance-coupling boundary is physically a `Γ=−1` TIR/open boundary (the confinement boundary) rather than a `Γ=0` matched boundary — i.e. Axiom 3 is already satisfied by the *winding*, leaving no separate match to set `k`; OR (b) the matched operating point exists but its loop-gain coefficient is provably ≠1 with no route to unity. Either falsifies "k=1 forced by match" and pushes to REFINE or STAYS-RESIDUAL.

## §8 — What the derivation must show (proof obligations)

1. Identify the physical internal boundary where `k` is set (loop↔loop coupling interface of the Borromean network / `X_L↔X_C` cross-sector boundary) and its characteristic impedances `Z₁,Z₂` (Op3).
2. Show Axiom 3 drives **that** boundary to `Γ=0` (not `Γ=−1`) — distinguish it from the confinement TIR boundary (which is `Γ=−1`, already accounted in `I_scalar`).
3. Show the 6-crossing `M/L=1/√2` network *admits* a matched operating point (the `1/√2` ≈ transitional/critical-coupling hint).
4. Show the per-channel loop-gain coefficient at the matched point is **exactly 1** (the `T²=1` readout), giving bare `V·p_c`.
5. Ground leg-(ii): orthogonal radial overlap → no chirality projection (vs lepton `√(3/7)`) — `ave-cavity-class-identification` fires here.

## §9 — Scope guard

R2-physics only. **FEEDS** the Parameter Ledger walk-back (sets the baryon-row classification); does **NOT** touch the manuscript walk-back PR. Output: this prereg + a `research/` result doc + (if needed) a forward-prediction driver that **imports** canonical constants and does **not** fit to 1836. Do **NOT** edit AVE-HOPF (read-only; R2 *contributes to* — does not one-to-one close — HOPF's "per-crossing AVE form" gated item per `AVE-HOPF/.agents/HANDOFF.md:50`). Branch off `main`, push, do **NOT** merge.
