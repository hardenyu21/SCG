import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Constants
FEATURES = ['feature ' + str(i) for i in range(1, 11)]
TARGET = 'target'

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if the DataFrame contains the required columns
    if not all(feature in df.columns for feature in FEATURES) or TARGET not in df.columns:
        raise ValueError("DataFrame must contain the specified features and target column.")
    
    # Split the data into features and target
    X = df[FEATURES]
    y = df[TARGET]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model