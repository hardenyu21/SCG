import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(df, col_a='A', col_b='B', col_c='C', seed=None):
    # Check if the DataFrame is empty
    if df.empty:
        return None, None
    
    # Check if the specified columns are in the DataFrame
    if not all(col in df.columns for col in [col_a, col_b, col_c]):
        return None, None
    
    # Check if the specified columns contain numeric data
    if not pd.api.types.is_numeric_dtype(df[col_a]) or not pd.api.types.is_numeric_dtype(df[col_b]) or not pd.api.types.is_numeric_dtype(df[col_c]):
        return None, None
    
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df[col_b] > 50) & (df[col_c] == 900)]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None, None
    
    # Prepare the data for training
    X = filtered_df[[col_a]]
    y = filtered_df[col_b]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    
    # Train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Generate predictions on the test set
    predictions = model.predict(X_test)
    
    return predictions, model