import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

ROWS = 100
COLUMNS = ['X', 'Y']

def task_func(df):
    # Ensure the DataFrame has the correct columns
    if not all(col in df.columns for col in COLUMNS):
        raise ValueError(f"DataFrame must contain columns: {COLUMNS}")
    
    # Prepare the data for linear regression
    X = df[['X']].values  # Features
    y = df['Y'].values    # Target variable
    
    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    return model

# Example usage:
# df = pd.DataFrame(np.random.rand(ROWS, len(COLUMNS)), columns=COLUMNS)
# model = task_func(df)
# print(model.coef_, model.intercept_)
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
    
    def test_case_2(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
    def test_case_3(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
    def test_case_4(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) is not None)
    def test_case_5(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) >= 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)