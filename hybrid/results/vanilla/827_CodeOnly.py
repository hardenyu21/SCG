import math
from sympy import isprime

def task_func(input_list):
    # Filter the prime numbers from the input list
    prime_numbers = [num for num in input_list if isprime(num)]
    
    # Sort the prime numbers based on their radian value converted to degrees
    sorted_primes = sorted(prime_numbers, key=lambda x: math.degrees(x))
    
    return sorted_primes

# Example usage
print(task_func([101, 102, 103, 104]))  # Output: [101, 103]