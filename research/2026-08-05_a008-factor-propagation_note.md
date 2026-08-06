# A-008 convention propagation check — RESULT NOTE

**Date:** 2026-08-05 · **Branch:** `research/a008-factor-propagation` · **Lane class:** CHECK
(derivation-only; no driver, no engine run, no KB edit).
**Frozen pre-registration:** [`2026-08-05_a008-factor-propagation_prereg-FROZEN.md`](2026-08-05_a008-factor-propagation_prereg-FROZEN.md),
pushed alone before any analysis text existed.
**Dispatch:** `_orchestration/docket-entries/2026-08-05-rulings-sheet-nine.md` item 2.

> **No backticked numerals in this note, and no number-check gate is minted.** This lane runs no
> driver. Every numeral below is either quoted verbatim from a cited corpus site or an integer /
> integer-ratio derived in-text. There is no computed float to gate.

---

## 0. Verdict, one screen

> **BIN: `FACTOR-CLOSED-BY-A008`.**
>
> **$E_g = \hbar\omega_m$** — not $2\hbar\omega_m$. Numerically $\hbar\omega_m = 2\,m_ec^2 = 1.022$
> MeV, which is exactly the pair-creation threshold the corpus already books as the bandgap.
>
> The factor-4-vs-2 discrepancy in the two-band lane's FLAG-1 is **exactly one factor of the
> already-ruled half-cover**, and nothing else. Applying A-008 consistently removes it with **no
> new choice**: there are two independent 2's in play — the $\mathrm{SU}(2)\to\mathrm{SO}(3)$
> covering degree and the Klein–Gordon $\pm$ branch doubling — and FLAG-1's arithmetic compounds
> them onto the same quantity. They live on opposite sides of the covering map and do not compound.
>
> **A-008 does not merely fail to select FLAG-1's other candidate — it already struck it out by
> name.** FLAG-1 offers "$G_c/I_\omega = 1/4$, not 1" as a live resolution. That exact move is a
> corpus path closed on the same 2026-04-27 adjudication, verbatim at
> `research/_archive/L5/axiom_derivation_status.md`:1395: *"**Reconciliation A (SUPERSEDED — moduli
> surgery unnecessary):** ~~Re-pin Cosserat moduli so m_Cosserat = m_e = 1. Requires `G_c/I_ω =
> 1/4`.~~ Unnecessary: m_Cosserat = 2 and m_e = 1 both correct (medium full-cover vs spinor
> projection)."*
>
> **Reconciliation with the corpus is total, not partial.** All 14 tracked non-lane sites carrying
> $\omega_m \sim 1$ MeV (§4, two-method, both engines named) are already reading
> $\omega_m = 2\omega_C$ and are therefore A-008-consistent as written. Three independent sites
> put the observable gap at $2m_ec^2 = 1.022$ MeV. **$E_g = 2\hbar\omega_m = 2.044$ MeV appears at
> exactly three sites in the whole corpus, and all three are the two-band FLAG-1 text and its two
> landings.** That is the repair surface, and it is ROUTED, not executed here.

**One live residue, quoted and NOT picked (§5, FLAG-D).** One canon prose clause
(`l3-electron-soliton-synthesis.md`:132) states the direction of the half-cover the *other* way.
Its own boxed conclusion three lines later (:134) states it the A-008 way. It was already flagged
for Grant on 2026-07-08 and is **not** reopened by this lane, because the direction is
over-determined against it by the 14-site witness set, by the three independent gap-energy sites,
and by the leaf's own box. If Grant were to rule that clause canonical, this lane's verdict
inverts and 14 corpus sites become wrong — that is the single hinge, and it is named here rather
than buried.

---

## 1. The ruled convention, re-derived (not assumed)

### 1.1 What A-008 says

`manuscript/ave-kb/common/trampoline-framework.md`:224-227, verbatim:

> **A-008 resolution canonical** (Grant adjudication 2026-04-27):
> - $m_{\text{Cosserat}} = 2$ is the **frame** (medium full-cover SO(3)) twist rate
> - $\omega_C = m_e = 1$ is the **field** (spin-½ projection) frequency
> - The factor of 2 IS the half-cover, exactly as the picture predicts

