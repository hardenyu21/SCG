from random import sample
import seaborn as sns
import pandas as pd

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Remove rows from a dataframe based on values of multiple columns, and then create n random joint plots
    of two columns against each other if the DataFrame is not empty.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list): A list of tuples where each tuple contains a column name and a value to filter out.
    n_plots (int): The number of random joint plots to generate.

    Returns:
    tuple: A tuple containing:
        DataFrame: The modified DataFrame.
        list: A list of generated joint plots (sns.JointGrid objects) if the DataFrame is not empty, otherwise an empty list.
    """
    # Remove rows based on the tuples
    for col, value in tuples:
        if col in df.columns:
            df = df[df[col] != value]

    # Check if the DataFrame is empty
    if df.empty:
        return df, []

    # Generate n random joint plots
    joint_plots = []
    for _ in range(n_plots):
        # Randomly select two columns from the DataFrame
        col1, col2 = sample(COLUMNS, 2)
        if col1 in df.columns and col2 in df.columns:
            # Create a joint plot
            joint_plot = sns.jointplot(data=df, x=col1, y=col2)
            joint_plots.append(joint_plot)

    return df, joint_plots