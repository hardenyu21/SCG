import pandas as pd
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt

COLUMN_NAMES = ["Name", "Email", "Age", "Country"]

def task_func(text):
    # Define the regular expression pattern
    pattern = r"Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)"
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Create a DataFrame from the matches
    df = pd.DataFrame(matches, columns=COLUMN_NAMES)
    
    # Convert the 'Age' column to integer
    df['Age'] = df['Age'].astype(int)
    
    # Plot the age distribution using seaborn
    sns.histplot(df['Age'], bins=10, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the DataFrame
    return df
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        input_text = "Name: John Doe, Email: john.doe@example.com, Age: 30, Country: USA\nName: Jane Doe, Email: jane.doe@example.com, Age: 25, Country: UK"
        df = task_func(input_text)
        self.assertEqual(df.shape, (2, 4))
        self.assertListEqual(list(df.columns), ["Name", "Email", "Age", "Country"])
        self.assertListEqual(
            df.iloc[0].tolist(), ["John Doe", "john.doe@example.com", 30, "USA"]
        )
        self.assertListEqual(
            df.iloc[1].tolist(), ["Jane Doe", "jane.doe@example.com", 25, "UK"]
        )
    def test_case_2(self):
        input_text = (
            "Name: Alex Smith, Email: alex.smith@example.com, Age: 35, Country: Canada"
        )
        df = task_func(input_text)
        self.assertEqual(df.shape, (1, 4))
        self.assertListEqual(
            df.iloc[0].tolist(), ["Alex Smith", "alex.smith@example.com", 35, "Canada"]
        )
    def test_case_3(self):
        input_text = ""
        df = task_func(input_text)
        self.assertTrue(df.empty)
    def test_case_4(self):
        input_text = (
            "Name: Alex Smith, Email: alex.smith@example.com, Age: 35, Country: Canada"
        )
        df = task_func(input_text)
        self.assertEqual(df.shape, (1, 4))
        self.assertListEqual(
            df.iloc[0].tolist(), ["Alex Smith", "alex.smith@example.com", 35, "Canada"]
        )
    def test_case_5(self):
        input_text = """Name: Alex Smith, Email: alex.smith@example.com, Age: 35, Country: Canada
        Name: Bob Miller, Email: bob.miller@example.com, Age: 25, Country: USA
        Name: Anna Karin, Email: anna.karin@example.com, Age: 47, Country: Finland
        """
        df = task_func(input_text)
        self.assertEqual(df.shape, (3, 4))
        self.assertListEqual(list(df.columns), ["Name", "Email", "Age", "Country"])
        self.assertListEqual(
            df.iloc[0].tolist(), ["Alex Smith", "alex.smith@example.com", 35, "Canada"]
        )
        self.assertListEqual(
            df.iloc[1].tolist(), ["Bob Miller", "bob.miller@example.com", 25, "USA"]
        )
        self.assertListEqual(
            df.iloc[2].tolist(), ["Anna Karin", "anna.karin@example.com", 47, "Finland"]
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)