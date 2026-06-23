# RESULT — Chiral srs / Laves-K4 Optical-Activity Channel: symmetry-PERMITTED, AVE-distinct-IN-FORM, magnitude-PENDING, NOT bankable

> **Class:** refute-by-default DEFLATION. This doc records the HONEST adjudicated outcome of a 5-agent
> refute-by-default workflow (derive: chiral eigensolve + space-group + relate/bounds → synthesis →
> adversarial-verify; the adversarial-verify UPHELD the verdict with two scoped corrections, both baked
> in below). The headline is FORM-only / magnitude-pending / NOT-bankable, plus a writhe-blind operator-stencil
> caveat on the eigensolve "zero," plus the open Phase-1 frontier. Do **not** read this as a positive
> forward-prediction; it is a permitted-but-undemonstrated channel.

## 0. TL;DR

The chiral srs / Laves-K4 substrate net (space group $I4_1 32$ #214, point group **432 = O**, chiral,
non-centrosymmetric) **symmetry-PERMITS** a field-free natural **optical-activity** (gyrotropy / natural
circular birefringence / polarization-plane rotation) photon channel — the lowest-order odd-in-$k$ axial
gyration tensor $g_{ijk}=g_0\,\varepsilon_{ijk}$ in the spatial-dispersion constitutive law
$D_i=\varepsilon_0(\varepsilon_{ij}E_j + i\,g_{ijk}k_k E_j)$. The **FORM** is genuinely AVE-distinct:
field-free natural optical activity is **parity-odd**, and QED's vacuum is parity-even ⟹ zero natural OA at
ANY magnitude (a zero-vs-nonzero discriminator, NOT a coefficient comparison). It is a **distinct channel**
from `clm-pp3qwf` (field-INDUCED, even-in-$k$, birefringence COEFFICIENT) and from `clm-yr6tu4`
(even-in-$k$ $(q\ell_{node})^4$ quartic): this one is field-FREE, odd-in-$k$, CIRCULAR.

**But the magnitude is UNDETERMINED and NOT substrate-derived**, by two non-reconciling routes (neither is
the substrate-derived constitutive $g_0$):

