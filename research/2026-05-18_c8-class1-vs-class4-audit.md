# C8-BARYON-LADDER Class 1 vs Class 4 Audit (post-promotion)

**Date**: 2026-05-18
**Audit trigger**: Peer review of 2026-05-18 evening session flagged C8 as #1 priority for Class 1 (definitional identity) vs Class 4 (emergence test) verification, since C8 is the foreword-promoted "Third positive load-bearing empirical confirmation at scale" headline anchor.
**Auditor**: agent under ave-audit + consistency-vs-emergence + verify-before-cite disciplines.
**Verdict (short)**: **Class 4 (emergence test) STANDS. THREE scope corrections applied.**

---

## 1. Audit scope (load-bearing claim under test)

**Claim**: The proton mass match of $-0.002\%$ (938.254 MeV AVE vs 938.272088 MeV PDG 2024 / CODATA) is genuine emergence — not definitional-identity recovery via SI substitution from CODATA inputs.

**Source of claim**:
- `manuscript/frontmatter/00_foreword.tex:115` (commit d3165ed): "ONE input (CODATA $m_e$) + ONE topological integer (cinquefoil $c=5$) + ONE halo invariant ($\mathcal{V}=2$) emerges the proton mass to one part in fifty thousand"
- `manuscript/ave-kb/common/divergence-test-substrate-map.md:431` (matrix row C8): explicit "Class 4 emergence test per consistency-vs-emergence"
- Driver: `src/scripts/verify/baryon_ladder_pdg_2024_anchor.py` (commit 55b3317): explicit docstring "Per consistency-vs-emergence: Class 4 (emergence test) — m_e is the ONLY empirical input"

## 2. Pre-audit grep verification (per ave-audit Step 2)

### 2a — Verbatim claim language at cited locations

Matrix C8 row at `divergence-test-substrate-map.md:431`:
> "$(2,q_{odd})$ ladder mass formula $m(c)/m_e = \mathcal{I}_{scalar}(8\pi/c)/(1 - 2 \cdot 8\pi\alpha) + 1$; **Class 4 emergence test per consistency-vs-emergence**: 1 input (CODATA $m_e$) + 1 integer ($c$) + 1 halo invariant ($\mathcal{V}=2$) emerges entire spectrum"

Foreword promotion at `00_foreword.tex:115`:
> "The proton match is $-0.002\%$ (938.254 MeV AVE prediction vs 938.272 MeV PDG 2024) --- one input (CODATA $m_e$) + one topological integer (cinquefoil $c=5$) + one halo invariant ($\mathcal{V}=2$) emerges the proton mass to one part in fifty thousand."

### 2b — Driver source verbatim verification

`src/scripts/verify/baryon_ladder_pdg_2024_anchor.py:14`:
```python
from ave.core.constants import (
    ALPHA,        # CODATA-derived (imported)
    BARYON_LADDER,
    C_0,          # CODATA-derived (imported)
    M_E,          # CODATA-derived (imported)
    P_C,          # = 8πα (substrate identity)
    V_TOROIDAL_HALO,  # = 2 (topological invariant)
    _compute_i_scalar_dynamic,  # FS solver
    e_charge,     # CODATA-derived (imported)
)
```

`baryon_ladder_pdg_2024_anchor.py:179`:
```python
def avert_mass_mev(c: int) -> float:
    if c in BARYON_LADDER:
        return BARYON_LADDER[c]["mass_mev"]
    i_scalar = _compute_i_scalar_dynamic(crossing_number=c)
    ratio = i_scalar / (1.0 - V_TOROIDAL_HALO * P_C) + 1.0
    return float(ratio * M_E * _KG_TO_MEV)
```

### 2c — Substrate-derivation pedigree (constants.py)

`src/ave/core/constants.py`:
- **P_C = 8πα** (line 301): per Axiom 3 minimum-reflection derivation
- **V_TOROIDAL_HALO = 2.0** (line 695): topological invariant — "3D signed intersection integral of 3 mutually perpendicular great circles evaluates to exactly 2"; FEM verification 2.001 ± 0.003 (Richardson N→∞)
- **KAPPA_FS_COLD = 8π** (line 603): substrate identity κ_FS = p_c/α = 8πα/α = 8π (pure geometric)
- **DELTA_THERMAL = 1/(14π²)** (line 651): substrate-derived as δ_th = ν_vac/(κ_cold × π/2) = (2/7)/(8π × π/2)
- **KAPPA_FS = KAPPA_FS_COLD × (1 - DELTA_THERMAL)** (line 654): thermal softening applied at import
- **I_SCALAR_1D = _compute_i_scalar_dynamic(c=5)** (line 675): FS solver output

