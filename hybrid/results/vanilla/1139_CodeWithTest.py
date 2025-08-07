import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

def task_func(data):
    # Ensure the data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data should be a pandas DataFrame.")
    
    # Check if the required columns are present
    if 'Hours' not in data.columns or 'Scores' not in data.columns:
        raise ValueError("DataFrame must contain 'Hours' and 'Scores' columns.")
    
    # Prepare the data
    X = data[['Hours']].values  # Independent variable
    y = data['Scores'].values   # Dependent variable
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)
    
    return mse
import unittest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
# Helper function
def calculate_mse(data):
    df = pd.DataFrame(data)
    X = df[['Hours']]
    y = df['Scores']
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Create and fit the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    # Make predictions
    predictions = model.predict(X_test)
    # Calculate MSE
    mse = np.mean((y_test - predictions) ** 2)
    
    return mse
class TestCases(unittest.TestCase):
    
    def test_with_typical_data(self):
        # Checks if MSE computed by task_func matches that computed by calculate_mse from a typical dataset
        data = {
            'Hours': [2.5, 5.1, 3.2, 8.5, 3.5],
            'Scores': [21, 47, 27, 75, 30],
        }
        mse_main = task_func(data)
        mse_helper = calculate_mse(data)
        self.assertIsInstance(mse_main, float)
        self.assertAlmostEqual(mse_main, mse_helper, places=5)
    def test_with_varied_data_size(self):
        # Verifies function handles different sizes of data inputs and results match between task_func and calculate_mse
        data = {
            'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2],
            'Scores': [21, 47, 27, 75, 30, 20, 88],
        }
        mse_main = task_func(data)
        mse_helper = calculate_mse(data)
        self.assertIsInstance(mse_main, float)
        self.assertAlmostEqual(mse_main, mse_helper, places=5)
    def test_with_minimum_data(self):
        # Tests the function's handling of minimal data to ensure MSE calculation is consistent between both methods
        data = {
            'Hours': [2.5, 2],
            'Scores': [21, 2],
        }
        mse_main = task_func(data)
        mse_helper = calculate_mse(data)
        self.assertIsInstance(mse_main, float)
        self.assertAlmostEqual(mse_main, mse_helper, places=5)
    def test_with_empty_data(self):
        # Ensures that providing empty data raises an error in both task_func and calculate_mse
        data = {'Hours': [], 'Scores': []}
        with self.assertRaises(ValueError):
            task_func(data)
        with self.assertRaises(ValueError):
            calculate_mse(data)
    def test_with_specific_known_value(self):
        # Asserts that MSE matches a known value and is consistent between task_func and calculate_mse
        data = {
            'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7],
            'Scores': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25],
        }
        mse_main = task_func(data)
        mse_helper = calculate_mse(data)
        self.assertAlmostEqual(mse_main, 6.182284986260905, places=5)
        self.assertAlmostEqual(mse_main, mse_helper, places=5)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)