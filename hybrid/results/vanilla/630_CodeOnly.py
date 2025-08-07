import pandas as pd
import os

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the full file path
    file_path = os.path.join(output_dir, filename)
    
    # Save the DataFrame to a JSON file
    df.to_json(file_path, orient='records', lines=True)
    
    # Return the full file path
    return file_path