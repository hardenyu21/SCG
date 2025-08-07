import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def task_func():
    # Generate a numeric array of random integers between 1 and 100
    random_array = np.random.randint(1, 101, size=ARRAY_SIZE)
    
    # Calculate the mean and standard deviation
    mean_value = np.mean(random_array)
    std_deviation = np.std(random_array)
    
    # Create a histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(random_array, bins=range(1, 102), edgecolor='black', alpha=0.7)
    
    # Plot the mean as a red dashed line
    ax.axvline(mean_value, color='red', linestyle='--', label=f'Mean: {mean_value:.2f}')
    
    # Plot the standard deviation as purple dashed lines
    ax.axvline(mean_value - std_deviation, color='purple', linestyle='--', label=f'Std Dev: {std_deviation:.2f}')
    ax.axvline(mean_value + std_deviation, color='purple', linestyle='--')
    
    # Set the title and labels
    ax.set_title("Histogram of Random Values")
    ax.set_xlabel("Val")
    ax.set_ylabel("Freq")
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the tuple containing the array, mean, standard deviation, and the histogram plot
    return random_array, mean_value, std_deviation, ax

# Example usage
task_func()
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        np.random.seed(0)
        array, mean, std, ax = task_func()
        self.assertEqual(array.size, ARRAY_SIZE)
        self.assertEqual(mean, 250.7154)
        self.assertEqual(std, 142.85617453522966)
        self.assertEqual(ax.get_title(), 'Histogram of Random Values')
    def test_case_2(self):
        array, mean, std, ax = task_func()
        self.assertEqual(ax.get_xlabel(), 'Val')
        self.assertEqual(ax.get_ylabel(), 'Freq')
    def test_case_3(self):
        np.random.seed(42)
        array, mean, std, ax = task_func()
        self.assertEqual(array[0], 103)
        self.assertEqual(array[-1], 474)
        self.assertEqual(mean, 250.171)
        self.assertEqual(std, 144.01374920124815)
        
    def test_case_4(self):
        np.random.seed(142)
        array, mean, std, ax = task_func()
        self.assertEqual(array[0], 278)
        self.assertEqual(array[-1], 113)
        self.assertEqual(mean, 251.1245)
        self.assertEqual(std, 144.49066405740547)
    def test_case_5(self):
        np.random.seed(250)
        array, mean, std, ax = task_func()
        self.assertEqual(array[0], 367)
        self.assertEqual(array[-1], 190)
        self.assertEqual(mean, 249.037)
        self.assertEqual(std, 144.32681882103546)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)