### 1.2 Is $m_{\text{Cosserat}}$ a frequency or a winding integer? — FREQUENCY, and it IS $\omega_m$

This is the first thing that had to be settled, because the corpus has a documented history of
homonymous integers (the electron's two "3"s; the "three distinct 2's" of
`dual-reactance-storage-taxonomy.md`:42-56). Three independent provenance sites give
$m_{\text{Cosserat}}$ **units**, and one derives it from the gap formula itself:

| site | verbatim | what it settles |
|---|---|---|
| `research/_archive/L3_electron_soliton/77_lattice_to_axiom4_bridge.md`:69 | *"m_Cosserat = 2·m_e. Medium twists at full SO(3) (360°), spinor observable wraps SU(2) (720°). Gives factor-of-2 between substrate ω_substrate = 2·m_e c²/ℏ and spin-½ observable ω_e = m_e c²/ℏ."* | it is a mass / frequency, dimensionally — not a winding count |
| `research/_archive/L5/axiom_derivation_status.md`:1377 | *"the Cosserat rotational mass-gap is `m² = 4·G_c/I_ω`. With engine defaults `G_c = I_omega = 1.0` …, the Cosserat rotational mass-gap is **m_Cosserat = 2 in natural units, NOT m_Cosserat = 1 = m_e**"* | $m_{\text{Cosserat}} \equiv \omega_m = \sqrt{4G_c/I_\omega}$ — an **identity**, not a numerical coincidence of the placeholder |
| `research/_archive/L5/axiom_derivation_status.md`:148 | *"the right global drive frequency (ω_global = m_Cosserat = 2 per A-008/Reconciliation B)"* | it is used operationally as a **drive frequency** |

So the two objects FLAG-1 has to relate — the engine's gap $\omega_m$ and A-008's frame twist rate
$m_{\text{Cosserat}}$ — are the **same object**, and A-008 is a ruling directly about it.

### 1.3 The direction, re-derived from the covering itself

A-008's numerals assign the larger frequency to the frame. That direction is not a convention this
lane has to take on trust — it follows from the covering map:

- A rotation of the medium frame by angle $\theta$ is represented on a spin-½ field by phase
  $\theta/2$ (the $\mathrm{SU}(2)\to\mathrm{SO}(3)$ 2-to-1 covering).
- At one common physical twist, the **frame** configuration returns to identity after $2\pi$ of
  frame angle; the **field** returns after $4\pi$ — i.e. the field's return period is **twice** the
  frame's.
- Twice the period is **half** the frequency. Therefore $\omega_{\text{field}} =
  \omega_{\text{frame}}/2$, i.e. $\boxed{\omega_m = 2\,\omega_C}$.

Corpus states the same conclusion in as many words at `research/_archive/L5/terminology_canonical.md`:115:
*"ω_C = 1 is the spin-½ projection (SU(2) → SO(3) is 2-to-1, so observable rate is half the
underlying medium rate)"*, and again at `axiom_derivation_status.md`:1361: *"Observer sees the
spinor's apparent frequency = m_Cosserat / 2 = 1."*

### 1.4 The two 2's, and which side of the covering each lives on

| the "2" | what it is | which side it acts on | provenance |
|---|---|---|---|
| $2_{\text{cover}}$ | the $\mathrm{SU}(2)\to\mathrm{SO}(3)$ covering degree | **maps across** the covering: field-frequency = frame-frequency / 2 | DERIVED + ratified (A-008, `trampoline-framework.md`:224-227) |
| $2_{\text{KG}}$ | the $\pm\omega$ branch doubling of a real second-order-in-time field: the interband beat is twice the branch bottom | **acts within** one side, whichever side you are standing on | the two-band operator's own structure (`research/2026-08-05_two-band-kinematics_result.md` §8) |

These are different objects. $2_{\text{cover}}$ changes which side of the covering a numeral is
quoted on; $2_{\text{KG}}$ relates a branch bottom to an interband beat on a fixed side. Applying
both to the same numeral, in the same direction, is the double-count.

---

## 2. Convention-propagation table — each site's factor reading under A-008

