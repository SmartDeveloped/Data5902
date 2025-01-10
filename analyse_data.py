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

def create_linegraph(dataset, category, title, xlabel, ylabel):
    """
    Creates and displays a graph.
    """
# Filter the data for the given category
    filtered_data = dataset[dataset["Category"] == category].set_index("Category")

    # Transpose the data to get years as rows
    filtered_data = filtered_data.T

    # Rename the column for clarity
    filtered_data.columns = [category]

    # Reset the index to prepare for graphing
    filtered_data = filtered_data.reset_index()
    filtered_data.rename(columns={"index": "Year"}, inplace=True)

    # Plot the data
    plt.figure(figsize=(10, 6))  # Create a new figure
    plt.plot(filtered_data["Year"], filtered_data[category], marker='o', label=category)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show() 

def create_boxplot(dataset, category, title, xlabel, ylabel):
    filtered_data = dataset[dataset["Category"] == category].set_index("Category")

    # Transpose the data to get years as rows
    filtered_data = filtered_data.T
    # Numerical values to a list for boxplot
    data_values = filtered_data.values.astype(float).tolist()

    # Prepare the years as labels
    years = filtered_data.index

    plt.figure(figsize=(10, 6))
    plt.boxplot(data_values, labels=years)
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

    # Create the line graph
    create_linegraph(
        dataset=data,
        category = "Signals",
        title="Analysis of Signals Over All Years",
        xlabel="Year",
        ylabel="Number of Occasions"
    )

    # Create the line graph
    create_linegraph(
        dataset=data,
        category = "Power Failure",
        title="Analysis of Power Failures Over All Years",
        xlabel="Year",
        ylabel="Number of Occasions"
    )

    # Create the boxplot graph
    create_boxplot(
        dataset=data,
        category = "Staff - Absence or Shortage",
        title="Analysis of Impact Staff absence or shortage of  Over All Years",
        xlabel="Year",
        ylabel="Number of Occasions"
    )