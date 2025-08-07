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
import unittest
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "group": ["A", "A", "A", "B", "B"],
            "date": pd.to_datetime(["2022-01-02", "2022-01-13", "2022-02-01", "2022-02-23", "2022-03-05"]),
            "value": [10, 20, 16, 31, 56],
        })
    def test_return_types(self):
        model, predictions, ax = task_func(self.df)
        self.assertIsInstance(model, LinearRegression)
        self.assertIsInstance(predictions, np.ndarray)
        self.assertEqual(predictions.shape, (self.df.shape[0],))
        self.assertEqual(ax.get_title(), 'Value vs Date (Linear Regression Prediction)')
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame({'a': [1, 2], 'b': [3, 4]}))
    def test_plot_labels(self):
        _, _, ax = task_func(self.df)
        self.assertEqual(ax.get_xlabel(), 'Date (ordinal)')
        self.assertEqual(ax.get_ylabel(), 'Value')
    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)