# Audit Results: Global Files & Volume 0 (IP Migration Plan)

## Scope Covered
- `manuscript/frontmatter/*`
- `manuscript/backmatter/*`
- `manuscript/common/*`
- `manuscript/vol_0_engineering_compendium/*`

## Tier 1: Hygiene & Mechanical Checks
**Status: Pass**
- All file inclusions and LaTeX dependencies are structurally sound.

## Tier 2: Mathematical Rigor & "Sci-Fi" Scrub

### 🚨 Hardware IP Identified for Migration 🚨

Instead of modifying the files in-place, this audit identifies the exact pieces of underdeveloped "sci-fi" / hardware thrust terminology and schemas that need to be structurally partitioned and migrated to the private `Hardware-Repo` / `ave-veritas-et-enodatio`.

#### 1. `manuscript/common/appendix_experiments.tex`
The following experiment descriptions contain explicit sci-fi terminology ("thrust wake", "pumped GRIN nozzle", "thrusters", "horizontal metric rectification") and must be ported to the hardware testing repository:

```latex
\item \textbf{Project TORSION-05 (Horizontal Metric Rectification):} \textit{Chapter 11: Experimental Falsification}. Isolates direct bulk translation coupling using a vacuum-suspended torsion balance.
\item \textbf{Project PONDER-01 (Stereo Phased Array Parallax):} \textit{Chapter 2 \& 11}. Tracks the time-resolved mechanical thrust wake across an asymmetric capacitive $35\,\text{kV}$ phased array.
\item \textbf{Project PONDER-02 (Bistatic Plume Diagnostics):} \textit{Chapter 6: Vacuum Torsion Metrology}. Measures microwave reflection phase-shifts scattering off the purely physical local $G_{vac}$ distortion of a pumped GRIN nozzle.
\item \textbf{Project PONDER-05 (Differential Saturation Parallax):} \textit{Chapter 5: DC-Biased Quartz}. Employs paired quartz-resonator thrusters across a vertical gravity gradient to map the exact Axiom 4 saturation differential.
```
*Recommendation:* Port these entries to a formal Hardware Taxonomy document in the private repo. For the public repo, leave out these entries or replace them with safe, solid-state electrical equivalents (e.g. `Asymmetric Varactor Rectification`).

#### 2. `manuscript/backmatter/04_physics_engine_architecture.tex`
Exposed APU Hardware architectures. Lines 261-267 contain explicit lists of private hardware solver paths (`geometric_diode.py`, `soliton_memory.py`, `continuous_fpga.py`, etc). 

*Recommendation:* Migrate the descriptions of these proprietary API models to the private repository's API docs.

#### 3. `manuscript/backmatter/06_spice_verification_manual.tex`
Lines 195+ and 256+: Exposes specific hardware topologies: 
`an asymmetric LTspice netlist using the Helium-4 emitter topology. The nonlinear varactor produces a DC offset... demonstrating ponderomotive rectification.`

*Recommendation:* Extract the "Helium-4 emitter topology" logic and PONDER-01 rectification netlist documentation to the private hardware repository.

#### 4. `manuscript/vol_0_engineering_compendium/chapters/02_analytical_summaries.tex` (Line 44) & `manuscript/backmatter/01_appendices.tex` (Line 89)
`\item \textbf{Non-Linear FDTD Acoustic Steepening PDE:} ... (Derived structurally for topological thrust metrics)`

*Recommendation:* Remove the "thrust metric" claim. Maintain mathematical equations but port the "thrust" application logic to the hardware repo.
