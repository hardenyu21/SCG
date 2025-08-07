import os
import random
import json

def task_func(directory, n):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(n):
        # Generate a random integer between 1 and 100
        random_number = random.randint(1, 100)
        
        # Create a JSON object with the key 'number'
        json_content = {'number': random_number}
        
        # Convert the JSON object to a string
        json_string = json.dumps(json_content)
        
        # Define the file path
        file_path = os.path.join(directory, f'file_{i+1}.json')
        
        # Write the JSON content to the file
        with open(file_path, 'w+') as file:
            file.write(json_string)
            # Reset the cursor to the beginning of the file
            file.seek(0)
    
    # Output the directory where the files were generated
    return directory