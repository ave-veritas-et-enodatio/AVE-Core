> **Notation (2026-06-18):** Substrate object symbol `$\mathcal{M}_A$` **retired** (Grant adjudication). Use prose: *substrate*, *chiral LC network*, *chiral Laves K4 Cosserat crystal*. Body below preserved per Rule-12.

# QM-Foundations Trio — Superposition / Collapse / Entanglement under AVE

**Date**: 2026-06-08
**Branch**: `analysis/2026-06-08-qm-foundations-trio`
**Author lane**: implementer
**Discipline applied**: `ave-prereg` + `verify-before-cite` + `ave-canonical-leaf-pull` + `consistency-vs-emergence` (dual-axis on collapse) + `ave-discrimination-check` + `ave-evidence-framing` + `substrate-native-check` (trigger-6) + `ave-walk-back` + `pure-AVE-corpus`

> **Status of this document**: SYNTHESIS / research-tier. It documents how three already-canonical (or research-tier) leaves jointly answer the QM-foundations question. It does **not** introduce new physics and does **not** promote any leg to a higher confidence class than its own leaf already carries. The three legs are deliberately kept at their native confidence tiers (see §1) — do not flatten them.

---

## §0 — One-paragraph summary

Standard QM treats superposition, wave-function collapse, and entanglement as three separate postulates. Under AVE they are three **different** substrate phenomena along two orthogonal axes — locality (local / nonlocal) and ontology (epistemic / dynamical / ontic):

- **Superposition = aliasing** — a *local, epistemic* reading: $|\psi|^2$ is the time-averaged trajectory density of a point-defect sweeping its standing-wave mode, under-sampled relative to the fast carrier oscillation. (SYNTHESIS / consistency-class.)
- **Collapse = sampling / saturation** — a *local, dynamical* event: a thresholded Ohmic load (detector) draws Joule energy from the substrate mode, crosses the extraction threshold, self-traps ($\Gamma \to -1$), and clicks. The Born $p=2$ exponent is **derived end-to-end with no Born-rule input**. (DUAL-AXIS: Class-2 substrate-mechanism emergence + Class-4 observable consistency.)
- **Entanglement = thread** — a *nonlocal, ontic* structure: a $2\pi$ quantised phase winding (topological thread) on the $\mathcal{M}_A$ graph, a lossless phase-locked gear train. (CANONICAL / Class-1, Axiom-1.)

The three legs are **non-overlapping** on both axes (no category bleed), and the trio is **Bell-surviving**: entanglement's nonlocality is carried by the real topological thread, not by the local aliasing picture — so the May-2025 origin seed "entanglement → aliasing" was mislabeled by exactly one slot (§4).

---

## §1 — Confidence asymmetry (stated UP FRONT — do not flatten)

The three legs do **not** carry equal epistemic weight. This asymmetry is load-bearing for any downstream write-up:

