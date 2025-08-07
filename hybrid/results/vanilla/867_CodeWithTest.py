import re
import string

def task_func(text1, text2):
    # Define a regular expression pattern to match all ASCII punctuation
    pattern = f"[{re.escape(string.punctuation)}]"
    
    # Remove punctuation from both text1 and text2 using re.sub
    cleaned_text1 = re.sub(pattern, '', text1)
    cleaned_text2 = re.sub(pattern, '', text2)
    
    # Return the cleaned texts as a tuple
    return (cleaned_text1, cleaned_text2)

# Example usage
cleaned_text1, cleaned_text2 = task_func("test (with parenthesis []!!)", "And, other; stuff ^_`")
print(cleaned_text1, cleaned_text2)  # Output: test with parenthesis  And other stuff
import unittest
class TestCases(unittest.TestCase):
    def test_with_common_punctuation(self):
        input_text1 = "Hello, world!"
        input_text2 = "How's it going?"
        expected_output = ("Hello world", "Hows it going")
        self.assertEqual(task_func(input_text1, input_text2), expected_output)
    def test_with_uncommon_punctuation(self):
        input_text1 = "Weird«text»with‰symbols"
        input_text2 = "More»symbols«here†too"
        expected_output = (input_text1, input_text2)  # Unchanged since uncommon punctuations are not removed
        self.assertEqual(task_func(input_text1, input_text2), expected_output)
    def test_with_numeric_characters(self):
        input_text1 = "Text with numbers 12345"
        input_text2 = "67890, numbers continue."
        expected_output = ("Text with numbers 12345", "67890 numbers continue")
        self.assertEqual(task_func(input_text1, input_text2), expected_output)
    def test_empty_strings(self):
        input_text1 = ""
        input_text2 = ""
        expected_output = ("", "")
        self.assertEqual(task_func(input_text1, input_text2), expected_output)
    def test_no_punctuation(self):
        input_text1 = "Just a normal sentence"
        input_text2 = "Another normal sentence"
        expected_output = ("Just a normal sentence", "Another normal sentence")
        self.assertEqual(task_func(input_text1, input_text2), expected_output)
    def test_all_symbols(self):
        input_text1 = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'"'''
        input_text2 = "test"
        expected_output = ("", "test")
        self.assertEqual(task_func(input_text1, input_text2), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)