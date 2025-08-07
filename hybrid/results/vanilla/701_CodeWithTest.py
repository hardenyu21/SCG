import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def task_func(df, target):
    # Separate the features and the target variable
    X = df.drop(columns=[target])
    y = df[target]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the Linear Regression model
    model = LinearRegression()
    
    # Fit the model on the training data
    model.fit(X_train, y_train)
    
    # Predict on the test data
    y_pred = model.predict(X_test)
    
    # Calculate the R-squared score
    score = r2_score(y_test, y_pred)
    
    return score
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]], columns = ['x', 'y', 'z'])
        r_squared = task_func(df, 'z')
        self.assertEqual(r_squared, 1.0)
        
    def test_case_2(self):
        df = pd.DataFrame([[-1, 1, 2], [3, 4, 5], [6, 7, 8]], columns = ['x', 'y', 'z'])
        r_squared = task_func(df, 'z')
        self.assertEqual(r_squared, 1.0)
    
    def test_case_3(self):
        df = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]], columns = ['x', 'y', 'z'])
        r_squared = task_func(df, 'z')
        self.assertEqual(r_squared, 1.0)
    def test_case_4(self):
        df = pd.DataFrame([[0, 0, 9], [1, 1, 35], [2, 2, 78]], columns = ['x', 'y', 'z'])
        r_squared = task_func(df, 'z')
        self.assertFalse(r_squared == 1.0)
    def test_case_5(self):
        df = pd.DataFrame([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]], columns = ['x', 'y', 'z', 'w'])
        r_squared = task_func(df, 'w')
        self.assertEqual(r_squared, 1.0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)