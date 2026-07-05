from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.outliers import tukey_bounds


def treat_outliers(
    df: pd.DataFrame, columns: list, method: str = "clip_tukey"
) -> pd.DataFrame:
    """
    Section 5a: Apply one strategy with justification:
    - winsorization / Tukey clipping: x* = min(max(x, L), U)
    - or keep extremes if they are plausible pollution events
    """
    result = df.copy()
    if method == "keep":
        return result

    if method not in {"clip_tukey", "winsorize"}:
        raise ValueError("method must be 'clip_tukey', 'winsorize', or 'keep'")

    for column in columns:
        lower, upper = tukey_bounds(result[column].dropna())
        result[column] = result[column].clip(lower=lower, upper=upper)
    return result


def build_comparison_table(
    before: pd.DataFrame, after: pd.DataFrame, metadata: dict | None = None
) -> pd.DataFrame:
    """
    Section 5c: Fill the activity comparison table with:
    rows, columns, total missing, columns removed,
    mean/median imputed vars, KNN imputed vars, outlier-treated vars.
    """
    metadata = metadata or {}
    columns_removed = metadata.get("columns_removed", [])
    mean_median_imputed = metadata.get("mean_median_imputed", [])
    knn_imputed = metadata.get("knn_imputed", [])
    outlier_treated = metadata.get("outlier_treated", [])

    def _format_items(items: list) -> str:
        return ", ".join(items) if items else "None"

    return pd.DataFrame(
        [
            {
                "Element": "Number of rows",
                "Before Cleaning": before.shape[0],
                "After Cleaning": after.shape[0],
            },
            {
                "Element": "Number of columns",
                "Before Cleaning": before.shape[1],
                "After Cleaning": after.shape[1],
            },
            {
                "Element": "Total missing values",
                "Before Cleaning": int(before.isna().sum().sum()),
                "After Cleaning": int(after.isna().sum().sum()),
            },
            {
                "Element": "Columns removed",
                "Before Cleaning": "None",
                "After Cleaning": _format_items(columns_removed),
            },
            {
                "Element": "Variables imputed with mean or median",
                "Before Cleaning": "None",
                "After Cleaning": _format_items(mean_median_imputed),
            },
            {
                "Element": "Variables imputed with KNNImputer",
                "Before Cleaning": "None",
                "After Cleaning": _format_items(knn_imputed),
            },
            {
                "Element": "Variables treated for outliers",
                "Before Cleaning": "None",
                "After Cleaning": _format_items(outlier_treated),
            },
        ]
    )


def export_clean_dataset(df: pd.DataFrame, path) -> None:
    """Save the cleaned dataset as air_quality_clean.csv (Section 5d)."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
