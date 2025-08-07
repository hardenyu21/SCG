import os
from datetime import datetime

def task_func(filepath: str) -> dict:
    try:
        # Get the size of the file in bytes
        size = os.path.getsize(filepath)
        
        # Get the last modification time of the file
        mod_time = os.path.getmtime(filepath)
        
        # Convert the modification time to a readable format
        mod_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
        
        # Return the results in a dictionary
        return {
            'size': size,
            'last_modified': mod_date
        }
    except FileNotFoundError:
        return {'error': 'File not found'}
    except Exception as e:
        return {'error': str(e)}