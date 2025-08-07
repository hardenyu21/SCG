import pandas as pd
import numpy as np

def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    # Set the random seed for reproducibility if provided
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random numeric data
    data = np.random.rand(num_rows, data_dimensions)
    
    # Create column names
    column_names = [f'Feature_{i+1}' for i in range(data_dimensions)]
    
    # Create a DataFrame
    df = pd.DataFrame(data, columns=column_names)
    
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    
    # Return the file path
    return file_path