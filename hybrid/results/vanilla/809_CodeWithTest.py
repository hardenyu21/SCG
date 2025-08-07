import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters):
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the cluster labels for each data point
    labels = kmeans.labels_
    
    # Create a dictionary to store the indices of data points in each cluster
    cluster_dict = {}
    for i, label in enumerate(labels):
        if label not in cluster_dict:
            cluster_dict[label] = []
        cluster_dict[label].append(i)
    
    # Convert the lists of indices to numpy arrays
    for label in cluster_dict:
        cluster_dict[label] = np.array(cluster_dict[label])
    
    return cluster_dict

# Example usage
data = np.array([[1, 1], [2, 2]])
cluster = task_func(data, 2)
cluster_list = list(cluster.values())
cluster_list.sort(key=lambda x: x[0])
print(cluster_list)  # Output: [array([0]), array([1])]
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data = np.array([[1, 1], [1.1, 1.1], [5, 5], [5.1, 5.1]])
        result = task_func(data, 2)
        self.assertEqual(len(result), 2)
        self.assertTrue(isinstance(result[0], np.ndarray))
        self.assertTrue(isinstance(result[1], np.ndarray))
        result_list = [x.tolist() for x in result.values()]
        self.assertCountEqual(result_list, [[0, 1], [2, 3]])
    def test_case_2(self):
        data = np.array([[1, 2], [1, 3],[1, 4], [1, 5], [200, 1], [200, 2], [200, 3], [3000, 1], [3000, 3]])
        result = task_func(data, 3)
        self.assertEqual(len(result), 3)
        self.assertTrue(isinstance(result[0], np.ndarray))
        self.assertTrue(isinstance(result[1], np.ndarray))
        result_list = [x.tolist() for x in result.values()]
        self.assertCountEqual(result_list, [[0, 1, 2, 3], [4, 5, 6], [7, 8]])
    def test_case_3(self):
        data = np.array([[1, 2]])
        result = task_func(data, 1)
        self.assertEqual(len(result), 1)
        self.assertTrue(isinstance(result[0], np.ndarray))
        self.assertCountEqual(list(result.values()), [0])
    def test_case_4(self):
        '''wrong input'''
        self.assertRaises(Exception, task_func, [])
        self.assertRaises(Exception, task_func, 2)
        self.assertRaises(Exception, task_func, [['asv', 1]])
        self.assertRaises(Exception, task_func, {})
    def test_case_5(self):
        data = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
        result = task_func(data, 5)
        self.assertEqual(len(result), 5)
        for i in range(5):
            self.assertTrue(isinstance(result[i], np.ndarray))
        result_list = [x.tolist() for x in result.values()]
        self.assertCountEqual(result_list, [[0], [1], [2], [3], [4]])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)