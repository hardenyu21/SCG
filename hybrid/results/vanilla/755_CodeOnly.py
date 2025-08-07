import os
import glob

def task_func(directory_path):
    # Get all files in the directory
    files = glob.glob(os.path.join(directory_path, '*'))
    
    new_filenames = []
    
    for file_path in files:
        # Extract the filename from the file path
        filename = os.path.basename(file_path)
        
        # Split the filename into words using period as the separator
        words = filename.split('.')
        
        # Reverse the order of words
        reversed_words = words[::-1]
        
        # Join the reversed words back into a filename
        new_filename = '.'.join(reversed_words)
        
        # Construct the new file path
        new_file_path = os.path.join(directory_path, new_filename)
        
        # Rename the file
        os.rename(file_path, new_file_path)
        
        # Add the new filename to the list
        new_filenames.append(new_filename)
    
    return new_filenames