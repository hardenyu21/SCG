import json
import os
import pandas as pd

def task_func(json_str, filename, sheet_name="sheet1"):
    # Validate input type
    if not isinstance(json_str, (str, bytes, bytearray)):
        raise TypeError("json_str must be a string, bytes, or bytearray.")
    
    try:
        # Parse JSON string
        data = json.loads(json_str)
    except json.JSONDecodeError:
        raise ValueError("json_str is not valid JSON.")
    
    # Check if data is a list
    if not isinstance(data, list):
        raise ValueError("json_str must represent a JSON array.")
    
    # Create a DataFrame from the JSON data
    df = pd.DataFrame(data)
    
    # Define the full path for the Excel file
    full_path = os.path.abspath(filename)
    
    try:
        # Write the DataFrame to an Excel file
        with pd.ExcelWriter(full_path, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    except Exception as e:
        raise Exception(f"An error occurred while writing to the file: {e}")
    
    # Return the absolute path of the created Excel file
    return full_path