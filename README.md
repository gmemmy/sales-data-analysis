# Sales Data Analysis Project

This project is a proof-of-concept that integrates **SQLAlchemy**, **Pandas**, **pytest**, **Docker Compose**, **Liquibase**, and **PyMySQL** geared towards helping me learn data analysis with python through a small sales data application. It creates a MySQL database using Docker, manages database migrations with Liquibase, connects to MySQL using PyMySQL, loads data into a Pandas DataFrame, performs basic analysis, and tests the functions using pytest.

## Project Structure
```
sales_data_analysis/
├── analysis.py      # Contains data analysis functions
├── extract.py       # Data extraction and database setup
├── models.py        # SQLAlchemy models
├── test_analysis.py # Test cases
├── requirements.txt # Project dependencies
├── docker-compose.yml # Docker Compose configuration
├── .env            # Environment variables
├── changelogs/     # Liquibase changelog files
│   └── db-changelog.xml
└── drivers/        # Database drivers
```

## Setup Guide

### Prerequisites
- Docker and Docker Compose
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

4. Set up environment variables:
   ```bash
   cp .env.example .env 
   # Edit .env with your desired database credentials
   ```

5. Start the database and run migrations:
   ```bash
   docker-compose up -d
   ```
   This will:
   - Start a MySQL container
   - Run Liquibase migrations to create the database schema
   - Set up the necessary database structure

6. Load sample data:
   ```bash
   python extract.py
   ```

### Running the Project

1. Run the analysis functions:
   ```bash
   python analysis.py
   ```

2. To run the tests:
   ```bash
   pytest
   ```

### Database Management

- To view database migrations:
  ```bash
  docker-compose run liquibase status
  ```

- To rollback changes:
  ```bash
  docker-compose run liquibase rollbackCount 1
  ```

- To stop the database:
  ```bash
  docker-compose down
  ```

### Project Dependencies
- SQLAlchemy (>=2.0.40): For database operations
- Pandas (>=2.2.3): For data analysis
- pytest (>=8.3.5): For running tests
- Docker and Docker Compose: For containerized database and migrations
- Liquibase: For database migration management
- PyMySQL (>=1.1.0): Python MySQL client library for database connectivity
- python-dotenv (>=1.0.0): For loading environment variables from .env file

## Database Connectivity

This project uses PyMySQL as the database connector for SQLAlchemy to communicate with MySQL. The connection string in `models.py` is configured as:

```python
connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
```

The `mysql+pymysql://` prefix tells SQLAlchemy to use the PyMySQL driver for connecting to the MySQL database. Environment variables from the `.env` file are used to configure the connection parameters.
