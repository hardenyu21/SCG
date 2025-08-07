import numpy as np
import matplotlib.pyplot as plt

# Constants
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']

def task_func(city_dict, max_range=1000000, seed=0):
    # Seed the random number generator
    np.random.seed(seed)
    
    # Initialize the dictionary for city populations
    city_populations = {}
    
    # Generate random populations for cities in the CITIES list
    for city in CITIES:
        if city in city_dict.values():
            city_populations[city] = np.random.randint(1, max_range + 1)
        else:
            city_populations[city] = -1
    
    # Plot the population data
    fig, ax = plt.subplots()
    ax.bar(city_populations.keys(), city_populations.values(), color='skyblue')
    ax.set_xlabel('City')
    ax.set_ylabel('Population')
    ax.set_title('City Populations')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Return the dictionary and the Axes object
    return city_populations, ax

# Example usage:
# city_dict = {'Alice': 'New York', 'Bob': 'Tokyo', 'Charlie': 'Paris'}
# populations, ax = task_func(city_dict)
# plt.show()
import unittest
from matplotlib.axes import Axes
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        """Test if the population dictionary has correct structure and values."""
        city_dict = {'John': 'New York', 'Alice': 'London', 'Bob': 'Beijing', 'Charlie': 'Tokyo', 'David': 'Mumbai'}
        population_dict, _ = task_func(city_dict, 250000, 56)
        self.assertSetEqual(set(population_dict.keys()), {'New York', 'London', 'Beijing', 'Tokyo', 'Mumbai'})
        for population in population_dict.values():
            self.assertTrue(-1 <= population <= 250000)
    def test_case_2(self):
        """Test if the bar chart plot has the correct attributes."""
        city_dict = {'Summer': 'New York', 'Alice': 'London', 'April': 'Beijing', 'Charlie': 'Tokyo', 'David': 'Sydney'}
        population_dict, ax = task_func(city_dict, seed=54)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), 'City Populations')
        self.assertEqual(ax.get_xlabel(), 'City')
        self.assertEqual(ax.get_ylabel(), 'Population')
        self.assertEqual(population_dict, {'New York': 72816, 'London': 367942, 'Beijing': 869251, 'Tokyo': 323344, 'Sydney': 267288})
        bars = [rect for rect in ax.get_children() if isinstance(rect, plt.Rectangle) and rect.get_width() > 0]
        bars = [bar for bar in bars if bar.get_xy()[0] != 0]  # Exclude the non-data bar
        self.assertEqual(len(bars), 5)
    def test_case_3(self):
        """Test the function with an empty input dictionary."""
        city_dict = {}
        population_dict, _ = task_func(city_dict)
        self.assertSetEqual(set(population_dict.keys()), set({}))
        self.assertTrue(all(1000000 <= pop <= 10000000 for pop in population_dict.values()))
    def test_case_4(self):
        """Test the function with a differently structured input dictionary."""
        city_dict = {'Person1': 'City1', 'Person2': 'City2'}
        population_dict, _ = task_func(city_dict)
        self.assertEqual(population_dict, {'City1': -1, 'City2': -1})
    def test_case_5(self):
        """Test if the population values are random with the same input and different seeds."""
        city_dict = {'John': 'New York', 'Alice': 'London'}
        population_dict1, _ = task_func(city_dict, seed=77)
        population_dict2, _ = task_func(city_dict, seed=42)
        self.assertNotEqual(population_dict1, population_dict2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)