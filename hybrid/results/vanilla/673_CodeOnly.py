import os
import random

def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(1, n_files + 1):
        file_name = f'file_{i}.txt'
        file_path = os.path.join(directory, file_name)
        
        # Generate a single digit random integer
        random_digit = random.randint(0, 9)
        
        # Write the random digit to the file
        with open(file_path, 'w') as file:
            file.write(str(random_digit))
        
        # Reset the cursor to the beginning of the file
        with open(file_path, 'r+') as file:
            file.seek(0)
    
    return n_files

# Example usage:
# directory_path = 'path/to/your/directory'
# number_of_files = 5
# task_func(directory_path, number_of_files)