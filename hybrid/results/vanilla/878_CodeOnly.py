import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def task_func(data, target, test_size=0.2, random_state=None):
    # Convert the input data into a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The input DataFrame is empty.")
    
    # Check if the target column is in the DataFrame
    if target not in df.columns:
        raise ValueError(f"The target column '{target}' is not in the DataFrame.")
    
    # Split the data into features and target
    X = df.drop(columns=[target])
    y = df[target]
    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Initialize and train the RandomForestRegressor
    model = RandomForestRegressor(random_state=random_state)
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)
    
    # Return the MSE, the trained model, and the DataFrame
    return mse, model, df