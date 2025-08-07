import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(page_title):
    try:
        # Fetch the content of the Wikipedia page
        page_content = wikipedia.page(page_title).content
        
        # Generate a word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(page_content)
        
        # Plot the word cloud
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')  # Turn off the axis
        
        # Return the Axes object
        return ax
    except wikipedia.exceptions.PageError:
        # Return None if the page does not exist
        return None
import unittest
from unittest.mock import patch
class A :
    def __init__(self, content) -> None:
        self.content = content
        self.text = content
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    @patch('wikipedia.page')
    def test_case_1(self, mock_function):
        # Mocking the function to prevent actual execution
        mock_function.return_value = A("I want to sleep")
        # Running the function
        _ = task_func('Python (programming language)')
    @patch('wikipedia.page')
    def test_case_2(self, mock_function):
        # Mocking the function to prevent actual execution
        mock_function.return_value = A("I want to sleep because it is important to sleep.")
        # Running the function
        _ = task_func('Python (programming language)')
    @patch('wikipedia.page')
    def test_case_3(self, mock_function):
        # Mocking the function to prevent actual execution
        mock_function.return_value = A("I want to sleep")
        # Running the function
        _ = task_func('Python (programming language)')
    @patch('wikipedia.page')
    def test_case_4(self, mock_function):
        # Mocking the function to prevent actual execution
        mock_function.return_value =A("I want to eat")
        # Running the function
        _ = task_func('Python (programming language)')
    @patch('wikipedia.page')
    def test_case_5(self, mock_function):
        # Mocking the function to prevent actual execution
        mock_function.return_value = A("I want to help you to get your business to work.")
        # Running the function
        _ = task_func('Python (programming language)')
    def test_case_6(self):
        ax = task_func("Invalid Page Title")
        self.assertIsNone(ax)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)