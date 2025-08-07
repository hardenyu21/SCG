import pandas as pd
from scipy.spatial.distance import pdist, squareform

def task_func(array):
    # Convert the 2D list into a DataFrame
    num_columns = len(array[0])
    column_names = [chr(65 + i) for i in range(num_columns)]  # Generate column names 'A', 'B', ..., 'Z'
    df = pd.DataFrame(array, columns=column_names)
    
    # Calculate the Euclidean distance matrix between rows
    distances = pdist(df, metric='euclidean')
    distance_matrix = pd.DataFrame(squareform(distances), index=df.index, columns=df.index)
    
    return df, distance_matrix

# Example usage:
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

df, distance_matrix = task_func(array)
print("DataFrame:")
print(df)
print("\nDistance Matrix:")
print(distance_matrix)