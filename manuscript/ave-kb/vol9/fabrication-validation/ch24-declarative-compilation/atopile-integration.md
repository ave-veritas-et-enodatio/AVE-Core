[↑ Ch.24: Declarative Compilation](./index.md)
<!-- leaf: verbatim -->

# atopile Integration: Physics-to-BOM Pipeline

The integration of a declarative hardware compiler fundamentally bridges abstract physics with standard industrial manufacturing. By projecting nonlinear continuum mathematics directly onto parametrized declarative modules, the atopile framework enables:

1. **Constraint Propagation:** Axiom-derived impedance constraints ($Z_0$, taper profiles, cavity lengths) flow from the FDTD validation engine directly into `.ato` module parameters.
2. **Part Selection:** The compiler queries real component databases (JLCPCB) to match the parametric constraints against available surface-mount components, automatically selecting the nearest valid part.
3. **Layout Generation:** The parametrized modules compile to KiCad-compatible PCB layouts with AVE-verified trace geometries, including Klopfenstein tapers and corrugated delay lines.

This pipeline eliminates manual translation errors between the physics validation stage and the manufacturing stage. Every constraint in the final BOM is traceable back to a specific axiom-derived equation.

> **[Resultbox]** *Chapter 24 Summary*
>
> The integration of a declarative hardware compiler fundamentally bridges abstract physics with standard industrial manufacturing. By projecting nonlinear continuum mathematics directly onto parametrized declarative modules, the APU design pipeline from axioms to physical bill of materials is fully automated.
