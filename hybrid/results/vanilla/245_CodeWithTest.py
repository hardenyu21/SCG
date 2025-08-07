import pandas as pd
import random
from scipy import stats

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    # Generate random floating-point numbers within the specified range
    data = [random.uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_data = [round(num, 3) for num in data]
    
    # Calculate statistical measures
    mean_value = sum(truncated_data) / len(truncated_data)
    median_value = pd.Series(truncated_data).median()
    mode_value = stats.mode(truncated_data).mode[0]
    
    # Return the results in a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }

# Example usage
result = task_func()
print(result)
import unittest
import random
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        random.seed(0)
        result = task_func()
        self.assertIn('mean', result)
        self.assertIn('median', result)
        self.assertIn('mode', result)
    def test_custom_range(self):
        random.seed(0)
        result = task_func(1000, 1.0, 5.0)
        self.assertGreaterEqual(result['mean'], 1.0)
        self.assertLessEqual(result['mean'], 5.0)
        self.assertGreaterEqual(result['median'], 1.0)
        self.assertLessEqual(result['median'], 5.0)
        self.assertGreaterEqual(result['mode'], 1.0)
        self.assertLessEqual(result['mode'], 5.0)
    def test_small_dataset(self):
        random.seed(0)
        result = task_func(10, 2.0, 2.0)
        self.assertEqual(result['mean'], 2.0)
        self.assertEqual(result['median'], 2.0)
        self.assertEqual(result['mode'], 2.0)
    def test_large_dataset(self):
        random.seed(0)
        result = task_func(10000, 0.0, 100.0)
        self.assertTrue(0.0 <= result['mean'] <= 100.0)
        self.assertTrue(0.0 <= result['median'] <= 100.0)
        self.assertTrue(0.0 <= result['mode'] <= 100.0)
    def test_single_value_range(self):
        random.seed(0)
        result = task_func(100, 5.0, 5.0)
        self.assertEqual(result['mean'], 5.0)
        self.assertEqual(result['median'], 5.0)
        self.assertEqual(result['mode'], 5.0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)