import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Constants
ALPHANUMERIC = re.compile('[\W_]+')
PUNCTUATIONS = string.punctuation

def task_func(text: str, sia: SentimentIntensityAnalyzer) -> dict:
    # Clean the text
    # Remove all non-alphanumeric characters except spaces
    text = ALPHANUMERIC.sub(' ', text)
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', PUNCTUATIONS))
    
    # Analyze sentiment
    sentiment_scores = sia.polarity_scores(text)
    
    return sentiment_scores

# Example usage
if __name__ == "__main__":
    sia = SentimentIntensityAnalyzer()
    text = "I love this product! It's amazing and works great."
    sentiment = task_func(text, sia)
    print(sentiment)
import unittest
# Mock the SentimentIntensityAnalyzer for our tests
class MockedSentimentIntensityAnalyzer:
    def polarity_scores(self, text):
        return {'compound': 0.5, 'neg': 0.25, 'neu': 0.25, 'pos': 0.5}
class TestCases(unittest.TestCase):
    def test_case_1(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = task_func("I love Python!", sia)
        expected = {'compound': 0.5, 'neg': 0.25, 'neu': 0.25, 'pos': 0.5}
        self.assertEqual(result, expected)
    
    def test_case_2(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = task_func("I hate rainy days.", sia)
        self.assertEqual(result['neg'], 0.25)
    
    def test_case_3(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = task_func("The weather is neutral today.", sia)
        self.assertEqual(result['neu'], 0.25)
    
    def test_case_4(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = task_func("Absolutely fantastic!", sia)
        self.assertEqual(result['pos'], 0.5)
    
    def test_case_5(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = task_func("This is a bad idea!", sia)
        self.assertEqual(result['neg'], 0.25)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)