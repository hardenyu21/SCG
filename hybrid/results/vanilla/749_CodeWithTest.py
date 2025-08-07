from sklearn.preprocessing import MinMaxScaler
import numpy as np

def task_func(myList):
    # Convert the list to a numpy array and reshape it for the scaler
    data = np.array(myList).reshape(-1, 1)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Fit the scaler to the data and transform it
    normalized_data = scaler.fit_transform(data)
    
    # Flatten the array to return a 1D array
    return normalized_data.flatten()

# Example usage:
# myList = [10, 20, 30, 40, 50]
# normalized_values = task_func(myList)
# print(normalized_values)
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_1(self):
        # Testing basic functionality
        input_data = [10, 20, 30, 40, 50]
        expected_output = np.array([0. , 0.25, 0.5 , 0.75, 1. ])
        np.testing.assert_array_almost_equal(task_func(input_data), expected_output, decimal=2)
    def test_2(self):
        # Testing with negative values
        input_data = [-50, -40, -30, -20, -10]
        expected_output = np.array([0. , 0.25, 0.5 , 0.75, 1. ])
        np.testing.assert_array_almost_equal(task_func(input_data), expected_output, decimal=2)
    def test_3(self):
        # Testing with mixed negative and positive values
        input_data = [-50, -25, 0, 25, 50]
        expected_output = np.array([0. , 0.25, 0.5 , 0.75, 1. ])
        np.testing.assert_array_almost_equal(task_func(input_data), expected_output, decimal=2)
    def test_4(self):
        # Testing with single value
        input_data = [100]
        expected_output = np.array([0.])
        np.testing.assert_array_almost_equal(task_func(input_data), expected_output, decimal=2)
    def test_5(self):
        # Testing with all zeros
        input_data = [0, 0, 0, 0, 0]
        expected_output = np.array([0., 0., 0., 0., 0.])
        np.testing.assert_array_almost_equal(task_func(input_data), expected_output, decimal=2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)