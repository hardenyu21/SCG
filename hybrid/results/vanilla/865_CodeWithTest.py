import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def task_func(data):
    # Unpack the data into separate lists
    items = [item for item, _, _ in data]
    counts = [count for _, count, _ in data]
    weights = [weight for _, _, weight in data]
    
    # Convert counts and weights to numpy arrays for processing
    counts_array = np.array(counts)
    weights_array = np.array(weights)
    
    # Normalize counts using z-score normalization
    normalized_counts = zscore(counts_array)
    
    # Normalize weights using min-max scaling
    scaler = MinMaxScaler()
    normalized_weights = scaler.fit_transform(weights_array.reshape(-1, 1)).flatten()
    
    # Create a DataFrame with the results
    df = pd.DataFrame({
        'Item': items,
        'Normalized Count': normalized_counts,
        'Normalized Weight': normalized_weights
    })
    
    return df
import unittest
import sys
sys.path.append('/mnt/data/testing')
import pandas as pd
import numpy as np
from faker import Faker
class TestCases(unittest.TestCase):
    def setUp(self):
        # This method will be used to set up any variables or conditions that are common across all test cases.
        self.tolerance = 1e-3  # Tolerance level for comparing floating point numbers
    def test_case_1(self):
        # Testing with basic input.
        data = [('A', 100, 0.5), ('B', 200, 0.6), ('C', 150, 0.7)]
        result = task_func(data)
        expected_items = ['A', 'B', 'C']
        # Check if all items are present and in the correct order
        self.assertEqual(list(result['Item']), expected_items)
        # Check if normalization is within the expected range (0-1 for min-max, mean=0 for z-score)
        self.assertTrue(result['Normalized Weight'].min() >= 0)
        self.assertTrue(result['Normalized Weight'].max() <= 1)
        self.assertTrue(abs(result['Normalized Count'].mean()) <= self.tolerance)
    def test_case_2(self):
        # Testing with negative counts and weights.
        data = [('A', -100, -0.5), ('B', -200, -0.1), ('C', -150, -0.2)]
        result = task_func(data)
        
        # Even with negative inputs, normalization should stay within the expected range
        self.assertTrue(result['Normalized Weight'].min() >= 0)
        self.assertTrue(result['Normalized Weight'].max() <= 1)
        self.assertTrue(abs(result['Normalized Count'].mean()) <= self.tolerance)
    def test_case_3(self):
        # Testing with identical counts and weights.
        data = [('A', 100, 0.5), ('B', 100, 0.5), ('C', 100, 0.5)]
        result = task_func(data)
        
        # If all counts and weights are identical, normalization should result in equality and nan for z score
        self.assertTrue(all(result['Normalized Weight'] == 0.0))
        self.assertTrue(all(result['Normalized Count'].isna()))
    def test_case_4(self):
        # Testing with large numbers.
        data = [('A', 1000000, 0.5), ('B', 2000000, 0.6), ('C', 1500000, 0.7)]
        result = task_func(data)
        # Even with large numbers, the properties of normalized data should hold
        self.assertTrue(result['Normalized Weight'].min() >= 0)
        self.assertTrue(result['Normalized Weight'].max() <= 1)
        self.assertTrue(abs(result['Normalized Count'].mean()) <= self.tolerance)
    def test_case_5(self):
        # Testing with a single data point.
        data = [('A', 100, 0.5)]
        result = task_func(data)
        # With a single data point, the normalized values should default to certain values
        self.assertEqual(result['Normalized Weight'][0], 0.0)
        self.assertTrue(result['Normalized Count'].isna()[0])
    def test_return_value(self):
        # test actual return values
        data = [('A', 10, 0.5), ('B', -1234, 12.6), ('C', 999,3, 0.7)]
        result = task_func(data)
        expected = pd.DataFrame({
            'Item': {0: 'A', 1: 'B', 2: 'C'},
            'Normalized Count': {0: 0.09303876818248032,
            1: -1.2686109685117022,
            2: 1.175572200329222},
            'Normalized Weight': {0: 0.0, 1: 1.0, 2: 0.2066115702479339}
        })
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)
    def test_large_data_amount(self):
        fake = Faker()
        num = 1000
        name = [fake.first_name() for _ in range(num)]
        count = [fake.random_int() for _ in range(num)]
        weight = [fake.random_number(digits=2)/80 for _ in range(num)]
        data = list(zip(name, count, weight))
        result = task_func(data)
        items, counts, weights = zip(*data)
        
        # Normalizing the counts and weights
        counts_normalized = zscore(counts)
        scaler = MinMaxScaler()
        weights_normalized = scaler.fit_transform(np.array(weights).reshape(-1, 1)).flatten()
        # Creating a DataFrame with the normalized data
        expected = pd.DataFrame({
            'Item': items,
            'Normalized Count': counts_normalized,
            'Normalized Weight': weights_normalized
        })
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)