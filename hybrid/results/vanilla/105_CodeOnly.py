import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df):
    # Check if the dataframe is empty
    if df.empty:
        raise ValueError("The dataframe is empty.")
    
    # Check if the required columns are present
    required_columns = ['date']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"The following required columns are missing: {missing_columns}.")
    
    # Check if the 'date' column is in datetime format
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        raise ValueError("The 'date' column is not in datetime format.")
    
    # Convert the 'date' column to an ordinal format
    df['date_ordinal'] = df['date'].apply(lambda x: x.toordinal())
    
    # Create a correlation matrix
    corr_matrix = df.corr()
    
    # Generate a pair plot
    pair_plot = sns.pairplot(df)
    
    # Create a heatmap for the correlation matrix
    plt.figure(figsize=(10, 8))
    corr_matrix_heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    
    # Return the figure and PairGrid objects
    return corr_matrix_heatmap.get_figure(), pair_plot

# Example usage:
# df = pd.DataFrame({
#     'date': pd.date_range(start='1/1/2020', periods=10),
#     'value1': range(10),
#     'value2': range(10, 20)
# })
# fig, pair_grid = task_func(df)
# plt.show()