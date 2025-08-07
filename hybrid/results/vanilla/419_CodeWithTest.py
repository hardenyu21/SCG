from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Determine the input dimension based on the first feature set of X
    input_dim = X_train.shape[1]

    # Construct a Keras Sequential model
    model = keras.Sequential([
        keras.layers.Dense(1, input_dim=input_dim, activation='sigmoid')
    ])

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='sgd')

    # Fit the model to the training data
    model.fit(X_train, Y_train, epochs=100, verbose=0)

    # Predict probabilities for the test set
    Y_pred_prob = model.predict(X_test).ravel()

    # Calculate precision and recall
    precision, recall, _ = precision_recall_curve(Y_test, Y_pred_prob)

    # Plot the Precision-Recall curve
    fig, ax = plt.subplots()
    ax.plot(recall, precision, marker='.')
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.set_title('Precision-Recall Curve')

    # Return the trained model and the Axes object
    return model, ax
import unittest
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    def setUp(self):
        # Initialize common test data used in multiple test cases.
        self.X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        self.Y = np.array([0, 1, 1, 0])
    def test_model_and_axes_types(self):
        # Verify if the returned objects include a Keras Sequential model and a matplotlib Axes.
        model, ax = task_func(self.X, self.Y)
        self.assertIsInstance(model, Sequential, "The function should return a Sequential model.")
        self.assertIsInstance(ax, Axes, "The function should return a matplotlib Axes object.")
    def test_model_output_shape(self):
        # Ensure the model's output shape is correct based on the input data.
        model, _ = task_func(self.X, self.Y)
        self.assertEqual(model.output_shape, (None, 1), "The model's output shape should have one dimension for binary classification.")
    def test_model_loss(self):
        # Confirm that the model uses binary cross-entropy as its loss function.
        model, _ = task_func(self.X, self.Y)
        self.assertEqual(model.loss, 'binary_crossentropy', "Binary cross-entropy should be the loss function for the model.")
    def test_model_optimizer(self):
        # Check if the model's optimizer is an instance of SGD.
        model, _ = task_func(self.X, self.Y)
        self.assertIsNotNone(model.optimizer)
        self.assertIsInstance(model.optimizer, SGD, "The optimizer for the model should be SGD.")
    def test_input_dimension_flexibility(self):
        # Test the model's ability to handle inputs with varying feature dimensions.
        X_varied = np.array([[0], [1], [2], [3]])
        Y_varied = np.array([0, 1, 0, 1])
        model, _ = task_func(X_varied, Y_varied)
        self.assertEqual(model.input_shape[1], X_varied.shape[1], "The model should dynamically adapt to the input feature size.")
    def test_axes_labels_and_title(self):
        # Test if the Axes object has the correct title and labels as specified.
        _, ax = task_func(self.X, self.Y)
        self.assertEqual(ax.get_title(), 'Precision-Recall Curve', "The plot's title should be 'Precision-Recall Curve'.")
        self.assertEqual(ax.get_xlabel(), 'Recall', "The plot's x-axis label should be 'Recall'.")
        self.assertEqual(ax.get_ylabel(), 'Precision', "The plot's y-axis label should be 'Precision'.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)