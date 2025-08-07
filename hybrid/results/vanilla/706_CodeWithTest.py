import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def task_func(data, columns, target_column):
    # Select the features and target column
    X = data[columns]
    y = data[target_column]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the Logistic Regression model
    model = LogisticRegression(max_iter=1000)
    
    # Fit the model on the training data
    model.fit(X_train, y_train)
    
    # Make predictions on the test data
    y_pred = model.predict(X_test)
    
    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = np.array([[1, 4, 0], [2, 5, 1], [3, 6, 0]])
        columns = ['A', 'B', 'C']
        self.assertEqual(task_func(data, columns, 'C'), 0.0)
    def test_case_2(self):
        data = np.array([[1, 2, 3, -10], [4, 5, 6, -10], [1, 1, 1, 0]])
        columns = ['A', 'B', 'C', 'D']
        self.assertEqual(task_func(data, columns, 'C'), 0.0)
    def test_case_3(self):
        data = np.array([
            [60, 45, 1],
            [40, 55, 1],
            [30, 71, 1],
            [20, 82, 1],
            [10, 95, 1],
            [59, 40, 0],
            [39, 60, 1],
            [29, 70, 1],
            [19, 80, 1],
            [9,  89, 1]
        ])
        columns = ['A', 'B', 'C']
        self.assertEqual(task_func(data, columns, 'C'), 1.0)
    def test_case_4(self):
        data = np.array([
            [-10, 2, 3, -10],
            [-10, 5, 6, 10],
            [-10, -2, -1, -10],
            [-10, 1, 0, -10],
            [-10, 8, 9, 10],
            [-10, -5, -4, -10]
        ])
        columns = ['A', 'B', 'C', 'D']
        self.assertEqual(task_func(data, columns, 'D'), 1.0)
    def test_case_5(self):
        data = np.array([
            [-10, 2, 3, -10, 1],
            [-10, 5, 6, 10, 1],
            [-10, -2, -1, -10, 1],
            [-10, 1, 0, -10, 1],
            [-10, 8, 9, 10, 1],
            [-10, -5, -4, -10, 1]
        ])
        columns = ['A', 'B', 'C', 'D', 'E']
        self.assertEqual(task_func(data, columns, 'D'), 1.0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)