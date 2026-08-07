# LC-1 — ONE-SPEED (multi-messenger) — RESULT: the detected messengers are at $c$ exactly and structurally; the superluminal channel is real, is forced by the SAME modulus that sets $c$, and is invisible to this comparator by five decades of band

**Date:** 2026-08-06 · **Branch:** `research/lc1-one-speed` · **Arc:** Lorentz-compliance, LC-1 (lead)
**Pre-registration (frozen ALONE, before any derivation text, driver code or number existed):**
[`2026-08-06_lc1-one-speed_prereg-FROZEN.md`](2026-08-06_lc1-one-speed_prereg-FROZEN.md) at commit
`992bb5a60230e66f8dd9181d9b3942cdc2b89593`.
**Driver:** [`research/drivers/lc1_one_speed_check.py`](drivers/lc1_one_speed_check.py) →
[`research/drivers/lc1_one_speed_results.json`](drivers/lc1_one_speed_results.json)
**Number gate:** [`research/drivers/lc1_one_speed_number_check.py`](drivers/lc1_one_speed_number_check.py),
wired into `make verify`, with a mutation receipt.
**Class:** DERIVATION-ONLY (Tier-2 at adjudication). Engine `src/ave` byte-untouched, imported
READ-ONLY for constants. **Mints no `clm-`/`def-`; edits no KB leaf, no register, no falsification
ledger, no ruling record; changes no solidity.** SVA v0.2-pilot pass.

---

## REGIME HEADER (restated at the point of reading)

**MODE** — far-field linear wave propagation between two astrophysical events, read as a two-receiver
delay measurement on a lossless multi-channel medium. **REGIME** — Regime-I cold-linear vacuum,
small-signal, $A \ll 1$, $S(A) = 1$ on the entire propagation path. **PHASE-STATE** — cold,
unsaturated. **The SOURCE is not cold** and every statement about source coupling is inherited, not
derived here. **A null in which the effect cannot exist under the frozen construction is
ARTIFACT-class**, and the one null this lane returns is classified explicitly in §5.

---

## HEADLINE

> **PRIMARY AXIS — `A-COMPLIANT-AT-COMPARATOR`. The frozen kill condition does NOT fire on LC-1's
> own comparator, and the arc is NOT terminated by this lane.**
>
> **SECONDARY AXIS — `S2-KILL-INHERITED`, FIRED. It was ENTAILED at freeze (prereg §8.1) and it is
> reported at full strength, not softened:** the framework carries a standing LIVE closed-negative
> against its gravitational-radiation sector — an independent far-field radiative bulk port at
> $\sqrt{10/3}\,c$, excluded at 9–110σ by Hulse-Taylor and by 100–1400× the double-pulsar bound
> (`genesis-chord-falsification-ledger.md`, entry `q1-reading-A-radiative-bulk-port`, PROMOTED LIVE
> 2026-07-20). **LC-1 does not clear that. LC-1 hardens it.**

**The three findings, in the order of their weight.**

**1. The detected messengers run at $c$, and the equality is structural, not tuned.** The transverse
branch's speed is $v_T^2 = G/\rho$ **identically for all moduli** — re-derived here from the
micropolar energy functional, with the gap modulus $G_c$ cancelling **exactly** (§1.3, residual
symbolically `0`). Against the retrieved comparator interval $[-3\times10^{-15}, +7\times10^{-16}]$
the framework predicts a difference of exactly zero, with zero free parameters. **But see §9: this
is EXPECTED-CONSISTENCY, not a discriminating survival, and it may be an outright IDENTITY.**

**2. ★The superluminal longitudinal channel is forced by the SAME modulus that sets $c$ — the
$K=2G$ GR-import is NOT what creates it.** Derived here and stronger than this lane pre-registered:

$$\frac{v_L^2}{v_T^2} \;=\; \frac{4}{3} + \frac{K}{G} \;\;\geq\;\; \frac{4}{3} \quad\text{for every } K \geq 0 .$$

So $v_L \geq \sqrt{4/3}\,c = $ `1.1547005383792515` $\,c$ **even at $K = 0$**. Bringing the
longitudinal branch down to $c$ requires $K = -G/3$ — a negative bulk modulus, i.e. a
thermodynamically unstable medium. **The $K=2G$ import moves the number from `1.1547005383792515`
to `1.8257418583505538`; it does not create the superluminality.** Every "maybe the GR-imported
$K$ is wrong" escape from the standing exclusion is therefore closed by the shear modulus alone —
and the shear modulus is the one the corpus *defines* as $\rho c^2$. This is the load-bearing new
result of the lane, and its direction is **against** the framework.

**3. LC-1's own comparator has essentially no power over that channel, and the reason is kinematic,
not a rescue.** A channel at $v > c$ hands the observer the source's PAST; a chirping source's past
is at LOWER frequency. For GW170817 the $\sqrt{10/3}\,c$ channel's content arriving coincident with
the merger was emitted `59.00526894684309` Myr earlier, when the binary radiated at
`0.00025411090220151336` Hz — **`4.896006697538493` decades below the ground-based band**, and
out-of-band across the whole $f_{low} \in [10,30]$ Hz bracket, the whole quoted distance interval,
and the whole component-mass range. **This is a statement about THIS comparator's power, not about
the physics.** The comparator class that retains full power is exactly the one that already fired:
binary-pulsar orbital decay, whose readout is a secular energy budget with no arrival-time or band
dependence at all.

**Net:** the multi-messenger dataset is the wrong instrument for the channel that is actually
killing this sector, and the standing pulsar exclusion is the sharp one — which is precisely what
the falsification ledger's own diagnostic said before this lane ran, verbatim `[sic]`: *"why pulsar
timing is the sharp kill, not the LIGO single event."* LC-1 confirms that judgement quantitatively
and adds the reason.

## §1 — Leg (a): the provenance of cold $c_{shear} = c$

### §1.1 The constants-module chain, read at file:line

`src/ave/core/constants.py`, verbatim `[sic]`:

- `:757-758` — `# Bulk mass density of the vacuum  ρ_bulk = ξ²μ₀ / (p_c · ℓ²_node)` /
  `RHO_BULK: float = (XI_TOPO**2 * MU_0) / (P_C * L_NODE**2)`
- `:764-766` — `# 3D continuum shear modulus  G_vac = ρ_bulk · c²` /
  **`# From v_transverse = √(G/ρ) = c (photons propagate at c on the LC lattice).`** /
  `G_VAC: float = RHO_BULK * C_0**2`

