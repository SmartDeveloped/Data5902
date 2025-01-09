import pytest
import pandas as pd
from analyse_data import load_data, get_value

def test_load_data():
    # Create a mock dataset for testing
    mock_data = pd.DataFrame({
        "Category": ["Test Category"],
        "2004/05": [100.0],
        "2005/06": [200.0]
    })
    mock_data.to_csv("test_data.csv", index=False)
    
    # Test the load_data function
    data = load_data("test_data.csv")
    assert data.shape == (1, 3)
    assert list(data.columns) == ["Category", "2004/05", "2005/06"]
    assert data["2004/05"].dtype == float

def test_get_value():
    # Create a mock dataset
    mock_data = pd.DataFrame({
        "Category": ["Test Category"],
        "2004/05": [100.0],
        "2005/06": [200.0]
    })
    
    # Test get_value function
    value = get_value(mock_data, "Test Category", "2004/05")
    assert value == 100.0

    # Test with invalid category
    with pytest.raises(ValueError):
        get_value(mock_data, "Invalid Category", "2004/05")
    
    # Test with invalid year
    with pytest.raises(ValueError):
        get_value(mock_data, "Test Category", "Invalid Year")
