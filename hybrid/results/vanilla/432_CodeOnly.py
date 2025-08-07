import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import pandas as pd

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge the dataframes on the 'id' column
    merged_df = pd.merge(df1, df2, on='id')
    
    # Create a contingency table from the specified columns
    contingency_table = pd.crosstab(merged_df[column1], merged_df[column2])
    
    # Perform the Chi-Squared test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    # Plot the heatmap of the contingency table
    plt.figure(figsize=(8, 6))
    heatmap = sns.heatmap(contingency_table, annot=True, fmt="d", cmap="YlGnBu")
    plt.title(f'Heatmap of {column1} vs {column2}')
    plt.xlabel(column2)
    plt.ylabel(column1)
    
    # Return the p-value and the heatmap
    return p, heatmap

# Example usage:
# df1 = pd.DataFrame({'id': [1, 2, 3, 4], 'feature1': ['A', 'B', 'A', 'B']})
# df2 = pd.DataFrame({'id': [1, 2, 3, 4], 'feature2': ['X', 'Y', 'X', 'Y']})
# p_value, heatmap = task_func(df1, df2)
# plt.show()