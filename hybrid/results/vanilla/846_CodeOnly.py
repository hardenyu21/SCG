import collections
import pandas as pd

def task_func(obj_list, attr):
    # Extract the specified attribute from each object in the list
    attribute_values = [getattr(obj, attr, None) for obj in obj_list]
    
    # Count the frequency of each attribute value using collections.Counter
    frequency_count = collections.Counter(attribute_values)
    
    # Convert the frequency count to a DataFrame
    df = pd.DataFrame(frequency_count.items(), columns=['attribute', 'count'])
    
    return df

# Example usage
class ExampleObject:
    def __init__(self, animal, shape):
        self.animal = animal
        self.shape = shape

obj_list = [
    ExampleObject('tiger', 'Square'),
    ExampleObject('leopard', 'Circle'),
    ExampleObject('cat', 'Rectangle'),
    ExampleObject('elephant', 'Rectangle')
]

count = task_func(obj_list, 'shape')
print(count)