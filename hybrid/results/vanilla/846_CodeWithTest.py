import collections
import pandas as pd

def task_func(obj_list, attr):
    # Extract the specified attribute from each object in the list
    attribute_values = [getattr(obj, attr, None) for obj in obj_list]
    
    # Count the frequency of each attribute value using collections.Counter
    frequency_count = collections.Counter(attribute_values)
    
    # Convert the frequency count to a DataFrame
    df = pd.DataFrame(frequency_count.items(), columns=['attribute', 'count'])
    
    return df

# Example usage
class ExampleObject:
    def __init__(self, animal, shape):
        self.animal = animal
        self.shape = shape

obj_list = [
    ExampleObject('tiger', 'Square'),
    ExampleObject('leopard', 'Circle'),
    ExampleObject('cat', 'Rectangle'),
    ExampleObject('elephant', 'Rectangle')
]

count = task_func(obj_list, 'shape')
print(count)
import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    class ExampleObject:
        def __init__(self, color, shape):
            self.color = color
            self.shape = shape
    def test_case_1(self):
        obj_list = [
            self.ExampleObject('Red', 'Square'),
            self.ExampleObject('Green', 'Circle'),
            self.ExampleObject('Red', 'Rectangle')
        ]
        result = task_func(obj_list, 'color')
        expected = pd.DataFrame({
            'attribute': ['Red', 'Green'],
            'count': [2, 1]
        })
        pd.testing.assert_frame_equal(result.sort_index(), expected)
    def test_case_2(self):
        obj_list = [
            self.ExampleObject('Red', 'Square'),
            self.ExampleObject('Green', 'Circle'),
            self.ExampleObject('Red', 'Square')
        ]
        result = task_func(obj_list, 'shape')
        expected = pd.DataFrame({
            'attribute': ['Square', 'Circle'],
            'count': [2, 1]
        })
        pd.testing.assert_frame_equal(result.sort_index(), expected)
    def test_case_3(self):
        obj_list = []
        result = task_func(obj_list, 'color')
        self.assertTrue(result.empty)
    def test_case_4(self):
        obj_list = [
            self.ExampleObject('Red', 'Square'),
            self.ExampleObject('Red', 'Square'),
            self.ExampleObject('Red', 'Square')
        ]
        result = task_func(obj_list, 'color')
        expected = pd.DataFrame({
            'attribute': ['Red'],
            'count': [3]
        })
        pd.testing.assert_frame_equal(result.sort_index(), expected)
    def test_case_5(self):
        obj_list = [
            self.ExampleObject('Red', 'Square'),
            self.ExampleObject('Green', 'Circle'),
            self.ExampleObject('Blue', 'Triangle')
        ]
        result = task_func(obj_list, 'shape')
        expected = pd.DataFrame({
            'attribute': ['Square', 'Circle', 'Triangle'],
            'count': [1, 1, 1]
        })
        pd.testing.assert_frame_equal(result.sort_index(), expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)