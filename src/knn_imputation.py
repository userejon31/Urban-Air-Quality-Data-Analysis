from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler


from src.plot_style import AQUA_PRIMARY, GRAY_BORDER


def select_numerical_columns(df: pd.DataFrame) -> list:
    """Select numeric columns suitable for KNNImputer (Section 3a)."""
    return df.select_dtypes(include=[np.number]).columns.tolist()


def knn_impute(df: pd.DataFrame, columns: list, n_neighbors: int) -> pd.DataFrame:
    """
    Section 3b:
    1. Scale numerical columns if units differ strongly.
    2. Fit KNNImputer with n_neighbors=k.
    3. Return imputed DataFrame.
    """
    result = df.copy()
    if not columns:
        return result

    scaler = StandardScaler()
    imputer = KNNImputer(n_neighbors=n_neighbors)

    scaled = scaler.fit_transform(result[columns])
    imputed_scaled = imputer.fit_transform(scaled)
    imputed = scaler.inverse_transform(imputed_scaled)

    result[columns] = imputed
    return result


def compare_distributions(
    original: pd.DataFrame,
    imputed_dict: dict,
    columns: list,
    save_dir,
) -> pd.DataFrame:
    """
    For at least three variables, plot before/after and compare summary statistics.
    """
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)

    stats_rows = []
    comparisons = {"original": original, **imputed_dict}

    for column in columns:
        fig, axes = plt.subplots(1, len(comparisons), figsize=(5 * len(comparisons), 4), sharey=True)
        if len(comparisons) == 1:
            axes = [axes]
        for axis, (label, frame) in zip(axes, comparisons.items()):
            series = frame[column].dropna()
            axis.hist(
                series,
                bins=25,
                alpha=0.75,
                color=AQUA_PRIMARY,
                edgecolor=GRAY_BORDER,
            )
            axis.set_title(f"{column} - {label}")
            axis.set_xlabel(column)
            axis.set_ylabel("Count")
            stats_rows.append(
                {
                    "variable": column,
                    "dataset": label,
                    "mean": series.mean(),
                    "median": series.median(),
                    "std": series.std(),
                    "min": series.min(),
                    "max": series.max(),
                    "iqr": series.quantile(0.75) - series.quantile(0.25),
                }
            )
        fig.tight_layout()
        fig.savefig(save_path / f"distribution_{column.replace('/', '_')}.png", dpi=150, bbox_inches="tight")
        plt.close(fig)

    return pd.DataFrame(stats_rows)
