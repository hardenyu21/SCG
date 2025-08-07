import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def task_func(df):
    # Validate input DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    if 'date' not in df.columns or 'value' not in df.columns:
        raise ValueError("DataFrame must contain 'date' and 'value' columns.")
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        raise ValueError("The 'date' column must be in datetime format.")
    
    # Convert 'date' to ordinal
    df['date_ordinal'] = df['date'].apply(lambda x: x.toordinal())
    
    # Prepare data for linear regression
    X = df[['date_ordinal']]
    y = df['value']
    
    # Perform linear regression
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    
    # Plot the original and predicted values
    fig, ax = plt.subplots()
    ax.scatter(df['date_ordinal'], y, color='blue', label='Original Values')
    ax.plot(df['date_ordinal'], predictions, color='red', label='Predicted Values')
    
    # Set plot labels and title
    ax.set_title('Value vs Date (Linear Regression Prediction)')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.legend()
    
    # Return the model, predictions, and Axes object
    return model, predictions, ax