#!/usr/bin/env bash
# One-time project setup (Ubuntu/Debian — system pip is blocked; use a venv).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Installing dependencies..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

echo "Registering Jupyter kernel..."
.venv/bin/python -m ipykernel install --user --name=urban-air-quality --display-name="Python (urban-air-quality)"

echo ""
echo "Done. Next steps:"
echo "  1. Reload Cursor (Ctrl+Shift+P -> Developer: Reload Window)"
echo "  2. Open a notebook and select kernel: Python (urban-air-quality)"
echo "  3. In terminal, pip works as: .venv/bin/pip install <package>"
