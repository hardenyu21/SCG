import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters=2, random_state=0):
    # Extract the 2D coordinates from the data
    coordinates = np.array([(x, y) for _, x, y in data])
    
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    
    # Fit the model to the coordinates and predict the cluster labels
    labels = kmeans.fit_predict(coordinates)
    
    return labels

# Example usage
data = [('T1', 1, 1), ('T2', 1, 1.1), ('T2', 1.1, 1), ('C1', 400, 400), ('C2', 401, 401), ('B1', 35, 35)]
labels = task_func(data, n_clusters=3, random_state=42)
print(labels)
import unittest
import warnings
import numpy as np
from faker import Faker
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with a basic dataset and default parameters
        data = [('A', 1, 1), ('B', 2, 2), ('C', 300, 300), ('D', 400, 400)]
        expected_labels = np.array([0, 0, 1, 1])  # Assuming 2 clusters and certain random_state
        labels = task_func(data, random_state=1)
        np.testing.assert_array_equal(labels, expected_labels)
    def test_case_2(self):
        # Testing with different number of clusters
        data = [('A', 1, 1), ('B', 2, 2), ('C', 3, 3), ('D', 4, 4)]
        n_clusters = 4
        labels = task_func(data, n_clusters=n_clusters)
        unique_labels = np.unique(labels)
        self.assertEqual(len(unique_labels), n_clusters)
    def test_case_3(self):
        # Testing with identical points (expecting a single cluster)
        data = [('A', 1, 1), ('B', 1, 1), ('C', 1, 1), ('D', 1, 1)]
        expected_labels = np.array([0, 0, 0, 0])  # All items are in the same cluster
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            labels = task_func(data, n_clusters=2, random_state=1)
        np.testing.assert_array_equal(labels, expected_labels)
    def test_case_4(self):
        # Testing with an empty dataset (expecting an exception)
        data = []
        with self.assertRaises(ValueError):
            task_func(data)  # Should raise an exception because KMeans cannot cluster an empty dataset
    def test_case_5(self):
        # Testing with non-numeric data (expecting an exception)
        data = [('A', 'foo', 'bar'), ('B', 'baz', 'qux')]
        with self.assertRaises(ValueError):
            task_func(data)  # Should raise an exception because coordinates must be numeric
    def test_big_data(self):
        fake = Faker()
        num = 1000
        name = [fake.first_name() for _ in range(num)]
        x = [fake.random_int() for _ in range(num)]
        y = [fake.random_int() for _ in range(num)]
        data = list(zip(name, x, y))
        labels = task_func(data, n_clusters=10, random_state=12)
        unique_labels = np.unique(labels)
        self.assertEqual(len(unique_labels), 10)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)