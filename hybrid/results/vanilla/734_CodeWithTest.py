import nltk
# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from collections import Counter

def task_func(content):
    # Tokenize the sentence into words
    words = nltk.word_tokenize(content)
    
    # Remove the last word
    words = words[:-1]
    
    # Get the POS tags for the words
    pos_tags = nltk.pos_tag(words)
    
    # Extract only the POS tags from the list of tuples
    pos_tags_list = [tag for word, tag in pos_tags]
    
    # Count the occurrences of each POS tag
    pos_count = Counter(pos_tags_list)
    
    return dict(pos_count)

# Example usage:
# sentence = "The quick brown fox jumps over the lazy dog."
# print(task_func(sentence))
import unittest
import re
class TestCases(unittest.TestCase):
    def test_case_1(self):
        sentence = "this is an example content"
        # Expected output after removing "content"
        expected_output = {'DT': 2, 'NN': 1, 'VBZ': 1}
        self.assertEqual(task_func(sentence), expected_output)
    def test_case_2(self):
        sentence = "The quick brown fox jumps"
        # "jumps" is removed; expect {'DT': 1, 'JJ': 1, 'NN': 1} for "The quick brown fox"
        expected_output = {'DT': 1, 'JJ': 1, 'NN': 2}
        self.assertEqual(task_func(sentence), expected_output)
    def test_case_3(self):
        sentence = "Over the lazy dog"
        # "dog" is removed; expect {'IN': 1, 'DT': 1, 'JJ': 1} for "Over the lazy"
        expected_output = {'DT': 1, 'IN': 1, 'NN': 1}
        self.assertEqual(task_func(sentence), expected_output)
    def test_case_4(self):
        sentence = "Hello world"
        # "world" is removed; expect {} for "Hello"
        expected_output = {'NN': 1}  # "Hello" might be tagged as interjection 'UH' if not considered a proper noun
        self.assertEqual(task_func(sentence), expected_output)
    def test_case_5(self):
        sentence = "This is a longer sentence with various parts of speech"
        # After removing "speech", adjust expectation
        expected_output = {'DT': 2, 'IN': 2, 'JJ': 1, 'NN': 1, 'NNS': 1, 'RBR': 1, 'VBZ': 1}
        self.assertEqual(task_func(sentence), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)