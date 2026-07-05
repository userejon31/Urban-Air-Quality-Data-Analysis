import numpy as np
import pandas as pd


def tukey_bounds(series: pd.Series) -> tuple[float, float]:
    """
    Compute Q1, Q3, IQR, lower and upper bounds (Section 4b).

    Lower = Q1 - 1.5 * IQR
    Upper = Q3 + 1.5 * IQR
    """
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return lower, upper


def detect_tukey_outliers(series: pd.Series) -> pd.Series:
    """Boolean mask for Tukey outliers (Section 4b)."""
    lower, upper = tukey_bounds(series)
    return (series < lower) | (series > upper)


def detect_zscore_outliers(
    series: pd.Series, threshold: float = 3.0
) -> pd.Series:
    """Boolean mask where |Z| > threshold (Section 4c)."""
    std = series.std()
    if pd.isna(std) or std == 0:
        return pd.Series(False, index=series.index)
    zscores = (series - series.mean()) / std
    return zscores.abs() > threshold


def outlier_report(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Table with count and percentage of outliers per variable per method.

    Suggested columns: CO(GT), C6H6(GT), NOx(GT), NO2(GT), T, RH, AH
    """
    rows = []
    total_rows = len(df)
    for column in columns:
        tukey_mask = detect_tukey_outliers(df[column])
        zscore_mask = detect_zscore_outliers(df[column])
        rows.append(
            {
                "variable": column,
                "tukey_count": int(tukey_mask.sum()),
                "tukey_pct": (tukey_mask.sum() / total_rows) * 100 if total_rows else 0,
                "zscore_count": int(zscore_mask.sum()),
                "zscore_pct": (zscore_mask.sum() / total_rows) * 100 if total_rows else 0,
            }
        )
    return pd.DataFrame(rows)