The comment states the logic explicitly and in the right direction: $G$ is **assigned** the value
that makes $\sqrt{G/\rho} = c$ true. $\rho_{bulk}$ is fixed independently from topological
primitives; $G$ is not. There is no independent determination of the vacuum shear modulus anywhere
in the corpus against which $\rho c^2$ could be checked.

### §1.2 `consistency-vs-emergence` classification — a SPLIT verdict, as pre-registered

| statement | class | why |
|---|---|---|
| "$G_{vac} = \rho c^2$", i.e. the **VALUE** $v_T = c$ | **DEFINITIONAL IDENTITY** | $G$ is defined as $\rho c^2$ at `constants.py:766`. Nothing is derived; the identity is a matching condition, and it is the SI-value carrier for the whole moduli chain. |
| "the transverse branch speed is $\sqrt{G/\rho}$, with the gap modulus cancelling exactly", i.e. the **FORM** | **AXIOM MANIFESTATION** | A theorem of the micropolar energy functional's long-wave reduction — re-derived independently in §1.3. Not put in by hand, and it could have come out contaminated by $G_c$. |
| "$c_{GW} = c_{EM}$" | **DEFINITIONAL IDENTITY or AXIOM MANIFESTATION, depending on FLAG-LC1-C** | If port-register channels 1 and 2 are one Christoffel eigenbranch, this is an identity (one branch, one speed). If two branches, it is a degeneracy the corpus owes a mechanism for. Canon does not settle it; §10 routes it. |
| "$c$ has the value $299792458$ m/s" | **SI-DEFINITIONAL** | not a physics claim in any framework. |

**None of the four is EMERGENCE-class.** The word "emergence" does not appear in this lane's
verdict, and the answer to the dispatch's question *"is $G_{vac} = \rho c^2$ a derivation or a
matching condition?"* is: **a matching condition — for the value; a derivation — for the form.**
This is the corpus's own FORM-deriving / VALUE-importing meta-finding, at another site.

### §1.3 The FORM, re-derived here from the energy functional (G-KP)

Not quoted from `clm-2bkp7v` — re-derived, on a functional whose normalization is pinned by a
*different* canonical quantity so the check is not circular.

Take the isotropic micropolar energy density
$W = W_{cauchy} + 2G_c\,(\boldsymbol\Omega - \boldsymbol\omega)^2$ with
$\boldsymbol\Omega = \tfrac12\nabla\times\mathbf u$. **The coefficient $2G_c$ is not chosen for
convenience: it is fixed by requiring the $k\to0$ optical branch to reproduce the corpus mass gap**
$m^2 = 4G_c/I_\omega$ (`cosserat-mass-gap.md`, `clm-jz0xaw`). The driver confirms that gap
symbolically (`gap_minus_4Gc_over_Iomega` = `0`).

For a transverse plane wave $\mathbf u = U\cos(kz)\,\hat x$, $\boldsymbol\omega = W\sin(kz)\,\hat y$,
the $z$-averaged stiffness and mass matrices in $(U,W)$ are

$$\mathbf K = \begin{pmatrix} (G+G_c)k^2/2 & G_c k \\ G_c k & 2G_c\end{pmatrix},\qquad
\mathbf M = \begin{pmatrix}\rho/2 & 0\\ 0 & I_\omega/2\end{pmatrix},$$

and the exact acoustic root's $O(k^2)$ coefficient is, symbolically,

$$v_T^2 \;=\; \frac{K_{UU} - K_{UW}^2/K_{WW}}{M_{UU}} \;=\; \frac{(G+G_c)/\rho \;-\; G_c/\rho}{1} \;=\; \frac{G}{\rho}.$$

Driver output: `acoustic_branch_v2_coefficient` = `G/rho`, residual against $G/\rho$ exactly `0`.
**The direct micropolar stiffness $(G+G_c)/\rho$ minus the level repulsion $G_c/\rho$ leaves $G/\rho$
identically — the same cancellation `clm-2bkp7v` reports, obtained independently, and with the
same functional simultaneously reproducing the canonical gap.** G-KP **PASS**.

### §1.4 ★The asymmetry that §2 turns on

The same computation, run for a **longitudinal** plane wave, gives $\nabla\times\mathbf u = 0$, hence
$\boldsymbol\Omega = 0$, hence the off-diagonal coupling $K_{UW}$ is **exactly zero**
(`longitudinal_offdiagonal_coupling` = `0`). **The longitudinal branch is micropolar-DECOUPLED: it
receives no level repulsion, so its speed is protected by nothing.** The transverse speed is
protected by a derived cancellation; the longitudinal speed is not protected at all. That asymmetry
is the whole of leg (b).

## §2 — Leg (b1/b2): the longitudinal speed, re-derived, and what forces it

### §2.1 The Christoffel spectrum, derived (G-SPEC)

$\Gamma_{ik}(\hat n) = C_{ijkl}\hat n_j\hat n_l$ with
$C_{ijkl} = \lambda\delta_{ij}\delta_{kl} + G(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})$,
$\lambda = K - \tfrac23 G$. Diagonalized symbolically for a general unit $\hat n$ and numerically on
five directions (`[100]`, `[110]`, `[111]`, `[210]`, `[321]`).

**Result — exactly TWO distinct eigenvalues, in every direction, at $K=2G$:**

| branch | $\rho v^2$ | multiplicity | value in units of $G$ at $K=2G$ |
|---|---|---|---|
| longitudinal (P) | $K + \tfrac43 G$ | 1 | `3.333333333333` |
| transverse (S) | $G$ | 2 | `1.0` |

Direction-independent (the medium is isotropic at this order, as it must be). **G-SPEC PASS**;
its fireability self-test fires (a deliberately anisotropic tensor reports `3` distinct
eigenvalues, driver field `gspec_fireability_selftest_distinct_count`).

**Poisson cross-check (G-NU):** $\nu = (3K-2G)/(2(3K+G))$ at $K=2G$ evaluates symbolically to
$2/7$, and $|\nu - $ `NU_VAC` $| = $ `0.0` against the corpus symbol. **PASS.**

At $K = 2G$: $v_L/v_T = \sqrt{10/3} = $ `1.8257418583505538`. The $\sqrt{10/3}$ of the corpus is
re-derived, not quoted, and it agrees with the two-band lane's independent $10G/(3\rho)$.

### §2.2 ★What actually forces the superluminality — and it is NOT the import

The general ratio is

$$\frac{v_L^2}{v_T^2} \;=\; \frac{4}{3} + \frac{K}{G}$$

(driver: `vL2_over_vT2_general_expr` = `4/3 + K_bulk/G`). Three consequences, all derived:

