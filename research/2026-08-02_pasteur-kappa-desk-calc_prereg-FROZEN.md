# Pasteur-κ desk-calc — PRE-REGISTRATION (FROZEN 2026-08-02)

> **Status:** FROZEN. Committed ALONE, before any number exists. Bins, estimators,
> gates, inputs and the commensurability checklist below are frozen at this commit.
> Rule 11: no retuning, no post-hoc bin edits, no dropped criteria.
>
> **Lane:** implementer (derivation lane). **Repo:** AVE-Core.
> **Companion result doc (not yet written):** `research/2026-08-02_pasteur-kappa-desk-calc_result.md`.
> **AVE-HOPF is READ-ONLY for this lane** — geometry is *read* from it, nothing is written there.

---

## §0 SECTOR DECLARATION (before any standard-physics word)

| Question | Answer |
|---|---|
| **Which sector?** | **NONE — this is a CLASSICAL-EM baseline computation.** No AVE sector (A1 dilatation / T2 transverse / Cosserat winding) is engaged. The object computed is a property of a *copper wire on FR-4*, derived from Maxwell's equations only. |
| **Does the engine carry that DOF?** | Not applicable — no engine, no lattice, no solver. Pure analytic + quadrature on an as-fabbed CAD polyline. |
| **Cold vs saturated?** | **COLD / LINEAR / LOSSLESS-REACTIVE.** Small-signal VNA regime; the round-1/round-2 scope fact is $r \sim 10^{-18}$ at the wire-antenna scale (13+ OOM below yield). Nothing here is above the saturation knee. |
| **What role does AVE play?** | AVE supplies **one reference number only** — $\kappa_{AVE,\text{eff}}$, quoted from AVE-HOPF round-2 §2.1 — which this lane compares against. No AVE constant, axiom, operator or kernel enters the classical computation. |

**Consistency-vs-emergence tag (fired at design time, per skill `consistency-vs-emergence`):**
this lane is **CLASSICAL-BASELINE / competitor-construction**. It is *not* an identity test,
*not* an axiom-manifestation test, *not* an emergence test. It makes **no AVE claim** of any
kind. Its only output is a competitor magnitude that a *separate* adjudication (round-2's own
Step-2.5 rule) consumes. The AVE-side reference $\kappa_{AVE,\text{eff}} = \alpha\,pq/(p+q)$ is
itself **CODATA-injected** (round-1 established $\alpha$ enters as a calibration input, not an
emergent output) — so even the AVE number in the comparison is consistency-class, and nothing
in this lane may be headlined as emergence.

---

## §1 WHY THIS LANE EXISTS — the round-2 gap, verbatim

Round-2 retired the two round-1 survivors (**C3** medium-independence, **C4** enantiomer
sign-flip) on **FORM alone**. Its own governing rule routes a form-shared claim to the
**MAGNITUDE** axis:

- `~/.claude/skills/ave-discrimination-check/SKILL.md:155` (Step 2.5, v1.1, 2026-06-01), verbatim:
  > **Shares the FORM** (same functional shape / scaling exponent), **differs in SCALE** (prefactor, orders of magnitude) **→ MAGNITUDE discriminates.**

- `~/.claude/skills/ave-discrimination-check/SKILL.md:166` (the check in one line), verbatim:
  > *before pinning a test's falsifier — does AVE share the FORM with the competitor (→ MAGNITUDE discriminates; a ratio claim is non-discriminating) or the SCALE (→ RATIO/slope discriminates; a magnitude claim carries calibration)?*

Round-2's result doc (AVE-HOPF `main`:`research/2026-06-04_hopf-round2-chiral-counterfactual-result.md`,
commit `d240d70`) establishes form-sharing at §2.2/§2.3 and books
**C3 → FORM-SHARED-RETIRE, C4 → FORM-SHARED-RETIRE** at §5 — but **never computes the classical
magnitude**. The MAGNITUDE leg of its own rule was not run. This lane runs it, at \$0, on the
as-fabbed hardware.

