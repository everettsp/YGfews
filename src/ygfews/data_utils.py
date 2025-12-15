"""Utilities for loading, saving, and cleaning data."""

import pandas as pd
from pathlib import Path
from typing import Optional, Union


def load_data(
    filepath: Union[str, Path], file_format: Optional[str] = None
) -> pd.DataFrame:
    """
    Load data from various file formats.

    Args:
        filepath: Path to the data file
        file_format: File format (csv, json, excel, parquet). If None, inferred from extension.

    Returns:
        DataFrame containing the loaded data

    Examples:
        >>> df = load_data("data/raw/dataset.csv")
        >>> df = load_data("data/raw/dataset.json", file_format="json")
    """
    filepath = Path(filepath)

    if file_format is None:
        file_format = filepath.suffix.lstrip(".")

    readers = {
        "csv": pd.read_csv,
        "json": pd.read_json,
        "xlsx": pd.read_excel,
        "xls": pd.read_excel,
        "parquet": pd.read_parquet,
    }

    if file_format not in readers:
        raise ValueError(
            f"Unsupported file format: {file_format}. "
            f"Supported formats: {list(readers.keys())}"
        )

    return readers[file_format](filepath)


def save_data(
    df: pd.DataFrame,
    filepath: Union[str, Path],
    file_format: Optional[str] = None,
    **kwargs,
) -> None:
    """
    Save DataFrame to various file formats.

    Args:
        df: DataFrame to save
        filepath: Path where the file will be saved
        file_format: File format (csv, json, excel, parquet). If None, inferred from extension.
        **kwargs: Additional arguments passed to the save function

    Examples:
        >>> save_data(df, "data/processed/clean_data.csv")
        >>> save_data(df, "data/processed/clean_data.parquet", index=False)
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    if file_format is None:
        file_format = filepath.suffix.lstrip(".")

    writers = {
        "csv": df.to_csv,
        "json": df.to_json,
        "xlsx": df.to_excel,
        "parquet": df.to_parquet,
    }

    if file_format not in writers:
        raise ValueError(
            f"Unsupported file format: {file_format}. "
            f"Supported formats: {list(writers.keys())}"
        )

    writers[file_format](filepath, **kwargs)


def clean_data(df: pd.DataFrame, drop_duplicates: bool = True) -> pd.DataFrame:
    """
    Basic data cleaning operations.

    Args:
        df: DataFrame to clean
        drop_duplicates: Whether to drop duplicate rows

    Returns:
        Cleaned DataFrame

    Examples:
        >>> cleaned_df = clean_data(df)
        >>> cleaned_df = clean_data(df, drop_duplicates=False)
    """
    df_clean = df.copy()

    # Remove completely empty rows and columns
    df_clean = df_clean.dropna(how="all", axis=0)
    df_clean = df_clean.dropna(how="all", axis=1)

    # Drop duplicates if specified
    if drop_duplicates:
        df_clean = df_clean.drop_duplicates()

    # Reset index
    df_clean = df_clean.reset_index(drop=True)

    return df_clean
