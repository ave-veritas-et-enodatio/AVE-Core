# G1 Ontology Walk Packet — what IS the imposed (2,3)? (Static-Existence Epic, 2026-08-24)

**For Grant, in chat.** Input to the epic's G1 gate
(`_orchestration/2026-08-24_static-existence-epic.md` §4: *"A wrong noun
here wastes the whole arc"*). Candidates are **ranked by receipt strength
only — no winner is recommended; the choice is this walk's.** Companion
inventory with full receipts: `capability-report.md` (same directory;
worktree HEAD `a2551384`). Provenance caveat: the P0 pull-lane outputs
never reached the synthesis (interpolation failure, logged in the
report); this packet is built from a direct corpus/engine re-read.

**The question in one line:** the named test says *"Impose the `(2,3)`
winding as a **boundary condition**, relax the lattice, and ask whether
the relaxed core **rails `S → 0` at the center`"*
(`saturation-rim-inversion.md:55`). Canon says the (2,3) is a
**phase-space** object (a Clifford-torus winding of the bond-pair tank's
phasors — real-space body = 0₁ unknot), and canon **measured this year
that no map carries phase-space interior structure into real space —
only the edges project (M and Q)**
(`research/2026-08-24_smith-annulus_result.md:421-424`). So: what do we
physically clamp?

---

## Guard reminders that bear on this choice (from epic §5 — each governs the walk)

- **Existence-not-emergence (guard 1).** Imposing the finished texture is
  legitimate ONLY because the claim is existence ("does a self-consistent
  railed state EXIST under this constraint"), never hosting/forming. No
  candidate below is a genesis route; any language drift to "the engine
  builds/holds/forms it" is out of bounds in the prereg and in this walk.
- **The transduction hazard (guard 3).** The (2,3) lives in phase space;
  a naive real-space imposition is the exact conflation A46 and the
  register's ambiguity flag police. This is not hypothetical: the tree's
  own `cosserat_field_3d` (2,3)-seeder disavows itself — *"writes a (2,3)
  torus-knot ansatz onto Cosserat ω … NOT the canonical electron"*
  (`cosserat_field_3d.py:1042-1046`) — and #415's real-space solve bled
  the winding. Every candidate is graded against this hazard below.
- **The structural-null trap (guard 4).** The longitudinal receipt: a
  per-node-uniform load cancels identically at the shunt junction
  (`vacuum_varactor_scatter.py:52-57`). The transverse analogs P0
  identified: (i) only GRADIENTS of ω enter the Cosserat energy — a
  common-mode component of an imposed texture relaxes invisibly; (ii) a
  uniform frame change is physically inert (frame-invariance walk §2) —
  an imposition whose content is common-mode tests nothing. **A null from
  a common-mode imposition is an artifact, not a DISPROVE.**
- **α-agnostic imposition (guard 8)** — bears directly on candidate
  choice: *"imposing a specific α imposes MORE than the winding"*
  (frame-invariance RECORD §5). Every concrete texture below picks a
  representative; the imposition must be the class or the swept family.
- **Sector ownership A1 ⊥ T2 (guard 5)** — the winding is Cosserat/T2;
  the S-railing readout is A1-adjacent bookkeeping. Whatever is clamped,
  the VERDICT observable (S at the center) is in the other sector — the
  prereg must keep the wiring explicit, never "the defect is the mass."

---

## The candidates, ranked by receipt strength

### Candidate 1 — Clamp the port-phase quadrature at the walls of the room (K4 phase-space voltage ansatz, held)

**The physical picture.** Walk into the lattice as its plumber: every
bond is an LC tank, every node a 4-port junction. You do not bend any
pipe into a trefoil. Instead you go to the **generator panel** — the
ports on the boundary of the region — and you **solder a fixed phase
relationship into the drive-less terminations**: port phases locked to
θ = 2φ + 3ψ quadrature (cos on ports 0,1; sin on ports 2,3), with the
per-port chirality weights, exactly the pattern
`initialize_2_3_voltage_ansatz` already encodes
(`tlm_electron_soliton_eigenmode.py:48-91`). Then you let the interior
plumbing settle however it wants and read the S-meter at the center. In
circuit language: **a phase-locked polyphase termination on the boundary
ports; the interior network is untouched and undriven.**

**Receipt strength: STRONGEST COMBINED.** The primitive exists in-tree
and is the only imposer explicitly fenced the canonical way
(def-kn0t01 SOLID, `:57-67`: the real-space body it builds is the 0₁
hedgehog shell; the (2,3) enters ONLY as phase — "the diagnostic shadow
of that phase winding, not a body curve"). Three precedent consumers ran
it (`coupled_engine_eigenmode.py:148` among them). It matches the
INVARIANT-N1 two-spaces canon exactly.

**Silent assumptions (each a prereg obligation if chosen):**
- It is today a **seeder, not a hold** — the clamp-during-relax mechanism
  is EXTENSION-NEEDED #1. Held-on-∂Ω vs held-everywhere are different
  tests.
- It writes **V_inc only**; the Clifford-torus object is the
  (V_inc, V_ref) pair (EXTENSION-NEEDED #2). Clamping half the pair may
  under-determine the class.
- It picks a specific tube phase and a specific metric (R, r) — guard 8
  demands the family sweep; the π₁ class is radius-blind, the ansatz is
  not.
- Phase-only vs phase+amplitude clamp is unspecified — clamping amplitude
  anywhere near the rail would smuggle the conclusion in (the S→0 verdict
  must be free to fail).

### Candidate 2 — Impose an ω-texture and let the springs settle (Cosserat real-space impose-and-relax)

**The physical picture.** The lattice's micro-rotation field is a room
full of gimballed flywheels coupled by torsion springs. You reach in and
**set every flywheel's axis by hand** to the (2,3) texture (or the 0₁
unknot texture), release, and watch the spring network settle under its
own (optionally saturating) stiffness — gradient descent on the Cosserat
energy, unwinding visible step by step (`relax_to_ground_state`,
`track_topology_every`). In circuit language: **pre-charge a specific
flux pattern into every inductor of the rotational sector, open all
sources, let the reactive network find its own operating point.**

**Receipt strength: STRONGEST MACHINERY, WEAKEST ONTOLOGY.** The only
end-to-end impose→relax→S-readout pipeline in the tree
(`cosserat_field_3d.py`: seeders `:1023/:1167`, saturated energy `:731`,
relaxers `:1550/:1686`, Op3 reactive wall-clamp `:977-1014`). But its own
docstring disavows the (2,3) mode as not-the-canonical-electron
(transduction hazard, verbatim in the guards above), and its canonical
0₁ mode carries *"NO (p,q) winding"* (`:1256`) — so as built it relaxes
either the wrong object or an unwound one. And nothing holds the texture:
this is exactly the configuration in which #415-class bleed-off is the
expected failure mode, and its relaxer is gradient descent — a
substrate-native-check-flagged default (walk Q2).

### Candidate 3 — Clamp only the topological class on the room's boundary (boundary-Link imposition)

**The physical picture.** Canon defines charge as
`Q = Link(∂Ω, F) ∈ ℤ` (`boundary-observables-m-q-j.md`) and the #416
ruling calls it the STATIC imposed Link. Take that literally: on the
**outer boundary of the simulation box** (not on any presumed core wall
— choosing a core wall would presuppose the object under test), fix the
boundary data so that the linking integer of the boundary with the
substrate field is (2,3)-class, and leave the ENTIRE interior free. In
circuit language: **a topological bias on the room's door frames — like
forcing one unit of trapped flux through a superconducting ring: you
don't specify any interior current pattern, you fix a winding integer the
interior must reconcile.** α-agnostic BY CONSTRUCTION — a class clamp,
not a representative clamp — which is exactly what guard 8 asks for.

**Receipt strength: STRONGEST ONTOLOGY, ZERO CLAMP MACHINERY.** The
definition receipts are the strongest in canon (charge's own canonical
definition; the static-Link ruling; the-abandoned-interior `:113`). But
the tree has only READERS of Link/holonomy (`charge_quantization.py`,
`k4_lattice_holonomy.py`, `boundary_invariants.py`) — a constraint
version is a pure extension. And the class does not uniquely determine
boundary data: any concrete run still picks a representative texture on
∂Ω, so the guard-8 family sweep reappears as an operational protocol
(sweep representatives, gate on class-invariance of the verdict).

### Candidate 4 — Re-pose the eigensolve with the winding held, not seeded (constrained #415)

**The physical picture.** The #415 machine already asks the
stationary-state question on the native connect-map (Hermitian H, the
stencil IS the connect-map — `fork_b_saturation_tank.py:169`). #415 let
the winding template float and it bled off. The re-pose: **solve the
eigenproblem in the constrained subspace where the winding class is
held** — in circuit language, find the network's natural resonance
subject to a hard phase-winding constraint on the tank phasors, the way
one solves a cavity mode with a fixed flux quantum threaded.

**Receipt strength: MACHINERY EXISTS, SITS CLOSEST TO A CANONICAL
NEGATIVE.** The distinctness argument must be made config-level in the
prereg (guard 2): #415 was an UNCONSTRAINED solve of a seeded template;
the named test is a HELD boundary condition — a different operator
problem. #417's re-scope (*"tested the WRONG LOCUS three ways"*,
`phase_space_winding.py:9-13`) cuts both ways: it licenses a re-pose at
a different locus AND warns that this candidate's real-space,
V_snap-adjacent, static locus was the criticized one.

**Anti-candidate, fenced:** imposing the S-profile itself
(`fork_b_saturation_tank.saturated_core_strain_native:120`) is imposing
the conclusion — legitimate as P1 probe plumbing only, never as the P2
imposition.

---

## The walk questions (only Grant can answer these)

**Q1 — Where does the clamp physically attach, and how much does it
say?** The named test says "boundary condition"; the candidates realize
that at three different strengths. Sitting inside the cell as the
plumber: are we
- clamping **phase relationships on the boundary ports only** — the
  polyphase termination at the walls of the room, interior fully free
  (Candidate 1 held-on-∂Ω, or Candidate 3 as its class-level version);
- clamping a **texture through the whole interior** and letting
  amplitudes settle around it (Candidate 1 held-everywhere /
  Candidate 2) — stronger grip, but more imposed than the winding
  (guard 8 pressure, and the transduction hazard bites hardest here);
- or clamping **only the integer** — no representative at all, the
  trapped-flux-quantum picture (Candidate 3 proper, the most honest to
  "charge = static imposed Link" and the most machinery to build?
And within whichever: phase-only, or phase+amplitude? My inventory note:
clamping any amplitude near the rail begs the S→0 verdict — the
plumber's instinct wanted here is whether a phase-only clamp can grip the
lattice at all.

**Q2 — What does "relax the lattice" mean on a lossless reactive
substrate?** The only in-tree relaxer is gradient descent on the energy
functional — a flagged SM-default (energy-basin thinking), while true
dissipation is un-native under Ax3. The stationary state can be reached
as
- an **eigensolve** (find the fixed point directly — but then #417's
  recorded objection, next question, is live);
- **damped native time-evolution**, loss declared as a numerical device
  only;
- **unitary evolution + time-average** (never relax at all; ask whether
  the imposed-BC dynamics KEEPS a railed center on average — the
  liveness twin);
- or **energy-gradient flow accepted openly as a device**, with the
  unwinding trajectory as diagnostic (what the tree does today).
The meaning of a DISPROVE changes with this choice — a sub-railed result
from gradient flow says "the energy landscape doesn't rail," which is not
obviously the same claim as "no stationary railed state exists."

**Q3 — Which sector physically receives the imposition?** The winding is
Cosserat/T2 (guard 5), but the strongest phase-space-honoring primitive
clamps the **K4 V-tank phasors** (Candidate 1), the strongest machinery
clamps **Cosserat ω rotors** (Candidate 2), and the class route clamps
**boundary holonomy/Link** (Candidate 3). In circuit terms: do we solder
the phase pattern into the electrical tanks, preset the mechanical
flywheels, or thread the flux quantum through the frame? The cross-wiring
watch lives exactly at this junction — and the readout (S railing) sits
in the A1-adjacent bookkeeping either way, so the imposition sector and
the verdict sector will differ in every candidate. Is that separation
physical to you, or a smell?

**Q4 — Can a time-independent texture carry the (2,3) at all?** Two
canon receipts pull against each other here. #417's own prereg header:
*"A (2,3) winding is a closed TIME-ORBIT θ(t)=2φ(t)+3ψ(t); a fixed-point
eigenstate has no orbit and cannot host it"*
(`phase_space_winding.py:11-13`). The #416 ruling and
the-abandoned-interior `:113`: the winding *"is a static Clifford-torus /
Link texture"* that never dynamically closes — and the frame-invariance
walk (§2) reads the orbit as the *presentation* under differential
detuning, the static Link as the invariant. For THIS test, which reading
governs the imposed object:
- the **static-texture** reading — a time-independent clamp carries the
  class, the named test runs as written;
- the **orbit** reading — a static run freezes out the carrier and the
  imposition needs a rotating-frame / envelope formulation to even
  contain a (2,3);
- or **both, carved by sector** — the class is static (impose it), the
  orbit is the carrier's presentation (do not impose it, and treat any
  carrier structure in the relaxed state as a RESULT)?
This is the single sharpest fork the imposition map turns on — it is the
"what the imposed thing IS" question in its purest form.

---

*Nothing in this packet asserts a route. Per the epic's open-goal
framing, PROVE and DISPROVE stand symmetric; whichever route the walk
picks, the P2 prereg discharges all eight §5 guards by name, and the
substrate — not this packet, not the walk — adjudicates the physics.*
