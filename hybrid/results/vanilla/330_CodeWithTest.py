import heapq
import random

def task_func(list_length: int = 5, k: int = 3):
    # Generate a random list of integers with the specified length
    random_list = [random.randint(1, 100) for _ in range(list_length)]
    
    # Find the k largest numbers using heapq
    k_largest_numbers = heapq.nlargest(k, random_list)
    
    # Return the tuple containing the random list and the k largest numbers
    return (random_list, k_largest_numbers)

# Example usage:
# result = task_func(10, 3)
# print(result)
import unittest
class TestCases(unittest.TestCase):
    def test_empty_list(self):
        random.seed(0)
        rand_list, top_k = task_func(0, 3)
        self.assertEqual(rand_list, [])
        self.assertEqual(top_k, [])
    def test_k_larger_than_list_length(self):
        random.seed(0)
        rand_list, top_k = task_func(5, 10)
        self.assertEqual(len(rand_list), 5)
        self.assertEqual(len(top_k), 5)
    def test_sorted_list(self):
        random.seed(0)
        rand_list, top_k = task_func(100, 3)
        self.assertEqual(top_k, sorted(rand_list, reverse=True)[:3])
    def test_top_k_sorted(self):
        random.seed(0)
        rand_list, top_k = task_func(100, 5)
        self.assertEqual(top_k, sorted(top_k, reverse=True)[:5])
    
    def test_top_k_sorted_first(self):
        random.seed(0)
        rand_list, top_k = task_func(100, 5)
        self.assertEqual(top_k[0], sorted(top_k, reverse=True)[0])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)