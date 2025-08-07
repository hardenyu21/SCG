import numpy as np
import matplotlib.pyplot as plt
from random import randint

def task_func(POINTS=100):
    # Initialize arrays to store the x and y coordinates
    x_coords = np.zeros(POINTS)
    y_coords = np.zeros(POINTS)
    
    # Define possible directions: right, left, up, down
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Generate the random walk
    for i in range(1, POINTS):
        dx, dy = directions[randint(0, 3)]
        x_coords[i] = x_coords[i - 1] + dx
        y_coords[i] = y_coords[i - 1] + dy
    
    # Plot the random walk
    fig, ax = plt.subplots()
    ax.plot(x_coords, y_coords, marker='o', linestyle='-')
    ax.set_title('2D Random Walk')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.grid(True)
    
    # Show the plot
    plt.show()
    
    # Return the figure object
    return fig

# Example usage
task_func(100)
import unittest
from unittest.mock import patch, MagicMock
import numpy as np
class TestCases(unittest.TestCase):
    @patch('matplotlib.pyplot.show')
    def test_no_error(self, mock_show):
        """Test that the function runs without error."""
        try:
            task_func(100)  # Adjust POINTS value if necessary for your specific test case
        except Exception as e:
            self.fail(f"Function task_func raised an exception: {e}")
    @patch('matplotlib.pyplot.subplots')
    def test_walk_length(self, mock_subplots):
        """Test that the walk has the correct length."""
        mock_ax = MagicMock()
        mock_fig = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        
        task_func(100)  # Using a specific POINTS value for testing
        mock_ax.plot.assert_called_once()
        args, kwargs = mock_ax.plot.call_args
        x, y = args[0], args[1]
        self.assertEqual(len(x), 100)
        self.assertEqual(len(y), 100)
    @patch('matplotlib.pyplot.subplots')
    def test_starting_point(self, mock_subplots):
        """Test that the walk starts at the origin."""
        mock_ax = MagicMock()
        mock_fig = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        task_func(100)  # Using a specific POINTS value for testing
        
        args, _ = mock_ax.plot.call_args
        x, y = args[0], args[1]
        self.assertEqual(x[0], 0)
        self.assertEqual(y[0], 0)
    @patch('matplotlib.pyplot.subplots')
    def test_step_direction(self, mock_subplots):
        """Test that each step moves in a valid direction according to the trigonometric calculation."""
        mock_ax = MagicMock()
        mock_fig = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        task_func(10)  # Using a smaller number for a more manageable test case
        args, _ = mock_ax.plot.call_args
        x, y = args[0], args[1]
        for i in range(1, len(x)):
            x_diff = abs(x[i] - x[i - 1])
            y_diff = abs(y[i] - y[i - 1])
            self.assertTrue(np.isclose(x_diff, 1, atol=0.1) or np.isclose(y_diff, 1, atol=0.1),
                            msg=f"Step from ({x[i-1]}, {y[i-1]}) to ({x[i]}, {y[i]}) is not valid.")
    @patch('matplotlib.pyplot.show')
    def test_plot_shown(self, mock_show):
        """Test that plt.show() is called."""
        task_func(100)  # Adjust POINTS value if necessary for your specific test case
        mock_show.assert_called_once()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)