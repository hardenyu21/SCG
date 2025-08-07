import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42, save_path=None):
    try:
        # Load the Boston Housing dataset
        raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
        # The last column is the target variable, so we separate it
        X = raw_df.iloc[:, :-1]
        y = raw_df.iloc[:, -1]
        # Assign column names
        X.columns = [
            "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX",
            "PTRATIO", "B", "LSTAT"
        ]
        # Combine features and target for correlation
        df = pd.concat([X, y], axis=1)
        df.columns = X.columns.tolist() + ["MEDV"]

        # Compute the correlation matrix
        corr_matrix = df.corr()

        # Set up the matplotlib figure
        plt.figure(figsize=(12, 10))

        # Draw the heatmap with the mask and correct aspect ratio
        ax = sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)

        # Save the plot if a path is provided
        if save_path:
            plt.savefig(save_path)

        # Return the Axes object
        return ax

    except Exception as e:
        raise ValueError("An error occurred in generating or saving the plot.") from e

# Example usage:
# ax = task_func(save_path="boston_heatmap.png")
# plt.show()