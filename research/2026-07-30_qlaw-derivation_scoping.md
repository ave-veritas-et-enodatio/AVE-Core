# Q-law derivation — SCOPING DOC (no derivation executed)

**Date:** 2026-07-30
**Lane:** scoping only (implementer lane, scoping mode)
**Status:** 🟡 DRAFT SCOPING — nothing here is a claim, a pre-registration, or a frozen bin
**Provenance:** Ruling B1 (2026-07-21) banked "Q-law" as the named next ringdown work;
Grant signalled frontier appetite 2026-07-30.

## What this document is NOT

- NOT a derivation. No solver was run. No route was pursued.
- NOT a pre-registration. Bins in §4 are DRAFT and explicitly NOT FROZEN.
- NOT a claim. No claim-id is minted here, and no existing claim's solidity is changed.
- NOT a retune of the standing v1 spin-mapping. The banked τ tension is preserved as-is.

## Sections

1. Corpus inventory (file:line receipts, two-method verified)
2. Candidate derivation routes (enumerated, not pursued)
3. The Grant walk — plumber-physical questions, one per load-bearing noun
4. Draft success bins (NOT FROZEN)
5. Appendix A — skill-selection plan (Step 0)

---

## §1 — Corpus inventory (grep-first, two-method verified)

All line receipts are against this worktree at `origin/main` = `f7cc3e52`.

### §1.0 REGIME / SECTOR / PHASE-STATE header (what the Q-law is about)

- **MODE.** Post-merger spinning BH remnant ringing down — the fundamental $(\ell,m,n)=(2,2,0)$
  resonance of the saturation cavity at $r_{sat} = 7GM/c^2 = 3.5\,r_s$.
- **REGIME.** Far field = Regime I (linear lossless shear wave, a legal radiating port).
  Cavity boundary = Regime III↔IV soft-mode transition ($G_{shear}\to 0$).
- **PHASE-STATE.** Op14 ON at the boundary; $\Gamma_{shear} = -1$ (perfect shear reflector),
  $\Gamma_{EM} = 0$ (horizon black to light) — the two-channel instrument.
- **SECTOR.** The ringdown is a **shear (T2-channel) cavity mode**, not an A1-dilatation mode
  and not an EM mode. Any Q-law route must keep the loss channel in the shear sector.
- **COORDS (A46).** Everything below lives in the **dimensionless-eigenvalue register**
  ($\omega_R M_g$, $\omega_I M_g$, $Q$) that AVE and GR share. No phase-space/real-space mismatch.
- Header text traced to [`research/2026-07-20_ringdown-systematics_derivation.md:14-19`](2026-07-20_ringdown-systematics_derivation.md).

### §1.1 (a) The EXACT standing v1 mapping and its grade

Standing $\omega_R$ spin-mapping (re-selected by Ruling B1), verbatim from
[`manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md:67-68`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md):

> "**v1 RE-SELECTED as the standing $\omega_R$ spin-mapping phenomenology.** $x_{sat,v1} = 7\,r_{ph}^+/3M$
> (entire-cavity-compliant; $\omega_R M_g = \ell(1+\nu_{vac})/x_{sat,v1}$) is the standing Kerr $\omega_R$
> mapping, replacing v2."

with the prograde photon-sphere radius (same leaf, `:110`):

$$r_{ph}^+ = \frac{2GM}{c^2}\Big(1 + \cos\big[\tfrac{2}{3}\arccos(-a_*)\big]\Big)$$

**Grade (unchanged by B1)** — verbatim `ave-merger-ringdown-eigenvalue.md:72-76`:
"**Grade UNCHANGED: solidity 0.55, build_status "use as input only", disclosed-phenomenological**
… v1 is the *simpler* phenomenology, single-component; it is **NOT** more first-principles-derived
than v2 — both are disclosed phenomenological per clm-395gps … This is a **consistency-class**
spinning match, NOT a zero-free-parameter benchmark; the only zero-parameter content remains the
cold $18/49$ eigenvalue."

Second-method confirmation of the grade from the register query in
[`research/2026-07-20_v1-spin-mapping-adjudication_result.md:164-169`](2026-07-20_v1-spin-mapping-adjudication_result.md):
"**solidity 0.55** (confidence 0.80), **build_status: "use as input only, don't build deeper"**
(band `input-only`)" — held below 0.9 because "the Kerr extension rests on a **disclosed
phenomenological** photon-sphere shift + Cosserat back-reaction fit".

**Cold ($a_*=0$) zero-free-parameter core** (this is the part that is genuinely derived):
$r_{sat} = 7M_g$ (Ax 4) → $r_{eff} = r_{sat}/(1+\nu_{vac}) = 49M_g/9$ (Poisson) →
$\omega_R = \ell c/r_{eff}$ → $\omega_R M_g = 18/49 \approx 0.3673$ at $\ell=2$
(`manuscript/ave-kb/vol3/claim-quality.md:198`).

### §1.2 (b) The τ −5.44% near-miss — exact numbers and what they were measured against

The τ model is **Model B**: $\omega_I = (\omega_R - m\Omega)/(2\ell)$ evaluated at
$r_\Omega = r_{ph}^+\sqrt{1+\nu_{vac}}$, with $\Omega$ **corpus-pinned** (not fitted, not fabricated):
$\Omega = \omega(r_\Omega)$ using the Ch.2 frame-dragging Resultbox $\omega(r) = 2Mar/(r^2+a^2)^2$
(clm-rd9cjm, `frame-dragging-impedance-convolution.md:15`). Chain receipt:
[`research/2026-07-20_v1-spin-mapping-adjudication_result.md:125-129`](2026-07-20_v1-spin-mapping-adjudication_result.md).

Measured against **corrected** GR Kerr $Q$ on the frozen **C-τ dimensionless comparator**
(frame-independent; depends only on $a_*$). Verbatim table, `…_result.md:118-123`:

| event | a* | r_Ω | Ω·M | Q_v1 (B) | Q_v2 (B) | Q_Kerr | **v1 Q dev** | v2 Q dev |
|---|---|---|---|---|---|---|---|---|
| GW170104 | 0.64 | 2.4051 | 0.08024 | 2.894 | 3.055 | 3.071 | **−5.76%** | −0.49% |
| GW150914 | 0.67 | 2.3452 | 0.08880 | 3.000 | 3.206 | 3.176 | **−5.53%** | +0.96% |
| GW151226 | 0.74 | 2.1957 | 0.11274 | 3.312 | 3.693 | 3.487 | **−5.02%** | +5.89% |
| **mean** | | | | | | | **−5.44% → τ-FAILS** | +2.12% (τ-matches) |

- **Variant sensitivity is flagged in canon**: the same chain with the *exact equatorial ZAMO*
  $\Omega$ gives **−4.57%** (`…_result.md:114-115`, `ave-merger-ringdown-eigenvalue.md:85-86`).
  → **This is a live inventory finding, see §1.4-F2: the two Ω forms are different formulas,
  not two roundings of one formula.**
- **Self-consistency check that this IS v1's model**: the same forward chain at source-frame
  masses regenerates $\tau = 3.44/2.67/1.19$ ms (Resultbox) / $3.47/2.69/1.21$ ms (exact-ZAMO)
  against the asserted KB table $3.5/2.7/1.2$ ms — "to 2-sig-fig rounding" (`…_result.md:130-132`).
  So the −5.44% is a property of the standing model, not of a mis-transcription.
- **Mirror-image split** (`…_result.md:135-137`): v2 near-matches τ (+2.12%) but fails $\omega_R$
  (−9.53%); v1 wins $\omega_R$ and near-misses τ. **No mapping matches on both axes.**

### §1.3 (c) The +2.63% ω_R mean primary

Verbatim `ave-merger-ringdown-eigenvalue.md:69-72`: "On the frozen C-1 dimensionless comparator v1
sits **+2.63% mean** on the primary catalog (a\*=0.64/0.67/0.74 → +2.24/+2.50/+3.17%; *inside* the
`|D̄| < 3%` MATCH band) and **+3.36% mean** on the secondary higher-spin set (marginal, 3–5%;
overshoot grows monotonically with spin)."

