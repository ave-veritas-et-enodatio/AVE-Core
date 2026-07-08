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
| **P4** | Propagation commitment (disclaimer vs charge-keyed) | **NEEDS-RULING** | fork located; our answer = YES loads; copper number owed |
| **P5** | Magnetic functional S_B + radiative-keying unification | **NEEDS-RULING** | Eq (6) static-only; full S_B in corpus not paper |
| **P6** | Sidereal boost order (β vs β²) | **ORDER RESOLVED → NEW FRAME-FORK** | first-order β (CMB frame) ⇒ ~4.9e-3; but frame CMB-vs-lab unresolved in paper (#574) |
| **H1** | Postulate count (1 → honest 2–3) | **OWED-PROSE** | "single" at L6/L42/L799 |
| **H2** | Drop "theorem of the confinement" | **OWED-PROSE** | L298–299 |
| **H3** | Engine-vocabulary leak | **OWED-PROSE** | 4 term families, lines listed |
| **H4** | Table I peak vs pulse-integrated | **PARTIAL** | peak convention stated; integrated value owed |
| **H5** | Record-floor wording (2.4e-10 vs 8e-11) | **OWED-PROSE** | abstract L53–54 |
| **D1** | Engine-independent route to N=7 | **PARTIAL (≈met)** | analytic Nyquist route already registered |
| **E1** | Overlap certificate (null branch) | **OWED-PROSE** | confirmed absent |
| **E2** | Bright-branch confirmation plan | **OWED-PROSE** | confirmed absent |

Autonomous (no ruling): P6, D1, H2, H3, H5, E1, E2, and the P4 copper number.
Grant-gated: **P4** (does a held static E load?), **P5** (is the key radiative
far-field character?). H1's exact count depends on the P5 ruling.

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

## P4 — Propagation commitment: static-field disclaimer vs charge-keyed loading — NEEDS-RULING

**The contradiction (both in the Letter).** (a) DISCLAIMER `main.tex:330–331` — we do
NOT assert the kernel as a universal static-field constitutive law. (b) CHARGE-KEYED
scoping (appears twice, §II.B) — a held field is a real operating-point bias, so it
loads. These read as two different theories.
**Our current answer (round-3 `[DERIVED: CHARGE-KEYED]`, merged #547).** YES — a probe
crossing a strong *non-uniform* static field experiences the loaded permittivity
(ε keys on mean-square, DC included). We are on Branch YES.
**The fork.** Confirm YES/NO explicitly and pre-register it. If YES, we owe an
X-ray-through-ordinary-matter constraint (see owed). If NO, the charge-keyed sentence
comes out and muonic-H restates as a domain-restriction demonstration (prose surgery).
**Owed (Branch YES).** (1) Compute the AVE refractive-decrement contribution for an
~8 keV photon in copper: volume-average ½A²(r) over the lattice with a reduced-Compton
cutoff, vs the measured Cu decrement (δ ~ 2.4e-5, known ~1%). (2) State whether
dispersion fences Delbrück / γ-attenuation above the 511 keV response scale.
**Where.** `main.tex:330–331`; `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md`;
`provenance.md:434–453` (#547). **All numbers to be OUR compute, not any external estimate.**

## P5 — Magnetic-sector functional Eq (6): static endpoint vs full S_B(circulation) — NEEDS-RULING

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

## P6 — Sidereal boost order — ORDER RESOLVED (first-order β); NEW frame-fork surfaced (PR #574)

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

## H1 — Postulate count: stated ONE, body uses more — OWED-PROSE

**Conclusion.** "Single constitutive postulate" (abstract L42, conclusion L799, file
comment L6) is an undercount: the body adds the magnetic circulation-keying statement
(L362) and a radiative-sector scoping statement. Honest count ≥ 2 (kernel + magnetic
keying), arguably 3 (incl. radiative-scoping). **Depends on the P5 ruling** (whether
radiative-scoping is a third postulate or a derived consequence).
**Owed.** Edit abstract + conclusion to the honest count (or explicitly demote the extra
statements to scoping). **Where.** `main.tex:L42, L799, L6, L362`.

## H2 — "Theorem of the confinement" overclaims — OWED-PROSE

**Conclusion.** "The exponent is therefore a theorem of the confinement, not a fitted
parameter" (`main.tex:298–299`) overclaims — the derivation is explicitly conditional on
the confinement/energy-conservation premise (L290–298), so p=2 is a *consequence* of the
hypothesis. The two-channel p-discriminator sentence (L299–302) is the keeper.
**Owed.** Replace "a theorem of the confinement" → "a consequence of the confinement
hypothesis"; keep the p-discriminator sentence unchanged.

## H3 — Engine-vocabulary leak into the standalone Letter — OWED-PROSE

**Conclusion.** Four framework-internal term families appear undefined in the Letter:
"lattice pitch / lattice-scale" (L282–284, L343, L353–355), "deep-cold" (L329),
"operating-point bias" (L281, L352), "charge-keyed" (L281, L351). The provenance note
that claims the Letter is grep-clean of engine vocabulary (`provenance.md:L24`) is stale.
**Owed.** Define or replace all four with self-contained language; re-grep to confirm.

## H4 — Table I peak-field vs pulse-integrated — PARTIAL

**Conclusion.** Table I is on the peak-field convention (peak carrier amplitude
E = 8.68e13 V/m; A² = 5.90e-7; peak-field P_flip = 5.39e-3 / 4.28e-3 / 9.28e-3 at
9835 / 8766 / 12914 eV), explicitly stated (`main.tex:514–518`, caption L583–587). No
pulse-envelope-integrated/measured-expectation value is given.
**Owed.** Recompute lane supplies the pulse-integrated expectation P_flip; then tabulate it
alongside the peak column or add a caption sentence that peak-field is the envelope maximum
(so no experimentalist chases a spurious factor). **Our numbers are the compute basis** — no
external estimate adopted.

## H5 — Record-floor wording — OWED-PROSE

**Conclusion.** Abstract (`main.tex:53–54`) labels 2.4e-10 the "record X-ray-polarimeter
purity floor"; the body (L695–698) and figure caption (L785–787) correctly give the record
as 8e-11 (Karbstein2021) with 2.4e-10 the conservative single-measurement demonstrated floor
(Marx2013).
**Owed.** Reword the abstract: 2.4e-10 = "conservative/demonstrated floor"; reserve "record"
for 8e-11 (or drop "record" from the abstract phrase).

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

## E1 — Overlap certificate for the null branch — OWED-PROSE

**Conclusion.** CONFIRMED ABSENT. The kill criterion (`sec:falsify`, `main.tex:674–720`)
commits a 5σ pump-on null (P_flip < 1e-8 at ≥1e18 W/cm²) and a third-party extraction
procedure, but has NO independent overlap-witness requirement. A null without a witness of
demonstrated pump-probe overlap at the stated intensity is an *absence*, not a kill — the
mirror of the false-victory failure (a false-execution/timing-miss null).
**Owed.** Insert a paragraph requiring an independent overlap witness (interleaved shots on a
gas puff / wire producing pump-driven signal) bracketing the data runs, as a precondition for
scoring a null as a kill.

## E2 — Bright-branch confirmation plan — OWED-PROSE

**Conclusion.** CONFIRMED ABSENT. The section registers only the null branch plus a bare
"a value at the 1e-3 level confirms the model" (`main.tex:719`); no calibrated-attenuator plan
and none of the three positive fingerprints. Registering *how a positive is believed* is the
same discipline as registering how a null kills.
**Owed.** Insert a bright-branch paragraph: a true ~1e-3 signal saturates an unattenuated
crossed channel, so run first well-overlapped shots through a calibrated attenuator; confirm
via the fingerprint battery — Δt peak at femtosecond width, sin²(2ψ) four-lobe polarization
dependence, I² intensity scaling. Predicted confirm level P_flip = 4.28e-3–9.28e-3.

---

## Phase plan

1. **Ledger** (this doc) — committed.
2. **Autonomous physics** — P6 re-derivation · P4 copper number (informs the P4 ruling) ·
   D1 write-up. Fire without waiting on rulings.
3. **Grant-gated forks** — P4 (held-E-loads yes/no) · P5 (radiative-keying ontology). Walk
   P5 before any engine dispatch.
4. **Paper v3 integration** — fold every resolved row into the manuscript; flip the postulate
   count honest (after P5); add the E1/E2 protocol paragraphs.

Each row is updated in the PR that closes it.
