"""Tests for visualization module."""

import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from ygfews.visualization import plot_distribution, plot_correlation_matrix


class TestVisualization:
    """Test suite for visualization functions."""

    @pytest.fixture
    def sample_series(self):
        """Create a sample Series for testing."""
        np.random.seed(42)
        return pd.Series(np.random.normal(100, 15, 1000), name="test_data")

    @pytest.fixture
    def sample_dataframe(self):
        """Create a sample DataFrame for testing."""
        np.random.seed(42)
        return pd.DataFrame(
            {
                "age": np.random.randint(20, 60, 100),
                "income": np.random.normal(50000, 15000, 100),
                "score": np.random.uniform(0, 100, 100),
            }
        )

    def test_plot_distribution_returns_figure(self, sample_series):
        """Test that plot_distribution returns a Figure object."""
        fig = plot_distribution(sample_series)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_plot_distribution_with_custom_title(self, sample_series):
        """Test plot_distribution with custom title."""
        fig = plot_distribution(sample_series, title="Custom Title")
        assert fig.axes[0].get_title() == "Custom Title"
        plt.close(fig)

    def test_plot_correlation_matrix_returns_figure(self, sample_dataframe):
        """Test that plot_correlation_matrix returns a Figure object."""
        fig = plot_correlation_matrix(sample_dataframe)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)

    def test_plot_correlation_matrix_with_selected_columns(self, sample_dataframe):
        """Test plot_correlation_matrix with specific columns."""
        fig = plot_correlation_matrix(sample_dataframe, columns=["age", "income"])
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
