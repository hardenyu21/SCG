import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def task_func(num_samples=1000, k=5, d=2, random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random numbers from a Gaussian normal distribution
    original_data = np.random.randn(num_samples, 1)
    
    # Apply a linear transformation: y = kx + d
    transformed_data = k * original_data + d
    
    # Standardize the transformed data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(transformed_data)
    
    # Calculate the mean squared error between the original and standardized data
    mse = mean_squared_error(original_data, standardized_data)
    
    return mse

# Example usage
mse = task_func()
print(mse)  # Output will vary depending on the random seed and parameters

mse = task_func(k=1, d=0)
print(mse)  # Output will vary depending on the random seed and parameters
import unittest
class TestCases(unittest.TestCase):
    def test_case_rng(self):
        'test rng reproducability'
        result1 = task_func(random_seed=23)
        result2 = task_func(random_seed=23)
        self.assertEqual(result1, result2)
    def test_case_1(self):
        'low mse + mse decreasing with num_samples'
        result1 = task_func(num_samples=1000000, k=1, d=0, random_seed=1)
        self.assertAlmostEqual(result1, 0, places=5)
        result2 = task_func(num_samples=1000, k=1, d=0, random_seed=1)
        result3 = task_func(num_samples=10000, k=1, d=0, random_seed=1)
        self.assertTrue(result2 > result3)
    def test_case_2(self):
        'deterministic mse'
        result = task_func(num_samples=100, k=0, d=10, random_seed=42)
        self.assertAlmostEqual(result, 100, places=5)
    def test_case_3(self):
        'random input'
        result = task_func(num_samples=10000, k=10, d=0, random_seed=42)
        self.assertAlmostEqual(result, 81.61581766096013, places=5)
    def test_case_5(self):
        'floats'
        result = task_func(num_samples=340, k=-3.4, d=123.4, random_seed=42)
        self.assertAlmostEqual(result, 15220.804873417765, places=5)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)