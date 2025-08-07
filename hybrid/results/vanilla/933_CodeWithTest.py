import string
import wordninja

def task_func(word):
    # Split the word into a list of words using wordninja
    words = wordninja.split(word)
    
    # Initialize an empty list to store the tuples
    result = []
    
    # Iterate over each word in the list
    for w in words:
        # Iterate over each character in the word
        for index, char in enumerate(w):
            # Convert the character to lowercase
            lower_char = char.lower()
            # Find the position of the character in the alphabet
            if lower_char in string.ascii_lowercase:
                position = string.ascii_lowercase.index(lower_char) + 1
                # Append the tuple (character, position) to the result list
                result.append((lower_char, position))
    
    return result

# Example usage:
# print(task_func("helloworld"))
import unittest
class TestCases(unittest.TestCase):
    
    def test_basic_word(self):
        self.assertEqual(task_func('abc'), ([('a', 1), ('b', 2), ('c', 3)], ['abc']))
        
    def test_non_consecutive_letters(self):
        self.assertEqual(task_func('ihatehim'), ([('i', 9), ('h', 8), ('a', 1), ('t', 20), ('e', 5), ('h', 8), ('i', 9), ('m', 13)], ['i', 'hate', 'him']))
    
    def test_single_letter(self):
        self.assertEqual(task_func('hellohello'), ([('h', 8), ('e', 5), ('l', 12), ('l', 12), ('o', 15), ('h', 8), ('e', 5), ('l', 12), ('l', 12), ('o', 15)], ['hello', 'hello']))
        
    def test_repeated_letters(self):
        self.assertEqual(task_func('aa'), ([('a', 1), ('a', 1)], ['a', 'a']))
        
    def test_empty_string(self):
        self.assertEqual(task_func(''), ([], []))
        
    def test_long_word(self):
        result = task_func('abcdefghijklmnopqrstuvwxyz')
        ALPHABET = list(string.ascii_lowercase)
        expected = [(letter, index + 1) for index, letter in enumerate(ALPHABET)]
        self.assertEqual(result, (expected, ['abcde', 'fg', 'hi', 'j', 'klm', 'no', 'p', 'qrs', 'tu', 'vw', 'xyz']))
        
    def test_word_with_uppercase_should_fail(self):
        with self.assertRaises(ValueError):
            task_func('aBc')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)