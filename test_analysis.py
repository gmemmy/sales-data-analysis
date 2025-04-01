import pandas as pd
import pytest
from analysis import calculate_total_sales, calculate_sales_by_region

@pytest.fixture
def sample_sales_data():
    # create a sample DataFrame with sales data
    data = {
        'id': [1, 2, 3, 4],
        'date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04'],
        'region': ['North', 'South', 'East', 'West'],
        'amount': [100, 200, 300, 400]
    }
    df = pd.DataFrame(data)
    return df

def test_calculate_total_sales(sample_sales_data):
    total = calculate_total_sales(sample_sales_data)
    # expected total sales is 100 + 200 + 300 + 400
    assert total == 1000

def test_calculate_sales_by_region(sample_sales_data):
    sales_by_region = calculate_sales_by_region(sample_sales_data)
    # expected sales by region is 100 for North, 200 for South, 300 for East, 400 for West
    assert sales_by_region['North'] == 100
    assert sales_by_region['South'] == 200
    assert sales_by_region['East'] == 300
    assert sales_by_region['West'] == 400
    