import pickle
import os
import pandas as pd

def task_func(df, file_name="save.pkl"):
    # Save the DataFrame to a pickle file
    with open(file_name, 'wb') as file:
        pickle.dump(df, file)
    
    # Read the DataFrame back from the pickle file
    with open(file_name, 'rb') as file:
        loaded_df = pickle.load(file)
    
    # Delete the intermediate pickle file
    os.remove(file_name)
    
    # Return the loaded DataFrame
    return loaded_df
import unittest
import os
import pandas as pd
import numpy as np
import tempfile
from datetime import datetime
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
    def tearDown(self):
        self.temp_dir.cleanup()
    def test_case_1(self):
        # Test with random integers
        df = pd.DataFrame(
            np.random.randint(0, 100, size=(100, 4)), columns=list("ABCD")
        )
        file_path = os.path.join(self.temp_dir.name, "test.pkl")
        loaded_df = task_func(df, file_path)
        self.assertTrue(df.equals(loaded_df))
        self.assertFalse(os.path.exists(file_path))
    def test_case_2(self):
        # Test with floats
        df = pd.DataFrame(np.random.rand(50, 3), columns=list("XYZ"))
        file_path = os.path.join(self.temp_dir.name, "floats.pkl")
        loaded_df = task_func(df, file_path)
        self.assertTrue(df.equals(loaded_df))
        self.assertFalse(os.path.exists(file_path))
    def test_case_3(self):
        # Test with strings
        df = pd.DataFrame({"A": ["foo", "bar", "baz"], "B": ["qux", "quux", "corge"]})
        file_path = os.path.join(self.temp_dir.name, "strings.pkl")
        loaded_df = task_func(df, file_path)
        self.assertTrue(df.equals(loaded_df))
        self.assertFalse(os.path.exists(file_path))
    def test_case_4(self):
        # Test with empty dataframe
        df = pd.DataFrame()
        file_path = os.path.join(self.temp_dir.name, "empty.pkl")
        loaded_df = task_func(df, file_path)
        self.assertTrue(df.equals(loaded_df))
        self.assertFalse(os.path.exists(file_path))
    def test_case_5(self):
        # Test with datetime
        df = pd.DataFrame(
            {"Date": [datetime(2020, 1, 1), datetime(2020, 1, 2)], "Value": [10, 20]}
        )
        file_path = os.path.join(self.temp_dir.name, "datetime.pkl")
        loaded_df = task_func(df, file_path)
        self.assertTrue(df.equals(loaded_df))
        self.assertFalse(os.path.exists(file_path))
    def test_case_6(self):
        # Test larger dataframe
        df = pd.DataFrame(
            np.random.randint(0, 100, size=(10000, 10)),
            columns=[f"Col{i}" for i in range(10)],
        )
        file_path = os.path.join(self.temp_dir.name, "large.pkl")
        loaded_df = task_func(df, file_path)
        self.assertTrue(df.equals(loaded_df))
        self.assertFalse(os.path.exists(file_path))
    def test_case_7(self):
        # Test single entry dataframe
        df = pd.DataFrame({"Single": [42]})
        file_path = os.path.join(self.temp_dir.name, "test_file_small.pkl")
        loaded_df = task_func(df, file_path)
        self.assertTrue(
            df.equals(loaded_df), "Loaded DataFrame does not match the original."
        )
        self.assertFalse(os.path.exists(file_path))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)