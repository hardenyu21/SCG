import numpy as np
from sklearn.preprocessing import OneHotEncoder

def task_func(list_of_lists):
    # Merge the list of lists into a single list
    merged_list = [item for sublist in list_of_lists for item in sublist]
    
    # Reshape the merged list to a 2D array for OneHotEncoder
    reshaped_list = np.array(merged_list).reshape(-1, 1)
    
    # Initialize the OneHotEncoder
    encoder = OneHotEncoder(sparse=False)
    
    # Fit and transform the reshaped list to get the one-hot encoding
    one_hot = encoder.fit_transform(reshaped_list)
    
    return one_hot

# Example usage:
# list_of_lists = [['apple', 'banana'], ['orange'], ['apple', 'grape']]
# one_hot_encoded = task_func(list_of_lists)
# print(one_hot_encoded)