Side tags: **F** = frame-side (medium $\mathrm{SO}(3)$ twist), **f** = field-side (spin-½ readout).
All frequencies in units of $\omega_C$; all energies in units of $m_ec^2$.

| # | site (file:line, base `0a37ddca`) | what it carries | side under A-008 | factor reading | status |
|---|---|---|---|---|---|
| 1 | `common/trampoline-framework.md`:224-227 | the ruling itself: frame $=2$, field $=1$ | — | defines $2_{\text{cover}}$ | **canonical** |
| 2 | `common/trampoline-framework.md`:192 | $m_\omega^2 = 4G_c/I_\omega$; $T = 2\pi/\omega_m = \pi$ | **F** | $\omega_m = 2$; period $\pi$ is the FRAME period | consistent |
| 3 | `common/trampoline-framework.md`:194 (Rule-12) | the gap is the *flywheel frequency / clock gap* of the Cosserat $\omega$ regulator, not the rest-mass store | **F** | confirms the gap is a medium-clock numeral | consistent — and it is the reason the projection is needed |
| 4 | `cosserat-mass-gap.md`:11, :17-19, :72, :80 | $\omega_m = \sqrt{4G_c/I_\omega} = 2$, $T = \pi$, Verlet-validated to 0.35% | **F** | frame-side throughout | consistent; the leaf never claims a field-side reading |
| 5 | `cosserat-mass-gap.md`:61 | the factor 4 $=2\times2$ ($\Sigma_{ij}$ doubling $\times$ Lagrangian→EOM) | **F** | **neither** of these 2's is $2_{\text{cover}}$ or $2_{\text{KG}}$ — a third and fourth distinct 2, internal to the modulus algebra | consistent; do-not-fuse |
| 6 | `cosserat-mass-gap.md`:143 | $m_ec^2 = \hbar\omega_C = T_{EM}\,\ell_{\text{node}}$ | **f** | the rest energy is booked against $\omega_C$, **not** $\omega_m$ | consistent — the leaf already keeps the two clocks apart |
| 7 | `cosserat-mass-gap.md`:151 | $G_c$, $I_\omega$ are "placeholders … rather than measured-from-substrate" | **F** | true of the **absolute** moduli; **understates** the ratio, which A-008 pins (§3.3) | ROUTED tag repair (FLAG-P) |
| 8 | `common/lattice-model-register.md`:104 | *"valid for $\omega\ll\omega_0=m_ec^2/\hbar=\omega_C$; the pair channel opens at $2\omega_C=1.022$ MeV"* | **f** | field-side branch bottom stated explicitly as $\omega_C$; gap $=2\omega_C$ | **consistent, and decisive** — canon already puts the branch bottom exactly where FLAG-1 says it must be, and gets there by reading the field side, not by retuning moduli |
| 9 | `common/translation-tables/translation-circuit.md`:890 | *"The pair-creation threshold $2m_ec^2 = 1.022$ MeV \| **The bandgap $E_g$**"* | **f** | $E_g = 2\,m_ec^2 = \hbar\omega_m$ | consistent |
| 10 | `vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`:180 | *"**Threshold $E > 2 m_e c^2 = 1.022$ MeV**"* | **f** | same | consistent |
| 11 | `vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`:41 | *"In natural units $\omega_m = 2$; in physical units, $\omega_m \sim 1$ MeV"* | **F**→MeV | the conversion **is** $\hbar\omega_m = 2m_ec^2$; the site is already using $\omega_m = 2\omega_C$ | consistent |
| 12 | the other 13 $\omega_m\sim1$ MeV sites (§4) | the gap at the $\sim$1 MeV scale | **F**→MeV | identical conversion | consistent |
| 13 | `research/2026-08-05_two-band-kinematics_result.md` §7 FLAG-1 (:221-230) | branch bottom read as the REST frequency, then $E_g = 2\hbar\omega_0$ with $\omega_0 = \omega_m$ ⇒ $E_g = 4m_ec^2$ | **F** numeral fed into an **f** formula | **the double-count**: $2_{\text{KG}}$ applied to a frame-side branch bottom without first crossing the covering | **the defect** — ROUTED |
| 14 | `research/2026-08-05_two-band-kinematics_result.md` §8 (:277-284) | *"the Dirac Zitterbewegung frequency is $2\omega_C$, which this operator reaches only if the branch bottom is $\omega_C$, i.e. $G_c/I_\omega = 1/4$"* | same | the operator **does** reach $2\omega_C$: its frame-side beat $2\omega_m = 4\omega_C$ has field-side image $2\omega_C$. No retune needed | ROUTED |
| 15 | `common/translation-tables/translation-circuit.md`:355-364 | the landing's Zitterbewegung-REFUSED bullet, carrying $E_g=4m_ec^2$ and *"Landing $E_g=2m_ec^2$ needs $G_c/I_\omega = 1/4$, not 1."* | same | same | ROUTED |
| 16 | `common/claim-quality.md`:1649 (`clm-2bkp7v`) | mirror of the same bullet | same | same | ROUTED |

