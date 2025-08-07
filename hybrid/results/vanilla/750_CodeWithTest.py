import pandas as pd
import statsmodels.api as sm

def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    # Check if the DataFrame is empty
    if df.empty:
        return None
    
    # Filter the DataFrame based on the given conditions
    filtered_df = df[(df[columns[1]] > height) & (df[columns[2]] < weight)]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None
    
    # Define the dependent variable (y) and independent variables (X)
    y = filtered_df[columns[0]]
    X = filtered_df[columns[1:]]
    
    # Add a constant to the independent variables
    X = sm.add_constant(X)
    
    # Perform OLS regression
    model = sm.OLS(y, X).fit()
    
    return model
import unittest
import numpy as np
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)  # Set a seed for reproducibility
    def test_case_1(self):
        # Test with a DataFrame of random values
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper) 
        self.assertEqual(results.params.index.to_list(), ['const', 'Height', 'Weight']) # There should be 3 parameters: const, Height, Weight
    def test_case_2(self):
        # Test with a DataFrame where no rows match the condition
        df = pd.DataFrame(np.random.randint(30,40,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsNone(results) # There should be no regression result since no rows match the condition
    def test_case_3(self):
        # Test with a DataFrame where all rows match the condition
        df = pd.DataFrame(np.random.randint(60,80,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper) 
        self.assertEqual(results.params.index.to_list(), ['const', 'Height', 'Weight']) # There should be 3 parameters: const, Height, Weight
    def test_case_4(self):
        # Test with a DataFrame with different column names
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 3)), columns=['Years', 'Size', 'Mass'])
        results = task_func(df, 50, 70, columns=['Years', 'Size', 'Mass'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper) 
        self.assertEqual(results.params.index.to_list(), ['const', 'Size', 'Mass']) # There should be 3 parameters: const, Height, Weight
    def test_case_5(self):
        # Test with an empty DataFrame
        df = pd.DataFrame(columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsNone(results) # There should be no regression result since DataFrame is empty


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)