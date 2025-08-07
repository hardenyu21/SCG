from collections import Counter
import heapq
import random

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def task_func(my_dict):
    # Count the occurrences of each letter in the dictionary
    letter_counts = Counter(my_dict.keys())
    
    # Find the 3 most common letters using a heap
    most_common_letters = heapq.nlargest(3, letter_counts, key=letter_counts.get)
    
    return most_common_letters

# Example usage
if __name__ == "__main__":
    # Create a dictionary with random integers as values
    my_dict = {letter: random.randint(1, 100) for letter in LETTERS}
    
    # Get the 3 most common letters
    result = task_func(my_dict)
    print("The 3 most common letters are:", result)