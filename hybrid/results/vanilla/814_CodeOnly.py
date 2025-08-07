import re
import os

def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    # Compile the regular expression pattern
    pattern = re.compile(file_pattern)
    
    # List to store file paths that match the pattern
    matching_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file name matches the pattern
            if pattern.search(file):
                # Construct the full file path
                file_path = os.path.join(root, file)
                matching_files.append(file_path)
    
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Define the path for the configuration file
    config_file_path = os.path.join(target_dir, 'config.txt')
    
    # Write the matching file paths to the configuration file
    with open(config_file_path, 'w') as config_file:
        for file_path in matching_files:
            config_file.write(file_path + '\n')
    
    # Return the path to the created configuration file
    return config_file_path

# Example usage
source_directory = 'C:\\SomeDir\\'
target_directory = 'C:\\ConfigDir\\'
config_file_path = task_func(source_directory, target_directory)
print(f"Configuration file created at: {config_file_path}")