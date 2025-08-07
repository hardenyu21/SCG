import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]

def task_func(file_path, save_path=None):
    # Load the dataset
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

    # Check if the dataset is empty
    if df.empty:
        print("The input file is empty.")
        return None

    # Assuming the text data is in a column named 'text'
    if 'text' not in df.columns:
        print("The 'text' column is not found in the dataset.")
        return None

    # Initialize the CountVectorizer with the specified stopwords
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)
    text_data = df['text'].dropna().str.lower().str.join(' ')

    # Fit and transform the text data
    word_counts = vectorizer.fit_transform([text_data])

    # Get feature names and their counts
    feature_names = vectorizer.get_feature_names_out()
    counts = word_counts.toarray().sum(axis=0)

    # Create a dictionary of word counts
    word_count_dict = dict(zip(feature_names, counts))

    # Sort the dictionary by counts in descending order
    sorted_word_counts = sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)

    # Get the ten most common words
    most_common_words = sorted_word_counts[:10]

    # Check if there are any valid words
    if not most_common_words:
        print("The input file contains only stopwords or no valid words.")
        return None

    # Create a histogram of the ten most common words
    words, counts = zip(*most_common_words)
    fig, ax = plt.subplots()
    ax.bar(words, counts)
    ax.set_title('Top 10 Most Common Words')
    ax.set_xlabel('Words')
    ax.set_ylabel('Counts')
    plt.xticks(rotation=45)

    # Save or display the plot
    if save_path:
        plt.savefig(save_path)
        plt.close(fig)
        return None
    else:
        plt.show()
        return ax
import unittest
from unittest.mock import patch
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    @patch("pandas.read_csv")
    def test_empty_csv(self, mock_read_csv):
        """
        Test with an empty CSV file. Checks if the function handles empty data gracefully.
        """
        mock_read_csv.return_value = pd.DataFrame(columns=["Text"])
        result = task_func("dummy_path.csv")
        self.assertIsNone(result, "The function should return None for empty data")
    @patch("pandas.read_csv")
    def test_single_line_csv(self, mock_read_csv):
        """
        Test with a CSV file containing a single line of text. Verifies correct handling of minimal data.
        """
        mock_read_csv.return_value = pd.DataFrame({"Text": ["test"]})
        ax = task_func("dummy_path.csv")
        self.assertEqual(
            len(ax.patches),
            1,
            "There should be one bar in the histogram for a single word",
        )
    @patch("pandas.read_csv")
    def test_stop_words_removal(self, mock_read_csv):
        """
        Test to ensure that stop words are correctly removed from the text.
        """
        mock_read_csv.return_value = pd.DataFrame({"Text": ["a test"]})
        ax = task_func("dummy_path.csv")
        x_labels = [label.get_text() for label in ax.get_xticklabels()]
        self.assertNotIn("a", x_labels, "Stop words should not appear in the histogram")
    @patch("pandas.read_csv")
    @patch("matplotlib.pyplot.savefig")
    def test_save_plot(self, mock_savefig, mock_read_csv):
        """
        Test the functionality of saving the plot to a file.
        """
        mock_read_csv.return_value = pd.DataFrame({"Text": ["save test"]})
        task_func("dummy_path.csv", "output.png")
        mock_savefig.assert_called_with("output.png")
    @patch("pandas.read_csv")
    def test_multiple_lines_csv(self, mock_read_csv):
        """
        Test with a CSV file containing multiple lines of text. Checks for correct handling of multiline data.
        """
        mock_read_csv.return_value = pd.DataFrame({"Text": ["test1", "test2"]})
        ax = task_func("dummy_path.csv")
        self.assertEqual(
            len(ax.patches),
            2,
            "There should be two bars in the histogram for two different words",
        )
    def tearDown(self):
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)