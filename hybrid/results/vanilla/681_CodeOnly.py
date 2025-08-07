import pandas as pd
import json

def task_func(file_path, key):
    # Load the JSON file into a list of dictionaries
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Remove the specified key from each dictionary
    for item in data:
        if key in item:
            del item[key]
    
    # Convert the list of dictionaries into a DataFrame
    df = pd.DataFrame(data)
    
    # Write the processed DataFrame back into a JSON file oriented by records
    df.to_json(file_path, orient='records', lines=True)
    
    # Return the DataFrame
    return df