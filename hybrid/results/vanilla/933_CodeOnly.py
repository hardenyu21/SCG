import string
import wordninja

def task_func(word):
    # Split the word into a list of words using wordninja
    words = wordninja.split(word)
    
    # Initialize an empty list to store the tuples
    result = []
    
    # Iterate over each word in the list
    for w in words:
        # Iterate over each character in the word
        for index, char in enumerate(w):
            # Convert the character to lowercase
            lower_char = char.lower()
            # Find the position of the character in the alphabet
            if lower_char in string.ascii_lowercase:
                position = string.ascii_lowercase.index(lower_char) + 1
                # Append the tuple (character, position) to the result list
                result.append((lower_char, position))
    
    return result

# Example usage:
# print(task_func("helloworld"))