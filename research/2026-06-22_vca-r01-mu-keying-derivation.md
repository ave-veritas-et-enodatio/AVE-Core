# VCA-R01 — mu-grade keying: derivation verified, clean implementation BLOCKED

**Status:** FLAGGED — derivation correct, implementation subtle (NOT applied; substrate-first).
**Date:** 2026-06-22
**Branch:** `fix/vca-r01-fdtd-mu-keying` (worktree off `origin/main` @ 865b9798)
**Scope:** confirm the VCA-R01 bug + the I-keyed derivation, determine whether the
fix is a clean swap. Verdict: the **physics derivation is correct and already
canonical**, but a clean FDTD implementation is **blocked** by a signature/threading
refactor, a propagating-wave singularity in the pointwise argument, and a
shared-kernel blast radius into correct B-keyed matter callers. **No code changed.**

> This note is a *substrate-first flag*, not a rescue. The corpus leaf
> `node-up-small-large-signal.md` §5 already records this fix as
> "flagged for a separate validated PR" with three blockers; this note verifies
> those blockers empirically and adds one new load-bearing finding (the
> propagating-wave singularity) that strengthens the flag.

## 1. The bug (verified at origin/main @ 865b9798)

`src/ave/core/fdtd_3d.py::_compute_local_mu(H_component)` keys the mu-grade
saturation on the **instantaneous static flux amplitude**:

- `:231` `B_local = self.mu_0 * np.abs(H_component)`
- `:245` `return mu_base * saturation_factor(B_local, self.b_yield)`
- `:396-397`, `:425-426` replicate it in `total_energy()` / `energy_density()`
- `self.b_yield` defaults to `B_SNAP` (`:56`).

`scale_invariant.mu_eff(amplitude, yield_limit, mu_base)` (`:198`) and
`saturation_factor` (`:107`) are **correct as written** — they evaluate the
Axiom-4 kernel `S(A)=sqrt(1-(A/A_yield)^2)` on whatever amplitude the caller
passes. The semantic error is at the **caller**, which feeds `mu_0*|H|` with
`b_yield=B_SNAP`.

Confirmed numerically (worktree venv):
- `XI_TOPO*C_0 = 124.3840330668883 A` (canon `I_max ≈ 124.4 A`, `XI_TOPO=4.149e-7 C/m`).
- `B_SNAP = 1.890e9 T`, and `B_SNAP^2/(2*mu_0) / (m_e c^2 / l_node^3) = 1.0000000000000002`
  — so **B_SNAP is an energy-density scale**, the flux whose magnetic energy
  density equals a node's rest-energy density — **NOT** a kernel-argument threshold.

Current test state on origin/main: `test_vca_r01_static_b_mu_keying.py` →
1 xfail + 1 pass (positive control); `test_vca_node_regime_sweep.py` → 10 pass.

## 2. The derivation (verified CORRECT against the canonical primitive)

The mu-grade IS the **relativistic inductor**
(`relativistic-inductor.md:15,:18`, clm-p5cf3t), keyed on the **circulating
current** `I`, NOT the external flux `B`:

```
L_eff(I) = L0 / sqrt(1 - (I/I_max)^2),   I_max = xi_topo * c ≈ 124.4 A
```

By the Topo-Kinematic map (`I = xi_topo*v`), the kernel argument is a normalized
**circulation velocity** `A_I = I_circ/I_max = v_circ/c`. By Faraday/Lenz the
internal Cosserat circulation is induced by the **rate** `dB/dt = -curl E`, so a
**static** external B (`dB/dt = 0`) induces **zero** internal circulation
→ `I_circ = 0` → `A_I = 0` → `S_mu = 1` exactly → `mu_eff = mu_0` (transparent,
regime R3). This is the canonical R3 result, and the leaf's derived-vs-asserted
ledger (`node-up-small-large-signal.md:175`) tags it **DERIVED (analytically
exact)**. The PVLAS/BMV static-B null is therefore *consistent* with AVE
(`pvlas-static-b-verdict.md`, clm-pvlas1), not a falsification.