**What a magnitude answer buys.** If the classical competitor's $\kappa$ is far from
$8.76\times10^{-3}$, then a *measured* $8.76\times10^{-3}$ would not be classically
accountable, form-sharing notwithstanding — and the retirement of at least one leg weakens.
If it lands on $8.76\times10^{-3}$, the retirement is final on both axes. If the two $\kappa$'s
turn out not to be the same kind of object, that is itself the finding, and the honest common
observable must be named instead.

---

## §2 THE AVE-SIDE NUMBER — verified at source before use

`verify-before-cite` fired. AVE-HOPF `main`:`research/2026-06-04_hopf-round2-chiral-counterfactual-result.md`
§2.1 (lines 54–56), verbatim:

> HOPF's wire-antenna projection of this is
> $k_{AVE}=k_0(1+\alpha\cdot pq/(p+q))$ (tool-doc:64), i.e. $\kappa_{AVE,\text{eff}} = \alpha\cdot
> pq/(p+q)$ as the per-knot effective chirality.

and §2.1 (lines 40–45), verbatim:

> A reciprocal Pasteur medium (chirality parameter $\kappa$) supports two circularly-polarized
> eigenmodes with split wavenumbers:
> $$ k_\pm = k_0\,(n \pm \kappa), \qquad k_0 = \omega/c. $$
> ...
> $$ \frac{\Delta k}{k} = \frac{k_+ - k_-}{2 k_0 n} = \frac{\kappa}{n}. $$

**Frozen AVE reference value.** For the as-fabbed $(p,q)=(2,3)$ knot,
$\kappa_{AVE,\text{eff}} = \alpha \cdot 6/5 = 1.2\,\alpha$, with $\alpha$ imported from
`src/ave/core/constants.py::ALPHA` (CODATA; the Rule-of-Constants import, never a literal).
Corpus cross-check of the same number at three independent sites:
`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md:201`
($1.2\alpha \approx 8.76\times10^{-3}$),
`manuscript/ave-kb/vol4/future-geometries/ch13-future-geometries/open-universe-boundaries.md:34`,
and AVE-HOPF `docs/glossary.md:149` ($n_{AVE} = \sqrt{\varepsilon_{\rm eff}}\,(1 + \alpha\,pq/(p+q))$).

