"""Tests for data_utils module."""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile
import shutil

from ygfews.data_utils import load_data, save_data, clean_data


class TestDataUtils:
    """Test suite for data utility functions."""

    @pytest.fixture
    def sample_dataframe(self):
        """Create a sample DataFrame for testing."""
        return pd.DataFrame(
            {
                "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
                "age": [25, 30, 35, 40, 45],
                "score": [85.5, 90.0, 78.5, 92.0, 88.5],
            }
        )

    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for testing."""
        temp_path = tempfile.mkdtemp()
        yield Path(temp_path)
        shutil.rmtree(temp_path)

    def test_save_and_load_csv(self, sample_dataframe, temp_dir):
        """Test saving and loading CSV files."""
        filepath = temp_dir / "test.csv"
        save_data(sample_dataframe, filepath, index=False)
        loaded_df = load_data(filepath)

        pd.testing.assert_frame_equal(
            sample_dataframe, loaded_df, check_dtype=False
        )

    def test_clean_data_removes_duplicates(self):
        """Test that clean_data removes duplicate rows."""
        df = pd.DataFrame(
            {
                "A": [1, 2, 2, 3],
                "B": [4, 5, 5, 6],
            }
        )
        cleaned = clean_data(df, drop_duplicates=True)
        assert len(cleaned) == 3
        assert not cleaned.duplicated().any()

    def test_clean_data_removes_empty_rows(self):
        """Test that clean_data removes completely empty rows."""
        df = pd.DataFrame(
            {
                "A": [1, np.nan, 3],
                "B": [4, np.nan, 6],
            }
        )
        cleaned = clean_data(df)
        assert len(cleaned) == 2

    def test_clean_data_preserves_partial_data(self):
        """Test that clean_data preserves rows with partial data."""
        df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "B": [4, np.nan, 6],
            }
        )
        cleaned = clean_data(df)
        assert len(cleaned) == 3
