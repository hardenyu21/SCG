import pandas as pd
import random
import re

def task_func(data_list, seed=42):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Function to normalize spaces and randomize the order of substrings
    def randomize_and_normalize(s):
        # Normalize spaces: ensure a single space follows each comma
        normalized = re.sub(r'\s*,\s*', ', ', s)
        # Split the string into substrings
        substrings = normalized.split(', ')
        # Randomize the order of substrings
        random.shuffle(substrings)
        # Join the substrings back into a single string
        randomized = ', '.join(substrings)
        return randomized
    
    # Apply the function to each string in the list
    randomized_list = [randomize_and_normalize(s) for s in data_list]
    
    # Create a DataFrame with original and randomized strings
    df = pd.DataFrame({
        'Original String': data_list,
        'Randomized String': randomized_list
    })
    
    return df

# Example usage:
data_list = [
    "apple, banana, cherry",
    "dog, cat, mouse",
    "red, blue, green, yellow"
]

df = task_func(data_list)
print(df)
import unittest
import pandas as pd
import re
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic functionality with a reproducible seed
        input_data = ["a, b", "c, d, e"]
        df = task_func(input_data, seed=42)
        self.assertEqual(len(df), 2)
        self.assertListEqual(df["Original String"].tolist(), input_data)
        self.assertNotEqual(
            df["Original String"].tolist(), df["Randomized String"].tolist()
        )
        self.assertSetEqual(
            set(df["Original String"].tolist()[0].split(", ")),
            set(df["Randomized String"].tolist()[0].split(", ")),
        )
    def test_case_2(self):
        # Test function's behavior with an empty input list
        input_data = []
        df = task_func(input_data)
        self.assertEqual(len(df), 0)
    def test_case_3(self):
        # Test with single items (no commas) to verify output matches input exactly
        input_data = ["a", "b", "c"]
        df = task_func(input_data)
        self.assertListEqual(
            df["Original String"].tolist(), df["Randomized String"].tolist()
        )
    def test_case_4(self):
        # Test with strings containing only commas
        input_data = [",,,", ",,"]
        expected_output = [", , , ", ", , "]
        df = task_func(input_data)
        self.assertTrue(
            all(df["Randomized String"].apply(lambda x: x in expected_output))
        )
    def test_case_5(self):
        # Test strings with inconsistent use of spaces and delimiters
        input_data = ["a,b,  c", "d ,e, f"]  # Inputs with inconsistent spacing
        df = task_func(input_data, seed=24)
        for i in range(len(input_data)):
            original_substrings = set(re.split("\s*,\s*", input_data[i]))
            randomized_substrings = set(df["Randomized String"].iloc[i].split(", "))
            self.assertEqual(
                original_substrings,
                randomized_substrings,
            )
    def test_case_6(self):
        # Test with strings that include special characters
        input_data = ["!@#, $%^", "&*(), )(_+"]
        df = task_func(input_data, seed=99)
        self.assertEqual(len(df), 2)
        for orig, rand in zip(df["Original String"], df["Randomized String"]):
            self.assertSetEqual(set(orig.split(", ")), set(rand.split(", ")))
    def test_case_7(self):
        # Test random seed
        input_data = ["lamp, bag, mirror", "table, chair, vase"]
        df1 = task_func(input_data, seed=42)
        df2 = task_func(input_data, seed=42)
        self.assertListEqual(
            df1["Randomized String"].tolist(), df2["Randomized String"].tolist()
        )
    def test_case_8(self):
        # Test the handling of non-standard separators
        input_data = ["a;b;c", "d:e:f"]
        df = task_func(input_data)
        self.assertListEqual(
            df["Original String"].tolist(), df["Randomized String"].tolist()
        )
    def test_case_9(self):
        ## Test handling of strings with commas not followed by spaces
        input_data = ["a,b,c", "d,e,f"]
        df = task_func(input_data, seed=42)
        for idx in range(len(input_data)):
            original_substrings = set(re.split(",\s*", input_data[idx].strip()))
            randomized_substrings = set(df["Randomized String"].iloc[idx].split(", "))
            self.assertEqual(
                original_substrings,
                randomized_substrings,
                "Substrings should be preserved and normalized after randomization.",
            )
    def test_case_10(self):
        # Test handling of strings with leading or trailing spaces
        input_data = [" a, b, c ", " d, e, f "]
        df = task_func(input_data, seed=42)
        for idx in range(len(input_data)):
            original_substrings = set(
                x.strip() for x in re.split(",\s*", input_data[idx].strip())
            )
            randomized_substrings = set(
                x.strip() for x in df["Randomized String"].iloc[idx].split(", ")
            )
            self.assertEqual(
                original_substrings,
                randomized_substrings,
                "Ensure substrings match after randomization, ignoring leading/trailing spaces.",
            )
    def test_case_11(self):
        # Test handling of strings with multiple spaces after a comma
        input_data = ["a,  b,   c", "d,    e, f"]
        df = task_func(input_data, seed=42)
        for rand_str in df["Randomized String"].tolist():
            self.assertTrue(
                ",  " not in rand_str
                and ",   " not in rand_str
                and ",    " not in rand_str,
                "Multiple spaces after commas should not appear in output.",
            )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)