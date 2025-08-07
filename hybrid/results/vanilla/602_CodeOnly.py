import numpy as np
import pandas as pd
import os

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'

def task_func(file_path, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the dimensions of the matrix
    rows, cols = 10, 10  # You can change these dimensions as needed
    
    # Generate a 2D matrix with random lowercase letters
    matrix = np.random.choice(LETTERS, size=(rows, cols))
    
    # Create a DataFrame from the matrix
    df = pd.DataFrame(matrix)
    
    # Define the full file path
    full_file_path = os.path.join(output_dir, file_path)
    
    # Write the DataFrame to a CSV file
    df.to_csv(full_file_path, index=False, header=False)

# Example usage
task_func('random_letters.csv')