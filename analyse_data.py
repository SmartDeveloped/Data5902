import pandas as pd

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
    """
    # Filter the DataFrame for the specified category
    filtered_data = data.loc[data['Category'] == category, year]
    
    # Check if the resulting DataFrame is empty
    if filtered_data.empty:
        raise ValueError(f"Category '{category}' does not exist.")
    
    # Return the first element of the filtered value
    return filtered_data.values[0]


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