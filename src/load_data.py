from __future__ import annotations

import pandas as pd


def load_raw_air_quality(path) -> pd.DataFrame:
    """
    Load the UCI Air Quality dataset.

    Hints:
    - Separator is ';'
    - Decimal separator is ','
    - There may be empty trailing columns

    Load the UCI Air Quality dataset with the original separators and decimals.
    """
    df = pd.read_csv(path, sep=";", decimal=",")
    return df.loc[:, ~df.columns.str.contains("^Unnamed")]


def diagnose_structure(df: pd.DataFrame) -> dict:
    """
    Return a dict with shape, dtypes, duplicate column names, and empty columns.
    """
    duplicate_columns = df.columns[df.columns.duplicated()].tolist()
    empty_columns = df.columns[df.isna().all()].tolist()
    numeric_like = df.select_dtypes(include="object").columns.tolist()

    return {
        "shape": df.shape,
        "dtypes": df.dtypes,
        "duplicate_columns": duplicate_columns,
        "empty_columns": empty_columns,
        "object_columns": numeric_like,
        "duplicate_rows": int(df.duplicated().sum()),
    }


def build_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Combine 'Date' and 'Time' into a single datetime column (Section 1f).

    Guiding question: What structural problems do you observe?
    """
    result = df.copy()
    result["Datetime"] = pd.to_datetime(
        result["Date"].astype(str).str.strip() + " " + result["Time"].astype(str).str.strip(),
        format="%d/%m/%Y %H.%M.%S",
        errors="coerce",
    )
    return result
