import os
import ctypes
import sys
import subprocess

def task_func(filepath):
    # Check if the filepath is a string
    if not isinstance(filepath, str):
        raise TypeError("The input filepath must be a string.")
    
    # Check if the filepath is valid and not empty
    if not filepath or not os.path.isfile(filepath):
        raise OSError("The input filepath is invalid or empty.")
    
    # Load the DLL file
    try:
        dll = ctypes.CDLL(filepath)
    except OSError as e:
        raise OSError(f"Failed to load the DLL file: {e}")
    
    # Retrieve system information
    import platform
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Python Version": sys.version,
        "PIP Version": subprocess.check_output([sys.executable, '-m', 'pip', '--version']).decode('utf-8').split()[1]
    }
    
    # Print system information
    print("System: {System} Node Name: {Node Name} Release: {Release} Version: {Version} Machine: {Machine} Python Version: {Python Version} PIP Version: {PIP Version}".format(**system_info))
    
    # Return the name of the loaded DLL file
    return os.path.basename(filepath)