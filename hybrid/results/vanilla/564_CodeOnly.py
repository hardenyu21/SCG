import os
import ctypes
from datetime import datetime
import pytz

def task_func(filepath):
    # Load the DLL file using ctypes
    try:
        dll = ctypes.CDLL(filepath)
    except OSError as e:
        return f"Error loading DLL: {e}", {}

    # Get the DLL file name
    dll_name = os.path.basename(filepath)

    # Get file metadata
    try:
        # Get creation time
        creation_time = os.path.getctime(filepath)
        creation_time_utc = datetime.fromtimestamp(creation_time, pytz.utc)

        # Get modification time
        modification_time = os.path.getmtime(filepath)
        modification_time_utc = datetime.fromtimestamp(modification_time, pytz.utc)

        # Get file size
        file_size = os.path.getsize(filepath)

        # Prepare metadata dictionary
        metadata = {
            'Creation Time': creation_time_utc.isoformat(),
            'Modification Time': modification_time_utc.isoformat(),
            'Size': file_size
        }

        return dll_name, metadata

    except OSError as e:
        return f"Error accessing file metadata: {e}", {}

# Example usage:
# dll_name, metadata = task_func('path_to_your_dll.dll')
# print(f"Loaded DLL: {dll_name}")
# print("Metadata:", metadata)