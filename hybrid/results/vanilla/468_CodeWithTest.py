import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Convert numeric values to floats
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Plot the data
    fig, ax = plt.subplots()
    for col in columns:
        if col in df.columns:
            ax.plot(df[col], label=col)
    ax.set_title('Line Chart of Specified Columns')
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.legend()
    
    # Compute the cube-root of the data
    cube_root_series = df[columns].apply(np.cbrt)
    
    # Return the DataFrame, Axes, and Series
    return df, ax, cube_root_series

# Example usage:
# df, ax, cube_root_series = task_func("data.csv", ["A", "B", "C"])
# plt.show()
import unittest
import tempfile
import pandas as pd
import matplotlib.pyplot as plt
import os
def round_dict(d, digits):
    return {k: {i: round(v, digits) for i, v in subdict.items()} for k, subdict in
            d.items()}
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_files = {}
        # Data setups for different scenarios
        self.data_sets = {
            "int": pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}),
            "varied": pd.DataFrame(
                {
                    "IntColumn": [1, 2, 3],
                    "FloatColumn": [1.1, 2.2, 3.3],
                    "StringColumn": ["4", "5", "6"],
                }
            ),
            "varied_invalid": pd.DataFrame(
                {
                    "IntColumn": [1, 2, 3],
                    "FloatColumn": [1.1, 2.2, 3.3],
                    "StringColumn": ["a", "b", "c"],
                }
            ),
        }
        # Write data sets to temporary files
        for key, df in self.data_sets.items():
            temp_file_path = os.path.join(self.test_dir.name, f"{key}.csv")
            df.to_csv(temp_file_path, index=False, header=True)
            self.temp_files[key] = temp_file_path
    def tearDown(self):
        self.test_dir.cleanup()
        plt.close("all")
    def test_case_1(self):
        file_path = self.temp_files["int"]
        df, ax, croot = task_func(file_path=file_path, columns=["A", "B", "C"])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(df.columns.tolist(), ["A", "B", "C"])
        self.assertTrue((df["A"].tolist() == [1, 2, 3]))
        self.assertTrue((df["B"].tolist() == [4, 5, 6]))
        self.assertTrue((df["C"].tolist() == [7, 8, 9]))
        rounded_croot = round_dict(croot.to_dict(), 6)
        self.assertEqual(rounded_croot,
                         {'A': {0: 1.0, 1: 1.259921, 2: 1.44225},
                          'B': {0: 1.587401, 1: 1.709976,
                                2: 1.817121},
                          'C': {0: 1.912931, 1: 2.0, 2: 2.080084}})
    def test_case_2(self):
        file_path = self.temp_files["int"]
        with self.assertRaises(KeyError):
            task_func(file_path=file_path, columns=["A", "B", "Nonexistent"])
    def test_case_3(self):
        file_path = self.temp_files["varied"]
        df, ax, croot = task_func(
            file_path=file_path, columns=["IntColumn", "FloatColumn", "StringColumn"]
        )
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(df["IntColumn"].equals(pd.Series([1.0, 2.0, 3.0])))
        self.assertTrue(df["FloatColumn"].equals(pd.Series([1.1, 2.2, 3.3])))
        self.assertTrue(df["StringColumn"].equals(pd.Series([4.0, 5.0, 6.0])))
        rounded_croot = round_dict(croot.to_dict(), 6)
        self.assertEqual(rounded_croot, {
            'IntColumn': {0: 1.0, 1: 1.259921, 2: 1.44225},
            'FloatColumn': {0: 1.03228, 1: 1.300591,
                            2: 1.488806},
            'StringColumn': {0: 1.587401, 1: 1.709976,
                             2: 1.817121}})
    def test_case_4(self):
        file_path = self.temp_files["varied_invalid"]
        with self.assertRaises(Exception):
            task_func(file_path=file_path, columns=["StringColumn"])
    def test_case_5(self):
        with self.assertRaises(FileNotFoundError):
            task_func(file_path="nonexistent_file.csv")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)