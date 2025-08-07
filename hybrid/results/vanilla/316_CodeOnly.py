import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    # Generate a random number of items within the specified range
    num_items = random.randint(value_range[0], value_range[1])
    
    # Randomly assign categories to each item
    category_assignments = [random.choice(CATEGORIES) for _ in range(num_items)]
    
    # Count the occurrences of each category
    category_counts = {category: category_assignments.count(category) for category in CATEGORIES}
    
    # Create a DataFrame from the category counts
    df = pd.DataFrame(list(category_counts.items()), columns=['Category', 'Count'])
    
    return df

# Example usage
df = task_func((50, 100))
print(df)