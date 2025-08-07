import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(d, target='z'):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)
    
    # Define the features and target variable
    X = df.drop(columns=[target])
    y = df[target]
    
    # Create and fit the Linear Regression model
    model = LinearRegression()
    model.fit(X, y)
    
    return model

# Example usage
data = [{'x': 4, 'y': 20, 'z': 10}, {'x': 5, 'y': 25, 'z': 15}, {'x': 6, 'y': 5, 'z': 20}]
model = task_func(data, target='y')
print(isinstance(model, LinearRegression))  # Should print: True