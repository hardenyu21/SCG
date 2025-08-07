from nltk.tokenize import RegexpTokenizer
from collections import Counter

def task_func(text):
    # Tokenizer to extract words starting with $ and ignore those with only $
    tokenizer = RegexpTokenizer(r'\$\w+')
    tokens = tokenizer.tokenize(text)
    
    # Remove the $ symbol from each token
    dollar_words = [token[1:] for token in tokens if len(token) > 1]
    
    # Count the frequency of each dollar-prefixed word
    word_counts = Counter(dollar_words)
    
    # Get the five most common words
    most_common_words = word_counts.most_common(5)
    
    return most_common_words

# Example usage:
text = "The $price of the $product is $100. The $product is on $sale. $discount available. $$ is not a word."
print(task_func(text))
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
        expected_output = [('abc', 3), ('hij', 3), ('efg', 1)]
        result = task_func(text)
        self.assertEqual(result, expected_output)
    def test_case_2(self):
        text = "This is a test without any $ prefixed words."
        expected_output = []
        result = task_func(text)
        self.assertEqual(result, expected_output)
    def test_case_3(self):
        text = "$apple $banana $apple $cherry $cherry $cherry"
        expected_output = [('cherry', 3), ('apple', 2), ('banana', 1)]
        result = task_func(text)
        self.assertEqual(result, expected_output)
    def test_case_4(self):
        text = "$$ $$ $$ $$"
        expected_output = [('$$', 4)]
        result = task_func(text)
        self.assertEqual(result, expected_output)
    def test_case_5(self):
        text = "$word1 $word2 $word3 $word4 $word5 $word6"
        expected_output = [('word1', 1), ('word2', 1), ('word3', 1), ('word4', 1), ('word5', 1)]
        result = task_func(text)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)