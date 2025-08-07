import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate a single feature dataset
    X = np.random.rand(num_samples, 1)
    
    # Define a linear relation with some true parameters
    true_slope = 2.5
    true_intercept = 1.0
    
    # Compute the target variable with added Gaussian noise
    y = true_slope * X + true_intercept + noise_strength * np.random.randn(num_samples, 1)
    
    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_seed)
    
    # Check if the test set size is smaller than 2
    if len(X_test) < 2:
        raise ValueError("Test set size is smaller than 2.")
    
    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Calculate the R-squared score on the test set
    r_squared = model.score(X_test, y_test)
    
    # Return the R-squared score and the trained model
    return r_squared, model
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        'rng reproducability'
        r_squared1, _ = task_func(random_seed=42)
        r_squared2, _ = task_func(random_seed=42)
        self.assertEqual(r_squared1, r_squared2)
    def test_case_2(self):
        'default params'
        r_squared, model = task_func(num_samples=1000)
        self.assertTrue(0 <= r_squared <= 1)
        self.assertTrue(isinstance(model, LinearRegression))
        
    def test_case_3(self):
        'noise strength'
        r_squared, model = task_func(noise_strength=0, random_seed=24)
        self.assertAlmostEqual(r_squared, 1)
        self.assertTrue(isinstance(model, LinearRegression))
    def test_case_4(self):
        'test set too small'
        self.assertRaises(Exception, task_func, {'num_samples': 10, 'test_size': 0.1})
    def test_case_5(self):
        r_squared, model = task_func(num_samples=1000, noise_strength=1000, random_seed=24, test_size=0.3)
        self.assertTrue(r_squared < 0.2)
        self.assertTrue(isinstance(model, LinearRegression))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)