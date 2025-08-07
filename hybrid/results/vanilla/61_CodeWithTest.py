import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    # Extract values associated with the key 'from_user'
    x_values = [d['from_user'] for d in result if 'from_user' in d]
    
    # Calculate square root values and round them to 2 decimals
    sqrt_values = np.round(np.sqrt(x_values), 2)
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x_values, sqrt_values, marker='o')
    
    # Annotate the plot with the current date and time
    current_time = datetime.now().strftime(TIME_FORMAT)
    ax.annotate(f'Generated on: {current_time}', xy=(0.05, 0.95), xycoords='axes fraction',
                fontsize=10, ha='left', va='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))
    
    # Set plot title and labels
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    
    # Show the plot
    plt.grid(True)
    plt.show()
    
    # Return the square root values as a numpy array and the plot axes
    return sqrt_values, ax
import unittest
import matplotlib
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        # Input 1: Normal case with 2 dictionaries with 'from_user' keys.
        data = [
            {"key_1": 7, "key_2": 4, "from_user": 16},
            {"key_1": 2, "key_2": 4, "from_user": 9},
        ]
        square_roots, ax = task_func(data)
        self.assertEqual(ax.get_title(), PLOT_TITLE)
        self.assertEqual(ax.get_xlabel(), X_LABEL)
        self.assertEqual(ax.get_ylabel(), Y_LABEL)
        np.testing.assert_array_equal(square_roots, np.array([4.0, 3.0]))
        annotations = [child for child in ax.get_children() if isinstance(child, matplotlib.text.Annotation)]
        try:
            datetime.strptime(annotations[0].get_text(), TIME_FORMAT)
        except:
            raise ValueError(f"The datetime in annotation ({annotations[0]}) does not have the right format ({TIME_FORMAT}).")
    def test_case_2(self):
        # Input 2: List with 1 dictionary without the 'from_user' key.
        data = [
            {
                "key_1": 7,
                "key_2": 4
            }
        ]
        square_roots, ax = task_func(data)
        self.assertEqual(len(square_roots), 0)
    def test_case_3(self):
        # Input 3: Empty list.
        data = []
        square_roots, ax = task_func(data)
        self.assertEqual(len(square_roots), 0)
    def test_case_4(self):
        # Input 4: Normal case with 5 dictionaries with 'from_user' keys.
        data = [
            {
                "from_user": 121,
                "unused_key": 45,
            },
            {
                "from_user": 169,
                "unused_key": -1,
            },
            {
                "from_user": 225,
            },
            {
                "from_user": 9,
            },
            {
                "from_user": 49,
            },
        ]
        square_roots, ax = task_func(data)
        np.testing.assert_array_equal(square_roots, np.array([11.0, 13.0, 15.0, 3.0, 7.0]))
    def test_case_5(self):
        # Input 5: List with 1 dictionary with the 'from_user' key.
        data = [{"from_user": 7, "bye": 4}]
        square_roots, ax = task_func(data)
        np.testing.assert_array_equal(square_roots, np.array([2.65]))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)