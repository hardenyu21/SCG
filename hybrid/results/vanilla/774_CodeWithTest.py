import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

def task_func(num_samples=100, n_estimators=100, random_seed=None, cv=5):
    # Check if the condition num_samples / cv < 2 is met
    if num_samples / cv < 2:
        raise ValueError("num_samples / cv must be at least 2.")
    
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate the dataset
    X = np.random.randn(num_samples, 5)  # 5 features
    noise = np.random.randn(num_samples)
    y = np.sum(X, axis=1) + noise  # Target variable
    
    # Initialize the RandomForestRegressor model
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_seed)
    
    # Perform cross-validation
    scores = cross_val_score(model, X, y, cv=cv, scoring='r2')
    
    # Calculate the mean cross-validation score
    mean_score = np.mean(scores)
    
    # Return the mean score and the trained model
    return mean_score, model

# Example usage
results = task_func(random_seed=1)
print(results)
import unittest
class TestCases(unittest.TestCase):
    def test_case_rng(self):
        'rng reproducability'
        result1, _ = task_func(random_seed=42)
        result2, _ = task_func(random_seed=42)
        self.assertAlmostEqual(result1, result2)
    def test_case_1(self):
        'default params'
        result, model = task_func(random_seed=1)
        self.assertAlmostEqual(result, 0.47332912782858)
        self.assertTrue(isinstance(model, RandomForestRegressor))
    def test_case_2(self):
        'random outcome with distinct seeds'
        result1, _ = task_func(random_seed=2)
        result2, _ = task_func(random_seed=3)
        self.assertFalse(result1 == result2)
    def test_case_3(self):
        result, model = task_func(random_seed=2, cv=2, n_estimators=2)
        self.assertAlmostEqual(result, 0.2316988319594362)
        self.assertTrue(isinstance(model, RandomForestRegressor))
    def test_case_4(self):
        'test exception'
        self.assertRaises(Exception,
                          task_func,
                          {'random_seed': 223, 'cv': 3,
                           'n_estimators': 100, 'num_samples': 4}
                          )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)