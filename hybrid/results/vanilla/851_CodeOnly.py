import textwrap
import re

def task_func(input_string, width):
    # Split the input string into separate lines
    lines = input_string.splitlines()
    
    # Wrap each line to the specified width
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    
    # Join the wrapped lines back into a single string with newline characters
    wrapped_string = '\n'.join(wrapped_lines)
    
    return wrapped_string