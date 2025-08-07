from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

def task_func(days_in_past=7, random_seed=0):
    if days_in_past < 1:
        raise ValueError("days_in_past must be at least 1.")
    
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate random temperatures between 15 and 35
    temperatures = np.random.randint(15, 36, size=days_in_past)
    
    # Generate dates for the past week
    dates = [datetime.now() - timedelta(days=i) for i in range(days_in_past)]
    dates.reverse()  # Reverse to have the oldest date first
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, marker='o', linestyle='-')
    
    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Trend')
    
    # Format the x-axis to show dates
    fig.autofmt_xdate()
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage
task_func()
import unittest
import matplotlib.pyplot as plt
import numpy as np
class TestCases(unittest.TestCase):
    def _test_plot(self, ax):
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_xlabel(), "Date")
        self.assertEqual(ax.get_ylabel(), "Temperature (°C)")
        self.assertEqual(ax.get_title(), "Temperature Trend")
    def test_case_1(self):
        # Test default parameters
        ax = task_func()
        self._test_plot(ax)
    def test_case_2(self):
        # Test days in the past
        for n_days in [1, 5, 50, 100]:
            ax = task_func(n_days, random_seed=2)
            self._test_plot(ax)
            self.assertEqual(len(ax.lines[0].get_ydata()), n_days)
    def test_case_3(self):
        # Test handling invalid days in the past
        with self.assertRaises(Exception):
            task_func(0, random_seed=4)
    def test_case_4(self):
        # Test handling invalid days in the past
        with self.assertRaises(Exception):
            task_func(-1, random_seed=4)
    def test_case_5(self):
        # Test random seed reproducibility
        ax1 = task_func(5, random_seed=42)
        ax2 = task_func(5, random_seed=42)
        self.assertTrue(
            np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())
        )
    def test_case_6(self):
        # Test random seed difference
        ax1 = task_func(5, random_seed=0)
        ax2 = task_func(5, random_seed=42)
        self.assertFalse(
            np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())
        )
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)