import pandas as pd
import requests
from io import StringIO

def task_func(csv_url_dict, sort_by_column="title"):
    # Check if the dictionary is empty or if the "URL" key does not exist
    if not csv_url_dict or "URL" not in csv_url_dict:
        raise ValueError("The dictionary is empty or does not contain the 'URL' key.")
    
    # Fetch the CSV data from the URL
    url = csv_url_dict["URL"]
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    
    # Read the CSV data into a pandas DataFrame
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)
    
    # Sort the DataFrame based on the specified column
    if sort_by_column not in df.columns:
        raise ValueError(f"The specified column '{sort_by_column}' does not exist in the DataFrame.")
    
    sorted_df = df.sort_values(by=sort_by_column)
    
    return sorted_df