import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np

def task_func(file_path='arena.csv', target_column='Index', seed=42):
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The specified file_path '{file_path}' does not lead to a valid file.")
    
    # Load the data from the CSV file
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error reading the CSV file: {e}")
    
    # Check if the target column exists
    if target_column not in data.columns:
        raise ValueError(f"The specified target_column '{target_column}' is not found in the CSV file's columns.")
    
    # Drop rows with any NaN values
    data = data.dropna()
    
    # Check for NaN, infinity, or values too large for dtype('float32')
    if data.isin([np.nan, np.inf, -np.inf]).any().any() or (data.abs() > np.finfo(np.float32).max).any().any():
        raise ValueError("The input data contains NaN, infinity or a value too large for dtype('float32').")
    
    # Separate features and target variable
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    # Train a random forest model
    rf_model = RandomForestClassifier(random_state=seed)
    rf_model.fit(X, y)
    
    # Get feature importances
    importances = rf_model.feature_importances_
    
    # Plot feature importances
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=importances, y=X.columns)
    ax.set_title('Feature Importances')
    ax.set_xlabel('Importance')
    ax.set_ylabel('Features')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax, importances