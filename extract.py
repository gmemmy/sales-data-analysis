import pandas as pd
from sqlalchemy import create_engine

def load_sales_data():
    # connect to the SQLite database 'sales.db'
    engine = create_engine('sqlite:///sales.db')
    query = "SELECT * FROM sales"

    # use pandas to execute the SQL query and return the data as a DataFrame
    df = pd.read_sql_query(query, engine)
    return df

if __name__ == "__main__":
    # if the script is run directly, we load the data and print it
    df = load_sales_data()
    print(df)
    