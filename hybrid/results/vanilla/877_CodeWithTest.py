import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    # Check if the input is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data is not a DataFrame.")
    
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("Input data is empty.")
    
    # Check if all columns in the DataFrame are numeric
    if not all(data.dtypes.apply(lambda x: pd.api.types.is_numeric_dtype(x))):
        raise ValueError("Input data contains non-numeric data.")
    
    # Check if n_components is greater than the number of columns
    if n_components > data.shape[1]:
        raise ValueError("n_components is greater than the number of columns in the data.")
    
    # Scale the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    # Apply PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(scaled_data)
    
    # Create a new DataFrame with the principal components
    columns = [f'PC{i+1}' for i in range(n_components)]
    result_df = pd.DataFrame(principal_components, columns=columns)
    
    return result_df
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.data_small = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [6, 7, 8, 9, 10],
            'C': [11, 12, 13, 14, 15],
            'D': [16, 17, 18, 19, 20]
        })
        self.data_large = pd.DataFrame(np.random.randint(0, 100, size=(1000, 50)))
    def test_basic_functionality(self):
        result = task_func(self.data_small)
        self.assertEqual(result.shape, (5, 2))
    def test_varying_components(self):
        for components in [1, 3, 4]:
            result = task_func(self.data_small, n_components=components)
            self.assertEqual(result.shape, (5, components))
    def test_large_dataset(self):
        result = task_func(self.data_large, n_components=10)
        self.assertEqual(result.shape, (1000, 10))
    def test_invalid_input(self):
        data_invalid = self.data_small.copy()
        data_invalid['E'] = ['non-numeric'] * 5
        with self.assertRaises(ValueError):
            task_func(data_invalid)
    def test_empty_dataframe(self):
        data_empty = pd.DataFrame()
        with self.assertRaises(ValueError):
            task_func(data_empty)
    def test_known_input(self):
        expected = np.array([
            [ 2.82842712e+00,  3.64856517e-16],
            [ 1.41421356e+00, -1.21618839e-16],
            [-0.00000000e+00,  0.00000000e+00],
            [-1.41421356e+00,  1.21618839e-16],
            [-2.82842712e+00,  2.43237678e-16]
       ])
        flipped = -expected
        transformed_data = task_func(self.data_small, n_components=2).values
        self.assertTrue(
            np.allclose(transformed_data, expected, atol=0.1) or np.allclose(transformed_data, flipped, atol=0.1),
            "The PCA results do not match the expected values considering possible sign flips."
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)