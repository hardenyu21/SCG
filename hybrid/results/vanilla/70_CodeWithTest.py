import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['email', 'list']

def task_func(json_file):
    try:
        # Load data from JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        # Check if data is empty
        if not data:
            return pd.DataFrame(columns=['email', 'list', 'sum', 'mean']), None
        
        # Convert JSON data to DataFrame
        df = pd.DataFrame(data, columns=COLUMNS)
        
        # Calculate sum and mean for each email
        df['sum'] = df['list'].apply(np.sum)
        df['mean'] = df['list'].apply(np.mean)
        
        # Plot the sum and mean values
        fig, ax = plt.subplots()
        df.plot(kind='bar', x='email', y=['sum', 'mean'], ax=ax)
        ax.set_title('Sum and Mean of Lists for Each Email')
        ax.set_ylabel('Values')
        ax.set_xlabel('Email')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return df, ax
    
    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean']), None
    except json.JSONDecodeError:
        print(f"Error: The file {json_file} is not a valid JSON.")
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean']), None
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean']), None

# Example usage:
# df, ax = task_func('emails.json')
# plt.show() if ax is not None else print("No data to plot.")
import os
import shutil
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        self.test_dir = 'data/task_func'
        os.makedirs(self.test_dir, exist_ok=True)
        self.f_1 = os.path.join(self.test_dir, "json_1.json")
        self.f_2 = os.path.join(self.test_dir, "json_2.json")
        self.f_3 = os.path.join(self.test_dir, "json_3.json")
        self.f_4 = os.path.join(self.test_dir, "json_4.json")
        self.f_5 = os.path.join(self.test_dir, "json_5.json")
        with open(self.f_1, "w") as fout :
            json.dump(
                [
                    {
                        "email" : "first@example.com",
                        "list" : [12, 17, 29, 45, 7, 3]
                    },
                    {
                        "email" : "second@example.com",
                        "list" : [1, 1, 3, 73, 21, 19, 12]
                    },
                    {
                        "email" : "third@example.com",
                        "list" : [91, 23, 7, 14, 66]
                    }
                ],
                fout
            )
        with open(self.f_2, "w") as fout :
            json.dump(
                [
                    {
                        "email" : "fourth@example.com",
                        "list" : [12, 21, 35, 2, 1]
                    },
                    {
                        "email" : "fifth@example.com",
                        "list" : [13, 4, 10, 20]
                    },
                    {
                        "email" : "sixth@example.com",
                        "list" : [82, 23, 7, 14, 66]
                    },
                    {
                        "email" : "seventh@example.com",
                        "list" : [111, 23, 4]
                    }
                ],
                fout
            )
        with open(self.f_3, "w") as fout :
            json.dump(
                [
                    {
                        "email" : "eight@example.com",
                        "list" : [1, 2, 3, 4, 5]
                    },
                    {
                        "email" : "ninth@example.com",
                        "list" : [6, 7, 8, 9, 10]
                    }
                ],
                fout
            )
        with open(self.f_4, "w") as fout :
            json.dump(
                [
                    {
                        "email" : "tenth@example.com",
                        "list" : [11, 12, 13, 14, 15]
                    }
                ],
                fout
            )
        with open(self.f_5, "w") as fout :
            json.dump(
                [],
                fout
            )
    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    def test_case_1(self):
        # Test with sample JSON data
        df, ax = task_func(self.f_1)
        # Assert DataFrame values
        self.assertEqual(df["email"].tolist(), ["first@example.com", "second@example.com", "third@example.com"])
        self.assertEqual(df["sum"].tolist(), [113, 130, 201])
        self.assertEqual(df["mean"].tolist(), [113/6.0, 130/7.0, 201/5.0])
        # Assert plot attributes
        self.assertEqual(ax.get_title(), '')
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], ['0', '1', '2'])
        self.assertListEqual([label.get_text() for label in ax.get_legend().get_texts()], ['sum', 'mean'])
    def test_case_2(self):
        # Test with sample JSON data
        df, ax = task_func(self.f_2)
        # Assert DataFrame values
        self.assertEqual(df["email"].tolist(), ["fourth@example.com", "fifth@example.com", "sixth@example.com", "seventh@example.com"])
        self.assertEqual(df["sum"].tolist(), [71, 47, 192, 138])
        self.assertEqual(df["mean"].tolist(), [71/5.0, 47/4.0, 192/5.0, 138/3.0])
        # Assert plot attributes
        self.assertEqual(ax.get_title(), '')
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], ['0', '1', '2', '3'])
        self.assertListEqual([label.get_text() for label in ax.get_legend().get_texts()], ['sum', 'mean'])
    def test_case_3(self):
        # Test with sample JSON data
        df, ax = task_func(self.f_3)
        # Assert DataFrame values
        self.assertEqual(df["email"].tolist(), ["eight@example.com", "ninth@example.com"])
        self.assertEqual(df["sum"].tolist(), [15.0, 40.0])
        self.assertEqual(df["mean"].tolist(), [3.0, 8.0])
        # Assert plot attributes
        self.assertEqual(ax.get_title(), '')
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], ['0', '1'])
        self.assertListEqual([label.get_text() for label in ax.get_legend().get_texts()], ['sum', 'mean'])
    def test_case_4(self):
        # Test with sample JSON data
        df, ax = task_func(self.f_4)
        # Assert DataFrame values
        self.assertEqual(df["email"].tolist(), ["tenth@example.com"])
        self.assertEqual(df["sum"].tolist(), [65.0])
        self.assertEqual(df["mean"].tolist(), [13.0])
        # Assert plot attributes
        self.assertEqual(ax.get_title(), '')
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], ['0'])
        self.assertListEqual([label.get_text() for label in ax.get_legend().get_texts()], ['sum', 'mean'])
    def test_case_5(self):
        # Test with empty JSON data
        df, ax = task_func(self.f_5)
        self.assertIsNone(ax)
        self.assertTrue(df.empty)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)