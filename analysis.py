import pandas as pd

def calculate_total_sales(df: pd.DataFrame) -> float:
    """Returns the total sales amount by summing the 'amount' column."""
    return df['amount'].sum()

def calculate_sales_by_region(df: pd.DataFrame) -> pd.Series:
    """Returns total sales grouped by region."""
    return df.groupby('region')['amount'].sum()

if __name__ == "__main__":
    # we import the data loading function from extract.py
    from extract import load_sales_data
    # load the sales data
    df = load_sales_data()

    total_sales = calculate_total_sales(df)
    by_region = calculate_sales_by_region(df)

    print("Total Sales:", total_sales)
    print("Sales by Region:\n", by_region)
    