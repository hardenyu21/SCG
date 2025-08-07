import os
import random
import string

def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(n_files):
        # Generate a random filename
        filename = f"file_{i+1}.txt"
        file_path = os.path.join(directory, filename)
        
        # Generate a random string
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
        
        # Write the random string to the file and reset the cursor
        with open(file_path, 'w+') as file:
            file.write(random_string)
            file.seek(0)
    
    return directory

# Example usage:
# directory_path = task_func('/path/to/directory', 5)
# print(f"Files generated in directory: {directory_path}")