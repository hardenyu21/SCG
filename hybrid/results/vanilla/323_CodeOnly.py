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