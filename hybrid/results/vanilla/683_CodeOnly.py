import math
import yaml

def task_func(yaml_path, key):
    # Read the YAML file
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    
    # Check if the key exists in the data
    if key in data:
        # Apply the cosine function to the value associated with the key
        data[key] = math.cos(data[key])
    else:
        raise KeyError(f"The key '{key}' does not exist in the YAML data.")
    
    # Write the modified data back to the YAML file
    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)
    
    # Return the modified data
    return data