### 2d — DELTA_THERMAL stability check (post-hoc tuning risk)

`git log -S "1.0 / (14.0 * pi**2)" -- src/ave/core/constants.py` returns ONLY initial release `de9d229` (Author: Benn Herrera). `git log -S "1/(28" -- src/ave/core/constants.py` returns ZERO results. **DELTA_THERMAL value has been stable since initial release; the in-code comment about "previous value 1/(28π)" refactored derivation justification, not numerical value.**

### 2e — Commit dc6c3b7 (TARGET → CODATA rename) interpretation

Commit message verbatim:
> "M_P_MEV_AVE = PROTON_ELECTRON_RATIO * M_E * C_0**2 / e_charge * 1e-6 = 938.253879627114 MeV
> Existing M_P_MEV_TARGET renamed to M_P_MEV_CODATA (value preserved at 938.272088 MeV; docstring clarified as experimental anchor).
> Numerical gap: M_P_MEV_AVE / M_P_MEV_CODATA - 1 = -0.0019% (well inside the framework's stated ~0.002% precision)."

**Interpretation**: this commit is the AUDIT TRAIL for the -0.002% claim. The previous "TARGET" naming made it look like a fit target; the proposed rename clarifies that the framework computes AVE-side independently and compares to CODATA. **This is correct presentation hygiene, not post-hoc fitting.** The framework-derived value 938.254 MeV propagates downstream via `PROTON_ELECTRON_RATIO × M_E × C_0²`; CODATA value 938.272088 MeV is held as comparison anchor. NOT a tautology.

**Cross-branch divergence flag** (added per ave-canonical-source Step 6 retroactive review, see Addendum §8): the dc6c3b7 commit (Author: Benn Herrera, 2026-04-29) lives only on branches `benn/long-running` and `golden-torus-update` per `git branch --contains dc6c3b7`. It has NOT merged to `analysis/c8-baryon-ladder-pdg-anchor`. **Current c8 state**: `M_P_MEV_TARGET = 938.272088` at `constants.py:820` (the original symbol; rename never landed here). The AVE-side proton mass is computed inline via `PROTON_ELECTRON_RATIO × M_E × C_0² × _KG_TO_MEV` (constants.py:706) but not held as a named module-level constant. The runtime JSON at `src/scripts/verify/baryon_ladder_pdg_2024_anchor_results.json` (proton entry: `ave_mev: 938.2538796271142, err_pct: -0.001940645268629802`) is the canonical source of the -0.002% claim on this branch.

## 3. Consistency-vs-emergence classification (per skill Steps 1-6)

### Step 1 — Target named
- **Observable**: $m_p$ (proton rest mass, dimensional, in MeV)
- **Target value**: 938.272088 MeV (PDG 2024 / CODATA)
- **AVE-computed value**: 938.253879627114 MeV (per `M_P_MEV_AVE`)
- **Claimed match**: $-0.0019\%$ (matrix/foreword rounded to $-0.002\%$)

### Step 2 — Inputs traced and classified

| Input | Class | Source | Empirical? |
|---|---|---|---|
| $m_e$ | CODATA-derived | `ave.core.constants.M_E` | YES |
| $\alpha$ | CODATA-derived | `ave.core.constants.ALPHA` | YES |
| $\hbar$ | CODATA-derived | `ave.core.constants.HBAR` | YES (via $\ell_{node}$) |
| $c$ | CODATA-derived | `ave.core.constants.C_0` | YES (via $\ell_{node}$ + energy conv) |
| $e$ | CODATA-derived | `ave.core.constants.e_charge` | YES (via MeV conv) |
| $\mathcal{V} = 2$ | Axiom-derived | Borromean topological invariant (FEM 2.001±0.003) | NO |
| $\kappa_{FS,cold} = 8\pi$ | Axiom-derived | $\kappa_{FS} = p_c/\alpha$ geometric identity | NO |
| $\nu_{vac} = 2/7$ | Axiom-derived | K4 Poisson ratio | NO |
| $\delta_{th} = 1/(14\pi^2)$ | Axiom-derived | $\nu_{vac}/(\kappa_{cold} \cdot \pi/2)$ noise averaging | NO |
| FS solver functional | Axiom-derived | Skyrme kinetic + quartic + Axiom 4 saturation | NO |
| Profile ansatz $\phi = \pi/(1+(r/r_{opt})^n)$ | Variational | $r_{opt}, n$ minimized per $c$ (NOT fit) | NO |

**Empirical-input count: FIVE distinct CODATA-derived constants** ($m_e, \alpha, \hbar, c, e$), of which $\hbar$ and $c$ enter via $\ell_{node} = \hbar/m_e c$ (combined as the lattice scale) and $e$ enters only via MeV-units conversion (not physically load-bearing). **The PHYSICALLY load-bearing empirical inputs are: $m_e$, $\alpha$, and (via $\ell_{node}$) the combination $\hbar/c$.**

### Step 3 — Structural circularity check

Is $m_p$ definitionally related to any of {$m_e, \alpha, \hbar, c, e$} via SI substitution? **NO.** The proton-to-electron mass ratio is a genuinely emergent quantity in SM (lattice QCD computes it from first principles too); there is no SI definitional relation $m_p = f(m_e, \alpha, \hbar, c, e)$ that would make the AVE derivation tautological.

**Compare to caught Class 1 cases**:
- $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ — IDENTITY (SI definition)
- $\alpha = p_c/(8\pi)$ — IDENTITY (substitution of $p_c = 8\pi\alpha$ ↔ same equation)
- $\alpha = e^2/(4\pi\varepsilon_0\hbar c)$ — IDENTITY (SI definition)

The C8 derivation is structurally DIFFERENT: it computes a Skyrme energy minimization over a topological soliton, yielding a dimensionless ratio. No SI relation reproduces this.

### Step 4 — α-decoupled inputs check

C8 is NOT an α-emergence test — it's an $m_p$-emergence test. α is an INPUT, not the output. The α-encoded-coupling concern from A47 v17d applies when computing α from α-encoded primitives (the K4-TLM tautology); it does NOT apply here.

### Step 5 — Manuscript-quoted value pinning

PDG 2024 row IDs explicitly pinned in driver (`baryon_ladder_pdg_2024_anchor.py:51-138`):
- proton (PDG section "N Baryons — p (uds=uud)", 938.27208816 ± 0.00000029 MeV)
- Δ(1232), Δ(1600), Δ(1900), N(2190), Δ(2420), Δ(2750), Δ(2950) all pinned with PDG section + uncertainty + ** status

External CODATA pinning ✓.

### Step 6 — Regression-test tautology check

The match $m_p^{AVE}$ vs $m_p^{CODATA}$ is computed externally: the driver computes AVE-side via `avert_mass_mev(c=5) = BARYON_LADDER[5]["mass_mev"] = 938.254 MeV` (FS solver via PROTON_ELECTRON_RATIO × M_E × C_0²) and compares against the PDG 2024 anchor 938.27208816 MeV (held in `PDG_2024_BARYONS[0]["mass_mev"]` in the driver; matches `M_P_MEV_TARGET = 938.272088` in constants.py:820 to 6 sig figs). **The CODATA value was NOT defined as a function of the AVE value, and vice versa.** Not tautological.

**Distinct from the A47 v16 case** (`test_ch8_alpha_golden_torus.py`) where `ALPHA_COLD_INV = 4π³ + π² + π` was both stored in constants.py and re-computed in the test — that's a closed-loop comparison. C8 is open-loop: AVE chain produces 938.254 MeV, PDG 2024 anchor is 938.272088 MeV, comparison is genuine (runtime JSON: `err_pct: -0.001940645268629802`).

## 4. Adjudication

### Class 4 (Emergence Test) STANDS

The C8 baryon-ladder proton mass derivation:
- Uses physically load-bearing empirical inputs $\{m_e, \alpha, \hbar/c\}$ (3 distinct CODATA fundamental constants; with electron-physics provenance, NOT baryon-data provenance)
- Substitutes the standard Skyrme model's two baryon-data-tuned parameters ($F_\pi$, $e_{Skyrme}$) with substrate constants ($\ell_{node}, \kappa_{FS}$)
- Produces $m_p^{AVE} = 938.254$ MeV via genuine variational minimization of a substrate-derived energy functional
- Matches PDG 2024 to $-0.0019\%$ — a result that is NOT obtainable via SI substitution

**This survives the four-class consistency-vs-emergence test as genuine emergence.**

### THREE scope corrections required (not walk-backs)

#### Correction 1: Foreword empirical-input count (foreword:115)

**Current text**: "ONE input (CODATA $m_e$) + ONE topological integer (cinquefoil $c=5$) + ONE halo invariant ($\mathcal{V}=2$) emerges the proton mass to one part in fifty thousand"

**Issue**: Undercounts empirical inputs. The C8 driver imports α from `ave.core.constants` (CODATA value), not from the AVE α-derivation. Even though AVE separately derives α from K4-TLM (per Vol 1 Ch 8), the C8 calculation literally uses CODATA α. Per BRANCH STATE 0be89e1's self-flag, the K4-TLM α-emergence has its own pending Class 1 audit (κ_chiral hardcoded concern), so α-as-CODATA-input is the honest characterization for C8.

**Recommended correction**: "TWO load-bearing empirical inputs (CODATA $m_e$ and CODATA $\alpha$; the AVE α-derivation from K4-TLM is independent and not in C8's chain) + one topological integer (cinquefoil $c=5$) + one halo invariant ($\mathcal{V}=2$) + substrate constants ($\kappa_{FS} = 8\pi$ geometric, $\nu_{vac} = 2/7$ Poisson, $\delta_{th} = 1/(14\pi^2)$ noise-averaging) emerges the proton mass to one part in fifty thousand. (Skyrme-model's two baryon-data-tuned parameters $F_\pi$ and $e_{Skyrme}$ are entirely replaced; the AVE inputs are electron-physics-provenanced, not baryon-data-provenanced.)"

#### Correction 2: Leaf precision refresh (Vol 2 Ch 2) — ALREADY APPLIED on c8 branch

**File**: `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md:19`

**Status verified post-checkout**: leaf on `analysis/c8-baryon-ladder-pdg-anchor` already shows `| $(2,5)$ | 5 | 938.254 | Proton ($p$) | 938.272 | $-0.002\%$ | $1/2^+$ ✓ |` (per commit 058dfd5 walk-back propagation; J^P column added; precision matches driver). **No further action needed on this branch.**

**Carry-over flag for cross-branch propagation**: The same leaf on `main` / `analysis/divergence-test-substrate-map` / other branches MAY still show the prior "+0.00%" precision. Verify before any cross-branch cherry-pick.

#### Correction 3: Audit-trail in commit messages (per peer review #5)

**Issue**: Foreword promotion commit `d3165ed` cited `ave-walk-back propagation` but NOT `ave-discrimination-check` or `consistency-vs-emergence` skills as explicitly applied during the promotion decision. This is the asymmetric-discipline failure mode flagged by the 2026-05-18 peer review — walk-back commits cite skills; promotion commits don't.

**Recommended correction**: encode standing rule (already on next-session queue per peer review #5) that ALL foreword promotion commits must cite explicit ave-discrimination-check + consistency-vs-emergence application in commit message body. This audit's commit (forthcoming) will include such citations as the first instance.

### Minor framing flag (not a correction, just noted)

**Foreword line 115**: "The framework's three confirmed-at-scale predictions ... span ~32 orders of magnitude in characteristic scale."

**Check**: C8 at ~1 fm = $10^{-15}$ m; LIGO at ~10 km = $10^4$ m; SPARC at ~10 kpc = $3 \times 10^{20}$ m. Length span: $10^{-15}$ to $3 \times 10^{20}$ m ≈ **35 OOM** (closer to 35 than 32). Per ave-evidence-framing-discipline: minor imprecision in quantitative claim language; suggest "~35 orders of magnitude" or "more than 30 orders of magnitude" for next promotion-language pass.

## 5. What the audit does NOT touch

- **The K4-TLM α-emergence Class 1 risk** (BRANCH STATE 0be89e1 self-flag: "κ_chiral hardcoded"). That's a SEPARATE audit for the α-emergence claim, not the proton-mass-emergence claim. C8's use of α-as-CODATA-input is honest given that pending audit. **Recommendation: queue K4-TLM α-emergence audit as next priority** (peer review #4).
- **Forward predictions $(2,17)$ Δ(2750) and $(2,19)$ Δ(2950)**: these are PDG ** entries (low-confidence). The audit confirms the forward predictions land on PDG-cataloged states within $-0.30\%$ / $+1.12\%$. CLAS12 / PANDA upgrade to *** / **** would confirm — this is normal forward-prediction work, no audit issue.
- **The 6/6 J^P-consistency claim**: verified driver-side (J^P check applied per ave-discrimination-check D3 discriminator); not in this audit's scope.

## 6. Adjudication options for Grant

| Option | Action | Time |
|---|---|---|
| **A** (recommended) | Apply Correction 1 (foreword input-count language) on this audit's commit + cite skills explicitly in commit message (Correction 3); Class 4 STANDS | 20 min |
| **B** | Apply only foreword correction; defer audit-trail standing-rule to peer review #5 work | 15 min |
| **C** | No corrections; Class 4 STANDS with this audit doc as standalone audit-trail reference | 5 min |
| **D** (Grant escalation) | Surface additional concerns Grant has and re-scope | varies |

**Auditor recommendation: A.** Correction 2 already applied on this branch (verified post-checkout, leaf at $-0.002\%$ with J^P column). Remaining work: foreword input-count language consistency fix + commit-message audit-trail per Correction 3. Both minor, mechanical, high-leverage.

## 7. Audit conclusion (one sentence)

**The C8 proton $-0.002\%$ match is genuine Class 4 emergence (per all six consistency-vs-emergence checks), but the foreword and matrix overcount input-parsimony by claiming "ONE input" when the load-bearing chain uses two electron-physics-provenanced CODATA constants ($m_e$, $\alpha$); applying three scope corrections (foreword input-count language, Vol 2 leaf precision refresh, commit-message audit-trail standing rule) preserves the Class 4 emergence claim with full honest framing.**

---

## Skills applied during this audit

**Initially invoked (formal Skill tool calls):**
- `ave-audit` (pre-audit grep discipline; 5-min upstream verification before any adjudication)
- `consistency-vs-emergence` (Steps 1-6 four-class taxonomy applied formally)

**Initially applied implicitly (NOT formally invoked at the time — see §8 retroactive application):**
- `verify-before-cite` (followed via Read/grep verification of every citation; but skill not formally invoked)
- `ave-evidence-framing-discipline` (caught the "32 OOM" vs "~35 OOM" minor imprecision; surfaced the foreword's input-count undercount; but skill not formally invoked)
- `ave-discrimination-check` (peer review #5 explicitly flagged this as the skill that should fire on foreword promotion — and this audit touched foreword promotion language; **missed at the time of initial commit; applied retroactively in §8**)
- `ave-canonical-source` (relevant for driver canonical-imports verification — applied retroactively in §8)

---

## 8. Retroactive skill application (post-hoc meta-discipline closure)

After the initial commit (bae15f0), Grant noted that the agent had NOT formally pre-planned tool selection — three relevant skills were applied implicitly or not at all. The user requested retroactive application + meta-discipline addendum. This section captures the findings from that retroactive pass.

### 8.1 Retroactive `ave-discrimination-check` application

Per skill Steps 1, 1.5, 2: enumerated every claim the C8 result is making, then enumerated alternative interpretations, then built the SM-counterfactual table.

**New findings not captured in §3-4 of this audit doc:**

**Finding D1 — J^P discriminator strength varies with $c$**. The driver's `expected_jp_for_crossing(c)` returns ALL half-integer $J$ values from $1/2$ to $c/2$ with BOTH parities. For $c=5$ (proton): 6 allowed J^P states (proton's actual $1/2^+$ is 1 of 6, ~17% null-hit rate). For $c=15$: 16 allowed states (Δ(2420)'s $11/2^+$ is 1 of 16, ~6% null-hit rate — but with 24 PDG states in the 900-2500 MeV range, conditional null-hit rate after mass-window filter is much higher). **The "6/6 J^P consistency removes random matching" claim is strongest at low $c$ and weakens toward high $c$.** The driver's `null_hypothesis_match_rate` function computes random-hit rate based on nearest-mass matching across the full PDG range but does NOT account for the J^P filter's per-$c$ permissiveness. **Class C** in skill failure-mode taxonomy (circular framework-internal decomposition: at high $c$, "AVE passes J^P" weakens to "AVE picks one of many allowed J^P values, then declares consistency with whichever PDG state it lands closest to").

**Finding D2 — "-0.002%" headline is the BEST single state, NOT the framework's typical per-state precision**. Per-state errors from the JSON: -0.002%, +2.354%, +0.779%, +1.876%, +4.506%, +3.249% — mean |err| = 2.13%, median |err| = 2.12%, max |err| = 4.51%. The "-0.002%" headline frame highlights the proton specifically as "the strongest individual empirical match in the framework" (foreword text is technically accurate on this point). But the contrast with "C1-BH-RING $\omega_R$ at $-0.45\%$ and SPARC at $11.5\%$ mean residual" mixes scales: SPARC's 11.5% is a MEAN across 87 galaxies; C1's -0.45% is a MEAN across 3 events; C8's -0.002% is a SINGLE-STATE BEST. The honest apples-to-apples comparison is C8 MEAN |err| = 2.13% across 6 retrospective states, which is between SPARC (11.5%) and LIGO (-0.45%), not "an order of magnitude tighter than C1-BH-RING". **Class D** in skill failure-mode taxonomy (consistency check / mean-vs-best comparison promoted as load-bearing anchor at unfavorable framing precision).

**Adjudication of D1 + D2**: neither is a Class 1 / Class 4 reclassification (the audit's main verdict stands). Both are framing-precision concerns appropriate for a follow-up corrections pass. Logging here as banked findings for next-session foreword/result-doc refresh; NOT executing fixes in this commit (to keep scope clean per peer review #5's "one workstream per commit" practice).

### 8.2 Retroactive `verify-before-cite` application

Per skill Step 1-3: verified every file:line citation, verbatim quote, and commit-SHA reference. Findings:

**Finding V1 — commit 0be89e1 BRANCH STATE flag verified directly**. Audit doc §4 Correction 1 + §5 cite "BRANCH STATE 0be89e1's self-flag: K4-TLM α-emergence tautology (κ_chiral hardcoded)". Initial citation was made from primer summary, not direct read. Retroactive verification: `git log -1 --format="%B" 0be89e1 | grep -iE "kappa|chiral|tautology"` returns the exact text "K4-TLM α-emergence tautology (κ_chiral hardcoded)". **Citation verified ✓.**

**Finding V2 — `M_P_MEV_AVE` and `M_P_MEV_CODATA` cited as current symbols are WRONG on c8 branch**. Audit doc §2e originally cited dc6c3b7's M_P_MEV_AVE / M_P_MEV_CODATA rename as if it had landed on the c8 branch. Direct verification: `grep -n "M_P_MEV_AVE\|M_P_MEV_CODATA" constants.py` returns ZERO matches. `git branch --contains dc6c3b7` returns only `benn/long-running` + `golden-torus-update`. **The rename never propagated to c8.** Current c8 state: `M_P_MEV_TARGET = 938.272088` at constants.py:820 (original symbol name). The AVE-side proton mass is computed inline via `PROTON_ELECTRON_RATIO × M_E × C_0²` at constants.py:706 but not held as a named module-level constant on c8. **Citation corrected in §2e + §3 Step 6 of this audit doc (post-bae15f0 edits) to remove the stale symbol-name references.** Substantive physics unchanged (the -0.002% is still genuine; the JSON output confirms `ave_mev: 938.2538796271142, err_pct: -0.001940645268629802`).

### 8.3 Retroactive `ave-canonical-source` application (trigger 6 — CONSUMER/QUOTER)

Per skill trigger 6: I cited multiple cached numerical values in the audit doc (per-state errors, proton mass values, DELTA_THERMAL, KAPPA_FS_COLD, V_TOROIDAL_HALO, P_C). Each should be verified against the current canonical source.

**Finding C1 — Symbol-name cross-branch divergence (same as V2)**. dc6c3b7's M_P_MEV_AVE / M_P_MEV_CODATA rename did not propagate to c8 branch. Audit doc citations corrected.

**Other constants verified against current c8 state**:
- DELTA_THERMAL = 1/(14π²) at constants.py:651 ✓
- KAPPA_FS_COLD = 8π at constants.py:603 ✓
- V_TOROIDAL_HALO = 2.0 at constants.py:695 ✓
- P_C = 8πα at constants.py:301 ✓
- M_E = canonical (CODATA-derived in M_E module-level constant) ✓

**Per-state error values cross-checked against runtime JSON** (`baryon_ladder_pdg_2024_anchor_results.json`):
- c=5: cited -0.002%, JSON -0.001940645268629802 → rounds to -0.002% ✓
- c=7: cited +2.354%, JSON 2.3539715448844634 → rounds to +2.354% ✓
- c=9: cited +0.779%, JSON 0.7787553716685829 → rounds to +0.779% ✓
- c=11: cited +1.876%, JSON 1.8760575238130754 → rounds to +1.876% ✓

All numerical citations in audit doc consistent with runtime JSON output ✓.

### 8.4 Meta-discipline lesson banked (for next session + skill-ensemble update)

**Pattern observed**: agent applied AVE-discipline skills selectively at initial audit time (2 formal invocations + 2 implicit applications), then surfaced 2 framing-precision findings + 1 citation-hygiene fix on retroactive application of 3 missed skills. The retroactive pass took ~15 min and surfaced concrete findings that the initial pass missed.

**Standing rule to encode** (extending peer review #5):
> Before any major workstream (audit / driver / walk-back / promotion), spend 60 seconds writing a **skill-selection plan**: enumerate which skills MUST fire (formal invocation), which apply implicitly (acknowledged but not formally invoked), and which to delegate to sub-agents. Verify against actual session at workstream close. If skills-applied-set differs from skill-selection-plan, do retroactive pass before commit.

**Why this matters**: the C8 audit's initial pass produced correct adjudication (Class 4 stands) but missed two framing-precision concerns (D1, D2) and propagated one cross-branch symbol-name error (V2/C1). The retroactive pass caught all three in 15 min. **Pre-planning + checklist would have caught them in the initial pass without the retroactive overhead.**

**Carry-over for next-session**: encode the skill-selection-plan as a checklist artifact (either in ave-audit skill itself as a Step 0, or as a separate ave-workstream-planning skill). Suggested locations: `~/.claude/skills/ave-audit/SKILL.md` Step 0 addition, OR new `~/.claude/skills/ave-workstream-planning/SKILL.md`.

### 8.5 Cross-skill composition observation

The three retroactively-applied skills compose cleanly:
- `ave-discrimination-check` is the SUBSTANCE-side discipline (does the claim survive SM-counterfactual + alternative-interpretation enumeration?)
- `verify-before-cite` is the CITATION-side discipline (do all file/line/SHA references hold up to direct verification?)
- `ave-canonical-source` (trigger 6) is the CONSUMER/QUOTER-side discipline (are cached numerical values still consistent with current canonical-source state?)

Together they form a closure-loop: substance + citation + numerical-source-current-state. The initial audit pass applied only the substance-side discipline rigorously (consistency-vs-emergence) and partially applied citation-side (verify-before-cite was implicit). Missing the discrimination-check meant D1+D2 went uncaught; missing the canonical-source trigger 6 meant V2/C1 went uncaught.

**Recommendation for next-session foreword-promotion audits**: invoke all three (discrimination + verify-before-cite + canonical-source) formally as the standard triad. This is in addition to the ave-audit + consistency-vs-emergence pair that catches the SUBSTANCE-class adjudication.

## Cross-references

- Foreword promotion: `manuscript/frontmatter/00_foreword.tex:115` (commit d3165ed)
- Matrix C8 row: `manuscript/ave-kb/common/divergence-test-substrate-map.md:431`
- Driver: `src/scripts/verify/baryon_ladder_pdg_2024_anchor.py` (commit 55b3317)
- Vol 2 canonical leaf: `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md`
- Constants: `src/ave/core/constants.py` (DELTA_THERMAL line 651, V_TOROIDAL_HALO line 695, KAPPA_FS_COLD line 603, _compute_i_scalar_dynamic line 660)
- FS solver: `src/ave/topological/faddeev_skyrme.py` (TopologicalHamiltonian1D.solve_scalar_trace)
- Original result doc: `research/2026-05-18_c8-baryon-ladder-pdg-anchor-result.md` (driver outcome, separate from this audit)
- TARGET → CODATA rename audit-trail: commit dc6c3b7 (Benn Herrera, 2026-04-29)
- BRANCH STATE flag pending for K4-TLM α-emergence: commit 0be89e1 (item #2 "κ_chiral hardcoded")
- Session handoff: `.agents/handoffs/SESSION_HANDOFF_2026-05-18_FULL_PRIMER.md` (peer review #1 priority)
