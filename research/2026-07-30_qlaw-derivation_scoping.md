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

**★ FINDING F6 (flag-don't-fix; auditor-lane item, NOT touched here).** The 2026-07-20 "sub-2%
RETRACTED" banner landed on `ave-merger-ringdown-eigenvalue.md:127` but did **not** propagate to
three other canonical sites, which still assert the retracted accuracy claim *and* call it
zero-free-parameter:

- `manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/kerr-q-correction.md:37` — "this formula
  reproduces the quality factor to **sub-2%** with zero free parameters" + the $Q_{AVE}$ vs $Q_{GR}$
  table at `:39-45` (2.24/2.54/3.02/3.75/4.93 vs 2.25/2.54/3.01/3.81/5.23) computed against the
  **corrupt** Kerr reference. No retraction banner anywhere in that file (`grep -n "RETRACT\|SUPERSED\|🔴"` → 0 hits).
- `manuscript/ave-kb/common/solver-toolchain.md:116` — same sentence, "reproduces the GR quality
  factor to **sub-2%** with zero free parameters". No banner.
- `manuscript/ave-kb/vol2/claim-quality.md:1097` — "sub-2% accuracy across $a_* = 0.3$–$0.8$".

This directly contradicts the load-bearing leaf's own grade ("solidity 0.55 …
disclosed-phenomenological … NOT a zero-free-parameter benchmark", `eigenvalue leaf:72-76`) and the
banked −5.44% Q deviation. **Surfaced with both paths + verbatim content; not resolved here.** A
derivation lane that reads app-F as canon would start from a false premise (that the Q-law already
matches to sub-2% with zero parameters) and would therefore have no tension to explain.

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
ratios** — candidates: $Q(a_*)/Q(0)$, $\omega_R(\ell')/\omega_R(\ell)$ (already derived, ORG-1),
and (Route R3) an echo-delay-to-ringdown-period ratio. This is the standing "the chord must be a
dimensionless ratio" discipline; it should be written into the derivation pre-reg header, not
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
- **★ BLOCKED by a real gap — FINDING F9.** $A^2(r)$ has **no canonical radial profile** for a BH
  anywhere in `manuscript/ave-kb/vol3/gravity/`. Targeted greps for an $A^2 = \varepsilon_{11}$ /
  $A^2 = 2GM/c^2r$ / $A^2(r)$ pinning in `ch01-gravity-yield/` and `ch02-general-relativity/`
  return **zero hits**. Two candidate conventions are both defensible and they disagree by 3.5×:
  $A^2 = \varepsilon_{11} = 7GM/(c^2 r)$ (gives $A^2 = 1$ exactly at $r_{sat}$, the Ax-4 yield
  surface) vs $A^2 = r_s/r = 2GM/(c^2 r)$ (gives GR's $\sqrt{1-r_s/r}$ clock and $A^2 = 1$ at the
  horizon). **This must be settled before R2 can be executed** — see §3 Q3.
- **What it would predict:** $Q$ from a barrier integral $\propto \exp(2\int|k|\,dr)$, which is
  intrinsically both $\ell$- and $a_*$-dependent — so it could in principle deliver the cold offset
  *and* the spin trend from one mechanism (addressing F5 at the root).
- **Class if it lands:** FORM-emergence; absolute values still VALUE-consistency per §2.1, but a
  ratio $Q(a_*)/Q(0)$ from the same profile could be emergence-capable.
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
- **Class if it lands:** FORM-emergence and **$\nu_{vac}$-free** (mode counting uses Ax 1 cell size
  and topology, not the elastic value) — R4 is the route with the cleanest class ceiling.
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

Honestly enumerated: if R1 returns $c_1 = 1.00$, R2 stays blocked on F9, R3's echo delay is excluded
or its cold limit breaks the anchor, and R4 merely reproduces the grafted law, then **nothing closes.**
That outcome is a **result**, not a failure: v1 stays at solidity 0.55, `build_status "use as input
only"`, disclosed-phenomenological, and the −5.4% is banked *deeper* — with the F8 decomposition
naming the mechanism honestly ("the offset is the cold $Q$ anchor's own ≈−4.7%, not the spin
mapping"). Naming the mechanism is worth more than moving the number.

<!-- REMAINING SECTIONS FILLED IN SUBSEQUENT COMMITS -->
