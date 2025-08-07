import requests
import pandas as pd

def task_func(url: str) -> pd.DataFrame:
    try:
        # Send a GET request to the specified URL with a timeout of 5 seconds
        response = requests.get(url, timeout=5)
        
        # Raise an HTTPError for unsuccessful status codes
        response.raise_for_status()
        
        # Convert the response content to JSON
        json_data = response.json()
        
        # Convert the JSON data to a Pandas DataFrame
        df = pd.DataFrame(json_data)
        
        return df
    
    except requests.RequestException as e:
        # Re-raise as SystemError for network-related issues
        raise SystemError(f"Network-related error occurred: {e}")
    
    except ValueError as e:
        # Raise ValueError for invalid JSON format
        raise ValueError(f"Invalid JSON format: {e}")