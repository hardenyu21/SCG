import ast
import re

def task_func(text_file: str) -> list:
    # Read the content of the file
    with open(text_file, 'r') as file:
        content = file.read()
    
    # Regular expression to find string representations of dictionaries
    dict_pattern = re.compile(r'\{.*?\}')
    
    # Find all matches in the content
    matches = dict_pattern.findall(content)
    
    # Convert string representations to actual dictionaries
    dictionaries = [ast.literal_eval(match) for match in matches]
    
    return dictionaries

# Example usage
# Assuming 'another_sample.txt' contains string representations of dictionaries
# print(task_func("another_sample.txt"))