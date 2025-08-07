import numpy as np
import pandas as pd

def task_func(matrix1, matrix2):
    # Concatenate the two matrices along the second axis (columns)
    combined_matrix = np.concatenate((matrix1, matrix2), axis=1)
    
    # Convert the combined matrix into a Pandas DataFrame
    df = pd.DataFrame(combined_matrix)
    
    # Get the string representation of the DataFrame without the index and header
    df_string = df.to_string(index=False, header=False)
    
    return df_string