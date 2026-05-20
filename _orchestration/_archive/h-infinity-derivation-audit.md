# H_∞ Derivation Audit Epic

**Status**: ACTIVE — implementor kickoff pending
**Last updated**: 2026-05-19 EOD
**Originating session**: Orchestration session following cosmic-axis-glossary Phase 4 Class-A halt

## Why this exists

The cosmic-axis-glossary implementor session correctly halted Phase 4 with a Class-A correctness flag: the orchestration brief had assumed commit `912dd88` ("consistency in framing of Hubble Constant as consistency check vs. prediction" by Benn Herrera, 2026-04-28) was on `analysis/integration` and had created a `"First principles"` ↔ `"Geometric consistency"` corpus inconsistency that needed fixing. Verification proved `912dd88` lives only on branches `benn/long-running` + `golden-torus-update`, never landed on `analysis/integration`. Both the KB leaf at [`lattice-genesis-hubble-tension.md:24`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md) and the LaTeX at [`04_generative_cosmology.tex:42`](../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex) currently carry the original `"First principles"` framing and are internally consistent in their pre-walk-back state.

The underlying physics question that `912dd88` raised is the real adjudication target: **is $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2)$ an independent first-principles prediction, OR a geometric-consistency identity rearrangement of the $G$ derivation?**

`912dd88`'s structural claim: $G$'s derivation routes through $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ with $R_H \equiv c/H_\infty$ substituted in, so $H_\infty$ and $G$ are one constraint, not two — making the "compute $H_\infty$ from $G$ to within 1σ of TRGB" framing a self-consistency check rather than an independent prediction.

This epic exists to **run down the math** — verify or refute the identity claim, characterize the dependency structure, and produce an audit-grade research doc that orchestration + Grant can use to adjudicate the framing forward on `analysis/integration`.

## The math question (precisely stated)

Two derivation chains need to be traced and compared:

1. **Chain A** (the H_∞ derivation): from substrate physics → $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2) \approx 69.32$ km/s/Mpc.
2. **Chain B** (the G derivation): from substrate physics → $G$ via Machian boundary impedance integration involving $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ and the cosmological horizon $R_H$.

Audit questions:

- **Q1**: Does Chain B require $R_H$ (and therefore $H_\infty \equiv c/R_H$) as INPUT? If yes — what role does it play? Is the substitution literal ($R_H$ enters $\xi$ explicitly) or does it enter via a different path?
- **Q2**: If Chain B uses $R_H$ as input, then substituting Chain B's $G$ into Chain A and solving for $H_\infty$ is algebraically circular. Verify this algebraically — is the resulting expression an IDENTITY (e.g., $H_\infty = H_\infty$ after simplification) or does it yield a genuine constraint?
- **Q3**: Is there an ALTERNATIVE Chain B' (an independent $G$ derivation NOT routing through $R_H$ / $H_\infty$)? Specifically: is $G$ derivable from local-thermodynamic-balance arguments (lattice tension, node-equipartition, per-node generation rate) WITHOUT cosmological-horizon-scale inputs?
- **Q4**: What does the corpus claim about Chain B' (independent $G$ derivation)? Is it a stated open gap, an implicit assumption, or has it been attempted?

Outcome map (no preferred outcome — the math decides):

| Math finding | Framing implication |
|---|---|
| Q2 yields identity AND no Chain B' exists | $H_\infty$ value is a consistency check, not an independent prediction. Corpus should walk back `"First principles"` to `"Geometric consistency"`. Effectively confirms 912dd88. |
| Q2 yields identity BUT Chain B' exists in corpus | Both framings can be made consistent: $H_\infty$ becomes a genuine prediction VIA the Chain B' path. Corpus framing depends on which $G$ derivation it cites. |
| Q2 does NOT yield identity (algebraic check fails) | 912dd88's claim is wrong; "First principles" framing on `analysis/integration` is correct as-is. |
| Q1: Chain B doesn't use $R_H$ at all | 912dd88's premise is wrong from the start. "First principles" framing is correct. |

## Scope (single phase: math audit + research doc)

**In scope:**
- Read + trace Chain A ($H_\infty$) derivation on `analysis/integration` HEAD
- Read + trace Chain B ($G$) derivation on `analysis/integration` HEAD  
- Inspect `912dd88` via `git show 912dd88` to read Benn's analysis verbatim (this is allowed — historical commits are visible across all branches)
- Algebraically verify or refute the identity claim (Q2)
- Search corpus for Chain B' candidates (independent $G$ derivation paths)
- Produce a research doc at `research/2026-05-19_h-infinity-derivation-audit.md` (or 2026-05-20 if session spans midnight)

**Out of scope:**
- Any corpus rewrites (`lattice-genesis-hubble-tension.md`, `04_generative_cosmology.tex`, `predictions.yaml`) — these are downstream of the math finding; orchestration + Grant adjudicate after research doc lands
- New derivations from scratch — this is an audit of existing derivations, not new physics
- The cosmic-axis-glossary branch (`analysis/cosmic-axis-glossary`) — that's a separate epic, held pending Phase 4 adjudication
- Any decision on Option A / B / C from the cosmic-axis-glossary Phase 4 framing — research doc is INPUT to that decision, not the decision itself

