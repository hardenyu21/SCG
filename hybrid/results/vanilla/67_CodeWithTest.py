import pandas as pd
import re
import os

def task_func(dir_path: str, pattern: str = '^EMP'):
    # Compile the regex pattern for matching file names
    regex = re.compile(pattern)
    
    # List to store file names and their sizes
    file_data = []
    
    # Iterate over all files in the directory
    for file_name in os.listdir(dir_path):
        # Check if the file name matches the pattern
        if regex.match(file_name):
            # Get the full path of the file
            file_path = os.path.join(dir_path, file_name)
            # Check if it's a file and not a directory
            if os.path.isfile(file_path):
                # Get the size of the file
                file_size = os.path.getsize(file_path)
                # Append the file name and size to the list
                file_data.append({'File': file_name, 'Size': file_size})
    
    # Sort the file data by file name
    file_data.sort(key=lambda x: x['File'])
    
    # Create a pandas DataFrame from the file data
    df = pd.DataFrame(file_data)
    
    return df
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        self.test_dir = "data/task_func"
        os.makedirs(self.test_dir, exist_ok=True)
        self.f_1 = os.path.join(self.test_dir, "EMP001.doc")
        self.f_2 = os.path.join(self.test_dir, "EMP002.doc")
        self.f_3 = os.path.join(self.test_dir, "EMP003.doc")
        self.f_4 = os.path.join(self.test_dir, "NOTEMP1.txt")
        self.f_5 = os.path.join(self.test_dir, "NOTEMP2.txt")
        self.f_6 = os.path.join(self.test_dir, "A1.txt")
        self.f_7 = os.path.join(self.test_dir, "A2.txt")
        self.f_8 = os.path.join(self.test_dir, "A3.txt")
        self.f_9 = os.path.join(self.test_dir, "B1.py")
        self.f_10 = os.path.join(self.test_dir, "B2.py")
        for i, element in enumerate([self.f_1, self.f_2, self.f_3, self.f_4, self.f_5, self.f_6, self.f_7, self.f_8, self.f_9, self.f_10]) :
            with open(element, "w") as f :
                f.write(f"Test content {i+1}")
    def tearDown(self):
        for filename in [
            self.f_1, self.f_2, self.f_3, self.f_4, self.f_5,
            self.f_6, self.f_7, self.f_8, self.f_9, self.f_10
        ]:
            os.remove(filename)
        os.rmdir(self.test_dir)
    def test_case_1(self):
        report = task_func(self.test_dir)
        self.assertEqual(len(report), 3)
        for i, row in report.iterrows():
            self.assertEqual(row['Size'], os.path.getsize(os.path.join(self.test_dir, f"EMP00{i+1}.doc")))
    def test_case_2(self):
        report = task_func(self.test_dir, pattern="^NOTEMP")
        self.assertEqual(len(report), 2)
        for i, row in report.iterrows():
            self.assertEqual(row['Size'], os.path.getsize(os.path.join(self.test_dir, f"NOTEMP{i+1}.txt")))
    def test_case_3(self):
        report = task_func(self.test_dir, pattern="NOTFOUND")
        expected_df = pd.DataFrame(
            {
                "File" : [],
                "Size" : []
            }
        ).astype({"File" : "object", "Size" : "object"})
        self.assertTrue(
            report.empty
        )
        self.assertTrue(report.shape == expected_df.shape)
    def test_case_4(self):
        report = task_func(self.test_dir, pattern="^A")
        self.assertEqual(len(report), 3)
        for i, row in report.iterrows():
            self.assertEqual(row['Size'], os.path.getsize(os.path.join(self.test_dir, f"A{i+1}.txt")))
    def test_case_5(self):
        report = task_func(self.test_dir, pattern="^B")
        self.assertEqual(len(report), 2)
        for i, row in report.iterrows():
            self.assertEqual(row['Size'], os.path.getsize(os.path.join(self.test_dir, f"B{i+1}.py")))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)