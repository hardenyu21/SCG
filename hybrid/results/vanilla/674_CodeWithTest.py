import pandas as pd
import os

def task_func(filename):
    # Check if the file exists
    if not os.path.exists(filename):
        return

    # Read the CSV file
    df = pd.read_csv(filename)

    # Reverse the order of the lines, excluding the header
    df_reversed = df.iloc[::-1].reset_index(drop=True)

    # Write the inverted lines back into the file
    df_reversed.to_csv(filename, index=False)

    # Move the cursor back to the beginning of the file
    with open(filename, 'r+') as file:
        file.seek(0)
import unittest
class TestCases(unittest.TestCase):
    def base(self, filename, contents, expected):
        # Create file
        with open(filename, 'w') as f:
            f.write(contents)
        # Run function
        task_func(filename)
        # Check file
        with open(filename, 'r') as f:
            self.assertEqual(f.read().strip(), expected.strip())
        # Remove file
        os.remove(filename)
    def test_case_1(self):
        self.base('file.csv', 'a,b,c\n1,2,3\n4,5,6\n7,8,9', 'a,b,c\n7,8,9\n4,5,6\n1,2,3')
    def test_case_2(self):
        self.base('file.csv', 'a,b,c\n1,2,3\n4,5,6', 'a,b,c\n4,5,6\n1,2,3')
    def test_case_3(self):
        self.base('file.csv', 'a,b,c\n1,2,3', 'a,b,c\n1,2,3')
    def test_case_4(self):
        self.base('file.csv', 'a,b,c', 'a,b,c')
    def test_case_5(self):
        self.base('file.csv', '', '')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)