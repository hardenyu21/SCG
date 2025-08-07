import random
import statistics
import matplotlib.pyplot as plt

def task_func(n, value):
    # Generate 'n' random numbers between 0 and 1
    random_numbers = [random.random() for _ in range(n)]
    
    # Calculate the average of the generated numbers
    average = statistics.mean(random_numbers)
    
    # Find numbers greater than the average
    greater_than_average = [num for num in random_numbers if num > average]
    
    # Count numbers greater than or equal to the specified value
    count_greater_or_equal = sum(1 for num in random_numbers if num >= value)
    
    # Sort the numbers
    sorted_numbers = sorted(random_numbers)
    
    # Plot the sorted numbers
    plt.plot(sorted_numbers, marker='o', linestyle='-')
    plt.title('Sorted Random Numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()
    
    # Return the list of numbers greater than the average and the count
    return greater_than_average, count_greater_or_equal

# Example usage:
# result = task_func(100, 0.5)
# print("Numbers greater than average:", result[0])
# print("Count of numbers >= 0.5:", result[1])
import unittest
from unittest.mock import MagicMock, patch
class TestCases(unittest.TestCase):
    def setUp(self):
        # Mock random.random to return a fixed sequence of numbers
        self.random_sequence = [0.6, 0.4, 0.8, 0.2, 0.5]
        self.random_mock = MagicMock(side_effect=self.random_sequence)
    @patch('matplotlib.pyplot.show')
    def test_plotting_mocked(self, mock_show):
        """ Test that the function calls plt.show(). """
        with patch('random.random', self.random_mock):
            _ = task_func(5, 0.5)
            mock_show.assert_called_once()
    def test_return_types(self):
        """ Test that the function returns a list and an int. """
        greater_avg, count = task_func(10, 0.5)
        self.assertIsInstance(greater_avg, list)
        self.assertIsInstance(count, int)
    def test_number_of_elements(self):
        """Check if the list contains only numbers greater than the average."""
        with patch('random.random', self.random_mock):
            greater_avg, _ = task_func(5, 0.5)
            self.assertEqual(len(greater_avg), 2)
    def test_count_greater_than_or_equal_value(self):
        """Verify the count includes numbers greater than or equal to the value."""
        with patch('random.random', self.random_mock):
            _, count = task_func(5, 0.5)
            self.assertEqual(count, 2)
    def test_empty_case(self):
        """Test the function's behavior with n=0."""
        greater_avg, count = task_func(0, 0.5)
        self.assertEqual((greater_avg, count), ([], 0))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)