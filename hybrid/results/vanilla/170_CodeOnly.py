import pandas as pd
import requests
from io import StringIO

def task_func(csv_url, sort_by_column="title"):
    # Send a GET request to the CSV URL
    response = requests.get(csv_url)
    
    # Check if the response status code is 200 (OK)
    if response.status_code != 200:
        raise Exception("Failed to fetch data: HTTP Status Code {}".format(response.status_code))
    
    # Read the CSV data from the response content
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)
    
    # Sort the DataFrame based on the specified column
    sorted_df = df.sort_values(by=sort_by_column)
    
    return sorted_df