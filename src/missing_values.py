import numpy as np
import pandas as pd


def replace_sentinel_with_nan(
    df: pd.DataFrame, sentinel: float = -200
) -> pd.DataFrame:
    """Replace sentinel values with np.nan (Section 2a)."""
    return df.replace(sentinel, np.nan)


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    For each column, compute count and percentage of missing values.

    Formula: Missing % = (missing_count / total_rows) * 100
    """
    total_rows = len(df)
    missing_count = df.isna().sum()
    summary = pd.DataFrame(
        {
            "missing_count": missing_count,
            "missing_pct": (missing_count / total_rows) * 100 if total_rows else 0,
        }
    )
    summary.index.name = "column"
    return summary.reset_index()


def decide_column_action(missing_pct: float, threshold: float) -> str:
    """
    Return 'keep', 'remove', or 'impute' based on your threshold.

    Guiding question: What threshold did you use for excessive missingness?
    """
    if missing_pct <= 0:
        return "keep"
    if missing_pct >= threshold * 100:
        return "remove"
    return "impute"


def impute_basic(
    df: pd.DataFrame, columns: list, strategy: str = "median"
) -> pd.DataFrame:
    """
    Apply mean or median imputation to selected columns only (Section 2d).

    Guiding question: When is median preferable to mean?
    """
    result = df.copy()
    for column in columns:
        if column not in result.columns:
            continue
        if not pd.api.types.is_numeric_dtype(result[column]):
            continue
        if strategy == "mean":
            fill_value = result[column].mean()
        elif strategy == "median":
            fill_value = result[column].median()
        else:
            raise ValueError("strategy must be 'mean' or 'median'")
        result[column] = result[column].fillna(fill_value)
    return result
