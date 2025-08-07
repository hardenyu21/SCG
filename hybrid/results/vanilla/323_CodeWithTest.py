import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture

def task_func(text, num_gaussians=1, seed=42):
    # Check for valid number of Gaussians
    if num_gaussians <= 0:
        raise ValueError("num_gaussians must be greater than 0.")
    
    # Extract names not enclosed by square brackets
    names = re.findall(r'\b(?!\[)[A-Za-z]+\b(?!\])', text)
    
    # Tokenize names into words
    words = [word for name in names for word in name.split()]
    
    # Count the frequency of each word
    word_freq = Counter(words)
    
    # Check if num_gaussians is greater than the number of unique words
    if num_gaussians > len(word_freq):
        raise Exception("num_gaussians must not be greater than the number of unique words.")
    
    # Prepare data for Gaussian Mixture Model
    word_freq_values = np.array(list(word_freq.values())).reshape(-1, 1)
    
    # Fit Gaussian Mixture Model
    gmm = GaussianMixture(n_components=num_gaussians, random_state=seed)
    gmm.fit(word_freq_values)
    
    # Extract means and variances
    means = gmm.means_.flatten()
    variances = gmm.covariances_.flatten()
    
    # Return the dictionary of word frequencies
    return {
        'word_frequencies': word_freq,
        'means': means,
        'variances': variances
    }
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        text = "John Doe [1234 Elm St, Springfield, IL 12345]Jane Smith [5678 Maple Dr, Anytown, CA 67890]"
        result, _ = task_func(text)
        expected = {'John': 1, 'Doe': 1, 'Jane': 1, 'Smith': 1}
        self.assertDictEqual(result, expected)
    def test_case_2(self):
        text = "Alice [7890 Oak Ln, Someplace, TX 23456]Bob Charlie Bob [2345 Birch Rd, Otherplace, NY 34567]"
        result, means = task_func(text, 2)
        expected = {'Alice': 1, 'Bob': 2, 'Charlie': 1}
        self.assertDictEqual(result, expected)
        self.assertAlmostEquals(means[0][0], 2.00, places=2)
        self.assertAlmostEquals(means[1][0], 1.00, places=2)
    def test_case_3(self):
        text = "Eve [3456 Cedar St, Thisplace, WA 45678]"
        self.assertRaises(Exception, task_func, text)
    def test_case_4(self):
        text = "Frank Grace Holly [4567 Pine Pl, Thatplace, NV 56789]"
        result, _ = task_func(text)
        expected = {'Frank': 1, 'Grace': 1, 'Holly': 1}
        self.assertDictEqual(result, expected)
    def test_case_5(self):
        text = "Ivy Jack [5678 Spruce Way, Hereplace, ME 67890]Katherine [6789 Fir Blvd, Thereplace, VT 78901]Leo"
        result, _ = task_func(text)
        expected = {'Ivy': 1, 'Jack': 1, 'Katherine': 1, 'Leo': 1}
        self.assertDictEqual(result, expected)
        # Long test case
        long_text = "Antony [2345 Elm St, Thiscity, CA 34567]Barbara [3456 Oak Dr, Thatcity, NY 45678]" + \
                    "Barbara [4567 Maple Ave, Othercity, TX 56789]Diana [5678 Birch Rd, Newcity, WA 67890]" + \
                    "Edward [6789 Cedar Ln, Oldcity, NV 78901]Antony [7890 Pine St, Anytown, ME 89012]" + \
                    "George [8901 Spruce Dr, Someplace, VT 90123]Helen [9012 Fir Ave, Anywhere, MD 01234]" + \
                    "Ian [0123 Elm Blvd, Nowhere, WI 12345]Jessica [1234 Oak Way, Everywhere, IL 23456]" + \
                    "Kevin [2345 Maple Pl, Somewhere, CA 34567]Laura [3456 Birch St, Thisplace, NY 45678]" + \
                    "Michael [4567 Cedar Dr, Thatplace, TX 56789]Barbara [5678 Pine Ave, Otherplace, WA 67890]" + \
                    "Oliver [6789 Spruce Rd, Newplace, NV 78901]Patricia [7890 Fir St, Oldplace, ME 89012]" + \
                    "Quentin [8901 Elm Dr, Anyplace, VT 90123]Rachel [9012 Oak Ln, Somecity, MD 01234]" + \
                    "Samuel [0123 Maple Dr, Thatcity, WI 12345]Antony [1234 Birch St, Othercity, IL 23456]" + \
                    "Ursula [2345 Cedar Ave, Newcity, CA 34567]Victor [3456 Pine Rd, Oldcity, NY 45678]" + \
                    "Wendy [4567 Spruce St, Anytown, TX 56789]John [5678 Fir Dr, Someplace, WA 67890]" + \
                    "Zachary [6789 Elm Way, Anywhere, NV 78901]Zachary [7890 Oak Pl, Nowhere, ME 89012]"
        result, means = task_func(long_text, 2)
        self.assertAlmostEquals(means[0][0], 1.05, places=2)
        self.assertAlmostEquals(means[1][0], 3.00, places=2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)