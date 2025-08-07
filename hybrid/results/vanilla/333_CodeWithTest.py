import heapq
import random

def task_func(k, list_length=5, min_value=0, max_value=100):
    # Generate a random list of integers
    random_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    
    # Find the k smallest numbers using heapq
    k_smallest = heapq.nsmallest(k, random_list)
    
    # Return the tuple containing the random list and the k smallest numbers
    return (random_list, k_smallest)

# Example usage:
# result = task_func(3, 10, 0, 50)
# print(result)
import unittest
import random
class TestCases(unittest.TestCase):
    
    def test_empty_list(self):
        random.seed(0)
        rand_list, least_k = task_func(0, 0)
        self.assertEqual(rand_list, [])
        self.assertEqual(least_k, [])
    def test_k_larger_than_list_length(self):
        random.seed(0)
        rand_list, least_k = task_func(5, 10)
        self.assertEqual(len(rand_list), 10)
        self.assertEqual(len(least_k), 5)
    def test_sorted_list(self):
        random.seed(0)
        rand_list, least_k = task_func(100, 3)
        self.assertEqual(least_k, sorted(rand_list)[:3])
    def test_least_k_sorted(self):
        random.seed(0)
        rand_list, least_k = task_func(100, 5, 100, 100)
        self.assertEqual(least_k, sorted(least_k)[:5])
    
    def test_least_k_sorted_first(self):
        random.seed(0)
        rand_list, least_k = task_func(100, 5)
        self.assertEqual(least_k[0], sorted(least_k)[0])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)