**Verdict on the physics: CORRECT.** The argument is rate/circulation-driven
(`dB/dt`), not `|B|`-amplitude-driven; the threshold is `I_max = xi_topo*c`, not
`B_SNAP`. The adversarial check (derivation-sound / matches-relativistic-inductor /
not-a-rescue / symmetric-standard) holds, and the I-keying is independently
derived upstream (E=mc^2 chain) with **zero** static-B/PVLAS mentions in the
primitive (grep-confirmed) — so static-B transparency is a *forced consequence*,
not a fitted input.

## 3. Blocker A — signature mismatch: the xfail test cannot be satisfied by the derived argument

`_compute_local_mu(self, H_component)` is a **pure function of an instantaneous
amplitude array** — no `dt`, no history, no `curl_e` (=`-dB/dt`). The xfail test
(`test_static_external_B_leaves_mu_unloaded`) calls
`eng._compute_local_mu(Hx_static)` on a **single static array** and asserts
`mu_eff == mu_0`.

The derived argument `A_I = (|dB/dt|/|B|)·l_node/c` requires `dB/dt`. **It cannot
be computed inside a function whose only argument is the instantaneous amplitude.**
The direct-kernel positive control sidesteps this exactly by *supplying* `I_vac=0`
by hand (`test_vca_node_regime_sweep.py:87` — "Static drive ⇒ no time-variation ⇒
no induced circulation"); it does **not** derive `I_vac` from a field state. The
engine has the opposite information: an instantaneous field with no
static-vs-propagating label.

To flip the xfail to PASS one must either:
- **(a)** make `_compute_local_mu` return `mu_0` unconditionally for any
  amplitude — which is itself a *guess* about how the rate enters and **throws
  away** the saturation behaviour the propagating-wave physics needs; or
- **(b)** **re-signature** `_compute_local_mu` / `_compute_ch` to receive
  `curl_e`, and rewrite `update_magnetic_field` to thread it in.

Path (b) is a genuine engine refactor, **not** the 5-site amplitude swap the
brief enumerates (`:231/:245/:396-397/:425-426 + scale_invariant`). The site list
does not include the signature/threading change, which is where the real work is.
The `total_energy()` / `energy_density()` sites (`:396`, `:425`) have **no rate
available at all** (they are post-hoc snapshots over `Hx/Hy/Hz`), so the R3
behaviour there cannot be recovered without storing per-cell circulation state.

## 4. Blocker B — propagating-wave singularity in the pointwise argument (NEW finding)

Even granting the rate were threaded in, the derived **pointwise** argument
`A_I = (|dB/dt|/|B|)·l_node/c` is **not** cleanly discretizable, because for a
propagating monochromatic wave `B ~ cos(ωt)`:

```
|dB/dt| / |B| = ω·|tan(ωt)|   →   DIVERGES at every field zero-crossing (cos ωt = 0)
```

Empirically (visible-band `ω=1e15 rad/s`, `ω/ω_C ≈ 1.3e-6`), sampling `A_I` over
one period gives values `[0, 7e-7, 2e-6, 2e10, 2e-6, …]` — **`A_I = 2.1e10 ≫ 1`**
at the wave nodes. After the kernel's `clip(0, 1-ε)`, that drives `S_mu → 0`
(`mu_eff → 0`) **at every zero-crossing of every propagating wave** — which would
**regress the validated propagating-wave physics** (the exact thing this fix must
not break).

The derivation conflates two distinct objects: the **envelope** rotation rate `ω`
of a coherent circulating mode (constant, the physically intended argument) versus
the **instantaneous pointwise** ratio `|dB/dt|/|B| = ω·|tan(ωt)|` (unbounded). The
FDTD has only the instantaneous pointwise field at one timestep; recovering a clean
per-cell `ω` (or the closed-loop circulation `I = ∮ H·dl`) requires
envelope/phase/curl-H bookkeeping the engine does not carry. This is precisely the
"curl-H bookkeeping the engine lacks" escape hatch the task flagged — and it is
**load-bearing**: the naive `I_circ ~ |dB/dt|/|B|` swap does NOT reproduce the
propagating regime, it breaks it.

## 5. Blocker C — shared-kernel blast radius into correct B-keyed matter callers

`scale_invariant.mu_eff` is shared by callers for which **B-amplitude keying is
the correct physics**:
- `superconductor.py:81 meissner_mu_eff(B_applied, B_critical)` — a **genuine**
  Meissner matter case: `μ → 0` as applied `B → B_critical` is *correct*
  superconductor screening, not the vacuum mu-grade. Rate-keying `mu_eff` would
  **break** this.
- `yang_mills.py:115,:162` — keys on `B_field` vs `B_SNAP`.
- `fdtd_3d_jax.py:80` — a JIT copy of `scale_invariant.mu_eff` (a *second* site
  needing the identical change).

So the brief's instruction to edit `scale_invariant.py` is **at odds** with the
Meissner caller. A correct fix must be **surgical to the FDTD vacuum path** and
leave `mu_eff`'s amplitude-semantics intact for matter callers. Additionally, a
**second, distinct** mu-saturation path exists — `cosserat_master_equation_fdtd.py`
keys `K_eff(V) = K_omega_0/S(V)` on the microrotation sector — and the leaf
(`node-up-small-large-signal.md:202-205`) requires a correct fix to reconcile both.

## 6. What a clean fix would require (for a future validated PR)

A correct, substrate-first fix is a bounded engine extension, not a swap. It needs,
in order:

1. **A per-cell circulation observable.** Derive the Yee-cell mapping from the
   discrete closed-loop circulation `I_cell = ∮ H·dl` (the curl-of-H / Ampère
   loop already computed in `update_electric_field`) onto `I_max = xi_topo*c`.
   This mapping does NOT exist in the corpus — constructing it (including its
   l_node-scale normalization and the `|B|→0` behaviour) is a derivation gated by
   substrate-first-for-numbers, and should be canonicalized as a leaf before code.
   Note the **envelope-vs-pointwise** distinction (Blocker B): the argument must be
   the circulating-mode rate, not the instantaneous `|dB/dt|/|B|`.
2. **A new FDTD-private mu-path** keyed on `A_I = I_cell/I_max`, threaded via a
   re-signatured `_compute_local_mu(H_component, circulation)` /
   `_compute_ch(...)`, with `update_magnetic_field` supplying the circulation.
   Leave `scale_invariant.mu_eff` (and the Meissner / yang_mills / JIT callers)
   **untouched** — they are correct B-amplitude matter callers.
3. **Reconcile the cosserat ω-keyed path** (`cosserat_master_equation_fdtd.py`)
   with the new FDTD circulation path.
4. **Energy-method sites** (`:396`, `:425`): either store per-cell circulation
   state across the step, or document that R3 transparency is a step-loop property
   not reproducible from a post-hoc field snapshot.
5. **Re-validate**: flip the xfail; confirm propagating-wave behaviour (and the
   acceptance suite) does not regress; keep the direct-kernel positive control green.

This is a multi-step derivation + engine extension that a future validated PR
owns — NOT this PR. **Decision is Grant's** on whether to schedule it (and on the
separate carried open: B_SNAP vs E_YIELD/c are not energy-density duals, differ
~5.01×; which magnetic-yield scale is canonical — see the leaf §-ledger).

