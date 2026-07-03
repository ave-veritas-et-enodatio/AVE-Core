# D1 Adjudication Memo — srs vs diamond (test-gated)

**Date:** 2026-06-12  
**Epic:** `_orchestration/2026-06-11_lattice-d1-test-gated.md`  
**Principle:** D1 is an **outcome bin**, not a pre-test Grant pick. This memo rules from landed bins only.

> **STATUS (2026-06-12 post-#207 audit):** **SESSION-RECORD** — structural bins (§2.1) stand on R3 + Phase-1 evidence. **§2.3 framing is OVER-CLOSED** pending Grant confirm: v9/v10 P5/P6 production used **POST-RUPTURE** regime (`max(A²) ≫ 1`; see quarantine banners on result docs). Do **not** cite §2.3 as **D1-FINAL** for substrate-migration or framing closure. Execution read: `_orchestration/2026-06-12_loop-gap-orchestration-plan.md` §2–§3.

**Inputs (all executed):**

| Phase | Artifact | Headline bins |
|-------|----------|---------------|
| R3 decoration discriminator | `research/2026-06-11_lattice-decoration-discriminator_result.md` | **D1-A partial** (R3-P5 FAIL, ρ=5.71×10⁻⁴) |
| v9 Phase-1 vector-TLM | `research/2026-06-11_genesis-v9-phase1-prereg_FROZEN.md` + driver | **P1–P4 ALL PASS** (κ=0 geometry channel) |
| v9 Phase-2 Op14/Op3 | `research/2026-06-12_genesis-v9-phase2_result.md` | **P5 FAIL**; **P6 inconclusive** (no BIN-G) |

---

## 1. Evidence ledger (per observable — discrimination discipline)

| Observable | srs | diamond | κ decoration | Class | AVE-distinct? |
|------------|-----|---------|--------------|-------|---------------|
| Ring writhe | ±4.087×10⁻² | 0 | 0 (Arm 3 writhe) | replication | **Yes** — graph chirality, not SM bulk medium |
| Bishop Δθ/L (R3) | ±75.46°/unit | 0 | ±7.5×10⁻⁴ (ρ=0.057%) | consistency + emergence candidate | **Partial** — κ channel generic; **structural srs channel substrate-distinct** when paired κ=0 |
| Dynamical Δθ/step (P2, κ=0) | ±2.341°/step | 0 | n/a (not run) | emergence @ κ=0 | **Yes** — signed, enantiomorph-odd, writhe-concordant (P3) |
| Vector-TLM unitarity (P1) | drift ≤1.3×10⁻¹⁴ | 0 | — | consistency | No — achiral transport preserved |
| Planted `(2,3)` hosting (P5) | E/E₀=0.43, Q drift 5064% | — | — | consistency test | **Fail** — not hosting |
| Precursor genesis (P6) | 3/4 CVR-SET @ amp=0.25 only | SET-ACHIRAL | Op3/Op14-OFF ≈ srs ON | emergence | **Inconclusive** — matched baseline fails; ablations localize |

**SM counterfactual:** Any chiral constitutive medium can produce polarization rotation (R3 Arm 3). **D1-A promotion requires pairing** with Arm-1-style **κ=0 structural channel** (ave-multi-falsifier-triangulation). Phase-1 P4 supplies that pairing on the **vector-TLM** platform.

---

## 2. Full D1 bins (post Phase-1 + Phase-2)

### 2.1 Structural / static channel — **D1-A CONFIRMED**

**Assignment rule (R3 §7 + Phase-1 P4):** R3-P5 **FAIL** (decoration cannot reproduce srs Bishop rate at ≥20%) **AND** Phase-1 **P4 PASS** (signed dynamical rotation at **κ_chiral = 0**).

**Ruling:** Bare **srs connectivity** carries a **structural chiral channel** that (i) is not mimicked by κ-decoration on diamond at the R3-P5 gate, and (ii) drives signed, writhe-concordant polarization transport in vector-TLM without injected κ.

**What this retires:** The lattice-net resolution label **"unbacked numerology"** for **static / kinematic** trivalent-chirality claims on the srs net. Those claims now have **test-gated support** on the v9 scaffold.

**What this does NOT retire:** The resolution that the **production engine computes on z=4 diamond** (`k4_tlm.py`, α/Lorentz chains). No bin here recomputes α or Lorentz on srs.

### 2.2 Dynamical hosting / genesis — **D1-DYNAMICAL-MISS**

**Assignment rule (Phase-2 prereg P5/P6 + Rule 11):** P5 **FAIL** + P6 **without BIN-G promotion** (matched-baseline fail; Op3/O14 ablations still localize; saturation past `V_SNAP`).

**Ruling:** On the **discrete srs TLM + instantaneous Op14/Op3** engine class (A-027), the framework **does not** demonstrate (a) stable hosting of a planted `(2,3)` ansatz (H3 falsified) or (b) prereg-grade genesis-by-precursor (H4 not confirmed).

**Engine-class honesty:** BIN-D / SET-ACHIRAL / partial localization remain **consistent with A-027 ceiling** (no Master-Equation `c_eff(V)`). Op3 is **not uniquely load-bearing** for localization at production amp=0.25.

### 2.3 §0 framing (A) vs (B) — **SESSION-RECORD (framing OPEN)**

> **Regime quarantine:** P5/P6 inputs for this subsection come from v9/v10 production at `max(A²) ≈ 13–38` — **POST-RUPTURE** bins. Structural read (§2.1) does not depend on these cells; **framing default (B) is provisional** until Grant confirms or regime-valid P5/P6 re-run lands.

| Framing | Text (design doc §0) | Test read |
|---------|----------------------|-----------|
| **(A) Substrate challenge** | srs pass ⇒ migrate substrate; pay α/Lorentz cost | **Partial only** — static chirality channel **confirmed**; **hosting/genesis miss** blocks migration |
| **(B) Decoration diagnostic** | srs = model of excited `k_χ` geometry; diamond stays engine | **Provisional default** — matches structural bins; **not FINAL** without Grant confirm on quarantined dynamical inputs |

**Session-record ruling (test-gated, pending Grant confirm on framing):**

> **Provisional operational default: (B).** Treat bare srs as **discrete instrument** for structural chirality (R3 + Phase-1). **Do not** migrate production engine to z=3 srs on these bins. **Do not** cite Phase-2 partial P6 as genesis confirmation.

**(A) remains a live falsification axis** on a **regime-valid** engine class (harness ranks, memristive loop) — not re-litigation from quarantined POST-RUPTURE cells alone.

---

## 3. Consolidated D1 label

| Label | Meaning |
|-------|---------|
| **D1 structural** | **LANDED** — srs structural chiral channel confirmed (D1-A); diamond stays engine substrate for α/Lorentz |
| **D1 framing** | **OPEN** — provisional (B); §2.3 SESSION-RECORD pending Grant confirm; quarantined P5/P6 excluded from FINAL |

**Short form for orchestration index:** `D1 → STRUCTURAL-LANDED / FRAMING-OPEN` (not D1-FINAL)

**Superseded label (do not use for new corpus):** ~~D1-FINAL: B-primary / A-partial~~ — retained here as session history only.

---

## 4. Implications (physics only)

1. **Genesis v9 record:** Phase-0/1 **PASS** on chirality transport; Phase-2 **FAIL / inconclusive** on hosting/genesis. Consistent with session diagnosis **LOOP GAP** (no mass retention without lock) — Op14 reactive trap ≠ remanence.
2. **Electron definitive model:** Class A/B **consistency structure** on **diamond envelope** remains the manuscript/engine default; srs results inform **chirality mechanism** tests, not a lattice swap.
3. **R8 / fundamentality plan:** R3 gate **cleared** for "srs carries structural chirality." **R8 v9 Phase-1** cleared as **instrument validation**, not substrate migration. **v10 spine** follows **(B)** + constitutive-loop / lock scope (R2).
4. **T4 parallel track** (helicity @ Γ=−1): **unblocked** on `main`; independent of this D1 ruling.

---

## 5. Corpus walk-back queue

**Status (2026-06-12):** Grant greenlit post-merge. **P0–P1 executed** on branch
`analysis/2026-06-12-lattice-d1-walkback`. Q1 preserved-historical / Q2 frozen-snapshot rules apply
to untouched historical docs (electron-synthesis epic, vocab audit).

| Priority | Site | Action |
|----------|------|--------|
| P0 | `manuscript/common_equations/eq_axiom_1.tex:20` | Clarify: **4-bond diamond engine** + **3-sector Cosserat spin** + optional **bare srs structural chirality as discrete instrument** — remove Laves-name / coordination self-contradiction without asserting z=3 engine migration |
| P1 | `_orchestration/2026-06-07_lattice-net-resolution.md` | Add **2026-06-12 amendment**: srs static chirality **test-gated**; conclusion 1 "unbacked numerology" **scoped** to dynamical/engine claims, not R3+Phase-1 structural channel |
| P1 | `research/2026-06-11_genesis-v9-chiral-lattice_design.md` §0 | Mark **ADJUDICATED** — ruling §2.3 above; flag-don't-fix **closed** |
| P2 | KB leaves citing "srs outliers" without sector | Grep-sweep `unbacked numerology`, `Do NOT rebuild on z=3`, `trivalent outlier` — classify per walk-back Q1/Q2 |
| P3 | Engine defaults | **No change** — `k4_tlm.py` / diamond remain default; optional `chiral_lattice_*` modules = **instrument path** |
| Deferred | α / Lorentz re-derivation on srs | **Not queued** — explicitly out of scope per D1-FINAL |

---

## 6. What would falsify this memo

- Production **P5 PASS** + **BIN-G** on srs with matched-baseline **PASS** on a **substrate-native** engine class → reopen **(A) substrate challenge** at full strength.
- Demonstration that R3-P5-scale κ-decoration **can** reproduce Phase-1 P2 rates → **D1-B** evidence path reopens.
- Regression of Phase-1 P4 (κ=0 channel dies) → downgrade D1-A to **D1-INCONCLUSIVE**.

---

## 7. Cross-refs

- Epic log: `_orchestration/2026-06-11_lattice-d1-test-gated.md`
- R3 prereg §7: `research/2026-06-11_lattice-decoration-discriminator_prereg.md`
- Phase-2 prereg: `research/2026-06-12_genesis-v9-phase2-prereg_FROZEN.md`
- Lattice resolution: `_orchestration/2026-06-07_lattice-net-resolution.md`
- Two-engine A-027: `manuscript/ave-kb/common/two-engine-architecture-a027.md`

---

## ADDENDUM (2026-07-03) — D1 RATIFIED: srs-z3 is the production carrier (provisional (B) SUPERSEDED)

**Append-only. This addendum SUPERSEDES §2.3's provisional operational default (B)
and the §3 "D1 framing — OPEN" label. It does NOT edit the body above (git is the
trail); the body stands as the 2026-06-12 session record.**

**Ruling (Grant 2026-07-03, verbatim charter: "yup makes sense, ratify"):**
**srs-z3** — the true Sunada-K4 / Laves / srs net (degree-3, chiral, $I4_1 32$ —
the object Axiom 1 names) — is **RATIFIED as the engine's production carrier**.
The provisional framing default **(B)** of §2.3 / §5-P0 ("srs = discrete
instrument, diamond = production engine"; this memo `:44`, `:61`, `:65`) is
**SUPERSEDED**. The **(A) substrate-challenge axis** of §2.3 is **CLOSED**: the
axiom object and the production object are now the SAME, so there is no
substrate-vs-axiom challenge left to litigate.

**Scope guard (carried verbatim):** this is an **ENGINEERING-FIDELITY** ruling —
the engine implements the lattice the axiom already names. It mints **NO** new
ontological claim beyond Axiom 1. `mass = A1` (PR#260 / PR#311 ECHO-final) is
untouched. This is NOT a re-opening of the crystalline-vs-amorphous structural
seam (`the-abandoned-interior.md:183`), which is a DISTINCT question and stays
open.

**Evidence basis (cite, NOT re-derived here — all re-verified at the ratification
arc's HEAD per verify-before-cite):**

1. **Diamond statics ill-posed** — the bipartite-checkerboard nullspace: the four
   diamond `TETRA_OFFSETS` all have odd coordinate-sum, so
   `L_D = Div·diag·Grad` couples only same-parity nodes → two non-communicating
   sublattices carrying a large frozen kernel a smooth seed dominantly occupies.
   `research/2026-07-03_localization-readjudication_result.md:51-60,196-197`;
   independently reproduced in the exposure sweep
   `research/2026-07-03_engine-verdict-exposure-sweep_result.md:79-93`.
2. **The five-axis instrument comparison** (§5 of the readjudication result,
   `research/2026-07-03_localization-readjudication_result.md:194-208`):
   statics well-posedness (diamond sublattice-decoupled vs srs well-posed graph
   Laplacian); nullspace burden (diamond 8–16 dim vs srs **1**); smooth-core live
   fraction (diamond **6.5%** vs srs **89.5%**); positive-control constructibility
   (both, but the diamond smooth-seed read is muddied by the dead-leg); chirality
   (**diamond achiral $Fd\bar3m$ CANNOT host the (2,3) winding = charge**; srs
   chiral $I4_1 32$ carries charge/spin/parity).
3. **The DEC 2-complex + exact operator calculus on srs**
   (`research/2026-07-03_srs-dec-operators_result.md`): $\partial_1\partial_2=0$
   exact (integer), $\mathrm{div}=-\mathrm{grad}^\top$ exact (the adjoint relation
   the Stage-1b pair LACKED), $b_1=3$ = the periodic-3-torus wraps (correct
   topology). A valid coordinate-free cochain calculus exists on srs.
4. **Axiom-1 canon itself** — z=3 chiral ($I4_1 32$), `eq_axiom_1.tex:23-24`.

**What §2.1 (structural D1-A LANDED) and this addendum say together:** §2.1 already
established srs carries a structural chiral channel diamond cannot mimic; the
2026-07-03 evidence establishes the diamond statics operator is *pathological* and
srs is the *well-posed, chirality-carrying* carrier. The ratification takes the
final step §2.3 explicitly deferred to Grant: **migrate the production carrier to
srs-z3.**

**Falsifier §6 status:** §6's re-open condition ("Production P5 PASS + BIN-G on
srs → reopen (A) at full strength") is now MOOT — (A) is not "reopened," it is
CLOSED-BY-RATIFICATION in srs's favor. The migration itself (re-homing the
existing diamond `TETRA_OFFSETS` modules onto srs, α/Lorentz-chain survival as a
P1 acceptance gate) is chartered — but NOT executed — in
`_orchestration/2026-07-03_srs-migration-policy.md` (future arcs execute).

**Corpus propagation of this addendum:** vocabulary register K4 def-entry
(def-4b1a2c, status → SOLID production-carrier sense); `eq_axiom_1.tex:18` in-body
D1 note; `_orchestration/index.md` (D1 moved open → adjudicated); the migration
charter above.

---

## ADDENDUM (2026-07-03, cold-eyes note) — the PRIMARY independence anchor is the 2026-06-25 ratification

**Append-only. Records the cold-eyes program audit's anti-circularity finding
([`2026-07-03_cold-eyes-program-audit_result.md`](2026-07-03_cold-eyes-program-audit_result.md) §1);
does not edit the addendum above.**

The strongest anti-circularity finding of the 2026-07-03 ruling-chain audit is that
**D1's true primary independence anchor is a PRE-SESSION Grant ratification, not the
day's srs-favorable arcs.** The z=3 chiral srs was **already ratified by Grant on
2026-06-25** — verbatim at
[`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/unified-engine-design-doctrine.md:211`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/unified-engine-design-doctrine.md):
*"Decision 1 (RATIFIED, Grant 2026-06-25): the production engine substrate is the
chiral z=3 srs net."*

So the 2026-07-03 D1 "ratification" is a **re-confirmation of a decision substantially
already made** (plus a deferred wording restoration — the z=4 clause was a drive-by
contamination, never a Grant-adjudicated sentence). The day's arcs (the diamond-statics
nullspace, the five-axis instrument comparison, the srs DEC operators) supplied
*confirming instrument evidence* for the standing decision — they did NOT bootstrap it.
**This is the load-bearing reason the 2026-07-03 chain is BENIGN-DEPENDENCE, not a real
circle.**

**Foregrounding correction:** the evidence-basis list in the addendum above lists this
anchor as evidence-item-4 ("Axiom-1 canon itself"). Per the cold-eyes recommendation,
the PRIMARY independence anchor is the **2026-06-25 `unified-engine-design-doctrine.md:211`
ratification**; the four evidence items are *corroboration of a pre-session decision*,
not the decision's foundation. Even if any one of them (e.g. the diamond-nullspace
arithmetic) were wrong, the 2026-06-25 anchor survives.
