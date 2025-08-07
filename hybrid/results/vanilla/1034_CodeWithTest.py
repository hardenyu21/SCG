import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def task_func(s1, s2):
    # Ensure the input series are pandas Series with the correct index
    s1 = s1.reindex(CATEGORIES).fillna(0)
    s2 = s2.reindex(CATEGORIES).fillna(0)
    
    # Filter categories where both stores have sales exceeding the threshold
    threshold = 200
    valid_categories = (s1 > threshold) & (s2 > threshold)
    
    if not valid_categories.any():
        return None, 0.0
    
    # Select the valid categories
    s1_filtered = s1[valid_categories]
    s2_filtered = s2[valid_categories]
    
    # Compute the Euclidean distance between the two series
    euclidean_distance = np.linalg.norm(s1_filtered - s2_filtered)
    
    # Plot the bar plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    index = np.arange(len(s1_filtered))
    
    ax.bar(index, s1_filtered, bar_width, label='Store 1')
    ax.bar(index + bar_width, s2_filtered, bar_width, label='Store 2')
    
    ax.set_xlabel('Categories')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Comparison for Categories Exceeding $200')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(s1_filtered.index)
    ax.legend()
    
    plt.tight_layout()
    plt.show()
    
    return ax, euclidean_distance

# Example usage:
# s1 = pd.Series([250, 150, 300, 100, 220], index=CATEGORIES)
# s2 = pd.Series([210, 180, 350, 90, 240], index=CATEGORIES)
# ax, distance = task_func(s1, s2)
# print("Euclidean Distance:", distance)
import pandas as pd
import numpy as np
import unittest
import matplotlib.pyplot as plt
# Constants (should be kept consistent with function.py)
CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]
class TestCases(unittest.TestCase):
    """Tests for function task_func."""
    def test_sales_above_threshold(self):
        """Test that the function returns a plot when sales exceed the threshold"""
        np.random.seed(seed=32)
        s1 = pd.Series(np.random.randint(100, 500, size=5), index=CATEGORIES)
        np.random.seed(seed=32)
        s2 = pd.Series(np.random.randint(150, 600, size=5), index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        # Check the correct categories are plotted
        categories_plotted = [label.get_text() for label in ax.get_xticklabels()]
        self.assertListEqual(
            categories_plotted, ["Electronics", "Home Decor", "Automotive", "Books"]
        )
        # Check the title of the plot
        self.assertEqual(
            ax.get_title(), "Sales Comparison Above Threshold in Categories"
        )
        self.assertAlmostEqual(edit_distance, 100.0)
        
    def test_no_sales_above_threshold(self):
        """Test that no categories are plotted when no sales exceed the threshold"""
        np.random.seed(seed=32)
        s1 = pd.Series(np.random.randint(50, 150, size=5), index=CATEGORIES)
        np.random.seed(seed=32)
        s2 = pd.Series(np.random.randint(50, 150, size=5), index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        # Check that no categories are plotted
        self.assertIsNone(
            ax, "Expected None as no categories should meet the threshold"
        )
        self.assertAlmostEqual(edit_distance, 0.0)
    def test_all_sales_above_threshold(self):
        """Test that all categories are plotted when all sales exceed the threshold"""
        np.random.seed(seed=123)
        s1 = pd.Series(np.random.randint(200, 500, size=5), index=CATEGORIES)
        np.random.seed(seed=123)
        s2 = pd.Series(np.random.randint(250, 600, size=5), index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        # Check that all categories are plotted
        categories_plotted = [label.get_text() for label in ax.get_xticklabels()]
        self.assertListEqual(categories_plotted, CATEGORIES)
        self.assertAlmostEqual(edit_distance, 389.8127755730948)
        
    def test_some_sales_above_threshold(self):
        """Test that some categories are plotted when some sales exceed the threshold"""
        s1 = pd.Series([250, 180, 290, 200, 290], index=CATEGORIES)
        s2 = pd.Series([260, 290, 195, 299, 295], index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        # Check that only the correct categories are plotted
        categories_plotted = [label.get_text() for label in ax.get_xticklabels()]
        self.assertListEqual(categories_plotted, ["Electronics", "Books"])
        self.assertAlmostEqual(edit_distance, 11.180339887498949)
        
    def test_single_sales_above_threshold(self):
        """Test that only a single category is plotted when only a single category has sales exceeding the threshold"""
        s1 = pd.Series([150, 180, 290, 200, 190], index=CATEGORIES)
        s2 = pd.Series([160, 190, 295, 199, 195], index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        # Check that only a single category is plotted
        categories_plotted = [label.get_text() for label in ax.get_xticklabels()]
        self.assertListEqual(categories_plotted, ["Home Decor"])
        self.assertAlmostEqual(edit_distance, 5.0)
        
    def tearDown(self):
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)