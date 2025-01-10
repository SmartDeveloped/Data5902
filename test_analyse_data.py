import pytest
import pandas as pd
from analyse_data import load_data, get_value, statistic_info

def create_mock_dataset():
    return pd.DataFrame({
        "Category": ["Test Category"],
        "2004/05": [100.0],
        "2005/06": [200.0]
    })

def test_load_data():
    # Create a mock dataset for testing
    mock_data = create_mock_dataset()
    mock_data.to_csv("test_data.csv", index=False)
    
    # Test the load_data function
    data = load_data("test_data.csv")
    assert data.shape == (1, 3)
    assert list(data.columns) == ["Category", "2004/05", "2005/06"]
    assert data["2004/05"].dtype == float


def test_get_value():
    # Create a mock dataset
    mock_data = create_mock_dataset()

    # Test get_value function
    value = get_value(mock_data, "Test Category", "2004/05")
    assert value == 100.0

    # Test with invalid category
    with pytest.raises(ValueError, match="The category 'Invalid Category' is not in the dataset."):
        get_value(mock_data, "Invalid Category", "2004/05")

    # Test with invalid year
    with pytest.raises(ValueError, match="The year 'Invalid Year' is not in the dataset."):
        get_value(mock_data, "Test Category", "Invalid Year")

def test_statistic_info():
    """
    Tests the `statistic_info` function.
    """
    # Create a mock dataset
    mock_data = create_mock_dataset()

    # Run the function
    stats = statistic_info(mock_data.drop(columns=["Category"]))

    # Assert that the result is a DataFrame
    assert isinstance(stats, pd.DataFrame), "Output should be a DataFrame."

    with pytest.raises(ValueError, match="The output is a DataFrame"):
        statistic_info(mock_data)