| Leg | Confidence tier | What that means |
|---|---|---|
| **Entanglement = thread** | **CANONICAL** (Class-1, Axiom-1) | Derived from substrate axioms; lives as a canonical KB leaf (`phase-locked-topological-thread.md`, claims `clm-zuf7g1, clm-b9eura, clm-unk0bd`). The mechanism is the corpus's own answer to non-locality. |
| **Collapse = sampling/saturation** | **DERIVED** (Class-2 emergence + Class-4 consistency) | End-to-end derivation closed in Phase 2-A (clm-ldmvwi, PR #38, merged 2026-05-26). Born $p=2$ has no postulate input. Scope-qualified (AC / sign-symmetric ensembles). |
| **Superposition = aliasing** | **SYNTHESIS** (consistency-class / Class-0 reframe) | The substrate mapping ($|\psi|^2$ = time-averaged trajectory density) is canonical (`translation-qm.md:19`). The *word* "aliasing" is **Grant's Nyquist reframe**, **not** corpus-verbatim for temporal phenomena: the corpus uses "aliasing" only for **spatial** Brillouin undersampling (`paley-wiener-hilbert.md:10`). No observable handle distinguishes it from QM. |

**Monotonicity**: the confidence axis is monotone and tracks the ontology axis — ontic/canonical > dynamical/derived > epistemic/synthesis. This is *consistency*, not coincidence: a more fundamental ontological role is exactly where the corpus has invested the stronger derivation.

---

## §2 — The locality × ontology table

Each leg with its canonical/derived cite and its honest class per `consistency-vs-emergence`.

| | **Superposition** | **Collapse** | **Entanglement** |
|---|---|---|---|
| **Substrate mechanism** | Time-averaged trajectory density of a point-defect sweeping its standing-wave mode; the observed $\|\psi\|^2$ under-samples the fast carrier oscillation (Nyquist/aliasing reading) | Thresholded Ohmic load draws Joule energy ($V^2/Z_{det}$) from the substrate mode; amplitude crosses the extraction threshold → saturation self-trap ($\Gamma \to -1$) → discrete energy-extraction event ("click") | $2\pi$ quantised phase winding on the $\mathcal{M}_A$ graph — a lossless phase-locked gear train ("topological thread"), mechanically identical to the Meissner effect (Vol III Ch 9) |
| **Locality** | **Local** | **Local** | **Nonlocal** |
| **Ontology** | **Epistemic** (observer under-samples; nothing new in the substrate) | **Dynamical** (a real boundary energy-extraction process unfolds) | **Ontic** (a real topological structure connects the pair) |
| **Class** (`consistency-vs-emergence`) | **SYNTHESIS / consistency-class** (Class-0 reframe) | **DUAL-AXIS**: Class-2 substrate-mechanism emergence (derivation-path) **+** Class-4 observable consistency (prediction) | **CANONICAL** Class-1 (Axiom-1 mechanism); CHSH $=2\sqrt2$ is Class-4 consistency, **not** a discriminator |
| **Canonical / cite anchor** | `manuscript/ave-kb/common/translation-tables/translation-qm.md:19` | `manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md:55,57-59,61` (clm-ldmvwi) | `manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md:8-13,116,177-185` (clm-zuf7g1) |

### Verbatim cite payloads (verify-before-cite, re-verified against shipped HEAD `966f4a2b` = base `63e6671a` + this workstream's body-only KB insertions; all line cites reconciled to that tree, 2026-06-08)

**Superposition** — `translation-qm.md:19`:
> `| $|\psi|^2$ probability | Time-averaged trajectory | Density of point-defect sweeping its standing-wave mode. |`

**Collapse** — `ohmic-decoherence-born.md:55`:
> "**Key result**: The $|\partial_t \mathbf{A}|^2$ click-probability scaling is **not asserted as a thermal-substrate stochastic property** — it is **derived end-to-end from substrate physics** (master vacuum equation + Axiom 1 Ohmic boundary + Vol 3 Ch 11 FDT + AVE Lagrangian + standard probability theory). **No Born rule input anywhere in the chain.**"

`ohmic-decoherence-born.md:57-59`:
> "**Classification per consistency-vs-emergence-UPGRADED discipline (Grant 2026-05-26)**:
> - **Class 2 substrate-mechanism emergence**: full derivation-path traces to master vacuum equation
> - **Class 4 observable consistency**: replicates standard QM Born-rule scaling exactly in canonical photodetection regime — no experimentally distinguishable corrections in current measurement precision"

`ohmic-decoherence-born.md:61` (scope qualifier — load-bearing):
> "**Scope qualifier**: derivation applies to **AC signals or sign-symmetric signal ensembles** … DC/sign-asymmetric signals retain a linear-in-$V_s$ contribution."

**Entanglement** — `phase-locked-topological-thread.md:13`:
> "the lattice architecture reveals that entangled particles are connected by a *topological thread* — a quantised phase winding on the $\mathcal{M}_A$ graph that functions as a phase-locked gear train, mechanically identical to the Meissner effect derived in Volume III, Chapter 9."

`phase-locked-topological-thread.md:116` (binary 2-antinode):
> "**Binary outcome from saturation (Axiom 4).** The particle's saturated boundary ($\Gamma = -1$) supports a standing wave with exactly two antinodes."

`phase-locked-topological-thread.md:182,185` (no-signalling, Bob's marginal $=1/2$):
> "$P(B{=}+) = \tfrac{1}{2}\sin^2(\theta_{ab}/2) + \tfrac{1}{2}\cos^2(\theta_{ab}/2) = \tfrac{1}{2}$ … Bob always observes a 50/50 outcome distribution."

**Deterministic substrate / Bell survival** — `statistics-under-ave.md:29`:
> "AVE carries no irreducible randomness. The substrate is deterministic; what standard physics reads as fundamental stochasticity is the coarse-grained appearance of the lattice's deterministic noise floor."

`statistics-under-ave.md:77`:
> "AVE self-classifies … as a **nonlocal deterministic hidden-variable theory** — it concedes *locality* (the correlation is carried by a topological thread), NOT determinism, and NOT via local hidden variables or superdeterminism. Since $|S|=2\sqrt2$ exactly equals QM, CHSH is **not** an AVE-vs-QM discriminator."

**Aliasing is spatial-only in the corpus** — `paley-wiener-hilbert.md:10`:
> "the $\mathcal{M}_A$ lattice has a fundamental pitch $\ell_{node}$ … The maximum spatial frequency the lattice can support without aliasing is the Brillouin boundary: $k_{max} = \pi / \ell_{node}$."

---

## §3 — Per-leg detail

### 3.1 Superposition = aliasing (LOCAL, EPISTEMIC) — SYNTHESIS / consistency-class

`translation-qm.md` Section A (intra-system cavity-mode) maps $|\psi|^2$ to the **time-averaged trajectory density** of a point-defect sweeping its standing-wave mode (`:19`). Grant's reframe reads this as **temporal Nyquist aliasing**: the observed probability density is what you get when the measurement bandwidth under-samples the fast carrier ($\omega_C$) oscillation of the defect on its mode. Nothing new exists in the substrate — the superposition is the **observer's** under-resolved view of a deterministic trajectory. Hence *local* and *epistemic*.

**Why SYNTHESIS, not canonical-derived** (`ave-evidence-framing` tier honored):
- The substrate mapping itself is canonical (`translation-qm.md:19`).
- But the corpus reserves the word **"aliasing"** for **spatial** Brillouin undersampling only (`paley-wiener-hilbert.md:10`). Applying it to the **temporal** carrier is Grant's reframe — a coherent synthesis, not a corpus-verbatim term.
- There is **no observable** that separates the aliasing reading from textbook $|\psi|^2$. This is a Class-0 mechanistic reframe, not a Class-2 emergence or a discriminator.

> Load-bearing caveat: do NOT promote "superposition = aliasing" to canonical-derived. It is the Nyquist *reading* of an already-canonical density mapping. Tagged synthesis-not-canonical + consistency-class.

### 3.2 Collapse = sampling / saturation (LOCAL, DYNAMICAL) — DUAL-AXIS Class-2 + Class-4

`ohmic-decoherence-born.md` derives the Born $p=2$ click-probability scaling end-to-end from substrate physics (7-step chain, `:48-53`): master vacuum equation → FDT Langevin boundary → stochastic master equation → Joule extraction $V^2/Z_{det}$ → $V \leftrightarrow \partial_t\mathbf{A}$ via the AVE Lagrangian → Gaussian amplitude via FDT+CLT → threshold-crossing first-passage (Rice/Wald) → $p=2$ uniqueness. **No Born-rule input anywhere in the chain** (`:55`).

This is the corpus's strongest demonstration of why collapse is **dynamical, not interpretive**: there is no observer and no discontinuous projection. The substrate evolves continuously *through* the extraction event; the "click" is a discrete energy quantum drawn through a boundary aperture at a threshold-crossing (`translation-qm.md:41-44`).

**Dual-axis classification** (`consistency-vs-emergence`, exactly as the leaf states at `:57-59`):
- **Class-2 substrate-mechanism emergence** on the *derivation-path* axis — the full path traces to the master vacuum equation.
- **Class-4 observable consistency** on the *prediction* axis — click-rate scaling replicates standard QM Born scaling exactly in the canonical photodetection regime; no distinguishable corrections at current precision.

**Scope qualifier** (`:61`): derivation holds for AC / sign-symmetric ensembles (the canonical photodetection regime). DC / sign-asymmetric signals retain a sub-leading linear-in-$V_s$ term. This is scope, not refutation.

**Open / not-yet-load-bearing**: the $p=2$ *scaling* is derived (A.3 + A.4); the definitional identification $\Pr \equiv |\psi|^2$ is **not** a step inside the ohmic leaf (whose derivation table runs A.2–A.4 only, `ohmic-decoherence-born.md:48-53`) — it is the still-pending **Phase 2-A.5 KB-integration step**, documented as the deferred definitional identification in `research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md:243` (and §9, `:272`). Forward-prediction candidates (Ax-4 saturation-induced narrow-aperture amplitude-shape corrections, nanoscale CLT failure, non-Markovian memory) exist but are below current measurement precision and are not load-bearing for this leaf's present solidity.

### 3.3 Entanglement = thread (NONLOCAL, ONTIC) — CANONICAL Class-1

`phase-locked-topological-thread.md` is the canonical leaf. Entangled particles are connected by a **real topological thread**: a $2\pi$ quantised phase winding on the $\mathcal{M}_A$ graph, realized as a lossless ($Q=\infty$) phase-locked LC gear train, characteristic impedance $Z_0 \approx 377\,\Omega$ (`:13`, `:17-34`). Binary measurement outcomes come from Axiom-4 saturation: the $\Gamma=-1$ boundary supports a standing wave with **exactly two antinodes** (`:116`). No-signalling is exact — Bob's marginal is $\tfrac{1}{2}$ independent of Alice's setting (`:182`). CHSH reaches the Tsirelson bound $|S|=2\sqrt2$, derived from substrate primitives (Möbius half-angle coupling + Axiom-4 binary saturation + Born from Ohmic extraction), **no import of Bell's theorem**.

**Class**: Class-1 (Axiom-1 canonical mechanism). The CHSH magnitude is Class-4 observable consistency — it matches QM exactly and is therefore **not** a discriminator (see §5).

---

## §4 — Origin-mislabel fix (one-slot, Bell-surviving)

The May-2025 origin seed framed the spark as **"entanglement → aliasing"**. Under the trio's two-axis structure this is mislabeled by **exactly one slot**:

- **Aliasing is local** (under-sampling a fast oscillation at one site) → it belongs to **superposition**, not entanglement.
- **Entanglement is nonlocal** → it needs the **thread**. A *local* aliasing account of entanglement would predict the correlation arises from a shared local under-sampling — i.e. a **local hidden variable** — and would therefore **Bell-falsify** (it cannot reproduce $|S|=2\sqrt2$ without signalling).

**The fix** (corpus-side; the memory seed is left untouched per the standing directive — do not edit memory):
- Keep **aliasing OUT** of the entanglement leaf. `phase-locked-topological-thread.md` contains **zero** occurrences of "aliasing" in the mechanism **body**; the sole mention is the line-15 guard-note (inserted by this workstream), which names "aliasing" only to **EXCLUDE** it from the thread. The mechanism there is the thread, full stop.
- Keep **aliasing IN** the superposition reading only (`translation-qm.md:19`, as the Nyquist reading).

Re-targeting the slot makes the trio **Bell-surviving**: AVE concedes *locality* (carried by the real thread), retains *determinism*, and is a nonlocal deterministic hidden-variable theory (`statistics-under-ave.md:77`). The spatial-vs-temporal aliasing disambiguation (`paley-wiener-hilbert.md:10`) is the structural guard that prevents reversion: spatial aliasing (Brillouin) ≠ temporal aliasing (superposition reading) ≠ the thread (entanglement).

---

## §5 — Measurement problem "dissolved" — framed via the discrimination-check

`ave-discrimination-check` + `ave-evidence-framing`: separate what is an AVE-distinct **interpretation** from what is a falsifiable **discriminator**.

**The interpretation (AVE-distinct, but not a proven empirical claim):** AVE dissolves the measurement problem by removing the observer. Collapse is a deterministic boundary-Joule extraction (§3.2); randomness is the coarse-grained substrate thermal floor + first-passage threshold-crossing, not irreducible (`statistics-under-ave.md:29`). There is no projection postulate, no branching, no special observer. This is a coherent **interpretation/mechanism** — but Copenhagen, MWI, and Bohm all reproduce identical QM phenomenology, so the interpretive claim is **not, by itself, falsifiable**. Frame it as AVE's deterministic-substrate stance, **not** as a proven discriminator.

**What is NOT a discriminator (Class-4 consistency only):**
- **CHSH $=2\sqrt2$** — matches QM exactly (`statistics-under-ave.md:77` says so verbatim: "CHSH is **not** an AVE-vs-QM discriminator").
- **Born $p=2$** — replicates QM exactly in the canonical regime (`ohmic-decoherence-born.md:59`). Its value is in being *derived* (confidence asset), not in being *distinct*.

**The only candidate discriminator across the whole trio:** the **entanglement-decoherence onset at $T_{\text{pair}}$** (`phase-locked-topological-thread.md:57-70`):
$$T_{\text{pair}} = \frac{2 m_e c^2}{k_B} \approx 1.19 \times 10^{10}\;\text{K}.$$
- **AVE** (`:69`): entanglement decoherence has a sharp, temperature-dependent onset at the pair-creation threshold; below it, the $2\pi$ winding is topologically protected ($P_{\text{break}} \propto e^{-2m_e c^2/k_B T}$).
- **Standard QM** (`:70`): decoherence is governed by environmental coupling strength alone, with **no** intrinsic temperature threshold tied to $2 m_e c^2$.
- **Caveat (load-bearing)**: this is a **cosmological-scale** temperature (heavy-ion / QGP regime, $T \gtrsim 10^{10}$ K), **not lab-near**. It is the one place the trio makes a falsifiable AVE-vs-QM prediction, but it is not currently a practical lab handle.

---

## §6 — Two corrections / scope notes (flag-don't-fix discipline)

1. **Collapse ≠ mass-forming.** Both photodetection-collapse and pair-production share the **same** substrate primitive — the $\Gamma \to -1$ saturation self-trap. But they are **different events**: collapse is a boundary-Joule energy *extraction* event at a detector; pair-production is a vacuum mass-*forming* event. Do not conflate "the same self-trap primitive" with "the same physical process."

2. **Leaf-metadata observation (surfaced, not fixed).** In this worktree (`origin/main` 63e6671a) `translation-qm.md` frontmatter is `claims: [clm-fy05jc]`. A prior verification pass (run in `pathc-wt`) attributed `clm-yiyyi3` to this leaf; in fact `clm-yiyyi3` is the AVE-Lagrangian claim cross-referenced from `ohmic-decoherence-born.md:50`, not the translation-leaf's own claim. Surfaced here per flag-don't-fix; not load-bearing for the trio; no edit made.

---

## §7 — Trio self-consistency check

| Axis | Superposition | Collapse | Entanglement | Status |
|---|---|---|---|---|
| **Locality** | Local | Local | Nonlocal | Non-overlapping ✓ |
| **Ontology** | Epistemic | Dynamical | Ontic | Non-overlapping ✓ |
| **Class** | SYNTHESIS (0) | DERIVED (2+4) | CANONICAL (1) | Monotone with ontology ✓ |
| **Bell** | — | — | Nonlocal thread carries correlation; determinism preserved | Bell-surviving ✓ |
| **Discriminator** | none | none (Class-4) | $T_{\text{pair}}$ only (cosmological) | One candidate, scope-flagged ✓ |

No category bleed; the two axes are independent and the confidence axis is monotone. Collapse ≠ mass-forming (§6.1). The trio answers the QM-foundations question without over-claiming: two of three legs are Class-4-consistent-with-QM, one leg supplies the single (cosmological) candidate discriminator.

---

## §8 — Files touched by this workstream

- **This research doc** (new): `research/2026-06-08_qm-foundations-trio.md`
- **KB cross-link** (consistency-class one-liner, synthesis-tagged): `manuscript/ave-kb/common/translation-tables/translation-qm.md` (Section A note under the `$|\psi|^2$` row)
- **KB guard note** (keep aliasing OUT of the thread): `manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md` (one-line note that the thread, not aliasing, is the entanglement mechanism)

Canonical leaves consulted (read-only): `ohmic-decoherence-born.md`, `statistics-under-ave.md`, `paley-wiener-hilbert.md`.
