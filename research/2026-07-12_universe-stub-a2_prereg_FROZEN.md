# A2 — Universe stub (projected \(\Omega_{\rm freeze}\) IC) — FROZEN prereg

**Freeze discipline.** This prereg is frozen **by push**: it is pushed as its own
commit BEFORE any A2 driver / bias helper / test code exists (ave-prereg v1.7
Step 3.11). Bins below are frozen; **frozen bins enforce, flags don't**.

**Authorization.** A1 landed **bin (i) FACE-PASSIVE-MATCHED**
(`research/2026-07-12_radiating-face-a1_result.md`, branch
`analysis/radiating-face-a1`). A1 prereg “Next after (i)” charters A2. Grant
2026-07-12 session: proceed to A2 when ready. **HOLD / no merge** until Grant
trusts the implementor lane.

**Class.** Engine-completeness / **projected cosmic IC into local solid BC** —
NOT a new chord, NOT live Machian integral, NOT full outer mesh, NOT
`genesis_v{N}` / srs v18+ / fourth engine. Rule-14: reuse A1
`NativeCageIMEX` radiating face + a thin projected-IC bias (srs Decision-5
pattern ported as IC, not as remanence).

**α-CLEAN on the verdict path.** \(\alpha\) may appear only as the **IC scale**
that sets the frozen bias angle \(\theta_\star=\sqrt{\alpha}\) (same Decision-5
scale as `apply_omega_freeze_ic`). Passivity / \(\mathcal{R}\) / OFF–ON
discrimination arithmetic must not import `ALPHA`. Do **not** claim
\(\Omega_{\rm freeze}\to\alpha/G\) forward derivation (u₀\* B2: \(\alpha,G\)
**fix** \(u_0^*\); \(\mathcal{J}_{\rm cosmic}\) tests).

---

## Sector header (mandatory)

- **SECTOR** = local solid (Regime I–II) looking into A1 matched radiating face,
  with a **slow projected cosmic IC** imprinted as constitutive / channel bias
  at \(t=0\). Not electron remanence; not live horizon integral; not melt.
- **Does the engine carry the DOF?** Interior + A1 face YES (landed). **Projected
  \(\Omega_{\rm freeze}\) bias on cage IMEX** — NO (srs-only today via
  `apply_omega_freeze_ic`). **Live Machian \(\xi\) integral / outer mesh** — NO
  (explicitly out of A2 thin charter).
- **MODE** = mechanical bulk + shear leave-taking (A1) + IC chirality bias
  (projected). EM-transverse not required.
- **REGIME** = I–II (sub-yield). Near-yield face is optional stress, not default
  PASS.
- **PHASE-STATE** = cold solid + infinite exterior port (A1) + frozen cosmic
  chirality projection (A2).
- **Instrument:** A1 open-port pulse **with bias OFF vs ON**; closed-box gate
  reused; sabotage = wrong-sign / oversized \(\theta\).
- **consistency-vs-emergence:** A2 is **FIREABLE instrumentation** /
  CERTIFICATION that projected IC does not break the radiating face. Success is
  **not** emergence of \(G\), \(u_0^*\), or CMB \(\mathcal{J}_{\rm cosmic}\).

---

## Corpus sweep (STEP-0)

| Prior | Finding |
|---|---|
| A1 prereg / result | bin (i); A2 chartered as next; no A2 prereg yet |
| `apply_omega_freeze_ic` (`chiral_lattice_v10`) | Cosmic chirality bias at \(t=0\), \(\theta\propto\sqrt{\alpha}\), writhe sign — **srs only** |
| `NativeCageIMEX` | A1 face; **0** Machian / \(\Omega_{\rm freeze}\) hooks |
| Stage-2 cage prereg \(\xi_{\rm machian}\) fence | Dimensionful \(G\) / \(\xi\) are **not** Stage-2/A2 claims; \(\xi\) = hierarchy marker / sabotage fence only |
| KB Ch 12 / B2 | \(G\) MIXED; \(\alpha,G\) fix \(u_0^*\); do not claim forward \(\Omega_{\rm freeze}\to\alpha\) |
| Namespace | \(\xi_{\rm Machian}\) (\(XI\_MACHIAN\)) ≠ \(\xi_{\rm topo}\) |

**VERDICT: authorized-open.** Thin projected-IC stub on cage+A1 is genuinely
missing; srs IC is the pattern to port as **IC**, not remanence.

---

## Target (one sentence)

On the A1 `NativeCageIMEX` radiating face, imprint a **frozen projected
\(\Omega_{\rm freeze}\) chirality bias** at \(t=0\) (Decision-5 scale
\(\theta_\star=\sqrt{\alpha}\), fixed cosmic sign) and gate that the face stays
passive / matched while OFF vs ON is **measurable**, with sabotage that trips.

---

## Analytic expectations (mandatory numbers)

### Projected IC (not dynamics)

