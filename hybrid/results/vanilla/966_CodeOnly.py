import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if all columns are numeric
    if not all(df.dtypes.apply(lambda x: pd.api.types.is_numeric_dtype(x))):
        raise ValueError("The DataFrame contains non-numeric data.")
    
    # Calculate the cumulative sum for each column, ignoring NaN values
    cumulative_sum_df = df.fillna(0).cumsum()
    
    # Plotting the cumulative sums
    fig, ax = plt.subplots()
    cumulative_sum_df.plot(kind='bar', ax=ax)
    
    # Setting the plot title and labels
    ax.set_title('Cumulative Sum per Column')
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Sum')
    
    # Adding a legend
    ax.legend(title='Columns')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return cumulative_sum_df, fig

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, np.nan, 4],
#     'B': [5, np.nan, np.nan, 8],
#     'C': [9, 10, 11, 12]
# })
# cumulative_sum_df, fig = task_func(df)