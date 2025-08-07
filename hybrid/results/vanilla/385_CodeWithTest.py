import matplotlib.pyplot as plt
from collections import Counter

FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']

def task_func(fruit_dict):
    # Initialize a Counter to keep track of fruit frequencies
    fruit_counter = Counter()
    
    # Iterate over the dictionary to count each fruit occurrence
    for person, fruit in fruit_dict.items():
        if fruit in FRUITS:
            fruit_counter[fruit] += 1
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(fruit_counter.keys(), fruit_counter.values(), color='skyblue')
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Frequency')
    ax.set_title('Fruit Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the dictionary and the axes object
    return dict(fruit_counter), ax

# Example usage:
# fruit_dict = {
#     'Alice': 'Apple',
#     'Bob': 'Banana',
#     'Charlie': 'Apple',
#     'David': 'Cherry',
#     'Eve': 'Banana',
#     'Frank': 'Grape',
#     'Grace': 'Apple'
# }
# fruit_counts, ax = task_func(fruit_dict)
# plt.show()
import unittest
import matplotlib.axes
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        fruit_dict = {'John': 'Apple', 'Alice': 'Banana', 'Bob': 'Cherry'}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {'Apple': 1, 'Banana': 1, 'Cherry': 1})
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_2(self):
        fruit_dict = {'John': 'Apple', 'Alice': 'Banana', 'Bob': 'Apple'}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {'Apple': 2, 'Banana': 1})
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_3(self):
        fruit_dict = {}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {})
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_4(self):
        fruit_dict = {'John': 'Apple'}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {'Apple': 1})
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_5(self):
        fruit_dict = {'John': 123, 'Alice': None, 'Bob': 'Apple'}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {'Apple': 1})
        self.assertIsInstance(ax, matplotlib.axes.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)