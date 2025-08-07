import random
import bisect
from array import array

def task_func(n=10, total=100):
    while True:
        # Generate 'n' random integers
        numbers = [random.randint(1, total - n + 1) for _ in range(n)]
        
        # Adjust the numbers to ensure their sum is 'total'
        current_sum = sum(numbers)
        if current_sum == total:
            break
        elif current_sum < total:
            # Increase some numbers to reach the total
            for _ in range(total - current_sum):
                numbers[random.randint(0, n - 1)] += 1
        else:
            # Decrease some numbers to reach the total
            for _ in range(current_sum - total):
                numbers[random.randint(0, n - 1)] -= 1
        
        # Ensure all numbers are positive
        for i in range(n):
            if numbers[i] <= 0:
                numbers[i] = 1
                total -= 1  # Adjust total to account for the change

    # Sort the numbers
    numbers.sort()

    # Generate a new random number
    new_number = random.randint(1, total)

    # Determine the insertion position for the new number
    insertion_position = bisect.bisect_left(numbers, new_number)

    # Convert the list to an array
    numbers_array = array('i', numbers)

    return (numbers_array, insertion_position)

# Example usage
result = task_func()
print("Sorted numbers:", result[0])
print("Insertion position for new number:", result[1])
import unittest
from array import array
class TestCases(unittest.TestCase):
    def test_return_type(self):
        nums, pos = task_func(5, 50)
        self.assertIsInstance(nums, array)
        self.assertIsInstance(pos, int)
    def test_correct_length(self):
        nums, _ = task_func(5, 50)
        self.assertEqual(len(nums), 5)
    def test_sum_of_numbers(self):
        nums, _ = task_func(5, 50)
        self.assertEqual(sum(nums), 50)
    def test_sorted_order(self):
        nums, _ = task_func(5, 50)
        self.assertEqual(list(nums), sorted(nums))
    def test_insertion_position(self):
        nums, pos = task_func(5, 50)
        new_num = random.randint(0, 50)
        nums.insert(pos, new_num)
        self.assertEqual(nums[pos], new_num)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)