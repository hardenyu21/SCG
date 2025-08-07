import re
import os
import subprocess

def task_func(dir_path, exe_pattern, execute_files=True):
    results = []
    
    # Compile the regular expression pattern
    pattern = re.compile(exe_pattern)
    
    # Iterate over all files in the specified directory
    for root, _, files in os.walk(dir_path):
        for file in files:
            # Check if the file matches the regular expression pattern
            if pattern.match(file):
                file_path = os.path.join(root, file)
                
                if execute_files:
                    # Execute the file and capture the standard output
                    try:
                        result = subprocess.check_output([file_path], stderr=subprocess.STDOUT, text=True)
                        results.append(result)
                    except subprocess.CalledProcessError as e:
                        # If execution fails, append the error output
                        results.append(e.output)
                else:
                    # If not executing, just add the file path to the results
                    results.append(file_path)
    
    return results