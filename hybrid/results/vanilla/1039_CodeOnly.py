import ssl
import os
import hashlib

def task_func(client_socket, cert_file, key_file, buffer_size=1024):
    try:
        # Wrap the client socket with SSL
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=cert_file, keyfile=key_file)
        secure_socket = context.wrap_socket(client_socket, server_side=True)

        # Receive the file path from the client
        file_path = secure_socket.recv(buffer_size).decode('utf-8').strip()

        # Check if the file exists
        if not os.path.exists(file_path):
            secure_socket.sendall(b'File not found')
            return 'File not found'

        # Calculate the SHA256 hash of the file
        sha256_hash = hashlib.sha256()
        with open(file_path, 'rb') as file:
            for byte_block in iter(lambda: file.read(buffer_size), b""):
                sha256_hash.update(byte_block)

        # Send the hash back to the client
        hash_hex = sha256_hash.hexdigest()
        secure_socket.sendall(hash_hex.encode('utf-8'))

        return hash_hex

    except Exception as e:
        # Handle any exceptions that occur during processing
        error_message = f'Error: {str(e)}'
        secure_socket.sendall(error_message.encode('utf-8'))
        return error_message