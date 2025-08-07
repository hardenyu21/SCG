import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'

def task_func(df, dict_mapping, plot_histogram=False):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    # Check if FEATURES and TARGET are in the DataFrame
    missing_features = [feature for feature in FEATURES if feature not in df.columns]
    if missing_features:
        raise ValueError(f"Missing features in DataFrame: {missing_features}")
    if TARGET not in df.columns:
        raise ValueError(f"Target column '{TARGET}' is not in the DataFrame.")
    
    # Replace values according to dict_mapping
    df_replaced = df.replace(dict_mapping)
    
    # Standardize specified features
    scaler = StandardScaler()
    df_replaced[FEATURES] = scaler.fit_transform(df_replaced[FEATURES])
    
    # Plot histogram of the target variable if requested
    ax = None
    if plot_histogram:
        ax = df_replaced[TARGET].hist()
        plt.title('Histogram of Target Variable')
        plt.xlabel(TARGET)
        plt.ylabel('Frequency')
        plt.show()
    
    return df_replaced, ax