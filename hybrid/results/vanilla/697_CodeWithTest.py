import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Extract the feature and target columns
    X = df[['feature']].values  # Assuming 'feature' is the column name for the independent variable
    y = df['value'].values      # Assuming 'value' is the column name for the dependent variable

    # Initialize the Linear Regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(X, y)

    # Get the coefficients and intercept
    coefficients = model.coef_
    intercept = model.intercept_

    # Create a result dictionary
    result = {
        'coefficients': coefficients[0],  # Since we have only one feature, we take the first element
        'intercept': intercept
    }

    return result
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'feature': np.random.rand(100), 'value': np.random.rand(100)})
        coefficients = task_func(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
    def test_case_2(self):
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [1, 2, 3, 4, 5]})
        coefficients = task_func(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
        self.assertAlmostEqual(coefficients['coefficients'][0][0], 1.0)
        self.assertAlmostEqual(coefficients['intercept'][0], 0.0)
    def test_case_3(self):
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [2, 4, 6, 8, 10]})
        coefficients = task_func(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
        self.assertAlmostEqual(coefficients['coefficients'][0][0], 2.0)
        self.assertAlmostEqual(coefficients['intercept'][0], 0.0)
    def test_case_4(self):
        df = pd.DataFrame({'feature': [0, 0, 0, 0, 0], 'value': [1, 2, 3, 4, 5]})
        coefficients = task_func(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
        self.assertAlmostEqual(coefficients['coefficients'][0][0], 0.0)
        self.assertAlmostEqual(coefficients['intercept'][0], 3.0)
    def test_case_5(self):
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [0, 0, 0, 0, 0]})
        coefficients = task_func(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
        self.assertAlmostEqual(coefficients['coefficients'][0][0], 0.0)
        self.assertAlmostEqual(coefficients['intercept'][0], 0.0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)