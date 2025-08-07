import numpy as np
import matplotlib.pyplot as plt

# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']

def task_func(data_size):
    # Generate random numeric data
    data = np.random.rand(data_size)
    
    # Randomly select a color for the histogram bars
    color = np.random.choice(BAR_COLOR)
    
    # Create a histogram of the data
    plt.hist(data, bins=10, color=color, edgecolor='black')
    plt.title('Histogram of Random Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the data and the color used
    return data, color

# Example usage
data, color = task_func(1000)
print(f"Data: {data}")
print(f"Color used for histogram: {color}")
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data, color = task_func(100)
        self.assertEqual(len(data), 100)
        self.assertTrue(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
    def test_case_2(self):
        data, color = task_func(50)
        self.assertEqual(len(data), 50)
        self.assertTrue(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
    def test_case_3(self):
        data, color = task_func(150)
        self.assertEqual(len(data), 150)
        self.assertTrue(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
    def test_case_4(self):
        data, color = task_func(200)
        self.assertEqual(len(data), 200)
        self.assertTrue(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
    def test_case_5(self):
        data, color = task_func(250)
        self.assertEqual(len(data), 250)
        self.assertTrue(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)