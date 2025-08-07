
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        # Generating a sample sales DataFrame
        self.sales_data = pd.DataFrame({
            'Month': range(1, 13),
            'Product A': np.random.randint(100, 200, size=12),
            'Product B': np.random.randint(150, 250, size=12),
            'Product C': np.random.randint(120, 220, size=12),
            'Product D': np.random.randint(130, 230, size=12),
            'Product E': np.random.randint(140, 240, size=12)
        })
    def test_plot_labels(self):
        """Ensure all product labels are present in the plot legend."""
        ax = task_func(self.sales_data)
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertEqual(set(legend_labels), set(self.sales_data.columns[1:]),
                         "Not all product labels are present in the plot legend.")
    def test_plot_lines(self):
        """Check if the plot contains lines for each product."""
        ax = task_func(self.sales_data)
        self.assertEqual(len(ax.lines), len(self.sales_data.columns) - 1,
                         "Plot does not contain the correct number of lines.")
    def test_monthly_ticks(self):
        """Verify that all months are correctly plotted as x-ticks."""
        ax = task_func(self.sales_data)
        # Convert x-ticks to integers for comparison
        x_ticks = [int(tick) for tick in ax.get_xticks() if isinstance(tick, (int, np.integer))]
        expected_ticks = self.sales_data['Month'].tolist()
        self.assertListEqual(x_ticks, expected_ticks, "Not all months are correctly plotted as x-ticks.")
    def test_positive_sales(self):
        """Ensure all plotted sales values are positive."""
        ax = task_func(self.sales_data)
        for line in ax.lines:
            self.assertTrue(all(y >= 0 for y in line.get_ydata()),
                            "Plotted sales values should be positive.")
    def test_std_dev_shading(self):
        """Check for standard deviation shading around each product line."""
        ax = task_func(self.sales_data)
        self.assertGreaterEqual(len(ax.collections), len(self.sales_data.columns) - 1,
                                "Missing standard deviation shading for one or more products.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)