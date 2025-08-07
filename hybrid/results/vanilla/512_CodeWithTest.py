import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check for negative values in the specified column
    if (data[column] < 0).any():
        raise ValueError("Quantity sold or total sales cannot be negative.")
    
    # Calculate sum, mean, min, and max of the column
    column_sum = data[column].sum()
    column_mean = data[column].mean()
    column_min = data[column].min()
    column_max = data[column].max()
    
    # Create a dictionary with the calculated statistics
    stats = {
        'sum': column_sum,
        'mean': column_mean,
        'min': column_min,
        'max': column_max
    }
    
    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(data['Product'], data[column])
    ax.set_title(f'Bar Chart of {column}')
    ax.set_xlabel('Product')
    ax.set_ylabel(column)
    
    # Return the statistics and the Axes object
    return stats, ax
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test total sales
        scenarios = [
            (
                [
                    ["Product A", 100, 10000],
                    ["Product B", 150, 15000],
                    ["Product C", 200, 20000],
                ],
                {"sum": 45000, "mean": 15000.0, "min": 10000, "max": 20000},
            ),
            (
                [
                    ["Product A", 10, 1000],
                    ["Product B", 20, 2000],
                    ["Product C", 30, 3000],
                    ["Product D", 40, 4000],
                ],
                {"sum": 10000, "mean": 2500.0, "min": 1000, "max": 4000},
            ),
            (
                [["Product A", 5, 500]],
                {"sum": 500, "mean": 500.0, "min": 500, "max": 500},
            ),
        ]
        for data, expected in scenarios:
            with self.subTest(data=data):
                stats, ax = task_func("Total Sales", data)
                self.assertDictEqual(stats, expected)
                self.assertEqual(ax.get_title(), "Bar Chart of Total Sales")
                plt.close("all")
    def test_case_2(self):
        # Test quantity sold
        scenarios = [
            (
                [
                    ["Product A", 100, 5000],
                    ["Product B", 200, 6000],
                    ["Product C", 300, 7000],
                ],
                {"sum": 600, "mean": 200.0, "min": 100, "max": 300},
            ),
            (
                [
                    ["Product A", 5, 500],
                    ["Product B", 10, 1000],
                    ["Product C", 15, 1500],
                    ["Product D", 20, 2000],
                    ["Product E", 25, 2500],
                ],
                {"sum": 75, "mean": 15.0, "min": 5, "max": 25},
            ),
        ]
        for data, expected in scenarios:
            with self.subTest(data=data):
                stats, ax = task_func("Quantity Sold", data)
                self.assertDictEqual(stats, expected)
                self.assertEqual(ax.get_title(), "Bar Chart of Quantity Sold")
                plt.close("all")
    def test_case_3(self):
        # Test error handling - invalid column
        with self.assertRaises(KeyError):
            task_func("Invalid Column", [["Product A", 100, 10000]])
    def test_case_4(self):
        # Test error handling - empty data and negative values
        with self.assertRaises(Exception):
            task_func("Total Sales", [])
        with self.assertRaises(Exception):
            task_func("Total Sales", [["Product A", -100, -10000]])
    def test_case_5(self):
        # Test plot data integrity
        data = [["Product A", 100, 5000], ["Product B", 200, 10000]]
        _, ax = task_func("Quantity Sold", data)
        bars = [rect.get_height() for rect in ax.patches]
        expected_bars = [100, 200]
        self.assertEqual(bars, expected_bars)
        plt.close("all")
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)