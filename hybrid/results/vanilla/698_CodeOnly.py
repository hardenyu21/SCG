import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df):
    # Separate the target column from the features
    X = df.drop(columns=['target'])
    y = df['target']
    
    # Split the data into training and test sets with a 70%:30% ratio
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Return the four resulting DataFrames
    return X_train, X_test, y_train, y_test