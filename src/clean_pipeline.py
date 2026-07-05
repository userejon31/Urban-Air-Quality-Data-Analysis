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
    rows = [
        {"metric": "rows_before", "value": before.shape[0]},
        {"metric": "rows_after", "value": after.shape[0]},
        {"metric": "columns_before", "value": before.shape[1]},
        {"metric": "columns_after", "value": after.shape[1]},
        {"metric": "missing_before", "value": int(before.isna().sum().sum())},
        {"metric": "missing_after", "value": int(after.isna().sum().sum())},
        {"metric": "columns_removed", "value": ", ".join(metadata.get("columns_removed", []))},
        {"metric": "mean_median_imputed", "value": ", ".join(metadata.get("mean_median_imputed", []))},
        {"metric": "knn_imputed", "value": ", ".join(metadata.get("knn_imputed", []))},
        {"metric": "outlier_treated", "value": ", ".join(metadata.get("outlier_treated", []))},
    ]
    return pd.DataFrame(rows)


def export_clean_dataset(df: pd.DataFrame, path) -> None:
    """Save the cleaned dataset as air_quality_clean.csv (Section 5d)."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