## 7. Verdict

**FLAGGED — derivation correct, clean implementation BLOCKED. No code changed.**

- The **physics is correct** and already canonical
  (`node-up-small-large-signal.md` §2/§4/§5, clm-vca7r1; `relativistic-inductor.md`
  clm-p5cf3t): static B → `dB/dt=0` → `I_circ=0` → `A_I=0` → `S_mu=1` exactly.
- The **fix is NOT a variable swap.** Three independent blockers — (A) the
  instantaneous-amplitude signature cannot compute the rate; (B) the pointwise
  `|dB/dt|/|B|` argument diverges at propagating-wave nodes and would regress the
  validated propagating physics; (C) the shared kernel is correctly B-keyed for
  matter (Meissner) callers, so `scale_invariant.mu_eff` must not change.
- All three are independently recorded in the canonical leaf's §5 fix-direction
  note as the reason the fix was flagged-not-applied; this note **verifies them
  empirically** and adds Blocker B (the singularity) as new load-bearing evidence.
- The `xfail` remains the correct machine-checked encoding of the live bug until a
  future validated PR lands the engine extension in §6.

The `xfail` test stays `xfail`. No edits to `fdtd_3d.py`, `scale_invariant.py`, or
the tests. This is the discipline working at full strength: the wrong reaction is
to force a swap that flips a green test by breaking the propagating regime; the
right reaction is a clean flag with the mechanism named.
