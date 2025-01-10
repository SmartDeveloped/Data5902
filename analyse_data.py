import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import linregress

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

def create_boxplot(dataset, title, xlabel, ylabel):
    print("Initial Dataset:\n", dataset)

    # Exclude the "TOTAL" row and drop any rows with missing numerical values
    dataset = dataset.loc[~dataset["Category"].str.strip().str.lower().eq("total")].dropna()

    print("Filtered Dataset (after excluding TOTAL):\n", dataset)

    # Initialise lists to store categories and values
    valid_categories = []
    values = []

    # Iterate through each category
    for category in dataset["Category"].unique():
        # Filter the data for the current category
        category_data = dataset[dataset["Category"] == category]

        # Ensure the category exists
        if not category_data.empty:
            # Extract numerical values
            row_values = category_data.iloc[0, 1:].values.astype(float)
            print(f"Debug - Category: {category}, Values: {row_values}")  # Debugging line
            valid_categories.append(category)  # Add the category
            values.append(row_values)  # Add the corresponding values

    print("Categories Extracted:", valid_categories)  # Debugging line
    print("Values Extracted:", values)  # Debugging line

    assert len(valid_categories) == len(values), "Mismatch between categories and values."

    # Plot the boxplot
    plt.figure(figsize=(15, 8))  # Larger figure for better readability
    plt.boxplot(values, labels=valid_categories)

    # Plot for better readability
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(rotation=45, fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    return valid_categories, values

def create_lineargraph(dataset, x, y, xlabel, ylabel, title):

    # Ensure the columns exist in the dataset
    if x not in dataset["Category"].values or y not in dataset["Category"].values:
        raise ValueError(f"Either '{x}' or '{y}' is not a valid category in the dataset.")

    # Extract data for x and y
    x_data = dataset[dataset["Category"] == x].iloc[:, 1:].values.flatten().astype(float)
    y_data = dataset[dataset["Category"] == y].iloc[:, 1:].values.flatten().astype(float)

    # Perform linear regression
    slope, intercept, r, p, std_err = linregress(x_data, y_data)

    # Define the regression function
    def myfunc(x):
        return slope * x + intercept

    # Generate the regression line
    regression_line = list(map(myfunc, x_data))

    # Plot the scatter plot and regression line
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, label='Data Points')
    plt.plot(x_data, regression_line, color='red', label=f'Line: y={slope:.2f}x+{intercept:.2f}')
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.tight_layout()
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
        title="Boxplot of Variable's number of occurance Over All Years",
        xlabel="Year",
        ylabel="Number of Occasions (1 = 100,000)"
    )
    
    # Create the linear regression graph
    create_lineargraph(
        dataset = data,
        x = "Staff - Absence or Shortage",
        y = "Other LU Operations",
        xlabel = "Absence or Shortage from staff",
        ylabel = "London Underground Operation",
        title = "Linear Regression on Absence or Shortage and London Underground Operation of  Over All Years"
    )