Second-method confirmation, same leaf `:117` (the #774 CORRECTION block): "the retired v1 mapping
($x_{sat,v1}=7\,r_{ph}^+/3M$, entire cavity compliant) sits at **+2.24%/+2.50%/+3.17%** at
a\*=0.64/0.67/0.74 (**mean +2.63%**) — *inside* the prereg's frozen `MATCH-SURVIVES |D̄| < 3%` band".

**Sign structure worth carrying into the derivation lane:** $\omega_R$ overshoots (+2.6%) while
$Q$ undershoots (−5.4%). Since $Q = \omega_R/(2\omega_I)$, a low $Q$ at a *high* $\omega_R$ means
$\omega_I$ is **too large by ≈ +8%** — the standing model **over-damps**. Whatever the Q-law is,
it must *reduce* the loss rate (or raise $m\Omega$) at catalog spins.
*(Arithmetic-consistency observation on already-banked numbers; not a new claim, not a derivation.)*

### §1.4 (d) `r_Ω = r_ph·√(1+ν_vac)` — every site, and is it derived?

**Sites** (7 canonical + 3 driver):

| site | form |
|---|---|
| `ave-merger-ringdown-eigenvalue.md:124` | Resultbox: $r_\Omega = r_{ph}(a_*)\cdot\sqrt{1+\nu_\mathrm{vac}}$ |
| `ave-merger-ringdown-eigenvalue.md:82` | B1 ruling restatement |
| `vol2/appendices/app-f-solver-toolchain/kerr-q-correction.md:23` | $= r_{ph}\cdot\sqrt{9/7}$ |
| `common/solver-toolchain.md:103` | $= r_{ph}\cdot\sqrt{9/7}$ (mirror of app-F) |
| `app-f-solver-toolchain/index.md:20` | table row, $r_\Omega = r_{ph}\cdot\sqrt{9/7}$ |
| `app-f-solver-toolchain/derived-numerology.md:39` | $\sqrt{9/7}=1.134$, "Kerr spin evaluation radius" |
| `vol2/claim-quality.md:1097` | register rationale |
| `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:135` | driver docstring + implementation |
| `research/ligo-ringdown-driver-design.md:425,438` | design-doc statement of the τ model |

**Is the factor derived? NO — it is asserted by analogy.** The entire justification in the corpus is
one sentence, appearing twice (verbatim, `kerr-q-correction.md:26` ≡ `common/solver-toolchain.md:106`):

> "The same $\nu_{\mathrm{vac}} = 2/7$ that corrects the eigenfrequency ($r_{\mathrm{eff}} =
> r_{\mathrm{sat}}/(1+\nu)$) also corrects the spin evaluation radius ($r_\Omega = r_{ph} \cdot
> \sqrt{1+\nu}$)."

**★ FINDING F1 — the asserted parallelism is not a parallelism.** The two "corrections" have
*different functional form and opposite direction*: the eigenfrequency correction **divides** a
radius by $(1+\nu)$ (shrinks it, $\times 7/9 = 0.778$); the spin-evaluation correction
**multiplies** by $\sqrt{1+\nu}$ (grows it, $\times\sqrt{9/7} = 1.134$). No derivation in the corpus
produces the square root, and none explains the sign flip. The register agrees this is unproven —
it grades exactly this object a "**disclosed phenomenological** photon-sphere shift"
(`…_result.md:167-169`). **This is the single most likely home of the −5.4%.**

**★ FINDING F2 — two different Ω formulas are both canonical.** `kerr-q-correction.md:29` gives
$\Omega = 2a_*/(r_\Omega^3 + a_*^2 r_\Omega + 2a_*^2)$ (this is the *exact* equatorial Kerr ZAMO
rate, $2Ma/(r^3+a^2r+2Ma^2)$, in $M=1$ units), while the Ch.2 Resultbox used by the standing τ chain
is $\omega(r) = 2Mar/(r^2+a^2)^2$ (the large-$r$ / dropped-$\Delta$ form). These are **not the same
function**; they differ by the $-a^2\Delta\sin^2\theta$ term in the Boyer–Lindquist $A$. That
difference **is** the banked −5.44% vs −4.57% variant split. Flagged, not fixed — which Ω is
substrate-canonical is a physics question for Grant (see §3 Q4).

**★ FINDING F3 — $\nu_{vac}$'s VALUE is GR-IMPORTED, so no route riding it can be value-emergence.**
Verbatim `manuscript/ave-kb/common/form-deriving-value-importing.md:87`: "**K = 2G** (ν_vac = 2/7) |
**GR-IMPORTED** (echo for the value) | the substrate forces the *form* of the elastic response
`K/G = f(ρ)` | the *value* 2/7 — the GR trace-reversal identity, not crystalline-forced nor
constitutively-forced". Second-method confirmation, same file `:407`: "`ν_vac = 2/7 ← K = 2G`,
which is **itself GR-IMPORTED**". The ringdown-systematics lane already applied this rider:
"every non-pure-ratio ORG-2 number that rides `ν_vac` — `(1+ν_vac)=9/7`, the `54/77` floor, the
`0.3673` cold eigenvalue — inherits a **GR-imported value**"
(`research/2026-07-20_ringdown-systematics_derivation.md:19`).

### §1.5 (e) The Q = ℓ cold-anchor re-scope

Verbatim `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md:20-30`:

> "🟩 GRANT RULING — Q = ℓ spin-scope pinned to the cold a\*=0 anchor (2026-07-21, Ruling B1). …
> the **axiom-manifestation Nyquist content of $Q = \ell$ is UNCHANGED** … **What the B1 ruling pins
> is only its SPIN SCOPE:** $Q = \ell$ is the **cold a\*=0 anchor** — the $\Omega \to 0$
> (Schwarzschild) limit of the spin-dependent damping law $\omega_I = (\omega_R - m\Omega)/(2\ell)$
> … at catalog spins (a\*=0.64–0.74) corrected-Kerr Q rises to 3.07→3.49, so the flat $Q = \ell = 2$
> reading would **fail at $\bar D_Q = -38.18\%$**"

**Where the cold anchor comes from (this is derived, and is the anchor a Q-law must not break).**
`op21-multi-mode-mode-counting.md:82-98`: substrate Q-definition $Q = 2\pi\,E_{stored}/E_{lost\,per\,cycle}$
with a per-cycle leak fraction $1/\ell$ from the $\Gamma=-1$ TIR boundary gives $Q_{mode,\ell} = \ell$;
"(The factor-of-$2\pi$ convention divides out because the substrate's natural per-cycle quantity is
per-radian leak in angular phase.)" The $1/\ell$ leak is sourced three ways
(`op21-…:78-80`), e.g. `regime-eigenvalue-method.md:63` "Each wavelength subtends angle $2\pi/\ell$,
and the curvature radiation loss per cycle **scales as** $1/\ell$". **So the $2\ell$ in the damping
denominator IS the $Q=\ell$ mode-counting identity — it is not an independent free constant.**

**★ FINDING F7 — the leak fraction is a SCALING assertion, not a computed radiated power.** All three
sources say the per-cycle loss "**scales as** $1/\ell$"; none computes a radiation resistance or a
transmitted power through the boundary. The $\Gamma=-1$ boundary is a *perfect* reflector
(`regime-eigenvalue-method.md:63`), so in the corpus the loss is not sourced at the boundary at all
— it is attributed to curvature radiation from the orbiting mode. The proportionality **constant** in
$E_{lost}/E_{stored} = c_1/\ell$ is set to exactly 1 by the $2\pi$-divides-out convention
(`op21-…:96`). A Q-law that computes the leak would fix $c_1$ from substrate impedance rather than
convention — and $c_1 \ne 1$ is a candidate ≈8% home for the tension (see §2 Route R2).

### §1.6 (f) Prior derivation attempts and their outcomes

