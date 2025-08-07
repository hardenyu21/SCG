from collections import Counter
from itertools import chain

def task_func(list_of_lists):
    # Merge all sublists into a single list using chain.from_iterable
    merged_list = list(chain.from_iterable(list_of_lists))
    # Create a Counter object to count the elements in the merged list
    element_count = Counter(merged_list)
    return element_count
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(task_func(list_of_lists), Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}))
    def test_case_2(self):
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2]]
        self.assertEqual(task_func(list_of_lists), Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}))
    def test_case_3(self):
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertEqual(task_func(list_of_lists), Counter({1: 3, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}))
    def test_case_4(self):
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3]]
        self.assertEqual(task_func(list_of_lists), Counter({1: 4, 2: 4, 3: 3, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}))
    def test_case_5(self):
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertEqual(task_func(list_of_lists), Counter({1: 5, 2: 5, 3: 4, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3}))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)