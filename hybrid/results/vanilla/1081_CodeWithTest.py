import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data=None):
    # Default dataset if no data is provided
    if data is None:
        data = {
            'Weight_String': ['70.5', '65.2', '80.0', '55.3', '72.1'],
            'Height': [170, 165, 180, 160, 175]
        }
    
    # Validate that all weights are strings
    if not all(isinstance(weight, str) for weight in data['Weight_String']):
        raise ValueError("All values in 'Weight_String' must be formatted as strings.")
    
    # Convert string-formatted weights to floats
    data['Weight'] = [float(weight) for weight in data['Weight_String']]
    
    # Create a DataFrame for easier plotting
    df = pd.DataFrame(data)
    
    # Plotting
    plt.figure(figsize=(8, 6))
    ax = sns.scatterplot(x='Weight', y='Height', data=df)
    ax.set_title("Weight vs Height")
    ax.set_xlabel("Weight (kg)")
    ax.set_ylabel("Height (cm)")
    
    # Show the plot
    plt.show()
    
    return ax
import unittest
import pandas as pd
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_default_data(self):
        """Test task_func with its default data."""
        result = task_func()
        self.assertIsInstance(result, Axes)
    def test_custom_data(self):
        """Test task_func with custom data."""
        custom_data = {
            "Weight_String": ["50.5", "55.7", "60.2"],
            "Height": [150, 155, 160],
        }
        result = task_func(custom_data)
        self.assertIsInstance(result, Axes)
    def test_incorrect_data_type(self):
        """Test task_func with incorrect data types in Weight_String."""
        incorrect_data = {
            "Weight_String": [
                60.5,
                65.7,
                70.2,
            ],  # Intentionally using floats instead of strings
            "Height": [160, 165, 170],
        }
        with self.assertRaises(ValueError):
            task_func(incorrect_data)
    def test_empty_data(self):
        """Test task_func with empty data."""
        empty_data = {"Weight_String": [], "Height": []}
        result = task_func(empty_data)
        self.assertIsInstance(result, Axes)
    def test_mismatched_data_length(self):
        """Test task_func with mismatched lengths of Weight_String and Height."""
        mismatched_data = {
            "Weight_String": ["60.5", "65.7"],  # Less weights than heights
            "Height": [160, 165, 170],
        }
        with self.assertRaises(ValueError):
            task_func(mismatched_data)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)