## Starting points (files to read first)

Implementer is expected to read these in order, then expand as the audit requires:

1. [`manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md) — the canonical $H_\infty$ formula leaf (Chain A starting point)
2. [`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md) — the Hubble-tension chapter
3. `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/` — the canonical $G$ derivation leaves (find them; likely names involve "machian", "boundary-impedance", "G-derivation", "newton-G")
4. [`manuscript/ave-kb/common/mathematical-closure.md`](../manuscript/ave-kb/common/mathematical-closure.md) — Outstanding Rigour Gaps table (currently 112 lines per the implementor's drift-check; if it has an $H_\infty$ / $G$ closure entry, that's the corpus's own statement of the gap)
5. [`manuscript/ave-kb/common/full-derivation-chain.md`](../manuscript/ave-kb/common/full-derivation-chain.md) — canonical derivation-chain registry
6. [`manuscript/ave-kb/common/xi-topo-traceability.md`](../manuscript/ave-kb/common/xi-topo-traceability.md) — $\xi$ traceability (directly relevant to Q1)
7. [`manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex`](../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex) — Vol 3 Ch 4 LaTeX source
8. [`manuscript/predictions.yaml`](../manuscript/predictions.yaml) — entry P23 ($H_\infty$ prediction) — verbatim claim text
9. `git show 912dd88` — Benn's walk-back diff, full content

## Skill discipline

- **`ave-prereg`** — SKIP. This is an audit of existing derivations, not a new derivation from scratch.
- **`consistency-vs-emergence`** — REQUIRED. This skill targets exactly this class of structural-circularity question. Apply it to classify the H_∞ ↔ G relationship per the skill's framework (definitional identity / axiom manifestation / consistency check / emergence test).
- **`ave-canonical-leaf-pull`** — REQUIRED. Pull the canonical leaves for $G$ derivation, Machian impedance, $\xi$ traceability, and $H_\infty$ derivation explicitly before deriving.
- **`ave-canonical-source`** — REQUIRED. If the research doc references constants ($m_e$, $\alpha$, $G$, $H_\infty$, $\ell_{node}$, $c$, $\hbar$), reference `src/ave/core/constants.py` for canonical values; do not hard-code.
- **`verify-before-cite`** — REQUIRED. Every file:line citation in the research doc must be re-grepped at execution time.
- **`ave-evidence-framing-discipline`** — REQUIRED. The research doc's conclusion must precisely match the strength of the evidence — no overreach ("Benn's analysis is correct" → "the algebraic identity check yields X, consistent with Benn's claim modulo Y").
- **Pure-AVE-corpus rule** — No external context.

## Branch + commit

- Branch: `analysis/h-infinity-derivation-audit` from `analysis/integration` HEAD (currently `d5693d7` — the orchestration commit landing the cosmic-axis-glossary brief)
- Commit: single commit at end of audit covering the research doc + any closure-roadmap update flagging the audit completion
- Push: yes
- Merge: NO — orchestration session merges after Grant adjudication on framing forward

## Expected return format

Research doc at `research/2026-05-19_h-infinity-derivation-audit.md` (or 2026-05-20 if session spans midnight) with sections:

1. **Audit question** (verbatim from this brief)
2. **Chain A — $H_\infty$ derivation** — verbatim formula, derivation chain with file:line citations, inputs identified
3. **Chain B — $G$ derivation** — verbatim derivation, chain with file:line citations, inputs identified
4. **Q1 finding** — does Chain B use $R_H$ / $H_\infty$ as input? Verbatim citation if yes.
5. **Q2 finding** — algebraic identity check. Show the substitution step-by-step. Verdict: identity / not-identity.
6. **Q3 finding** — Chain B' search. Does corpus have an independent $G$ derivation? Cite if yes.
7. **Q4 finding** — what does corpus claim about Chain B' existence? Cite mathematical-closure.md if relevant.
8. **Cross-check vs 912dd88** — read `git show 912dd88` and compare its analysis to this audit's findings. Note agreement / disagreement.
9. **Implication matrix** — for each of the 4 outcomes in this brief, state which one the math finding supports.
10. **NO recommendation on Option A / B / C** — that's Grant's adjudication. Research doc presents findings only.

Plus implementor return summary to orchestration session listing: commits, push status, audit findings summary (1 paragraph), self-audit verdict.

## Cross-references

- Halted phase (the trigger): [`cosmic-axis-glossary.md` Phase 4](cosmic-axis-glossary.md) — currently labeled DEFERRED, will be re-scoped after this audit lands
- Related branches: `benn/long-running`, `golden-torus-update` (carry 912dd88; not active integration)
- Active integration HEAD that needs the framing question resolved: `analysis/integration` at `d5693d7`
