# Sales Data Analysis Project

This project is a proof-of-concept that integrates **SQLAlchemy**, **Pandas**, and **pytest** geared towards helping me learn data analysis with python through a small sales data application. It creates a simple SQLite database, loads data into a Pandas DataFrame, performs basic analysis, and tests the functions using pytest.

## Project Structure
```
sales_data_analysis/
├── analysis.py      # Contains data analysis functions
├── extract.py       # Data extraction and database setup
├── models.py        # SQLAlchemy models
├── test_analysis.py # Test cases
├── requirements.txt # Project dependencies
└── sales.db        # SQLite database (generated on setup)
```

## Setup Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/gmemmy/sales-data-analysis.git
   cd sales_data_analysis
   ```

2. Create and activate a virtual environment:
   ```bash
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Generate the database and load sample data:
   ```bash
   python extract.py
   ```
   This will create a `sales.db` file with sample data for analysis.

### Running the Project

1. Run the analysis functions:
   ```bash
   python analysis.py
   ```

2. To run the tests:
   ```bash
   pytest
   ```

### Project Dependencies
- SQLAlchemy (>=2.0.40): For database operations
- Pandas (>=2.2.3): For data analysis
- pytest (>=8.3.5): For running tests
