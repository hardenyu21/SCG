import pandas as pd
import os
import time

OUTPUT_DIR = './output'

def task_func(df: pd.DataFrame, filename: str) -> str:
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Construct the full file path
    file_path = os.path.join(OUTPUT_DIR, filename)
    
    # Write the DataFrame to a JSON Lines file
    df.to_json(file_path, orient='records', lines=True)
    
    # Return the full path where the file was saved
    return file_path

# Example usage:
# df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
# print(task_func(df, 'data.jsonl'))