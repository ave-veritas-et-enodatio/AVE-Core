#!/usr/bin/env bash
THIS_DIR=$(dirname "$0")
cd "${THIS_DIR}"
# Setup script for Applied Vacuum Engineering project
# This script sets up the Python environment and installs dependencies

set -e

echo "🚀 Setting up Applied Vacuum Engineering project..."

OS=$(uname -s)
case "${OS}" in
    Linux|Darwin) ;;
    *)
        echo "❌ ${OS} unsupported." 1>&2
        exit 1
        ;;
esac

# version tag in ave-veritas-et-enodatio/agents repo
AGENTS_VERSION=v0.1.0

[[ -f ".claude/agents/.git/HEAD" ]] || {
  # parse git protocol instead of hard-coding ssh or http
  AGENTS_REPO=$(git remote -v | awk '{print $2; exit(0); }')
  AGENTS_REPO=${AGENTS_REPO%/*}/agents.git
	git clone "${AGENTS_REPO}" .claude/agents
	(cd .claude/agents && git checkout ${AGENTS_VERSION})
	(cd .claude && ln -s agents/commands .)
}

# Check if Python 3 is installed
if ! command -v uv &> /dev/null; then
    echo "uv is missing. Please install." 1>&2
    exit 1
fi

uv sync

# Optional: SPICE verification toolchain
# ngspice is required for SPICE-based verification tests (src/tests/test_spice_*)
if command -v ngspice &> /dev/null; then
    echo "✅ ngspice found: $(ngspice --version 2>&1 | head -1)"
else
    echo "⚠️  ngspice not found (optional — needed for SPICE verification tests)"
    echo "   Install with: brew install ngspice  (macOS)"
    echo "                 apt install ngspice    (Debian/Ubuntu)"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Install Jupyter Lab extensions (optional)
echo "🔧 Setting up Jupyter Lab..."
jupyter lab build

# Create Jupyter kernel for this project
echo "🎯 Creating Jupyter kernel..."
python -m ipykernel install --user --name=applied-vacuum-engineering --display-name="Applied Vacuum Engineering"

cat << EOF
✅ Setup complete!

To get started:
1. Activate the virtual environment: source .venv/bin/activate
2. Start Jupyter Lab: jupyter lab
3. Open a notebook from the notebooks/ directory

Happy exploring! 🔬
EOF
