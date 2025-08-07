import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    # Check if the input data has exactly eight columns
    if data.shape[1] != 8:
        raise ValueError("The input data must have exactly eight columns.")
    
    # Ensure the data is a DataFrame with the correct column names
    data.columns = COLUMN_NAMES
    
    # Compute the average of each row
    data['Average'] = data.mean(axis=1)
    
    # Plot the distribution of the averages
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(data['Average'], kde=True)
    ax.set_title('Distribution of Row Averages')
    ax.set_xlabel('Average')
    ax.set_ylabel('Frequency')
    
    # Evaluate normality using the normaltest
    p_value = None
    if len(data) >= 20:
        _, p_value = stats.normaltest(data['Average'])
    
    # Return the DataFrame, Axes object, and p-value
    return data, ax, p_value

# Example usage:
# df = pd.DataFrame(np.random.rand(100, 8))
# result_df, ax, p_value = task_func(df)
# plt.show()
# print("P-value:", p_value)