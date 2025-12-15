"""Visualization utilities for data exploration."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Optional, List, Tuple


def plot_distribution(
    data: pd.Series,
    title: Optional[str] = None,
    bins: int = 30,
    figsize: Tuple[int, int] = (10, 6),
) -> plt.Figure:
    """
    Plot the distribution of a numeric series.

    Args:
        data: Pandas Series or array-like data to plot
        title: Plot title. If None, uses the series name
        bins: Number of histogram bins
        figsize: Figure size (width, height)

    Returns:
        Matplotlib Figure object

    Examples:
        >>> fig = plot_distribution(df['age'], title='Age Distribution')
        >>> plt.show()
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Plot histogram with KDE
    ax.hist(data.dropna(), bins=bins, alpha=0.7, edgecolor="black", density=True)

    # Add KDE line
    data_clean = data.dropna()
    if len(data_clean) > 1:
        from scipy import stats

        kde = stats.gaussian_kde(data_clean)
        x_range = np.linspace(data_clean.min(), data_clean.max(), 100)
        ax.plot(x_range, kde(x_range), "r-", linewidth=2, label="KDE")
        ax.legend()

    # Set title and labels
    if title is None:
        title = f"Distribution of {data.name}" if hasattr(data, "name") else "Distribution"
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel("Value", fontsize=12)
    ax.set_ylabel("Density", fontsize=12)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def plot_correlation_matrix(
    df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    figsize: Tuple[int, int] = (12, 10),
    cmap: str = "coolwarm",
) -> plt.Figure:
    """
    Plot correlation matrix heatmap for numeric columns.

    Args:
        df: DataFrame containing the data
        columns: List of column names to include. If None, uses all numeric columns
        figsize: Figure size (width, height)
        cmap: Colormap for the heatmap

    Returns:
        Matplotlib Figure object

    Examples:
        >>> fig = plot_correlation_matrix(df)
        >>> fig = plot_correlation_matrix(df, columns=['age', 'income', 'score'])
        >>> plt.show()
    """
    # Select columns
    if columns is None:
        data = df.select_dtypes(include=[np.number])
    else:
        data = df[columns]

    # Calculate correlation matrix
    corr_matrix = data.corr()

    # Create heatmap
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap=cmap,
        center=0,
        square=True,
        linewidths=1,
        cbar_kws={"shrink": 0.8},
        ax=ax,
    )

    ax.set_title("Correlation Matrix", fontsize=14, fontweight="bold")
    plt.tight_layout()
    return fig
