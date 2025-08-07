import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(x, y, labels):
    # Ensure x and y are lists of arrays
    if not isinstance(x, list) or not isinstance(y, list):
        raise ValueError("x and y should be lists of arrays.")
    
    if not isinstance(labels, list):
        raise ValueError("labels should be a list of strings.")
    
    if len(x) != len(y) or len(x) != len(labels):
        raise ValueError("x, y, and labels should have the same length.")
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Iterate over each pair of x and y arrays
    for i in range(len(x)):
        # Reshape the arrays for scaling
        x_scaled = x[i].reshape(-1, 1)
        y_scaled = y[i].reshape(-1, 1)
        
        # Initialize the StandardScaler
        scaler = StandardScaler()
        
        # Fit and transform the data
        x_scaled = scaler.fit_transform(x_scaled).flatten()
        y_scaled = scaler.fit_transform(y_scaled).flatten()
        
        # Plot the scaled data
        ax.plot(x_scaled, y_scaled, label=labels[i])
    
    # Add labels and legend
    ax.set_xlabel('Scaled X')
    ax.set_ylabel('Scaled Y')
    ax.legend()
    
    # Return the figure object
    return fig
import unittest
import numpy.testing as npt
class TestCases(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.x = [np.array([1,2,3]), np.array([4,5,6])]
        self.y = [np.array([4,5,6]), np.array([7,8,9])]
        self.labels = ['Group 1', 'Group 2']
    def test_figure_type(self):
        """Test that the function returns a matplotlib figure."""
        fig = task_func(self.x, self.y, self.labels)
        self.assertTrue(str(type(fig)).endswith("matplotlib.figure.Figure'>"))
    def test_plot_labels(self):
        """Test that the correct number of labels are in the legend."""
        fig = task_func(self.x, self.y, self.labels)
        ax = fig.axes[0]
        self.assertEqual(len(ax.get_legend_handles_labels()[1]), len(self.labels))
    def test_non_empty_plot(self):
        """Test that the plot is not empty."""
        fig = task_func(self.x, self.y, self.labels)
        ax = fig.axes[0]
        self.assertTrue(len(ax.lines) > 0)
    def test_scaled_values_range(self):
        """Test that the scaled values have a mean close to 0 and a standard deviation close to 1."""
        scaler = StandardScaler()
        for xy in zip(self.x, self.y):
            xy_scaled = scaler.fit_transform(np.vstack(xy).T)
            self.assertTrue(np.allclose(np.mean(xy_scaled, axis=0), 0, atol=1e-7))
            self.assertTrue(np.allclose(np.std(xy_scaled, axis=0), 1, atol=1e-7))
    def test_input_unchanged(self):
        """Test that the original input arrays are unchanged after scaling."""
        x_original = [arr.copy() for arr in self.x]
        y_original = [arr.copy() for arr in self.y]
        task_func(self.x, self.y, self.labels)
        for orig, after in zip(x_original, self.x):
            npt.assert_array_equal(orig, after)
        for orig, after in zip(y_original, self.y):
            npt.assert_array_equal(orig, after)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)