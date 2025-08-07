import rsa
import os
import zipfile
from base64 import b64encode

def task_func(directory):
    # Generate RSA public and private keys
    (public_key, private_key) = rsa.newkeys(2048)

    # Create a temporary directory to store encrypted files
    temp_dir = 'encrypted_files'
    os.makedirs(temp_dir, exist_ok=True)

    # Encrypt each file in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()
                # Encrypt the file data using the public key
                encrypted_data = rsa.encrypt(file_data, public_key)
                # Encode the encrypted data in base64 to ensure it's safe to write to a file
                encoded_data = b64encode(encrypted_data).decode('utf-8')
                # Save the encrypted data to a new file in the temporary directory
                encrypted_file_path = os.path.join(temp_dir, filename + '.enc')
                with open(encrypted_file_path, 'w') as encrypted_file:
                    encrypted_file.write(encoded_data)

    # Create a zip file containing all the encrypted files
    zip_filename = 'encrypted_files.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_dir)
                zipf.write(file_path, arcname)

    # Clean up the temporary directory
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_dir)

    # Return the public key and the name of the zip file
    return public_key, zip_filename