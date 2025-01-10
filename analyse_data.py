import pandas as pd
import numpy as np

def load_data(filepath="performance-data.csv"):
    """
    Loads data from a CSV file.
    
    Returns:
        DataFrame: Loaded and cleaned data.
    """

    return pd.read_csv(filepath)

def get_value(data, category, year):
    """
    Retrieves the value for a specific category and year.

    Args:
        data (pd.DataFrame): The dataset.
        category (str): The category to search for.
        year (str): The year to search for.

    Returns:
        float: Value for the specified category and year.

    Raises:
        ValueError: If the category or year is not found in the dataset.
    """
    if year not in data.columns:
        raise ValueError(f"The year '{year}' is not in the dataset.")
    if category not in data['Category'].values:
        raise ValueError(f"The category '{category}' is not in the dataset.")
    return data.loc[data['Category'] == category, year].values[0]

def statistic_info(data):
    """
    Returns statistical information about the dataset.
    
    Args:
        data (pd.DataFrame): The dataset.
    
    Returns:
        pd.DataFrame: Statistical summary of the dataset (transposed).
    """
    info = data.describe().T
    return info

if __name__ == "__main__":
    # Filepath to the cleaned dataset
    filepath = "performance-data.csv"

    # Load the data
    data = load_data(filepath)
    
    # Specify the category and year for analysis
    category = "ATP / ATO"
    year = "2004/05"
    
    # Retrieve the value for the specified category and year
    try:
        value = get_value(data, category, year)
        print(f"The value for '{category}' in {year} is: {value}")
    except ValueError as e:
        print(e)

    stats = statistic_info(data)
    print(stats)