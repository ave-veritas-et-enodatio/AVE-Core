# NOTE — The AVE chart instrument: a doubly-normalized Smith chart for the vacuum circuit

**Built:** 2026-08-24
**Lane:** implementer (engineering/infrastructure; research-tier, no canon edit, nothing minted)
**Branch:** `infra/2026-08-24-ave-chart-instrument` (off `origin/main`)
**Module:** [`src/ave/viz/ave_chart.py`](../src/ave/viz/ave_chart.py) · **Tests:** [`src/tests/test_ave_chart.py`](../src/tests/test_ave_chart.py) · **Driver:** [`src/scripts/vol_4_circuit/ave_chart_sweeps.py`](../src/scripts/vol_4_circuit/ave_chart_sweeps.py)
**Figures:** `research/figures/2026-08-24-ave-chart-instrument/` (+ `ave_chart_sweeps_metrics.json`)

---

## §0 — SECTOR HEADER

| Axis | Declaration |
|---|---|
| **MODE** | Reflection-coefficient (Op3) plane of the vacuum circuit; the canonical locus drawn is the A1/mass-sector tank trajectory $Z_{core}=Z_0\sqrt{S}$; rim-pole annotations follow the PR#260 sector discipline (§3 below). No charge-sector content is asserted. |
| **REGIME** | The instrument is regime-free plotting machinery; the loci it draws span cold ($A=0$, matched) to saturated ($A\to1$, the wall). No dynamical claim. |
| **CLASS** | **Nothing minted.** No `clm-`/`def-` node authored, no solidity moves, no KB leaf edited. Engineering tool only. |

## §1 — What this IS (and is not)

An **engineering plotting instrument**: a reusable module that renders the reflection-coefficient
disk with the vacuum medium's own datasheet constants baked into the normalization, so substrate
operating points, bias trajectories, frequency loci, and envelope occupancies can be read the way
an RF engineer reads a device on a Smith chart. It packages ALREADY-CANONICAL content
(the View-3 plot of `cvr_ee_sweep.py`, previously a one-off figure) into a tested library
plus a sweep driver. **No physics is minted**: every analytic anchor is a quotation of an
existing canonical leaf, cited below, and everything the instrument adds beyond those anchors is
tagged as an engineering choice on the figure and in the docstring.

### The four added axes (relative to the existing static View-3 figure)

1. **Reusable base chart** — unit disk + standard Smith grid, centre annotated as the matched
   cold-lattice reference ($Z_0$), the $1-\alpha$ rim band shaded from `ave.core.constants.ALPHA`
   (never hard-coded), rim poles annotated under the PR#260 sign-selector discipline.
2. **Bias-trajectory axis** — $\Gamma(A)$ in three forms (canonical core + the two graded
   two-junction constructions J/B), drawable on any chart axes.
3. **Frequency axis** — the two-junction composite's $\Gamma(\theta)$ locus
   (minimal ABCD transfer matrix; $\theta=\omega\ell/c_{bond}$), cold or biased.
4. **Occupancy axis** — an envelope orbit $A(t)\mapsto\Gamma(A(t))$ as a chart trace with dwell
   density (hexbin + 1D histogram); the orbit is caller-supplied.

## §2 — The double normalization and the invariance reading

The chart is normalized **twice by the medium's own datasheet constants**: impedance by $Z_0$
(the chart centre IS the matched cold lattice) and amplitude by $V_{yield}$ (the Axiom-4
saturation scale, entering through $S(A)=\sqrt{1-A^2}$).

The instrument's one structural statement — adversarially verified this session's lane, and
**tested numerically, not asserted** (`test_ave_chart.py::TestUniformBiasInvariance`, atol
$10^{-14}$ across 400 amplitudes; driver-computed max deviation $5.6\times10^{-17}$) — is:

> Under a UNIFORM bias every impedance in a junction network rescales by the same $\sqrt{S}$,
> and the bilinear map $\Gamma=(z_2-z_1)/(z_2+z_1)$ cancels a common rescaling — so the bare
> $z=3$ vertex reflection $\Gamma=(2-z)/z=-1/3$ is EXACT at all orders of a uniform bias; only a
> DIFFERENTIAL bias splits it. **The chart is blind to uniform medium changes** — the
> self-cancellation principle drawn as geometry.

This is a property of the bilinear map, i.e. of the instrument's coordinates — a consistency
statement, not a new physics result.

## §3 — Sector discipline at the rim (binding on every chart annotation)

