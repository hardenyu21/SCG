import pandas as pd
from random import seed, choices, sample

def task_func(L, num_dataframes=5, random_seed=None):
    if not L:
        return pd.DataFrame(), []

    if random_seed is not None:
        seed(random_seed)

    column_names = [chr(i) for i in range(97, 123)]  # Lowercase English letters
    df_list = []

    for _ in range(num_dataframes):
        # Randomly choose 3 rows from L
        sampled_rows = sample(L, min(3, len(L)))
        # Randomly choose 3 column names
        columns = choices(column_names, k=3)
        # Create a DataFrame with the sampled rows and columns
        df = pd.DataFrame(sampled_rows, columns=columns)
        df_list.append(df)

    # Find the common rows between all DataFrames
    common_rows = df_list[0]
    for df in df_list[1:]:
        common_rows = pd.merge(common_rows, df, how='inner')

    return common_rows, df_list

# Example usage
L = [[1, '65', 76], [2, '5', 6]]
common_rows, df_list = task_func(L, num_dataframes=1, random_seed=1)
print(common_rows)
print(df_list)
# Generating fake data for the test cases
import unittest
from faker import Faker
import pandas as pd
# [Your modified task_func_modified function goes here]
fake = Faker()
def generate_fake_data(num_rows=5, num_columns=5):
    """Generate fake data for test cases"""
    fake.seed_instance(12)
    data = []
    for _ in range(num_rows):
        row = [fake.random_int() for _ in range(num_columns)]
        data.append(row)
    return data
# Writing the blackbox test function
class TestCases(unittest.TestCase):
    def test_rng(self):
        data = generate_fake_data(5, 3)
        result1, _ = task_func(data, random_seed=12)
        result2, _ = task_func(data, random_seed=12)
        result3, _ = task_func(data, random_seed=1)
        pd.testing.assert_frame_equal(result1, result2)
        try:
            pd.testing.assert_frame_equal(result1, result3)
        except AssertionError:
            # frames are not equal
            pass
        else:
            # frames are equal
            raise AssertionError
    def test_case_1(self):
        data = generate_fake_data(5, 3)
        result, df_list = task_func(data, random_seed=123)
        expected = pd.DataFrame(
            {'b': {0: 7775, 1: 3729, 3: 177, 4: 5730}, 'c': {0: 4407, 1: 9145, 3: 6139, 4: 2336}, 'k': {0: 8669, 1: 27, 3: 7905, 4: 6252}}        )
        pd.testing.assert_frame_equal(result, expected)
        self.assertEqual(len(df_list), 5)
        self.assertEqual(len(df_list[0]), 3)
    def test_case_2(self):
        data = generate_fake_data(10, 5)
        result, df_list = task_func(data, random_seed=42)
        expected = pd.DataFrame(
            {'q': {0: 995, 1: 5120, 2: 7775, 5: 7540, 6: 8413}, 'a': {0: 8338, 1: 9144, 2: 4407, 5: 9854, 6: 5521}, 'h': {0: 3657, 1: 2679, 2: 8669, 5: 3729, 6: 6629}, 'f': {0: 1490, 1: 841, 2: 5730, 5: 9145, 6: 1431}, 't': {0: 6943, 1: 9095, 2: 2336, 5: 27, 6: 304}}
        )
        pd.testing.assert_frame_equal(result, expected)
        self.assertEqual(len(df_list), 5)
        self.assertEqual(len(df_list[0]), 3)
    def test_case_3(self):
        data = generate_fake_data(8, 4)
        result, df_list = task_func(data, random_seed=121, num_dataframes=10)
        expected = pd.DataFrame(
{'c': {0: 7209, 2: 1431, 3: 7905, 4: 1222, 5: 3729, 6: 3444, 11: 7775, 16: 2336}, 'p': {0: 6023, 2: 304, 3: 4490, 4: 8413, 5: 9145, 6: 963, 11: 4407, 16: 6252}, 'k': {0: 2658, 2: 995, 3: 7540, 4: 5521, 5: 27, 6: 9440, 11: 8669, 16: 177}, 'x': {0: 5565, 2: 8338, 3: 9854, 4: 6629, 5: 2380, 6: 3270, 11: 5730, 16: 6139}}  
        )
        pd.testing.assert_frame_equal(result, expected)
        self.assertEqual(len(df_list), 10)
        self.assertEqual(len(df_list[0]), 3)
    def test_case_4(self):
        data = generate_fake_data(3, 2)
        result, df_list = task_func(data, random_seed=1233)
        expected = pd.DataFrame(
            {'i': {0: 7775, 2: 2336, 7: 8669}, 'n': {0: 4407, 2: 6252, 7: 5730}}
        )
        pd.testing.assert_frame_equal(result, expected)
        self.assertEqual(len(df_list), 5)
        self.assertEqual(len(df_list[0]), 3)
    def test_empty_input(self):
        data = []
        result, df_list = task_func(data, random_seed=123)
        self.assertTrue(result.empty)
        self.assertEqual(len(df_list), 0)
    def test_single_row_input(self):
        data = [[1, 2, 3]]
        result, df_list = task_func(data, random_seed=123)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(df_list), 5)
        self.assertEqual(len(df_list[0]), 3)
    def test_single_column_input(self):
        data = [[1], [2], [3]]
        result, df_list = task_func(data, random_seed=123)
        self.assertEqual(result.shape[1], 1)
        self.assertEqual(len(df_list), 5)
        self.assertEqual(len(df_list[0]), 3)
    def test_large_number_of_rows(self):
        data = generate_fake_data(1000, 5)
        result, df_list = task_func(data, random_seed=123)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertEqual(len(df_list), 5)
        self.assertEqual(len(df_list[0]), 3)
    def test_non_uniform_row_lengths(self):
        data = [[1, 2], [3, 4, 5], [6]]
        with self.assertRaises(ValueError):
            task_func(data, random_seed=123)
    def test_all_identical_rows(self):
        data = [[1, 2, 3]] * 5
        result, df_list = task_func(data, random_seed=123)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(df_list), 5)
        self.assertEqual(len(df_list[0]), 3)
    def test_no_common_rows(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result, df_list = task_func(data, random_seed=123)
        expected = pd.DataFrame(
            {'b': {0: 1, 1: 7, 3: 4}, 'c': {0: 2, 1: 8, 3: 5}, 'k': {0: 3, 1: 9, 3: 6}}
        )
        pd.testing.assert_frame_equal(result, expected)
        self.assertEqual(len(df_list), 5)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)