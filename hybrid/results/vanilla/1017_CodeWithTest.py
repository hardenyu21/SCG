import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def task_func(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    # Load the CSV file into a DataFrame
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        raise ValueError(f"Error reading the CSV file: {e}")

    # Check if the target column exists in the DataFrame
    if target_column not in df.columns:
        raise ValueError(f"The specified target column '{target_column}' is not found in the CSV file.")

    # Separate the features and the target variable
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Initialize the Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)

    # Train the classifier
    clf.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = clf.predict(X_test)

    # Generate the classification report
    report = classification_report(y_test, y_pred)

    return report
import unittest
from unittest.mock import patch
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for task_func."""
    @patch("pandas.read_csv")
    def test_default_parameters(self, mock_read_csv):
        """
        Test task_func with default parameters using an adequately sized mock dataset.
        """
        mock_data = {
            "feature1": range(100),
            "feature2": range(100, 200),
            "target": [0, 1] * 50,  # Alternating 0s and 1s
        }
        mock_read_csv.return_value = pd.DataFrame(mock_data)
        result = task_func("dummy_path.csv")
        self.assertIn("precision", result)
    @patch("pandas.read_csv")
    def test_non_default_target_column(self, mock_read_csv):
        """
        Test task_func with a non-default target column using a larger mock dataset.
        """
        mock_data = {
            "feature1": range(100),
            "feature2": range(100, 200),
            "label": [1, 0] * 50,  # Alternating 1s and 0s
        }
        mock_read_csv.return_value = pd.DataFrame(mock_data)
        result = task_func("dummy_path.csv", target_column="label")
        self.assertIn("precision", result)
    @patch("pandas.read_csv")
    def test_different_test_size(self, mock_read_csv):
        """
        Test task_func with a different test size and a larger dataset.
        """
        mock_data = {
            "feature1": range(100),
            "feature2": range(100, 200),
            "target": [0, 1, 1, 0] * 25,  # Repeated pattern
        }
        mock_read_csv.return_value = pd.DataFrame(mock_data)
        result = task_func("dummy_path.csv", test_size=0.5)
        self.assertIn("precision", result)
    @patch("pandas.read_csv")
    def test_different_n_estimators(self, mock_read_csv):
        """
        Test task_func with a different number of estimators and an expanded dataset.
        """
        mock_data = {
            "feature1": range(100),
            "feature2": range(100, 200),
            "target": [1, 0] * 50,  # Alternating 1s and 0s
        }
        mock_read_csv.return_value = pd.DataFrame(mock_data)
        result = task_func("dummy_path.csv", n_estimators=50)
        self.assertIn("precision", result)
    @patch("pandas.read_csv")
    def test_missing_target_column(self, mock_read_csv):
        """
        Test task_func with a missing target column.
        """
        mock_read_csv.return_value = pd.DataFrame(
            {"feature1": [1, 2], "feature2": [3, 4]}
        )
        with self.assertRaises(ValueError):
            task_func("dummy_path.csv", target_column="not_exist")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)