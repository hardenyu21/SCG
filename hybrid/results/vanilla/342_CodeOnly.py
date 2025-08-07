import string
import random
import re

def task_func(elements, pattern, seed=100):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # List to store formatted elements
    formatted_elements = []
    
    # Iterate over each element in the elements list
    for element in elements:
        # Replace each character in the element with a random character
        replaced_element = ''.join(random.choice(string.ascii_letters) for _ in element)
        
        # Format the replaced element into the pattern "%{0}%"
        formatted_element = f"%{replaced_element}%"
        
        # Append the formatted element to the list
        formatted_elements.append(formatted_element)
    
    # Concatenate all formatted elements into a single string
    concatenated_string = ''.join(formatted_elements)
    
    # Search for the regex pattern in the concatenated string
    search_result = re.search(pattern, concatenated_string) is not None
    
    # Return the list of formatted elements and the search result
    return formatted_elements, search_result