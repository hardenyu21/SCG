import pandas as pd
import itertools
import random

def task_func(colors, states):
    # Generate the Cartesian product of colors and states
    combinations = list(itertools.product(colors, states))
    
    # Shuffle the combinations
    random.shuffle(combinations)
    
    # Determine the number of columns for the DataFrame
    num_columns = min(len(colors), len(states))
    
    # Calculate the number of rows needed for each column
    num_rows = len(combinations) // num_columns
    remainder = len(combinations) % num_columns
    
    # Create a list to hold the data for each column
    column_data = []
    
    # Distribute the combinations into columns
    start_index = 0
    for i in range(num_columns):
        # Calculate the end index for the current column
        end_index = start_index + num_rows + (1 if i < remainder else 0)
        # Extract the combinations for the current column
        column_combinations = combinations[start_index:end_index]
        # Format the combinations as "Color:State"
        formatted_column = [f"{color}:{state}" for color, state in column_combinations]
        # Add the formatted column to the list
        column_data.append(formatted_column)
        # Update the start index for the next column
        start_index = end_index
    
    # Create the DataFrame from the column data
    df = pd.DataFrame(column_data).T
    
    return df

# Example usage:
colors = ['Red', 'Green', 'Blue']
states = ['California', 'Texas', 'New York', 'Florida']
df = task_func(colors, states)
print(df)
import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    """Test cases for task_func."""
    def test_empty_lists(self):
        """Test with empty color and state lists."""
        self.assertEqual(task_func([], []).empty, True)
    def test_single_color_and_state(self):
        """Test with one color and one state."""
        random.seed(0)
        result = task_func(["Red"], ["Solid"])
        expected = pd.DataFrame({"Color:State 1": ["Red:Solid"]})
        pd.testing.assert_frame_equal(result, expected)
    def test_multiple_colors_single_state(self):
        """Test with multiple colors and a single state."""
        random.seed(1)
        result = task_func(["Red", "Blue", "Green"], ["Solid"])
        expected_combinations = set(["Red:Solid", "Blue:Solid", "Green:Solid"])
        result_combinations = set(result["Color:State 1"])
        self.assertEqual(result_combinations, expected_combinations)
    def test_single_color_multiple_states(self):
        """Test with a single color and multiple states."""
        random.seed(2)
        result = task_func(["Red"], ["Solid", "Liquid", "Gas"])
        expected_combinations = set(["Red:Solid", "Red:Liquid", "Red:Gas"])
        result_combinations = set(result["Color:State 1"])
        self.assertEqual(result_combinations, expected_combinations)
    def test_multiple_colors_and_states(self):
        """Test with multiple colors and states."""
        random.seed(3)
        colors = ["Red", "Blue"]
        states = ["Solid", "Liquid"]
        result = task_func(colors, states)
        expected_combinations = set(
            [f"{color}:{state}" for color in colors for state in states]
        )
        result_combinations = set(result.values.flatten())
        self.assertEqual(result_combinations, expected_combinations)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)