from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "AirQualityUCI.csv"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "air_quality_clean.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

MISSING_SENTINEL = -200

# TODO: Define your missingness threshold (e.g., 0.40 means 40%).
MISSINGNESS_THRESHOLD = 0.40

# TODO: Choose at least two k values for KNNImputer.
KNN_K_VALUES = [3, 5]

# TODO: Z-score threshold (common default: 3).
ZSCORE_THRESHOLD = 3.0
