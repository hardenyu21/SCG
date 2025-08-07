import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data, column="c"):
    # Convert the data dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Remove the specified column if it exists
    if column in df.columns:
        df = df.drop(columns=[column])
    
    # Check if there is any numeric data left to plot
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Plot the numeric data if it exists
    ax = None
    if not numeric_df.empty:
        ax = numeric_df.plot(kind='line', figsize=(10, 6))
        plt.title('Plot of Numeric Data')
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.grid(True)
        plt.show()
    
    return df, ax
import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Scenario: DataFrame with columns 'a', 'b', and 'c'.
        np.random.seed(0)
        data = {
                "a": np.random.randn(10),
                "b": np.random.randn(10),
                "c": np.random.randn(10),
            }
        df = pd.DataFrame(
            data
        )
        modified_df, ax = task_func(data)  # Remove default column 'c'.
        # Assert column 'c' removal and plot data verification.
        self.assertNotIn("c", modified_df.columns)
        plotted_data = [line.get_ydata() for line in ax.get_lines()]
        self.assertTrue(
            all(
                [
                    np.array_equal(data, modified_df[col].values)
                    for data, col in zip(plotted_data, modified_df.columns)
                ]
            )
        )
    def test_case_2(self):
        # Scenario: DataFrame with columns 'a' and 'b' (no 'c').
        np.random.seed(0)
        data = {"a": np.random.randn(10), "b": np.random.randn(10)}
        df = pd.DataFrame(data)
        modified_df, ax = task_func(data)
        # Assert that the modified DataFrame remains unchanged and plot is generated.
        self.assertEqual(list(df.columns), list(modified_df.columns))
        self.assertIsNotNone(ax)
    def test_case_3(self):
        # Scenario: Empty DataFrame
        data = {}
        df = pd.DataFrame(data)
        modified_df, ax = task_func(data)
        # Assert empty DataFrame and no plot.
        self.assertTrue(modified_df.empty)
        self.assertIsNone(ax)
    def test_case_4(self):
        # Scenario: DataFrame with single non-numeric column 'c'.
        data = {"c": ["apple", "banana", "cherry"]}
        df = pd.DataFrame(data)
        modified_df, ax = task_func(data)
        # Assert empty DataFrame after 'c' removal and no plot.
        self.assertTrue(modified_df.empty)
        self.assertIsNone(ax)
    def test_case_5(self):
        np.random.seed(0)
        # Scenario: DataFrame with columns 'a', 'b', 'c', and non-numeric column 'd'.
        data = {
                "a": np.random.randn(10),
                "b": np.random.randn(10),
                "c": np.random.randn(10),
                "d": [
                    "apple",
                    "banana",
                    "cherry",
                    "date",
                    "fig",
                    "grape",
                    "honeydew",
                    "kiwi",
                    "lime",
                    "mango",
                ],
            }
        df = pd.DataFrame(
            data
        )
        modified_df, ax = task_func(data)
        # Assert column 'c' removal and plot data verification excluding non-numeric column 'd'.
        self.assertNotIn("c", modified_df.columns)
        plotted_data = [line.get_ydata() for line in ax.get_lines()]
        self.assertTrue(
            all(
                [
                    np.array_equal(data, modified_df[col].values)
                    for data, col in zip(plotted_data, modified_df.columns)
                    if col != "d"
                ]
            )
        )
    def test_case_6(self):
        # Scenario: Remove specified column.
        np.random.seed(0)
        data = {
                "a": np.random.randn(10),
                "b": np.random.randn(10),
            }
        df = pd.DataFrame(
            data
        )
        modified_df, ax = task_func(df, column="a")
        self.assertNotIn("a", modified_df.columns)
        plotted_data = [line.get_ydata() for line in ax.get_lines()]
        self.assertTrue(
            all(
                [
                    np.array_equal(data, modified_df[col].values)
                    for data, col in zip(plotted_data, modified_df.columns)
                ]
            )
        )
    def test_case_7(self):
        # Scenario: Only non-numeric columns.
        data = {
                "a": ["apple", "banana"],
                "b": ["cherry", "date"],
                "c": ["fig", "grape"],
            }
        df = pd.DataFrame(
            data
        )
        modified_df, ax = task_func(data)
        self.assertNotIn("c", modified_df.columns)
        pd.testing.assert_frame_equal(df[["a", "b"]], modified_df)
        self.assertEqual(ax, None)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)