\[
\theta_\star = \sqrt{\alpha} \approx 0.0854
\quad(\text{same scale as srs } \texttt{apply\_omega\_freeze\_ic}),
\quad
\hat{\Omega}_{\rm freeze}=+1
\quad(\text{frozen right-handed cosmic sign for the default arm}).
\]

Bias acts on the seeded cage state by a **planar channel rotation** in the
\((V_x,V_y)\) components (cage has scalar \(V\) per cell — implement as a
**small preferred-axis shear offset** proportional to \(\sin\theta_\star\) along
a fixed cosmic axis \(\hat{e}_\Omega\), plus optional tiny orthogonal couple so
the OFF–ON residual is not a pure amplitude shift). Exact helper signature is
implementation detail; the **frozen** content is: amplitude \(\theta_\star\),
sign \(+1\), applied once at \(t=0\), then free A1 evolution.

**Honesty:** this is a **projection** of cosmic IC into the local solid — not a
live integral over \(R_H\), not a derivation of \(G\) from \(\xi\), not
remanence.

### A1 face must remain green (with stub ON)

Reuse A1 floors (unchanged):

\[
\mathcal{R} \equiv \frac{H_{\rm end}}{H_0} < 10^{-2},\qquad
\max_t H(t)/H_0 \le 1+\varepsilon_{\rm inj},\quad \varepsilon_{\rm inj}=10^{-3}.
\]

Closed-box control still PASS.

### OFF–ON discrimination (fireable)

Let \(\mathcal{R}_{\rm off}\), \(\mathcal{R}_{\rm on}\) be the A1 residual on
identical seeds with bias OFF vs ON. Define

\[
\Delta_{\rm bias} \equiv \bigl|\mathcal{R}_{\rm on}-\mathcal{R}_{\rm off}\bigr|
\quad\text{or}\quad
\bigl|A_{\rm asym,on}-A_{\rm asym,off}\bigr|
\]

where \(A_{\rm asym}\) is a frozen asymmetry of interior \(V\) about
\(\hat{e}_\Omega\) at mid-window (implementation picks one primary; prereg
accepts either if declared in the result).

**Floor:** \(\Delta_{\rm bias} > 10^{-6}\) (above float noise; well below A1
\(\mathcal{R}\) itself). Stub that leaves **zero** OFF–ON difference fails
discrimination even if A1 stays green.

### Sabotage

Wrong-sign oversized bias \(\theta = -10\,\theta_\star\) (or \(+10\,\theta_\star\)
with flipped cosmic axis) must **TRIP**: either passivity fails
(\(H_{\max}/H_0 > 1+\varepsilon_{\rm inj}\)) **or** \(\mathcal{R} \ge 10^{-2}\).
Silent green sabotage = fail of the stub gate.

### Machian fence (not a PASS claim)

`XI_MACHIAN` may appear only as a **named hierarchy fence** in prose /
optional log — never as the bias amplitude, never as a derived-\(G\) claim.
A2 does **not** implement the Machian impedance integral.

---

## Frozen bins (enforce)

| Bin | Label | Criterion |
|---|---|---|
| **(i)** | **STUB-PASSIVE-BIASED** | Closed-box PASS; A1 passivity + \(\mathcal{R}<10^{-2}\) with bias **ON**; \(\Delta_{\rm bias}>10^{-6}\); sabotage TRIPS |
| **(ii)** | **STUB-WEAK** | A1 green with bias ON, but \(\Delta_{\rm bias}\le 10^{-6}\) **or** sabotage silent |
| **(iii)** | **STUB-BREAKS-FACE** | Bias ON breaks A1 passivity or \(\mathcal{R}\) floor |

Flags (non-enforcing): whether \(\Delta_{\rm bias}\) is carried by \(\mathcal{R}\)
vs asymmetry; numerical \(\theta_\star\) float printout.

---

## Out of scope

- Live Machian integral / full outer mesh / cosmic horizon DOF
- Forward \(\Omega_{\rm freeze}\to\alpha/G/u_0^*\) claims
- Node-mint, melt EOS, `genesis_v{N}`, srs v18+, fourth engine
- Equating A1 PML/port with cosmic \(\Gamma=-1\)
- Merging HOLD PRs (#652 / #655 / #656) without Grant

---

## Deliverables (after this freeze push)

- This FROZEN prereg (this commit, pushed first).
- Orchestration pointer in `_orchestration/` + index line.
- Later: thin driver + tests + result on follow-on commit(s); **HOLD PR, no merge**.

---

## Physical / EE picture (for the result narrative)

Cosmic freeze picks a preferred chirality once; the local solid does not recompute
the horizon — it **inherits a projected bias** the way a circuit inherits a
slow DC offset / preferred-axis mismatch from the larger world. A1 is the
**matched port** into that world; A2 is the **IC tag** that the world is not
perfectly isotropic. If the port stays matched and the tag is detectable but
not destructive, the stub is doing its job.
