# Freeze-Handedness Survey — Verdict Note (rotation-at-freeze chirality lock)

**Date:** 2026-06-10
**Branch:** `analysis/2026-06-10-survey-verdicts-consolidation`
**Provenance:** Read-only survey workflow (2026-06-10). No engine runs, no corpus mutation — a verdict consolidation over already-canon material. Every file:line below was **re-verified live in this worktree** before write (verify-before-cite governing); the one cite that did not re-verify cleanly is FLAGGED in §Verification, not silently dropped.
**Status:** FINDINGS FROZEN. One Grant-gated fork recorded OPEN at the foot (flag-don't-fix); one archive→canon promotion candidate surfaced for the auditor lane.

---

## §0 Verdict

Grant's "rotation-at-freeze sets the handedness" hypothesis is **not new** — it is **already canon as his own 2026-05-15 mechanism**. The survey's job was to locate it, classify its derivation status, and test the three downstream links (direction / sign / magnitude) into baryogenesis. Result: **mechanism CANON, value FIAT-IC** (`PARTIALLY-DERIVED`). The rotation story does not remove a free input; it **relocates** the input from a bare chirality fiat to the parent cosmic angular momentum `J_parent`.

---

## §1 The mechanism is canon (CANONICAL)

- The genesis mechanism is stated verbatim as **"Grant hypothesis, 2026-05-15"** at [`trampoline-framework.md:95`](../manuscript/ave-kb/common/trampoline-framework.md), with the full derivation at lines 97–105: crystallization while rotating at $\Omega_{\text{freeze}}$ locks bond rest-lengths at the rotating-frame equilibrium, giving over-bracing $u_0 = \rho\,\Omega_{\text{freeze}}^2\, r_{\text{node}}^2 / 2K_0$ (line 103) and right-handed chirality by the right-hand rule on centrifugal-force × bond-axis (line 105). **CANONICAL.**
- The cosmic-spin source is canon at [`omega-freeze-cosmic-grain-cascade.md:206`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md): **"Parent-BH-spin → daughter-K4-chirality lock"** via the same $u_0$ relation; reinforced at [`cosmic-axes-and-frames-glossary.md:71-73`](../manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md) where $\hat{J}_{\text{parent}}$ **is identified with** $\hat{\Omega}_{\text{freeze}}$ and the pre-crystallization phase is the supercooled pre-geodesic plasma inside the parent BH's $r_s$.
- The datasheet states the same at [`11_topological_characteristics.tex:95`](../manuscript/vol_9_vacuum_datasheet/chapters/11_topological_characteristics.tex): right-handed $I4_1 32$ chirality is "selected at lattice genesis by the direction of $\hat{\Omega}_{freeze}$." **CANONICAL.**

**Rotation is SATURATED in the freeze canon** (not a loose hook): $u_0$ is the over-bracing primitive; $\alpha$ AND $G$ are both anchored *through* $u_0(\Omega_{\text{freeze}})$ ([`trampoline-framework.md:114,120-121`](../manuscript/ave-kb/common/trampoline-framework.md)); and **Q-G21** (simultaneous lattice-wide chirality locking) is resolved by coherent rotation as the synchronizer ([`trampoline-framework.md:119`](../manuscript/ave-kb/common/trampoline-framework.md) — "the rotation IS the synchronization mechanism. No super-luminal propagation required"). There is no idle DOF here for a new mechanism to occupy.

## §2 Value is fiat-IC; the rotation relocates, not removes (Grant-gated framing)

- The VALUE remains a cosmological initial condition, not an emergent number. This is **A-031 "God's Hand"** — confirmed at [`claim-quality-closure-roadmap.md:33`](../manuscript/ave-kb/claim-quality-closure-roadmap.md) ("Refines A-031 ('God's Hand' = cosmic-parameter horizon, NOT mechanism horizon …)"). The rotation story relocates the fiat from "pick a handedness" to "inherit $J_{\text{parent}}$." Classification: **PARTIALLY-DERIVED** (mechanism canon / value fiat-IC). Per `consistency-vs-emergence`: this is an **operating-point projection (Class E)** input, not an emergence-class derivation.

## §3 Bookkeeping correction (CANONICAL)

There is **no "four calibration inputs" framing anywhere in the corpus** — that count does not exist. The canonical framing is **ONE scale primitive ($\ell_{\text{node}}$) + ONE cosmological IC ($\hat{\Omega}_{\text{freeze}}$) + gated constants**:

- [`constants.py:114`](../src/ave/core/constants.py): the historical label was **"three calibration inputs" $\{m_e, \alpha, G\}$**, reconciled under structural closure to "one scale ($\ell_{\text{node}}$) plus constants derived at Class B substrate-mechanism manifestation."
- [`claim-quality-closure-roadmap.md:92`](../manuscript/ave-kb/claim-quality-closure-roadmap.md): the `constants.py` internal contradiction was reconciled to **"ONE SCALE + GATED CONSTANTS."**

So "four inputs" is a phantom; the rotation reframe collapses $\{\alpha, G, \mathcal{J}_{\text{cosmic}}\}$ onto the single IC $\hat{\Omega}_{\text{freeze}}$, consistent with the canon, not additive to it.

## §4 Non-rotating counterfactual — the real fork is already derived (PROMOTION CANDIDATE)

The naive counterfactual is "no rotation → racemic universe." The canon is **sharper**: $\Omega = 0 \Rightarrow u_0 = 0 \Rightarrow$ no over-bracing $\Rightarrow$ no magic-angle operating point $\Rightarrow$ the lattice is **NON-VIABLE**, not merely racemic (per the $u_0$ chain at `trampoline-framework.md:103,120`). The substantive fork is **driven-vs-stochastic origin**, and it is **already derived** in the archive at [`59_memristive_yield_crossing_derivation.md:267`](../research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md): "Our single-domain universe instead requires a **driven origin** at cosmic scale." → **PROMOTION CANDIDATE (archive → canon)** for the auditor lane: the driven-origin argument already exists, unpromoted.

## §5 Baryon link — SPLIT three ways

| Link | Verdict | Class |
|---|---|---|
| **Direction-link** ($\hat{\Omega}_{\text{freeze}} \to$ observed spin/matter axis) | present-weak; inherits the **C5 5.33σ adverse tension** (CMB–LSS alignment excluded at 5.33σ from zero, [`claim-quality-closure-roadmap.md:88`](../manuscript/ave-kb/claim-quality-closure-roadmap.md)) | consistency-class (adverse) |
| **Sign-link** (handedness $\to$ matter/antimatter) | transitive and clean | CANONICAL |
| **Magnitude-link** ($\eta \propto L_{\text{net}}$) | CONTRADICTED-soft (would over-determine) | consistency-class, do-not-build |

- **Sign-link (CANONICAL):** [`baryon-asymmetry.md:24-25`](../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/baryon-asymmetry.md) (lattice chirality → C and CP violation) + [`chirality-and-antimatter.md:10`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/chirality-and-antimatter.md) ("an electron ($e^-$) is a right-handed unknot; a positron ($e^+$) … wound as a left-handed unknot").
- **Magnitude-link (CONTRADICTED-soft):** the corpus already derives $\eta$ from a **zero-parameter** route, $\eta = \delta_{CP}\cdot\alpha_W^4\cdot C_{sph}/g_*$ ([`baryon-asymmetry.md:42-46`](../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/baryon-asymmetry.md)) — but that claim is **`clm-4vwsjc`, confidence 0.4, build_status "do not build on, rework needed"** (registry status pinned at [`vol2/claim-quality.md:491,496`](../manuscript/ave-kb/vol2/claim-quality.md), block header `clm-4vwsjc` at :476; the leaf `baryon-asymmetry.md` itself carries only `claims: [clm-4vwsjc]` at :5). A second magnitude route $\eta \propto L_{\text{net}}$ from the freeze would be **over-determination**, not corroboration. Per `consistency-vs-emergence`: the existing $\eta$ formula is consistency-class with an **imported electroweak-baryogenesis formula** (the substrate supplies $\delta_{CP}$, $g_*$, $C_{sph}$ assignments; the $\alpha_W^4 C_{sph}/g_*$ scaffold is SM-imported), not emergence-class — do not headline.

---

## §6 Class-tag table

| Claim | Cite (re-verified) | Class |
|---|---|---|
| Rotation-at-freeze sets handedness | `trampoline-framework.md:95-105` | CANONICAL (Grant 2026-05-15) |
| Parent-BH-spin → K4 chirality lock | `omega-freeze-cosmic-grain-cascade.md:206`; `cosmic-axes-and-frames-glossary.md:71-73` | CANONICAL |
| $I4_1 32$ chirality selected by $\hat{\Omega}_{freeze}$ | `11_topological_characteristics.tex:95` | CANONICAL |
| $\alpha$ + $G$ + Q-G21 anchored through $u_0(\Omega)$ | `trampoline-framework.md:114,119,120-121` | CANONICAL |
| VALUE is fiat-IC (A-031 God's Hand), rotation relocates to $J_{\text{parent}}$ | `claim-quality-closure-roadmap.md:33` | PARTIALLY-DERIVED / Class-E input |
| No "four calibration inputs"; ONE scale + ONE IC + gated | `constants.py:114`; `claim-quality-closure-roadmap.md:92` | CANONICAL (bookkeeping correction) |
| $\Omega=0 \Rightarrow$ non-viable lattice (not merely racemic) | derived from $u_0$ chain | hypothesis (derived-framing) |
| Driven-vs-stochastic origin already derived | `59_memristive_yield_crossing_derivation.md:267` | PROMOTION CANDIDATE (archive→canon) |
| Direction-link present-weak | `claim-quality-closure-roadmap.md:88` (5.33σ) | consistency-class (adverse) |
| Sign-link transitive | `baryon-asymmetry.md:24-25`; `chirality-and-antimatter.md:10` | CANONICAL |
| Magnitude-link $\eta\propto L_{\text{net}}$ would over-determine | `baryon-asymmetry.md:42-46` (η formula); `vol2/claim-quality.md:491,496` (`clm-4vwsjc` registry: conf 0.4, do-not-build) | consistency-class, do-not-build |

## §7 KB-action / Grant-gated queue

- **GRANT-GATED FORK (OPEN — do not resolve):** two coexisting baryogenesis mechanisms sit in the corpus unreconciled.
  - Archive: [`59_memristive_yield_crossing_derivation.md:283`](../research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md) — **"No CP violation required; no baryon-number violation required; no out-of-equilibrium condition required"** (topological-inheritance baryogenesis).
  - Canon: [`baryon-asymmetry.md:12-26`](../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/baryon-asymmetry.md) — **imports the Sakharov conditions** (B-violation, C+CP violation, equilibrium departure) and reproduces them inside the lattice.
  - These are physically distinct origin stories (inherited-seed vs dynamically-generated). Surfaced verbatim per flag-don't-fix; **Grant adjudicates** which is canonical or whether both survive at different scales. Not resolved here.
- **PROMOTION CANDIDATE (auditor lane):** the driven-origin argument (`59:267`) → promote archive→canon as the freeze-driven single-domain mechanism. Implementer surfaces; auditor lands.

---

## §Verification (verify-before-cite, re-grepped live 2026-06-10 in this worktree)

All cites in §1–§6 re-verified verbatim against the named files/lines. Notes:

- `59_memristive_yield_crossing_derivation.md` is **titled** "Memristive Yield-Crossing Derivation" — a casual filename match would look wrong for baryogenesis, but the §5.4 baryogenesis content is genuinely present at lines 267 and 283 (verbatim-verified). Verify-before-cite earned its keep here.
- `closure-roadmap.md` resolves to the actual file **`claim-quality-closure-roadmap.md`** (no bare `closure-roadmap.md` exists in the tree); :92 and :88 verified there.
- No cite in this note FAILED re-verification.
- **Registry-pin precision (auditor FINDING 2, applied 2026-06-10):** the `clm-4vwsjc` `confidence 0.4` / `do not build on, rework needed` value is verbatim-correct but its registry home is [`vol2/claim-quality.md:491,496`](../manuscript/ave-kb/vol2/claim-quality.md) (block header `clm-4vwsjc` at :476), **not** `baryon-asymmetry.md` (which carries only `claims: [clm-4vwsjc]` at :5). §5 and §6 now pin both the formula location and the registry-status location. Non-falsifying cite-location polish (Class-B); the value and the do-not-headline conclusion are unchanged.
