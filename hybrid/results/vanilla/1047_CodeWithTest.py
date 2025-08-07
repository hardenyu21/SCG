from datetime import datetime
import random
import matplotlib.pyplot as plt

def task_func(date_str):
    # Parse the date string to a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Get the day of the month
    day_of_month = date.day
    
    # Generate a list of random integers with the count equal to the day of the month
    random_integers = [random.randint(0, 100) for _ in range(day_of_month)]
    
    # Create a line plot of the random integers
    fig, ax = plt.subplots()
    ax.plot(random_integers, marker='o')
    
    # Set labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Random Integer')
    ax.set_title(f'Random Integers for {date_str}')
    
    # Return the Axes object
    return ax
import unittest
import matplotlib.axes
from datetime import datetime
class TestCases(unittest.TestCase):
    """Test cases for task_func."""
    def test_mid_month(self):
        """
        Test the function with a mid-month date.
        Checks if the generated plot has 15 data points for a date like '2023-06-15'.
        """
        ax = task_func("2023-06-15")
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 15)
    def test_beginning_of_month(self):
        """
        Test the function with a date at the beginning of the month.
        Checks if the plot has 1 data point for a date like '2023-06-01'.
        """
        ax = task_func("2023-06-01")
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 1)
    def test_end_of_month(self):
        """
        Test the function with a date at the end of the month.
        Checks if the plot has 31 data points for a date like '2023-07-31'.
        """
        ax = task_func("2023-07-31")
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 31)
    def test_leap_year(self):
        """
        Test the function with a leap year date.
        Checks if the plot has 29 data points for a leap year date like '2024-02-29'.
        """
        ax = task_func("2024-02-29")
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 29)
    def test_invalid_date(self):
        """
        Test the function with an invalid date format.
        Expects a ValueError to be raised for an incorrectly formatted date.
        """
        with self.assertRaises(ValueError):
            task_func("2023/06/15")
    def tearDown(self):
        plt.clf()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)