import numpy as np
from difflib import SequenceMatcher
import matplotlib.pyplot as plt

def task_func(s_list, plot_path=None):
    # Validate input
    if not isinstance(s_list, list) or not all(isinstance(item, str) for item in s_list):
        raise ValueError("s_list must be a list of strings.")
    
    # Handle the case where the list contains a single element
    if len(s_list) == 1:
        return [np.nan]
    
    # Calculate average similarity scores
    scores = []
    for i, str1 in enumerate(s_list):
        total_similarity = 0
        for j, str2 in enumerate(s_list):
            if i != j:
                similarity = SequenceMatcher(None, str1, str2).ratio()
                total_similarity += similarity
        average_similarity = total_similarity / (len(s_list) - 1)
        scores.append(average_similarity)
    
    # Plot the scores if a plot path is provided
    if plot_path:
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(s_list)), scores, tick_label=[f'String {i+1}' for i in range(len(s_list))])
        plt.xlabel('Strings')
        plt.ylabel('Average Similarity Score')
        plt.title('Average Similarity Scores of Strings')
        plt.savefig(plot_path)
        plt.close()
    
    return scores