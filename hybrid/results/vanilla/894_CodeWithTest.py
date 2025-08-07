import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def task_func():
    # Generate a numeric array of random integers between 1 and 100
    random_integers = np.random.randint(1, 101, size=ARRAY_SIZE)
    
    # Calculate the mean and standard deviation
    mean_value = np.mean(random_integers)
    std_deviation = np.std(random_integers)
    
    # Create a histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(random_integers, bins=range(1, 102), edgecolor='black', alpha=0.7)
    
    # Plot the mean as a red dashed line
    ax.axvline(mean_value, color='red', linestyle='--', label=f'Mean: {mean_value:.2f}')
    
    # Plot the standard deviation as purple dashed lines
    ax.axvline(mean_value - std_deviation, color='purple', linestyle='--', label=f'Std Dev: {std_deviation:.2f}')
    ax.axvline(mean_value + std_deviation, color='purple', linestyle='--')
    
    # Set the title and labels
    ax.set_title("Histogram of Random Integers")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the tuple containing the array, mean, standard deviation, and the histogram plot
    return random_integers, mean_value, std_deviation, ax

# Call the function
task_func()
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        np.random.seed(0)
        array, mean, std, ax = task_func()
        self.assertEqual(array.size, ARRAY_SIZE)
        self.assertEqual(mean, 49.6135)
        self.assertEqual(std, 28.5323416100046)
        self.assertEqual(ax.get_title(), 'Histogram of Random Integers')
    def test_case_2(self):
        array, mean, std, ax = task_func()
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
    def test_case_3(self):
        np.random.seed(1)
        array, mean, std, ax = task_func()
        self.assertEqual(mean, 50.0717)
        self.assertEqual(std, 28.559862729186918)
    def test_case_4(self):
        np.random.seed(100)
        array, mean, std, ax = task_func()
        self.assertEqual(mean, 50.2223)
        self.assertEqual(std, 28.494467580742757)
    def test_case_5(self):
        np.random.seed(500)
        array, mean, std, ax = task_func()
        self.assertEqual(mean, 49.8636)
        self.assertEqual(std, 28.516030492338864)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)