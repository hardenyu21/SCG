import os
import time
import pandas as pd

OUTPUT_DIR = './output'

def task_func(datasets, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the full path for the output file
    file_path = os.path.join(output_dir, filename)
    
    # Open the file in write mode
    with open(file_path, 'w') as file:
        for i, df in enumerate(datasets):
            # Write the DataFrame to the file
            df.to_csv(file, index=False)
            
            # Add a separator line if it's not the last DataFrame
            if i < len(datasets) - 1:
                file.write('------\n')

# Example usage:
# df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})
# task_func([df1, df2], 'output.csv')