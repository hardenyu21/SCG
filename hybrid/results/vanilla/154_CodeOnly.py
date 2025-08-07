import re
import os
import glob
import mimetypes

def task_func(directory, file_pattern, suffix):
    # Initialize an empty dictionary to store file names and their MIME types
    file_mime_dict = {}
    
    # Construct the search pattern using the provided file pattern and suffix
    search_pattern = os.path.join(directory, f"*{file_pattern}*{suffix}")
    
    # Use glob to find all files matching the pattern
    matching_files = glob.glob(search_pattern)
    
    # Iterate over each matching file
    for file_path in matching_files:
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)
        
        # Determine the MIME type of the file
        mime_type, _ = mimetypes.guess_type(file_path)
        
        # If the MIME type is not None, add it to the dictionary
        if mime_type:
            file_mime_dict[file_name] = mime_type
    
    # Return the dictionary mapping file names to their MIME types
    return file_mime_dict