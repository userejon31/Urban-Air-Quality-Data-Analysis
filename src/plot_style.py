"""Shared aqua and gray palette for tables and plots."""

from __future__ import annotations

import pandas as pd

# Aqua tones
AQUA_PRIMARY = "#4ECDC4"
AQUA_DARK = "#2C7A7B"
AQUA_MID = "#38B2AC"
AQUA_LIGHT = "#B2F5EA"
AQUA_PALE = "#E6FFFA"

# Gray tones
GRAY_DARK = "#4A5568"
GRAY_MID = "#718096"
GRAY_BORDER = "#CBD5E0"
GRAY_ROW_EVEN = "#EDF2F7"
GRAY_ROW_ODD = "#FFFFFF"
GRAY_HEADER_TEXT = "#F7FAFC"

PALETTE = {
    "aqua_primary": AQUA_PRIMARY,
    "aqua_dark": AQUA_DARK,
    "aqua_mid": AQUA_MID,
    "aqua_light": AQUA_LIGHT,
    "gray_dark": GRAY_DARK,
    "gray_mid": GRAY_MID,
    "gray_border": GRAY_BORDER,
    "gray_row_even": GRAY_ROW_EVEN,
    "gray_row_odd": GRAY_ROW_ODD,
}


def apply_plot_style() -> None:
    """Apply the aqua/gray palette to matplotlib defaults."""
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set_theme(
        style="whitegrid",
        palette=[AQUA_PRIMARY, AQUA_MID, GRAY_MID, AQUA_LIGHT, GRAY_DARK],
    )
    plt.rcParams.update(
        {
            "axes.facecolor": GRAY_ROW_ODD,
            "figure.facecolor": GRAY_ROW_ODD,
            "axes.edgecolor": GRAY_BORDER,
            "axes.labelcolor": GRAY_DARK,
            "text.color": GRAY_DARK,
            "xtick.color": GRAY_MID,
            "ytick.color": GRAY_MID,
            "grid.color": GRAY_ROW_EVEN,
            "grid.alpha": 0.9,
        }
    )


def style_table(df: pd.DataFrame) -> pd.io.formats.style.Styler:
    """Return a pandas Styler with aqua headers and alternating gray rows."""
    table_styles = [
        {
            "selector": "thead th",
            "props": [
                ("background-color", AQUA_DARK),
                ("color", GRAY_HEADER_TEXT),
                ("font-weight", "600"),
                ("border", f"1px solid {GRAY_BORDER}"),
                ("padding", "8px 12px"),
            ],
        },
        {
            "selector": "tbody td",
            "props": [
                ("border", f"1px solid {GRAY_BORDER}"),
                ("color", GRAY_DARK),
                ("padding", "6px 12px"),
            ],
        },
        {
            "selector": "tbody tr:nth-child(even) td",
            "props": [("background-color", GRAY_ROW_EVEN)],
        },
        {
            "selector": "tbody tr:nth-child(odd) td",
            "props": [("background-color", GRAY_ROW_ODD)],
        },
        {
            "selector": "tbody tr:hover td",
            "props": [("background-color", AQUA_PALE)],
        },
        {
            "selector": "caption",
            "props": [
                ("color", GRAY_MID),
                ("font-size", "0.9em"),
                ("padding", "6px"),
            ],
        },
    ]

    return df.style.set_table_styles(table_styles).hide(axis="index")
