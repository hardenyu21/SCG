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