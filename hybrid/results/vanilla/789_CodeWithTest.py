import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Constants
ARRAY_LENGTH = 10

def task_func():
    # Generate a random array
    random_array = np.random.rand(ARRAY_LENGTH)
    
    # Reshape the array to fit the scaler's input requirements
    random_array_reshaped = random_array.reshape(-1, 1)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Fit and transform the array
    scaled_array_reshaped = scaler.fit_transform(random_array_reshaped)
    
    # Reshape back to the original array shape
    scaled_array = scaled_array_reshaped.flatten()
    
    return scaled_array

# Example usage
scaled_array = task_func()
print(scaled_array)
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        self.result = task_func()  # Call the function once to use in multiple tests if needed
    def test_normal_functionality(self):
        """Testing the basic functionality and shape of the output array."""
        self.assertEqual(self.result.shape, (10, 1), "Array shape should be (10, 1)")
        self.assertTrue((self.result >= 0).all() and (self.result <= 1).all(), "Array values should be in the range [0, 1]")
    def test_output_values(self):
        """ Ensuring that the scaling works as expected. """
        expected_min = 0
        expected_max = 1
        actual_min = np.min(self.result)
        actual_max = np.max(self.result)
        self.assertEqual(actual_min, expected_min, "The minimum of the scaled array should be 0")
        self.assertAlmostEqual(actual_max, expected_max, places=15, msg="The maximum of the scaled array should be very close to 1")
    def test_no_arguments(self):
        """Ensure that no arguments are passed to the function."""
        with self.assertRaises(TypeError):
            task_func(10)  # This should fail since the function expects no arguments
    def test_unchanging_output(self):
        """Test if multiple calls to the function give the same result due to seed setting."""
        second_result = task_func()
        np.testing.assert_array_equal(self.result, second_result, "Results should be the same on every call due to fixed seed.")
    def test_distribution_of_values(self):
        """Test that the distribution of scaled values is neither constant nor degenerate (not all values the same)."""
        unique_values = np.unique(self.result)
        self.assertTrue(len(unique_values) > 1, "There should be more than one unique scaled value to confirm distribution.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)