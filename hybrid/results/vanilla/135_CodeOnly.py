import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame and has at least one column
    if not isinstance(df, pd.DataFrame) or df.shape[1] == 0:
        raise ValueError("Input must be a DataFrame with at least one column.")
    
    # Select the last column
    last_column = df.columns[-1]
    
    # Impute missing values in the last column using mean imputation
    imputer = SimpleImputer(strategy='mean')
    df[last_column] = imputer.fit_transform(df[[last_column]])
    
    # Create a box plot to visualize the distribution of data in the last column
    plt.figure(figsize=(8, 6))
    ax = sns.boxplot(y=df[last_column])
    ax.set_title(f'Box Plot of {last_column}')
    ax.set_ylabel(last_column)
    
    # Return the DataFrame with imputed values and the Axes object
    return df, ax

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, np.nan, 4],
#     'B': [5, np.nan, 7, 8]
# })
# imputed_df, ax = task_func(df)
# plt.show()