import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

def task_func(intervals=100, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Initialize lists to store time and random numbers
    times = []
    random_numbers = []
    
    # Start the timer
    start_time = time.time()
    
    for i in range(intervals):
        # Generate a random number
        random_number = random.random()
        
        # Record the current elapsed time
        elapsed_time = time.time() - start_time
        
        # Append the time and random number to their respective lists
        times.append(elapsed_time)
        random_numbers.append(random_number)
        
        # Wait for 1 second
        time.sleep(1)
    
    # Plot the random numbers as a function of elapsed time
    fig, ax = plt.subplots()
    ax.plot(times, random_numbers, marker='o', linestyle='-')
    ax.set_xlabel('Elapsed Time (s)')
    ax.set_ylabel('Random Number')
    ax.set_title('Random Numbers Over Time')
    
    # Calculate the kurtosis of the generated numbers
    kurtosis_value = kurtosis(random_numbers)
    
    # Return the Axes object and the kurtosis value
    return ax, kurtosis_value

# Example usage:
# ax, kurtosis_value = task_func(intervals=10, seed=42)
# plt.show()
# print(f"Kurtosis: {kurtosis_value}")
import unittest
import doctest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    
    @patch('time.sleep', return_value=None)  # Mocking time.sleep
    def test_case_1(self, mock_sleep):
        ax, kurtosis = task_func(5)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 5)
        self.assertEqual(len(lines[0].get_ydata()), 5)
        self.assertEqual(mock_sleep.call_count, 5)
    @patch('time.sleep', return_value=None)
    def test_case_2(self, mock_sleep):
        ax, kurtosis = task_func(10, 44)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 10)
        self.assertEqual(len(lines[0].get_ydata()), 10)
        self.assertNotAlmostEqual(kurtosis, -0.34024, places=5)
    @patch('time.sleep', return_value=None)
    def test_case_3(self, mock_sleep):
        ax, kurtosis = task_func()  # Default intervals = 100
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 100)
        self.assertEqual(len(lines[0].get_ydata()), 100)
        
    @patch('time.sleep', return_value=None)
    def test_case_4(self, mock_sleep):
        ax, kurtosis = task_func(1)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 1)
        self.assertEqual(len(lines[0].get_ydata()), 1)
    @patch('time.sleep', return_value=None)
    def test_case_5(self, mock_sleep):
        ax, kurtosis = task_func(0)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 0)
        self.assertEqual(len(lines[0].get_ydata()), 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)