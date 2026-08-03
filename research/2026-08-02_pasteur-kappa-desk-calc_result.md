# Pasteur-κ desk-calc — RESULT (2026-08-02)

> **Prereg-file**: `research/2026-08-02_pasteur-kappa-desk-calc_prereg-FROZEN.md`
> **Prereg-commit**: `3ae1f3de`
> **Driver:** `research/drivers/pasteur_kappa_desk_calc.py` →
> `research/drivers/pasteur_kappa_desk_calc_results.json`
> **Number-check:** `research/drivers/pasteur_kappa_desk_calc_number_check.py`
> (wired into `make verify-lane-number-checks`)
> **Lane:** implementer / derivation. **AVE-HOPF: READ-ONLY — byte-untouched.**
>
> **Class (consistency-vs-emergence, fired at design time):** **CLASSICAL-BASELINE.**
> This document computes a property of a copper wire on FR-4 from Maxwell's equations.
> It makes **no AVE claim** — not identity, not manifestation, not consistency, not emergence.
> Its only AVE-side input is one reference number, itself CODATA-injected.

---

## §1 One-paragraph result

The classical chirality of the as-fabbed HOPF-02a (2,3) knot is **large**, and it is **not the
same kind of object** as $\kappa_{AVE,\text{eff}}$. Computed from the frozen chain, the knot's
origin-independent chiral invariant is $\chi = -5.951479\times10^{-7}$ m³ with radiation
resistance $R_{\rm rad} = 0.7385$ Ω, giving a **chiral volume** $V_\chi = 1.012047\times10^{-4}$
m³ (≈ 101 cm³). A dilute classical composite of these very knots therefore reaches
$\kappa = 8.756823\times10^{-3}$ — the AVE number — at a density of **one knot per 11.6 litres**
($N^\star = 86.5258$ m⁻³), which is **11.4× more dilute than the conventional linear-mixing
validity ceiling**, i.e. comfortably inside the regime where the formula that produced it is
valid. At the frozen reference density (close-packed as-fabbed bounding boxes) the same formula
returns $\kappa_{\rm cls} = 29.09$, a factor $\mathcal{R} = 3322$ above the AVE number — the
frozen magnitude bin is **(a) DISCRIMINATES-HIGH**, stable across every frozen sensitivity leg
(ratio 964–6481). **But the frozen commensurability checklist fires bin (d):** three of its four
items return DIFFERENT. $\kappa_{\rm cls}$ is a **bulk constitutive parameter proportional to an
inclusion density**, whose observable is the LCP-vs-RCP split of a wave *transmitted through a
medium*; $\kappa_{AVE,\text{eff}}$ is a **density-free per-topology number** whose observable is
a **scalar shift of one structure's own 1-port resonance**, sign-keyed to the *structure's*
handedness rather than the *wave's*. **So the magnitude comparison does not adjudicate**, and the
prereg's §7 obligation takes over: the honest common observable is the **enantiomer split of the
scalar self-resonance**, for which classical EM predicts **exactly zero** (parity-covariance;
the as-fabbed L↔R map is a pure reflection $x\to-x$ with zero translation, computed here at
`0.0` mm residual; and AVE-HOPF's own NEC2 table reads `+0.000 MHz`) against AVE's
$2\kappa_{AVE,\text{eff}} = 1.751365\times10^{-2}$ = `11.9093` MHz — **a presence/absence
divergence, not a magnitude one.** That result stands in tension with round-2 §2.3, which reads
the classical enantiomer sign-flip and the HOPF $\Delta f$ sign-flip as "term for term" the same;
**both sides are recorded verbatim in §6 and neither is reframed.**

---

## §2 What was computed, and the chain that produced it

Every step is the frozen prereg §3.1 chain, in order. Nothing below is fitted; the only inputs
are the as-fabbed polyline, the as-fabbed resonance, and CODATA SI constants.

| Step | Quantity | Value | Where it comes from |
|---|---|---|---|
| geometry | arc length | `230.560` mm | as-fabbed CSV, sha256-gated |
| geometry | bounding box | `34.581583` × `38.688032` × `2.6` mm | as-fabbed CSV |
| 0 | $\lambda$ at $f_0 = $ `680` MHz | `0.44087126176470587` m | $c/f_0$, `ave.core.constants.C_0` |
| 2 | $\boldsymbol\ell_e$ | `6.8949e-3` m (vector `[-6.7696e-3, -1.0742e-3, -7.4729e-4]`) | $\frac1{I_0}\!\int\! I\hat{\mathbf t}\,ds$ |
| 2 | $\mathbf A_e$ | `8.8679e-4` m² (vector `[-1.0511e-5, 3.4085e-6, 8.8672e-4]`) | $\frac1{2I_0}\!\int\! I(\mathbf r\times\hat{\mathbf t})\,ds$ |
| 3 | $\cos\angle(\boldsymbol\ell_e,\mathbf A_e)$ | `-0.0973` | the knot is only ~10 % "aligned-chiral" — its 2.6 mm out-of-plane excursion tilts an otherwise in-plane $\boldsymbol\ell_e$ against an otherwise normal $\mathbf A_e$ |
| 3 | $\chi = \boldsymbol\ell_e\cdot\mathbf A_e$ | `-5.951479e-07` m³ | origin-independent pseudoscalar (G1) |
| 6 | $R_{\rm rad}$ | `0.7385` Ω | far-field radiation integral of the SAME mode |
| 5 | $V_\chi = Z_0|\chi|/(3R_{\rm rad})$ | `1.012047e-04` m³ | $\kappa_{\rm cls} = N V_\chi$ for any $N$ |
| 7 | $N_{\rm ref} = 1/V_{\rm bbox}$ | `2.874784e+05` m⁻³ | close-packed as-fabbed bounding boxes |
| — | $\kappa_{\rm cls}(N_{\rm ref})$ | `29.09` | K-1 PRIMARY |
| — | $\kappa_{AVE,\text{eff}} = 1.2\alpha$ | `8.756823e-03` | AVE side only; `ave.core.constants.ALPHA` |
| — | $\mathcal{R} = \kappa_{\rm cls}/\kappa_{AVE,\text{eff}}$ | `3322.457263790723` | frozen bin variable |

**Physical read of $R_{\rm rad} = 0.7385\ \Omega$.** A 231 mm wire at 680 MHz is a half-wave
radiator *if it is straight* (73 Ω). Coiled into the (2,3) knot, the vector sum
$\boldsymbol\ell_e$ collapses from $\lambda/\pi = $ `0.1403` m to `6.8949e-3` m — a factor `20.35` —
and $R_{\rm rad}\propto\ell_e^2$ drops with its square. The knot is a *bad radiator and a good
inductor*: that is why $Z_0/3R_{\rm rad} = $ `170.05` is large, and it is the whole reason the
chiral volume comes out at the scale of a coffee cup rather than the scale of the wire.

---

## §3 K-3 — the density-free statement (the load-bearing number)

$\kappa_{\rm cls}$ is proportional to $N$. Quoting it at any single density invites an argument
about the cell. The density-free form does not:

| Quantity | Value | Reading |
|---|---|---|
| $V_\chi$ | `1.012047e-04` m³ | the knot's chiral volume; $\kappa_{\rm cls}=N V_\chi$ |
| $N^\star = \kappa_{AVE,\text{eff}}/V_\chi$ | `86.5258233657606` m⁻³ | **one knot per `0.011557243388171132` m³ ≈ 11.6 litres** reproduces the AVE number classically |
| $N$ at the linear-mixing ceiling $\kappa=$ `0.1` | `988.0960542888662` m⁻³ | one knot per `0.0010120473567923527` m³ ≈ 1.0 litre |
| $N_{\rm ref}/N^\star$ | `3322.4572637907227` | close packing is 3.3×10³ times denser than the iso-κ density |

**★ The one line that matters here.** $N^\star$ (`86.5258` m⁻³) is **`11.4197`× more dilute** than
the density at which linear mixing conventionally stops being trustworthy (`988.0961` m⁻³).
So the statement *"a classical composite of these as-fabbed copper knots has
$\kappa = 8.76\times10^{-3}$ at one knot per 11.6 litres"* is made **inside** the validity
domain of the formula that makes it. By contrast $\kappa_{\rm cls}(N_{\rm ref}) = $ `29.09`
sits `290.942`× **outside** it — so the frozen K-1 value is a **formal linear-response extrapolation,
not a physical prediction for a close-packed array**, and it is reported as such. The frozen bin
is computed on it because the prereg froze it that way (Rule 11); the *physics* is carried by
$N^\star$, and both point the same direction.

---

## §4 Gates — all seven PASS, including one that fired

Frozen: `every gate below must PASS before any bin verdict is booked`.

| Gate | Frozen criterion | Measured | Verdict |
|---|---|---|---|
| **G1** origin-invariance | Frozen: `|chi(shifted) - chi(0)| / |chi(0)| <= 1e-9` | worst `4.513421561571926e-13` over 8 seeded shifts | **PASS** |
| **G2** mirror antisymmetry | Frozen: `|chi_L + chi_R| / |chi_R| <= 1e-9` | `0.0` (exact) | **PASS** |
| **G3** planar null (**known-negative**) | Frozen: `|chi_control| / |chi_k23R| <= 1e-9` | `0.0` (exact — the control's points share one $x$) | **PASS** |
| **G4** analytic helix (**known-positive, exact target**) | prereg §5: reproduces the closed form $\chi=\pi a^2h$ to Frozen: `<= 1e-6` relative | `1.5707963009561105e-07` vs `1.5707963267948966e-07`, rel `1.6449e-08` | **PASS** |
| **G5** radiation integral (**known-positive**) | Frozen: `R_rad within 2 percent of 73.13 ohm` + Frozen: `|ell_e| within 1 percent of lambda/pi` | `73.07904449143211` Ω (rel `6.9678e-04`); $\ell_e$ rel `2.8558e-07` | **PASS** |
| **G6** subwavelength admissibility | Frozen: `bbox diagonal / lambda <= 0.25` | `0.11784810733938897` | **PASS** |
| **G7** reciprocity | prereg §5 G7 (stated there unquoted): $\overleftrightarrow{\alpha}_{em}=-\mu_0\overleftrightarrow{\alpha}_{me}^{T}$ holds identically | rel residual `1.977e-17` | **PASS** |

**★ G7 FIRED on the first run — and here is exactly how much that is worth.** *(Rule 12
quote-and-correct, 2026-08-02. The `f9d5c86c` text read: "The bug was in the cross-polarizability
— precisely the quantity the whole lane exists to compute. A gate that has never fired is a
checklist; this one is a gate." That overstated it, and the audit was right to say so.)*

The initial implementation built $\overleftrightarrow{\alpha}_{me}$ with a flipped sign
($\mathbf A_e\otimes\boldsymbol\ell_e/(-R)$ instead of $/R$), and G7 returned a residual of order
the dyad itself. But the defect lived in **the gate's own reconstruction** of
$\overleftrightarrow{\alpha}_{me}$ (driver `run_gates`, the G7 block), and **no reported number in
this lane consumes a signed $\overleftrightarrow{\alpha}_{em}$**: the production chain routes
through `chiral_volume()`, which takes $|\chi|$. **So the reported chain is sign-free and the
defect could not have propagated.** G7 caught a real bug in real code; it did not catch a bug that
was on its way into a shipped number.

**The numerically load-bearing known-positives are G4 and G5**, because they are the two that
compare a computed quantity against an *independent* target: G4 the helix against the exact closed
form $\chi=\pi a^2h$ (rel `1.6449e-08`), G5 the straight dipole against the textbook `73.13` Ω
(computed `73.079`, rel `6.9678e-04`). Those are what stand behind the numbers this document
quotes.

**Repair, disclosed and KEEP-BOTH (post-audit, NOT FROZEN).** Because F3's point is fair, the
driver now also routes $V_\chi$ through **both signed dyads** —
$-c\,\mathrm{tr}(\overleftrightarrow{\alpha}_{em})/3 = +\mu_0
c\,\mathrm{tr}(\overleftrightarrow{\alpha}_{me})/3 = Z_0\chi/(3R_{\rm rad}) =
\mathrm{sign}(\chi)\,V_\chi$ — so a sign flip in *either* dyad now shows up in a reported quantity.
Agreement `0.0` and `1.3391198608554297e-16` relative
(`post_audit_supplementary_NOT_FROZEN.S1_dyad_consumption`). The seven frozen gates are
byte-unchanged and this block is excluded from `ALL_PASS` by construction. (The
second bug the lane caught was not physics: the far-field integral originally materialised the
full direction×element phase matrix and spent six minutes in swap. Chunked; arithmetic unchanged;
`quadrature_convergence` shows `chi` and `R_rad` drifting at most `1.04355e-06` and `2.57188e-06` across a 4x mesh change.)

---

## §5 THE VERDICT — bin (d) fires; the magnitude bin is (a) and is non-adjudicating

### §5.1 The commensurability checklist (frozen §7, decided by definitions)

| # | Question | $\kappa_{\rm cls}$ (K-1) | $\kappa_{AVE,\text{eff}}$ | Verdict |
|---|---|---|---|---|
| **C-i** | physical dimension | dimensionless | dimensionless | **SAME** |
| **C-ii** | defining equation, and what the sign keys to | coefficient in $k_\pm=k_0(n\pm\kappa)$; the $\pm$ is keyed to the **wave's** circular-polarisation handedness | coefficient in $k_{AVE}=k_0(1+\alpha\,pq/(p+q))$ — a single shifted wavenumber, **no $\pm$ pair**; the sign is keyed to the **structure's** handedness (round-2 §2.3: $\Delta f_R=-\Delta f_L$) | **DIFFERENT** |
| **C-iii** | object class | bulk effective-medium constitutive parameter, strictly **∝ N**; not a property of one object | a fixed number per knot **topology**, no density in it; a fractional shift of **one** structure's own eigenfrequency | **DIFFERENT** |
| **C-iv** | observable consequence | optical rotation / circular birefringence of a wave **transmitted through** the composite, $\Delta k/k=\kappa/n$ between LCP and RCP | $\Delta f/f$ of the knot's **own** 1-port $S_{11}$ resonance, enantiomers shifting oppositely | **DIFFERENT** |

3 of 4 DIFFERENT ⇒ **bin (d) INCOMMENSURABLE fires.**

**The one-sentence diagnosis.** A Pasteur $\kappa$ tells you how much *a medium* rotates *a
wave's* polarisation, and you can dial it anywhere from 0 to O(1) by choosing how many knots per
litre you stir in; $\kappa_{AVE,\text{eff}}$ is a fixed dimensionless number attached to *one
knot's topology* that shifts *that knot's own* resonance. **A knob and a constant are not the
same kind of object**, and comparing their numerical values does not adjudicate anything.

### §5.2 The magnitude bin, reported and labelled

| | |
|---|---|
| Frozen bin variable $\mathcal{R}$ | `3322.457263790723` |
| Frozen bin | **(a) DISCRIMINATES-HIGH**, strong sub-band ($\mathcal{R}\ge$ `10`) |
| Across the frozen sensitivity legs | $\mathcal{R}\in[$`963.6431295970821`, `6481.485872877981`$]$ — bin **stable** |
| Status | **REPORTED BUT NON-ADJUDICATING** (bin (d) fired; prereg §4) |

Sensitivity spread (frozen legs I-1, I-2): $\kappa_{\rm cls}\in[$`8.438452401184271`,
`56.75722510479334`$]$, spread factor `6.726023020148565`. The current-profile leg spans `27.229641103511227` (γ=1.2) to `31.784754192972528` (γ=0.8),
with the unphysical uniform-current variant at `56.75722510479334`; the host-index leg falls to
`8.438452401184271` at $\varepsilon_{\rm eff}=$ `2.0` (a denser host shortens $\lambda$, which
raises $R_{\rm rad}$). Nothing in that envelope reaches bin (b).

**Direction-conservative additions, NOT FROZEN, disclosed:** including copper skin-effect loss
($R_{\rm ohm} = $ `0.4826838832906189` Ω at skin depth `2.501614100400152e-06` m against
$R_{\rm rad}=$ `0.7385` Ω) multiplies every $\kappa_{\rm cls}$ by
`0.6047315980017243`. That **shrinks** the classical number and still leaves $\mathcal{R}\sim2\times10^3$.
It cannot move the verdict toward the bin this lane reports.

---

## §6 THE §7 OBLIGATION — what IS commensurable, and the contradiction it exposes

Bin (d) fired, so the prereg's frozen obligation applies: *"the result doc must state,
constructively, what WOULD be commensurable … 'Incommensurable, therefore nothing can be said'
is not an admissible closure."*

### §6.1 The honest common observable

| | |
|---|---|
| **(1) The observable both sides predict in the same coordinates** | the **enantiomer split of the scalar self-resonance**, $(f_R-f_L)/f_0$, on the as-fabbed HOPF-02a pair in an **achiral host** (air + FR-4) — the quantity a 1-port $S_{11}$ differential actually reads |
| **(2) Classical value** | **exactly `0`** |
| **(3) AVE value** | `1.751365e-02` fractional = **`11.9093` MHz** at `680` MHz |
| **(4) The experiment that reads it** | the HOPF-02a enantiomer pair, differential $S_{11}$ — **designed to fab-artifact completeness (Gerbers + drill + DRC + BOM + ORDERING exported); NOT FABBED.** The physical fab order is AVE-HOPF **Phase 0b, gated on Grant, ~\$`123` BOM + build**. Round-2 §4 inherits the S-8 **FABRICATION** floor ≈ `130` kHz = `1.911765e-04` fractional at `680` MHz ⇒ margin `91.6098`× — see the floor-class note below |

**★ Floor-class note — what the `91.6098`× is a margin over, and what it is not.** *(Rule 12
quote-and-correct, 2026-08-02. The `f9d5c86c` text quoted "margin `91.6098`×" against "the S-8 fab
floor" without saying which CLASS of floor that is; the audit's F4 is that the qualifier is
load-bearing.)*

The `91.6098`× is against the **S-8 FABRICATION floor** — AVE-HOPF
`docs/analysis/2026-06-03_hopf_antenna_hardened_prereg.md:264`, an L↔R fab/assembly asymmetry
drawn from a `5000`-trial Monte Carlo over hole, mandrel, wire-bend and operator. That **is** the
correct floor *class* for an enantiomer differential: what an L-vs-R comparison is exposed to is
precisely an L-vs-R build asymmetry. But it is not the whole floor. A *measured* differential also
carries a **MEASUREMENT** floor $\sigma_{\rm repeat}\sqrt{2/N}$, and $\sigma_{\rm repeat}$ **has
never been measured on this hardware** — it is routed at **AVE-HOPF PR #`3`** (branch
`bench/sigma-repeat-and-sweep-spec`, unmerged), whose `docs/open_questions.md:116` puts the
ceiling S-1's own $N\ge$ `10` implies at $\sigma_{\rm repeat}\le$ `0.29` MHz.

At that worst admitted value the combined floor is
$\sqrt{(`130`\,\text{kHz})^2 + (`290`\,\text{kHz}\sqrt{2/`10`})^2} = $ `183.630` kHz
(measurement term alone `129.692` kHz), giving margin **`64.855`×**
(`post_audit_supplementary_NOT_FROZEN.S3_combined_floor_scope`). **The EXISTENCE claim is robust
under both floors** — `0` versus `11.9093` MHz clears either by ~two orders of magnitude. Only
the margin *figure* moves, `91.6098`× → `64.855`×, and both are quoted here rather than one
being silently swapped for the other.

**Why the classical value is exactly zero, and what that is conditional on.** Maxwell's equations
are parity-covariant: the mirror image of a solution is a solution, so in a **mirror-symmetric
fixture** the two enantiomers are exactly degenerate. This lane makes that premise *checkable
rather than assumed*: the as-fabbed L↔R map was extracted from the CSVs and is a **pure
reflection $x\to-x$ with zero translation**, max residual `0.0` mm (the two competing coordinate
mirrors miss by `47.1397` mm and `40.1328` mm). The control wire lies exactly in that mirror
plane. Three independent corpus receipts say the wire-level statement holds under a full
classical solver:

- AVE-HOPF `docs/design/2026-05-05_hopf02_design_proposal.md:57`, verbatim:
  > the L↔R mirror is length-preserving (`f_R = f_L` to floating-point precision in NEC2)
- AVE-HOPF `docs/design/2026-05-05_hopf02_nec2_prediction.md:72`, verbatim:
  > **R and L give bit-identical NEC2 output for every antenna pair.** This confirms the L↔R
  > wire-CSV mirror exactness propagates through MoM into bit-identical impedance predictions —
  > Maxwell is parity-invariant and our wires are parity-symmetric inputs.
- AVE-HOPF `docs/design/2026-05-05_hopf02_nec2_prediction.md:80` — the NEC2 prediction table's
  own `Δ_classical` column for $(2,3)$ reads **`+0.000 MHz`**, against
  `Δ_AVE_pred` = **`−11.91 MHz`** and `Δ_AVE / f₀` = **`1.75%`**.

**★ The fixture-symmetry premise, DISCHARGED for the released fab artifacts.**
*(2026-08-02 audit-lane check against AVE-HOPF `main`:`hardware/Gerbers_hopf_02a/`. Rule 12
quote-and-correct: the version of this document committed at `f9d5c86c` read, verbatim, "**The
residual obligation, stated and not discharged here:** the rest of the fixture — board outline,
feed position, hole pattern, connector — must also be symmetric about $x=0$ for the theorem to
bind at the bench." That obligation is now discharged for all four named items; what replaces it
is a shorter and different list.)*

| Fab artifact | What was checked | Result |
|---|---|---|
| `Edge_Cuts.gm1` | panel outline + internal v-score lines | `250` × `185` mm panel, v-scores at $x=$ `50` / `100` / `150` / `200` mm — five equal `50` mm coupon lanes, so **each enantiomer pair straddles a v-score, and the board outline is symmetric about it** |
| `PTH.drl` | all `45` plated holes, per tool diameter | coupon0↔coupon1 about $x=$ `50`: max mirror residual **`0.000` mm**; coupon2↔coupon3 about $x=$ `150`: **`0.000` mm** |
| `NPTH.drl` | all `94` unplated (wire-form) holes | **`0.001` mm** both pairs — the file's own 3-decimal-place quantization, not an asymmetry |
| `F_Cu.gtl` / `B_Cu.gbl` | all `45` copper flashes per layer | **exact set match** under $x\to-x$ about each pair's v-score, on **both** layers, including the `6` mm SMA-ground aperture |
| feed position | SMA centre-pin flash | `7.709` mm either side of the $x=$ `50` mirror line for the (2,3) pair (`8.436` mm about $x=$ `150` for (2,5)) — **the feed is mirror-placed, not merely present on both** |
| control coupon4 | self-mirror about its own centre | **`0.000` mm** — the control is its own mirror image, as its role requires |

So *board outline*, *hole pattern*, *feed position* and *connector ground* — all four items the
prior text left open — are symmetric in the released artifacts, at the artifact's own numerical
resolution.

**The two residuals that survive that check — and they are not the ones the prior text named.**

1. **FR-4 glass-weave off-diagonal permittivity.** A woven laminate is a *parity-even* dielectric
   only if its weave axes are aligned with the board axes. If the panel is cut at an angle to the
   weave, $\varepsilon$ acquires an off-diagonal $\varepsilon_{xy}$, the host stops being
   $x\to-x$-invariant, and the two enantiomers see *different* dielectric environments. This is a
   **systematic**, not a random fab tolerance: it is **not** in the S-8 geometry-only Monte Carlo
   (AVE-HOPF `docs/analysis/2026-06-03_hopf_antenna_hardened_prereg.md:264`, whose `5000`-trial
   draw is over hole, mandrel, wire-bend and operator — all *mechanical*). Order of magnitude: take
   the weave anisotropy at the few-percent level of the split — `6` % of `11.9093` MHz is `0.7`
   MHz — which is small against the signal but roughly `5`× **above** the `130` kHz S-8 floor. It
   is the one channel that can put a nonzero classical number on this observable in an achiral
   *bulk* host.
2. **The singulation precondition.** The mirror premise is a statement about **singulated**
   coupons. Measured at panel level, each coupon's neighbours are *not* its mirror image (coupon1's
   left neighbour is coupon0, its right neighbour is coupon2), so neighbour-coupling breaks the
   symmetry that the v-score-local check establishes. **Break the panel before measuring**, or the
   theorem does not bind.

**The cheap kill for residual 1.** The panel carries a **second, independent** enantiomer pair:
$(p,q)=(2,5)$ on coupons 2/3, mirrored about $x=$ `150`. A weave systematic is **common-mode**
across the two pairs (same laminate, same weave angle, same panel), whereas the AVE prediction
scales as $pq/(p+q)$ — `1.2` for (2,3) against `1.429` for (2,5) in AVE-HOPF's own
`nec2_prediction.md:81` row. So the two pairs discriminate a weave artifact from the predicted
effect without any new hardware. *(Honest caveat, from AVE-HOPF's own text: `nec2_prediction.md:74`
warns the (2,5) dip near `380` MHz "are likely both dominated by the cable counterpoise's
resonance", so the (2,5) leg needs its mode identified before it can carry weight.)*

**What class of zero this is — and why it is stronger than the last time this corpus wrote
"exactly 0".** The classical `0` here is protected by a **symmetry theorem** (parity covariance of
Maxwell, with the mirror operation itself computed rather than assumed), not by absence of
imagination. That distinction is load-bearing, because this corpus has already been burned by the
other kind: round-1's Cleave-01 asserted an exact classical zero and it was **false**. AVE-Core
`research/2026-06-04_experimental-round2-synthesis.md:19`, verbatim:
> | **Cleave-01** | **SURVIVES + upgraded** | Round-1's "SM predicts exactly 0.0" was *false*
> (contact-potential-difference mimics the floor on magnitude + polarity). Cured by the
> **gap-independence corner** → a 4-corner symmetry discriminator {linear ∧ polarity-odd ∧
> material-indep ∧ gap-indep} no single classical mechanism fakes. The flagship GO ($7.7k). |

A contact-potential difference could mimic Cleave-01's zero because nothing forbade it. Here,
*any* classical mechanism that produces $f_R\neq f_L$ must break $x\to-x$ somewhere in the
fixture — which is why the escape routes are **enumerable at all**, and why the table above
closes four of them and the numbered list leaves exactly two.

> **Independent reproduction:** this lane recomputed the AVE-side entry from
> `ave.core.constants.ALPHA` and got `11.9093` MHz / `1.751365e-02`, matching AVE-HOPF's
> `−11.91 MHz` / `1.75%` to quoted precision. The two sides of that table are reproduced from
> different repos by different routes.

**The classical zero is conditional on the HOST being achiral — and that condition is exactly
what round-2's counterfactual relaxes.** A classical **chiral** host *does* split a handed
structure's scalar self-resonance: put the knot in sugar water and $f_R\neq f_L$, because the
composite system is no longer mirror-symmetric. So the observable is not "chirality vs no
chirality"; it is **"is the *host* chiral?"** — and on the HOPF-02a bench the host is air.

**Consequence for the discriminating axis on this observable: EXISTENCE, not magnitude.** A
measured nonzero split in an achiral host is classically forbidden; a measured zero is
classically expected. The specific value `8.756823e-03` carries no extra discriminating weight,
because — as round-1 already established and this lane does not disturb — the magnitude is
$\alpha$-injected: AVE-HOPF `docs/ave_crib_sheet.md:27`, verbatim:
> The form is **generic parallel-Γ algebra**: `(α·p · α·q)/(α·p + α·q) = α · pq/(p+q)`.
> Standard Kirchhoff parallel-impedance combination.

### §6.2 FLAG-DON'T-FIX — two contradictions surfaced, both sides verbatim, neither reframed

#### §6.2.1 The one this lane exists to expose — what the enantiomer sign-flip is a sign-flip *of*

**Side A — AVE-HOPF `main`:`research/2026-06-04_hopf-round2-chiral-counterfactual-result.md`
§2.3 (lines 84–88), verbatim:**

> Then $\Delta k/k = \kappa/n \to -\kappa/n$: **opposite-sign shift for the mirror image.**
> The HOPF enantiomer prediction ($\Delta f_R = -\Delta f_L$) is, term for term, the classical
> enantiomer sign-flip of a Pasteur medium. Classical mutual inductance (round-1's competitor) is
> parity-invariant and does NOT flip — true, but that was the wrong competitor. The right competitor,
> a *chiral* classical medium, flips exactly as AVE predicts. **C4 cannot tell them apart.**

**Side B — this lane, §5.1 C-iv + §6.1:**

> The quantity that reverses between classical enantiomers is $\Delta k/k = \kappa/n$, which
> §2.1 of that same document defines as $(k_+-k_-)/(2k_0 n)$ — a **difference between two
> circular polarisations of a wave inside a medium**. HOPF-02a measures a **scalar 1-port
> resonance of a single structure in an achiral host**. For *that* observable the classical
> prediction is **exactly zero**, not an opposite-sign shift — and AVE-HOPF's own NEC2 table
> states it: `Δ_classical = +0.000 MHz`. The classical sign-flip and the HOPF $\Delta f$
> sign-flip are therefore not "term for term" the same term: one flips a polarisation
> *difference*, the other flips a *scalar frequency*, and a classical medium delivers the second
> only when the **host** is chiral.

**Live corpus state, verified at source (`verify-before-cite`).** The round-2 relabel has
**landed** — AVE-HOPF `main`:`hardware/hopf_01_TEST_PROCEDURE.md:180`, verbatim:
> | Opposite-sign Δf for L vs R enantiomer | **CONSISTENCY-CLASS** — reproducible by classical reciprocal Pasteur (chiral) media: mirroring sends κ→−κ, so a classical chiral medium ALSO flips the sign.

So the contradiction is against **live, merged corpus text**, not a draft.

#### §6.2.2 A SECOND contradiction, found while repairing this document: is the board fabbed?

*(Rule 12 quote-and-correct, 2026-08-02. The `f9d5c86c` version of this document asserted the
HOPF-02a board was **"already fabbed"** at four places, and the driver wrote the same claim into
the shipped JSON at a fifth. All five are corrected above and in
`K2_observable_matched`/`commensurability_checklist`. The claim was inherited, not invented — and
its source is itself contradicted.)*

**Side A — AVE-HOPF `main`:`.agents/HANDOFF.md:14`, verbatim (the live status line):**

> Phase 0a fab-artifact-generation is **complete**; Grant can upload `hardware/Gerbers_hopf_02a/`
> ZIP to JLCPCB per `hardware/hopf_02a_ORDERING.md`. **Working tree is clean.** **Next gate**:
> Phase 0b — physical fab order for HOPF-02a (user action; ~$123 BOM; ordering guide ready)

**and `.agents/HANDOFF.md:42`, verbatim (the live TODO list, item 1):**

> 1. **(active, gated on user) Order HOPF-02a fab panel + 3D-print mandrels.** ~$123 BOM

**Side B — AVE-HOPF `main`:`research/2026-06-04_hopf-round2-chiral-counterfactual-result.md:193`,
verbatim:**

> **Roll-up:** HOPF-02a (the fabbed, $123, enantiomer-pair board) was designed to deliver C4 as "the

**Both are live, merged AVE-HOPF `main` text, and they cannot both be true.** A board whose fab
order is the *next gate* is not a *fabbed* board. This lane has corrected **its own** documents to
the HANDOFF reading, because HANDOFF is the file whose job is current status and it is the more
recent of the two — but that is a working assumption, not an adjudication.

**Flag-don't-fix.** Nothing was written to AVE-HOPF. Which of the two is wrong, and the correction
to whichever it is, belongs to an AVE-HOPF lane and to Grant — who is the one person who knows
whether a PCB order was ever placed. It is routed as question **(2)** in §8.

**One more disclosure, so the trail is complete.** This lane's own **FROZEN** prereg carries the
same inherited phrasing at `research/2026-08-02_pasteur-kappa-desk-calc_prereg-FROZEN.md:48–49`
— "This lane runs it, at \$`0`, on the as-fabbed hardware." Read narrowly that is true (the
desk-calc itself cost nothing and consumed the released as-fabbed *geometry*); read as a claim
about a *bench*, it inherits the same error. **The prereg is frozen and was not touched** — a
frozen document's errors are corrected in the result, not in the freeze. `git diff` on that file
across this repair is empty by construction.

**Scope of what this lane does and does not say.**

- It does **not** adjudicate whether C4 returns. That is a framing call and it routes to Grant /
  the auditor lane, with both sides above on the record.
- It does **not** disturb round-2's **C3** verdict. If the classical split is zero in every
  achiral host, then "same $\Delta f/f$ in air, oil and vacuum" is classically $0=0=0$, so C3
  remains non-discriminating on its own — §2.2 of round-2 is untouched.
- It does **not** claim the magnitude `8.756823e-03` is AVE-distinct. It is $\alpha$-injected
  (§6.1). What is at issue is a **presence/absence** divergence, which is the shape the corpus's
  own round-2 synthesis says survives (`research/2026-06-04_experimental-round2-synthesis.md`).
- It does **not** touch AVE-HOPF. Nothing was written to that repo.

### §6.3 What would make the two κ's genuinely commensurable

Constructively, three routes — each is a real experiment or a real derivation, not a re-definition:

1. **Build the composite.** Stack $N \gtrsim$ `86.5258` knots per m³ into a slab and measure the
   optical rotation of a transmitted wave. That reads $\kappa_{\rm cls}$ *in its own defining
   coordinates*. AVE would then have to predict the same slab's rotation — which requires a
   derivation the corpus does not have (AVE-HOPF `docs/glossary.md:131`: the K4-substrate →
   wire-antenna $\Delta f/f$ path "is NOT derived end-to-end in either repo").
2. **Derive the AVE side as a bulk parameter.** Show that $\alpha\,pq/(p+q)$ *is* the
   coefficient of a $k_\pm$ split for a wave in the AVE vacuum, with a stated density-free
   mechanism. Then C-iii and C-iv become SAME and the magnitude comparison adjudicates directly.
3. **Measure the common observable (cheapest — the board is *designed*, not built).** The
   enantiomer split of the scalar self-resonance in air: `0` vs `1.751365e-02`, margin
   `91.6098`× over the S-8 **fabrication** floor (`64.855`× over the worst combined
   fabrication+measurement floor S-1 admits — §6.1 floor-class note). This is still the
   cheapest of the three: it needs **no new
   design and no new derivation**, only the fab order that is already staged and gated — AVE-HOPF
   Phase 0b, ~\$`123` BOM **plus build time**, not \$`0`. Routes 1 and 2 need a whole new
   composite slab and a whole new derivation respectively; this one needs a PCB order.

---

## §7 Idealizations, as frozen — and where each one lands

| # | Idealization | Frozen bounding leg | Outcome |
|---|---|---|---|
| **I-1** | mode $I_0\sin(\pi s/L)$ | γ ∈ {`0.8`,`1.0`,`1.2`} + uniform | $\kappa$: `31.784754192972528` / `29.094170460375217` / `27.229641103511227` / `56.75722510479334` — bin unchanged |
| **I-2** | free space (no FR-4, no ground plane, no counterpoise) | $\varepsilon_{\rm eff}$ ∈ {`1.0`,`1.5`,`2.0`} | $\kappa$: `29.094170460375217` / `14.222269603995263` / `8.438452401184271` — bin unchanged |
| **I-3** | dipole truncation | G6 | bbox diag / λ = `0.11784810733938897`, well inside `0.25` |
| **I-4** | lossless copper | direction of the bound (frozen) + a number (**not frozen**) | $R_{\rm rad}=$ `0.7385` Ω is a strict upper bound on $\kappa$; loss factor `0.6047315980017243` |
| **I-5** | dilute mixing at close packing | K-3's $V_\chi$, $N^\star$ (frozen escape) | **this is the one that bites**: $\kappa_{\rm cls}(N_{\rm ref})$ is `290.942`× past the linear ceiling, so §3's $N^\star$ carries the physics, not §5.2's `29.09` |

**No NEC2 was run** (PyNEC / necpp are not installed in this environment; disclosed at freeze
time, prereg §6.2). K-2 needed none — it is a parity theorem plus two existing AVE-HOPF receipts.
The classical chain is analytic + quadrature, validated against two closed-form known-positives.
**No external experimental value was used or invented.**

---

## §8 The single most load-bearing finding

> **The round-2 MAGNITUDE leg cannot be run as posed, because the two κ's are different kinds of
> object — a density-scaled bulk medium parameter versus a density-free per-topology
> self-resonance shift (3 of 4 checklist items DIFFERENT). What CAN be run, and what the
> **already-designed** HOPF-02a hardware is built to read once it is **ordered** (Phase 0b,
> gated), is the enantiomer split of the scalar self-resonance
> in an achiral host: classical EM gives exactly `0` (parity-covariance, with the as-fabbed
> mirror verified to be a pure $x\to-x$ reflection at `0.0` mm residual, and AVE-HOPF's own NEC2
> column reading `+0.000 MHz`), against AVE's `11.9093` MHz. That is a presence/absence
> divergence, not a magnitude one — and a classical chiral medium reproduces it only when the
> HOST is chiral, which the air-bath HOPF-02a bench is not.**

The actionable consequence, stated as a routed question and not as a lane decision: round-2's
§2.3 equates the classical enantiomer sign-flip (a reversal of a *polarisation difference*) with
the HOPF enantiomer prediction (a reversal of a *scalar frequency*), and the live protocol row at
`hopf_01_TEST_PROCEDURE.md:180` carries that reading as CONSISTENCY-CLASS. **Whether the C4 leg
returns to the table — as an EXISTENCE discriminator on an achiral bench, never as a magnitude
one — is Grant's / the auditor lane's call, with both sides verbatim in §6.2.** This lane's own
verdict is the frozen one: **bin (d), magnitude bin (a) reported and non-adjudicating.**
