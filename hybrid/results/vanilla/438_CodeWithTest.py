import pickle
import os
import matplotlib.pyplot as plt

def task_func(numbers, file_path="save.pkl"):
    # Check if the input is a list of numbers
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("Input must be a list of numbers.")
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(numbers)
    ax.set_title("Plot of Numbers")
    
    # Save the figure to a pickle file
    with open(file_path, 'wb') as file:
        pickle.dump(fig, file)
    
    # Close the figure to free up memory
    plt.close(fig)
    
    # Load the figure back from the pickle file
    with open(file_path, 'rb') as file:
        loaded_fig = pickle.load(file)
    
    # Delete the pickle file
    os.remove(file_path)
    
    return loaded_fig
import unittest
import matplotlib.pyplot as plt
import tempfile
import os
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        random.seed(0)
    def test_case_1(self):
        # Test default case - correct file was generated & correct removal
        numbers = list(range(10))
        loaded_fig = task_func(numbers)
        self.assertIsInstance(
            loaded_fig,
            type(plt.figure()),
            "Returned object is not a Matplotlib figure.",
        )
        self.assertFalse(os.path.exists("save.pkl"), "Pickle file was not deleted.")
    def test_case_2(self):
        # Test when saving intermediate file to specified location
        numbers = list(range(10))
        path = os.path.join(self.temp_dir.name, "default.pkl")
        loaded_fig = task_func(numbers, path)
        self.assertIsInstance(
            loaded_fig,
            type(plt.figure()),
            "Returned object is not a Matplotlib figure.",
        )
        self.assertFalse(os.path.exists(path), "Pickle file was not deleted.")
    def test_case_3(self):
        # Test with floats
        numbers = [random.random() for _ in range(10)]
        loaded_fig = task_func(numbers)
        self.assertIsInstance(
            loaded_fig,
            type(plt.figure()),
            "Returned object is not a Matplotlib figure.",
        )
        self.assertFalse(os.path.exists("save.pkl"), "Pickle file was not deleted.")
    def test_case_4(self):
        # Test with a mix of positive, negative, integer, and floating numbers
        numbers = [1, -1, 2.5, -2.5, 3, -3, 4.5, -4.5]
        loaded_fig = task_func(numbers)
        self.assertIsInstance(
            loaded_fig,
            type(plt.figure()),
            "Returned object is not a Matplotlib figure.",
        )
        self.assertFalse(os.path.exists("save.pkl"), "Pickle file was not deleted.")
    def test_case_5(self):
        # Test with an empty list
        numbers = []
        loaded_fig = task_func(numbers)
        self.assertIsInstance(
            loaded_fig,
            type(plt.figure()),
            "Returned object is not a Matplotlib figure.",
        )
        self.assertFalse(os.path.exists("save.pkl"), "Pickle file was not deleted.")
    def test_case_6(self):
        # Function should fail when there's invalid input
        with self.assertRaises(TypeError):
            task_func("123")
        with self.assertRaises(TypeError):
            task_func(["1", "2", "3"])
        with self.assertRaises(TypeError):
            task_func([None, None, None])
    def tearDown(self):
        plt.close("all")
        self.temp_dir.cleanup()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)