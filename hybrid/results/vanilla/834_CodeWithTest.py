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
import unittest
import binascii
import io
import gzip
def generate_compressed_hex(original_string):
    """
    Helper function to generate a gzip-compressed hexadecimal string from an original string.
    """
    compressed_bytes = gzip.compress(original_string.encode('utf-8'))
    compressed_hex = binascii.hexlify(compressed_bytes).decode('utf-8')
    return compressed_hex
class TestCases(unittest.TestCase):
    def test_1(self):
        # Test with the word "HELLO"
        compressed_hex = generate_compressed_hex("HELLO")
        self.assertEqual(task_func(compressed_hex), "HELLO")
    def test_2(self):
        # Test with a single character "A"
        compressed_hex = generate_compressed_hex("A")
        self.assertEqual(task_func(compressed_hex), "A")
    def test_3(self):
        # Test with numbers "12345"
        compressed_hex = generate_compressed_hex("12345")
        self.assertEqual(task_func(compressed_hex), "12345")
    def test_4(self):
        # Test with special characters "!@#"
        compressed_hex = generate_compressed_hex("!@#")
        self.assertEqual(task_func(compressed_hex), "!@#")
    def test_5(self):
        # Test with an empty string
        compressed_hex = generate_compressed_hex("")
        self.assertEqual(task_func(compressed_hex), "")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)