| attempt | date | outcome |
|---|---|---|
| **v1** entire-cavity-compliant $\omega_R$ mapping | pre-2026-05-18 | retired for v2 on a **frame-mixed + corrupt-table** diagnosis; that retirement RETRACTED 2026-07-20 (`eigenvalue leaf:115-117`); **v1 RE-SELECTED** by Ruling B1 |
| **v2** Cosserat back-reaction $x_{sat}=2+5r_{ph}^+/3M$ | 2026-05-18 | post-hoc fit against LIGO; $\omega_R$ **fails** at −9.53% dimensionless; preserved verbatim as superseded (Rule 12) |
| **Op21 mode-counting formalization** of $Q=\ell$ | 2026-05-27 (Phase 3-A4) | **SUCCEEDED** — but only delivers the $a_*=0$ cold anchor; carries no spin dependence |
| **Model A** (flat $Q=\ell$ at catalog spins) | 2026-07-20 | **FAILS decisively**, $\bar D_Q = -38.18\%$ (`…_result.md:26-27`) |
| **Model B** Ω-pinning repair (PR #776 finding 0) | 2026-07-20 | Ω shown **corpus-pinned, not undetermined**; Model B computed → τ-FAILS at −5.44%/−4.57%. The prior "UNDETERMINED — Ω not numerically pinned anywhere" was a **false corpus-completeness claim from a numeric-literal grep that cannot see a formula pin** (`…_result.md:141-146`) |
| **Ringdown-systematics ORG-1** (mode-ratio locking) | 2026-07-20 | derived: $\omega_R(\ell')/\omega_R(\ell)$ is spin-independent EXACTLY ($x_{sat}$ and $(1+\nu_{vac})$ cancel); **point value fork-banded 1.41–1.50**, not 1.50 unconditionally |
| **Ringdown-systematics ORG-2** (sign/floor) | 2026-07-20 | sign/floor content **RETRACTED** in the same lane |

**★ FINDING F4 — an OPEN upstream fork the Q-law inherits.** The linear-$\ell$ mode form
$\omega_R = \ell c/r_{eff}$ is **asserted-not-derived**; the spherical-membrane alternative
$\omega \propto \sqrt{\ell(\ell+1)}$ is live and binned UNDETERMINED
(`research/2026-07-20_ringdown-systematics_derivation.md:41-44`, quoting
`ave-merger-ringdown-eigenvalue.md:16`). This matters for the Q-law because the **same $\ell$**
appears in the numerator ($\omega_R \propto \ell$) and the damping denominator ($2\ell$). If the
mode form is $\sqrt{\ell(\ell+1)}$, the cold $Q$ is not $\ell$.

**★ FINDING F5 — the three-way Q tension is still OPEN and un-discharged.** Verbatim
`…_result.md:152-156`: "Three corpus statements about Q still need reconciling:
`qnm-quality-factor.md` says `Q = ℓ` (spin-independent); `ave-merger-ringdown-eigenvalue.md` says Q
*"increases with spin"*; Phase-5 (`ligo-ringdown-driver-design.md` §10) says Q is *v1/v2-invariant*.
Model A instantiates the first, Model B the second; they give −38% and −5% respectively, so the two
are **not the same physics** and the three-way tension is real. A single pinned τ story needs these
reconciled first. Surfaced, not resolved." Ruling B1 discharged (1) and (3) by scoping/retraction;
the derivation lane should confirm rather than assume the reconciliation is complete.

### §1.7 Honesty-lag flag — a stale "sub-2% / zero free parameters" premise the derivation lane would inherit

**★ FINDING F6 (flag-don't-fix; reconcile with the in-flight propagation lane — NOT touched here).**
The 2026-07-20 "sub-2% RETRACTED" banner landed on `ave-merger-ringdown-eigenvalue.md:127` but did
**not** propagate. **State as of `origin/main` = `f7cc3e52` (2026-07-30):** **six** un-bannered sites
still assert the retracted accuracy claim, most of them also calling it zero-free-parameter.

| # | site (at `f7cc3e52`) | verbatim content |
|---|---|---|
| 1 | `manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/kerr-q-correction.md:37` | "this formula reproduces the quality factor to **sub-2%** with zero free parameters" + the $Q_{AVE}$ vs $Q_{GR}$ table at `:39-45` (2.24/2.54/3.02/3.75/4.93 vs 2.25/2.54/3.01/3.81/5.23) computed against the **corrupt** Kerr reference. No retraction banner anywhere in that file (`grep -n "RETRACT\|SUPERSED\|🔴" kerr-q-correction.md` → 0 hits). |
| 2 | `manuscript/ave-kb/common/solver-toolchain.md:116` | same sentence, "reproduces the GR quality factor to **sub-2%** with zero free parameters". No banner. |
| 3 | `manuscript/ave-kb/vol2/claim-quality.md:1097` | "sub-2% accuracy across $a_* = 0.3$–$0.8$". |
| 4 | `manuscript/ave-kb/common/claim-quality.md:136` | "The Kerr $Q$ correction (co-rotating frame decomposition) reproduces GR to sub-2% for $a_* \in [0.3, 0.8]$." — filed under `_Specific Claims_`. |
| 5 | `manuscript/backmatter/05_universal_solver_toolchain.tex:101` | "this formula reproduces the GR quality factor to \textbf{sub-2\%} with zero free parameters". `grep -c "RETRACT\|SUPERSED\|🔴"` on that file → **0**. |
| 6 | `src/ave/solvers/orbital_resonance.py:485` | code comment "`a* = 0.3–0.8: Q error < 2% vs GR (LIGO observing band)`". |

**Why the count was wrong the first time — a grep-completeness false negative.** Site 6 says
"**< 2%**", not "sub-2%"; a single-pattern `grep "sub-2"` cannot see it. Sites 4 and 5 were missed by
scoping the grep to the KB subtree that the eigenvalue leaf lives in rather than to
`manuscript/` + `src/`. The two-method rule that caught the first three has to include a
**pattern**-variant second method, not only a **file**-variant one.

**Companion overclaim riding the same sentence (not a "sub-2%" string, so a `sub-2` grep misses it
entirely).** Four sites assert superradiance as first-principles-derived:
`kerr-q-correction.md:33` ≡ `common/solver-toolchain.md:113` ≡
`backmatter/05_universal_solver_toolchain.tex:98` — verbatim "This is the first-principles prediction
of superradiance from pure lattice geometry" — plus `vol2/claim-quality.md:1097` ("with superradiance
recovered from first principles at $\omega_R = m\Omega$"). Superradiance there is the
$\omega_R = m\Omega \Rightarrow \omega_I \to 0$ root of the **same grafted Park-transform law** whose
$Q$ this lane finds at −5.4%; "first-principles" is doing the same work "zero free parameters" was.
Flagged in the same bin, not adjudicated here.

**Partially mitigated (do not double-count as un-bannered):** `manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex`
carries the retracted figures at `:271` (which *quotes* "matches GR sub-2\% only for $a_* = 0.3$--$0.8$"
from the `clm-395gps` caveat that `vol3/claim-quality.md:204` has since struck 🔴) and at `:387`
(the same $a_*=0.3$–$0.8$ validation-scope restatement, plus "cold-cavity forward prediction (zero
free parameters)" — no literal "sub-2%" string on that line). Both sit under the Ruling-B1 number-
correction banner at `:31` and per-occurrence `#780` pointer comments at `:270` / `:289`. Mitigated
at the section level, un-reconciled at the occurrence level — the tex file's own pointers route it to
"the manuscript-reconciliation program".

This directly contradicts the load-bearing leaf's own grade ("solidity 0.55 …
disclosed-phenomenological … NOT a zero-free-parameter benchmark", `eigenvalue leaf:72-76`) and the
banked −5.44% Q deviation. A derivation lane that reads app-F or the backmatter as canon would start
from a false premise (that the Q-law already matches to sub-2% with zero parameters) and would
therefore have no tension to explain.

**Routing — reconcile, don't re-open.** A B1-retraction propagation lane is **in flight** on branch
`docs/b1-retraction-propagation` (local at `014d2cf5`; **not** pushed and **no** PR open as of
2026-07-30 — verified via `git ls-remote origin refs/heads/docs/b1-retraction-propagation` → empty
and `gh pr list --state all` → no PR on that head). This F6 list is therefore **not** new
auditor-lane work to route; it is a **reconciliation input** to that lane: sites 1–3 are the ones
already named in the earlier three-site version of this finding, and sites 4–6 + the four
superradiance sites are the additions this pass verified. Whoever lands that lane should diff its
touched-file set against this table and against a `< 2%` / `first-principles` pattern sweep, not only
a `sub-2%` one. **State is as-of-`f7cc3e52`; re-verify at that lane's ship time** (branch state moves
between authoring and shipping).

---

## §2 — Candidate derivation routes (enumerated, NOT pursued)

### §2.0 ★ FINDING F8 — a decomposition the derivation lane must see before choosing a route

The Ruling-B1 queue item names the suspect: verbatim
[`_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md:109`](../_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md):
"**Q-law derivation** (why the standing-v1 mΩ τ lands at −5.4%: the `r_Ω = r_ph·√(1+ν_vac)` / `ν_vac`
factor / mapping — the named next ringdown work banked by Ruling B1)".

**That suspect cannot carry most of the deficit.** Arithmetic on already-banked corpus numbers only:

- At $a_* = 0$ the standing model gives $\Omega = 0$, so $\omega_I = \omega_R/(2\ell)$ and
  $Q_{AVE} = \ell = 2$ **exactly** — $r_\Omega$, $\sqrt{1+\nu_{vac}}$ and $\Omega$ have all dropped
  out of the calculation.
- Corpus-sourced GR Schwarzschild $\ell=2$ references: $\omega_R M = 0.3737$
  (`manuscript/ave-kb/vol3/claim-quality.md:199` — "vs GR exact $0.3737$, **error 1.7%**") and
  $\omega_I M = 0.0890$ (`qnm-quality-factor.md:18` — "GR exact: $0.0890$, error $3.2\%$").
  → $Q_{GR}(a_*{=}0) = 0.3737/(2\times 0.0890) = 2.0994$.
- So the **cold** $Q$ deficit is $2/2.0994 - 1 = \mathbf{-4.74\%}$.
- The banked **catalog** deficit is $\mathbf{-5.44\%}$ mean (−5.76 / −5.53 / −5.02).

**The Q deficit is very nearly spin-FLAT: ≈ −4.7% at $a_*=0$, ≈ −5.4% at $a_*\approx0.68$.**
Roughly **87% of the banked −5.44% is already present at zero spin**, where the named suspect
($r_\Omega$, $\sqrt{1+\nu_{vac}}$, the spin mapping) is *absent from the arithmetic*. The
spin-refined mΩ law is therefore doing its job well — it tracks the Kerr $Q$ *rise* (3.07→3.49) to
about a percentage point — and what remains is **an offset inherited from the cold anchor itself.**

> **FLAG (don't fix) — routed to Grant/auditor.** The queue text and the eigenvalue-leaf ruling both
> point the next work at `r_Ω`/`ν_vac`/mapping (`ave-merger-ringdown-eigenvalue.md:88-89`: "why
> −5.4%: the $r_\Omega$ / $\nu_{vac}$ factor / mapping"). The decomposition above says the dominant
> term lives instead in the **cold $Q = \ell$ anchor** — i.e. in the $1/\ell$ leak-fraction
> convention (F7), not in the spin machinery. **Class of this statement: arithmetic-consistency
> observation on banked corpus numbers** (same class as §1.3), **NOT a derivation and NOT a claim.**
> It is offered as hypothesis **H1** for the derivation lane to test, and as a re-pointing candidate
> for the queue item. Surfaced with receipts; not resolved here.

Corollary for route selection: a route that only repairs $r_\Omega$ has a **ceiling of ≈0.7 pp** of
the 5.44 pp. Routes must reach the cold anchor to be capable of closing the tension.

### §2.1 Cross-cutting class ceiling (consistency-vs-emergence, applies to EVERY route)

Because $\nu_{vac} = 2/7$'s **VALUE** is GR-IMPORTED via $K = 2G$ (F3), and $r_{sat} = 7GM/c^2$ and
$r_{eff} = 49M_g/9$ both ride it, **no route below can produce a value-level EMERGENCE claim for an
absolute $Q$ or $\omega$.** The best available class for absolutes is **FORM-emergence /
VALUE-consistency**. The only emergence-capable objects are **$\nu_{vac}$-free dimensionless
ratios** — and "dimensionless ratio" is **not** the test; **$\nu_{vac}$-cancellation is**, and it has
to be checked per-candidate rather than assumed:

- **$\omega_R(\ell')/\omega_R(\ell)$ — SURVIVES.** Genuine cancellation: $\omega_R M_g =
  \ell(1+\nu_{vac})/x_{sat}$, so the ratio is $\ell'/\ell$ with both $x_{sat}$ and $(1+\nu_{vac})$
  gone. Corroborated in canon-adjacent research:
  `research/2026-07-20_ringdown-systematics_derivation.md:45` — "it is genuinely exact and
  spin-independent (the `x_sat` and `(1+ν_vac)` cancellation holds at all spins for ORG-1)".
- **$Q(a_*)/Q(0)$ — ★ STRUCK (repair-pass correction). It does NOT cancel $\nu_{vac}$.** Under the
  standing model $Q = \ell/(1 - m\Omega/\omega_R)$ and $Q(0) = \ell$, so
  $Q(a_*)/Q(0) = 1/(1 - m\Omega/\omega_R)$ — a ratio in which **both** factors carry $\nu_{vac}$:
  $\omega_R$ rides $(1+\nu_{vac})$ in its numerator, and $\Omega$ is evaluated at
  $r_\Omega = r_{ph}\sqrt{1+\nu_{vac}}$. Nothing divides out. Recomputed on the frozen driver's own
  chain (`research/2026-07-20_v1-spin-mapping-adjudication_rerun.py`, reproducing its banked
  −5.76/−5.53/−5.02% row-for-row): at $a_*=0.67$ the ratio is **1.500** at $\nu_{vac}=2/7$ versus
  **2.492** at $\nu_{vac}=0$ — a **+66%** swing (0.64: 1.447 → 2.261, +56%; 0.74: 1.656 → 3.347,
  +102%). A "$\nu_{vac}$-free" object cannot move by 66% when $\nu_{vac}$ is set to zero. It is
  removed from the emergence-capable list wherever it appeared (§2.1 here, Route R2's class line,
  and the docket entry).
- **(Route R3) echo-delay-to-ringdown-period ratio — UNTESTED, must be checked before it is
  headlined.** Both legs are lengths/times inside the same $\nu_{vac}$-scaled cavity, so cancellation
  is *plausible* — but that is exactly the reasoning that failed for $Q(a_*)/Q(0)$. The pre-reg must
  carry the explicit $\nu_{vac} \to 0$ sensitivity computation, not the plausibility argument.

**The discipline this corrects:** the standing "the chord must be a dimensionless ratio" rule is
necessary, not sufficient. Dimensionlessness is cheap; **cancellation is the actual requirement**, and
the way to establish it is to re-run the chain at $\nu_{vac}=0$ and show the number does not move.
That $\nu_{vac}\to0$ sensitivity run belongs in the derivation pre-reg header per candidate ratio, not
discovered afterwards.

### §2.2 Route R1 — Radiation-resistance leaky-cavity Q in the SHEAR channel

**The electron-template route.** Replace the scaling assertion "loss per cycle scales as $1/\ell$"
(F7) with a **computed radiation resistance** at the port, exactly as the electron tank does it.

- **Consumes from canon:** the Q template
  `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:40-42`
  ($Q_{tank} = \omega_C L_e / R$ at "the impedance-matched boundary $R = Z_0/(4\pi)$", where
  `:79-83` derives $Z_0/(4\pi)$ as "radiation impedance averaged over one full observable Compton
  cycle") — clm-rtdmsn / clm-0ktpcn; the port-class licence
  `manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md:100` verbatim:
  "the **RADIATIVE-PORT** class ($R_{\text{rad}} \equiv Z_0$, `requires_R = port-only`), which is
  **Axiom-3-LICENSED** loss"; the channel law $Z_{shear} = \rho\,c_{shear}$
  (`manuscript/ave-kb/vol3/claim-quality.md:122`).
- **What it would predict:** $Q = c_1\,\ell$ with $c_1$ **computed** from the shear-channel radiation
  resistance instead of set to 1 by the $2\pi$-divides-out convention. H1 says the target is
  $c_1 \approx 1.05$. It would also predict the analogous $\ell$-dependence, i.e. a check against
  the GR overtone/$\ell>2$ structure that $Q=\ell$ currently "disagrees with" (register rationale).
- **Class if it lands:** FORM-emergence, VALUE-consistency (per §2.1). The *ratio* $c_1$ is
  potentially $\nu_{vac}$-free and would be the emergence-capable object.
- **What would falsify it:** the computed $c_1$ lands at $1.00$ (then the tension is not here and H1
  is wrong); or $c_1$ carries the wrong sign (a route that makes $Q$ *smaller* deepens the deficit);
  or the computation requires a bulk $\mathrm{Re}(Z)$ (Ax 3 violation → route is illegal, not merely
  wrong).
- **Sector check:** must stay in the **shear** channel. The electron template uses $Z_0 \equiv Z_{EM}$;
  transplanting $Z_0$ into a GW problem is exactly the category error the corpus already caught twice
  (`gw-impedance-perturbation.md:18`, `invariant-gravitational-impedance.md:30`). **This is the
  route's main leak risk.**

### §2.3 Route R2 — Graded-$Z_{shear}$ turning-point (WKB) Q

**The honest-profile route.** The corpus models the boundary as a *hard* wall at $r_{sat}$ with
$\Gamma_{shear} = -1$; but $Z_{shear}(r) = \rho\,c_0\,(1-A^2(r))^{1/4}$ is a **continuous grade**
(`saturating-modulus-and-backreaction.md:60` verbatim: "**SHEAR softens:**
$c_{\text{shear}}=c_0\sqrt{S}=c_0(1-A^2)^{1/4}\to0$ — a **derived** $\sqrt{S}$ projection").
A graded resonator's $Q$ is set by **barrier transmission at a turning point**, not by mode-counting.

- **Consumes:** the Ax-4 kernel $S = \sqrt{1-A^2}$ and the $c_{shear}$ projection above;
  $Z_{shear} = \rho c_{shear}$; Op14 local-clock $\omega_{local}(r) = \omega_{global}\sqrt{1-A^2(r)}$
  (`op14-cosmic-horizon-profile.md:43`).
- **★ FINDING F9 — a live CANON INCONSISTENCY, not a gap. R2 is NOT blocked.**
  *(Repair-pass correction. The first version of this finding asserted that "$A^2(r)$ has no
  canonical radial profile … targeted greps in `ch01-gravity-yield/` and `ch02-general-relativity/`
  return zero hits." **That absence claim is FALSE** — the same absence-direction
  `verify-before-cite` trigger-6 failure that under-counted F6. The pinning is in the second of those
  two directories, and the grep that "returned zero hits" was pattern-scoped to `A^2 = …` while canon
  writes the identification on **$A$**, not $A^2$. Corrected below with receipts.)*

  **The shear-channel profile IS canonically pinned, in two lines:**
  - `vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md:51` — Resultbox,
    verbatim: `\qquad A=\varepsilon_{11}/\varepsilon_{\text{yield}}\ (\varepsilon_{\text{yield}}=1),`
    → i.e. **$A = \varepsilon_{11}$**, with the one Op14 kernel $S(A)=(1-A^2)^{1/2}$ at `:52`.
  - `vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md:14` — "The principal
    radial strain $\varepsilon_{11} = 7GM/(c^2 r)$ compresses the lattice asymmetrically" (clm-rd9cjm).
  - Third-site corroboration, `common/vocabulary-register.md:309`: $\varepsilon_{11} = 7GM/(c^2 r)$ is
    "the A1-dilatation **radial 'strain' that IS the Axiom-4 saturation amplitude $A$**".
  - And the shear projection rides **the same $A$**: `saturating-modulus-and-backreaction.md:60`
    "$c_{\text{shear}}=c_0\sqrt{S}=c_0(1-A^2)^{1/4}\to0$".

  ⇒ $A(r) = 7GM/(c^2 r)$, $A = 1$ exactly at $r_{sat} = 7GM/c^2$, and
  $c_{shear}(r) = c_0\,[1-(7GM/c^2r)^2]^{1/4} \to 0$ at $r_{sat}$. **That is R2's integrand, in canon,
  with no free function.**

  **What is genuinely inconsistent (the real F9).** A *second* convention is also canonically stated,
  on the temporal/EM side: `temporal-spatial-lattice-decomposition.md:24` and the W2 walk-back at
  `:28` both give the local clock as $\sqrt{g_{00}} = \sqrt{S} \approx 1 - GM/(c^2 r)$, i.e.
  $S \approx 1 - r_s/r$. That cannot be the same $A$: it puts $A \to 1$ at a radius of order
  $r_s = 2GM/c^2$ (the 3.5× discrepancy already banked here) **and** it makes $A \propto 1/\sqrt{r}$
  rather than the $A \propto 1/r$ of $\varepsilon_{11}$ — the two conventions disagree on the yield
  *surface* and on the *functional form*. Both are canonically asserted. The convention-split leaf
  `vol4/circuit-theory/ch1-vacuum-circuit-analysis/q-g22-strain-convention.md:10` resolves the
  *electron/Coulomb* $A$ ($A_{\text{geom}}$ vs $A_{\text{field}}$) and is **silent on the
  gravitational case** — `vocabulary-register.md:309` says so in as many words.

  **Why R2 un-blocks anyway — the channel-split decides it.** `vol3/claim-quality.md:121` (verbatim,
  one line above the `:122`/`:123` lines already quoted in §2.2/§2.4) splits the surface **by
  channel**: "The event horizon at $r_s = 2GM/c^2$ marks the **EM-transverse** saturation limit
  ($n \to \infty$, $\varepsilon_{11}(r_s) = 1$ in the GW-gauge transverse formulation); the
  **shear/bulk** rupture boundary is deeper, at $r_{sat} = 7GM/c^2 = 3.5\,r_s$ where the radial strain
  $\varepsilon_{11} = 1$". So the $r_s$-surface convention is the **EM-transverse** reading and the
  $r_{sat}$-surface convention is the **shear/bulk** reading — and this document's own §1.0 SECTOR
  header declares the ringdown a **shear (T2-channel) cavity mode**. R2 therefore takes
  $A = \varepsilon_{11} = 7GM/(c^2 r)$ and is **executable**.

- **R2's remaining prerequisites (both narrow, neither a blocker):** (i) confirm the channel-split
  reading with Grant (§3 Q3, now a confirm-note not a walk question) — the residual is the
  kernel-argument **power**, $A = \varepsilon_{11}$ (per `:51`) vs $A^2 = \varepsilon_{11}$ (as this
  doc's own first draft wrote it); `:51` pins $A = \varepsilon_{11}$ for the **A1/radial-bulk**
  Resultbox and `:60` projects the *same* $A$ into shear, so the power looks settled, but `q-g22` does
  **not** settle the gravitational case and the reading should be confirmed, not assumed. (ii) the
  open $S$-exponent flag at `vol3/gravity/ch02-general-relativity/k4-tlm-lensing-validation.md:25-35`,
  which is exactly R2's WKB integrand.
- **What it would predict:** $Q$ from a barrier integral $\propto \exp(2\int|k|\,dr)$, which is
  intrinsically both $\ell$- and $a_*$-dependent — so it could in principle deliver the cold offset
  *and* the spin trend from one mechanism (addressing F5 at the root).
- **Class if it lands:** FORM-emergence; absolute values still VALUE-consistency per §2.1. **No
  emergence-capable ratio is named for this route** — $Q(a_*)/Q(0)$ was the candidate and it is
  **struck** (§2.1: it does not cancel $\nu_{vac}$; +66% swing at $\nu_{vac}\to0$). Worse for R2 than
  for the standing model: R2's profile *is* $A = \varepsilon_{11} = 7GM/(c^2r)$, whose $7$ is the
  $\nu_{vac}$-riding $r_{sat}$ coefficient, so the barrier integral carries $\nu_{vac}$ through the
  integrand itself. Any ratio proposed off this route needs its own $\nu_{vac}\to0$ sensitivity run.
- **What would falsify it:** the barrier integral lands $\gg 5\%$ from GR; or $A^2(r)$ turns out to
  be a free function chosen to fit (then the route is a re-parameterised fit, not a derivation, and
  must be reported as such); or the graded profile destroys the clean $Q=\ell$ cold anchor that
  Ruling B1 just pinned (a route that breaks a ratified anchor is a **flag**, not a fix).

### §2.4 Route R3 — Light-ring barrier-transmission cavity (the echo-coupled route)

**The route that could retire F1 instead of patching it.** In GR the ringdown $Q$ *is* the light-ring
barrier's property. AVE's $r_{ph}^+(a_*)$ already appears in **both** $x_{sat,v1}$ **and** $r_\Omega$
— a tell that the photon sphere is doing load-bearing work that the corpus attributes to a
"phenomenological shift." Reframe: the cavity is bounded **inside** by the $\Gamma_{shear} = -1$
mirror at $r_{sat}$ and **outside** by the light-ring potential barrier; $Q$ = round-trip phase /
barrier leakage.

- **Consumes:** $r_{ph}^+(a_*)$ (`ave-merger-ringdown-eigenvalue.md:110`); the two-channel instrument
  ($\Gamma_{shear} = -1$, $\Gamma_{EM} = 0$, `electron-bh-isomorphism.md:34-42`); and the corpus's
  **own already-banked echo prediction** — verbatim `manuscript/ave-kb/vol3/claim-quality.md:123`:
  "GW (transverse shear) modes therefore reflect off $r_{sat}$ — gravitational ringdown **echoes are
  predicted** (reflect $\Rightarrow$ echo; retrospective, no SHA-pinned forward prereg yet)".
- **What it would predict:** (i) a $Q$-law with **no free radius factor** — the evaluation radius
  becomes the *computed* barrier-peak / turning-point radius, so $r_\Omega = r_{ph}\sqrt{1+\nu_{vac}}$
  is either **derived or replaced** (this is the only route that removes F1 rather than re-justifying
  it); (ii) as a by-product, an **echo delay** $\Delta t \approx 2\int dr/c_{shear}$ between $r_{sat}$
  and the barrier — an independent, already-searched-for LIGO observable.
- **Class if it lands:** FORM-emergence for the $Q$-law; the **echo-delay-to-ringdown-period ratio is
  a genuine forward, $\nu_{vac}$-sensitive-but-ratio-structured chord candidate** — the highest-value
  by-product of the whole Q-law item.
- **What would falsify it:** the round-trip $Q$ lands nowhere near $\ell$ at $a_*=0$ (breaks the
  ratified cold anchor); or the implied echo delay is already excluded by published LIGO echo-search
  limits (**a clean kill, and a good one** — and note it would be a kill of an *existing banked
  corpus prediction*, so this route carries real downside risk for the corpus and must be pre-reg'd
  with that bin reachable).
- **Discipline note:** R3 must respect the KERR-WORDING FENCE already riding this arc
  (`research/2026-07-20_ringdown-systematics_derivation.md:14`) — GR QNMs are $(M,a)$-determined;
  R3 is an organizer for the AVE $Q$, never a replacement for the Kerr spectrum.

### §2.5 Route R4 — Op21 mode-counting re-derived in the co-rotating frame

**The route that addresses F5 at the root.** The cold $Q=\ell$ is a Nyquist-cell mode-counting
identity (`op21-multi-mode-mode-counting.md:82-98`). The spinning law
$\omega_I = (\omega_R - m\Omega)/(2\ell)$ is *grafted on* as a Park-transform decomposition
(`kerr-q-correction.md:49-61`), not obtained from the same counting. R4 asks: **redo the
Nyquist-cell count in the co-rotating frame** and see what damping law falls out.

- **Consumes:** Op21's five-step chain (Ax 1 Nyquist cell size → Ax 3 + Ax 4 forcing $\Gamma=-1$ →
  per-cycle leak $1/\ell$ → $Q_{mode,\ell} = \ell$ → cell-count = geometric measure); the FOC/Park
  analogy table as the *hypothesis to test*, not as the derivation.
- **What it would predict:** either (a) exactly $(\omega_R - m\Omega)/(2\ell)$ — in which case the
  spin law is **derived rather than analogised**, a real solidity upgrade even though it moves no
  number; or (b) a different law (e.g. leak-per-*co-rotating*-radian, which changes the count when
  the boundary itself spins), which would move the spin-dependent ≈0.7 pp.
- **Class if it lands:** FORM-emergence, and **$\nu_{vac}$-free only in its COLD half.** The
  mode-counting content (Ax 1 cell size + topology → $Q_{mode,\ell} = \ell$) genuinely carries no
  elastic value: at $a_*=0$, $Q = \ell$ with no $\nu_{vac}$ anywhere. **But the co-rotating spin term
  is not $\nu_{vac}$-free** — it enters as $m\Omega/\omega_R$, and $\Omega$ is evaluated at
  $r_\Omega(\nu_{vac}) = r_{ph}\sqrt{1+\nu_{vac}}$ while $\omega_R$ rides $(1+\nu_{vac})$. R4 inherits
  both unless it **also re-derives the evaluation radius** from the co-rotating count instead of
  importing $r_\Omega$ — which is worth stating as an R4 sub-goal, because a co-rotating Nyquist count
  that produces its own evaluation radius would simultaneously discharge F1. **Honest statement of the
  ceiling:** R4 has the cleanest ceiling *at the cold anchor*; at catalog spins its class is the same
  VALUE-consistency as every other route unless the $r_\Omega$ import is eliminated. (Struck: the
  earlier blanket "R4 is the route with the cleanest class ceiling" — it was true only of the half of
  R4 that has no spin in it.)
- **What would falsify it:** the co-rotating count is frame-ambiguous (no unique cell count in a
  rotating frame → route is ill-posed); or it reproduces the existing law exactly *and* H1 is right,
  in which case R4 legitimises the spin law but explains none of the tension.

### §2.6 Route R5 — Ω-form adjudication (canon hygiene; run FIRST, but NOT a derivation)

F2 established that two different $\Omega$ formulas are both canonical. R5 is simply: decide which
one is the substrate's frame-dragging rate.

- **Consumes:** `frame-dragging-impedance-convolution.md:15` ($\omega = 2Mar/(r^2+a^2)^2$, clm-rd9cjm)
  vs `kerr-q-correction.md:29` ($\Omega = 2a_*/(r_\Omega^3 + a_*^2 r_\Omega + 2a_*^2)$, clm-d9ivj1).
- **What it decides:** whether the banked number is **−5.44%** or **−4.57%**.
- **Class:** none — this is an **adjudication/hygiene item**, not a hypothesis. It cannot close the
  tension (0.9 pp of 5.44 pp) but everything downstream inherits the choice, so it should be settled
  before any route is executed.
- **★ Rule-11 fence, explicit:** choosing the exact-ZAMO form *because* −4.57% is closer to the band
  is **RETUNING and inadmissible.** The choice must be made on substrate grounds (which rate is the
  physical impedance-convolution rate at $r_\Omega$), and the resulting number is then whatever it is
  — including "still outside the band."

### §2.7 Route R6 — Mode-form fork (prerequisite, not a route)

F4's open fork (linear-$\ell$ vs $\sqrt{\ell(\ell+1)}$) sets **both** the $\omega_R$ numerator and the
$2\ell$ damping denominator, so no $Q$-law is well-posed until it is resolved. Note the fork is
*probably* already decided on $\omega_R$ grounds — the $\sqrt{\ell(\ell+1)}$ form would move the cold
eigenvalue from $0.3673$ to $\approx 0.4498$ against GR's $0.3737$ (a ≈+20% error vs the standing
−1.7%) — but that inference is **not** in the corpus and the fork is formally binned UNDETERMINED
(`research/2026-07-20_ringdown-systematics_derivation.md:41-44`). Resolve, don't assume.

### §2.8 Route R0 — no route closes (must stay reachable)

Honestly enumerated: if R1 returns $c_1 = 1.00$, R2's barrier integral lands nowhere near GR, R3's echo delay is excluded
or its cold limit breaks the anchor, and R4 merely reproduces the grafted law, then **nothing closes.**
That outcome is a **result**, not a failure: v1 stays at solidity 0.55, `build_status "use as input
only"`, disclosed-phenomenological, and the −5.4% is banked *deeper* — with the F8 decomposition
naming the mechanism honestly ("the offset is the cold $Q$ anchor's own ≈−4.7%, not the spin
mapping"). Naming the mechanism is worth more than moving the number.

---

## §3 — The Grant walk (pre-test-physics-check; must happen IN CHAT before any derivation fires)

Per Rule 16 strengthening: these are asked **before** design, not after 30 commits return Mode III.
One question per load-bearing noun. Sector-declaration header for the whole walk: **shear (T2)
channel, saturated boundary, Op14 ON, $\Gamma_{shear}=-1$, cold-reactive far field.**

**Count after the repair pass: SEVEN walk questions (Q1, Q2, Q4–Q8) + one demoted confirm-note (Q3).**
Q3 was drafted as a walk question on a false premise and is demoted rather than deleted — the residual
it still carries is narrow and is stated in place.

### Q1 — THE ontology one-liner: what IS the ringdown, physically, in the substrate?

Three mutually exclusive pictures are all *implied* somewhere in canon, and they route to different
derivations:

- **(i) A leaky cavity with a radiative port.** The mode is trapped between $r_{sat}$ and infinity;
  the "loss" is a real external port ($R_{rad}$, Ax-3-licensed) and $Q$ is stored reactance over port
  resistance. → Route R1. *Plumber picture: a bell with a small hole drilled in it.*
- **(ii) An impedance-mismatch ring-down on a graded profile.** No hole at all — the mode sits in a
  continuously graded $Z_{shear}(r)$ well and leaks by **tunnelling past a turning point**. $Q$ is a
  barrier-transmission integral. → Route R2/R3. *Plumber picture: a water-hammer surge in a pipe
  whose diameter tapers — it reflects off the taper, not off a valve.*
- **(iii) A mode-conversion drain.** The shear mode converts into another channel (bulk/A1, or EM) at
  the boundary and *that* is where the energy goes. → not currently a corpus route at all.
  *Plumber picture: the ring dies because it couples into the mounting bracket.*

**Ask Grant:** which one is it? And is it exactly one, or does the corpus need to say "(i) at the
port AND (ii) at the taper" — because if it's both, $Q^{-1}$ is a **sum of two loss terms** and the
whole $Q=\ell$ single-channel derivation is under-counting. *(Note: Op21 explicitly classifies BH
ringdown as **single-channel**, `op21-multi-mode-mode-counting.md:31,36` — so "both" would be a
substantive correction to a ratified leaf, not a detail.)*

### Q2 — the noun "$\Gamma_{shear} = -1$": is the reflector *perfect*, and if so where does the energy go?

Canon says the saturated interior is a **perfect** reflector for shear waves
(`electron-bh-isomorphism.md:36`) — $|\Gamma| = 1$, zero transmitted. But the ringdown *decays*.
Canon resolves this by attributing the loss to **curvature radiation from the orbiting mode**
(`regime-eigenvalue-method.md:63`), i.e. to the *outward* side, not the boundary.

**Ask Grant:** in the plumber picture, is the ringdown's decay (a) radiation *outward* to infinity
from a mode that is perfectly mirrored inward, or (b) leakage *inward* through an imperfect mirror?
If (a) — and canon says (a) — then **the $Q$ is set entirely by the outer radiation impedance and
the $\Gamma_{shear}=-1$ inner mirror contributes nothing to $Q$ at all**, which makes the current
derivation's attribution ("$Q$ from the $\Gamma=-1$ saturation/TIR boundary") a mislabel of where
the physics lives.

### Q3 — DEMOTED to a confirm-the-channel-split note (was: "what is $A^2(r)$?"; F9, R2)

**Demoted in the repair pass.** This was drafted as a full walk question on the premise that $A(r)$ had
no canonical profile. That premise was wrong (see §2.3 F9): canon pins
$A = \varepsilon_{11} = 7GM/(c^2 r)$ (`saturating-modulus-and-backreaction.md:51` +
`temporal-spatial-lattice-decomposition.md:14`, corroborated `vocabulary-register.md:309`), and
`vol3/claim-quality.md:121` **already channel-splits** the two conflicting surfaces — $r_s$ is the
**EM-transverse** saturation limit, $r_{sat} = 3.5\,r_s$ is the **shear/bulk** rupture boundary. The
ringdown is declared shear/T2 in §1.0. Grant has, in effect, already answered "two surfaces, one per
channel."

**What is left to confirm (a note, not a walk):** (i) that the channel-split reading is the intended
one for a *graded* (not hard-wall) shear profile; and (ii) the narrow residual — the kernel-argument
**power**: $A = \varepsilon_{11}$ (what `:51` writes) vs $A^2 = \varepsilon_{11}$ (what this doc's own
first draft assumed). `:51` + the `:60` shear projection read as $A = \varepsilon_{11}$;
`q-g22-strain-convention.md:10` splits the *electron/Coulomb* $A$ and is silent on the gravitational
case, so this is not settled by fiat elsewhere. The difference is not cosmetic — it moves the
weak-field falloff of the WKB integrand by one power of $r$.

*Plumber picture retained (it is the right one): is there one wall, or a soft yield zone standing off a
hard wall? Canon's answer is the second, per channel — light stops at the hard wall, shear stops at the
yield zone $3.5\times$ further out.*

### Q4 — the noun "$\Omega$": which rate is the substrate's frame-dragging? (F2, R5)

Two canonical formulas: $\omega(r) = 2Mar/(r^2+a^2)^2$ (Ch.2 Resultbox, clm-rd9cjm) and
$\Omega = 2a_*/(r_\Omega^3 + a_*^2 r_\Omega + 2a_*^2)$ (app-F, clm-d9ivj1 — the exact equatorial
Kerr ZAMO). The second is the exact GR object; the first drops the $-a^2\Delta\sin^2\theta$ term.

**Ask Grant:** the corpus calls $\Omega$ "the asymmetric impedance convolution rate (formerly
interpreted as Lense–Thirring angular velocity)" (`ave-merger-ringdown-eigenvalue.md:127`). If it is
an **impedance-convolution** rate and not a GR kinematic rate, then *neither* imported Kerr formula
is automatically right — the substrate should have its own expression. Is $\Omega$ (a) an imported
GR ZAMO rate, (b) an approximation of one, or (c) a substrate quantity that merely *coincides* with
frame-dragging in the weak-field limit? *Plumber picture: is this the speed the water swirls, or the
rate at which the pipe's impedance rotates past the mode?*

### Q5 — the noun "$\sqrt{1+\nu_{vac}}$": why a square root, and why does it grow the radius? (F1)

The eigenfrequency correction **shrinks** a radius by $(1+\nu)$; the spin-evaluation correction
**grows** one by $\sqrt{1+\nu}$. Canon asserts these are "the same $\nu_{vac}$ correcting" both.

**Ask Grant:** is there a physical reason a *rotational* evaluation radius would pick up
$\sqrt{1+\nu}$ (e.g. a geometric-mean / two-way-transit reading, $\sqrt{r_{in}r_{out}}$-like) rather
than the linear Poisson factor — or is this an unmotivated fit that should be *replaced* by a
computed turning point (R3) rather than justified? **Do not let the answer be "it works."** Per F8
the factor can only be worth ≈0.7 pp anyway, so the honest outcome may be "retire the factor, accept
the number moves the wrong way."

### Q6 — the noun "the $1/\ell$ leak": is the leak-constant really 1? (F7, H1, R1)

The per-cycle leak is asserted to *scale as* $1/\ell$ with the proportionality constant set to
exactly 1 by a $2\pi$ convention. H1 says the missing ≈5% lives here.

**Ask Grant:** for a mode with $\ell$ wavelengths around the cavity, is "one wavelength's worth of
energy radiates per cycle" a **counting statement** (exactly $1/\ell$, no constant) or a **scaling
statement** ($c_1/\ell$ with $c_1$ to be computed from radiation resistance)? *Plumber picture: does
each bend in the pipe dump exactly its own share, or its share times an efficiency?*

### Q7 — the noun "echo": is the corpus's own echo prediction in play, and are we willing to risk it?

`vol3/claim-quality.md:123` already banks "gravitational ringdown **echoes are predicted**." Route R3
would *derive* the echo delay as a by-product — and could therefore **kill an existing banked corpus
prediction** against published LIGO echo-search limits.

**Ask Grant:** do we want that exposure in this lane, or is the echo a separate pre-reg? *(A kill
there would be a clean, high-value negative — but it should be a chosen risk, pre-registered, not a
surprise mid-derivation.)*

### Q8 — scope: is this lane allowed to touch the ratified cold anchor?

Ruling B1 just pinned $Q = \ell$ as the cold $a_*=0$ anchor. F8/H1 says the tension **is** in that
anchor (it is ≈−4.7% low against GR by the corpus's own reference values).

**Ask Grant:** if a route lands a cold $Q = c_1\ell$ with $c_1 \approx 1.05$, is that (a) a permitted
refinement of the B1-ratified anchor, (b) a flag-don't-fix routed back to you, or (c) out of scope —
in which case the lane's ceiling is ≈0.7 pp and bin (c) is the likely outcome and we should say so
up front. **This question determines whether the lane is worth firing at all.**

---

## §4 — DRAFT success bins — ⚠ NOT FROZEN

> **Freezing happens at derivation-fire time, in a separate pre-reg, after the §3 walk.** These are
> drafts for Grant to react to. Adjudication criteria may be *tightened* before freezing; they may
> **not** be loosened after results are seen (no post-hoc dropping of criteria to convert ❌ to ✅).

**Rule 11 framing, stated up front:** the −5.44% is a **clean banked tension**, already honestly
recorded at solidity 0.55 with `build_status "use as input only"`. This lane **explains it or banks
it deeper.** It is **not** a rescue-debug. **No retuning of v1 is admissible** — not the mapping, not
the $\sqrt{1+\nu_{vac}}$ factor, not the $\Omega$ variant choice, not the leak constant. Any route
must derive its numbers from substrate inputs fixed *before* comparison, and the comparator (the
frozen C-τ dimensionless $Q$ comparator against corrected Kerr) is inherited unchanged.

| bin | condition (draft) | outcome | class |
|---|---|---|---|
| **(a) RESOLVED** | a route derives the mapping from substrate inputs fixed pre-comparison AND reproduces $Q$ (equivalently $\tau$) within a **tolerance stated in the frozen pre-reg** — draft proposal: $\|\bar D_Q\| < 3\%$, the same band already frozen for $\omega_R$, on the same primary catalog (a\*=0.64/0.67/0.74) **and** at the cold $a_*=0$ anchor | tension resolved; solidity re-graded on the derivation's own merits | **FORM-emergence / VALUE-consistency** per §2.1 — must NOT be headlined as emergence at value level; only a $\nu_{vac}$-free ratio could carry that |
| **(b) DEEPENED** | a route derives a **different** value (outside the stated tolerance, either sign) from an honest substrate chain | **tension deepens — banked honestly. THIS IS A GOOD OUTCOME.** The mechanism is now named rather than unexplained; the disagreement becomes a sharper falsifier than the near-miss was | consistency-class negative with a named mechanism |
| **(c) NO ROUTE CLOSES** | R1 returns $c_1 = 1$; R2's barrier integral lands $\gg$ tolerance from GR (or its profile turns out to be a fitted free function); R3's cold limit breaks the anchor or its echo delay is excluded; R4 reproduces the grafted law | v1 **stays** disclosed-phenomenological at solidity 0.55, `build_status "use as input only"`; −5.4% banked deeper with the F8 decomposition attached | no class change; a recorded negative |
| **(d) SCOPE-BLOCKED** | the §3 walk returns "cold anchor is out of scope" (Q8c) | lane's reachable ceiling is ≈0.7 pp of 5.44 pp → (c) is the predicted outcome and the lane may be **declined before firing** | n/a — a scoping decision, recorded not executed |
| **(e) CANON-INCONSISTENT** | a route is well-posed but two canonical inputs contradict (e.g. Q4 has no substrate answer; Q1 answer conflicts with Op21's single-channel classification) | **flag-don't-fix** — surface both file paths + verbatim content to Grant; do NOT reframe one to match the other | n/a — adjudication routed, not resolved |

**Reachability audit** (per the standing design lesson that every outcome class needs a reachable bin):
(a) reachable via R1/R2/R3/R4; (b) reachable via any route that computes rather than fits;
(c) reachable and explicitly *not* a failure; (d) reachable from the walk alone, before any code;
(e) reachable and **already partially triggered** — **F2**, **F6** and **F9** are live canon
inconsistencies today. (F2: two Ω formulas both canonical. F6: six un-bannered "sub-2%" sites against
a leaf-level retraction. **F9: two saturation-amplitude conventions both canonically stated —
$A = \varepsilon_{11} = 7GM/c^2r$ per `saturating-modulus-and-backreaction.md:51` +
`temporal-spatial-lattice-decomposition.md:14` vs the $\sqrt{g_{00}} = \sqrt{S} \approx 1 - GM/c^2r$
clock at `temporal-spatial-lattice-decomposition.md:24`/`:28` — reconciled *for the shear channel* by
the channel-split at `vol3/claim-quality.md:121`, un-reconciled as a global convention.**)
No outcome of this lane is unbinnable.

**Non-goals, stated so they cannot creep in:** this lane does **not** re-open the v1↔v2 fork (B1
ruled it), does **not** revisit the frame/table corrections (#774 settled them), does **not** touch
$\nu_{vac}$'s value provenance (GR-imported, PR #261 closed), and does **not** land any manuscript or
`COLLABORATION_NOTES` entry — findings F1–F9 are surfaced for the auditor lane to land.

---

## Appendix A — Step-0 skill-selection plan (written before §1, retro-checked before push)

Written as a 60-second plan at lane start; the retro-pass at the bottom records where the applied set
drifted.

| skill / discipline | fired? | why (and where it bit) |
|---|---|---|
| **`ave-prereg` corpus-grep-first** | YES, first action | Grep before thinking. It bit immediately: the ringdown arc is spread over 65 KB files + ~25 research docs, and the load-bearing τ chain lives in a **research doc** (`…_v1-spin-mapping-adjudication_result.md`), not in the KB leaf. Thinking first would have missed the −5.44% table entirely. |
| **`verify-before-cite` (two-method)** | YES, on every quoted formula/number — **but NOT strongly enough on the absence direction** | It bit twice. (i) `regime-eigenvalue-method.md:63` looked like a **wrong** citation under `cut -c1-200` — the quote lives in the *tail* of a long line; a naive check would have mis-flagged a correct corpus cite. (ii) It opened F6 (un-bannered "sub-2%" sites) because I re-grepped for retraction banners instead of assuming the 2026-07-20 banner propagated. **Self-correction (repair pass):** my first version of F6 said **three** sites; review re-grepped and found **six** (+4 companion superradiance sites). Both misses were trigger-6 absence-direction failures: a single-pattern `grep "sub-2"` cannot see `orbital_resonance.py:485`'s "`< 2%`", and a KB-subtree-scoped grep cannot see `manuscript/backmatter/` or `src/`. The two-method rule as I applied it varied the *file* and not the *pattern* or the *scope* — see §1.7. F9 failed the same way and worse (a "returns zero hits" absence claim that was false, §1.4-F9 / §2.3). |
| **`consistency-vs-emergence`** | YES, applied to all 6 routes | Every route rides $\nu_{vac} = 2/7$, whose **VALUE is GR-imported** via $K=2G$. Without this pass, a landed Q-law would get headlined as emergence when its absolute scale is inherited from GR's trace-reversal identity. Produced the §2.1 class ceiling and the "only $\nu_{vac}$-free ratios are emergence-capable" constraint. |
| **`pre-test-physics-check` (trigger 8, ontology one-liner)** | YES → §3 Q1, routed to Grant | The load-bearing ontology question ("what IS the ringdown") has **three** mutually-exclusive answers implied in canon, and they route to different derivations. Asked BEFORE design per the Rule-16 strengthening — this is exactly the item that would otherwise surface after 30 commits as Mode III. |
| **`substrate-native-check`** | PARTIAL — deliberately | No solver/observer/operator is scaffolded in this lane, so the full K4/Cosserat/Op14 walk is **deferred to the derivation lane** (it is a firing prerequisite, listed at Q1/Q3). What *was* done: the §1.0 sector/regime/phase-state header, and the sector-ownership check that flagged R1's main leak risk (transplanting $Z_0 \equiv Z_{EM}$ into a **shear**-channel problem — the category error canon already caught twice). |
| **`phase-space-coordinate-check` (A46)** | YES, cheap pass | The whole confrontation lives in the dimensionless-eigenvalue register ($\omega M$, $Q$) that AVE and GR share — no phase-space-vs-real-space mismatch. Recorded in §1.0 COORDS rather than left implicit. |
| **`pure-AVE-corpus`** | YES, standing | No external, non-physics context appears anywhere in this doc, its commits, its branch name, or the docket fragment. Grant's frontier signal is recorded as a **physics** rationale (the named next ringdown work banked by Ruling B1). |
| **flag-don't-fix (durable directive)** | YES, 9 times | F1–F9 are all surfaced with both paths + verbatim content and **zero corpus files modified**. F6 in particular (a stale "zero free parameters / sub-2%" premise) is the kind of thing that is tempting to just fix — fixing it silently would have hidden a real propagation-discipline signal. F6's routing is now **reconcile-with-the-in-flight-lane** (`docs/b1-retraction-propagation`), not "open new auditor work" — surfacing a finding into a lane that already owns the file set is the non-duplicating form of flag-don't-fix. |
| **Rule 11 honest-closure** | YES, structurally | Bin (b) "tension deepens" is written as a **good** outcome, bin (c) as a **result**; the Rule-11 fence in §4 names the four specific retunings that are inadmissible (mapping, $\sqrt{1+\nu_{vac}}$, $\Omega$-variant, leak constant) so they can't be reached for later. |
| **lane discipline (Rule 15)** | YES | Scoping lane: no derivation, no solver, no claim, no `COLLABORATION_NOTES`/manuscript entry. F1–F9 are handed to the **auditor** lane to land; Q1–Q8 are handed to **Grant**. This doc mints nothing. |
| `ave-discrimination-check` | NOT fired | Deferred: correct at derivation-fire time (does the landed law discriminate AVE from GR?). Noted rather than silently skipped — R3's echo delay is the discrimination candidate to test then. |
| `ave-audit` | NOT fired | This is not an audit of a landed claim; it is pre-work scoping. F1–F9 are audit *leads* for the auditor lane, not audit findings. |

**Retro-pass (applied-set drift).** Two skills fired that were **not** in the opening plan, both
because the corpus forced them: (1) `consistency-vs-emergence` was planned as a per-route tag but had
to be promoted to a **cross-cutting §2.1 ceiling** once F3 established the $\nu_{vac}$ value-import —
a per-route tag would have let a "ratio is emergent, therefore the law is emergent" slide through;
(2) the **sector-ownership** check (`A1 ⊥ T2` cross-wiring watch) was not planned at all and became
load-bearing for R1 — the electron $Q$ template is an **EM**-channel calculation and the ringdown is
a **shear**-channel object, so the template cannot be copied verbatim. Recorded here rather than
back-dated into the plan.

**One skill I should flag as *not applicable* despite looking applicable:** the structural-null
stencil lens. There is no coupling=0 / spectator null in this lane — the −5.44% is a *non-null*
near-miss, so there is no disabled-flag-validated-as-physics hazard to check for here.

