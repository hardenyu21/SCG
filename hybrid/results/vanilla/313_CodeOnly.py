import re
import os
import shutil

def task_func(directory):
    # Dictionary to store the mapping of subdirectories to files
    subdirectory_files = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            # Use regex to find the first text not enclosed in square brackets
            match = re.search(r'\[(.*?)\]', filename)
            if match:
                # Extract the text inside the brackets
                subdirectory_name = match.group(1)
                
                # Create the full path for the subdirectory
                subdirectory_path = os.path.join(directory, subdirectory_name)
                
                # Create the subdirectory if it doesn't exist
                if not os.path.exists(subdirectory_path):
                    os.makedirs(subdirectory_path)
                
                # Move the file to the subdirectory
                shutil.move(file_path, os.path.join(subdirectory_path, filename))
                
                # Update the dictionary
                if subdirectory_name not in subdirectory_files:
                    subdirectory_files[subdirectory_name] = []
                subdirectory_files[subdirectory_name].append(filename)

    # Return the directory path and the dictionary of subdirectories and files
    return directory, subdirectory_files