import matplotlib.pyplot as plt
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
    
    Returns:
        pd.DataFrame: Statistical summary of the dataset (transposed).
    """
    info = data.describe().T
    return info

def create_linegraph(dataset, x, y, title, xlabel, ylabel):
    """
    Creates and displays a graph.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(dataset[x], dataset[y], marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()


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

    # Print the statistic information from dataset
    stats = statistic_info(data)
    print(stats)

# Filter for the "Power Failure" category
    power_filtered = data[data["Category"] == "Power Failure"].set_index("Category")

    # Transpose the data to get years as rows
    power_filtered = power_filtered.T
    power_filtered.columns = ["Power Failure"]  # Rename the column for clarity

    # Reset index to prepare for graphing
    power_filtered = power_filtered.reset_index()
    power_filtered.rename(columns={"index": "Year"}, inplace=True)

    # Create the line graph
    create_linegraph(
        dataset=power_filtered,
        x="Year",
        y="Power Failure",
        title="Analysis of Power Failures Over All Years",
        xlabel="Year",
        ylabel="Number of Occasions"
    )