import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

def task_func(feature: pd.Series, target: pd.Series) -> (np.ndarray, plt.Axes):
    # Reshape the feature to be 2D for the model
    X = feature.values.reshape(-1, 1)
    y = target.values
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Predict the target for the test set
    y_pred = model.predict(X_test)
    
    # Compute the confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    
    # Plot the confusion matrix
    fig, ax = plt.subplots()
    cax = ax.matshow(cm, cmap=plt.cm.Blues)
    fig.colorbar(cax)
    
    # Set labels for the confusion matrix
    ax.set_xticklabels([''] + target.unique().tolist())
    ax.set_yticklabels([''] + target.unique().tolist())
    
    # Rotate the tick labels and set alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    
    # Loop over data dimensions and create text annotations
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > cm.max() / 2. else "black")
    
    # Set title and labels
    ax.set_title('Confusion Matrix')
    ax.set_xlabel('Predicted label')
    ax.set_ylabel('True label')
    
    # Return the confusion matrix and the Axes object
    return cm, ax
import unittest
import pandas as pd
import numpy as np
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    """Test cases for the function task_func."""
    def test_with_random_data(self):
        """
        Test the function with random data to ensure normal functionality.
        """
        np.random.seed(42)
        feature = pd.Series(np.random.rand(100))
        np.random.seed(42)
        target = pd.Series(np.random.randint(0, 2, size=100))
        cm, ax = task_func(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)
    def test_with_all_zeroes(self):
        """
        Test the function with all zeroes in the feature set.
        """
        feature = pd.Series(np.zeros(100))
        np.random.seed(123)
        target = pd.Series(np.random.randint(0, 2, size=100))
        cm, ax = task_func(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)
    def test_with_all_ones(self):
        """
        Test the function with all ones in the feature set.
        """
        feature = pd.Series(np.ones(100))
        np.random.seed(42)
        target = pd.Series(np.random.randint(0, 2, size=100))
        cm, ax = task_func(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)
    def test_with_perfect_correlation(self):
        """
        Test the function when the feature perfectly predicts the target.
        """
        np.random.seed(123)
        feature = pd.Series(np.random.rand(100))
        target = feature.round()
        cm, ax = task_func(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)
    def test_with_no_correlation(self):
        """
        Test the function when there is no correlation between feature and target.
        """
        np.random.seed(42)
        feature = pd.Series(np.random.rand(100))
        np.random.seed(42)
        target = pd.Series(np.random.choice([0, 1], size=100))
        cm, ax = task_func(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)
    def tearDown(self):
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)