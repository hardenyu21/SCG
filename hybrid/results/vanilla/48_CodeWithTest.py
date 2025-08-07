import time
from datetime import datetime
import random
import matplotlib.pyplot as plt

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def task_func(n, output_path=None):
    # Generate n random Unix timestamps
    timestamps = [random.randint(0, int(time.time())) for _ in range(n)]
    
    # Convert timestamps to formatted strings
    formatted_timestamps = [datetime.utcfromtimestamp(ts).strftime(DATE_FORMAT) for ts in timestamps]
    
    # Plot a histogram of the distribution of the generated timestamps
    plt.hist(timestamps, bins=30, color='blue', alpha=0.7)
    plt.title('Distribution of Random Unix Timestamps')
    plt.xlabel('Unix Timestamp')
    plt.ylabel('Frequency')
    
    # Save the plot to the specified path if provided, otherwise display it
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    
    # Return the list of formatted timestamps
    return formatted_timestamps
import unittest
import os
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        self.test_dir = "data/task_func"
        os.makedirs(self.test_dir, exist_ok=True)
        self.o_1 = os.path.join(self.test_dir, "histogram_1.png")
    def tearDown(self) -> None:
        import shutil
        try:
            shutil.rmtree(self.test_dir)
        except:
            pass
    def test_case_1(self):
        random.seed(42)
        result = task_func(10)
        self.assertEqual(len(result), 10)
    def test_case_2(self):
        random.seed(42)
        result = task_func(15)
        for timestamp in result:
            try:
                datetime.strptime(timestamp, DATE_FORMAT)
            except ValueError:
                self.fail(f"Timestamp {timestamp} doesn't match the specified format.")
    def test_case_3(self):
        random.seed(42)
        task_func(20, output_path=self.o_1)
        self.assertTrue(os.path.exists(self.o_1))
    def test_case_4(self):
        result = task_func(50)
        self.assertEqual(len(result), len(set(result)))
    def test_case_5(self):
        result = task_func(0)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)