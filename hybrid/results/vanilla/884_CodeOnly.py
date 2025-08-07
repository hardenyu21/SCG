import pandas as pd
from scipy.stats import chi2_contingency

def task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900):
    # Check if the number of specified columns is 3
    if len(columns) != 3:
        raise ValueError("The number of specified columns must be 3.")
    
    # Check if the specified columns are contained in df
    if not all(col in df.columns for col in columns):
        raise ValueError("The specified columns are not contained in the DataFrame.")
    
    # Unpack the column names
    col1, col2, col3 = columns
    
    # Filter the DataFrame based on the criteria
    filtered_df = df[(df[col2] > larger) & (df[col3] == equal)]
    
    # Check if there's sufficient data for the test
    if filtered_df.empty:
        raise ValueError("There's insufficient data for the test (no rows meeting the criteria).")
    
    # Create a contingency table of the first two columns
    contingency_table = pd.crosstab(filtered_df[col1], filtered_df[col2])
    
    # Perform the chi-square independence test
    chi2, p_value, _, _ = chi2_contingency(contingency_table)
    
    # Return the p-value
    return p_value