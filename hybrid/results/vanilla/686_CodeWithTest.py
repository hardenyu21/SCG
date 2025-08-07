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
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).shape, (9, 9))
    def test_case_2(self):
        arr = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertTrue(np.all(arr.sum(axis=0) == 1))
        self.assertTrue(np.all(arr.sum(axis=1) == 1))
        self.assertTrue(np.all(arr >= 0))
    def test_case_3(self):
        arr = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(arr[0, 0], 1)
        self.assertEqual(arr[1, 1], 1)
        self.assertEqual(arr[2, 2], 1)
        self.assertEqual(arr[3, 3], 1)
        self.assertEqual(arr[4, 4], 1)
        self.assertEqual(arr[5, 5], 1)
        self.assertEqual(arr[6, 6], 1)
        self.assertEqual(arr[7, 7], 1)
        self.assertEqual(arr[8, 8], 1)
        
    def test_case_4(self):
        arr = task_func([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        self.assertEqual(arr[0, 0], 1)
        self.assertEqual(arr[1, 0], 1)
        self.assertEqual(arr[2, 0], 1)
        self.assertEqual(arr[3, 1], 1)
        self.assertEqual(arr[4, 1], 1)
        self.assertEqual(arr[5, 1], 1)
        self.assertEqual(arr[6, 2], 1)
        self.assertEqual(arr[7, 2], 1)
        self.assertEqual(arr[8, 2], 1)
    def test_case_5(self):
        arr = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(arr[0, 0], 1)
        self.assertEqual(arr[1, 1], 1)
        self.assertEqual(arr[2, 2], 1)
        self.assertEqual(arr[3, 3], 1)
        self.assertEqual(arr[4, 4], 1)
        self.assertEqual(arr[5, 5], 1)
        self.assertEqual(arr[6, 6], 1)
        self.assertEqual(arr[7, 7], 1)
        self.assertEqual(arr[8, 8], 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)