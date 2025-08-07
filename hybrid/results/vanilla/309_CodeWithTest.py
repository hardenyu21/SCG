import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_lists, seed=42):
    # Set the random seed for reproducibility
    random.seed(seed)
    np.random.seed(seed)
    
    # Fill empty inner lists with five random integers between 0 and 100
    for i in range(len(list_of_lists)):
        if not list_of_lists[i]:
            list_of_lists[i] = [random.randint(0, 100) for _ in range(5)]
    
    # Flatten the list of lists to scale all values together
    flat_list = [item for sublist in list_of_lists for item in sublist]
    
    # Reshape the flat list to a 2D array for MinMaxScaler
    flat_list_reshaped = np.array(flat_list).reshape(-1, 1)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Fit and transform the data
    scaled_flat_list = scaler.fit_transform(flat_list_reshaped)
    
    # Reshape the scaled data back into the original list of lists structure
    scaled_list_of_lists = []
    index = 0
    for sublist in list_of_lists:
        sublist_length = len(sublist)
        scaled_sublist = scaled_flat_list[index:index + sublist_length].flatten().tolist()
        scaled_list_of_lists.append(scaled_sublist)
        index += sublist_length
    
    return scaled_list_of_lists
import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        input_data = [[1, 2, 3], [], [4, 5, 6]]
        output = task_func(input_data)
        for inner_list in output:
            self.assertTrue(0.0 <= min(inner_list) <= 1.0)
            self.assertTrue(0.0 <= max(inner_list) <= 1.0)
            self.assertTrue(len(inner_list) <= 5)
    
    def test_case_2(self):
        input_data = [[10, 20, 30, 40, 50], [], [60, 70, 80, 90, 100]]
        output = task_func(input_data)
        for inner_list in output:
            self.assertTrue(0.0 <= min(inner_list) <= 1.0)
            self.assertTrue(0.0 <= max(inner_list) <= 1.0)
            self.assertEqual(len(inner_list), 5)
        
    def test_case_3(self):
        input_data = [[], [], []]
        output = task_func(input_data)
        for inner_list in output:
            self.assertTrue(0.0 <= min(inner_list) <= 1.0)
            self.assertTrue(0.0 <= max(inner_list) <= 1.0)
            self.assertEqual(len(inner_list), 5)
    def test_case_4(self):
        input_data = [[15], [25], [35], [45], [55]]
        expected_output = [[0.0], [0.0], [0.0], [0.0], [0.0]]
        output = task_func(input_data)
        self.assertEqual(output, expected_output)
    
    def test_case_5(self):
        input_data = [[0, 100], [0, 50], [50, 100]]
        expected_output = [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0]]
        output = task_func(input_data)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)