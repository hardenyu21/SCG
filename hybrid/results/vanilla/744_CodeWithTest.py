import nltk
from string import punctuation
import pandas as pd

def task_func(text):
    # Check if the input is a string
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")
    
    # Tokenize the text into words
    words = text.split()
    
    # Filter words that start with '$' and are not entirely punctuation
    filtered_words = [word for word in words if word.startswith('$') and not all(char in punctuation for char in word[1:])]
    
    # Count the occurrences of each word
    word_counts = nltk.FreqDist(filtered_words)
    
    # Create a DataFrame from the word counts
    df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])
    
    return df

# Example usage
text = "$hello this i$s a $test $test $test"
print(task_func(text))
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
        result = task_func(text)
        expected_words = ["$abc", "$efg", "$hij"]
        expected_freqs = [3, 1, 3]
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    def test_case_2(self):
        text = "This is a test without dollar words."
        result = task_func(text)
        self.assertEqual(len(result), 0)
    def test_case_3(self):
        text = "$test1 $test2 $test1 $test3"
        result = task_func(text)
        expected_words = ["$test1", "$test2", "$test3"]
        expected_freqs = [2, 1, 1]
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    def test_case_4(self):
        text = "$! $$ $a $a $a"
        result = task_func(text)
        expected_words = ["$a"]
        expected_freqs = [3]
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    def test_case_5(self):
        text = "$word1 word2 $word2 $word1 $word3 $word1"
        result = task_func(text)
        expected_words = ["$word1", "$word2", "$word3"]
        expected_freqs = [3, 1, 1]
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    def test_case_6(self):
        '''empty input string'''
        text = ""
        result = task_func(text)
        expected_words = []
        expected_freqs = []
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    
    def test_case_7(self):
        '''check for correct return type'''
        text = "$test 123 abcd.aef"
        result = task_func(text)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('Word' in result.columns)
        self.assertTrue('Frequency' in result.columns)
    def test_case_8(self):
        '''word with $ in the middle'''
        text = "asdfj;alskdfj;$kjhkjhdf"
        result = task_func(text)
        expected_words = []
        expected_freqs = []
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    def test_case_9(self):
        '''non string input'''
        input = 24
        self.assertRaises(Exception, task_func, input)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)