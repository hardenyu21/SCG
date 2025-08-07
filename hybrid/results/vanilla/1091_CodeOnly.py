import ast
import os
import glob

# Constants
DIRECTORY = 'data'

def task_func(directory):
    # List to store the dictionaries extracted from the text files
    dictionaries = []
    
    # Get all text files in the specified directory
    text_files = glob.glob(os.path.join(directory, '*.txt'))
    
    for file_path in text_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            
            try:
                # Attempt to parse the content as a dictionary
                parsed_dict = ast.literal_eval(content)
                
                # Check if the parsed content is indeed a dictionary
                if isinstance(parsed_dict, dict):
                    dictionaries.append(parsed_dict)
                else:
                    raise ValueError(f"Invalid dictionary representation in file: {file_path}")
            
            except (ValueError, SyntaxError) as e:
                # Raise an exception if the content is not a valid dictionary
                raise ValueError(f"Invalid dictionary representation in file: {file_path}") from e
    
    return dictionaries

# Example usage:
# dictionaries = task_func(DIRECTORY)
# print(dictionaries)