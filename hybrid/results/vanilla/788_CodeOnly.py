import heapq
from scipy import stats
import pandas as pd

def task_func(df, col1, col2, N=10):
    # Check if the specified columns are in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError("Specified columns are not in the provided DataFrame.")
    
    # Check if N is greater than 1
    if N <= 1:
        raise ValueError("N must be greater than 1.")
    
    # Calculate the absolute differences between the corresponding elements of the two columns
    differences = abs(df[col1] - df[col2])
    
    # Find the indices of the N largest differences
    largest_diff_indices = heapq.nlargest(N, range(len(differences)), key=differences.__getitem__)
    
    # Extract the elements from the specified columns using these indices
    col1_values = df[col1].iloc[largest_diff_indices]
    col2_values = df[col2].iloc[largest_diff_indices]
    
    # Perform a t-Test on these elements
    t_stat, p_value = stats.ttest_ind(col1_values, col2_values)
    
    return p_value

# Example usage
df = pd.DataFrame({
    'col1': [1, 3, 4, 70],
    'col2': [2, 3, 5, 1]
})
p_value = task_func(df, 'col1', 'col2', N=5)
print(p_value)