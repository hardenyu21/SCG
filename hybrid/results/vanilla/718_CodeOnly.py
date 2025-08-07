import re
import numpy as np
from scipy.stats import ttest_rel

def task_func(text1, text2):
    # Function to count words in a string
    def count_words(text):
        # Use regex to find words
        words = re.findall(r'\b\w+\b', text)
        return len(words)
    
    # Count words in both texts
    words1 = count_words(text1)
    words2 = count_words(text2)
    
    # Check if the number of words is the same
    if words1 != words2:
        return np.nan, np.nan
    
    # Convert the number of words to arrays (for t-test)
    data1 = np.array([words1])
    data2 = np.array([words2])
    
    # Perform paired t-test
    t_statistic, p_value = ttest_rel(data1, data2)
    
    return t_statistic, p_value