import requests
import pandas as pd
import matplotlib.pyplot as plt

def task_func(api_url):
    # Check if the provided API URL is a string
    if not isinstance(api_url, str):
        raise TypeError("The API URL must be a string.")
    
    try:
        # Fetch data from the specified API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Process the JSON response
        data = response.json()
        
        # Convert the JSON data into a pandas DataFrame
        df = pd.DataFrame(data)
        
        # Check if the DataFrame is empty
        if df.empty:
            print("No data to plot.")
            return df, None
        
        # Plot the data using matplotlib
        ax = df.plot()
        plt.title('API Data Plot')
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.show()
        
        return df, ax
    
    except requests.exceptions.HTTPError as http_err:
        raise requests.exceptions.HTTPError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise Exception(f"An error occurred: {err}")

# Example usage:
# df, ax = task_func("https://api.example.com/data")