# Feature: Universal SPICE Library

**Branch:** `feature/universal_spice_library`  
**Base:** `main` @ `ae43875`  
**Status:** Complete — ready for PR

## Objective

Build the canonical AVE-SPICE integration: one universal vacuum cell behavioral model (`ave_vacuum_cell.lib`), one Python netlist compiler, and a backmatter appendix formalizing the SPICE verification path.

## Scope

### Phase 1: Engine (`.lib` + compiler)
- `src/ave/hardware/spice_models/ave_vacuum_cell.lib` — universal ngspice subcircuit
- `src/ave/solvers/spice_netlist_compiler.py` — topology → .cir compiler
- Refactor `src/ave/condensed/spice_exporter.py` to use universal cell

### Phase 2: Verification
- `src/tests/test_spice_vacuum_cell.py` — DC sweep, AC resonance, glycine FTIR
- `src/tests/test_netlist_compiler.py` — unit tests for string generation

### Phase 3: Manuscript
- `manuscript/backmatter/06_spice_verification_manual.tex` — new appendix
- Update `manuscript/backmatter/04_physics_engine_architecture.tex`

### Phase 4: Cleanup
- Deprecate dead code in `spice_transient.py`
- Fix stale import in `simulate_protein_spice_transmission_line.py`

## Dependencies
- ngspice (external, CI-optional)
- Existing: `ave.axioms.saturation`, `ave.core.constants`, `spice_organic_mapper.py`

## Key Design Decisions
1. **Appendix, not volume**: SPICE verification is a methodology appendix (App 6), not new physics
2. **ngspice-first**: Target ngspice syntax; document LTspice/Xyce compatibility notes
3. **One cell**: All domain-specific exporters become wiring topologies of `AVE_VACUUM_CELL`
