import pandas as pd

def load_data(filepath):
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

    value = data.loc[data['Category'] == category, year].values[0]
    return value

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