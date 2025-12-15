# Getting Started with YGfews

## Quick Start

This guide will help you get started with the YGfews data science project.

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation Steps

### 1. Set Up Virtual Environment

It's recommended to use a virtual environment to isolate project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install in development mode (recommended for development)
pip install -e ".[dev]"
```

### 3. Verify Installation

```bash
# Run tests to verify everything is working
pytest tests/
```

## First Analysis

### 1. Create a Dataset

Create a CSV file in `data/raw/sample.csv`:

```csv
name,age,score
Alice,25,85.5
Bob,30,90.0
Charlie,35,78.5
```

### 2. Load and Process Data

Create a Python script or use a Jupyter notebook:

```python
from ygfews import load_data, clean_data, plot_distribution
import matplotlib.pyplot as plt

# Load data
df = load_data('data/raw/sample.csv')
print(df.head())

# Clean data
df_clean = clean_data(df)

# Visualize
fig = plot_distribution(df_clean['age'], title='Age Distribution')
plt.show()
```

### 3. Explore the Example Notebook

Open the example notebook to see more detailed workflows:

```bash
jupyter notebook notebooks/example_analysis.ipynb
```

## Next Steps

- Read the [API documentation](api_reference.md) for detailed function descriptions
- Explore the example notebook for common workflows
- Check out the test files for usage examples
- Customize the package for your specific needs

## Common Tasks

### Adding New Data Sources

1. Place raw data in `data/raw/`
2. Load with `load_data()` function
3. Process and save to `data/processed/`

### Creating Custom Analysis

1. Create a new notebook in `notebooks/`
2. Import utilities from `ygfews`
3. Document your analysis with markdown cells

### Extending Functionality

1. Add new functions to `src/ygfews/`
2. Write tests in `tests/`
3. Update documentation

## Troubleshooting

### Import Errors

If you get import errors, make sure:
- Virtual environment is activated
- Package is installed: `pip install -e .`
- You're in the project root directory

### Missing Dependencies

Install missing packages:
```bash
pip install -r requirements.txt
```

### Test Failures

Check Python version:
```bash
python --version  # Should be 3.8+
```

## Getting Help

- Check the [README.md](../README.md) for project overview
- Review test files for usage examples
- Open an issue on GitHub for bugs or questions
