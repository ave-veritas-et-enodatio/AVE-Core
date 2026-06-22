# Arc record — Vacuum-birefringence / VCA bench (2026-06-22)

Captures the workflow chain that resolved FORK-1 (is the μ-grade saturable or an ideal inductor under static
B?), canonicalized the node-up V/I-keyed dual + the PVLAS static-B verdict, and surveyed the facility
landscape for the real (E-route) test. This arc record is the orchestration spine; the physics lives in the
research docs + canonical leaves linked below.

## §0 One-paragraph state

The vacuum cell is one LC tank with two reactive grades keyed on **different drive variables**: ε = varactor
keyed on **V** (a static E is a real operating point → E-route birefringence), μ = relativistic inductor
keyed on the circulating **I** (a static external B has ∂B/∂t = 0 → no internal circulation → S_μ = 1 →
`δn_μ = 0` analytically exact). So **PVLAS / BMV (static B) do NOT test AVE**; their null is the expected AVE
result. The discriminating experiment is the **E-route** (HIBEF @ European XFEL), where AVE rides
`7.5/α³ ≈ 1.93×10⁷` above differenced Euler-Heisenberg on a shared E²-leading slope. Form is the AVE-distinct
chord (the vacuum saturates at all, the static-B route is *exactly* transparent — categorical); the magnitude
rides the α-echo family.

## §1 Workflow chain

| Step | Workflow | What it produced | State |
|---|---|---|---|
| FORK-1 resolution | `wy1dl84a3` | node-up V/I-keyed dual, large+small-signal, mu-ideal-inductor verdict, B_SNAP reconciliation | DONE → [`research/2026-06-22_node-up-small-large-signal_result.md`](../research/2026-06-22_node-up-small-large-signal_result.md) |
| C4 reconciliation | `w8d8hyhvz` | C4 = doc-local label, already closed in-corpus (W6 `e5307e53`); R1/R2/R3 taxonomy; regime sweep | DONE → [`research/2026-06-22_c4-symmetric-loading-reconciliation.md`](../research/2026-06-22_c4-symmetric-loading-reconciliation.md) |
| Canonicalization | **PR #357** (`canon/birefringence-nodeup` → `main`, merged 2026-06-22) | leaves `clm-vca7r1` (node-up) + `clm-pvlas1` (PVLAS verdict); `test_vca_node_regime_sweep.py` + `test_vca_r01_static_b_mu_keying.py` | MERGED |
| Facility / tolerance survey | `w14ptjz80` | 26 setups, cited tolerances, E-route vs magnetic-route split | DONE → [`research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md`](../research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md) |
| VCA skill | `w5pj40157` | the VCA (vacuum-circuit-analysis) discipline skill | DONE (AVE-Skills commit PENDING, Grant-gated) |
| Network derivation | `w9yaz7tku` | coupled-grade network equations | **RUNNING** |
| Bench-hunt | `wmjbpekmc` | E-route bench candidate / discriminator design | **RUNNING** |
| Doc arc (this) | — | the 3 research docs + leaf-citation fix + this arc record | DONE (this PR) |

## §2 Lessons

- **The rescue was caught twice.** The mu-ideal-inductor verdict is the one that "saves AVE from PVLAS" —
  exactly a convenient-rescue shape. The substrate-native-check forced deriving the μ-grade kernel argument
  (`I`, not `|B|`) *before* trusting the engine's `|B|`-keying (catch #1, FORK-1). The C4 pass then found the
  apparent INVARIANT-S2 collision was a **stale-citation artifact already closed in-corpus** (W6 commit
  `e5307e53`), not a live contradiction needing a new rescue (catch #2). Both passes derived the answer and
  let the substrate decide; neither debugged toward keeping AVE alive. The rescue-guard PASSES on all six
  anti-rescue tells (predates the question / pays rent / one mechanism many uses / independent E=mc²
  corroborant / symmetric-standard pass / the rejected fork would itself have failed).

- **An overclaim was found inside the anti-overclaim canonicalization.** The earlier tolerance pass headlined
  "PVLAS falsifies AVE ~37,000×" — built by feeding a *static* B through the **ε-route** propagating-wave
  proxy `A = cB/E_yield`, conflating an energy-density construction with a static-DC-B response. The
  synthesis arithmetic-catch corrected it: even the *rejected* saturable-μ counterfactual gives
  `δn ≈ −4.4×10⁻¹⁹` at 2.5 T, ~2600× **above** (not below) the PVLAS floor — so PVLAS never discriminates the
  forks regardless. The headline is **RETRACTED**; the resolved framing is "magnetic-route does not test
  AVE." (Lesson: an anti-overclaim canonicalization can still carry an inherited overclaim in its framing —
  re-run the arithmetic, don't inherit the inequality direction.)

- **Form/value scoreboard.** AVE **forces the FORMS** (the vacuum saturates at all → tree-level O(1)
  structure QED lacks; the static-B route is *exactly* transparent → a categorical zero-vs-nonzero
  discriminator; the E²-leading shared slope) and **imports the dimensionful VALUE** of the coefficient (the
  `7.5/α³` ratio is an α-echo at the value level — AVE does not derive α). The chord lives in the **forward
  predictions** (the categorical static-B null + the E-route coefficient gap), not in the value of the
  number. Consistency/manifestation class, tagged on both leaves.

## §3 Open items

- **VCA-R01 code fix** — the fdtd engine keys μ-saturation on static `|B|` (`fdtd_3d.py`:231,:245,:396-397,
  :425-426; `scale_invariant.py`:198 caller), contradicting the canonical R3 verdict for a static B. The
  desired R3 behaviour is an `xfail` in `test_vca_r01_static_b_mu_keying.py` (flips to PASS once fixed). The
  fix is **gated on deriving the I-keyed per-cell circulation → I_max threshold** (a derivation, not a
  variable swap — substrate-first-for-numbers). Separate validated PR. `flagged-for-separate-PR`.
- **Canonical magnetic-yield scale** — `B_SNAP` (energy-density-matched) vs `E_YIELD/c` (the ε-proxy) differ
  by ~5.01×; surface to Grant before any leaf quotes a *magnetic* birefringence number. (Does not touch R3:
  `A_I = 0` ⟹ `δn_μ = 0` independent of either scale.)
- **Stale gravity-sign-result flags** — the 2026-06-05 gravity-sign result/prereg carry stale "Not reconciled"
  + `CLAUDE.md`:58,:60 citations (live content at :75). Auditor-lane propagation item (Rule-12 preserve body,
  git-only trail). Surfaced, not silently edited.
- **VCA skill AVE-Skills commit** — `w5pj40157` produced the VCA discipline skill; the AVE-Skills repo commit
  is HARD-GATED on Grant go (one-repo-two-checkouts amendment ledger).

> **PENDING: fold in network-derivation (`w9yaz7tku`) + bench-hunt (`wmjbpekmc`) results when they land.**
> The coupled-grade network equations (the central derivation) and the E-route bench candidate /
> discriminator design are in flight; their results extend §1 and may add a 4th research doc + a bench
> pre-reg. Do not close this arc until both land and are reconciled against the node-up dual.

---

### Links

- Leaves: [`node-up-small-large-signal.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md) (`clm-vca7r1`),
  [`pvlas-static-b-verdict.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md) (`clm-pvlas1`),
  [`vacuum-birefringence-e4.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md) (`clm-pp3qwf`, E-route coefficient).
- Tests: `src/tests/test_vca_node_regime_sweep.py` (direct-kernel control), `src/tests/test_vca_r01_static_b_mu_keying.py` (VCA-R01 defect xfail).
- Canonicalization: PR #357.
