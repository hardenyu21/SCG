import pandas as pd
from scipy import stats

def task_func(matrix):
    # Convert the input matrix to a DataFrame
    df = pd.DataFrame(matrix)
    
    # Apply Z-score normalization to each column
    normalized_df = df.apply(stats.zscore)
    
    return normalized_df