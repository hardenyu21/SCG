import os
import glob

def task_func(directory_path, file_extension='.csv'):
    # Initialize an empty dictionary to store the data
    data = {}
    
    # Construct the search pattern for files with the specified extension
    search_pattern = os.path.join(directory_path, f'*{file_extension}')
    
    # Use glob to find all files matching the pattern
    for file_path in glob.glob(search_pattern):
        # Extract the filename without the extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Initialize a list to store the rows of the file
        rows = []
        
        # Open the file and read its contents
        with open(file_path, 'r', newline='') as file:
            # Use csv.reader to read the file, assuming comma as the delimiter
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        
        # Add the file's data to the dictionary
        data[file_name] = rows
    
    return data