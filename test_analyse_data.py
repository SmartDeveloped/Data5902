import pytest
import pandas as pd
from analyse_data import load_data, get_value, statistic_info, create_linegraph

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

import pandas as pd

def create_graph_mock_dataset():
    """
    Creates a mock dataset for testing purposes.
    """
    data = {
        "Category": ["Test Category 1", "Test Category 2", "Test Category 3"],
        "2004/05": [100, 200, 300],
        "2005/06": [150, 250, 350],
        "2006/07": [120, 220, 320]
    }
    return pd.DataFrame(data)

def test_create_linegraph():
    """
    Tests the create_linegraph function using a mock dataset.
    """
    # Create the mock dataset
    dataset = create_graph_mock_dataset()

    # Define test parameters
    category = "Test Category 1"
    title = "Category vs Units Over Time"
    xlabel = "Years"
    ylabel = "Units"

    # Call the function
    create_linegraph(
        dataset=dataset,
        category=category,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel
    )

# Run the test
if __name__ == "__main__":
    test_create_linegraph()