**⚠ Frozen reading of what $\kappa_{AVE,\text{eff}}$ MEANS in that doc** (this reading is frozen
because the whole comparison turns on it, and §7's checklist tests it):
round-2 §2.1 introduces $\kappa$ as the **bulk constitutive parameter of a Pasteur medium**
(the coefficient in $k_\pm = k_0(n\pm\kappa)$, whose observable is the LCP-vs-RCP wavenumber
split of a wave *propagating through the medium*), then **identifies AVE's** $\alpha\,pq/(p+q)$
**with it** via the wire-antenna projection $k_{AVE}=k_0(1+\alpha pq/(p+q))$ — whose observable
in the HOPF program is the **scalar self-resonance shift** $\Delta f/f$ of the knotted wire, with
the enantiomer pair predicted to shift in opposite directions
($\Delta f_{LR}/f_0 = 2\kappa_{AVE,\text{eff}} = 1.75\times10^{-2}$; AVE-HOPF
`docs/design/2026-05-05_hopf02_nec2_prediction.md:80`). Whether those are the same kind of
object is **not assumed here** — it is exactly what §7 adjudicates.

---

## §3 FROZEN ESTIMATORS

Three estimators are frozen. **K-1 is the PRIMARY** and is the only one that feeds the
magnitude bin. K-2 is the commensurability bridge. K-3 is the density-free reporting form.

### §3.1 K-1 (PRIMARY) — the co-polarizability route to a classical Pasteur $\kappa$

Every step is elementary classical electromagnetism, written out so it is checkable by
derivation rather than by page number.

**Step 1 — the resonant mode.** A thin perfectly-conducting wire follows the as-fabbed
polyline $\mathbf{r}(s)$, $s\in[0,L]$, with unit tangent $\hat{\mathbf t}(s)$. At its
fundamental (half-wave) standing-wave resonance the current is
$$ I(s) = I_0 \sin(\pi s/L), $$
the leading term of the thin-wire (Pocklington/Hallén) resonant solution: zero at both open
ends, single antinode. $I_0$ is the antinode current and is the reference for every quantity below.

**Step 2 — the two dipole moments of that mode.** From $\partial_t \mathbf p = \int \mathbf J\,dV
= \oint I\hat{\mathbf t}\,ds$ and $\mathbf m = \tfrac12\int \mathbf r\times\mathbf J\,dV$:
$$ \boldsymbol\ell_e \;\equiv\; \frac{1}{I_0}\int_0^L I(s)\,\hat{\mathbf t}(s)\,ds
   \quad[\text{m}],\qquad
   \mathbf A_e \;\equiv\; \frac{1}{2 I_0}\int_0^L I(s)\,\big[\mathbf r(s)\times\hat{\mathbf t}(s)\big]\,ds
   \quad[\text{m}^2], $$
so $|\mathbf p| = I_0|\boldsymbol\ell_e|/\omega$ and $\mathbf m = I_0\mathbf A_e$.

**Step 3 — the origin-independent chiral invariant.** Under an origin shift
$\mathbf r\to\mathbf r+\mathbf a$, $\mathbf A_e \to \mathbf A_e + \tfrac12\,\mathbf a\times\boldsymbol\ell_e$,
which is **perpendicular to** $\boldsymbol\ell_e$. Hence the parallel projection is invariant, and
$$ \boxed{\;\chi \;\equiv\; \boldsymbol\ell_e\cdot\mathbf A_e \quad [\text{m}^3]\;} $$
is an **origin-independent pseudoscalar** — the parity-odd invariant of the radiating mode. It is
identically zero for any planar structure (in-plane $\hat{\mathbf t}\Rightarrow$ in-plane
$\boldsymbol\ell_e$, and $\mathbf r\times\hat{\mathbf t}\perp$ plane $\Rightarrow \mathbf A_e\perp
\boldsymbol\ell_e$), and it changes sign under mirroring. $\chi$ IS the classical chirality of the
as-fabbed knot.

**Step 4 — the magnetoelectric (cross) polarizability.** By reciprocity the same
$\boldsymbol\ell_e$ / $\mathbf A_e$ describe reception: an incident field drives an EMF
$V = \mathbf E\cdot\boldsymbol\ell_e + i\omega\mu_0\,\mathbf H\cdot\mathbf A_e$ (the second term
is Faraday's law through the mode's effective area). At resonance the input impedance is real,
$Z_{\rm in}=R$, so $I_0 = V/R$, giving (Tellegen convention
$\mathbf p = \alpha_{ee}\mathbf E + \alpha_{em}\mathbf H$):
$$ \overleftrightarrow{\alpha}_{em} \;=\; -\,\frac{\mu_0}{R}\,\boldsymbol\ell_e\otimes\mathbf A_e ,
\qquad
\alpha_{em}^{\rm(iso)} \;=\; \tfrac13\,{\rm tr}\,\overleftrightarrow{\alpha}_{em}
\;=\; -\,\frac{\mu_0\,\chi}{3R}. $$

**Step 5 — dilute mixing to a bulk Pasteur $\kappa$.** With $\mathbf P = N\mathbf p$,
$\mathbf M = N\mathbf m$ and the Tellegen constitutive pair
$\mathbf D = \varepsilon\mathbf E - i(\kappa/c)\mathbf H$, $\mathbf B = \mu\mathbf H + i(\kappa/c)\mathbf E$,
matching the $\mathbf H$-coefficient gives $-i\kappa/c = N\alpha_{em}$, i.e.
$|\kappa| = c\,N\,|\alpha_{em}^{\rm(iso)}|$. With $c\mu_0 = Z_0$:
$$ \boxed{\;\kappa_{\rm cls} \;=\; \frac{N\,Z_0\,|\chi|}{3\,R_{\rm rad}}\;} $$
(dimensionally: $[\text{m}^{-3}]\cdot[\text{dimensionless}]\cdot[\text{m}^3]$ = dimensionless ✓).

**Step 6 — $R_{\rm rad}$ from the same mode, not from a table.** The far-field of the
polyline current, integrated over the sphere:
$$ P_{\rm rad} = \frac{Z_0 k^2}{32\pi^2}\oint \Big|\int_0^L I(s)\,\hat{\mathbf t}_\perp(s)\,
   e^{\,i\mathbf k\cdot\mathbf r(s)}\,ds\Big|^2 d\Omega ,\qquad R_{\rm rad} = \frac{2P_{\rm rad}}{I_0^2}, $$
with $\hat{\mathbf t}_\perp$ the component of $\hat{\mathbf t}$ transverse to the observation
direction $\hat{\mathbf k}$. Referenced to the SAME $I_0$ as $\boldsymbol\ell_e$, $\mathbf A_e$.

**Step 7 — the frozen reference density.**
$$ N_{\rm ref} \;\equiv\; 1/V_{\rm bbox}, \qquad
   V_{\rm bbox} = \prod_{i\in\{x,y,z\}} \big(\max r_i - \min r_i\big) $$
of the as-fabbed polyline: the **densest non-overlapping packing of as-fabbed copies**, hence
$\kappa_{\rm cls}(N_{\rm ref})$ is the **maximum bulk chirality obtainable from these
meta-atoms** under linear dilute mixing. (Chosen because it is a property of the as-fabbed
geometry alone — no board dimension, no arbitrary cell. Its linear-response validity limit is
disclosed in §6.)

**Frozen bin variable:**
$$ \mathcal{R} \;\equiv\; \kappa_{\rm cls}(N_{\rm ref})\;/\;\kappa_{AVE,\text{eff}}. $$

### §3.2 K-2 (COMMENSURABILITY BRIDGE) — the observable-matched classical $\kappa$

Per `phase-space-coordinate-check` / A46: the estimator must be read in the coordinates the
claim is made in. The HOPF-02a **measurement** is the scalar $S_{11}$ resonance of each board;
the AVE claim in those coordinates is $\Delta f_{LR}/f_0 = 2\kappa_{AVE,\text{eff}}$. So define
$$ \kappa^{\rm(obs)}_{\rm cls} \;\equiv\; \tfrac12\,\big|f_R - f_L\big|\big/f_0
   \quad\text{predicted by classical EM for the as-fabbed enantiomer pair.} $$
**Frozen classical prediction: exactly zero.** Maxwell's equations are parity-covariant, so
the mirror image of a solution is a solution; in a mirror-symmetric environment (achiral FR-4
slab, mirror-symmetric feed) the two enantiomers are exactly degenerate. Two independent corpus
receipts on this exact geometry are to be reported:

- AVE-HOPF `docs/design/2026-05-05_hopf02_design_proposal.md:57`, verbatim:
  > the L↔R mirror is length-preserving (`f_R = f_L` to floating-point precision in NEC2)
- AVE-HOPF `docs/design/2026-05-05_hopf02_nec2_prediction.md:80` — the as-fabbed NEC2 prediction
  table's own **`Δ_classical`** column for $(2,3)$ reads **`+0.000 MHz`**, against
  **`Δ_AVE_pred = −11.91 MHz`** / **`Δ_AVE / f₀ = 1.75%`**. NEC2 is full classical EM run on
  these very polylines: the classical enantiomer split it returns is zero.

This estimator requires **no new simulation**; it is a theorem plus an existing receipt. It is
frozen as the bridge, not as the bin variable.

### §3.3 K-3 (density-free reporting) — the chiral volume and the iso-κ density

$$ V_\chi \;\equiv\; \frac{Z_0\,|\chi|}{3\,R_{\rm rad}}\ [\text{m}^3]
   \quad\Longrightarrow\quad \kappa_{\rm cls} = N\,V_\chi\ \ \forall N ,
\qquad
   N^\star \;\equiv\; \frac{\kappa_{AVE,\text{eff}}}{V_\chi} $$
$N^\star$ is **the number density of as-fabbed knots at which a classical composite reproduces
the AVE number exactly** — the density-free statement of the same comparison, immune to any
argument about the reference cell. Reported always; never binned.

---

## §4 FROZEN BINS (exhaustive, gap-free, all reachable)

Bin (d) is a **classification** outcome and is evaluated FIRST; (a)/(b)/(c) partition
$\mathcal{R}\in(0,\infty)$ with no gaps. If (d) fires, the magnitude bin is still reported (the
number is not withheld) but is explicitly labelled non-adjudicating, and §7's "what WOULD be
commensurable" statement becomes the deliverable.

| Bin | Frozen criterion | Frozen meaning |
|---|---|---|
| **(d) INCOMMENSURABLE** | Any item of the §7 four-point commensurability checklist returns DIFFERENT | The two $\kappa$'s are not the same kind of object; the magnitude comparison does not adjudicate. Deliverable becomes the honest common observable + what would be commensurable. |
| **(a) DISCRIMINATES-HIGH** | `R_bin >= 3` (strong sub-band: `R_bin >= 10`) | Classical $\kappa$ far exceeds AVE's ⇒ a measured $8.76\times10^{-3}$ is NOT what the classical competitor predicts ⇒ the MAGNITUDE axis discriminates ⇒ round-2's form-only retirement weakens; a leg returns to the table. |
| **(b) RETIREMENT-FINAL** | `1/3 < R_bin < 3` | Classical reproduces FORM *and* MAGNITUDE ⇒ round-2's retirement is final on both axes; nothing returns. |
| **(c) DISCRIMINATES-LOW** | `R_bin <= 1/3` (strong sub-band: `R_bin <= 0.1`) | Classical $\kappa$ far below AVE's ⇒ anomalous the other way; the magnitude axis discriminates but in the direction that makes the AVE number the LARGE one. **Flag for Grant walk** — do not book a verdict from this lane. |

**Mutual-satisfiability check (standing DESIGN LESSON 3), run BEFORE freeze:**

1. **(a)/(b)/(c) are exhaustive and mutually exclusive** on $\mathcal{R}\in(0,\infty)$:
   $[3,\infty)\cup(1/3,3)\cup(0,1/3]$ partitions the line with no gap and no overlap. The task
   brief's "$\gtrsim 10\times$" and "$\ll$" are preserved as named STRONG sub-bands, not as bin
   edges — the edges are the brief's own "within $\sim3\times$" for (b), extended outward, which
   is the only gap-free reading of the brief's three bands.
2. **No bin is excluded by construction.** $\kappa_{\rm cls} = N_{\rm ref}Z_0|\chi|/(3R_{\rm rad})$
   is a single positive number with no free parameter; the geometry admits any of the three.
   Concretely: the as-fabbed knot is *strongly* subwavelength laterally (bbox $34.6\times38.7$ mm
   against $\lambda\approx441$ mm) but *weakly* out-of-plane ($2.6$ mm), so $\chi$ could plausibly
   land anywhere from tiny (near-planar ⇒ (c)) to large (close-packing ⇒ (a)); nothing in the
   setup forces a band.
3. **No frozen requirement contradicts another.** The three estimators are computed from ONE
   frozen mode ($I(s)=I_0\sin(\pi s/L)$) on ONE frozen geometry at ONE frozen $f_0$; K-2 is a
   parity theorem requiring no numerics; K-3 is an algebraic re-expression of K-1. There is no
   pair of requirements that cannot be simultaneously satisfied.
4. **Bin (d) does not silently swallow (a)/(b)/(c).** Its trigger is the §7 checklist, which is
   a set of four YES/NO structural questions decided by reading definitions, not by the computed
   number. It is therefore decidable *before* $\mathcal{R}$ is known, and cannot be used to escape
   an unwelcome magnitude.

---

## §5 FROZEN GATES (each demonstrably fireable, known-positive and known-negative)

Frozen: `every gate below must PASS before any bin verdict is booked`. A failed gate voids the
verdict; it does not get relaxed.

| # | Gate | Frozen criterion | Class |
|---|---|---|---|
| **G1** | Origin-invariance of $\chi$ | `|chi(shifted) - chi(0)| / |chi(0)| <= 1e-9` under 8 random origin shifts of magnitude ~1 m | self-consistency (the pseudoscalar theorem) |
| **G2** | Mirror antisymmetry | `|chi_L + chi_R| / |chi_R| <= 1e-9` between the as-fabbed `k23_L` and `k23_R` polylines | known-positive (the classical enantiomer sign-flip, computed) |
| **G3** | Planar null | `|chi_control| / |chi_k23R| <= 1e-9` on the as-fabbed control wire (all points share one x ⇒ planar ⇒ achiral) | **known-negative** |
| **G4** | Analytic helix known-positive | a synthetic 1-turn helix (radius $a$, pitch $h$, uniform current) reproduces the closed form $\chi = \pi a^2 h$ to `<= 1e-6` relative | **known-positive with an exact target** |
| **G5** | Radiation-integral validation | a straight half-wave dipole returns `R_rad within 2 percent of 73.13 ohm` and `|ell_e| within 1 percent of lambda/pi` | known-positive (textbook value the code must reproduce) |
| **G6** | Subwavelength admissibility | `bbox diagonal / lambda <= 0.25` (the dipole/meta-atom truncation is admissible) | scope gate — failure routes to bin (d), it does not get waived |
| **G7** | Reciprocity self-check | $\overleftrightarrow{\alpha}_{em} = -\mu_0\overleftrightarrow{\alpha}_{me}^{T}$ holds identically in the implementation (checked symbolically in the driver's assertions) | structural |

G4's closed form is derived here so it is a real target and not a fit: for a single helical turn
of radius $a$ and pitch $h$ carrying uniform current, $\boldsymbol\ell_e = h\hat z$ (the loop's
transverse contributions cancel) and $\mathbf A_e = \pi a^2\hat z + O(h)$, so
$\chi = \pi a^2 h$ — the classic "canonical helix" chirality, equal to the volume of the
cylinder the turn encloses.

---

## §6 FROZEN INPUTS, EACH TAGGED — and the idealizations, each BOUNDED

### §6.1 Inputs

| Input | Value | Tag | Source |
|---|---|---|---|
| Knot polyline (2,3) R | `data/hopf_02/k23_R_wire.csv`, 40 points, arc length `230.560` mm, bbox `34.581583 x 38.688032 x 2.6` mm | **engineering as-fabbed** | AVE-HOPF `main` (READ-ONLY); vendored into `research/drivers/data/` with sha256 + source commit |
| Knot polyline (2,3) L | `data/hopf_02/k23_L_wire.csv`, same arc length/bbox | **engineering as-fabbed** | idem |
| Control polyline | `data/hopf_02/control_wire.csv`, 18 points, arc length `177.471` mm, x-extent `0` (planar) | **engineering as-fabbed** | idem |
| Wire | 24 AWG enamelled magnet wire | **engineering as-fabbed** | AVE-HOPF `hardware/hopf_02_ASSEMBLY_GUIDE.md` BOM |
| Substrate | 2-layer FR-4, 1.6 mm, ENIG | **engineering as-fabbed** | idem |
| $f_0$ | `680` MHz | **engineering as-fabbed (NEC2 prediction on this exact geometry)** | AVE-HOPF `docs/design/2026-05-05_hopf02_nec2_prediction.md:65` |
| $Z_0$, $c$, $\mu_0$ | `src/ave/core/constants.py::Z_0, C_0, MU_0` | **CODATA-SI, classical** | Rule-of-Constants import; no literals |
| $\alpha$ | `src/ave/core/constants.py::ALPHA` | **CODATA — AVE SIDE ONLY** | enters *only* $\kappa_{AVE,\text{eff}} = 1.2\alpha$; appears nowhere in the classical chain |

**No external experimental value is used and none may be invented.** If any step turns out to
need a measured chiral-medium $\kappa$, a measured $Q$, or a published metamaterial value, it is
tagged `[requires-external-retrieval]` and the step is reported unexecuted.

### §6.2 Idealizations, and how each is bounded (frozen sensitivity legs)

| # | Idealization | Bounding leg (frozen — must be reported whatever it shows) |
|---|---|---|
| **I-1** | Current profile $I_0\sin(\pi s/L)$ | Sweep the family $I_0\sin(\pi s/L)^\gamma$, $\gamma\in\{0.8,1.0,1.2\}$, plus a uniform-current variant; report the full spread of $\kappa_{\rm cls}$ |
| **I-2** | Free space (no FR-4 slab, no ground plane, no coax counterpoise) | Recompute at $\lambda_{\rm eff}=\lambda/\sqrt{\varepsilon_{\rm eff}}$ for $\varepsilon_{\rm eff}\in\{1.0,1.5,2.0\}$ (wire sits ~1 mm above a 1.6 mm FR-4 slab, so the mode is air-dominated); report the spread |
| **I-3** | Electric+magnetic dipole truncation (no quadrupole) | Gate G6 bounds the expansion parameter; report bbox-diagonal/$\lambda$ explicitly |
| **I-4** | Lossless copper: $R = R_{\rm rad}$ | Copper loss only *increases* $R$, which only *decreases* $\kappa_{\rm cls}$ — so $R=R_{\rm rad}$ is a strict **upper bound** on the classical $\kappa$. Direction of the bound is stated in the result. |
| **I-5** | Dilute mixing at close packing (no local-field / no inter-inclusion coupling) | The weakest assumption. Disclosed as such; K-3's $V_\chi$ and $N^\star$ are the density-free escape and are reported alongside. Additionally report the value of $\kappa_{\rm cls}$ at which linear mixing is conventionally taken to fail (`0.1`) and the density that corresponds to. |

**No NEC2 in the frozen chain.** PyNEC / necpp are not installed in this repo's environment
(verified at design time), and K-2 needs no simulation (it is a parity theorem plus an existing
AVE-HOPF receipt). The classical chain is therefore **analytic + quadrature only**, hermetic,
stdlib+numpy, no network, no RNG beyond G1's seeded origin shifts. This is a deliberate
simplification relative to the brief's NEC2 option; the cost is bounded by I-1…I-5 and by G5
(which forces the radiation code to reproduce the textbook half-wave dipole before it is trusted).

---

## §7 THE COMMENSURABILITY CHECKLIST (frozen; decided by definitions, not by the number)

Four YES/NO questions. **All four SAME ⇒ commensurable ⇒ bins (a)/(b)/(c) adjudicate.
Any DIFFERENT ⇒ bin (d) fires.**

| # | Question | $\kappa_{\rm cls}$ (K-1) | $\kappa_{AVE,\text{eff}}$ | Verdict |
|---|---|---|---|---|
| **C-i** | Physical dimension | dimensionless | dimensionless | *(to be filled)* |
| **C-ii** | Defining equation | coefficient in $k_\pm = k_0(n\pm\kappa)$ | *(to be read from round-2 §2.1)* | *(to be filled)* |
| **C-iii** | Object class | bulk effective-medium constitutive parameter of a composite (scales with $N$) / single-inclusion property / self-resonance fractional shift | *(to be read)* | *(to be filled)* |
| **C-iv** | Observable consequence | *(to be read from the defining equation)* | *(to be read)* | *(to be filled)* |

**Frozen obligation if (d) fires:** the result doc must state, constructively, **what WOULD be
commensurable** — i.e. name (1) the observable both sides predict in the same coordinates, (2)
the classical value of that observable, (3) the AVE value, and (4) the experiment that reads it.
"Incommensurable, therefore nothing can be said" is **not** an admissible closure.

---

## §8 DELIVERABLES + ACCEPTANCE (frozen)

1. This prereg, committed **alone** and pushed before any number exists.
2. `research/drivers/pasteur_kappa_desk_calc.py` — hermetic driver; ships
   `pasteur_kappa_desk_calc_results.json`.
3. `research/drivers/pasteur_kappa_desk_calc_number_check.py` — every inline-code numeral in the
   result doc + docket fragment must resolve to a NAMED JSON leaf or an allow-listed constant
   with a reason (the #801/#802 pattern), wired into `make verify-lane-number-checks`.
4. `research/2026-08-02_pasteur-kappa-desk-calc_result.md` — carries `Prereg-file:` +
   `Prereg-commit:` pointers and byte-identical `Frozen:` labels.
5. `_orchestration/docket-entries/2026-08-02-pasteur-kappa-calc.md`.
6. Acceptance: `make verify` exit 0; refresh idempotent; docket lint; pure-corpus;
   **AVE-HOPF byte-untouched** (asserted by `git -C AVE-HOPF status --porcelain` being empty of
   this lane's paths).

**Rule 11 restated for this lane:** the bins above exist before the number does. If the number
lands in (c) — the awkward band — it is reported as (c) and walked with Grant. It is not
re-binned, and no criterion is dropped to convert it.
