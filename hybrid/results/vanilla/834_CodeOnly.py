import binascii
import io
import gzip

def task_func(compressed_hex):
    try:
        # Convert the hexadecimal string to bytes
        compressed_bytes = binascii.unhexlify(compressed_hex)
        
        # Use a BytesIO object to work with the bytes as a file-like object
        byte_stream = io.BytesIO(compressed_bytes)
        
        # Decompress the gzip-compressed data
        with gzip.GzipFile(fileobj=byte_stream, mode='rb') as gzip_file:
            decompressed_bytes = gzip_file.read()
        
        # Decode the decompressed bytes to a UTF-8 string
        decoded_string = decompressed_bytes.decode('utf-8')
        
        return decoded_string
    
    except (binascii.Error, gzip.BadGzipFile, UnicodeDecodeError) as e:
        return f"Error: {str(e)}"

# Example usage:
# compressed_hex = "1f8b0800000000000003edc9b15708cf2fca495504000000"
# print(task_func(compressed_hex))