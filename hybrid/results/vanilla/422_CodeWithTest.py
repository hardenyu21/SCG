import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    # Check if the column_to_remove exists in the DataFrame and drop it if it does
    if column_to_remove in df.columns:
        df = df.drop(columns=[column_to_remove])
    
    # Separate the target column from the features
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    return X_train, X_test, y_train, y_test
import unittest
import pandas as pd
from sklearn.utils._param_validation import InvalidParameterError
class TestCases(unittest.TestCase):
    def setUp(self):
        # basic test dataframe
        self.df = {"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8], "c": [7, 8, 9, 10, 11]}
    def shape_testing_helper(self, expected_train_len, expected_test_len, split_data):
        X_train, X_test, y_train, y_test = split_data
        self.assertTrue(len(X_train) == expected_train_len)
        self.assertTrue(len(y_train) == expected_train_len)
        self.assertTrue(len(X_test) == expected_test_len)
        self.assertTrue(len(y_test) == expected_test_len)
    def test_case_1(self):
        # Dataframe with a 'c' column to be removed
        X_train, X_test, y_train, y_test = task_func(self.df, "b")
        self.assertEqual("a", X_train.columns[0])
        self.assertEqual("b", y_train.name)
        self.assertNotIn("c", X_train.columns)
        self.shape_testing_helper(4, 1, (X_train, X_test, y_train, y_test))
    def test_case_2(self):
        # Specify removal of separate column
        X_train, X_test, y_train, y_test = task_func(self.df, "a", column_to_remove="b")
        self.assertEqual("c", X_train.columns[0])
        self.assertEqual("a", y_train.name)
        self.assertNotIn("b", X_train.columns)
        self.shape_testing_helper(4, 1, (X_train, X_test, y_train, y_test))
    def test_case_3(self):
        # Dataframe doesn't have column to be removed
        X_train, X_test, y_train, y_test = task_func(self.df, "a", column_to_remove="FOO")
        self.assertEqual("a", y_train.name)
        self.assertIn("b", X_train.columns)
        self.assertIn("c", X_train.columns)
        self.shape_testing_helper(4, 1, (X_train, X_test, y_train, y_test))
    def test_case_4(self):
        # Change testing ratio
        X_train, X_test, y_train, y_test = task_func(self.df, "a", test_size=0.8)
        self.shape_testing_helper(1, 4, (X_train, X_test, y_train, y_test))
    def test_case_5(self):
        # Should fail if specify invalid ratio
        with self.assertRaises(InvalidParameterError):
            task_func(self.df, "a", test_size=-999)
        with self.assertRaises(InvalidParameterError):
            task_func(self.df, "a", test_size="foo")
    def test_case_6(self):
        # Testing with a dataframe having mixed data types
        df = {
                "a": [pd.NA, 2.3, 3.4, 4.5, 5.5],
                "b": ["one", "two", pd.NA, "four", "five"],
                "c": [True, False, True, False, pd.NA],
            }
        X_train, X_test, y_train, y_test = task_func(df, "b")
        self.assertNotIn("c", X_train.columns)
        self.shape_testing_helper(4, 1, (X_train, X_test, y_train, y_test))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)