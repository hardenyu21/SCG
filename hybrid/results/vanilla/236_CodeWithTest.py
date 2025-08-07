import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def task_func(df, test_size=0.2, random_state=42):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Drop rows with duplicate 'Name' entries
    df = df.drop_duplicates(subset='Name')
    
    # Check if 'Age' and 'Score' columns are present
    if 'Age' not in df.columns or 'Score' not in df.columns:
        raise ValueError("DataFrame must contain 'Age' and 'Score' columns.")
    
    # Check if 'Category' column is present for training
    if 'Category' not in df.columns:
        raise ValueError("DataFrame must contain 'Category' column for training.")
    
    # Features and target variable
    X = df[['Age', 'Score']]
    y = df['Category']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Initialize the Random Forest Classifier
    clf = RandomForestClassifier(random_state=random_state)
    
    # Train the classifier
    clf.fit(X_train, y_train)
    
    # Make predictions
    y_pred = clf.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy
import unittest
import pandas as pd
from faker import Faker
import random
class TestCases(unittest.TestCase):
    # Helper function to generate test data
    def generate_test_data(self, num_records):
        random.seed(0)
        fake = Faker()
        data = []
        for _ in range(num_records):
            record = {
                'Name': fake.name(),
                'Age': random.randint(18, 70),
                'Score': random.randint(50, 100),
                'Category': fake.job()
            }
            data.append(record)
        return pd.DataFrame(data)
    
    def test_basic_data(self):
        data = self.generate_test_data(10)
        accuracy = task_func(data)
        self.assertIsInstance(accuracy, float)
        self.assertGreaterEqual(accuracy, 0)
        self.assertLessEqual(accuracy, 1)
    def test_more_data(self):
        data = self.generate_test_data(20)
        accuracy = task_func(data)
        self.assertEqual(accuracy, 0)
    def test_large_data(self):
        data = self.generate_test_data(100)
        accuracy = task_func(data)
        self.assertIsInstance(accuracy, float)
    def test_single_record(self):
        data = pd.DataFrame([{'Name': 'James', 'Age': 30, 'Score': 85, 'Category': 'Electronics'},
            {'Name': 'Bob', 'Age': 20, 'Score': 75, 'Category': 'Home'},
            {'Name': 'Nick', 'Age': 40, 'Score': 90, 'Category': 'Electronics'},
            {'Name': 'Amy', 'Age': 60, 'Score': 95, 'Category': 'Home'}])
        accuracy = task_func(data)
        self.assertEqual(accuracy, 0)
    def test_moderate_size_data(self):
        data = self.generate_test_data(20)
        accuracy = task_func(data)
        self.assertIsInstance(accuracy, float)
    
    def test_case_non_df(self):
        with self.assertRaises(ValueError):
            task_func("non_df")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)