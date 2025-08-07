import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    # Combine the list of dictionaries into a DataFrame
    df = pd.DataFrame(data)
    
    # Fill NA/NaN values with 0
    df_filled = df.fillna(0)
    
    # Set the index to be the time column
    df_filled.set_index('Time', inplace=True)
    
    # Plot the data
    ax = df_filled.plot(kind='line', title='Fruit Sales over Time')
    
    # Set the labels for the axes
    ax.set_xlabel('Time')
    ax.set_ylabel('Sales Quantity')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax
import unittest
import matplotlib
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data = [{"apple": 10}, {"banana": 15, "cherry": 12}]
        ax = task_func(data)
        # Test default plot values
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertTrue(isinstance(ax.lines[0], matplotlib.lines.Line2D))
        self.assertEqual(ax.get_title(), "Fruit Sales over Time")
        self.assertEqual(ax.get_xlabel(), "Time")
        self.assertEqual(ax.get_ylabel(), "Sales Quantity")
    def test_case_2(self):
        # Test flat input
        data = [{"apple": 11, "banana": 15, "cherry": 12, "durian": 10}]
        ax = task_func(data)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(len(ax.lines), len(data[0]))
        for i, (fruit_name, fruit_quantity) in enumerate(data[0].items()):
            self.assertEqual(ax.lines[i]._label, fruit_name)
            self.assertEqual(ax.lines[i]._y, fruit_quantity)
            self.assertIsInstance(ax.lines[i], matplotlib.lines.Line2D)
    def test_case_3(self):
        data = [
            {"apple": 15},
            {"apple": 2, "banana": 11, "cherry": 8},
        ]
        ax = task_func(data)
        # Test data correctness
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(len(ax.lines), 3)
        self.assertEqual(ax.lines[0]._label, "apple")
        self.assertEqual(ax.lines[0]._y.tolist(), [15, 2])
        self.assertEqual(ax.lines[1]._label, "banana")
        self.assertEqual(ax.lines[1]._y.tolist(), [0, 11])
        self.assertEqual(ax.lines[2]._label, "cherry")
        self.assertEqual(ax.lines[2]._y.tolist(), [0, 8])
    def test_case_4(self):
        # Test one fruit only
        data = [{"apple": 10}, {"apple": 12}, {"apple": 15}]
        ax = task_func(data)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(len(ax.lines), 1)
        self.assertEqual(ax.lines[0]._label, "apple")
        self.assertEqual(ax.lines[0]._y.tolist(), [10, 12, 15])
    def test_case_5(self):
        # Test that function fails with unexpected data values
        with self.assertRaises(ValueError):
            task_func("")
        with self.assertRaises(ValueError):
            task_func(1)
        # Test that function fails with unexpected data types
        with self.assertRaises(TypeError):
            task_func(["apple", 10, "banana", 10])
        with self.assertRaises(TypeError):
            task_func([{"apple": "10"}, {"cherry": 10}])
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)