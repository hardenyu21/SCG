import ctypes
import os
import shutil
import glob

def task_func(filepath, destination_dir):
    # Load the DLL file specified by the given filepath
    try:
        dll_name = os.path.basename(filepath)
        dll = ctypes.CDLL(filepath)
        print(f"Successfully loaded DLL: {dll_name}")
    except Exception as e:
        print(f"Failed to load DLL: {dll_name}. Error: {e}")
        return None

    # Get the directory of the loaded DLL
    dll_directory = os.path.dirname(filepath)

    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Move all DLL files in the same directory to the destination directory
    try:
        dll_files = glob.glob(os.path.join(dll_directory, '*.dll'))
        for dll_file in dll_files:
            if dll_file != filepath:  # Skip the already loaded DLL
                shutil.move(dll_file, destination_dir)
                print(f"Moved DLL: {os.path.basename(dll_file)} to {destination_dir}")
    except Exception as e:
        print(f"Error moving DLL files: {e}")

    # Return the name of the loaded DLL file
    return dll_name