import re
import string

def task_func(text1, text2):
    # Define a regular expression pattern to match all ASCII punctuation
    pattern = f"[{re.escape(string.punctuation)}]"
    
    # Remove punctuation from both text1 and text2 using re.sub
    cleaned_text1 = re.sub(pattern, '', text1)
    cleaned_text2 = re.sub(pattern, '', text2)
    
    # Return the cleaned texts as a tuple
    return (cleaned_text1, cleaned_text2)

# Example usage
cleaned_text1, cleaned_text2 = task_func("test (with parenthesis []!!)", "And, other; stuff ^_`")
print(cleaned_text1, cleaned_text2)  # Output: test with parenthesis  And other stuff