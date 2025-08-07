from collections import Counter
import pandas as pd

def task_func(list_of_menuitems):
    # Helper function to flatten the nested list
    def flatten(nested_list):
        for item in nested_list:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    # Flatten the list of menu items
    flat_list = list(flatten(list_of_menuitems))
    
    # Count the occurrences of each menu item
    item_counts = Counter(flat_list)
    
    # Create a DataFrame from the counter
    df = pd.DataFrame.from_dict(item_counts, orient='index', columns=['Count'])
    
    # Rename the index to 'MenuItem'
    df.index.name = 'MenuItem'
    
    return df
import unittest
class TestCases(unittest.TestCase):
    def test_normal_functionality(self):
        """Test the function with typical nested lists."""
        input_list = [['apple', 'banana'], ['apple'], ['banana', 'orange']]
        expected_df = pd.DataFrame({'Count': [2, 2, 1]}, index=['apple', 'banana', 'orange'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(task_func(input_list), expected_df)
    def test_empty_list(self):
        """Test the function with an empty list."""
        expected_df = pd.DataFrame(columns=['Count'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(task_func([]), expected_df)
    def test_single_level_list(self):
        """Test with a non-nested, single-level list."""
        input_list = [['apple', 'banana', 'apple']]
        expected_df = pd.DataFrame({'Count': [2, 1]}, index=['apple', 'banana'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(task_func(input_list), expected_df)
    def test_uniform_list(self):
        """Test with a list where all sublists contain the same item."""
        input_list = [['apple'], ['apple'], ['apple']]
        expected_df = pd.DataFrame({'Count': [3]}, index=['apple'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(task_func(input_list), expected_df)
    def test_duplicate_items_across_sublists(self):
        """Ensure items appearing in multiple sublists are counted correctly."""
        input_list = [['apple', 'banana'], ['banana', 'banana', 'apple']]
        expected_df = pd.DataFrame({'Count': [2, 3]}, index=['apple', 'banana'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(task_func(input_list), expected_df)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)