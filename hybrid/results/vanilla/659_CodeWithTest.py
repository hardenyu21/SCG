import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def task_func(x, y, labels):
    # Check if the input arrays and labels have the same length
    if not (len(x) == len(y) == len(labels)):
        raise ValueError("The length of x, y, and labels must be the same.")
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot normal distributions for each pair (x, y) with corresponding label
    for i in range(len(x)):
        # Calculate the mean and standard deviation
        mean = x[i]
        std_dev = y[i]
        
        # Generate a range of x values for the normal distribution
        x_values = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
        
        # Calculate the normal distribution
        y_values = stats.norm.pdf(x_values, mean, std_dev)
        
        # Plot the normal distribution
        ax.plot(x_values, y_values, label=labels[i])
    
    # Add labels and legend
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.set_title('Normal Distributions of Chemical Compounds')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the figure object
    return fig
import unittest
import matplotlib
class TestCases(unittest.TestCase):
    def test_case_1(self):
        x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
        y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
        labels = ['H₂O', 'O₂', 'CO₂']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)
    def test_case_2(self):
        x = [np.array([1,3,5]), np.array([2,4,6])]
        y = [np.array([2,4,6]), np.array([1,3,5])]
        labels = ['N₂', 'Ar']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)
    def test_case_3(self):
        x = [np.array([10,20,30])]
        y = [np.array([15,25,35])]
        labels = ['H₂O']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)
    def test_case_4(self):
        x = [np.array([5,15,25]), np.array([10,20,30]), np.array([15,25,35])]
        y = [np.array([10,20,30]), np.array([15,25,35]), np.array([5,15,25])]
        labels = ['H₂O', 'O₂', 'CO₂']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)
    def test_case_5(self):
        x = [np.array([2,4,8]), np.array([1,3,7])]
        y = [np.array([1,3,7]), np.array([2,4,8])]
        labels = ['N₂', 'Ar']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)