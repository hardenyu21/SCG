import ctypes
import hashlib
import binascii

def task_func(filepath):
    # Load the DLL file
    try:
        dll = ctypes.CDLL(filepath)
    except OSError as e:
        print(f"Error loading DLL: {e}")
        return None

    # Get the actual name of the loaded DLL file
    dll_name = dll._name

    # Calculate MD5 hash
    md5_hash = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    md5_hex = binascii.hexlify(md5_hash.digest()).decode('utf-8')

    # Calculate SHA256 hash
    sha256_hash = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    sha256_hex = binascii.hexlify(sha256_hash.digest()).decode('utf-8')

    # Print the hashes
    print(f"MD5 Hash: {md5_hex}")
    print(f"SHA256 Hash: {sha256_hex}")

    # Return the actual name of the loaded DLL file
    return dll_name

# Example usage:
# dll_name = task_func("path_to_your_dll.dll")
# print(f"Loaded DLL Name: {dll_name}")