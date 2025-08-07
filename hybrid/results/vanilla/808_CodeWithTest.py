import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    # Split the text into words
    words = text.split()
    
    # Remove stopwords and duplicates
    unique_words = []
    seen = set()
    for word in words:
        if word not in STOPWORDS and word not in seen:
            unique_words.append(word)
            seen.add(word)
    
    # Join the unique words back into a string
    cleaned_text = ' '.join(unique_words)
    
    # Analyze the sentiment of the cleaned text
    blob = TextBlob(cleaned_text)
    sentiment = blob.sentiment
    
    # Output the sentiment
    return f"Sentiment: {sentiment}"

# Example usage
text = "This is a sample text with some sample words and some stopwords."
print(task_func(text))
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test Case 1: Regular Sentence
        # Description: This test case checks the function's behavior with a regular sentence containing duplicate words
        # and stopwords. The function should remove the duplicate words and stopwords, and return the sentiment analysis
        # result as a tuple of two float values.
        text = "The quick brown fox jumps over the lazy dog and the dog was not quick."
        sentiment = task_func(text)
        self.assertIsInstance(sentiment, tuple, "The function should return a tuple")
        self.assertEqual(len(sentiment), 2, "The tuple should contain two elements")
        self.assertIsInstance(sentiment[0], float, "The polarity should be a float")
        self.assertIsInstance(sentiment[1], float, "The subjectivity should be a float")
    def test_case_2(self):
        # Test Case 2: Empty String
        # Description: This test case checks the function's behavior with an empty string. The function should return
        # (0.0, 0.0) as the sentiment of an empty string is neutral.
        text = ""
        sentiment = task_func(text)
        self.assertEqual(sentiment, (0.0, 0.0), "The sentiment of an empty string should be (0.0, 0.0)")
    def test_case_3(self):
        # Test Case 3: Positive Sentiment
        # Description: This test case checks the function's behavior with a sentence that has a positive sentiment.
        # The function should return a positive polarity value.
        text = "I absolutely love this! It's amazing."
        sentiment = task_func(text)
        self.assertGreater(sentiment[0], 0, "The polarity of a positive sentiment sentence should be greater than 0")
    def test_case_4(self):
        # Test Case 4: Negative Sentiment
        # Description: This test case checks the function's behavior with a sentence that has a negative sentiment.
        # The function should return a negative polarity value.
        text = "This is really bad. I hate it."
        sentiment = task_func(text)
        self.assertLess(sentiment[0], 0, "The polarity of a negative sentiment sentence should be less than 0")
    def test_case_5(self):
        # Test Case 5: Neutral Sentiment
        # Description: This test case checks the function's behavior with a sentence that has a neutral sentiment.
        # The function should return a zero polarity value.
        text = "This is a pen."
        sentiment = task_func(text)
        self.assertEqual(sentiment[0], 0, "The polarity of a neutral sentiment sentence should be 0")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)