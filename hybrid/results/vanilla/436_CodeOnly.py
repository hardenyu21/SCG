import string
import matplotlib.pyplot as plt

def task_func(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    
    # Convert the string to lowercase to ensure case-insensitivity
    s = s.lower()
    
    # Initialize a dictionary to store the frequency of each letter
    frequency = {letter: 0 for letter in string.ascii_lowercase}
    
    # Calculate the frequency of each letter
    for char in s:
        if char in frequency:
            frequency[char] += 1
    
    # Filter out letters that do not appear in the string
    frequency = {letter: count for letter, count in frequency.items() if count > 0}
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(frequency.keys(), frequency.values())
    ax.set_title('Letter Frequencies')
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    
    # Return the frequency dictionary and the Axes object
    return frequency, ax

# Example usage:
# freq, ax = task_func("Hello World!")
# plt.show()