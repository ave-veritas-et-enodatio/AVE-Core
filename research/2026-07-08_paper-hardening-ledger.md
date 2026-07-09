# Birefringence / Reach Paper — Hardening Ledger

**Date opened:** 2026-07-08
**Nature:** LIVING TRACKER. Internal paper-hardening QA of the birefringence Letter
(`papers/2026_birefringence_letter/main.tex`) and the reach paper
(`papers/2026_reach_saturating_family/`). One row per open exposure; each row
carries **status · how · where (file:line / PR) · conclusion · owed-next**. Every
"already addressed" claim is backed by a grep-confirmed file:line. Rows are updated
in the same PR that closes them, so this page always shows the true frontier.
**Framing:** every item is stated as our own physics/exposition QA — the physics
stands on its own regardless of who first flagged it.

**Legend:** `DONE` = closed, located, concluded · `PARTIAL` = substantially met,
residue owed · `OWED-PHYSICS` = a computation/derivation owed · `OWED-PROSE` =
an edit owed · `NEEDS-RULING` = a physics fork awaiting Grant's ontology call.

---

## Status board

| ID | Item | Status | Where it stands |
|----|------|--------|-----------------|
| **A0** | Muonic-H static-sector exclusion | **DONE** | `[C-EXCLUDED]` clm-sve3xc @0.80; printed retraction |
| **A0b** | Born–Infeld = zero-birefringence; E-route discriminator | **DONE** | corrected across all sites (FIX 1–6, #555) |
| **P4** | Propagation commitment (disclaimer vs charge-keyed) | **SUPERSEDED by R3-A** | v3 recorded **Branch-YES** (held fields load continuously from zero, weak-field response cut off at `ℓ_node`). Round-3 ruling **supersedes to Branch-no**: static fields sit **OUTSIDE the model**; loads-continuously falsified (X-ray transport; fenced-scale escape killed by K4-TLM band-edge derivation). Muonic `[C-EXCLUDED]` survives as a **domain-restriction demonstration**; copper survives as a **moot** bound. See R3-A/R3-B. |
| **P5** | Magnetic functional S_B + radiative-keying unification | **DONE (v3)** | S_B `=√(1−A_I²)`, `μ_eff=μ₀/√(1−A_I²)` lifted into paper as Eq (6) w/ static + `(kr)²` limits; radiative-far-field unification **REFUTED**, grounding = Maxwell source asymmetry `∇·B=0`; `main.tex:399,448` (Letter v3) |
| **P6** | Sidereal boost order (β vs β²) + frame + LV | **DONE (v3)** | re-stated `[SIDEREAL-REAL]`: first-order β `4β≈4.9e-3` first harmonic (was subdominant 2nd harmonic `(v/c)²=1.5e-6`); frame → CMB/substrate rest; LV framing = unconstrained+testable, two structural reasons (nonlinear + pump-safe); `main.tex:460–515` (Letter v3) |
| **H1** | Postulate count (1 → honest 2) | **DONE (v3)** | "single constitutive postulate" → **two constitutive statements** (kernel + sector keying, grounded in `∇·B=0`); `main.tex:7,45,927` (Letter v3) |
| **H2** | Drop "theorem of the confinement" | **DONE** | softened → "consequence of the confinement hypothesis", `main.tex:299–300` (#578) |
| **H3** | Engine-vocabulary leak | **DONE (v3)** | lattice-\* + deep-cold self-contained (#578); charge-keyed / operating-point-bias now folded into self-contained weak-field-response language in the P4 rewrite, `main.tex:289,346` (Letter v3) — grep of both terms in `main.tex` = 0 |
| **H4** | Table I peak vs pulse-integrated | **DONE (v3)** | pulse-integrated expectation added to caption: peak × fluence-weighted envelope form factor `3^(−3/2)≈0.19` ⇒ `1.0e-3 / 8.2e-4 / 1.8e-3`; OUR compute, driver `src/scripts/vol_9_device/h4_pulse_integrated_expectation.py` (exact ⟨sin²⟩ cross-check <0.2%); `main.tex:680` caption (Letter v3) |
| **H5** | Record-floor wording (2.4e-10 vs 8e-11) | **DONE** | abstract relabelled "conservative (demonstrated)" floor, `main.tex:53–54` (#578) |
| **D1** | Engine-independent route to N=7 | **PARTIAL (≈met)** | analytic Nyquist route already registered |
| **E1** | Overlap certificate (null branch) | **DONE** | independent-overlap-witness paragraph, `sec:falsify` `main.tex:696–710` (#578) |
| **E2** | Bright-branch confirmation plan | **DONE** | attenuator + fingerprint-battery paragraph, `sec:falsify` `main.tex:712–731` (#578) |

**All rows integrated into the Letter (v3), then P4 revised at round-3.** **P5** —
the radiative-far-field unification is **REFUTED**, and the E/B sector keys are
grounded in the Maxwell source asymmetry (`∇·B=0`), which also settles **H1** at
**two** constitutive statements. **P4 is superseded to Branch-no** (see R3 section
below): the v3 "held static field *does* load, continuously from zero, cut off at
`ℓ_node`" commitment is retracted — static fields sit **outside the model's scope**,
the muonic-H test is re-cast as a **domain-restriction demonstration**, and the
radiative scoping is named an **open postulate**. Only D1's optional round-2
(nonlinear-regime N=7) remains open, and it is not cited in the Letter.

---

## A0 — Muonic-hydrogen static-sector exclusion — DONE

**Conclusion.** Sector-scope verdict `[C-EXCLUDED]` (claim `clm-sve3xc`, solidity 0.80):
the continuum static-E law ε_eff = ε₀√(1−(E/E_c)²) is excluded at atomic scales by
muonic hydrogen, non-perturbatively — both the continuum arm (7.5×–114× the full
202.37 meV Lamb interval) and the lattice-scoped arm (~2×10⁴× the 2.3 µeV CREMA
window) violate; the protective cutoff would need ~9·ℓ_node ≈ 3.5 pm (a free
parameter; the ~300 fm floor estimate refuted). High-Z (U91+) is worse: the kernel
has no real solution over the bulk of the 1s orbit (A² = 12.56 > 1). What survives,
disjoint: the registered radiative pump–probe falsifier (A² ≈ 6e-7) and static-B
transparency. The earlier implicit universal-static reading is retracted **in print**.
**How/where.** A² = 2.5e-2 at `main.tex:336`; high-Z no-solution at `:337`; printed
retraction = honesty-ledger item (v), `:259–286`. Adjudicator
`research/2026-07-05_problem3-muonic-lamb_RESULT.md:16` (`[C-EXCLUDED]`), Gate-0 table
`:24–35`. Driver `src/scripts/verify/problem3_muonic_lamb_shift.py`. Provenance §10,
`provenance.md:313–403`. Merged #539/#540/#542.
**Flag.** No literal "mass-ratio claim" exists in the corpus (`git log -S` empty);
A0's "old mass-ratio claim" = the retracted implicit universal-permittivity reading.

## A0b — Born–Infeld = zero-birefringence NLED; E-route is the discriminator — DONE

**Conclusion.** The earlier framing (static-magnetic null separates us from B-I) was
corrected in print: exact B-I is itself the zero-birefringence theory (single
effective light cone in any constant background; Boillat uniqueness; the unique
Russo–Townsend zero-bir member *with a Maxwell weak-field limit*), so the static-B
null cannot separate the model from exact B-I — the discriminator is the tree-level,
O(1) **electric-route coefficient**, and the pump-on E-route measurement separates
model / QED / exact-B-I at once.
**How/where.** Intro `main.tex:97–109`, `:119–128`; Signature §V `:622–663`. Refs
`refs.bib`: RussoTownsend2023, Boillat1970, BornInfeld1934, Plebanski1970. Landed via
FIX 1–6 (commits 4ff9e20c / aaf2479c / d6b300ca / 0fe8c3df / 8e74c9df / 9d4af5cf) +
RT-miscount fix 1f7f7480; DEFECT A/B/C round = #555, provenance §12 `:572–596`.

## P4 — Propagation commitment: static-field disclaimer vs charge-keyed loading — DONE (integrated, Letter v3)

> 🔴 **SUPERSEDED by Letter round-3 (Branch-no) — this detailed entry is stale; the summary ROW above
> already reads `SUPERSEDED by R3-A`, but this narrative was not brought into line until now.** The
> round-3 ruling resolves the fork to **Branch-no**: static fields lie **OUTSIDE the model's scope**;
> the "loads-continuously" / **Branch YES** framing throughout this entry is **retracted**. The
> charge-keyed *derivation* survives as substrate physics, but the Letter no longer **owns** the static
> sector (muonic-H = **domain-restriction demonstration**; copper = **MOOT bound**). See the Round-3
> section of this ledger + provenance R3-A/R3-B. Body preserved beneath (v3 record).

**RESOLVED (v3).** The two contradictory sentences are rewritten to one honest
statement: a held static field *does* load (continuously from zero, same mean-square
dependence), but only as a **weak-field effective response cut off at the lattice
pitch `ℓ_node`**, NOT a universal continuum constitutive law; the strong-field
extrapolation is excluded (muonic `[C-EXCLUDED]`, unchanged), and in ordinary matter
the loading is unobservably small (copper decrement `δ_AVE≈4e-8 ≪` measured `2.4e-5`,
OUR WS-cell compute per `research/2026-07-08_p4-forward-voltage-threshold_RESULT.md`).
The forward-voltage threshold `V_f` routed **FREE** and is **dropped** (not reintroduced).
This rewrite also absorbs the deferred H3 vocab (`charge-keyed`, `operating-point bias`)
into self-contained language. `main.tex:289` (item v), `:346` (sector scope), `:369`
(copper). Source: P4 RESULT §9 (branch `analysis/p4-forward-voltage`).

**The contradiction (both in the Letter).** (a) DISCLAIMER `main.tex:330–331` — we do
NOT assert the kernel as a universal static-field constitutive law. (b) CHARGE-KEYED
scoping (appears twice, §II.B) — a held field is a real operating-point bias, so it
loads. These read as two different theories.
**Our current answer (round-3 `[DERIVED: CHARGE-KEYED]`, merged #547).** YES — a probe
crossing a strong *non-uniform* static field experiences the loaded permittivity
(ε keys on mean-square, DC included). ~~We are on Branch YES.~~ 🔴 **STRUCK — round-3 resolved Branch-no** (static outside model scope; charge-keyed derivation survives, Letter ownership of the static sector reversed).
**The fork.** Confirm YES/NO explicitly and pre-register it. If YES, we owe an
X-ray-through-ordinary-matter constraint (see owed). If NO, the charge-keyed sentence
comes out and muonic-H restates as a domain-restriction demonstration (prose surgery).
**MOOT, fork resolved NO** (was "Owed (Branch YES)"). 🔴 Under Branch-no these deliverables are moot as *owed* items — static is outside scope; the copper decrement was nonetheless computed (`δ_AVE≈4.2e-8`, R3-B) and retained only as a MOOT ordinary-matter bound. Original owed-list preserved: (1) Compute the AVE refractive-decrement contribution for an
~8 keV photon in copper: volume-average ½A²(r) over the lattice with a reduced-Compton
cutoff, vs the measured Cu decrement (δ ~ 2.4e-5, known ~1%). (2) State whether
dispersion fences Delbrück / γ-attenuation above the 511 keV response scale.
**Where.** `main.tex:330–331`; `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md`;
`provenance.md:434–453` (#547). **All numbers to be OUR compute, not any external estimate.**

## P5 — Magnetic-sector functional Eq (6): static endpoint vs full S_B(circulation) — DONE (integrated, Letter v3)

**RESOLVED (v3).** The explicit parameter-free functional is lifted into the Letter's
magnetic-sector subsection as Eq (6): `S_B=√(1−A_I²)`, `μ_eff=μ₀/√(1−A_I²)`,
`A_I=|∮H·dℓ|/I_max`, with its two limits stated — **(a)** static B ⇒ `∮H·dℓ=0 ⇒ A_I=0
⇒ δn_μ=0` (recovers the endpoint, now Eq (7)), and **(b)** near-zone `A_I ∝ (kr)²` ⇒
PVLAS/BMV consistency **COMPUTED**, not asserted. The radiative-far-field unification
was **REFUTED** (`research/2026-07-08_p5-radiative-far-field-keying_RESULT.md`,
`[RADIATIVE-KEY-REFUTED]`), so it is **NOT asserted**; the E/B sector keying is grounded
in the **Maxwell source asymmetry** (`∇·E=ρ` has charge sources, `∇·B=0` has no monopole)
— the true grounding, `main.tex:448`. S_B eq at `main.tex:399`. Note: the new S_B took
Eq (6); the static-B endpoint renumbered to Eq (7) (all refs are `\eqref`, auto-updated).

**State.** The magnetic prediction is registered only as the strictly-static endpoint
δn_μ = 0 (static B, exactly) [Eq (6), `main.tex:370–373`], asserted parameter-free — but
this does not cover PVLAS (Hz-rotating 2.5 T, demodulated at rotation harmonics) or BMV
(ms pulses, large ∂B/∂t); neither is static in the sense the endpoint requires. The full
S_B(circulation) functional (route-C: μ_eff = μ₀/√(1−A_I²), A_I = curl_h·ℓ_node/I_max)
exists in the corpus but is **not in the paper**.
**The unification hypothesis (do not assert — walk first).** The true key for both
sectors may be **radiative far-field character**: a held E is charge-sourced → operating-
point bias → loads (round-3, charge-keyed); a held B has no monopole to bias it →
transparent (FORK-1, circulation-keyed); the pump is pure radiation → active. This would
turn two asserted sector-facts into one derived principle ("charges exist, monopoles
don't").
**Owed.** (a) **Grant ontology ruling:** is the unifying key radiative far-field character,
or do E-charge-keying and B-circulation-keying stay as two independent postulates? (b)
Lift route-C S_B into the paper as an explicit equation; (c) engine-test far-field keying
(compare held-E, held-B, radiation through the same functional). **Where.** Eq (6)
`main.tex:370–373`; provenance `:91`; round-3 result doc.

## P6 — Sidereal boost order + frame + LV classification — DONE (integrated, Letter v3)

**RESOLVED (v3).** The sidereal signature is re-stated as `[SIDEREAL-REAL]` in the Letter:
(i) **order corrected** to first-order β — dominant **first-harmonic** `P_flip` amplitude
`4β≈4.9e-3` at one sidereal day, phased to the CMB dipole, with `~8%` annual sideband; the
old `(v/c)²≈1.5e-6` is re-attributed to the **subdominant second harmonic**. (ii) **frame
contradiction resolved** toward the CMB / substrate rest frame (the vacuum is a real medium,
responds in its own rest frame = cosmic frame; `main.tex:404`-lab-frame vs `:420`-CMB tension
closed). (iii) **LV framing** written exactly: *"unconstrained by existing data + testable,"*
NOT "confirmed," carrying the **two structural reasons** — (1) NONLINEAR (field-dependent),
so the minimal-SME linear `k_F`/`k_AF` bounds carry no coefficient for it, and (2) no
astrophysical pump fires it (`[PUMP-SAFE]`: static ambient B transparent by circulation-keying;
radiation channels below the lab pump or geometrically suppressed). The stale static-B O(β²)
motional estimate is re-scoped (kept only as the weak-static-field figure). `main.tex:460–515`.
Sources: `_p6-sidereal-boost-order_result.md`, `_p6-frame-boost-dependence_result.md`,
`_p6-lv-sector-classification_result.md`, `pump-inventory-astrophysical_RESULT.md`.

**Conclusion (boost order).** The birefringence signal is carried by the **pump — a radiation
field** — whose amplitude transforms by the Doppler factor D(θ) = γ(1+β cosθ), which has a
nonzero **linear-in-β** term. So the modulation is **first order in β, not (v/c)²**. sympy
β-expansion: radiation D = 1 + β cosθ + … (O(β)); static motional field γ = 1 + ½β² (O(β²)).
The registered (v/c)² = 1.523e-6 is exactly β² — it captured the **subdominant second harmonic**
(5β² ≈ 7.6e-6) and **missed the dominant first harmonic**. Propagation: δn_bir ∝ D² (mod 2β),
P_flip ∝ D⁴ (mod 4β).
**Corrected numbers (driver compute, β = 1.234e-3, best case c₁→1):** P_flip first-harmonic
amplitude **4.94e-3** (≈3.5 OOM above the registered 1.5e-6); δn_bir first-harmonic 2.47e-3;
second harmonic 7.6e-6. **Signature:** fundamental sidereal period 86164.1 s phased to the CMB
dipole; 2×sidereal subdominant; ~8% annual sideband from Earth's orbital velocity.
**★ NEW FORK surfaced (NEEDS-GRANT-RULING) — the response frame.** The whole result is
frame-conditional and the paper contradicts itself: `main.tex:420–421` says the response frame
is the **CMB rest frame** (→ signal ≈ 4.9e-3), while `main.tex:404–406` says the prediction is
in the **lab frame** of the optical focus (→ sidereal signal **exactly zero**). This
re-derivation fixes the ORDER given the CMB-frame premise; the frame choice itself is a physics
ruling. (Joins P4/P5 in the fork queue.)
**Where.** PR #574 (`analysis/p6-sidereal-boost`); prereg + result
`research/2026-07-08_p6-sidereal-boost-order_{prereg,result}.md`; driver
`src/scripts/vol_9_device/p6_sidereal_boost_order.py`. `make verify` green.
**Owed-next.** Grant rules the frame (CMB vs lab); if CMB, correct the registered number to
4.9e-3 (first harmonic) with the honest premise stated, and note β² is the second-harmonic order.

## H1 — Postulate count: stated ONE → honest TWO — DONE (integrated, Letter v3)

**RESOLVED (v3).** "Single constitutive postulate" → **two constitutive statements** at
all three sites (file-comment `main.tex:7`, abstract `:45`, conclusion `:927`): the
saturation kernel, and the sector keying — with the sector keying noted to **follow from
the Maxwell source asymmetry (`∇·B=0`)**. Honest and stronger than "single." The P5 ruling
fixed the count at **two** (the radiative-scoping is not a third postulate; it is refuted as
a unifier and replaced by the source-asymmetry grounding). The intro's "one constitutive
hypothesis for the dielectric response" (`:94`) is harmonized to name the magnetic companion.

**Conclusion.** "Single constitutive postulate" (abstract L42, conclusion L799, file
comment L6) is an undercount: the body adds the magnetic circulation-keying statement
(L362) and a radiative-sector scoping statement. Honest count ≥ 2 (kernel + magnetic
keying), arguably 3 (incl. radiative-scoping). **Depends on the P5 ruling** (whether
radiative-scoping is a third postulate or a derived consequence).
**Owed.** Edit abstract + conclusion to the honest count (or explicitly demote the extra
statements to scoping). **Where.** `main.tex:L42, L799, L6, L362`.

## H2 — "Theorem of the confinement" overclaims — DONE (#578)

**Conclusion.** "The exponent is therefore a theorem of the confinement, not a fitted
parameter" (was `main.tex:298–299`) overclaims — the derivation is explicitly conditional on
the confinement/energy-conservation premise (L290–298), so p=2 is a *consequence* of the
hypothesis. The two-channel p-discriminator sentence is the keeper.
**Done (#578).** Replaced "a theorem of the confinement" → "a consequence of the confinement
hypothesis" at `main.tex:299–300`. The p=2 derivation and the two-channel p-discriminator
sentence (now `main.tex:300–303`) are preserved unchanged; only the one overclaiming word
moved. Letter compiles clean (latexmk exit 0, 9 pages).

## H3 — Engine-vocabulary leak into the standalone Letter — DONE (integrated, Letter v3)

**RESOLVED (v3).** The two P4-deferred term families (`charge-keyed`, `operating-point
bias`) are now folded into self-contained weak-field-response language by the P4 rewrite
(`main.tex:289,346` — see P4 row). Grep of both terms in `main.tex` = **0**. Combined with
the two families closed in #578 (`lattice-*` → `ℓ_node`, `deep-cold` → `quiescent`), the
Letter is now free of the flagged engine-vocabulary families.

**Conclusion.** Four framework-internal term families appear undefined in the Letter:
"lattice pitch / lattice-scale" (was L282–284, L343, L353–355), "deep-cold" (was L329),
"operating-point bias" (L281, L352), "charge-keyed" (L281, L351). The provenance note
that claims the Letter is grep-clean of engine vocabulary (`provenance.md:L24`) is stale.
**Done, two families (#578).** The two clearly-independent families are now self-contained:
- "lattice pitch / lattice-scale / lattice-pitch" → a short-distance length scale
  `\ell_{\mathrm{node}}`, **defined once at first use** ("the length scale below which the
  continuum form of the constitutive law is not guaranteed to be the correct accounting",
  `main.tex:282`) and reused at `main.tex:285, 344–345, 354–357`. Grep of "lattice" in
  `main.tex` now returns 0.
- "deep-cold" → "quiescent (unbiased, unexcited-vacuum)", defined inline at first use
  (`main.tex:330`). Grep of "deep-cold" now returns 0.
**DEFERRED to P4.** "charge-keyed" (`main.tex:281, 352`) and "operating-point bias"
(`main.tex:281, 353`) are **left exactly as-is** — those sentences are being rewritten by
the separate P4 propagation-commitment workstream; folding a vocab fix in here would
collide with the P4 rewrite. They fold into the P4 integration, not this PR.
**Owed (residue).** The two P4-owned term families, closed when P4 lands. Also update the
stale `provenance.md:L24` grep-clean claim (owned alongside the P4 rewrite).

## H4 — Table I peak-field vs pulse-integrated — DONE (integrated, Letter v3)

**RESOLVED (v3).** The pulse-integrated expectation is COMPUTED and added to the Table I
caption. Method (auditable, not adopted from any external estimate): `P_flip ∝ I²` in the
small-angle regime, so the pulse-integrated value is the peak scaled by the fluence-weighted
envelope form factor `⟨I²⟩/I_peak² = 3^(−3/2) ≈ 0.19245` (matched co-focused 3D Gaussian:
temporal + 2D transverse focal; width-independent Gaussian-moment ratio). Result per demonstrated
row: `1.0e-3 / 8.2e-4 / 1.8e-3` (9835/8766/12914 eV) — still `~10⁶–10⁷` above the demonstrated
purity floor. Peak values reproduce Table I exactly (`5.39e-3/4.28e-3/9.28e-3`); an exact
fluence-weighted `⟨sin²(Δφ/2)⟩` quadrature cross-checks the form-factor method to `<0.2%`.
Driver (constants imported canonically via the GAP-1 chain, no hardcoding):
`src/scripts/vol_9_device/h4_pulse_integrated_expectation.py`; artifact
`src/scripts/vol_9_device/_output/h4_pulse_integrated_expectation.json`. Caption at
`main.tex:680`. OUR compute; no external estimate is adopted.

**Conclusion.** Table I is on the peak-field convention (peak carrier amplitude
E = 8.68e13 V/m; A² = 5.90e-7; peak-field P_flip = 5.39e-3 / 4.28e-3 / 9.28e-3 at
9835 / 8766 / 12914 eV), explicitly stated (`main.tex:514–518`, caption L583–587). No
pulse-envelope-integrated/measured-expectation value is given.
**Owed.** Recompute lane supplies the pulse-integrated expectation P_flip; then tabulate it
alongside the peak column or add a caption sentence that peak-field is the envelope maximum
(so no experimentalist chases a spurious factor). **Our numbers are the compute basis** — no
external estimate adopted.

## H5 — Record-floor wording — DONE (#578)

**Conclusion.** Abstract (`main.tex:53–54`) labels 2.4e-10 the "record X-ray-polarimeter
purity floor"; the body (L695–698) and figure caption (L785–787) correctly give the record
as 8e-11 (Karbstein2021) with 2.4e-10 the conservative single-measurement demonstrated floor
(Marx2013).
**Done (#578).** Abstract reworded to "the conservative (demonstrated) X-ray-polarimeter
purity floor (2.4e-10)" (`main.tex:53–54`) — "record" dropped from the abstract floor phrase,
now matching the body and figure caption (both unchanged; already correct). The abstract's
other floor reference ("above the demonstrated purity floor", L59–61) was already consistent.

## D1 — Engine-independent route to N=7 — PARTIAL (≈met)

**Conclusion.** An engine-INDEPENDENT analytic route to N_min = 7 **already exists and is the
registered derivation**: a by-hand Nyquist / non-collision sampling count
N_min = 2·k_max + 1 = 7 for a uniform (2,3) winding (k_max = 3), α-free, sympy-verified in `src/scripts/verify/electron_tick_floor_sampling.py` —
it does not pass through the engine. The reproduction-vs-independence overclaim was already
withdrawn (tick-floor re-scope, #567): N=7 is a linear-regime lower bound (FLOOR-ONLY;
N_max = ∞ at δ=0, no m_e-pinning ceiling), and the engine leg is labeled illustration.
**Where.** `research/2026-07-07_electron-tick-floor_RESULT.md`,
`src/scripts/verify/electron_tick_floor_sampling.py` (main @37798c2b).
**Owed (optional).** A round-2 nonlinear-saturation-regime derivation to move from the
linear-regime lower bound to the physical (2,3)-soliton floor. And: if N=7 is cited in the
paper, cite it as the analytic Nyquist bound, not an engine result. (No "derived=N7" prose is
currently in either paper — clean.)

## E1 — Overlap certificate for the null branch — DONE (#578)

**Conclusion.** CONFIRMED ABSENT. The kill criterion (`sec:falsify`, was `main.tex:674–720`)
commits a 5σ pump-on null (P_flip < 1e-8 at ≥1e18 W/cm²) and a third-party extraction
procedure, but had NO independent overlap-witness requirement. A null without a witness of
demonstrated pump-probe overlap at the stated intensity is an *absence*, not a kill — the
mirror of the false-victory failure (a false-execution/timing-miss null).
**Done (#578).** Inserted a "\paragraph*{Overlap certificate (precondition for a null)}"
into `sec:falsify` (`main.tex:696–710`), immediately after the kill-criterion paragraph. It
requires, as a precondition for scoring any null as a kill, an independent overlap witness:
interleaved shots on a known pump-only target (gas puff / thin wire at the interaction point)
producing a pump-driven signal (plasma emission, ionization yield, pump-induced scattering)
that brackets the polarimetric data runs in time at the same nominal intensity
(≥1e18 W/cm²) and focal geometry. Absent it, a sub-1e-8 result is logged as an unwitnessed
null and does not close the electric-sector hypothesis. Physics self-contained; compiles clean.

## E2 — Bright-branch confirmation plan — DONE (#578)

**Conclusion.** CONFIRMED ABSENT. The section registered only the null branch plus a bare
"a value at the 1e-3 level confirms the model" (`main.tex:719`); no calibrated-attenuator plan
and none of the three positive fingerprints. Registering *how a positive is believed* is the
same discipline as registering how a null kills.
**Done (#578).** Inserted a "\paragraph*{Bright branch: how a positive is confirmed}" into
`sec:falsify` (`main.tex:712–731`), after the E1 overlap-certificate paragraph. A true signal
at the predicted P_flip ≃ 4e-3–9e-3 (Table I) saturates an unattenuated crossed channel, so
the first well-overlapped shots run through a calibrated attenuator (calibrated on the
pump-off direct beam so the recovered P_flip stays traceable). A positive is confirmed by the
fingerprint battery: (i) a Δt scan peaking at the femtosecond pump-pulse width, (ii) a
sin²(2ψ) four-lobe dependence on the pump-vs-analyzer angle, (iii) I² intensity scaling
(δn_bir ∝ E² [eq:dnbir] through P_flip ∝ δn_bir² [eq:flip], so P_flip ∝ I²). Numbers
consistent with Table I; physics self-contained; compiles clean.

---

## Round-3 review integration (co-author feedback, 2026-07-08) — DONE (staged, DO-NOT-MERGE)

**Nature.** Round-3 punch list against the Letter (v3). The load-bearing physics
ruling: **Problem 8 resolves to Branch-no.** The v3 "a held static field *does*
load the permittivity, continuously from zero (weak-field response cut off at
`ℓ_node`)" commitment (P4 row above, Branch-YES) is **superseded**: static fields
sit **outside the model's scope**. The "loads-continuously-from-zero" branch is
falsified by X-ray transport, and the fenced-scale escape (lowering the response
scale to 30–80 keV) was killed on physics — a full K4-TLM network derivation of
the loading response shows it reaches the band edge at ~MeV, gapless, with no
sub-band fence, so there is no scale at which static loading can be quietly
parked. Branch-no is a **simplification, not a wound**: the registered radiative
falsifier (Table I pump–probe coefficient, the kill criterion) is untouched.

**Status board (round-3).**

| ID | Item | Status | Where it stands (`papers/2026_birefringence_letter/main.tex`) |
|----|------|--------|-----------------|
| **R3-A** | Branch-no surgery (Problem 8): static fields outside model; remove loads-continuously | **DONE** | item (v) `:285` (outside-scope) `:288` (domain-restriction); sector scope `:366`; II.D motional `:505` (identical zero); bounds `:953` |
| **R3-B** | Copper cutoff prose fix (`r_c(Cu)=√29·160 fm≈861 fm`, not `ℓ_node`) | **DONE** | `:382` `r_c(Cu)=√Z×160 fm≈861 fm`; `δ_AVE≈4.2e-8` (was mis-named `ℓ_node`=386 fm); kept as MOOT bound |
| **R3-C1** | Print `I_max = ε₀c·E_c·ℓ_node = E_c·ℓ_node/Z₀ ≈ 116 A` (2π loop ≈ 730 A) | **DONE** | `:421` `I_max≈116 A` (2π loop ≈730 A; O(1) immaterial) |
| **R3-C2** | State which side of the `μ_eff` root the model uses (denominator branch) | **DONE** | `:427` `μ_eff=μ₀/S_B≥μ₀` (denominator/stiffening branch; branch-indep at static endpoint) |
| **R3-C3** | Pump magnetic self-consistency: `A_I=A(kℓ_node)`, `A_I²/A²≈1e-11` (Outcome A) | **DONE** | `:475` `A_I=A(kℓ_node)`, `kℓ_node≈3.0e-6`, `A_I²/A²≈9e-12` → Table I stands (Outcome A) |
| **R3-P9** | Anomalous high-Z X-ray refractive decrements — DIES UNBORN under Branch-no; considered-and-dropped, NOT registered | **DROPPED** | this row only; nothing added to paper (registering it would contradict Branch-no) |
| **R3-D3** | One-line `ℓ_node`/"node" definition at first use (load-bearing in Eq) | **DONE** | `:367` `ℓ_node≡ħ/(m_ec)≈3.86e-13 m` (reduced Compton; node scale) |
| **R3-D4** | Soften intro "neutral to any wider interpretation" to match II.D declared medium | **DONE** | `:103` intro now declares a material medium at rest in CMB frame (premise the sidereal falsifier needs) |
| **R3-D5** | Sidereal `4β` amplitude-only → probe-side O(β) transforms bounded + grow astro dismissal to 2 sentences | **DONE → refined (PR #591)** | `:556` co-propagation `(1−cosθ)⁴` suppression, 2 sentences (original pass). Sidereal para **corrected in #591**: `4β` is the pump-amplitude term *alone*; probe-side transforms (probe-freq Doppler via `Δφ∝ω_probe`, aberration of `ϑ_coll` via `(1−cosϑ)⁴`, path-length) are **same-order O(β)**, not subdominant — `4β` registered as order-of-magnitude scale not exact coefficient; first-harmonic *presence*-discriminator preserved & shown robust. (The original "pure amplitude / amplitude-dominated" framing was not honestly available and was replaced.) |
| **R3-D6** | Overlap certificate: add two-beam observable (probe through pump plasma vs delay) | **DONE** | `:861` probe transmission/deflection through pump plasma vs `Δt`; kill now needs BOTH certificates |
| **R3-D7** | Table I carrier average `⟨cos²⟩=½` → extra ¼ on P → measured expectation ~2–5e-4 | **DONE** | caption `:737` `P_flip^meas ≈ 2.6/2.1/4.5 ×10⁻⁴`; tabulated column = instantaneous peak (item iv); ratio unchanged |

**Recomputed numbers (this session, verified `python3`):**
- **C1:** `I_max = E_c·ℓ_node/Z₀ = 1.13e17 · 3.8616e-13 / 376.73 = 115.8 A ≈ 116 A`;
  `= ε₀c·E_c·ℓ_node` (identical, since `ε₀c = 1/Z₀`); 2π-loop convention `= 727.8 A ≈ 730 A`. O(1) loop ambiguity immaterial.
- **C3:** pump 1.55 eV → `λ=800 nm`, `k=7.854e6 m⁻¹`; `k·ℓ_node = 3.03e-6`;
  `A_I²/A² = (k·ℓ_node)² = 9.2e-12 ≈ 1e-11` → magnetic contribution ~11 orders below the electric birefringence ⇒ Table I (electric-route) stands, **Outcome A confirmed**.
- **B:** `r_c(Cu) = √29·160 fm = 861.6 fm` (was mis-named `ℓ_node = 386.2 fm`);
  integrating from `r_c(Cu)` gives `δ_AVE ≈ 4.2e-8`, matching the stated `~4e-8` to 5%.
- **D7:** peak `5.39/4.28/9.28 ×10⁻³` × envelope `3^(−3/2)=0.1925` × carrier `¼`
  = `2.6e-4 / 2.1e-4 / 4.5e-4` (~2–5e-4); vs floor `2.4e-10` = `1.1e6 / 8.6e5 / 1.9e6` (~6 orders above).
- **ℓ_node** `= ħ/(m_e c) = 3.8616e-13 m = 386.2 fm` (reduced Compton wavelength).

**Transport comparators — exact NIST XCOM (task #26, review Data-flag closure).**
The round-3 Data flag marked the Problem-8 attenuation comparators as
±20%-from-memory, owed exact NIST XCOM before external use. Verified this session
(NIST XrayMassCoef `ElemTab/z26`, `z82`; total μ/ρ with coherent scattering):

| element | E | μ/ρ NIST (cm²/g) | reviewer (memory) | σ = (μ/ρ)·A/N_A |
|---|---|---|---|---|
| Pb (A=207.2) | 100 keV | 5.549 | ~5.46 ✓ | — |
| Pb | 150 keV | 2.014 | ~2.0 ✓ | **0.69 kb** |
| Pb | 200 keV | 0.9985 | 0.999 ✓ | — |
| Pb | 500 keV | 0.1614 | 0.161 ✓ | — |
| Fe (A=55.85) | 500 keV | 0.08414 | 0.084 ✓ | **7.80 b** |

- **μ/ρ values confirmed** accurate to ~2% (well inside the flagged ±20%). **No
  Letter-body number changes**: `main.tex` carries no μ/ρ table — its only
  attenuation datum is the copper decrement, verified next.
- **Copper decrement** `δ(Cu,8 keV)=2.4e-5` (`main.tex:392`) **confirmed exact**:
  CXRO `f₁(Cu,8 keV)≈26.4` (below the 8.98 keV K-edge) ⇒
  `δ=(r_e λ²/2π)·n_a·f₁ = 2.42e-5`. Unchanged.
- **CORRECTION — reviewer verification-ledger Entry 3 (untracked `~/Downloads`
  file), to relay to K.M.:** the Fe total cross-section at 500 keV is **σ=7.80 b**,
  not the Entry-3 "77 b" — a 10× barn-conversion slip (`μ/ρ=0.08414` is itself
  correct). The Fe **shell-only** kill margin is therefore
  `σ_shell/σ = 1.7 kb / 7.8 b ≈ 220×`, not `22×`. **Verdict unchanged** (Branch-no
  static extension excluded; margin ~10× *larger*, consistent with the "up to 200×"
  quoted elsewhere in Entry 3). Pb margin unchanged: `1.5 kb / 0.69 kb ≈ 2.2×`.
  The ledger working, as the reviewer invited.

**Build + commits.** Branch `analysis/letter-round3-updates` (worktree `wt-round3`),
all commits tagged `[REVIEW: pending-orchestrator]`, **DO-NOT-MERGE**. Letter
compiles clean via `latexmk` (exit 0, **11 pp**, zero undefined refs / citations
with aux present); tracked PDF `sve_vacuum_birefringence_letter.pdf` rebuilt via
`make paper`; `make verify` green. Paper edits, one section per commit: intro (D4)
· item (v) Branch-no · sector-scope Branch-no + copper + `ℓ_node` def ·
magnetic C1/C2/C3 · frame/sidereal (A4/D5) · falsify (D6 + bounds) · Table I (D7).
**Flag for orchestrator:** R3-A **reverses** the P4 v3 Branch-YES resolution
(held-E-loads); this is the co-author's decided Branch-no ruling applied, not a
silent change — P4 row marked `SUPERSEDED by R3-A` above.

## Phase plan

1. **Ledger** (this doc) — committed.
2. **Autonomous physics** — P6 re-derivation · P4 copper number (informs the P4 ruling) ·
   D1 write-up. Fire without waiting on rulings.
3. **Grant-gated forks** — P4 (held-E-loads yes/no) · P5 (radiative-keying ontology). Walk
   P5 before any engine dispatch.
4. **Paper v3 integration** — **DONE.** Every resolved row folded into `main.tex`
   (P4/H3 · P5 · H1 · P6 · H4); postulate count flipped honest (two, grounded in `∇·B=0`);
   E1/E2 protocol paragraphs landed at v2 (#578). Letter stamped **v3**,
   compiles clean (10 pp, zero undefined refs), committed PDF rebuilt.

Each row is updated in the PR that closes it.