**Reading of the table.** Every frame-side site is internally consistent; every field-side site is
internally consistent; the two families agree with each other through exactly one factor of
$2_{\text{cover}}$. The only sites that do not fit are rows 13-16, and they are one text and its
two landings.

---

## 3. FLAG-1, resolved

### 3.1 The computation, both sides written out

Frame side (what the two-band operator's eigenvalues literally are):

$$\omega_0^{(F)} = \omega_m = 2, \qquad \text{frame interband beat } = 2\,\omega_m = 4 .$$

Field side (what a spin-½ port reads), obtained by one application of $2_{\text{cover}}$:

$$\omega_0^{(f)} = \omega_m/2 = \omega_C = 1, \qquad \text{field interband beat } = 2\,\omega_C = 2 = \omega_m .$$

$E_g$ is a **field-side** quantity in every corpus use of it — the pair-creation threshold and the
Zitterbewegung frequency are both defined on the spin-½ observable, not on the medium frame.
Therefore

$$E_g = \hbar\cdot 2\omega_C = \hbar\,\omega_m = 2\,m_ec^2 = 1.022\ \text{MeV}.$$

### 3.2 Which FLAG-1 candidate A-008 selects

FLAG-1 (as corrected by the Tier-2 verify, which collapsed its three candidates to two) offers:

| candidate | A-008 verdict |
|---|---|
| **(a)** *"the placeholder is off by 4 in $G_c/I_\omega$"* — i.e. $G_c/I_\omega = 1/4$ | **RULED OUT, by name.** It is "Reconciliation A", struck through as SUPERSEDED on the same 2026-04-27 adjudication (`axiom_derivation_status.md`:1395). Adopting it would set the medium twist rate equal to the spinor readout rate and **delete the half-cover**. `terminology_canonical.md`:115: *"Engine at default G_c = I_ω = 1 is correctly tuned; no moduli surgery needed."* |
| **(b) ≡ (c)** *"$\omega_m$ is being read as the FULL gap rather than the branch bottom"* ≡ *"the two 2's are being double-counted"* | **SELECTED.** Under A-008, $\hbar\omega_m$ **is** the full field-side gap — precisely because $\omega_m$ is a frame-side numeral whose field-side image is $\omega_C$. The lane's two phrasings are the same operation seen from the two sides, which is why the Tier-2 verify was right to merge them. |

### 3.3 Corollary — the ratio $G_c/I_\omega$ is RULED, not ENG-CHOICE

Under A-008 plus the corpus's own length calibration $\ell_{\text{node}} \equiv \hbar/(m_ec)$
(so that $\omega_C = 1$), the ratio is forced:

$$\omega_m^2 = 4G_c/I_\omega \quad\text{and}\quad \omega_m = 2\omega_C \;\Longrightarrow\; G_c/I_\omega = \omega_C^2 = 1 .$$

`terminology_canonical.md`:115 states this as the ratified outcome. So the ENG-CHOICE-placeholder
tag carried at `cosserat-mass-gap.md`:151, `translation-circuit.md`:365-369 and
`common/claim-quality.md`:1648 is correct about the **absolute** moduli and **understates** the
**ratio**, which A-008 pins. Routed as FLAG-P; not executed.

---

## 4. The $\omega_m \sim 1$ MeV witness set — re-derived here, two methods, engines named

Per the prereg (§0 row 9, §3 step 3): the two-band Tier-2 verify retracted an absence claim that
had been made on a single grep. This lane therefore re-derives the list rather than inheriting it,
with two different regex engines.

**Method 1 — ripgrep (Rust `regex` crate).** Pattern (gap-token), then filtered on `MeV`:

```
(\\omega_m|\\omega_\{m\}|ω_m|omega_m|m_\\omega|mass.?gap)
```

**Method 2 — `git grep -E` (git's own POSIX-ERE matcher).** Pattern (surface form of the value):

```
(\\sim|~|\{\\sim\})[ ]?1(\.0)?[$ ]*(~|\\,)?[ ]*(\\text\{)?MeV
```

> **Recorded conditioning defect, same class as the lesson being applied.** Method 2's *first*
> formulation omitted the `[$ ]*` allowance for LaTeX math delimiters and silently returned 9 of
> the 20 files — a false negative on more than half the set, invisible without the cross-check.
> This is the known `$…$`-escape false-negative failure mode, reproduced here on the very lane
> that exists because of a single-method false negative. Both methods are reported as run, with
> the corrected pattern.

**Agreement.** After correction the two methods return the same file set. Fourteen tracked,
non-archive, non-lane files carry the gap at the $\sim$1 MeV scale:

| # | file | lines |
|---|---|---|
| 1 | `manuscript/ave-kb/common/translation-tables/translation-circuit.md` | 102, 518, 600, 695, 754, 760, 767, 790 |
| 2 | `manuscript/ave-kb/common/statistics-under-ave.md` | 103 |
| 3 | `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` | 179 |
| 4 | `manuscript/ave-kb/vol1/claim-quality.md` | 127 |
| 5 | `manuscript/ave-kb/vol3/claim-quality.md` | 1220 |
| 6 | `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md` | 13, 25, 41, 55, 185 |
| 7 | `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/index.md` | 36 |
| 8 | `manuscript/ave-kb/vol9/ch6-temperature-characteristics/index.md` | 23, 35 |
| 9 | `manuscript/ave-kb/vol9/ch9-mechanical-characteristics/index.md` | 32 |
| 10 | `manuscript/ave-kb/vol9/ch10-magnetic-microrotational-characteristics/index.md` | 11 |
| 11 | `manuscript/vol_9_vacuum_datasheet/chapters/06_temperature_characteristics.tex` | 36, 118, 164 |
| 12 | `manuscript/vol_9_vacuum_datasheet/chapters/09_mechanical_characteristics.tex` | 217, 272, 290 |
| 13 | `manuscript/vol_9_vacuum_datasheet/chapters/16_cross_volume_reference.tex` | 70 |
| 14 | `manuscript/vol_9_vacuum_datasheet/figures/gen_thermal_characteristics.py` | 17, 55, 114 |

Plus, outside the corpus proper, three lane / orchestration docs:
`research/2026-05-31_FT-1_delta-strain-eta-epsilon_prereg.md`:18,
`research/2026-08-05_two-band-kinematics_prereg-FROZEN.md`:114,117, and
`_orchestration/2026-05-28_vol-9-vacuum-datasheet-plan-and-handoff.md`:53. Fourteen non-lane files
confirms and exceeds the Tier-2 verify's "$\geq 9$ tracked sites".

### 4.1 Reconciliation — the whole witness set is already A-008-consistent

Every one of these sites reaches "$\sim$1 MeV" by the **same** conversion, and two of them write
it out:

- `delta-strain-cosmic-tcc.md`:41 — *"In natural units $\omega_m = 2$; in physical units,
  $\omega_m \sim 1$ MeV per the canonical Cosserat-couple-stress + nodal-inertia scaling."*
- `manuscript/vol_9_vacuum_datasheet/chapters/06_temperature_characteristics.tex`:36 — *"In natural
  units $\omega_m = 2$; in physical units $\hbar\omega_m \sim 1$ MeV."*

and the two-band lane's own prereg does the arithmetic explicitly at
`2026-08-05_two-band-kinematics_prereg-FROZEN.md`:117 — *"so $\omega_m = 2 \Rightarrow
\hbar\omega_m = 2\,m_ec^2 = 1.022$ MeV."*

The unit that turns $\omega_m = 2$ into $\sim$1 MeV **is** $\hbar\omega_C = m_ec^2 = 0.511$ MeV.
So each of the 14 sites is, silently, already asserting $\omega_m = 2\omega_C$ — the A-008 ratio.
**No site needs repair for the ratio; the whole set is consistent as written.**

### 4.2 Independent corroboration from the gap-ENERGY side

Three sites that never mention $\omega_m$ put the observable gap at the same place:

- `common/translation-tables/translation-circuit.md`:890 — the pair-creation threshold
  $2m_ec^2 = 1.022$ MeV **is** the bandgap $E_g$.
- `common/lattice-model-register.md`:104 — the field-side branch bottom is
  $\omega_0 = m_ec^2/\hbar = \omega_C$ and the pair channel opens at $2\omega_C = 1.022$ MeV.
- `vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`:180 — threshold
  $E > 2m_ec^2 = 1.022$ MeV.

$1.022$ MeV $= \hbar\omega_m$. The two families — the $\omega_m$ sites and the $E_g$ sites — meet
exactly at $E_g = \hbar\omega_m$, with no residual.

`lattice-model-register.md`:104 deserves the emphasis: FLAG-1's own statement of what it wants is
*"To land $E_g = 2m_ec^2$ the branch bottom must be $\omega_C$."* Canon **already puts the branch
bottom at $\omega_C$** — on the field side, by projection — without touching a modulus.

### 4.3 The counter-set

$E_g = 2\hbar\omega_m = 4m_ec^2 = 2.044$ MeV occurs at exactly three places in the tracked corpus,
all descended from one text: `research/2026-08-05_two-band-kinematics_result.md`:224 (and its
prereg :138), `common/translation-tables/translation-circuit.md`:355-364, and
`common/claim-quality.md`:1649. Repair surface, routed.

---

## 5. FLAGS (verbatim; flag-don't-fix — none silently resolved)

### FLAG-D — the direction-of-the-2 prose, two sites, quoted, NOT picked

This is the prereg's mandated negative control (§0 row 9): hunt for a site that would invert the
A-008 direction if read at face value.

**D1 — `manuscript/ave-kb/common/trampoline-framework.md`:220, verbatim:**

> **The half-cover paradox.** When you rotate the field by $2\pi$ (one full turn), the frame must
> rotate by $\pi$ (half turn) for the bond network to re-close in the same configuration. This is
> the SU(2) → SO(3) double cover: 720° of field rotation = 360° of frame rotation = identity.

The first sentence assigns the field the larger swept angle; four lines later, :225-226 assign the
frame the larger numeral. The second sentence is the standard return-period statement and **is**
consistent with :225-226 once one notes that the longer return period is the *lower* frequency
(§1.3). So :220 is a loose picture whose first clause reads backwards against its own second
clause; it is not a competing ruling.

**D2 — `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md`:132, verbatim:**

> The factor of 2 between $m_{\text{Cosserat}}$ (medium oscillation period) and $m_e$ (observable
> envelope cycle period) arises directly from **K4 bipartite structure**. … one full
> medium-frequency traversal visits both lobes, but the time-averaged envelope completes a cycle
> per LOBE-VISIT, so observable frequency = 2 × medium frequency:

**Against A-008, `research/_archive/L5/terminology_canonical.md`:115, verbatim:**

> $\omega_C = 1$ is the spin-½ projection (SU(2) → SO(3) is 2-to-1, so **observable rate is half
> the underlying medium rate**).

**These two cannot both be read at face value.** But the SAME leaf, three lines below D2, boxes the
A-008 direction — `l3-electron-soliton-synthesis.md`:134, verbatim:

> $$\boxed{\, m_e \text{ (observable)} = m_{\text{Cosserat}} \text{ (medium)} / 2 \,}$$

so the contradiction is **intra-leaf**, between a prose clause and its own boxed conclusion, not
between A-008 and a leaf's ruling.

**Already flagged, and the flag's cite has shifted.** `research/2026-07-08_electron-g2-selforbit_result.md`:73
flags this exact pair — *"Read against E ∝ ω these two lines point in **opposite directions** …
This is a **corpus-internal direction-of-the-2 tension**, FLAGGED not resolved … (Grant's call on
the direction; it does not move the verdict.)"* — citing `l3-electron-soliton-synthesis.md:103-105`.
That cite has **line-shifted**: :103-105 now holds the $C_e$ / $V_{\text{SNAP}}$ /
$V_{\text{yield,macro}}$ table rows. Content-primary target is now **:132-134**.

**Why FLAG-D does not reopen the bin.** The direction is over-determined against D2's prose by
four independent things: (i) the same leaf's boxed :134; (ii) the ratified A-008 text at
:224-227 plus its three provenance sites; (iii) the 14-file witness set of §4, every member of
which converts $\omega_m = 2$ to $\sim$1 MeV and therefore only closes if $\omega_m = 2\omega_C$;
(iv) the three independent gap-energy sites of §4.2. **If D2's prose were canonical, $\hbar\omega_m$
would have to be $0.511$ MeV and all fourteen sites would be wrong.** This lane does not pick;
it records that the corpus's mass sits overwhelmingly on the A-008 side and routes the prose
repair.

### FLAG-C — the gap cite `trampoline-framework.md:188` is corpus-wide stale

On this lane's base, `trampoline-framework.md`:188 is the microrotation equation of motion
($I_\omega\ddot{\boldsymbol\omega} = \nabla\cdot\boldsymbol\mu + 2\sigma^A + \mathbf{g}$); the gap
statement is at **:192**. Pure line-shift, correct-when-written (the two-band lane re-located it
for its own use at its §1). Sites still citing :188:
`translation-circuit.md`:518, :600, :695, :754, :790; `vol9/ch6-temperature-characteristics/index.md`:23;
`vol9/ch9-mechanical-characteristics/index.md`:32; `vol3/claim-quality.md`:1220;
`vol1/claim-quality.md`:127; `delta-strain-cosmic-tcc.md`:185;
`vol_9_vacuum_datasheet/chapters/06_temperature_characteristics.tex`:36;
`…/09_mechanical_characteristics.tex`:217, :290; `…/16_cross_volume_reference.tex`:70;
`_orchestration/2026-05-28_vol-9-vacuum-datasheet-plan-and-handoff.md`:53. Doc-lane repair; ROUTED.

### FLAG-H — two objects are called "the mass gap" and they differ by exactly the half-cover 2

- Cosserat rotation-sector gap: $\hbar\omega_m \approx 1.022$ MeV $= 2m_ec^2$ (**frame** side).
- Yang-Mills mass gap: *"$\Delta = m_e c^2 \approx 0.511$ MeV (unknot ground state)"*
  (`vol2/nuclear-field/index.md`:25; `vol2/nuclear-field/ch12-millennium-prizes/index.md`:18;
  `…/yang-mills-steps3-5.md`:34; `src/ave/axioms/yang_mills.py`:368).

Different sectors, different objects — and their ratio is exactly $2$, which is precisely the
coincidence-magnet class the corpus already guards elsewhere ("the three distinct 2's",
`dual-reactance-storage-taxonomy.md`:42-56; "three speeds, do NOT fuse",
`cosserat-mass-gap.md`:116-132). Note the existing three-2's table carries **neither**
$2_{\text{cover}}$ **nor** $2_{\text{KG}}$, and `cosserat-mass-gap.md`:61's factor 4 is a further
pair of distinct 2's. A do-not-fuse extension is a candidate; ROUTED, not drafted here.

### FLAG-P — provenance-tag understatement on $G_c/I_\omega$

Per §3.3, A-008 pins the **ratio** $G_c/I_\omega = 1$ while leaving the absolute moduli free.
`cosserat-mass-gap.md`:151, `translation-circuit.md`:365-369 and `common/claim-quality.md`:1648 tag the
pair as ENG-CHOICE placeholders without distinguishing ratio from scale. ROUTED.

### FLAG-S — the mandated SVA v0.2 leaf is not on `main`

The dispatch mandates the §0 header at leaf v0.2 with row 11. On this lane's base
`manuscript/ave-kb/common/standard-vacuum-analysis.md` is still v0.1 (10 rows); v0.2 exists only on
the unmerged branch `kb/sheet-nine-execution-0805`. This lane used the stricter 11-row form,
sourced from that branch, and declared the deviation in the frozen prereg §5. Secondary
observation: on that branch the fenced header block still self-labels "SVA v0.1-pilot" in its own
first line while carrying eleven rows. ROUTED to whoever lands v0.2.

---

## 6. Routed repairs — NOT executed by this lane

| # | target | change implied by the verdict | owner |
|---|---|---|---|
| R1 | `common/translation-tables/translation-circuit.md`:355-364 | the Zitterbewegung bullet's *"$E_g = 4m_ec^2$ … needs $G_c/I_\omega = 1/4$, not 1"* is superseded by A-008; the operator reaches $2\omega_C$ by projection, not by retune | auditor / doc lane |
| R2 | `common/claim-quality.md`:1649 (`clm-2bkp7v`) | same bullet, same repair | auditor / doc lane |
| R3 | `research/2026-08-05_two-band-kinematics_result.md` §7 FLAG-1 + §8 | Rule-12 header recording that FLAG-1 is closed by A-008 with candidate (a) struck and (b)≡(c) selected; body preserved | two-band lane / auditor |
| R4 | `l3-electron-soliton-synthesis.md`:132 | the prose clause *"observable frequency = 2 × medium frequency"* contradicts its own :134 box and A-008 — Grant's direction call, already open since 2026-07-08 | Grant, then doc lane |
| R5 | `research/2026-07-08_electron-g2-selforbit_result.md`:73 + `_prereg.md`:86 | the flag's cite `:103-105` has line-shifted; content-primary is `:132-134` | doc lane |
| R6 | `trampoline-framework.md`:220 first clause | reads backwards against its own second clause and against :225-226 | doc lane |
| R7 | the 15 sites citing `trampoline-framework.md:188` | repin to :192 (FLAG-C) | doc lane |
| R8 | `cosserat-mass-gap.md`:151, `translation-circuit.md`:365-369, `common/claim-quality.md`:1648 | distinguish ratio-RULED from scale-ENG-CHOICE (FLAG-P) | auditor |
| R9 | `dual-reactance-storage-taxonomy.md` three-2's table + a do-not-fuse line for the two mass gaps | extend the coincidence-magnet guard (FLAG-H) | auditor |
| R10 | `cosserat-mass-gap.md` §4 | the leaf carries the frame-side $\omega_m$ and the field-side $\omega_C$ (:143) without ever naming the projection between them; a one-line side tag would have prevented FLAG-1 | auditor |

---

## 7. Classification + fence

**Class: consistency / convention audit. Mints nothing, moves no solidity, adjudicates no physics
fork.** The half-cover factor is DERIVED (a covering degree) and was ratified 2026-04-27; this lane
adds no new derivation, it propagates an existing ruling and finds the corpus already consistent
with it at 14 of 14 witness sites.

**This lane does NOT license:** any statement about the electron's rest-mass value; any
Zitterbewegung *claim* (only a reading of what the corpus's own identification implies); any change
to the two-band lane's `FORM-REPRODUCED-V-MISMATCH` verdict, which is independent of FLAG-1 and
untouched; any KB edit — every repair above is routed; and any promotion of $E_g = 2m_ec^2$ to an
AVE result. That value is definitional given $m_e$, as `translation-circuit.md`:890 already tags it
(*"the VALUE is imported via $m_e$ (definitional)"*). The content here is that a ruled convention,
applied consistently, is self-consistent — and that FLAG-1's residual was a projection error, not
a physics fork.

**The single hinge, stated plainly:** if Grant rules FLAG-D's D2 prose clause canonical over
A-008, this verdict inverts to $E_g = 2\hbar\omega_m$ and the fourteen $\sim$1 MeV sites all become
wrong. That is the only way this bin moves.
