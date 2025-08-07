import numpy as np
from scipy import stats

def task_func(word: str) -> (np.ndarray, float):
    # Calculate the differences between ASCII values of adjacent letters
    differences = np.array([ord(word[i+1]) - ord(word[i]) for i in range(len(word) - 1)])
    
    # Calculate the entropy of the differences
    # First, calculate the probability distribution of the differences
    value_counts = np.bincount(differences)
    probabilities = value_counts / len(differences)
    
    # Calculate entropy using the formula: H(X) = -sum(p(x) * log2(p(x)))
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))  # Adding a small epsilon to avoid log(0)
    
    return differences, entropy