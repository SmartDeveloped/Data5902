import pandas as pd

def load_data(filepath):
    """
    Loads data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
    
    Returns:
        DataFrame: Loaded data.
    """
    return pd.read_csv(filepath)

def calculate_mean(data):
    """
    Calculates the mean of the 'value' column.
    
    Args:
        data (DataFrame): Pandas DataFrame with a 'value' column.
    
    Returns:
        float: Mean value of the 'value' column.
    """
    return data['value'].mean()

if __name__ == "__main__":
    # Filepath to the data
    filepath = "/Users/timothysmartomoruyi/Documents/Data5902/sample_data.csv"
    
    # Load the data
    data = load_data(filepath)
    
    # Calculate the mean value
    mean_value = calculate_mean(data)
    
    print(f"The mean value is: {mean_value}")