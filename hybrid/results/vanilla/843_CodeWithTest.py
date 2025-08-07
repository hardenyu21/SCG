import random
import re

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def task_func(n_sentences):
    sentences = []
    for _ in range(n_sentences):
        # Randomly choose a number of words for the sentence (1 to 5)
        num_words = random.randint(1, 5)
        # Randomly select words from the WORD_LIST
        sentence_words = random.sample(WORD_LIST, num_words)
        # Join the words into a sentence
        sentence = ' '.join(sentence_words) + '.'
        # Append the sentence to the list
        sentences.append(sentence)
    
    # Join all sentences into a single string
    result = ' '.join(sentences)
    # Convert to lowercase and remove non-alphanumeric characters except spaces and periods
    result = re.sub(r'[^a-z0-9 .]', '', result.lower())
    
    return result

# Example usage
print(task_func(3))
import unittest
import re
class TestCases(unittest.TestCase):
    def test_single_sentence(self):
        result = task_func(1)
        self.assertIsInstance(result, str)
        self.assertEqual(result.count('.'), 1)
        self.assertTrue(result.endswith('.'))
        self.assertTrue(all(c.isalnum() or c.isspace() or c == '.' for c in result))
    def test_multiple_sentences(self):
        result = task_func(3)
        # Ensure the text ends with a period for accurate splitting
        self.assertTrue(result.endswith('.'), "The generated text should end with a period.")
        # Split the sentences properly by using regex that keeps the period with each sentence
        sentences = re.split(r'(?<=\.)\s+', result.strip())
        self.assertEqual(len(sentences), 3, "There should be exactly three sentences.")
        # Check that each sentence (excluding the last split empty due to trailing period) ends with a period
        self.assertTrue(all(sentence.endswith('.') for sentence in sentences), "Each sentence should end with a period.")
    def test_no_sentences(self):
        result = task_func(0)
        self.assertEqual(result, '')
    def test_randomness(self):
        random.seed(42)  # Set seed for reproducibility in testing
        result1 = task_func(2)
        random.seed(42)
        result2 = task_func(2)
        self.assertEqual(result1, result2)
    def test_sentence_length(self):
        result = task_func(1)
        words = result[:-1].split()  # Remove period and split by spaces
        self.assertTrue(5 <= len(words) <= 10)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)