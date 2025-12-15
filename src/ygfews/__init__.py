"""YGfews - A basic Python data science package."""

__version__ = "0.1.0"

from .data_utils import load_data, save_data, clean_data
from .visualization import plot_distribution, plot_correlation_matrix

__all__ = [
    "load_data",
    "save_data",
    "clean_data",
    "plot_distribution",
    "plot_correlation_matrix",
]
