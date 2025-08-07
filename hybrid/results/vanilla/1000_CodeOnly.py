import urllib.request
import os
import json
import pandas as pd

# Constants
TARGET_JSON_FILE = "downloaded_file.json"

def task_func(url):
    # Download the JSON file from the given URL
    urllib.request.urlretrieve(url, TARGET_JSON_FILE)
    
    # Open and read the downloaded JSON file
    with open(TARGET_JSON_FILE, 'r') as file:
        json_data = json.load(file)
    
    # Convert the JSON data into a pandas DataFrame
    df = pd.DataFrame(json_data)
    
    # Delete the temporary JSON file
    os.remove(TARGET_JSON_FILE)
    
    # Return the DataFrame
    return df