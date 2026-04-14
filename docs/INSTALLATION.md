# Installation

See the project [README](../README.md) for complete installation instructions.

## Quick Start

```bash
# Clone
git clone https://github.com/ave-veritas-et-enodatio/AVE-Core.git
cd AVE-Core

# Bootstrap (installs uv, creates .venv, installs dependencies)
make setup

# Verify
make verify    # 354-file anti-cheat scan
make test      # 746 unit tests
make pdf       # Compile all 7 manuscript volumes
```

## Requirements

- macOS or Linux
- [uv](https://github.com/astral-sh/uv) Python dependency manager
- LaTeX distribution (for manuscript compilation)