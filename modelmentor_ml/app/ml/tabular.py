"""Pandas / sklearn helpers aligned with common ModelMentor-style analysis."""
from __future__ import annotations

from typing import Any

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def records_to_dataframe(records: list[dict[str, Any]]) -> pd.DataFrame:
    return pd.DataFrame(records)


def describe_dataframe(records: list[dict[str, Any]]) -> dict[str, Any]:
    df = records_to_dataframe(records)
    try:
        desc = df.describe(include="all", datetime_is_numeric=True)
    except TypeError:
        desc = df.describe(include="all")
    describe = desc.transpose()
    missing = df.isna().mean().mul(100).round(2).to_dict()
    dtypes = {c: str(t) for c, t in df.dtypes.items()}
    desc_records = describe.reset_index().rename(columns={"index": "column"})
    desc_records = desc_records.astype(object).where(desc_records.notna(), None)
    return {
        "row_count": int(len(df)),
        "column_count": int(df.shape[1]),
        "columns": list(df.columns),
        "dtypes": dtypes,
        "missing_percent": missing,
        "describe_rows": desc_records.to_dict(orient="records"),
    }


def iqr_outlier_mask(records: list[dict[str, Any]], column: str) -> list[bool]:
    df = records_to_dataframe(records)
    if column not in df.columns:
        raise KeyError(column)
    series = pd.to_numeric(df[column], errors="coerce")
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    low = q1 - 1.5 * iqr
    high = q3 + 1.5 * iqr
    mask = (series < low) | (series > high)
    return [bool(x) for x in mask.fillna(False).tolist()]


def build_basic_preprocessing_pipeline(
    numeric_cols: list[str], categorical_cols: list[str]
) -> ColumnTransformer:
    """
    Example sklearn ColumnTransformer for mixed-type tabular data
    (use from notebooks or custom training scripts).
    """
    numeric_pipe = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())]
    )
    categorical_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
        ]
    )
    transformers: list[tuple[str, Pipeline, list[str]]] = []
    if numeric_cols:
        transformers.append(("num", numeric_pipe, numeric_cols))
    if categorical_cols:
        transformers.append(("cat", categorical_pipe, categorical_cols))
    return ColumnTransformer(transformers=transformers)
