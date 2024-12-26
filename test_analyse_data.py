import pytest
import pandas as pd
from analyse_data import load_data, calculate_mean

def test_load_data():
    # Create a temporary CSV file
    test_data = pd.DataFrame({"id": [1, 2], "value": [10, 20]})
    test_data.to_csv("tests/temp_data.csv", index=False)

    # Test the load_data function
    data = load_data("tests/temp_data.csv")
    assert data.shape == (2, 2)
    assert list(data.columns) == ["id", "value"]

def test_calculate_mean():
    # Create test data
    test_data = pd.DataFrame({"value": [10, 20, 30]})
    
    # Test the calculate_mean function
    mean_value = calculate_mean(test_data)
    assert mean_value == 20