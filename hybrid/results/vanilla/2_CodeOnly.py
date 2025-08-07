import random
import statistics

def task_func(LETTERS):
    # Create a dictionary with random letters as keys and lists of random integers as values
    random_dict = {letter: [random.randint(1, 100) for _ in range(random.randint(3, 10))] for letter in LETTERS}
    
    # Sort the dictionary by the mean of the values in descending order
    sorted_dict = dict(sorted(random_dict.items(), key=lambda item: statistics.mean(item[1]), reverse=True))
    
    return sorted_dict

# Example usage
LETTERS = ['A', 'B', 'C', 'D', 'E']
sorted_dictionary = task_func(LETTERS)
print(sorted_dictionary)