Per the PR#260 B3-DEGENERATE ruling (Grant-ratified; quoted in the Rule-12 note of
[`cvr-reflection-smith.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md) §2):
the "magnetic branch $\mu_{eff}\to0$" labelling of the $\Gamma\to-1$ wall is the chirality/spin
**SIGN-selector** ($\mu$-first $\Rightarrow\Gamma=-1$ vs $\varepsilon$-first
$\Rightarrow\Gamma=+1$ are spin-conjugate), MUTE on the mass sector; the mass-cage is the A1
longitudinal bulk short ($Z_{bulk}\to0\Rightarrow\Gamma_{bulk}=-1$); the fork is DEGENERATE on
equilibrium observables ($Z=Z_0\sqrt S$, $|\Gamma|=1$ both ways). Accordingly the instrument's
rim annotations **never** say "the magnetic wall" and never cross-wire confinement into the
charge sector — this is enforced in `base_chart()`'s docstring and annotation text.

## §4 — PARK COMPLIANCE (binding)

The CP¹ / one-chart-per-sector **ontology** canonization is Grant-PARKED:
[`_orchestration/open-items/2026-08-18-smith-chart-cp1-canonization.md`](../_orchestration/open-items/2026-08-18-smith-chart-cp1-canonization.md), re-open condition quoted verbatim:

> **Re-open condition:** an engine lane actually wants the dual-sector Smith chart as a live
> instrument (the old toolkit build-order question). Until then this item is the parking
> spot, not a request for a ruling.

**This build complies with the park.** It is the INSTRUMENT — plotting machinery, an
engineering deliverable — and mints no ontology claim: no CP¹ identification, no
one-chart-per-sector doctrine, no canonical leaf touched. **Whether this build itself trips the
re-open condition** (is a chart-sweep driver "an engine lane wanting the chart as a live
instrument"?) **is GRANT'S ruling, not this lane's** — the park item carries a dated note
recording exactly that (same branch).

## §5 — Per-figure gallery (with receipts)

All figures: white background via `ave.viz.style.apply()`, Okabe-Ito palette, honest
colorbars/axes with units, legends outside the data, no on-figure titles
(smoke-tested in `test_ave_chart.py`).

| Figure | What it shows | Receipt(s) |
|---|---|---|
| `fig1_three_form_traces` | The walk picture: core ($0\to-1$), J ($-1/3\to-1$), B ($-1/3\to+1$ through the matched crossing at $A=\sqrt{15}/4$) on one chart + $\Gamma$-vs-$A$ panel. J/B drawn at annotated ±0.035 Im offsets (visibility only; all three loci are real-axis runs). | Core locus + endpoints: [`cvr-reflection-smith.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md) §2. Vertex $-1/3$: [`translation-circuit.md:189`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md) (`a COUNTING fact`). Rim band: §3 of the same leaf, $|\Gamma|=\sqrt{1-\alpha}$. |
| `fig2_cold_frequency_locus` | Cold $\Gamma(\theta)$ of the bond-between-two-$z{=}3$-junctions composite ($Z_0$ line, $Z_0/2$ ends); $\theta=0$ gives $\Gamma=-3/5$ (both junction pairs in parallel). | Composite construction documented in `two_junction_gamma()`; junction arms per the :189 counting fact; **isolated/incoherent scoping** per the same line's T4 fork close. |
| `fig3_graded_family` | $\Gamma(\theta,A)$ family: the composite biased (line+ends) against a cold feed collapses toward the $\Gamma=-1$ rim. | Same anchors as fig2 + the $\sqrt{S}$ impedance scaling of `cvr-reflection-smith.md` §2. |
| `fig4_differential_split` | Uniform bias pins $-1/3$ exactly (computed max deviation $5.6\times10^{-17}$); the differential forms J/B split; B crossing marked at $\sqrt{15}/4$. | §2 above (this session's adversarially-verified lane); counter-arm in the same figure (the split is real when the bias is differential). |
| `fig5_occupancy_demo` | Envelope orbit $A(t)=0.55+0.42\sin t$ → chart dwell hexbin + 1D dwell histogram (turning-point peaks). | **UNDERIVED-CHOICE demo orbit**, tagged on the figure itself; locus form = canonical core. |

## §6 — Specific Non-Claims and Caveats

- **The two-junction composite's terminations are an underived engineering
  choice:** the far junction arms are modeled as reflectionless semi-infinite
  $Z_0/2$ loads (no lattice back-reflection) — the isolated-junction reading,
  declared in the `two_junction_gamma` docstring and repeated here because a
  Non-Claims block owes every such choice: the in-lattice (Bethe-tree) closure
  differs, per the smith-annulus result doc's scoping.

- **No ontology.** Nothing here canonizes (or argues for) the CP¹ reading or a
  one-chart-per-sector doctrine; the park (§4) stands untouched, and the re-open ruling is
  reserved to Grant.
- **The occupancy orbit $A(t)$ is a demo.** An illustrative envelope chosen to sweep a wide
  chart arc — not a derived substrate trajectory. Deriving a physical $A(t)$ is engine-lane
  work.
- **Forms J and B carry an underived side-assignment.** Which side of the junction the bias
  lands on (junction-arms vs feed-bond) is an engineering choice of the construction, tagged in
  both docstrings and in the figure legends. Neither form is asserted as the substrate's
  graded-bias geometry.
- **The vertex floor is scoped.** $\Gamma=(2-z)/z=-1/3$ is the bare, isolated, per-vertex /
  incoherent reading ([`translation-circuit.md:189`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md));
  in-band collective carriers homogenize it (~0.12 of the incoherent value, T4 fork close, same
  line). The two-junction composite and the J/B loci inherit this scoping.
- **The three-form question is an OPEN Grant walk.** Which (if any) of core/J/B is the right
  picture for a graded-bias vertex — and whether the composite is the right minimal frequency
  object — is a walk-the-picture-first item for Grant, not something this note adjudicates.
- **The $1-\alpha$ rim band is a Class-B value-level echo**, not an emergence readout
  (`cvr-reflection-smith.md` §7, the exponent-defect bullet — *"anchored to the per-cycle leak (α=1/Q, clm-rtdmsn)"*); the instrument shades it as the canonical
  annotation it is, owned by the $\alpha=1/Q$ leak (clm-rtdmsn) — cited as identity, not
  derivation.
- **The dual-sector caveat is inherited, not resolved.** `cvr-reflection-smith.md` §7
  (INVARIANT-S2 Q1=B): the transverse-T2 wall is a distinct impedance belonging on its own
  chart; this instrument draws the one canonical A1-tank locus and takes no position on the
  per-sector chart question (that IS the parked ontology).

---

## §7 — Means-test register (what validates this instrument, and against what)

Per the means-test discipline: each row names the target, the independent
route, and what a failure would mean. Classes A–B validate the INSTRUMENT
(machinery); C is the one that would test PHYSICS.

| class | test | independent route | status |
|---|---|---|---|
| **A — textbook EE** | quarter-wave transformer ($z_t^2/z_{load}$), half-wave identity, VSWR=2 ↔ \|Γ\|=1/3 ↔ z∈{2, ½}, constant-r circle geometry (center r/(r+1), radius 1/(r+1)), series-RLC locus = constant-r circle | closed-form Pozar-class identities, framework-independent | **RUN — `TestTextbookMeansTests`, 5 fixtures, pass.** A failure here is an instrument bug, never physics |
| **A′ — internal canon receipts** | Γ(A₀) endpoints (0 → −1), FORM J (−1/3 → −1), B matched crossing √15/4, rim band √(1−α) from `ave.core.constants`, uniform-rescale invariance, −3/5 DC / −3/7 quarter-wave | canon leaves + hand derivation + independent ABCD chain (challenge lens: 35 checks, ≤3.4e-16) | **RUN** (19 base tests + challenge round) |
| **B — cross-solver** | the two-junction composite's Γ(ω) and the graded loci, measured in **ngspice** on the exported netlist and overlaid on fig 2/3 — same objects, two independent computational routes (transfer matrix vs MNA) | the R56-ratified Phase-1 SCX exporter (`2026-08-24_solver-crosscheck-phase1-brief.md`); the two-junction fixture is a natural first netlist target | **PLANNED — rides the Phase-1 satellite.** Divergence = a bug in one route; agreement = the instrument's loci carry solver-grade trust |
| **C — engine time-domain (the physics one)** | launch a pulse in the in-tree scalar TLM engine at a REGION GRADED by the kernel; measure the reflected amplitude vs grading level; overlay the measured Γ(A) on the three drawn forms | the engine's own dynamics — no chart machinery in the loop | **DISPATCHED (Grant, 2026-08-24, verbatim: *"go on C"*).** Lane: capability/prior-art pulls → FROZEN prereg (author firewalled from results; config-grep vs the energize-LOCK + #415/#417 closed-negative signatures) → cold-sanity-gated run over the three graded configurations → 3-lens adversarial verify. Result lands as its own research pair via reviewed PR. This is the J/B/taper fork's substrate adjudication: the lattice itself draws whichever locus is real. A prereg (challenge-canonical-negative config-grep incl.) is owed before any run |
| **D — material analog (shape-class only)** | a real varactor's Γ(V_bias) locus vs the kernel-shaped trajectory | bench LCR / VNA measurement | **FENCED — PONDER-05 per-node-conflation rule: material analogs test kernel SHAPE, never vacuum values.** Recorded so nobody promotes it past shape-class |

The register's honest summary: A and A′ are green; B is bought already (it
rides a lane Grant has ratified); **C is the only row that can produce a
physics verdict**, and it doubles as the side-assignment fork's resolution —
per the substrate-adjudicates-forks discipline, preferable to ruling J/B/taper
by fiat.