1. **$v_L > c$ for every $K \geq 0$.** The floor at $K=0$ is $\sqrt{4/3}\,c = $
   `1.1547005383792515` $\,c$. The $4G/3$ term is the SHEAR contribution to a compressional wave —
   a plane compression shears the medium — and $G$ is the modulus the corpus *defines* as
   $\rho c^2$. **The superluminal channel is forced by the very modulus that sets the speed of
   light.**
2. **$v_L = c$ requires $K = -G/3$** (driver: `K_required_for_vL_equals_c` = `['-G/3']`), a negative
   bulk modulus. A medium with $K < 0$ is unstable against uniform compression; a medium that
   carries A1 dilatation-mass has $K > 0$ by construction. There is no stable configuration of this
   medium with a single wave speed.
3. **The $K=2G$ GR-import (PR #261) is a MAGNITUDE knob, not an existence knob.** It carries
   `1.1547005383792515` $\to$ `1.8257418583505538`. Re-deriving, disputing or replacing $K$ cannot
   remove the channel. **The FORM-derived / VALUE-imported split lands here too: the FORM (a second,
   faster branch exists) is derived and axiom-forced; only its VALUE is import-conditioned.**

**Negative control (G-NEG):** with $K$ set to zero the driver recovers $v_L/v_T =$
`1.1547005383792517` against the analytic $\sqrt{4/3} =$ `1.1547005383792515`, and with $G_c\to0$ the
carrier splitting vanishes (inherited, `clm-2bkp7v` G6). The instrument reproduces both known limits.
**PASS.**

### §2.3 Direction of this result, stated plainly

**This section's content runs against the framework.** It removes the last modulus-level escape from
the standing pulsar exclusion. It is reported as the lane's principal derived finding because it is
true, not because it is comfortable, and no attempt is made downstream to convert it into a
survival.

## §3 — Leg (b3): FLAG-A narrowed — one column is a wave, the other is not

The port register carries channel 3 with two speed columns and resolves the label confusion
structurally, verbatim `[sic]` (`port-register.md`:56-58):

> "The **PORT/impedance speed $\sqrt2\,c$** ($Z_{bulk}=\rho c_{bulk}$) governs *reflection at a
> boundary* … The **RADIATIVE (far-field) speed $\sqrt{10/3}\,c$** governs a *freely propagating
> longitudinal wave* … **Both superluminal** ⇒ the causality/observability consequences are robust
> to the fork; only the exact flux prefactor moves."

**§2.1's spectrum settles the status of the first column without any new physics.** The isotropic
acoustic tensor has exactly two eigenvalues, $K+\tfrac43G$ and $G$. **$K/\rho$ is not among them**
(driver: `sqrt2_is_an_eigenvalue_at_K2G` = `false`; the numeric spectrum at $K=2G$ in units of $G$
is `[1.0, 3.333333333333]`, and $K/\rho = 2G/\rho$ would appear as `2.0`). The module's own value
confirms the two objects are distinct: `V_LONG`/`C_0` = `1.414213562373095` versus the Christoffel
$v_L/c$ = `1.8257418583505538`.

**Narrowing (NOT an overturn), with the fence held:**

- $\sqrt2\,c = \sqrt{K/\rho}$ is a **modulus/impedance quantity**, the fluid-limit bulk-sound speed
  ($G\to0$ in the compressional stiffness). It is the right object for a boundary-reflection or
  reactive-near-field impedance in the A1-only projection, exactly as the register says. **It is
  not a plane-wave eigenvalue of this medium**, so it carries **NO free inter-event wave** — status
  `NOT-A-WAVE` in the §5 enumeration.
- Therefore the register's *"Both superluminal ⇒ … robust to the fork"* gloss is describing **one
  wave and one impedance**, not two waves. **The conclusion the gloss protects still holds** (the
  radiative column is superluminal, so the observability consequence is unchanged) — but it holds
  for a stronger reason than "the fork doesn't matter": **there is no fork on the radiative row at
  all.** The Q1 radiative port has exactly one available speed, $\sqrt{10/3}\,c$.
- **No register edit is made.** The register's §4 already records, verbatim `[sic]`: *"Owed: an
  auditor-lane band-map channel-3 speed-label reconciliation."* This narrowing is routed there
  (§10, FLAG-LC1-A). KEEP-BOTH: both columns stay, and the added content is a status column, not a
  redefinition.

## §4 — Leg (c): the arrival kinematics of a superluminal channel from a chirping source

### §4.1 The mechanism, in plumber terms

A superluminal channel is a **kinematic detuner**. At a fixed reception epoch it delivers radiation
emitted at $t_e = t_{obs} - D/v$ rather than $t_{obs} - D/c$, so it shows you the source **earlier**
by $\Delta t = (D/c)(1 - c/v)$. If the source is a **chirp**, the epoch fixes the frequency — and a
binary's deep past is at *low* frequency. **The faster the channel, the deeper the past, the lower
the frequency it hands you.** This is not an AVE-specific effect; it is what any faster-than-light
channel from any inspiraling source does, and it is why a single multi-messenger event is a poor
instrument for one.

### §4.2 The numbers, for the retrieved comparator

Inputs verbatim from §2 of the prereg: $D_L = 40$ Mpc, $M_{tot} = 2.74\,M_\odot$. Chirp mass derived
in-lane under a declared equal-mass assumption: $\mathcal{M} = M_{tot}(1/4)^{3/5} = $
`1.19265427171569` $M_\odot$.

| quantity | value |
|---|---|
| light-travel time over 40 Mpc | `130.46255108669735` Myr |
| $1 - c/v_L$ at $v_L = \sqrt{10/3}\,c$ | `0.4522774424948339` |
| **retarded offset $\Delta t$** | **`59.00526894684309` Myr** |
| **$f_{GW}$ at $t_c = \Delta t$** | **`0.00025411090220151336` Hz** |
| shortfall vs $f_{low} = 20$ Hz | factor `78705.79273351967` |
| **decades below the ground-based band** | **`4.896006697538493`** |

### §4.3 Robustness (G-BAND / G-CHIRP / G-DIST) — all three PASS

| bracket | swept | verdict |
|---|---|---|
| $f_{low}$ | 10, 20, 30 Hz | out-of-band at all three (`4.594976701874511` – `5.072097956594174` decades below) |
| chirp mass | $q = 1.0, 0.75, 0.6, 0.5$ (spanning the paper's component-mass range) | out-of-band at all four; $f$ moves only from `0.00025411090220151336` to `0.00026558619323211206` Hz |
| distance | 26, 40, 48 Mpc (the quoted $40^{+8}_{-14}$) | out-of-band at all three; $f$ moves only to `0.0002986625641482756` Hz at the near end |

**Fireability (mandatory):** fed a fictitious detector with $f_{low} = 10^{-6}$ Hz, G-BAND flips to
in-band (`gband_fireability_selftest`). **The gate can fail; it did not.**

### §4.4 ★What this is, and what it is emphatically NOT

**It is:** a derived statement that the GW170817 multi-messenger dataset has no sensitivity to the
$\sqrt{10/3}\,c$ channel, by roughly five decades, for kinematic reasons that hold for any
superluminal channel from any chirping source.

**It is NOT a compliance mechanism and NOT a rescue.** The channel still exists, still propagates,
still carries energy, and is still sourced. The mechanism can only ever move a superluminal
channel's coincident-arrival content *down* in frequency; it therefore has **zero** effect on any
comparator whose readout is a secular energy budget rather than an arrival time. **Binary-pulsar
$\dot P_b$ is exactly such a readout** — it integrates the total radiated flux over decades of
orbits with masses pinned independently by the conservative post-Keplerian parameters — and that is
the comparator on which this channel is already excluded. Stated in the prereg before the number
existed; restated here because the failure mode of a finding like this one is to be quoted without
its second half.

For completeness the driver also evaluates the $\sqrt2\,c$ column's arrival row; per §3 that column
is `NOT-A-WAVE`, so the row is reported as a formality and carries nothing.

### §4.5 ★The obvious objection, addressed: GW170817's chirp RATE is a second handle — and it is degenerate

**Objection.** The arrival-time argument only covers the *timing* readout. But LIGO also measures the
**chirp rate**, which is an energy-budget observable: an extra radiative channel drains the orbit
faster, so the binary sweeps through the band faster. Doesn't that give this comparator power over
row 3b after all?

**Answer: no, for a single event — and the reason is the one the corpus already banked.** For an
inspiral, the chirp mass is *inferred from* the chirp rate. An unmodelled extra channel does not
show up as an anomaly; it shows up as a shifted $\mathcal{M}$. There is no independent, conservative
measurement of the component masses in a single LIGO event to break that degeneracy — which is
exactly why the ledger's own diagnostic says, verbatim `[sic]`, that in a binary pulsar *"the masses
are pinned **independently** by the *conservative* post-Keplerian parameters (periastron advance
`ω̇`, Einstein delay `γ`, Shapiro `r,s`; mass ratio in the double pulsar), so the *radiative* `Ṗ_b`
is an **over-determined consistency check** — **the chirp-mass degeneracy that blunts a single LIGO
event is broken.**"*

**So both of GW170817's readouts are blunted, by two independent mechanisms:** the timing readout by
band mismatch (derived here, `4.896006697538493` decades), and the energy readout by chirp-mass
degeneracy (inherited, and not re-derived here). **This does not weaken the standing exclusion by
one bit** — it locates the exclusion's power entirely in the pulsar comparator, where it already
sits. It also means LC-1 supplies **no second independent comparator** against the bulk channel,
which is a real limitation of this lane and is stated as one.

## §5 — THE CHANNEL ENUMERATION (the deliverable of leg b)

Enumeration frame: the port register's channel inventory (`port-register.md` §1), with channel 3
split into its two FLAG-A columns per §3, plus one row for a messenger the corpus cannot yet assign.
Observability vocabulary: the dispatch's four mechanisms plus the two this lane declared at freeze
(prereg §5.2) — `NOT-A-WAVE` and `OUT-OF-BAND-AT-ARRIVAL`.

| # | channel (sector / irrep) | speed | wave? | sourced by a GW170817-class event? | read by the GW170817 network? | mechanism |
|---|---|---|---|---|---|---|
| **1** | EM-transverse photon ($T_2$ shear-EM, transverse-$u$) | $c$ | YES | YES — the sGRB | **YES** — Fermi-GBM / INTEGRAL | **AT $c$** (the comparator's reference messenger) |
| **2** | mechanical shear / GW ($T_2$ shear-G) | $c$, exactly and for all moduli (§1.3) | YES | YES — mass quadrupole | **YES** — LIGO/Virgo | **AT $c$** |
| **3a** | A1 bulk PORT/impedance column, $\sqrt{K/\rho}$ | $\sqrt2\,c$ | **NO** — not a Christoffel eigenvalue (§3) | n/a | n/a | **`NOT-A-WAVE`** — modulus/impedance quantity; governs boundary reflection + reactive near-field storage (P9 NOT-A-PORT); carries no inter-event energy |
| **3b** | **A1 bulk RADIATIVE column — the P-wave** | $\sqrt{10/3}\,c = $ `1.8257418583505538` $c$ | **YES** — the longitudinal eigenbranch, gapless, micropolar-**unprotected** (§1.4) | **YES (INHERITED, CONDITIONAL)** — #761 falsified all three escapes; conditional on the envelope lane's OPEN constituent-knot-core fork | **NO** — `4.896006697538493` decades out of band (§4) | **`OUT-OF-BAND-AT-ARRIVAL`** — radiative, sourced, in-principle readable, invisible to *this* comparator. **NOT a compliance mechanism (§4.4).** ★THE CRUX ROW |
| **4** | Cosserat micro-rotation / wryness (couple-stress, the $(2,3)$ winding) | $v_\parallel = \sqrt{2\gamma/I_\omega}$, $v_\perp = \sqrt{2\gamma/I_\omega + G_c/\rho}$ — **both $\neq c$** (`clm-2bkp7v`) | above the gap only | **NO** — drive/gap $= $ `4.0466498947022305e-19` (`-18.39290436797714` decades) | n/a | **`GAPPED`** — $E_g = 2m_ec^2 = $ `1.0219978999923285` MeV (A-008); doubly dead: also **`CONFINED/EVANESCENT`**, Yukawa reach $\ell_{node}$, path $= $ `3.1962745316728043e+36` reaches |
| **5** | matter messengers (neutrinos, cosmic rays) — bound excitations, not a medium channel | **UNDERIVED** | — | YES (a BNS merger is a copious $\nu$ source) | GW170817 $\nu$ searches returned NULL | **`UNDERIVED`** — the corpus does not establish the limiting speed of a bound matter excitation in a medium with $v_L > v_T$. Enumerated, flagged (§10 FLAG-LC1-D), **NOT folded into the verdict, and no speed is guessed** |

### §5.1 Reading the table

- **Two channels are read by this comparator, and both run at exactly $c$.** Row 2's $c$ is
  structurally protected (§1.3); row 1's is the reference. Against the retrieved interval
  $[-3\times10^{-15}, +7\times10^{-16}]$, AVE predicts exactly zero difference.
- **Two channels run at $\neq c$ and neither is read by this comparator** — row 3b by band mismatch,
  row 4 by an 18-decade energy gap that is over-determined by a 36-decade Yukawa suppression
  (G-GAPMARGIN: still dead across gap $\times\{0.25, 0.5, 1, 2, 4\}$, so C6's factor-of-4 hinge
  cannot move it).
- **One row is not a wave at all**, and that is a derived narrowing of the register's FLAG-A.
- **One row the corpus cannot fill.** It is left open and visible rather than assumed compliant.

### §5.2 The null in row 3b is classified

Per the regime discipline: is "row 3b is not read" an ARTIFACT-class null (the effect cannot exist
under the frozen construction) or a PHYSICS-class null? **It is neither, and the third category is
the honest one: a COMPARATOR-POWER null.** The effect exists, is constructible, and is measurable
in principle; the specific instrument used by this comparator cannot see it, for a derived
kinematic reason, by a margin that is robust across every quoted uncertainty. A comparator-power
null constrains nothing about the physics and must never be banked as if it did.

## §6 — The bins, scored against the frozen criteria

Scored against the criteria frozen in prereg §7, with nothing dropped, widened, or re-defined.

### §6.1 PRIMARY AXIS (comparator-scoped) — **`A-COMPLIANT-AT-COMPARATOR`**

Criterion, verbatim from the freeze: *"Every channel the GW170817 detector network can read runs at
$c$, AND every $\neq c$ channel is unread by that network with its blocking mechanism NAMED per
channel."* Both conjuncts met (§5): rows 1 and 2 at $c$; rows 3a/3b/4 unread with mechanisms
`NOT-A-WAVE` / `OUT-OF-BAND-AT-ARRIVAL` / `GAPPED`+`CONFINED`. Row 5 is `UNDERIVED` and is
excluded from the verdict rather than counted as compliant.

**`B-KILL-AT-COMPARATOR` did NOT fire.** Its criterion needed a $\neq c$ channel in-band and
antenna-coupled at the coincidence epoch; the in-band leg fails by `4.896006697538493` decades and
is robust across all three brackets.

**`C-NOT-CERTIFIED` did NOT fire.** Every gate ran and passed (§7); all three fireability self-tests
fired.

**KILL-CONDITION STATUS on this axis: NOT-FIRED. The arc is NOT terminated by this lane** (prereg
§7.3).

### §6.2 SECONDARY AXIS (inherited corpus state) — **`S2-KILL-INHERITED`, FIRED**

Declared ENTAILED at freeze (prereg §8.1), so this fires by DEMONSTRATION, not adjudication. Three
merged receipts, re-verified at this worktree HEAD:

1. `manuscript/ave-kb/common/port-register.md` frontmatter, verbatim `[sic]`: *"Q1 is a RULED row —
   REVERTED 2026-07-20 to Reading-A-live … the independent-radiative-port exclusion is live against
   the framework (was: explicitly-OPEN, adjudication-pending)."*
2. `manuscript/ave-kb/common/genesis-chord-falsification-ledger.md`, entry
   `q1-reading-A-radiative-bulk-port`, verbatim `[sic]`: *"🔴 PROMOTED LIVE 2026-07-20 …
   the AVE gravitational bulk sector carries an independent far-field radiative port at O(1)
   coupling that binary-pulsar timing excludes at 9–110σ (Hulse-Taylor) / 100–1400×
   (double-pulsar) — a standing closed-negative against the framework's gravitational-radiation
   sector, no longer a conditional bank."*
3. `research/2026-07-20_envelope-sector-reduction_result.md`: BIN-1-CONDITIONAL, *"the standing
   Reading-A exclusion + the reverted Q1 ruling STAND on this analysis"*, with the constituent
   knot-core fork OPEN and potentially verdict-flipping.

**`S1-NO-INHERITED-KILL` was unreachable at freeze and is not claimed.**

### §6.3 The dispatch's own three bins, scored as frozen (prereg §7.5)

| dispatch bin | score |
|---|---|
| **(i) COMPLIANT** — *"all inter-event energy channels at c, or non-c channels shown gapped/confined/sourceless"* | **NOT LANDED, and UNREACHABLE.** Channel 3b is not gapped (gapless acoustic), not confined (it propagates), and not sourceless (#761 falsified source-decoupling). `A-COMPLIANT-AT-COMPARATOR` is **not** a renaming of this bin: it is strictly weaker, and the difference is exactly the `OUT-OF-BAND-AT-ARRIVAL` mechanism. **Landing A must never be read as landing (i).** |
| **(ii) KILL** | **NOT FIRED on the comparator-scoped reading; FIRED on the broad reading, where it was entailed.** |
| **(iii) NOT-CERTIFIED** | not fired. |

### §6.4 The arc-termination decision — routed to Grant, not taken here

Per prereg §7.3, LC-1 terminates the arc only on `B-KILL-AT-COMPARATOR`, which did not fire. But
`S2` did fire, and whether a standing exclusion on the **pulsar** comparator should terminate a
**multi-messenger** arc is a framing-level question about arc scope. **That is Grant's decision and
this lane does not take it.** The decision package:

- **Argument for continuing LC-2..LC-5:** each remaining test targets a different observable class
  (anisotropy, dispersion, birefringence, form factor) against different data, and none of them is
  adjudicated by the bulk-radiative-port question. They remain independently informative about the
  framework's *other* sectors regardless of the gravitational sector's standing negative.
- **Argument for terminating:** the arc was scoped as a Lorentz-compliance harvest, and its lead
  test has just re-derived — with a *stronger* mechanism than the corpus had — that the framework
  carries a live, sector-level, superluminal-channel exclusion. Testing four more compliance axes
  while one is already closed-negative may be low truth-per-token.
- **This lane's own read, offered as input and not as a verdict:** §2.2 is the material change since
  the arc brief was written. The exclusion is now shown to be *modulus-independent* — forced by
  $G$ alone. That makes the standing negative harder to escape and correspondingly raises the value
  of routing effort to the **mechanism** question (what, if anything, makes a real medium's
  longitudinal channel non-radiative) rather than to further compliance axes.

## §7 — Gate table (UNRUN ≠ PASSED)

| # | gate | run | result | pass |
|---|---|---|---|---|
| **G-SPEC** | isotropic Christoffel spectrum | RUN | exactly `2` distinct eigenvalues in all five directions at $K=2G$; symbolic eigenvalues $K+\tfrac43G$ (×1), $G$ (×2) | **PASS** |
| **G-NU** | Poisson cross-check vs `NU_VAC` | RUN | symbolic $2/7$; $|\Delta| = $ `0.0` | **PASS** |
| **G-KP** | independent re-derivation of the photon cancellation | RUN | $v_T^2 = $ `G/rho` exactly; residual `0`; same functional reproduces the canonical gap $4G_c/I_\omega$ exactly | **PASS** |
| **G-MEMBER** | combine-member insensitivity at $S=1$ (#905/#907 fence) | RUN | per-grade vs normalized-L2 member: $|\Delta v_T| = $ `0.0`, $|\Delta v_L| = $ `0.0` | **PASS** |
| **G-BAND** | $f_{low}$ bracket robustness | RUN | out-of-band at 10, 20 and 30 Hz | **PASS** |
| **G-CHIRP** | chirp-mass robustness | RUN | out-of-band for $q \in \{1.0, 0.75, 0.6, 0.5\}$ | **PASS** |
| **G-DIST** | distance robustness | RUN | out-of-band at 26, 40, 48 Mpc | **PASS** |
| **G-GAPMARGIN** | gap over-determination (C6 hinge) | RUN | dead at gap $\times\{0.25,0.5,1,2,4\}$; drive/gap `4.0466498947022305e-19`; path `3.1962745316728043e+36` Yukawa reaches | **PASS**, and the margin is reported so the pass reads as over-determination, not a tight call |
| **G-CONST** | canonical-source discipline | RUN | every substrate constant imported from `ave.core.constants`; the three unit definitions (solar mass parameter, parsec, Julian year) declared and emitted into the JSON | **PASS** |
| **G-NEG** | negative controls | RUN | $K\to0$ gives $v_L/v_T = $ `1.1547005383792517` vs analytic `1.1547005383792515`; $G_c\to0$ splitting vanishes (inherited) | **PASS** |
| **G-DET** | determinism | RUN | double-run digest `fabf7bf8d043605f8706b395ed6b0eed521c571425aa695fb8bd8d242776ba1c` twice | **PASS** |
| **G-DOC** | result-doc numeral gate | RUN | `lc1_one_speed_number_check.py` re-derives every backticked load-bearing numeral from the shipped JSON; mutation receipt included | **PASS** |

### §7.1 Fireability self-tests — all three FIRED

1. **G-SPEC** fed a deliberately anisotropic tensor reports `3` distinct eigenvalues (would fail the
   two-eigenvalue criterion). **FIRES.**
2. **G-BAND** fed a fictitious $f_{low} = 10^{-6}$ Hz detector flips to in-band. **FIRES.**
3. **G-DOC** under `--mutation-receipt` fails on every perturbed JSON source value. **FIRES.**

No gate in this lane is decorative.

## §8 — What this does to port-register Q1, and what it does NOT do

**Verdict: LC-1 NARROWS Q1. It does not answer it, re-open it, or re-close it — Q1 was already
answered against the framework on 2026-07-20, and this lane leaves that ruling exactly where it
found it.**

**Three derived narrowings, each a routed auditor-lane item, none executed here:**

1. **The Q1 radiative row has exactly ONE available speed, not two.** §3: $\sqrt2\,c$ is not a
   plane-wave eigenvalue, so the FLAG-A fork does not reach the radiative row. Q1's flux prefactor
   is not bracketed by a speed fork; it is a single number at $\sqrt{10/3}\,c$. (This *narrows* the
   pulsar-hardening doc's $[0.0148, 0.1768]$ speed-fork spread on the speed axis; the $O(1)$
   coupling bracket is untouched and remains the real uncertainty.)
2. **Q1's exclusion cannot be escaped through the $K=2G$ import.** §2.2: $v_L > c$ for every
   $K \geq 0$. Any future re-derivation, dispute, or replacement of $K$ leaves a superluminal
   radiative longitudinal branch. **This closes a live-looking escape route on Q1 and it closes it
   in the framework's disfavour.**
3. **The longitudinal branch is micropolar-UNPROTECTED.** §1.4: the transverse branch's $c$ is
   protected by an exact level-repulsion cancellation; the longitudinal branch receives no such
   cancellation because $\nabla\times\mathbf u = 0$ kills the coupling. So the corpus's own
   protection mechanism for $c$ is *structurally unavailable* to the channel that needs one. A
   future Reading-B suppression derivation must come from somewhere other than the micropolar
   sector.

**Fence held.** No row edited, no ruling touched, no ledger entry amended, no `clm-` minted, no
solidity moved. The three items above are stated with receipts and routed (§10).

**What LC-1 explicitly does NOT do to Q1:** it does not supply the Reading-B suppression mechanism
the ledger says is owed; it does not adjudicate the envelope lane's constituent knot-core fork; and
it does not weigh in on whether the pulsar exclusion should be re-opened.

## §9 — Discrimination note: what kind of statement the compliance is

`ave-discrimination-check` was run at freeze (prereg §1.2), not after the number, and its verdict
binds this section.

**Sector class: PURE-AC.** Wave speeds and arrival times are shared observables. GR predicts
$c_{GW} = c$ exactly; the SM predicts $c_\gamma = c$ exactly. **A pure-AC agreement cannot be a
framework-level positive**, because Maxwell/GR recovery is *mandatory* for AVE — agreement here is
required, not risky.

**Tautology filter: the compliance may be an outright identity.** If port-register channels 1 and 2
are one Christoffel eigenbranch read through two conjugate variable pairs (FLAG-LC1-C, unresolved),
then "$c_{GW} = c_{EM}$" restates "one branch has one speed." An identity cannot be evidence. The
honest label is therefore **IDENTITY-or-MANIFESTATION-class compliance**, and the lane does not
choose the flattering one.

**SM counterfactual:** a framework that builds $c$ in by construction passes this comparator for
free. AVE does exactly that at `constants.py:766` for the VALUE. **Symmetric-standard note:** GR
also does not *derive* $c_{GW} = c$ — it is a consequence of the metric's structure, put in. So the
value-level equality is peer, not inferior; the honest asymmetry is elsewhere and runs the other
way (§2.2).

**Forbidden vocabulary, and it does not appear in this document:** "AVE-distinct", "STRONG",
"chord", "discriminating survival", "confirms AVE", "passes a stringent test". The one-speed PASS
is **expected consistency**, and the word that belongs in the headline is the one used there.

**Is anything here TRUE and non-trivial?** Yes, and it is the part that runs against the framework:
$v_L/v_T = \sqrt{4/3 + K/G} > 1$ for every stable medium is a real, derived, previously-unstated
constraint on this substrate, and the arrival-kinematics mechanism (§4.1) is a real, derived,
general fact about superluminal channels from chirping sources that the corpus did not have. Both
are bankable. Neither is a chord.

## §10 — FLAG-DON'T-FIX: routed, not resolved

All five flags were raised at freeze (prereg §11) or fall directly out of the derivation. **None is
resolved here. No leaf, register, ledger or ruling is edited.**

### FLAG-LC1-DISPATCH — the dispatch's and the arc brief's description of Q1 is STALE against `main`

**Dispatch:** *"the explicitly-OPEN Q1"*. **Arc brief LC-1 row:** *"bulk $\sqrt{10/3}c$ P-wave
observability — gapped, confined, or sourceless?"*

**`port-register.md` frontmatter at HEAD, verbatim `[sic]`:** *"Q1 is a RULED row — REVERTED
2026-07-20 to Reading-A-live … the independent-radiative-port exclusion is live against the
framework (was: explicitly-OPEN, adjudication-pending)."*

Q1 was answered against the framework on 2026-07-20, **before the arc brief was written on
2026-08-04**, and all three of the brief's proposed answers (gapped / confined / sourceless) were
falsified by #761 at review grade on the same date. The dated currency update of 2026-08-06 did not
catch it. **Consequence: the dispatch's bin (i) was unreachable at freeze (§6.3), which is why the
prereg had to add a comparator-scoped axis to leave this lane a real adjudication to perform.**
Routed to Grant + auditor lane as an arc-brief currency finding.

### FLAG-LC1-A — FLAG-A's two columns are a wave and a not-a-wave

Derived in §3. The register's *"Both superluminal ⇒ … robust to the fork"* gloss protects a
conclusion that still holds, for a stronger reason. **Routed to the auditor-lane item the register
itself already lists as owed** (`port-register.md` §4, verbatim `[sic]`: *"Owed: an auditor-lane
band-map channel-3 speed-label reconciliation."*). No register edit by this lane; KEEP-BOTH.

### FLAG-LC1-B — a live corpus contradiction on A1 free-space radiativity, on this lane's crux channel

Two canon leaves make opposite claims:

- `manuscript/ave-kb/common/physics-lineage-map.md:63`, verbatim `[sic]`: *"AVE evades by sector
  assignment, claiming **no longitudinal photon** (the A1 grade is non-radiative in free space,
  re-engaging only inside saturation …). The gapped/confined status is simultaneously the evasion
  and the exposure: any mechanism coupling the A1 bulk mode to EM detectors below saturation walks
  back into these bounds."*
- `manuscript/ave-kb/common/port-register.md` §3 Q1 (standing, via #761 §5): the A1-dilatation rides
  the **gapless** P-branch, the binary drives it at quadrupole order, the port is **OPEN**.

**These cannot both be read at face value.** The likely reconciliation is that "A1" names TWO
objects — the EM-scalar grade (Gauss-constrained; no propagating longitudinal *EM* wave, the
Goldhaber–Nieto-relevant statement, correctly qualified at `historical-precedents.md:21`) and the
MECHANICAL A1 dilatation (the elastic P-wave, which §2 shows must propagate for any stable medium)
— but the corpus's own vocabulary node `def-9a4f07` currently IDENTIFIES them, reading the V-sector
scalar as *"'the 3' in its A1 dilatation-MASS sense."*

**Why it is LC-1-relevant and not a bookkeeping nit:** an interferometer reading a scalar GW
polarization is a *mechanical* channel read out *optically* — the exact configuration
`physics-lineage-map.md:63` warns about. Row 3b's readability leg sits precisely on this
distinction. **Both sides quoted; neither picked. Routed to Grant (sector-ownership adjudication)
and the auditor lane (leaf repair, once adjudicated).**

### FLAG-LC1-C — are port-register channels 1 and 2 the same branch?

Both $T_2$, both transverse-$u$, both at $c$, but carrying $Z_{EM} = Z_0$ and
$Z_{shear} = \rho c_{shear}$ in different unit systems. §2.1 finds exactly ONE transverse
eigenbranch (multiplicity 2 — the two polarizations). If the photon and the GW ride it, LC-1(a)'s
answer is an identity (§9). **Raised; not decided. This lane's verdict is constructed not to depend
on it** — both channels are at $c$ either way.

### FLAG-LC1-D — the messenger the corpus cannot assign

Neutrinos. Row 5 of §5. The corpus does not establish the limiting speed of a bound matter
excitation in a medium whose longitudinal eigenspeed exceeds its transverse one — and if matter is
A1-dilatation-owned (canon) while the A1 channel runs at `1.8257418583505538` $c$, that question is
live. GW170817's neutrino searches were null so nothing moves for THIS comparator, but the row is
left visibly open rather than assumed compliant. **Routed as a follow-on lane. No speed is guessed.**

### FLAG-LC1-E (new, from the derivation) — the vocabulary this arc froze is incomplete

The dispatch's four-item observability vocabulary (gapped / confined / sourceless / radiative) has
no slot for either a modulus-that-is-not-a-wave or a sourced-radiative-but-out-of-band channel, and
**both occur in this substrate**. The prereg added them at freeze (§5.2) rather than forcing a
channel into a wrong slot. **Surfaced as an incompleteness finding against the arc's frozen frame,
for LC-2..LC-5 to inherit if the arc continues.**

## §11 — Conditionals carried, and the fence on this result

### §11.1 Conditionals carried from the mandatory inputs (prereg §6), and where each bites

| # | conditional | does it move this verdict? |
|---|---|---|
| **C1** scale separation — every speed is an $O(k^2)$ long-wave coefficient; the two-band lane's validity window closes before its relativistic regime opens, and the review softened the attribution to depend on the additional gap = Compton identification | **NO.** At 100 Hz, $k\ell_{node} \sim 10^{-18}$: the long-wave limit is exact to any relevant precision. Nothing in this lane reads a zone-edge quantity. |
| **C2** gap identification | **NO** for the verdict; the row-4 conclusion is over-determined by 18 + 36 decades and survives the whole C6 factor range. |
| **C3/C4** connectivity — the $O(k^2)$ forms are connectivity-independent (with the review-corrected reason: the least-squares gradient's asymmetric piece enters eigenvalues only at $O(k^3)$); the $O(k^4)$ coefficients and band tops ARE diamond-specific, and the canonical Cosserat operator runs on the $z=4$ diamond CONTROL net, not the ratified $z=3$ srs carrier | **NO** — this lane uses only $O(k^2)$ quantities and the continuum Christoffel spectrum. **But it is a real fence:** nothing here licenses any statement about band tops, zone-edge transport, or $O(k^4)$ dispersion on the production carrier. LC-3 inherits that fence, not this result. |
| **C5** the 0.612 full-BZ group-velocity figure is a LOWER BOUND | **NO** — cited qualitatively only, never as a number. |
| **C6** the A-008 single hinge (`l3-electron-soliton-synthesis.md:132`); if Grant ruled that clause canonical the gap moves by a factor of 2–4 | **NO** — G-GAPMARGIN swept $\times\{0.25,0.5,1,2,4\}$; row 4 stays dead in every case. |
| **C7** $G_c$, $I_\omega$, $\gamma$ are ENG-CHOICE placeholders with no `constants.py` symbols | **NO** — no carrier-branch *number* is load-bearing here; row 4's speeds are reported as placeholder-conditioned symbols, and its DEAD status rests on the gap and the reach, not on $v_\parallel$ or $v_\perp$. |
| **#905/#907** cross-grade combine member is OPEN in canon | **NO for propagation** (G-MEMBER measured $|\Delta| = $ `0.0` at $S=1$, as declared at freeze). **YES in principle for source coupling**, which is inherited and not derived here. |
| **#890 NO-TWIST** | over-determination only: it independently removes a homogeneous-strain pump into row 4, which was already dead by 18 decades. |
| **envelope lane's OPEN constituent-knot-core fork** | **THIS IS THE ONE THAT COULD MOVE `S2`.** The "sourced" leg of row 3b is inherited at BIN-1-**CONDITIONAL** grade; the envelope result states the fork is *"unadjudicated both ways and potentially verdict-flipping."* If it resolves toward image-cancelled constituent cores, the standing exclusion could weaken. **LC-1 does not touch it and does not lean on it in either direction.** |

### §11.2 The fence on this result — what it does NOT license

1. **No canon propagation of any kind.** No `clm-`/`def-` mint, no KB or manuscript leaf edit, no
   register row, no ledger entry, no solidity change, no ruling amendment.
2. **No re-opening, re-closing, or re-grading of Q1** — only the three routed narrowings of §8.
3. **No arc termination by this lane's act** (§6.4); the arc-scope decision is Grant's.
4. **No LC-2..LC-5 content.** In particular: nothing here about anisotropy order, dispersion
   curvature, birefringence, or form factors, and the C3/C4 fence explicitly blocks reuse of this
   lane's continuum spectrum for zone-edge questions.
5. **No AVE-distinctness, chord, or strength claim on the compliance** (§9).
6. **No claim that the arrival-kinematics mechanism rescues anything** (§4.4).
7. **No statement about the electron, the rest mass, the numerical value of $c$, or whether the
   $K=2G$ import is correct** — only that its correctness is irrelevant to the existence of the
   superluminal branch.
8. **No adjudication of FLAG-LC1-B's sector-ownership question**, on which row 3b's readability leg
   partly rests.

## §12 — SVA pilot log (per-row fill experience)

Per `standard-vacuum-analysis.md` §3, each of the eleven §0 rows scored, with gaps logged as dated
amendment candidates. **This lane does NOT canonize the SVA leaf.**

| row | score | note |
|---|---|---|
| 1 sector / ownership | **FILLED** | The per-channel ownership table caught the A1/T2 hazard *and* surfaced FLAG-LC1-C (two register rows, one eigenbranch) — a defect the row's own cross-wiring check does not name but which the discipline of writing the table exposed. |
| 2 regime / phase-state | **FILLED** | Forced the cold-propagation / hot-source SPLIT to be declared in advance, which is what kept the member-insensitivity claim honest (§11.1). |
| 3 circuit statement first | **FILLED** | Stating the observable as "how many propagating channels between two terminals, and which terminate into a real impedance" is what produced the three-question structure of §5.3. Framework-word-first would have produced "is AVE Lorentz invariant," which is unanswerable. |
| 4 plane & projection | **FILLED, and load-bearing** | Declaring the projection as the plane-wave **eigenvalue** basis rather than the modulus basis is *exactly* the distinction that resolved FLAG-A (§3). Without this row the lane would have compared $\sqrt2$ against $\sqrt{10/3}$ as two candidate speeds. |
| 5 constitutive provenance | **FILLED** | Tagging $G$ DEFINITIONAL and $K$ IMPORTED *before* deriving is what made §2.2's "the import is not what forces it" statement legible instead of surprising. |
| 6 energy ledger | **FILLED** | The "sourced = arrow in, read = arrow out" formulation is the §5.3 question set. |
| 7 calibratability | **FILLED** | Both targets are ratios/phase differences; no unit bridge crossed. |
| 8 discrimination class | **FILLED, and it constrained the headline** | PURE-AC declared at freeze forbade the flattering framing before any number existed. |
| 9 certification plan | **FILLED** | 12 gates, 3 fireability self-tests, all fired. |
| 10 adjudication routing | **FILLED** | Prereg §12; the arc-scope decision is routed, not taken. |
| 11 numerical conditioning | **FILLED, thinly** | Genuinely easy here: no iterated map, no cancellation-sensitive subtraction, one power law in log space. The regex-engine naming sub-clause applied to the checker. |

**Amendment candidates surfaced by this pilot (logged, not applied):**

1. **A COMPARATOR-POWER row is missing.** Rows 8–9 cover discrimination class and certification, but
   nothing forces a lane to ask *"does the comparator I chose have power over the channel I am
   testing?"* This lane's entire content is that answer, and the SVA header did not prompt it — the
   pre-test physics check (§0.5) did. Candidate: extend row 9 with a comparator-power sub-clause, or
   mint row 12.
2. **Row 5 could carry an ENTAILMENT sub-clause.** Provenance tagging catches imported *values*; it
   does not catch imported *verdicts* — a merged ruling that pre-determines a bin. `ave-prereg`
   Step 3.10 catches it, but only if the author remembers to run it; the SVA header would fire it
   structurally.
3. **Row 4's "plane & projection" gloss should name the eigenbasis-vs-modulus-basis distinction
   explicitly** for elastic/acoustic lanes, the way it already names the spectral-lane
   branch-selection projection. This lane is the receipt: it is the row that resolved FLAG-A.

---

## §13 — Reproduction

```
python research/drivers/lc1_one_speed_check.py          # writes lc1_one_speed_results.json
python research/drivers/lc1_one_speed_number_check.py   # G-DOC, gating
python research/drivers/lc1_one_speed_number_check.py --mutation-receipt
make verify-lc1-one-speed-number-check
```

Deterministic double-run digest: `fabf7bf8d043605f8706b395ed6b0eed521c571425aa695fb8bd8d242776ba1c`.
