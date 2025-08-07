import numpy as np
from scipy.stats import norm

def task_func(data: np.ndarray, threshold: float = 2.0) -> list:
    # Calculate the mean and standard deviation of the data
    mean = np.mean(data)
    std_dev = np.std(data)
    
    # Calculate the variance
    var = std_dev ** 2
    
    # If the standard deviation is 0, return an empty list for outliers
    if std_dev == 0:
        return [], mean, var
    
    # Calculate the Z scores for each data point
    z_scores = (data - mean) / std_dev
    
    # Find the indices of outliers where the absolute Z score is greater than the threshold
    outliers = [index for index, z_score in enumerate(z_scores) if abs(z_score) > threshold]
    
    return outliers, mean, var

# Example usage
data = np.array([-10, 3, 5, 5, 5, 5, 5, 7, 20])
outliers, mean, var = task_func(data, threshold=4)
print(outliers)  # Output: []
print(mean)       # Output: 5.0
print(var)        # Output: 50.888888888888886
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data = np.array([1, 2, 3, 4, 5, 6, 100])
        result, mean, var = task_func(data)
        self.assertEqual(result, [6])
        self.assertAlmostEqual(mean, 17.2, delta=0.1)
        self.assertAlmostEqual(var, 1142.78, delta=0.1)
    def test_case_2(self):
        data = np.array([1, 2, 3, 4, 5, 6, 7])
        result, mean, var = task_func(data)
        self.assertEqual(result, [])
        self.assertAlmostEqual(mean, 4, delta=0.1)
        self.assertAlmostEqual(var, 4, delta=0.1)
    def test_case_3(self):
        data = np.array([5, 5, 5, 5, 5])
        result, mean, var = task_func(data)
        self.assertEqual(result, [])
        self.assertAlmostEqual(mean, 5, delta=0.1)
        self.assertAlmostEqual(var, 0, delta=0.1)
    def test_case_4(self):
        from faker import Faker
        fake = Faker()
        fake.seed_instance(12)
        data = np.array([fake.random_int(min=0, max=100) for _ in range(10000)])
        result, mean, var = task_func(data)
        self.assertEqual(len(result), 0)
        self.assertAlmostEqual(mean, 50.28, delta=0.1)
        self.assertAlmostEqual(var, 842.86, delta=0.1)
    def test_case_5(self):
        data = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 50])
        result, mean, var = task_func(data, threshold=0.5)
        self.assertEqual(result, [0, 1, 2, 11])
        self.assertAlmostEqual(mean, 4.17, delta=0.1)
        self.assertAlmostEqual(var, 200.14, delta=0.1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)