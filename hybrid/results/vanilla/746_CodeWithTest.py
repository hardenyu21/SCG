import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target_column, target_values=None):
    # Validate inputs
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas DataFrame.")
    if not isinstance(target_column, str):
        raise ValueError("target_column must be a string.")
    if target_values is not None and not hasattr(target_values, '__iter__'):
        raise ValueError("target_values must be an array-like object.")
    
    # Replace elements not in target_values with zeros
    if target_values is not None:
        for column in df.columns:
            if column != target_column:
                df[column] = df[column].apply(lambda x: x if x in target_values else 0)
    
    # Prepare data for linear regression
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Train the Linear Regression model
    model = LinearRegression()
    model.fit(X, y)
    
    return model

# Example usage
rng = np.random.default_rng(seed=0)
df = pd.DataFrame(rng.integers(0, 100, size=(1000, 5)), columns=['A', 'B', 'C', 'D', 'predict'])
model = task_func(df, 'predict', target_values=[10, 20, 30, 40, 50])
print(model.coef_)
print(model.intercept_)
import unittest
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
class TestCases(unittest.TestCase):
    
    def lin_relation_1d(self, x, w0, w1):
        '''1-d linear relation for testing'''
        return w0 + w1*x
    
    def lin_relation_nd(self, row, w0, w):
        '''n-dimension linear relation for testing'''
        result = 0
        for i, x in enumerate(row.values):
            result += x * w[i]
        return w0 + result 
    def test_case_df(self):
        '''non DataFrame input'''
        df = 3
        target_column = 'test'
        self.assertRaises(Exception, task_func, df, target_column)
    def test_case_target_column(self):
        '''target column not in DataFrame'''
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.integers(0, 10, size=(5, 2)), columns=['test', 'python'])
        target_column = 'not'
        self.assertRaises(Exception, task_func, df, target_column)
    def test_case_empty_df(self):
        '''empty df as input'''
        df = pd.DataFrame(columns=['A', 'B'])
        target_column = 'A'
        self.assertRaises(Exception, task_func, df, target_column)
    
    def test_case_non_numeric_values(self):
        '''df not numeric'''
        data = {
            'A': [1, 2, 'test'],
            'B': [3, 3, 3]
        }
        df = pd.DataFrame(data)
        target_column = 'A'
        self.assertRaises(Exception, task_func, df, target_column)
    def test_case_1(self):
        '''prediction for one column'''
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.integers(0, 100, size=(1000, 1)), columns=list('A'))
        df['predict'] = df.apply(self.lin_relation_1d, args=(2, 4))
        model = task_func(df, 'predict')
        self.assertIsInstance(model, LinearRegression, "Returned value is not a LinearRegression model.")
        # make sure predictions work as expected
        pred = model.predict(df.drop('predict', axis=1))
        self.assertTrue(np.allclose(pred.tolist(), df['predict'].tolist()))
        # assert model params
        self.assertAlmostEqual(model.coef_[0], 4, places=4)
        self.assertAlmostEqual(model.intercept_, 2, places=4)
        
    def test_case_2(self):
        '''multiple column prediction'''
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.integers(0, 100, size=(1000, 5)), columns=list('ABCDE'))
        df['predict'] = df.apply(self.lin_relation_nd, axis=1, args=(4, [2.5, 5.8, 6, 4, -1]))
        model = task_func(df, 'predict')
        self.assertIsInstance(model, LinearRegression, "Returned value is not a LinearRegression model.")
        # make sure predictions work as expected
        pred = model.predict(df.drop('predict', axis=1))
        self.assertTrue(np.allclose(pred.tolist(), df['predict'].tolist()))
        # assert model params
        self.assertTrue(np.allclose(model.coef_, [2.5, 5.8, 6, 4, -1]))
        self.assertAlmostEqual(model.intercept_, 4, places=4)
    def test_case_3(self):
        '''test working target value --> with target value linear regression can't deliver good results'''
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.integers(0, 10, size=(1000, 1)), columns=list('A'))
        df['predict'] = df.apply(self.lin_relation_1d, args=(0, 2))
        model = task_func(df, 'predict', target_values=[1, 2, 4, 8])
        self.assertIsInstance(model, LinearRegression, "Returned value is not a LinearRegression model.")
        
        # make sure predictions work as expected
        masked_df = df.applymap(lambda x: x if x in [1, 2, 4, 8] else 0)
        masked_predict = masked_df['predict']
        pred = model.predict(masked_df.drop('predict', axis=1))
        self.assertTrue(not np.allclose(pred.tolist(), masked_predict.tolist()))
        # assert model params
        self.assertAlmostEqual(model.coef_[0], 0.2921456, places=2)
        self.assertAlmostEqual(model.intercept_, 0.81175, places=4)
        
    def test_case_4(self):
        '''df with constant values'''
        df = pd.DataFrame(np.full((10, 10), 3), columns=list('ABCDEFGHIJ'))
        model = task_func(df, 'J')
        self.assertTrue(all(coef == 0 for coef in model.coef_), "Model coefficients are not correct.")
        self.assertAlmostEqual(model.intercept_, 3, places=4)
    def test_case_5(self):
        '''df filled with random floats'''
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.random(size=(1000, 5)) * 10, columns=list('ABCDE'))
        df['predict'] = df.apply(self.lin_relation_nd, axis=1, args=(-1, [15, -4.8, 12, 40.2, -2]))
        model = task_func(df, 'predict')
        self.assertIsInstance(model, LinearRegression, "Returned value is not a LinearRegression model.")
        # make sure predictions work as expected
        pred = model.predict(df.drop('predict', axis=1))
        self.assertTrue(np.allclose(pred.tolist(), df['predict'].tolist()))
        # assert model params
        self.assertTrue(np.allclose(model.coef_, [15, -4.8, 12, 40.2, -2]))
        self.assertAlmostEqual(model.intercept_, -1, places=4)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)