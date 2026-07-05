# Urban Air Quality Data Analysis

Data cleaning project using the [UCI Air Quality dataset](https://archive.ics.uci.edu/dataset/360/air%2Bquality).

## Objective

Prepare a real-world air quality dataset through structured cleaning: missing values, imputation comparison (basic vs KNN), outlier detection, and final export.

## Setup

On Ubuntu/Debian, system Python is **externally managed** — you cannot run `pip install` globally. Use the project virtual environment instead.

> **Already set up?** The `.venv` folder and kernel should exist. Reload Cursor and select kernel **Python (urban-air-quality)** in your notebook.

### First-time setup (terminal)

```bash
cd Urban-Air-Quality-Data-Analysis
bash scripts/setup.sh
```

Or manually:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name=urban-air-quality --display-name="Python (urban-air-quality)"
```

### Use pip in the terminal

Never use bare `pip` or `pip3` — they target system Python and will fail. Always use:

```bash
.venv/bin/pip install <package>
.venv/bin/pip list
```

If Cursor opens a terminal with `(.venv)` in the prompt, plain `pip` works there too (the venv is active).

### Cursor / VS Code (notebooks)

1. **Reload the window:** `Ctrl+Shift+P` → `Developer: Reload Window`
2. Open `notebooks/01_dataset_loading.ipynb`
3. Top-right kernel selector → **Python (urban-air-quality)**
4. If missing: **Select Another Kernel** → **Python Environments** → `.venv/bin/python`

Project settings in `.vscode/settings.json` point Cursor to `.venv` automatically.

### Run Jupyter in the browser

```bash
.venv/bin/jupyter lab
```

## Project Layout

| Path | Description |
|------|-------------|
| `notebooks/01–05` | One notebook per activity section |
| `src/` | Reusable Python functions (implement the TODOs) |
| `data/raw/` | Raw dataset files |
| `data/processed/` | Cleaned output (`air_quality_clean.csv`) |
| `reports/figures/` | Saved plots for your write-up |
| `skills/context.md` | Full activity specification |

## Workflow

1. **Section 1** — Load and diagnose the dataset
2. **Section 2** — Replace `-200` with NaN and apply basic imputation
3. **Section 3** — KNN imputation and distribution comparison
4. **Section 4** — Outlier detection (Tukey vs Z-score)
5. **Section 5** — Outlier treatment and export cleaned CSV

## Constraints

- No machine learning models
- Every cleaning decision must include visual or statistical evidence
- Do not remove rows/columns or impute without justification

## Submission Checklist

- [ ] All notebook cells executed
- [ ] Guiding questions answered in markdown
- [ ] `data/processed/air_quality_clean.csv` generated
- [ ] Comparison table completed (Section 5)
