import random
import matplotlib.pyplot as plt

# Sample data
class Object:
    value = 0
    def __init__(self, value=None):
        if value is None:
            self.value = random.gauss(0, 1)
        else:
            self.value = value

def task_func(obj_list, attr, num_bins=30, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Extract the attribute values from the list of objects
    attr_values = [getattr(obj, attr) for obj in obj_list]
    
    # Create the histogram plot
    fig, ax = plt.subplots()
    ax.hist(attr_values, bins=num_bins, edgecolor='black')
    
    # Set the title and labels
    ax.set_title('Histogram of attribute values')
    ax.set_xlabel('Attribute Value')
    ax.set_ylabel('Count')
    
    # Return the Axes object
    return ax

# Example usage
if __name__ == "__main__":
    # Create a list of Object instances
    obj_list = [Object() for _ in range(100)]
    
    # Generate the histogram plot
    ax = task_func(obj_list, 'value')
    
    # Display the plot
    plt.show()