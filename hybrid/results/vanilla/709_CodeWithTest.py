import base64
import re
from html import unescape
import textwrap

def task_func(raw_string, line_length):
    # Decode the base64 encoded string
    decoded_bytes = base64.b64decode(raw_string)
    decoded_string = decoded_bytes.decode('utf-8')
    
    # Decouple HTML entities
    unescaped_string = unescape(decoded_string)
    
    # Replace multiple spaces with a single space
    single_spaced_string = re.sub(r'\s+', ' ', unescaped_string)
    
    # Strip leading and trailing spaces
    stripped_string = single_spaced_string.strip()
    
    # Wrap text to the specified line length
    wrapped_text = textwrap.fill(stripped_string, width=line_length)
    
    return wrapped_text
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(task_func('SGVsbG8sICBXb3JsZCEgICAg', 5), 'Hello\n, Wor\nld!')
    def test_case_2(self):
        self.assertEqual(task_func('SGVsbG8sICBXb3JsZCEgICAg', 10), 'Hello,\nWorld!')
    def test_case_3(self):
        self.assertEqual(task_func('SGVsbG8sICBXb3JsZCEgICAg', 20), 'Hello, World!')
    def test_case_4(self):
        self.assertEqual(task_func('SGVsbG8sICBXb3JsZCEgICAg', 1), 'H\ne\nl\nl\no\n,\nW\no\nr\nl\nd\n!')
    def test_case_5(self):
        self.assertEqual(task_func('SGVsbG8sICBXb3JsZCEgICAg', 2), 'He\nll\no,\nWo\nrl\nd!')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)