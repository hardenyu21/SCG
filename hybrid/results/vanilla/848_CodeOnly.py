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