from datetime import datetime, timedelta
import pytz
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_time, end_time):
    # Define the time zones
    time_zones = ["UTC", "America/Los_Angeles", "Europe/Paris", "Asia/Kolkata", "Australia/Sydney"]
    colors = ["b", "g", "r", "c", "m", "y", "k"]
    
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Generate a list of dates from start_time to end_time
    current_date = start_time
    while current_date <= end_time:
        # Plot the time difference for each time zone
        for i, tz_name in enumerate(time_zones):
            tz = pytz.timezone(tz_name)
            utc_tz = pytz.utc
            
            # Get the local time for the current date in the specified time zone
            local_time = tz.localize(datetime(current_date.year, current_date.month, current_date.day))
            utc_time = local_time.astimezone(utc_tz)
            
            # Calculate the time difference in hours
            time_diff_hours = (local_time.utcoffset().total_seconds()) / 3600
            
            # Plot the time difference
            ax.plot(current_date, time_diff_hours, color=colors[i % len(colors)], marker='o', label=tz_name if i == 0 else "")
        
        # Move to the next day
        current_date += timedelta(days=1)
    
    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Time Difference (hours)')
    ax.set_title('Hourly Difference between UTC and Specified Time Zones')
    ax.legend(title='Time Zones')
    
    # Format the x-axis to show dates
    fig.autofmt_xdate()
    
    # Show grid
    ax.grid(True)
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# start_time = datetime(2023, 10, 1)
# end_time = datetime(2023, 10, 5)
# task_func(start_time, end_time)
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic functionality
        ax = task_func("2021-01-01", "2021-01-10")
        self._common_assertions(ax)
    def test_case_2(self):
        # Test single day range
        ax = task_func("2021-01-01", "2021-01-01")
        self._common_assertions(ax)
    def test_case_3(self):
        # Test leap year
        ax = task_func("2020-02-28", "2020-03-01")
        self._common_assertions(ax)
    def test_case_4(self):
        # Test DST transition
        ax = task_func("2021-03-27", "2021-03-29")
        self._common_assertions(ax)
    def test_case_5(self):
        # Test plotting consistency
        ax = task_func("2021-01-01", "2021-01-10")
        colors = [line.get_color() for line in ax.get_lines()]
        self.assertEqual(len(set(colors)), len(colors))  # Check if colors are unique
    def test_case_6(self):
        # Testing input validation via invalid date format
        with self.assertRaises(ValueError):
            task_func("01-01-2021", "10-01-2021")
    def _common_assertions(self, ax):
        """Common assertions for all test cases"""
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_xlabel(), "Date")
        self.assertEqual(ax.get_ylabel().lower(), "time difference (hours)".lower())
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        expected_timezones = [
            "UTC",
            "America/Los_Angeles",
            "Europe/Paris",
            "Asia/Kolkata",
            "Australia/Sydney",
        ]
        self.assertListEqual(legend_labels, expected_timezones)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)