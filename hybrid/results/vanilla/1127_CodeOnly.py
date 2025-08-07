import os
import re
import hashlib

def task_func(path, delimiter):
    # Split the path by the specified delimiter, retaining the delimiter in the output
    components = re.split(f'({re.escape(delimiter)})', path)
    
    # Initialize the result list
    result = []
    
    # Iterate over the components
    for component in components:
        # Check if the component is a file
        if os.path.isfile(component):
            # Compute the hash of the file
            file_hash = hashlib.sha256()
            with open(component, 'rb') as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    file_hash.update(byte_block)
            result.append((component, file_hash.hexdigest()))
        else:
            # If it's not a file, append None as the hash
            result.append((component, None))
    
    return result