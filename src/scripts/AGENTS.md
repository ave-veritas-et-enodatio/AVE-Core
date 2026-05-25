# Agent Guide for AVE Scripts

## Documentation Canonicality (KB leaves > LaTeX)

As of **2026-05-07**, the KB markdown tree (`manuscript/ave-kb/`) is the **sole canonical source** for AVE results, derivations, and prose. The LaTeX manuscript (`manuscript/vol_*/`) is a **derived publication artifact** that mirrors KB state, not its inverse.

For script work, the practical implications:

- When a script produces a new or revised result that warrants documentation, the documentation goes in the **KB leaf first** — with frontmatter `claims:`, Tier 2 inline markers, and subtree-claims aggregation per INVARIANT-S5/S8 in `manuscript/ave-kb/CLAUDE.md`. Sync to LaTeX as a downstream step.
- When LaTeX and KB disagree about a result, the KB is right; treat the LaTeX as stale until synced.
- This inverts the older intake-era framing where LaTeX was canonical and the KB was a projection.

## Running Scripts

Individual scripts are run from the repository root with Python:

```bash
python src/scripts/vol_1_foundations/simulate_double_slit_observer.py
```

The `src/` directory must be on PYTHONPATH for `from ave.*` imports to resolve. Most scripts handle this via `sys.path` manipulation or rely on the project being installed in development mode. From the repo root:

```bash
PYTHONPATH=src python src/scripts/vol_2_subatomic/simulate_electroweak_unification.py
```

Some scripts require JAX. If JAX is not installed, scripts that use the JAX fallback pattern will degrade to NumPy. Scripts that import JAX directly (without fallback) will fail if JAX is absent.

Scripts in `vol_6_periodic_table/` that import from `periodic_table.simulations.*` require that `src/scripts/vol_6_periodic_table` is on PYTHONPATH (they use the package name `periodic_table`, not the full path).

## Relationship to `src/ave/`

The `src/ave/` library is the physics engine. It defines:

- **Constants** (`ave.core.constants`): All physical constants used by the model — calibration inputs (M_E, ALPHA, G), SI electromagnetic constants (C_0, MU_0, EPSILON_0, Z_0, HBAR, e_charge, K_B), and hundreds of derived quantities.
- **Operators** (`ave.core.universal_operators`): Universal saturation, impedance, and reflection functions.
- **Solvers** (`ave.solvers.*`): FDTD, eigenvalue, coupled resonator, transmission line solvers.
- **Topological modules** (`ave.topological.*`): Borromean links, Faddeev-Skyrme, Cosserat, soliton bond solvers.
- **Domain modules**: Gravity, plasma, regime-specific physics.

Scripts are consumers of this library. They import constants and functions from `ave` and use them to produce derivations, simulations, and figures for the manuscript.

## The Zero-Free-Parameters Constraint

This model derives ALL physical constants from three calibration inputs (electron mass M_E, fine-structure constant ALPHA, gravitational constant G) plus SI definitions. What the Standard Model treats as independent empirical constants (particle masses, coupling constants, mixing angles) are derived outputs of the model.

**For script code, this means:**

1. Physical constants must be imported from `ave.core.constants`, not hard-coded. The constants module is the single source of truth.

2. No external constant libraries (`scipy.constants`, `astropy.constants`, etc.) may be used to obtain physical constants. These would introduce Standard Model values that bypass the derivation chain.

3. When a script computes a derived quantity (e.g., W boson mass), it must build it from the AVE constants, not look up the PDG value and use it as an input.

4. Experimental/PDG values may appear in scripts ONLY as comparison targets — the "expected" column in a prediction table. They must not feed back into any computation.

5. Hard-coding a value like `m_e = 0.51099895` (MeV) is a violation when that value is used as a computational input. It should be computed from the constants: `M_E * C_0**2 / e_charge * 1e-6`.

## Common Patterns for New Scripts

### Standard file header

```python
#!/usr/bin/env python3
"""
Title of Script
================
Description of what this script derives/simulates/plots.

Usage:
    python src/scripts/vol_N_name/script_name.py
"""
```

### Importing constants

```python
from ave.core.constants import C_0, ALPHA, M_E, HBAR, e_charge, Z_0
```

Import only what you need. The constants module exports individual names, not a namespace.

### Output location

Scripts save figures and data to `assets/sim_outputs/` at the repository root:

```python
import os
from pathlib import Path

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").is_dir())
OUT_DIR = PROJECT_ROOT / "assets" / "sim_outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
```

### Dark background plotting

```python
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
```

### JAX with fallback

```python
try:
    from ave.core.fdtd_3d_jax import FDTD3DEngineJAX as FDTD3DEngine
except ImportError:
    from ave.core.fdtd_3d import FDTD3DEngine
```

### Script entry point

```python
def main():
    # ... script body ...

if __name__ == "__main__":
    main()
```

## Output Conventions

- **Plots/figures**: PNG files saved to `assets/sim_outputs/` at the repo root.
- **Animations**: GIF files saved to `assets/sim_outputs/`.
- **SPICE netlists**: Saved to `assets/sim_outputs/spice_models/`.
- **STL meshes**: Saved to `assets/sim_outputs/`.
- **Console output**: Most scripts print detailed derivation chains and comparison tables to stdout.
- **No data persistence between scripts**: Each script is independent. They do not read output files from other scripts (with rare exceptions in vol_3 and vol_6).

## Non-Obvious Conventions

### Empirical masses as comparison targets

Scripts like `master_predictions.py` define empirical values (e.g., `mp_exp = 938.272 # MeV`) as comparison targets. These are PDG experimental values used ONLY for computing percentage deviation. They do not enter any derivation.

### The `periodic_table` import namespace

Scripts that import from `periodic_table.simulations.*` expect that the vol_6 directory is importable as `periodic_table`. This is a legacy naming convention — the directory is actually `vol_6_periodic_table/`.

### Notebook-append scripts in vol_7

The `append_*.py` scripts in vol_7 are notebook cell generators — they programmatically add cells to a Jupyter notebook file at a hardcoded absolute path. They are not standalone physics scripts.

### Natural units vs SI

Some scripts work in "natural units" where the lattice pitch, electron mass, and speed of light are all set to 1. Conversion back to SI is done at the end for human-readable output. The constants module provides `NATIVE_TO_SI_*` conversion factors for this purpose.

### The `verify_universe.py` script

`vol_1_foundations/verify_universe.py` is an AST scanner that checks the `src/ave/` library for smuggled Standard Model constants. It scans for banned imports and magic numbers. It does not check the scripts themselves.
