import re
import random
import pandas as pd

def task_func(data_list, seed=None):
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Initialize lists to store original and shuffled strings
    original_strings = []
    shuffled_strings = []
    
    # Iterate over each string in the input list
    for original_string in data_list:
        # Split the string into substrings based on commas
        substrings = re.split(r'\s*,\s*', original_string.strip())
        
        # Shuffle the substrings
        shuffled_substrings = substrings[:]
        random.shuffle(shuffled_substrings)
        
        # Join the shuffled substrings back into a single string
        shuffled_string = ', '.join(shuffled_substrings)
        
        # Append the original and shuffled strings to their respective lists
        original_strings.append(original_string)
        shuffled_strings.append(shuffled_string)
    
    # Create a DataFrame with the original and shuffled strings
    df = pd.DataFrame({
        'Original String': original_strings,
        'Shuffled String': shuffled_strings
    })
    
    return df

# Example usage:
# data_list = ["apple, banana, cherry", "dog, elephant, frog"]
# df = task_func(data_list, seed=42)
# print(df)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        input_data = ["lamp, bag, mirror", "table, chair"]
        output_df = task_func(input_data)
        self.assertEqual(output_df["Original String"].iloc[0], "lamp, bag, mirror")
        self.assertEqual(output_df["Original String"].iloc[1], "table, chair")
        self.assertEqual(len(output_df["Shuffled String"].iloc[0].split(", ")), 3)
        self.assertEqual(len(output_df["Shuffled String"].iloc[1].split(", ")), 2)
    def test_case_2(self):
        # Test single character substrings
        input_data = ["A, B, C, D", "E, F, G"]
        output_df = task_func(input_data)
        self.assertEqual(output_df["Original String"].iloc[0], "A, B, C, D")
        self.assertEqual(output_df["Original String"].iloc[1], "E, F, G")
        self.assertEqual(len(output_df["Shuffled String"].iloc[0].split(", ")), 4)
        self.assertEqual(len(output_df["Shuffled String"].iloc[1].split(", ")), 3)
    def test_case_3(self):
        # Test single-item list
        input_data = ["word1, word2"]
        output_df = task_func(input_data)
        self.assertEqual(output_df["Original String"].iloc[0], "word1, word2")
        self.assertEqual(len(output_df["Shuffled String"].iloc[0].split(", ")), 2)
    def test_case_4(self):
        # Tests shuffling with an empty string
        input_data = [""]
        output_df = task_func(input_data)
        self.assertEqual(output_df["Original String"].iloc[0], "")
        self.assertEqual(output_df["Shuffled String"].iloc[0], "")
    def test_case_5(self):
        # Test shuffling single substring (no shuffling)
        input_data = ["single"]
        output_df = task_func(input_data)
        self.assertEqual(output_df["Original String"].iloc[0], "single")
        self.assertEqual(output_df["Shuffled String"].iloc[0], "single")
    def test_case_6(self):
        # Testing the effect of a specific random seed to ensure reproducibility
        input_data = ["a, b, c, d"]
        output_df1 = task_func(input_data, seed=42)
        output_df2 = task_func(input_data, seed=42)
        self.assertEqual(
            output_df1["Shuffled String"].iloc[0], output_df2["Shuffled String"].iloc[0]
        )
    def test_case_7(self):
        # Tests shuffling with varying spaces around commas
        input_data = ["one,two, three"]
        corrected_expected_shuffled = "two, one, three"
        output_df = task_func(input_data, seed=42)
        self.assertEqual(output_df["Original String"].iloc[0], "one,two, three")
        self.assertEqual(
            output_df["Shuffled String"].iloc[0], corrected_expected_shuffled
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)