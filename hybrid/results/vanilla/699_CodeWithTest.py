import pandas as pd
from sklearn.cluster import KMeans

def task_func(x_list, y_list, n_clusters=2, random_state=0):
    # Create a DataFrame from the input lists
    data = pd.DataFrame({'x': x_list, 'y': y_list})
    
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Return the labels and centroids as a tuple
    return (labels, centroids)

# Example usage:
# x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# labels, centroids = task_func(x_list, y_list, n_clusters=2)
# print("Labels:", labels)
# print("Centroids:", centroids)
import unittest
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.random_state = 0
        self.n_clusters = 2
    def test_case_1(self):
        labels, centroids = task_func([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7],
                                  self.n_clusters, self.random_state)
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
        self.assertEqual(labels[2], 0)
        self.assertEqual(labels[3], 1)
        self.assertEqual(labels[4], 1)
        self.assertEqual(labels[5], 1)
        self.assertEqual(centroids[0][0], 2.)
        self.assertEqual(centroids[0][1], 3.)
        self.assertEqual(centroids[1][0], 5.)
        self.assertEqual(centroids[1][1], 6.)
    def test_case_2(self):
        labels, centroids = task_func([1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2],
                                  self.n_clusters, self.random_state)
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
        self.assertEqual(labels[2], 0)
        self.assertEqual(labels[3], 0)
        self.assertEqual(labels[4], 0)
        self.assertEqual(labels[5], 0)
        self.assertEqual(centroids[0][0], 1.)
        self.assertEqual(centroids[0][1], 2.)
    def test_case_3(self):
        labels, centroids = task_func([1, 2, 3, 4, 5, 6], [2, 2, 2, 2, 2, 2],
                                  self.n_clusters, self.random_state)
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
        self.assertEqual(labels[2], 0)
        self.assertEqual(labels[3], 1)
        self.assertEqual(labels[4], 1)
        self.assertEqual(labels[5], 1)
        self.assertEqual(centroids[0][0], 2.)
        self.assertEqual(centroids[0][1], 2.)
        self.assertEqual(centroids[1][0], 5.)
        self.assertEqual(centroids[1][1], 2.)
    def test_case_4(self):
        labels, centroids = task_func([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                                  self.n_clusters, self.random_state)
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
    def test_case_5(self):
        labels, centroids = task_func([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
                                  self.n_clusters, self.random_state)
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
        self.assertEqual(labels[2], 0)
        self.assertEqual(labels[3], 1)
        self.assertEqual(labels[4], 1)
        self.assertEqual(labels[5], 1)
        self.assertEqual(centroids[0][0], 2.)
        self.assertEqual(centroids[0][1], 2.)
        self.assertEqual(centroids[1][0], 5.)
        self.assertEqual(centroids[1][1], 5.)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)