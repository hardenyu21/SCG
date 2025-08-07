from collections import Counter
import itertools

def task_func(list_of_menuitems):
    # Flatten the nested list using itertools.chain
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))
    
    # Count the occurrences of each menu item
    item_counts = Counter(flattened_list)
    
    # Find the most common menu item
    most_common_item, _ = item_counts.most_common(1)[0]
    
    return most_common_item
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Description: Testing with a list where 'Pizza' appears more frequently than other items.
        input_data = [['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']]
        output = task_func(input_data)
        self.assertEqual(output, 'Pizza')
    
    def test_case_2(self):
        # Description: Testing with a list where 'Burger' appears more frequently than other items.
        input_data = [['Burger', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']]
        output = task_func(input_data)
        self.assertEqual(output, 'Burger')
    
    def test_case_3(self):
        # Description: Testing with a list where 'Pasta' appears more frequently than other items.
        input_data = [['Pasta', 'Pasta'], ['Pasta', 'Coke'], ['Pizza', 'Coke']]
        output = task_func(input_data)
        self.assertEqual(output, 'Pasta')
    
    def test_case_4(self):
        # Description: Testing with a list where 'Sushi' appears more frequently than other items.
        input_data = [['Sushi'], ['Sushi', 'Coke'], ['Pizza', 'Coke']]
        output = task_func(input_data)
        self.assertEqual(output, 'Sushi')
    
    def test_case_5(self):
        # Description: Testing with a list where 'Salad' appears more frequently than other items.
        input_data = [['Salad'], ['Salad', 'Coke'], ['Pizza', 'Coke'], ['Salad', 'Burger']]
        output = task_func(input_data)
        self.assertEqual(output, 'Salad')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)