import random
import pandas as pd
import collections

# Constants
VEGETABLES = ['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']

def task_func(vegetable_dict, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Reverse the dictionary to map vegetables to people
    reversed_dict = collections.defaultdict(list)
    for person, vegetable in vegetable_dict.items():
        reversed_dict[vegetable].append(person)
    
    # Assign random counts to each vegetable
    vegetable_counts = {vegetable: random.randint(1, 10) for vegetable in reversed_dict.keys()}
    
    # Calculate the total counts
    total_counts = sum(vegetable_counts.values())
    
    # Calculate the percentage occurrence of each vegetable
    vegetable_percentages = {vegetable: (count / total_counts) * 100 for vegetable, count in vegetable_counts.items()}
    
    # Create a dictionary to map each vegetable to a person
    vegetable_to_person = {vegetable: reversed_dict[vegetable][0] for vegetable in reversed_dict.keys()}
    
    # Create a DataFrame with the results
    data = {
        'Vegetable': list(vegetable_counts.keys()),
        'Random Count': list(vegetable_counts.values()),
        'Percentage Occurrence': list(vegetable_percentages.values())
    }
    df = pd.DataFrame(data)
    
    return df

# Example usage
vegetable_dict = {
    'Alice': 'Carrot',
    'Bob': 'Potato',
    'Charlie': 'Tomato',
    'David': 'Cabbage',
    'Eve': 'Spinach',
    'Frank': 'Carrot',
    'Grace': 'Potato'
}

df = task_func(vegetable_dict)
print(df)