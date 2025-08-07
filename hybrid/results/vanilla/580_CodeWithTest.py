import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

# Constants
RANGE = 10000  # The range within which random numbers are generated
SIZE = 1000  # The number of random numbers to generate
BIN_WIDTH = 100  # The width of bins for the histogram

def task_func():
    # Generate random numbers
    random_numbers = [random.randint(0, RANGE) for _ in range(SIZE)]
    
    # Calculate moving average
    moving_averages = []
    for i in range(SIZE):
        window = random_numbers[max(0, i-5):i+1]
        moving_average = statistics.mean(window)
        moving_averages.append(moving_average)
    
    # Create DataFrame
    df = pd.DataFrame({
        "Random Numbers": random_numbers,
        "Moving Average": moving_averages
    })
    
    # Plot histogram of "Random Numbers"
    plt.figure(figsize=(10, 6))
    plt.hist(df["Random Numbers"], bins=np.arange(0, RANGE + BIN_WIDTH, BIN_WIDTH), edgecolor='black')
    plt.title("Histogram of Random Numbers")
    plt.xlabel("Random Numbers")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
    
    return df

# Call the function
df = task_func()
import unittest
class TestCases(unittest.TestCase):
    def test_dataframe_shape(self):
        """Test that the DataFrame has the correct shape."""
        df = task_func()
        self.assertEqual(df.shape, (SIZE, 2))
    def test_random_numbers_range(self):
        """Test that the random numbers fall within the specified range."""
        df = task_func()
        self.assertTrue(df['Random Numbers'].between(0, RANGE).all())
    def test_moving_average_calculation(self):
        """Test that the moving average is correctly calculated."""
        df = task_func()
        # Assuming moving average calculation correctness check for the first few entries
        for i in range(6):  # Check the first 6 entries for a window of 6 elements
            expected_avg = statistics.mean(df['Random Numbers'].iloc[max(0, i - 5):i + 1])
            self.assertEqual(df['Moving Average'].iloc[i], expected_avg, "Moving average calculation mismatch.")
    def test_columns_existence(self):
        """Ensure both required columns exist in the DataFrame."""
        df = task_func()
        self.assertIn('Random Numbers', df.columns)
        self.assertIn('Moving Average', df.columns)
    def test_non_empty_dataframe(self):
        """Check that the DataFrame is not empty."""
        df = task_func()
        self.assertFalse(df.empty)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)