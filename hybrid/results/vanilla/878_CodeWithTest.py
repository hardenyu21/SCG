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
import unittest
import pandas as pd
import numpy as np
from faker import Faker
from sklearn.ensemble import RandomForestRegressor
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.fake = Faker() 
    def test_case_1(self):
        # Simple test case
        data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'target': [10, 11, 12]}
        mse, model, df = task_func(data, 'target', random_state=2)
        self.assertAlmostEqual(mse, 1.537, delta=0.2)
        self.assertTrue(isinstance(model, RandomForestRegressor))
        pd.testing.assert_frame_equal(pd.DataFrame(data), df)
    def test_case_2(self):
        # Random test case with larger data
        np.random.seed(42)
        data = {'A': np.random.randint(0, 100), 'B': np.random.randint(0, 100), 'C': np.random.randint(0, 100), 'D': np.random.randint(0, 100) }
        data['target'] = np.random.randint(0, 100, size=(100,))
        mse, model, df = task_func(data, 'target', random_state=12)
        self.assertAlmostEqual(mse, 1012, delta=20)
        self.assertTrue(isinstance(model, RandomForestRegressor))
        pd.testing.assert_frame_equal(pd.DataFrame(data), df)
    def test_case_3(self):
        # Random test case with different test_size
        np.random.seed(42)
        data = {'A': np.random.randint(0, 100), 'B': np.random.randint(0, 100), 'C': np.random.randint(0, 100), 'D': np.random.randint(0, 100) }
        data['target'] = np.random.randint(0, 100, size=(100,))
        mse, model, df = task_func(data, 'target', test_size=0.3, random_state=12)
        self.assertAlmostEqual(mse, 1048, delta=20)
        self.assertTrue(isinstance(model, RandomForestRegressor))
        pd.testing.assert_frame_equal(pd.DataFrame(data), df)
    def test_case_4(self):
        # test working random state
        np.random.seed(42)
        data = {'A': np.random.randint(0, 100), 'B': np.random.randint(0, 100), 'C': np.random.randint(0, 100), 'D': np.random.randint(0, 100) }
        data['target'] = np.random.randint(0, 100, size=(100,))
        mse1, model, df = task_func(data, 'target', test_size=0.3, random_state=12)
        mse2, model, _ = task_func(data, 'target', test_size=0.3, random_state=12)
        self.assertAlmostEqual(mse1, mse2)
        pd.testing.assert_frame_equal(pd.DataFrame(data), df)
    def test_case_5(self):
        # Random test case with Faker-generated data
        self.fake.seed_instance(42)
        data = {'A': [self.fake.random_int(min=0, max=100) for _ in range(100)],
                             'B': [self.fake.random_int(min=0, max=100) for _ in range(100)],
                             'C': [self.fake.random_int(min=0, max=100) for _ in range(100)],
                             'D': [self.fake.random_int(min=0, max=100) for _ in range(100)],
                             'target': [self.fake.random_int(min=0, max=100) for _ in range(100)]}
        mse, model, df = task_func(data, 'target')
        self.assertAlmostEqual(mse, 844, delta=20)
        self.assertTrue(isinstance(model, RandomForestRegressor))
        pd.testing.assert_frame_equal(pd.DataFrame(data), df)
    def test_edge_case_empty_dataset(self):
        # Edge case: Empty dataset
        data = dict.fromkeys(['A', 'B', 'C', 'target'])
        with self.assertRaises(ValueError):
            task_func(data, 'target')
    def test_edge_case_very_small_dataset(self):
        # Edge case: Very small dataset
        data = {'A': [1], 'B': [2], 'C': [3], 'target': [4]}
        with self.assertRaises(ValueError):
            task_func(data, 'target')
    def test_edge_case_invalid_test_size(self):
        # Edge case: Invalid test size
        data = {'A': np.random.randint(0, 100), 'B': np.random.randint(0, 100), 'C': np.random.randint(0, 100), 'D': np.random.randint(0, 100) }
        data['target'] = np.random.randint(0, 100, size=(100,))
        with self.assertRaises(ValueError):
            task_func(data, 'target', test_size=-0.1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)