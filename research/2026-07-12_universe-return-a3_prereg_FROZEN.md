# A3 — Universe return path (exterior → local) — FROZEN prereg

**Freeze discipline.** This prereg is frozen **by push**: it is pushed as its own
commit BEFORE any A3 driver / return injector / test code exists (ave-prereg v1.7
Step 3.11). Bins below are frozen; **frozen bins enforce, flags don't**.

**Authorization.** A2 landed **bin (i) STUB-PASSIVE-BIASED**
(`research/2026-07-12_universe-stub-a2_result.md`, HOLD #657). Grant 2026-07-12:
A2 passed → proceed to A3. **HOLD / no merge** until Grant.

**Class.** Engine-completeness / **bidirectional universe BC for local solids** —
NOT a new chord, NOT live Machian integral, NOT full outer mesh, NOT
`genesis_v{N}` / srs v18+ / fourth engine. Rule-14: reuse A1
`NativeCageIMEX` radiating face (+ optional A2 projected IC as a flag, not
required for the A3 PASS path).

**α-CLEAN.** No `ALPHA` on the verdict path. A2’s \(\theta_\star\) may appear only
as an optional IC flag arm.

---

## Sector header (mandatory)

- **SECTOR** = local solid with A1 matched radiating face that can **receive** a
  controlled exterior return packet from the port shell (universe → interior),
  without meshing the horizon.
- **Does the engine carry the DOF?** Outgoing leave-taking YES (A1). Projected
  IC YES (A2). **Controlled exterior→local return on the face** — NO (A1 port
  is absorber-only; no exterior source term).
- **MODE** = mechanical bulk / shear. Return packet is a slow shell drive, not
  EM-transverse.
- **REGIME** = I–II (sub-yield).
- **PHASE-STATE** = cold solid + infinite exterior stub (thin).
- **Instrument:** (1) outgoing pulse leave-takes; (2) after clearance, inject
  known exterior packet on `port_shell`; (3) measure interior energy rise;
  (4) sabotage = inject as if it were interior remanence / anti-causal pump.
- **consistency-vs-emergence:** A3 is **FIREABLE instrumentation**. Success ≠
  emergence of \(G\), CMB, or remanence.

---

## Corpus sweep (STEP-0)

| Prior | Finding |
|---|---|
| A1 bin (i) | Matched one-way leave-taking; \(Z_{\rm univ}=1\) absorber |
| A2 bin (i) | Projected \(\Omega_{\rm freeze}\) IC tag; no return path |
| A2 cascade | A3 “only if needed — still no full outer mesh” — Grant asked for A3 |
| `NativeCageIMEX` Newmark \(C\) | PSD absorber — **passive for outgoing**; no exterior source API |
| Machian / outer mesh | Explicitly out of thin charter (A1/A2) |

**VERDICT: authorized-open.** Natural completion of local↔universe BC stack:
radiate out (A1), inherit IC (A2), **hear the universe back** (A3) without an
outer mesh.

---

## Target (one sentence)

After an A1 leave-taking clears the interior, inject a **known exterior return
packet** on the port shell and gate that the interior **receives** a fireable
energy / asymmetry rise attributable to the exterior source — while the face
remains a passive absorber for *outgoing* content, and sabotage (treating the
return as interior remanence / continuous interior pump) trips.

---

## Analytic expectations (mandatory numbers)

### Protocol

1. **Leave-take arm (control):** A1 open-port sech; wait \(N_{\rm clear}\) steps
   until \(\mathcal{R}_{\rm pre} = H/H_0 < 10^{-2}\) (reuse A1 floor).
2. **Return inject:** for \(N_{\rm ret}\) steps, add a shell-localized drive
   \[
   \delta V \;=\; A_{\rm ret}\,\texttt{port\_shell}\,\sin(\omega_{\rm ret}\,t)
   \]
   with frozen \(A_{\rm ret}=0.01\), \(\omega_{\rm ret}\) set so a few cycles fit
   in the window (implementation freezes the exact \(\omega\) in the driver
   header; must be declared in the result). Drive is **exterior** — applied on
   the shell only.
3. **Reception observable:**
   \[
   \Delta E_{\rm int} \equiv E_{\rm int}(t_{\rm end}) - E_{\rm int}(t_{\rm clear})
   \]
   on the PML-excluded interior (Rule 10). **Floor:** \(\Delta E_{\rm int} >
   10^{-4}\,E_{\rm int}(t_{\rm clear})\) when a floor on absolute scale is
   needed, or simply \(\Delta E_{\rm int} > 10^{-6}\) in engine units when
   \(E_{\rm int}(t_{\rm clear})\) is near zero — pick the max of the two so a
   near-empty interior after leave-take still has a fireable bar.

### Passivity of the *absorber* (outgoing)

During the leave-take phase (before return inject), A1 passivity still holds:
\(H_{\max}/H_0 \le 1+\varepsilon_{\rm inj}\), \(\varepsilon_{\rm inj}=10^{-3}\).

During return inject, **total \(H\) may rise** — that is exterior work, not a
face failure. Do **not** score return-phase \(H\) growth as A1 passivity fail.
Score reception via \(\Delta E_{\rm int}\) instead.

### Null arm

Identical protocol with \(A_{\rm ret}=0\): \(\Delta E_{\rm int,null}\) must
satisfy \(\Delta E_{\rm int,ret} - \Delta E_{\rm int,null} > 10^{-6}\)
(discrimination).

### Sabotage

Re-wire the same drive onto the **interior** (not shell) as a continuous pump
after clearance — that is the remanence / fake-universe miswiring. Must **TRIP**
a named gate: either declare `sabotage_interior_pump=True` when
\(\Delta E_{\rm int}\) rises under interior drive **and** the run is flagged
as non-exterior, OR require that an honest classifier
`source_is_exterior` is False for that arm while True for the shell arm.
Frozen trip rule:

- Shell arm: `source_is_exterior = True` and \(\Delta E_{\rm int}\) above floor.
- Interior-pump arm: `source_is_exterior = False` **and** the adjudicator
  requires that a PASS bin never treats the interior-pump arm as exterior
  reception. Practically: **bin (i) requires shell reception PASS + interior
  sabotage arm correctly labeled non-exterior**; if the driver cannot tell them
  apart (same label / same mask), → bin (ii) or (iii).

Simpler frozen trip (preferred): interior-pump arm must produce
\(\Delta E_{\rm int} > 10\times\) the shell arm’s \(\Delta E_{\rm int}\)
**or** \(H_{\max}/H_{\rm clear} > 1+10^{-3}\) with the rise attributed to
interior cells — and the suite **fails** if the interior-pump arm is scored as
a successful exterior return. Adjudicator: shell PASS + interior arm
`trips_as_sabotage=True` (driver sets this when interior drive is used).

---

## Frozen bins (enforce)

| Bin | Label | Criterion |
|---|---|---|
| **(i)** | **RETURN-RECEIVED** | Leave-take A1 green; shell return \(\Delta E_{\rm int}\) above floor; null discrimination PASS; interior-pump sabotage correctly trips / labeled non-exterior |
| **(ii)** | **RETURN-WEAK** | Leave-take green but shell \(\Delta E_{\rm int}\) ≤ floor **or** null discrimination fails **or** sabotage unlabeled |
| **(iii)** | **RETURN-FAIL** | Leave-take broken **or** shell inject cannot couple to interior |

Flags (non-enforcing): optional A2 bias ON/OFF; exact \(\omega_{\rm ret}\).

---

## Out of scope

- Live Machian integral / full outer mesh / cosmic horizon DOF
- Claiming return packet *is* CMB / \(\mathcal{J}_{\rm cosmic}\)
- Node-mint, melt, `genesis_v{N}`, fourth engine
- Merging HOLD PRs without Grant

---

## Deliverables (after this freeze push)

- This FROZEN prereg (this commit, pushed first).
- Orchestration pointer + index line.
- Later: thin driver + tests + result; **HOLD PR, no merge**.

---

## Physical / EE picture (for the result narrative)

A1 is a matched **load** looking into the universe. A2 stamps a slow IC tag.
A3 asks whether the local box can also **hear** a controlled exterior signal on
the same port — like a transmission line that both absorbs outgoing waves and
can carry an incoming generator at the far end — without building the far-end
mesh. If the interior energy rises only when the drive sits on the shell, and
an interior fake pump is caught as sabotage, the bidirectional stub is working.
