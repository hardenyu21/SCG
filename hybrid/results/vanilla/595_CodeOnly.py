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