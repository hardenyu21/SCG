import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt

def task_func(duration):
    timestamps = []
    random_values = []
    start_time = time.time()
    
    while (time.time() - start_time) < duration:
        current_time = datetime.now().strftime('%H:%M:%S.%f')
        random_value = randint(0, 100)
        
        timestamps.append(current_time)
        random_values.append(random_value)
        
        # Print the current timestamp and random value for real-time monitoring
        print(f"Time: {current_time}, Value: {random_value}")
        
        # Sleep for a short duration to simulate real-time data generation
        time.sleep(0.1)
    
    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, random_values, marker='o')
    plt.xlabel('Time')
    plt.ylabel('Random Value')
    plt.title('Real-time Random Data Generation')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return (timestamps, random_values)

# Example usage:
# task_func(10)  # Generate random data for 10 seconds
### Unit Tests
# Check and set the backend
import unittest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    @patch('matplotlib.pyplot.pause', return_value=None)
    def test_data_list_lengths_match(self, mock_pause):
        """
        Test that the lengths of timestamp and data lists match.
        """
        x_data, y_data = task_func(1)
        self.assertEqual(len(x_data), len(y_data))
    @patch('matplotlib.pyplot.pause', return_value=None)
    def test_function_runs_without_error(self, mock_pause):
        """
        Test that the function runs without error.
        """
        try:
            task_func(1)
            function_ran_successfully = True
        except Exception as e:
            function_ran_successfully = False
        self.assertTrue(function_ran_successfully)
    @patch('matplotlib.pyplot.pause', return_value=None)
    def test_random_values_within_range(self, mock_pause):
        """
        Test that the random values are within the specified range.
        """
        _, y_data = task_func(1)
        self.assertTrue(all(0 <= y <= 100 for y in y_data))
    @patch('matplotlib.pyplot.pause', return_value=None)
    @patch(__name__ + '.randint', return_value=50)
    def test_random_values_consistency(self, mock_randint, mock_pause):
        """
        Test that generated values are consistent with the mocked random function.
        """
        _, y_data = task_func(1)
        self.assertTrue(all(y == 50 for y in y_data))
    @patch('matplotlib.pyplot.pause', return_value=None)
    def test_timestamps_format(self, mock_pause):
        """
        Test that timestamps are in the expected format.
        """
        x_data, _ = task_func(1)
        for timestamp in x_data:
            datetime.strptime(timestamp, '%H:%M:%S.%f')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)