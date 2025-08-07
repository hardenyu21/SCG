import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    # Check if the input is 2D
    if records.ndim != 2:
        raise ValueError("Input records must be 2D.")
    
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Shuffle the features
    num_features = records.shape[1]
    shuffled_indices = np.random.permutation(num_features)
    shuffled_records = records[:, shuffled_indices]
    
    # Normalize the values
    scaler = StandardScaler()
    normalized_records = scaler.fit_transform(shuffled_records)
    
    # Create shuffled feature names
    feature_names = [f"f{i+1}" for i in range(num_features)]
    np.random.shuffle(feature_names)
    
    # Convert to DataFrame
    df = pd.DataFrame(normalized_records, columns=feature_names)
    
    return df
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        self.data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.expected_shape = (2, 5)
    def test_case_1(self):
        # Test basic shape and columns
        df = task_func(self.data, random_seed=1)
        self.assertEqual(df.shape, self.expected_shape)
        self.assertTrue(set(df.columns) == set(["f1", "f2", "f3", "f4", "f5"]))
        # assert last row values
        self.assertEqual(df.iloc[-1].tolist(), [1.0, 1.0, 1.0, 1.0, 1.0])
        self.assertEqual(df.iloc[0].tolist(), [-1.0, -1.0, -1.0, -1.0, -1.0])
        
    def test_case_2(self):
        # Test normalization
        df = task_func(self.data, random_seed=2)
        np.testing.assert_array_almost_equal(
            df.mean(axis=0), np.zeros(self.expected_shape[1]), decimal=5
        )
        np.testing.assert_array_almost_equal(
            df.std(axis=0, ddof=0), np.ones(self.expected_shape[1]), decimal=5
        )
        
    def test_case_3(self):
        # Test random seed effect
        df1 = task_func(self.data, random_seed=3)
        df2 = task_func(self.data, random_seed=3)
        pd.testing.assert_frame_equal(df1, df2)
    def test_case_4(self):
        # Test handling invalid inputs
        with self.assertRaises(ValueError):
            task_func(np.array([1, 2, 3]), random_seed=4)
        with self.assertRaises(ValueError):
            task_func(np.array([[1, 2, 3], [4, 5]], dtype=object), random_seed=4)
    def test_case_5(self):
        # Test handling zero variance
        data = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
        df = task_func(data, random_seed=42)
        # In cases of zero variance, StandardScaler will set values to 0
        np.testing.assert_array_equal(df.values, np.zeros(data.shape))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)