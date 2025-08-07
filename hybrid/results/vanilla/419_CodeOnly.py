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