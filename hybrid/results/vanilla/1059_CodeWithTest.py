import numpy as np
import random
import itertools
import pandas as pd

# Constants
PLANETS = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]
ELEMENTS = [
    "Hydrogen",
    "Helium",
    "Oxygen",
    "Carbon",
    "Nitrogen",
    "Magnesium",
    "Silicon",
    "Iron",
    "Nickel",
]

def task_func():
    # Create a list of all possible planet-element pairs
    planet_element_pairs = list(itertools.product(PLANETS, ELEMENTS))
    
    # Shuffle the list to ensure randomness
    random.shuffle(planet_element_pairs)
    
    # Create a DataFrame with the number of rows equal to the number of planets
    # and the number of columns equal to the number of elements
    df = pd.DataFrame(index=PLANETS, columns=ELEMENTS)
    
    # Fill the DataFrame with the shuffled planet-element pairs
    for i, (planet, element) in enumerate(planet_element_pairs):
        row_idx = PLANETS.index(planet)
        col_idx = ELEMENTS.index(element)
        df.iloc[row_idx, col_idx] = f"{planet}:{element}"
    
    return df

# Example usage
df = task_func()
print(df)
import unittest
import itertools
import pandas as pd
import random
class TestCases(unittest.TestCase):
    """Tests for `task_func`."""
    def test_basic_structure(self):
        """Test the basic structure of the table."""
        random.seed(0)
        table = task_func()
        # Verify the structure of the table
        self.assertEqual(len(table), len(PLANETS))
        self.assertEqual(list(table.columns), ELEMENTS)
    def test_pair_existence(self):
        """Test the existence of planet-element pairs."""
        random.seed(1)
        table = task_func()
        # Verify all planet-element pairs are present
        all_pairs = set(f"{p}:{e}" for p, e in itertools.product(PLANETS, ELEMENTS))
        generated_pairs = set(table.values.flatten())
        self.assertEqual(all_pairs, generated_pairs)
        # Verify no extra pairs are present
        self.assertEqual(len(all_pairs), len(generated_pairs))
    def test_data_type(self):
        """Test the data type of the table and its elements."""
        random.seed(2)
        table = task_func()
        # Check the data type of the table and its elements
        self.assertIsInstance(table, pd.DataFrame)
        self.assertTrue(all(isinstance(cell, str) for cell in table.values.flatten()))
    def test_data_format(self):
        """Test the format of the elements in the table."""
        random.seed(3)
        table = task_func()
        # Check the format of the elements in the table
        self.assertTrue(
            all(
                ":" in cell and len(cell.split(":")) == 2
                for cell in table.values.flatten()
            )
        )
    def test_uniqueness(self):
        """Test the uniqueness of the pairs."""
        random.seed(4)
        table = task_func()
        # Check uniqueness of the pairs
        generated_pairs = table.values.flatten()
        self.assertEqual(len(generated_pairs), len(set(generated_pairs)))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)