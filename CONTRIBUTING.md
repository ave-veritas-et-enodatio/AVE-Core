# Contributing to AVE-Core

Thank you for your interest in contributing to Applied Vacuum Engineering.

## The Prime Directive

> **Derive Before You Code.** No physics engine code may be written unless every
> operator, constant, and formula has a complete, traceable derivation chain from
> the four AVE axioms. If it can't be derived, it doesn't go in the engine.

## How to Contribute

### Reporting Issues
- Open an issue with a clear description
- For physics discrepancies, include the prediction, expected value, and derivation chain

### Code Contributions
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes following the coding standards below
4. Run verification: `make verify && make test`
5. Submit a pull request

### Coding Standards
- **All constants** must come from `ave.core.constants` — never hardcode physics values
- **`scipy.constants` is banned** — use `ave.core.constants` exclusively
- **No smuggled data** — never normalize to match experiment or use ad-hoc corrections
- **Every derivation** must be documented in the manuscript before going in the engine
- **Run the kernel check** (`make verify`) — it validates 350 files for parameter smuggling

### Manuscript Contributions
- LaTeX files should follow the established volume structure
- All equations must be derivable from Axioms 1–4
- Include step-by-step derivation chains
- Cross-reference the physics engine module that implements the result

## License

By contributing, you agree that your contributions will be licensed under
the [Apache License 2.0](LICENSE).