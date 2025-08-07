import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    # Check if the column_to_remove exists in the DataFrame and drop it if it does
    if column_to_remove in df.columns:
        df = df.drop(columns=[column_to_remove])
    
    # Separate the target column from the features
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    return X_train, X_test, y_train, y_test