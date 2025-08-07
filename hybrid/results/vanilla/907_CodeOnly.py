import os
import re

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    try:
        # Compile the regex pattern for matching
        regex = re.compile(pattern)
        
        # Iterate over all files in the specified directory
        for filename in os.listdir(directory):
            # Check if the current file matches the pattern
            if regex.search(filename):
                # Create the new filename by replacing the pattern with the replacement string
                new_filename = regex.sub(replacement, filename)
                
                # Construct full file paths
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                
                # Rename the file
                os.rename(old_file_path, new_file_path)
        
        # Return True if all operations were successful
        return True
    except Exception as e:
        # Return False if any exception occurred
        print(f"An error occurred: {e}")
        return False