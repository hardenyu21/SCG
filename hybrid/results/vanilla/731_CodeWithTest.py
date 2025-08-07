import pickle
import os
from sklearn.datasets import make_classification

# Constants
FILE_NAME = 'save.pkl'
DATA, TARGET = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)

def task_func(data, target):
    # Save the dataset to a pickle file
    with open(FILE_NAME, 'wb') as file:
        pickle.dump((data, target), file)
    
    # Read the dataset back from the pickle file
    with open(FILE_NAME, 'rb') as file:
        loaded_data, loaded_target = pickle.load(file)
    
    # Return the loaded data and target
    return loaded_data, loaded_target

# Example usage
loaded_data, loaded_target = task_func(DATA, TARGET)
print("Loaded Data Shape:", loaded_data.shape)
print("Loaded Target Shape:", loaded_target.shape)
from sklearn.datasets import make_classification
import numpy as np
import unittest
import sys
sys.path.append("/mnt/data")
# Defining the test function
class TestCases(unittest.TestCase):
    def test_save_and_load_data(self):
        data, target = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data))
        self.assertTrue(np.array_equal(target, loaded_target))
    
    def test_save_and_load_empty_data(self):
        data, target = np.array([]), np.array([])
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data))
        self.assertTrue(np.array_equal(target, loaded_target))
    
    def test_save_and_load_single_element_data(self):
        data, target = np.array([5]), np.array([1])
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data))
        self.assertTrue(np.array_equal(target, loaded_target))
    
    def test_save_and_load_large_data(self):
        data, target = make_classification(n_samples=1000, n_features=50, n_informative=5, n_redundant=25, n_classes=3, random_state=2)
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data))
        self.assertTrue(np.array_equal(target, loaded_target))
    
    def test_save_and_load_random_data(self):
        data, target = np.random.rand(50, 5), np.random.randint(0, 2, 50)
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data))
        self.assertTrue(np.array_equal(target, loaded_target))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)