1. Engine `def-0pt1ac` (#195): a $\pm75.46°$/node-span ceiling — but a **hand-injected kinematic SO(2)
   twist** riding `ETA_ROT_PER_WRITHE = 1.0` (a tagged engineering scale) × an unpinned apparatus
   `chirality_fraction`. A decree, not a derivation.
2. The static lattice-dynamics / Cosserat Bloch eigensolve: **zero** — but this is a **writhe-blind
   operator-stencil ARTIFACT**, not "the substrate sources zero" (the operators are built from local bond
   directions, and the left/right srs bond-direction multisets are identical, so the operator cannot
   resolve handedness; chirality lives in the ring TOPOLOGY, which this stencil discards).

**VERDICT: symmetry-PERMITTED, AVE-distinct-IN-FORM, magnitude-PENDING, NOT bankable as it stands. Do NOT
promote `def-0pt1ac` to a bankable forward prediction.** The make-or-break OPEN FRONTIER is the deferred,
never-executed Phase-1 **writhe-aware** full vector-TLM derivation, which is what would settle the
substrate-derived $g_0$.

**Consistency-vs-emergence tag:** CONSISTENCY / FORM-class (symmetry permits the form; magnitude
undetermined and not substrate-derived). The discrimination axis is ZERO-vs-NONZERO (parity), not a
coefficient — but AVE has not demonstrated the nonzero side from the substrate, so the chord is not yet
banked.

---

## 1. Symmetry PERMITS the channel

The srs / Laves-K4 net is space group $I4_1 32$ (#214), point group **432 = O** — 24 proper rotations,
0 improper, hence chiral and non-centrosymmetric. This is asserted by executable keepers, not by fiat:

- The $I4_1 32$ (#214), Wyckoff-8a motif is declared at
  [`src/ave/core/chiral_lattice.py:45`](../src/ave/core/chiral_lattice.py) ("I4_1 32 (#214), Wyckoff 8a.
  Native = right-handed enantiomorph").
- The point-group 432 self-symmetry (24 proper / 0 improper) is a passing keeper:
  [`src/tests/test_chiral_lattice_smokes.py:86-93`](../src/tests/test_chiral_lattice_smokes.py)
  (`test_srs_chiral_point_group_432`: `assert proper == 24`, `assert improper == 0`).

**Why 432 is the relevant class.** Point group 432 is one of the 18 (15 non-cubic + 3 cubic) gyrotropic
crystal classes. Among the cubic classes it is the *unique* case with **isotropic** optical activity — the
NaClO₃ / NaBrO₃ textbook case, where the gyration tensor reduces to a single scalar $g_0$ and the optical
rotation is the same along every direction. In the spatial-dispersion constitutive law

$$D_i = \varepsilon_0\left(\varepsilon_{ij}E_j + i\,g_{ijk}\,k_k\,E_j\right),$$

the lowest-order odd-in-$k$ axial gyration tensor permitted by 432 is

$$g_{ijk} = g_0\,\varepsilon_{ijk},$$

i.e. the fully antisymmetric (pseudoscalar-weighted) Levi-Civita form. This is the term that produces a
circular birefringence (left/right circular eigenmodes with different phase velocities) and hence a
rotation of the polarization plane that flips sign with the lattice handedness.

**The achiral control forces $g=0$.** The canonical diamond control net ($Fd\bar3m$, point group $O_h$,
centrosymmetric) is declared at [`src/ave/core/chiral_lattice.py:13`](../src/ave/core/chiral_lattice.py)
("the canonical diamond (engine-'K4', degree-4, achiral) net as the control") with
`handedness="achiral (Fd-3m)"` at `chiral_lattice.py:266`. Inversion symmetry forces every axial
$g_{ijk}$ to vanish: an inversion-symmetric medium cannot carry an odd-in-$k$ pseudotensor. The corpus
states this directly at `chiral_lattice.py:308-309` ("ring writhes ... [vanish] identically for an achiral
(centrosymmetric) net"). So 432 **permits** the channel; $O_h$ **forbids** it — the textbook
symmetry-selection result, reproduced substrate-native.

> **Scope of this section.** "Permits" is a symmetry statement only. Symmetry permitting a tensor component
> does NOT fix its magnitude (or even guarantee it is nonzero in a given microscopic realization) — that is
> §4–§5.

## 2. AVE-distinct IN FORM, not in sourced amplitude

Field-free **natural** optical activity is **parity-odd**: under spatial inversion the gyration
pseudotensor $g_{ijk}$ changes sign, so a medium with unbroken parity has identically zero natural OA. QED's
vacuum is **parity-even** (the photon sector conserves P; the parity-violating weak sector does not couple to
the optical photon at any accessible order). Therefore:

- **QED prediction:** zero natural (field-free) optical activity, at ANY magnitude. This is a genuine zero,
  not a small number — the discriminator is **zero-vs-nonzero**, NOT a coefficient comparison. Verified in the
  companion bench result: [`research/2026-06-20_vacuum-birefringence-bench_result.md:90`](2026-06-20_vacuum-birefringence-bench_result.md)
  — "QED has NO vacuum optical activity. A nonzero rotation that (i) flips sign with the lattice handedness
  and (ii) is zero on an achiral control has **no QED explanation at any magnitude** — a zero-vs-nonzero
  test, not a coefficient-comparison."

- **AVE FORM:** parity-odd, sign-flipping with lattice handedness, achiral-null. This FORM is genuinely
  AVE-distinct — it is structurally on the nonzero side of a zero-vs-nonzero axis that QED is structurally on
  the zero side of.

**Symmetric-standard check, both ways (`consensus-bias-symmetric-standard`):**

- QED gets **no free pass** here: its zero is a genuine structural zero (parity conservation in the optical
  sector), not a hidden fit. So this is not a case of "the SM does the same thing and gets a pass" — the FORM
  asymmetry is real.
- **AVE gets no free pass either:** AVE has demonstrated only that 432 *permits* the nonzero side; it has
  **not** demonstrated the nonzero side *from the substrate*. A permitted-but-unsourced tensor component is
  not a banked prediction. The FORM is distinct; the **sourced amplitude is not in hand** (§4–§5). Headlining
  this as an AVE chord at this stage would be exactly the consensus-bias error in reverse — crediting AVE for
  a derivation it has not done.

## 3. DISTINCT channel from clm-pp3qwf and clm-yr6tu4

This optical-activity channel is a **third, distinct** vacuum-photon discriminator. It must not be conflated
with either of the two already-tracked birefringence channels:

| | Mechanism | $k$-parity | Birefringence type | Field | Status |
|---|---|---|---|---|---|
| **This channel** (`def-0pt1ac`, FORM) | natural gyrotropy $g_0\varepsilon_{ijk}$ | **odd**-in-$k$ | **circular** | field-**FREE** | FORM-permitted, magnitude-pending |
| `clm-pp3qwf` | field-induced index shift COEFFICIENT | even-in-$k$ | linear (par−perp differential) | field-**INDUCED** ($\delta n\propto E^2$) | bankable E-route discriminator |
| `clm-yr6tu4` | $(q\ell_{node})^4$ cubic-harmonic anisotropy | even-in-$k$ | linear / dispersion | field-free dispersion | FORM-class, $\sim$2–3 OOM below bounds |

- **`clm-pp3qwf`** is the field-INDUCED vacuum birefringence COEFFICIENT (AVE $\sim10^6$–$10^7\times$ QED at
  the matched differential observable; the $1.93\times10^7=7.5/\alpha^3$ matched-differential ratio).
  Verified at [`manuscript/ave-kb/vol4/claim-quality.md:387-389`](../manuscript/ave-kb/vol4/claim-quality.md)
  (heading "Vacuum Birefringence Discriminator: COEFFICIENT (AVE $\sim10^7\times$ QED ...)", `id: clm-pp3qwf`).
  It is an **even-in-field, even-in-$k$** index shift ($\delta n\propto E^2$-leading), a *linear* (par−perp)
  birefringence requiring an applied field. **NOTE / drift correction:** the workflow brief shorthand
  "field-INDUCED, even-in-k, LINEAR uniaxial birefringence coefficient" is accurate as to *field-induced*,
  *even-in-k*, *linear*; HEAD describes it specifically as the $E^2$-leading index-shift COEFFICIENT (not a
  "uniaxial" label). The load-bearing distinction from this doc's channel — field-induced vs field-free,
  even-in-$k$ vs odd-in-$k$, linear vs circular — holds exactly.
- **`clm-yr6tu4`** is the $(q\ell_{node})^4$ cubic-symmetry anisotropy (K4 4th-moment cubic harmonic
  $q_x^4+q_y^4+q_z^4$), an **even-in-$k$ QUARTIC** dispersion tell. Verified at
  [`manuscript/ave-kb/vol4/claim-quality.md:1428,1445`](../manuscript/ave-kb/vol4/claim-quality.md)
  ("the first anisotropic invariant is QUARTIC $(q\ell_{node})^4$ ... (clm-yr6tu4)").
  **NOTE:** `clm-yr6tu4`'s canonical leaf is the preferred-frame / emergent-Lorentz cohesive-narrative node
  (`vol1/.../preferred-frame-and-emergent-lorentz.md`); it is *referenced* in vol4/claim-quality as the
  $(q\ell_{node})^4$ anisotropy claim. The even-in-$k$ quartic FORM is the load-bearing distinction and it
  holds.

This channel is the **only** one of the three that is field-FREE, odd-in-$k$, and CIRCULAR — orthogonal to
both. Whether it warrants its own `clm-` node is Grant-call (i), §10.

## 4. The eigensolve "zero" is a WRITHE-BLIND operator-stencil ARTIFACT

> **PROVENANCE FLAG (verify-before-cite).** The eigensolve numbers in this section
> (spec_R − spec_L ≈ 4.4×10⁻¹⁵; the imposed-$\alpha_g=0.3$ positive control with log-log slope 1.000; the
> realization-independent TRS theorem $D(-k)=D(k)^*$) were produced by the 5-agent refute-by-default DERIVE
> lane in-session and are **NOT committed to HEAD** (re-grepped against 2967fcb5: no `per-helicity`,
> `gyration tensor`, `g_ijk`, `odd-in-k`, or `circular_split` driver exists in the tree). They are reported
> here as **workflow findings with stated provenance**, NOT as cited HEAD file:line results. The HEAD
> chiral-dynamics module [`src/ave/core/chiral_lattice_dynamics.py`](../src/ave/core/chiral_lattice_dynamics.py)
> carries only the *scalar* TLM-dispersion eigensolve (Smoke A, V-sector, `measure_dispersion`), not the
> per-helicity circular-split Bloch operator these findings used. The writhe values (§5) and the design-doc
> Phase-1 record ARE on HEAD and are cited as such.

**The claim being deflated.** A static lattice-dynamics / Cosserat Bloch eigensolve of the chiral srs net
returns a polarization splitting of **zero**. The tempting (and WRONG) reading is "the substrate sources
zero optical activity." Per the `structural-null-needs-stencil-lens` discipline, a coupling=0 null from a
non-substrate-native operator stencil validates a *disabled-flag / blind discretization*, not physics.

**Why this zero is an artifact, not physics.** The static lattice-dynamics and Cosserat Bloch operators are
assembled from **local bond directions** $\{\hat d,\,k\cdot d\}$ at each node. But the left and right srs
enantiomorphs have **identical bond-direction multisets** — the set of bond vectors is the same; only the
*topological connectivity* (how the bonds thread into closed circuits) differs. The workflow measured
$\text{spec}_R - \text{spec}_L \approx 4.4\times10^{-15}$ (machine zero): the operator literally cannot
resolve handedness, because handedness is not in its inputs. The chirality lives in the **ring TOPOLOGY** —
the writhe pseudoscalar of the net's shortest circuits, which is $\pm0.04087$ (sign-flipped between
enantiomorphs, zero on diamond; §5) — and the local-bond-direction stencil **discards** that topological
content.

**The probe is alive (positive control).** The workflow imposed a synthetic gyration $\alpha_g=0.3$ directly
into the Bloch operator and recovered a real odd-in-$k$ circular split: a per-helicity splitting that scales
with a log-log slope of **1.000** (linear-in-$k$, the gyrotropic signature) and is reciprocal /
TRS-preserving. So the eigensolve *can* see a gyration when one is present in the operator — the zero is a
**sourcing-by-this-stencil** result, NOT a substrate no-go.

**The TRS theorem fixes the WRONG observable, not a no-go.** For ANY real-force-constant reciprocal lattice,
time-reversal symmetry forces $D(-k) = D(k)^*$ (realization-independent). This makes the **sorted-band**
$\omega^2(k) - \omega^2(-k)$ **theorem-forced even** — so the sorted-band even-ness is the WRONG observable
to test for optical activity (it would be zero even in a medium with real gyrotropy). The RIGHT observable is
the **per-helicity circular split** (left- vs right-circular eigenmode phase velocity), which is exactly what
the $\alpha_g=0.3$ positive control resolves. Reporting "the bands are even, so there is no optical activity"
would be the writhe-blind error compounded by a wrong-observable error.

**Bottom line of §4:** the eigensolve zero is a writhe-blind operator-stencil artifact. It is NOT evidence
that the substrate sources zero optical activity, and it must NOT be recorded as such. It is, at most, the
statement "a local-bond-direction stencil that discards ring topology cannot source the topological
gyration" — which is a statement about the stencil, not the physics. A writhe-aware operator is required to
settle the substrate-derived $g_0$ (§7).

## 5. Magnitude is UNDETERMINED — two non-reconciling numbers, neither substrate-derived

There are two numbers in the corpus/workflow for this channel's magnitude. **Neither is the substrate-derived
constitutive coefficient $g_0$, and they do not reconcile — because they are not "the same physics in two
languages."** One is a decree; the other is a writhe-blind probe.

**(a) Engine `def-0pt1ac` (#195): a $\pm75.46°$/node-span CEILING — a hand-injected kinematic decree.**

- Adjudicated meaning + value verified at
  [`manuscript/ave-kb/common/vocabulary-register.md:523,526`](../manuscript/ave-kb/common/vocabulary-register.md)
  (`<!-- id: def-0pt1ac -->`; "the chiral srs-grid result $\pm75.46°$/unit ([#195])"). Canonical-home
  `engine-capability-map.md:44` ("optical-activity $\pm75.46°$/unit, [#195]").
- The bench result phrases the same number per-length:
  [`research/2026-06-20_vacuum-birefringence-bench_result.md:88`](2026-06-20_vacuum-birefringence-bench_result.md)
  ("$\pm75.462°$/node-span", a "full-chirality CEILING").
- **Mechanism = a hand-injected kinematic SO(2) twist, not a derived coupling.** The engine applies a 2×2
  rotation of the two transverse field components, with rotation angle
  `ETA_ROT_PER_WRITHE × mean_ring_writhe`, where `ETA_ROT_PER_WRITHE = 1.0` is an **explicitly tagged
  engineering choice** (not substrate-derived): see
  [`src/ave/core/chiral_lattice_vector.py:27`](../src/ave/core/chiral_lattice_vector.py) (`ETA_ROT_PER_WRITHE
  = 1.0`, comment: "Tagged engineering choice: sets the optical-activity (gyrotropy) rate scale ... NOT a
  micro-rotation DOF"). The 2×2 SO(2) twist is applied at `chiral_lattice_vector.py:48-61`.
- The ceiling is further multiplied by an **unpinned apparatus `chirality_fraction`** (how much of the bare
  lattice chirality a real bench actually presents to a probe): bench result
  `2026-06-20_vacuum-birefringence-bench_result.md:88` ("a bench realizes a fraction `chirality_fraction`
  of it (apparatus-set, **unpinned**)"). So even the engine number is `(engineering-scale) × (writhe) ×
  (unpinned apparatus factor)` — a decree riding two un-derived inputs.

**(b) The static eigensolve: ZERO — a writhe-blind artifact (§4).** Not a substrate no-go; the operator
stencil cannot resolve handedness because it discards the ring topology where the chirality lives.

**These do not adjudicate against each other.** (a) is a kinematic decree (a chosen rotation rate × a
geometric source × an apparatus knob); (b) is a writhe-blind probe returning machine-zero by construction.
Neither computes the substrate-derived constitutive $g_0$ from the field equations on the chiral net. There
is **nothing to reconcile** between a decree and a blind probe — and crucially, there is no
substrate-derived number on the table at all.

**The writhe source IS on HEAD and IS real** (it is the geometric pseudoscalar that a writhe-aware operator
would couple to): live re-run on HEAD 2967fcb5 —

```
srs-right: writhe_mean = -4.08672e-02  (std 2.7e-09, 36 rings, girth [10,10])
srs-left : writhe_mean = +4.08672e-02  (std 2.2e-09, 35 rings, girth [10,10])
diamond  : writhe_mean = +0.00000e+00  (std 0,        4 rings, girth [4,4])
```

matching the design-doc record `+4.0867e-02` / exact sign-flip / `0.0` on diamond
([`research/2026-06-11_genesis-v9-chiral-lattice_design.md:300`](2026-06-11_genesis-v9-chiral-lattice_design.md)).
The writhe is a genuine reflection-odd substrate source (`def-wr1th3`, SOLID). What is missing is the
substrate-derived *coupling* of that source into a propagating-field rotation rate ($g_0$) — that is the
Phase-1 deliverable, never executed (§7).

## 6. VERDICT

**Symmetry-PERMITTED, AVE-distinct-IN-FORM, magnitude-PENDING, NOT bankable as it stands.**

- **PERMITTED:** point group 432 = O permits the isotropic gyration tensor $g_0\varepsilon_{ijk}$; $O_h$
  diamond forbids it. (§1)
- **AVE-distinct IN FORM:** parity-odd natural OA is structurally nonzero-side where QED is structurally
  zero-side (zero-vs-nonzero, not a coefficient). But AVE has demonstrated only the *permission*, not the
  *sourcing*. (§2)
- **DISTINCT channel:** field-free, odd-in-$k$, circular — orthogonal to `clm-pp3qwf` (field-induced,
  even-in-$k$, linear) and `clm-yr6tu4` (even-in-$k$ quartic). (§3)
- **Magnitude PENDING:** the eigensolve zero is a writhe-blind stencil artifact (§4); the engine
  $\pm75.46°$ is a hand-injected kinematic decree on a tagged engineering scale × unpinned apparatus factor
  (§5). No substrate-derived $g_0$ exists. (§4–§5)
- **NOT bankable:** **do NOT promote `def-0pt1ac` to a bankable forward prediction.** Its magnitude is an
  engineering decree, not a derivation; banking it would be substitution-not-retraction (crediting a
  derivation that has not been done).

This is a clean refute-by-default DEFLATION: the channel is real *in form* but its bankable content (a
substrate-derived, sign-correct, magnitude-correct forward prediction) is **not yet established**. The
discipline result is: keep the FORM as a flagged FORM-class object, do not headline it as a chord, and gate
the bankability on the Phase-1 derivation (§7).

## 7. OPEN FRONTIER (make-or-break)

**The deferred, never-executed Phase-1 WRITHE-AWARE full vector-TLM derivation is what would settle the
substrate-derived $g_0$ — and hence whether this channel is bankable.**

- The Phase-1 deliverable is named in the design doc but **never executed**:
  [`research/2026-06-11_genesis-v9-chiral-lattice_design.md:89-103`](2026-06-11_genesis-v9-chiral-lattice_design.md)
  ("The dynamical polarization-rotation it sources (frame parallel-transport / full vector-TLM) is the
  **Phase-1** deliverable — the substrate-native locus of optical activity named but never executed in
  canon") and `:285-291` (the writhe measurement is the Phase-0 *source*; the polarization-plane angle
  $\Delta\theta_{pol}/L$ is the Phase-1 *response*).
- The first parallel-transport attempt was **non-converged** and is recorded honestly at design-doc
  `:278-280`: "found **non-converged at Phase-0**: a discrete scalar walk through a finite periodic
  supercell *wanders*, the net along-axis displacement is non-monotonic, and the measured rate is sensitive
  to box size and step count (it even sign-flipped between `L=6` and `L=8`)." A magnitude that sign-flips
  with supercell size is not a converged constitutive coefficient — it is the symptom of a probe that has
  not yet captured the topological coupling.
- **What Phase-1 must do:** build a writhe-AWARE operator (one whose Bloch / transport stencil retains the
  ring-topology content the local-bond-direction stencil discards, §4), propagate a transverse vector field,
  and measure a CONVERGED per-length circular split / polarization-rotation rate that (i) flips sign with
  enantiomorph, (ii) is zero on the diamond control, and (iii) is box-size-independent. That converged rate
  IS the substrate-derived $g_0$. Until it exists, the magnitude is pending and the channel is not bankable.

**Separately open:** whether the cosmic-chirality freeze-in ($\hat\Omega_{\text{freeze}}$) injects a
**complex / TRS-odd** constitutive term. The static eigensolve **cannot** settle this — a real-force-constant
lattice is TRS-even by theorem ($D(-k)=D(k)^*$, §4), so any TRS-odd contribution must come from a
freeze-in-induced complex term that the static, real-operator probe is structurally blind to. This is a
distinct open question from the Phase-1 $g_0$ derivation and should be tracked separately.

## 8. SEDUCTIVE-NARRATIVE GUARD (held)

**Do NOT map this channel onto the live cosmic-birefringence anomaly. That is OVER-REACH, and it is held
out as a separate flagged conjecture, never a corpus map.**

There is a tempting narrative: "AVE predicts vacuum optical activity → the Planck/SPT cosmic-birefringence
anomaly ($\beta\sim0.3°$) is AVE's signature." This is seductive and wrong on the mechanism:

- AVE's actual cosmic observable #5 is **E/B polarization DECOUPLING** from *asymmetric crystallization*
  ($K/G \neq 2$), verified at
  [`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:65`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)
  ("E/B polarization decoupling | Same axis IF asymmetric crystallization ($K/G \neq 2$)").
- A uniform **parity-rotation $\beta$** (a single rotation of the polarization plane across the whole sky,
  which is what the cosmic-birefringence anomaly reports) is a **DIFFERENT mechanism** than E/B decoupling.
  The corpus contains **no derived cosmic-$\beta$** — there is no chain from $g_0$ (which itself is not yet
  derived, §5–§7) to a sky-averaged rotation angle.
- Mapping the two would be a coincidence-magnet narrative bridge across two unestablished links (no derived
  $g_0$, no derived cosmic-$\beta$). It is held as a SEPARATE, explicitly-flagged conjecture — **never**
  written into the corpus as a map, and **not** counted toward this channel's status.

## 9. Anchor verification table (verify-before-cite, against HEAD 2967fcb5)

Every anchor in the workflow brief was re-confirmed against worktree HEAD `2967fcb5` (off `origin/main`).
Drift / provenance notes are explicit.

| # | Anchor (as briefed) | HEAD result | Status |
|---|---|---|---|
| 1a | `src/ave/core/chiral_lattice.py:45` — I4_1 32 (#214) Wyckoff 8a | line 45 = "I4_1 32 (#214), Wyckoff 8a. Native = right-handed enantiomorph." | **PASS** |
| 1b | `src/tests/test_chiral_lattice_smokes.py:86-93` — 432, 24 proper / 0 improper | `test_srs_chiral_point_group_432`, `assert proper==24`, `assert improper==0` | **PASS** |
| 1c | `chiral_lattice.py:13` — achiral diamond control | line 13 = "the canonical diamond (engine-'K4', degree-4, achiral) net as the control" (`handedness="achiral (Fd-3m)"` at :266; inversion-null prose :308-309) | **PASS** |
| 2 | `research/2026-06-20_vacuum-birefringence-bench_result.md:90` — zero-vs-nonzero discriminator | line ~90: "no QED explanation at any magnitude — a zero-vs-nonzero test, not a coefficient-comparison" | **PASS** (in range; the exact sentence sits ~:90, the "$\pm75.462°$/node-span" ceiling at :88) |
| 3a | `manuscript/ave-kb/vol4/claim-quality.md:387-389` — clm-pp3qwf | heading at :388, `<!-- id: clm-pp3qwf -->` at :389; coefficient $\sim10^6$–$10^7\times$ QED ($1.93\times10^7=7.5/\alpha^3$ at :399) | **PASS** (see note) |
| 3b | clm-yr6tu4 — even-in-$k$ $(q\ell_{node})^4$ quartic | EXISTS; $(q\ell_{node})^4$ at vol4/claim-quality.md:1428,1445; canonical leaf is vol1 preferred-frame | **PASS** (see note) |
| 4 | eigensolve: spec_R−spec_L=4.4e-15; $\alpha_g=0.3$ slope 1.000; TRS $D(-k)=D(k)^*$ | **NOT ON HEAD** — no `per-helicity`/`gyration tensor`/`g_ijk`/`odd-in-k`/`circular_split` driver in tree (re-grepped). HEAD has only scalar TLM dispersion (`chiral_lattice_dynamics.py:measure_dispersion`). | **DRIFT — in-session workflow product, NOT a HEAD cite.** Documented as workflow finding with provenance flag (§4). |
| 5a | `def-0pt1ac` ±75.46 deg/node-span; `vocabulary-register.md ~:522-534` | `<!-- id: def-0pt1ac -->` at :523 (not :522); "$\pm75.46°$/unit ([#195])" at :526; verification at :534 | **PASS w/ minor drift** (id marker at :523 not :522; value "/unit" in vocab-register, "/node-span" in bench result :88 — both cited correctly) |
| 5b | `ETA_ROT_PER_WRITHE=1.0` tagged engineering, `chiral_lattice_vector.py:27`; 2×2 rot ~:48-61 | line 27 = `ETA_ROT_PER_WRITHE = 1.0` ("Tagged engineering choice"); SO(2) 2×2 twist at :48-61 | **PASS** |
| 7a | design doc `:89-103` Phase-1 writhe-aware vector-TLM never executed | :89-103 = "Phase-1 deliverable — ... named but never executed in canon" | **PASS** |
| 7b | design doc `:285-291` writhe measurement | :285-291 = mean ring-writhe measurement, native/mirror/diamond | **PASS** |
| 7c | design doc §3 non-converged parallel-transport, sign-flip L=6 vs L=8 | :278-280 = "non-converged at Phase-0 ... it even sign-flipped between L=6 and L=8" (note: brief said "L=6 vs L=8"; design doc also notes L=8 implicitly — text reads "L=6 and L=8") | **PASS** |
| 8 | `omega-freeze-cosmic-grain-cascade.md:65` — cosmic obs #5 = E/B decoupling at K/G≠2 | line 65 = "E/B polarization decoupling | Same axis IF asymmetric crystallization ($K/G \neq 2$)" | **PASS** |
| — | writhe values ±0.04087, sign-flip, diamond 0 | live re-run on HEAD: srs-right −4.08672e-02, srs-left +4.08672e-02, diamond 0.0 exactly | **PASS** (live-verified) |
| — | `def-0pt1ac` / `def-wr1th3` clm_cross_links empty (Grant-call i basis) | `claims.jsonl`: both `clm_cross_links: []`; `def-0pt1ac` SOLID + `open_ambiguity:true`; `def-wr1th3` SOLID | **PASS** |

**Drift notes:**
- **Item 4 is the load-bearing drift:** the eigensolve circular-split / TRS-theorem / $\alpha_g$-positive-control
  numbers are **in-session 5-agent workflow products, not committed to HEAD**. They are documented as workflow
  findings (§4) with an explicit provenance flag, NOT cited as HEAD file:line. The *interpretation*
  (writhe-blind stencil → the zero is an artifact, not a substrate no-go) is the durable finding and is
  consistent with the on-HEAD facts (identical bond-direction multisets; topology-only writhe; scalar-only
  HEAD eigensolve). If those drivers are to be cited canonically, they must first be committed.
- **Item 3a:** clm-pp3qwf body on HEAD describes the field-induced birefringence *COEFFICIENT* ($E^2$-leading
  index shift), accurately matching "field-induced, even-in-k, linear"; the brief's "uniaxial" label is not a
  HEAD term — the load-bearing distinctions hold.
- **Item 5a:** `def-0pt1ac` id marker is at vocabulary-register.md **:523** (brief said ~:522); "/unit" in
  vocab-register vs "/node-span" in the bench result — both phrasings cited at their correct homes.

## 10. Canonical-propagation Grant-calls (SURFACED, not executed)

These are **surfaced for Grant adjudication only**. This PR does NOT mint any `clm-` node and does NOT edit
`def-0pt1ac`'s record — research-doc only, per the lane discipline (implementer surfaces empirical findings;
canonical landings are Grant-adjudicated / auditor-landed).

**(i) Mint-or-not a FORM-class `clm-` node for this channel?**
Currently both `def-0pt1ac` and `def-wr1th3` carry empty `clm_cross_links` (verified in `claims.jsonl`):
there is no claim node for the optical-activity *prediction*, only the vocabulary definitions. A new node
would be tagged **FORM-class / magnitude-pending** and cross-linked to `def-0pt1ac` (engine result),
`def-wr1th3` (writhe source), `clm-pp3qwf` (the distinct field-induced coefficient), and `clm-yr6tu4` (the
distinct even-in-$k$ quartic). **Recommendation:** *lean yes* — the FORM is genuinely distinct from the two
existing birefringence nodes and currently has no claim-register home, so it is invisible to subtree-claim
tracking; but it MUST be minted with the magnitude-pending / not-bankable status front-loaded (not as a
forward prediction). **Grant decides.** Do NOT mint in this PR.

**(ii) Should `def-0pt1ac`'s record carry an explicit "magnitude = engineering decree, NOT substrate-derived
→ not bankable" flag?**
The current `def-0pt1ac` status is "SOLID" and headlines "$\pm75.46°$/unit ([#195]) ... validated." That
SOLID/validated framing is true for the *locked optical-activity sense and the lossless-rotation engine
mechanism*, but it does NOT distinguish "the FORM is validated" from "the MAGNITUDE is a hand-injected
`ETA_ROT_PER_WRITHE` engineering decree × unpinned `chirality_fraction`." A reader could mistake the
$\pm75.46°$ ceiling for a derived forward prediction. **Recommendation:** *lean yes* — add a one-line flag to
the `def-0pt1ac` record (and/or `engine-capability-map.md:44`) reading approximately: "magnitude
$\pm75.46°$/unit is an engineering decree (`ETA_ROT_PER_WRITHE`, tagged) × unpinned apparatus chirality
fraction — NOT substrate-derived, NOT bankable; the substrate-derived $g_0$ is the open Phase-1 deliverable."
**Grant decides.** Do NOT edit `def-0pt1ac` in this PR.

**(iii) Should the Phase-1 writhe-aware vector-TLM derivation be commissioned?**
This is the make-or-break (§7): it is the only route to a substrate-derived $g_0$, and hence the gate on
whether this channel becomes a bankable forward prediction. The first parallel-transport attempt was
non-converged (sign-flipped L=6 vs L=8); a writhe-AWARE operator (retaining the ring-topology content the
local-bond-direction stencil discards) is the design requirement. **Recommendation:** *lean yes, but scope it
as a discrete chartered workstream* with the convergence acceptance criteria stated up front (sign-flip with
enantiomorph + diamond-null + box-size-independence). **Grant decides** whether to commission now or hold.

---

### Provenance / discipline footer

- Skills applied: `verify-before-cite` (every anchor re-grepped against HEAD 2967fcb5; item-4 drift flagged),
  `consensus-bias-symmetric-standard` (§2 both-ways check — QED's zero is genuine, AVE's nonzero is
  un-sourced), `ave-discrimination-check` (zero-vs-nonzero axis vs coefficient; distinctness from
  clm-pp3qwf/clm-yr6tu4), `flag-don't-fix` (item-4 not-on-HEAD surfaced, not papered over; def-0pt1ac
  SOLID-vs-magnitude tension surfaced for Grant), `structural-null-needs-stencil-lens` (§4 writhe-blind
  stencil = the eigensolve zero is an artifact), `ave-canonical-source` (KB leaves + claims.jsonl as
  truth-source).
- Worktree: `/tmp/wt-chiral-oa`, branch `analysis/chiral-srs-optical-activity`, off `origin/main` @ `2967fcb5`.
- This doc is research substrate only. No `clm-` minted, no `def-0pt1ac` edit. Canonical-propagation
  Grant-calls (i)/(ii)/(iii) above are surfaced, not executed.

