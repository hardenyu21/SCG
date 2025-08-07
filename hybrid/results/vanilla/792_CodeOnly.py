import heapq
from sklearn.linear_model import LinearRegression
import pandas as pd

def task_func(df, feature, target, n=10):
    # Check if the specified columns are in the DataFrame
    if feature not in df.columns or target not in df.columns:
        raise ValueError("Specified columns are not in the provided DataFrame.")
    
    # Extract the feature and target columns
    X = df[[feature]].values
    y = df[target].values
    
    # Fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict the target values
    y_pred = model.predict(X)
    
    # Calculate the residuals
    residuals = y - y_pred
    
    # Get the indices of the n largest residuals
    largest_residuals_indices = heapq.nlargest(n, range(len(residuals)), key=lambda i: abs(residuals[i]))
    
    return largest_residuals_indices, model

# Example usage
df = pd.DataFrame({
    'a': [1, 2, 3, 4, 5],
    'b': [1, 2, 3, 4, 5]
})
indices, model = task_func(df, 'a', 'b', n=3)
print(indices)  # Output: [0, 1, 2]
print(model)    # Output: LinearRegression()