# YGfews

A basic Python data science project skeleton with common utilities for data loading, cleaning, and visualization.

## Project Structure

```
YGfews/
├── data/
│   ├── raw/           # Raw, immutable data
│   ├── processed/     # Cleaned and processed data
│   └── external/      # External data sources
├── notebooks/         # Jupyter notebooks for analysis
│   └── example_analysis.ipynb
├── src/
│   └── ygfews/       # Source code for the project
│       ├── __init__.py
│       ├── data_utils.py      # Data loading and cleaning utilities
│       └── visualization.py   # Plotting and visualization functions
├── tests/            # Unit tests
│   ├── test_data_utils.py
│   └── test_visualization.py
├── .env.example      # Example environment variables
├── .gitignore        # Git ignore rules
├── pyproject.toml    # Project configuration and dependencies
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Features

- **Data Utilities**: Load, save, and clean data in multiple formats (CSV, JSON, Excel, Parquet)
- **Visualization**: Create distribution plots and correlation matrices
- **Testing**: Comprehensive unit tests with pytest
- **Jupyter Notebooks**: Example analysis workflow

## Installation

1. Clone the repository:
```bash
git clone https://github.com/everettsp/YGfews.git
cd YGfews
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install in development mode:
```bash
pip install -e .
```

## Usage

### Basic Data Operations

```python
from ygfews import load_data, save_data, clean_data

# Load data
df = load_data('data/raw/dataset.csv')

# Clean data
df_clean = clean_data(df, drop_duplicates=True)

# Save processed data
save_data(df_clean, 'data/processed/clean_data.csv', index=False)
```

### Visualization

```python
from ygfews import plot_distribution, plot_correlation_matrix
import matplotlib.pyplot as plt

# Plot distribution
fig = plot_distribution(df['column_name'], title='My Distribution')
plt.show()

# Plot correlation matrix
fig = plot_correlation_matrix(df)
plt.show()
```

### Jupyter Notebooks

Launch Jupyter and explore the example notebook:
```bash
jupyter notebook notebooks/example_analysis.ipynb
```

## Running Tests

Run all tests:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=ygfews tests/
```

## Development

### Code Formatting

Format code with Black:
```bash
black src/ tests/
```

### Linting

Check code style with flake8:
```bash
flake8 src/ tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.