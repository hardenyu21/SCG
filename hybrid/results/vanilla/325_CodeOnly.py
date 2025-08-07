import re
import os
from pathlib import Path
import glob

def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    # Compile the regular expression pattern
    pattern = re.compile(regex_pattern)
    
    # Initialize a dictionary to store results
    results = {}
    
    # Use glob to find all text files in the specified directory
    text_files = glob.glob(os.path.join(directory_path, '*.txt'))
    
    # Iterate over each text file
    for file_path in text_files:
        # Extract the file name without the path
        file_name = Path(file_path).name
        
        # Initialize a list to store matches for the current file
        matches = []
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the file content
            content = file.read()
            
            # Find all matches using the compiled pattern
            found_matches = pattern.findall(content)
            
            # Process the matches to ensure they are in the desired format
            for match in found_matches:
                if isinstance(match, tuple):
                    # If the match is a tuple, it means it was captured by a group
                    matches.append(match[0])
                else:
                    # Otherwise, it's a single character match
                    matches.append(match)
        
        # Add the matches to the results dictionary
        results[file_name] = matches
    
    return results