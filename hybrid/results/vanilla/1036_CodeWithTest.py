import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(s1, s2):
    # Find the intersection of the two series
    intersection = s1[s1.isin(s2)]
    
    # Create a DataFrame to hold the data for plotting
    df = pd.DataFrame({
        'Series': ['s1'] * len(s1) + ['s2'] * len(s2),
        'Values': s1.tolist() + s2.tolist()
    })
    
    # Create a swarm plot
    plt.figure(figsize=(10, 6))
    ax = sns.swarmplot(x='Series', y='Values', data=df, palette='Set2')
    
    # Highlight the intersection points with red dashed lines
    for value in intersection:
        ax.axhline(y=value, color='red', linestyle='--', linewidth=1)
    
    # Set plot labels and title
    ax.set_title('Swarm Plot with Intersection Highlight')
    ax.set_xlabel('Series')
    ax.set_ylabel('Values')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object and the intersection count
    return ax, len(intersection)

# Example usage:
# s1 = pd.Series([1, 2, 3, 4, 5])
# s2 = pd.Series([3, 4, 5, 6, 7])
# ax, intersection_count = task_func(s1, s2)
# print(f"Intersection count: {intersection_count}")
import pandas as pd
import unittest
class TestCases(unittest.TestCase):
    """Tests for the function task_func."""
    def test_intersection_exists(self):
        """Test that the function works when the two series have an intersection."""
        s1 = pd.Series([1, 2, 3, 4, 5], name="Series1")
        s2 = pd.Series([4, 5, 6, 7, 8], name="Series2")
        ax, intersection_count = task_func(s1, s2)
        self.assertEqual(ax.get_title(), "Overlap Between Series1 and Series2")
        self.assertEqual(intersection_count, 2)
    def test_no_intersection(self):
        """Test that the function works when the two series have no intersection."""
        s1 = pd.Series([1, 2, 3], name="Series1")
        s2 = pd.Series([4, 5, 6], name="Series2")
        ax, intersection_count = task_func(s1, s2)
        self.assertEqual(ax.get_title(), "Overlap Between Series1 and Series2")
        self.assertEqual(intersection_count, 0)
    def test_empty_series(self):
        """Test that the function works when one of the series is empty."""
        s1 = pd.Series([], name="Series1")
        s2 = pd.Series([], name="Series2")
        ax, intersection_count = task_func(s1, s2)
        self.assertEqual(ax.get_title(), "Overlap Between Series1 and Series2")
        self.assertEqual(intersection_count, 0)
    def test_partial_intersection(self):
        """Test that the function works when the two series have a partial intersection."""
        s1 = pd.Series([1, 2], name="Series1")
        s2 = pd.Series([2, 3], name="Series2")
        ax, intersection_count = task_func(s1, s2)
        self.assertEqual(ax.get_title(), "Overlap Between Series1 and Series2")
        self.assertEqual(intersection_count, 1)
    def test_identical_series(self):
        """Test that the function works when the two series are identical."""
        s1 = pd.Series([1, 2, 3], name="Series1")
        s2 = pd.Series([1, 2, 3], name="Series2")
        ax, intersection_count = task_func(s1, s2)
        self.assertEqual(ax.get_title(), "Overlap Between Series1 and Series2")
        self.assertEqual(intersection_count, 3)
    def tearDown(self):
        plt.clf()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)