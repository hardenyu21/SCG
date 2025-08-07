import ast
import pandas as pd
import seaborn as sns

def task_func(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert the string representations of dictionaries in 'dict_column' to actual dictionaries
    df['dict_column'] = df['dict_column'].apply(ast.literal_eval)
    
    # Explode the dictionaries into separate columns
    dict_df = df['dict_column'].apply(pd.Series)
    
    # Concatenate the original DataFrame (excluding 'dict_column') with the exploded DataFrame
    df = pd.concat([df.drop(columns=['dict_column']), dict_df], axis=1)
    
    # Visualize the data using Seaborn's pairplot
    ax = sns.pairplot(df)
    
    # Return the DataFrame and the PairGrid object
    return df, ax
import unittest
import matplotlib
import os
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        self.test_dir = "data/task_func"
        os.makedirs(self.test_dir, exist_ok=True)
        df = pd.DataFrame(
            {
                "dict_column": [
                    "{'A' : 1, 'B' : 2, 'C' : 3}",
                    "{'D' : 4, 'E' : 5, 'F' : 6}",
                ],
                "Value1": [1, 2],
                "Value2": [3, 4],
            }
        )
        self.f_1 = os.path.join(self.test_dir, "csv_1.csv")
        df.to_csv(self.f_1, index=False)
        df = pd.DataFrame(
            {
                "dict_column": [
                    "{'G' : 7, 'H' : 8}",
                    "{'I' : 9, 'J' : 10}",
                    "{'G' : 7, 'H' : 8}",
                    "{'I' : 9, 'J' : 10}",
                ],
                "Value1": [2, 1, 2, 2],
                "Value2": [1, 1, 3, 1],
            }
        )
        self.f_2 = os.path.join(self.test_dir, "csv_2.csv")
        df.to_csv(self.f_2, index=False)
        df = pd.DataFrame(
            {
                "dict_column": [
                    "{'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14}",
                ],
                "Value1": [1],
                "Value2": [2],
            }
        )
        self.f_3 = os.path.join(self.test_dir, "csv_3.csv")
        df.to_csv(self.f_3, index=False)
        df = pd.DataFrame(
            {
                "dict_column": [
                    "{'O' : 15}",
                    "{'P' : 16}",
                    "{'Q' : 17}",
                    "{'R' : 18}",
                    "{'Q' : 17}",
                    "{'P' : 16}",
                    "{'P' : 16}",
                    "{'P' : 16}",
                ],
                "Value1": [1, 2, 2, 1, 1, 1, 2, 2],
                "Value2": [1, 1, 1, 1, 2, 2, 2, 2],
            }
        )
        self.f_4 = os.path.join(self.test_dir, "csv_4.csv")
        df.to_csv(self.f_4, index=False)
        df = pd.DataFrame(
            {
                "dict_column": [
                    "{'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22}",
                    "{'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}",
                ],
                "Value1": [1, 2],
                "Value2": [1, 2],
            }
        )
        self.f_5 = os.path.join(self.test_dir, "csv_5.csv")
        df.to_csv(self.f_5, index=False)
    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.test_dir)
    def test_case_1(self):
        df, ax = task_func(self.f_1)
        # Assertions for DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertTrue("dict_column" in df.columns)
        self.assertTrue(isinstance(df.iloc[0]["dict_column"], dict))
        # Assertions for Seaborn PairGrid (plot)
        self.assertIsInstance(ax, sns.axisgrid.PairGrid)
        self.assertTrue(hasattr(ax, "fig"))
        self.assertIsInstance(ax.fig, matplotlib.figure.Figure)
    def test_case_2(self):
        df, ax = task_func(self.f_2)
        # Assertions for DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 4)
        self.assertTrue("dict_column" in df.columns)
        self.assertTrue(isinstance(df.iloc[0]["dict_column"], dict))
        # Assertions for Seaborn PairGrid (plot)
        self.assertIsInstance(ax, sns.axisgrid.PairGrid)
        self.assertTrue(hasattr(ax, "fig"))
        self.assertIsInstance(ax.fig, matplotlib.figure.Figure)
    def test_case_3(self):
        df, ax = task_func(self.f_3)
        # Assertions for DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 1)
        self.assertTrue("dict_column" in df.columns)
        self.assertTrue(isinstance(df.iloc[0]["dict_column"], dict))
        # Assertions for Seaborn PairGrid (plot)
        self.assertIsInstance(ax, sns.axisgrid.PairGrid)
        self.assertTrue(hasattr(ax, "fig"))
        self.assertIsInstance(ax.fig, matplotlib.figure.Figure)
    def test_case_4(self):
        df, ax = task_func(self.f_4)
        # Assertions for DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 8)
        self.assertTrue("dict_column" in df.columns)
        self.assertTrue(isinstance(df.iloc[0]["dict_column"], dict))
        # Assertions for Seaborn PairGrid (plot)
        self.assertIsInstance(ax, sns.axisgrid.PairGrid)
        self.assertTrue(hasattr(ax, "fig"))
        self.assertIsInstance(ax.fig, matplotlib.figure.Figure)
    def test_case_5(self):
        df, ax = task_func(self.f_5)
        # Assertions for DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertTrue("dict_column" in df.columns)
        self.assertTrue(isinstance(df.iloc[0]["dict_column"], dict))
        # Assertions for Seaborn PairGrid (plot)
        self.assertIsInstance(ax, sns.axisgrid.PairGrid)
        self.assertTrue(hasattr(ax, "fig"))
        self.assertIsInstance(ax.fig, matplotlib.figure.Figure)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)