import random
import string
from matplotlib import pyplot as plt

def task_func(elements, seed=100):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Function to generate a random alphanumeric string of length 5
    def generate_random_string():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    
    # Format each element in the list with the random pattern
    formatted_elements = [f"% {generate_random_string()}%" for _ in elements]
    
    # Count the occurrence of each character in all formatted strings
    char_count = {}
    for element in formatted_elements:
        for char in element:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    # Prepare data for the histogram
    characters = list(char_count.keys())
    counts = list(char_count.values())
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(characters, counts)
    ax.set_xlabel('Character')
    ax.set_ylabel('Count')
    ax.set_title('Character Occurrence in Formatted Strings')
    plt.xticks(rotation=90)
    plt.tight_layout()
    
    # Return the formatted elements, the plot axes, and the character count dictionary
    return formatted_elements, ax, char_count

# Example usage:
# elements = ["apple", "banana", "cherry"]
# formatted_elements, ax, char_count = task_func(elements)
# plt.show()
# print(formatted_elements)
# print(char_count)