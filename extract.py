import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

def load_sales_data():
    load_dotenv()

    # get database credentials from environment variables
    user = os.getenv("MYSQL_USER", "user")
    password = os.getenv("MYSQL_PASSWORD", "userpassword")
    host = os.getenv("MYSQL_HOST", "localhost")
    port = os.getenv("MYSQL_PORT", "3306")
    database = os.getenv("MYSQL_DATABASE", "sales")
    
    # connect to the MySQL database
    connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)


    query = "SELECT * FROM sales"
    # use pandas to execute the SQL query and return the data as a DataFrame
    df = pd.read_sql_query(query, engine)
    return df

if __name__ == "__main__":
    # if the script is run directly, we load the data and print it
    df = load_sales_data()
    print(df)
    