import heapq
import random

def task_func(obj_list, attr, top_n=5, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Extract the specified attribute values from the list of objects
    attr_values = [getattr(obj, attr, None) for obj in obj_list]
    
    # Filter out None values in case the attribute does not exist
    attr_values = [value for value in attr_values if value is not None]
    
    if not attr_values:
        return [], None
    
    # Find the top N values using a heap
    top_values = heapq.nlargest(top_n, attr_values)
    
    # Randomly sample a value from all attributes
    random_value = random.choice(attr_values)
    
    return top_values, random_value

# Example usage
class Object:
    def __init__(self, value):
        self.test = value

random.seed(2)
obj_list = [Object(random.randint(1, 12)) for _ in range(13)]
top_values, random_value = task_func(obj_list, 'test', 2, 12)
print(top_values)  # Output: [12, 11]
print(random_value)  # Output: 5
import unittest
from faker import Faker
# Test cases with random data
class TestCases(unittest.TestCase):
    faker = Faker()
    faker.seed_instance(42)
    
    def generate_objects(self, count):
        class TestObject:
            def __init__(self, value):
                self.value = value
        
        return [TestObject(self.faker.random_int(min=1, max=100)) for _ in range(count)]
    
    def test_case_1(self):
        obj_list = self.generate_objects(10)
        result, rand = task_func(obj_list, 'value', 5, seed=12)
        self.assertEqual(result, [95, 95, 82, 36, 32])
        self.assertEqual(rand, 18)
    def test_case_2(self):
        obj_list = self.generate_objects(50)
        result, rand = task_func(obj_list, 'value', 7, seed=1)
        self.assertEqual(result, [98, 98, 95, 94, 92, 90, 90])
        self.assertEqual(rand, 12)
        
    def test_case_3(self):
        obj_list = []
        result, rand = task_func(obj_list, 'value', 5, seed=2)
        self.assertEqual(result, [])
        self.assertEqual(rand, None)
        
    def test_case_4(self):
        obj_list = self.generate_objects(5)
        result, rand = task_func(obj_list, 'value', 10, seed=3)
        self.assertEqual(result, [81, 80, 71, 38, 11])
        self.assertEqual(rand, 71)
        
    def test_case_5(self):
        obj_list = self.generate_objects(100)
        result, rand = task_func(obj_list, 'value', 3, seed=4)
        self.assertEqual(result, [100, 99, 99])
        self.assertEqual(rand, 22)
    def test_case_rng(self):
        obj_list = self.generate_objects(100)
        result, rand = task_func(obj_list, 'value', 3, seed=123)
        result2, rand2 = task_func(obj_list, 'value', 3, seed=43)
        self.assertEqual(result, result2)
        self.assertNotEqual(rand, rand2)
        result, rand3 = task_func(obj_list, 'value', 3, seed=123)
        self.assertEqual(rand, rand3)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)