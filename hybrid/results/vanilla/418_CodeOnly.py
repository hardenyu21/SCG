from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Create a Keras Sequential model
    model = keras.models.Sequential([
        keras.layers.Dense(1, activation='sigmoid', input_shape=(X_train.shape[1],))
    ])

    # Compile the model
    model.compile(optimizer=keras.optimizers.SGD(learning_rate=0.01),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # Fit the model to the training data
    model.fit(X_train, Y_train, epochs=100, verbose=0)

    # Predict probabilities on the test set
    Y_pred_prob = model.predict(X_test).ravel()

    # Compute ROC curve and AUC
    fpr, tpr, _ = roc_curve(Y_test, Y_pred_prob)
    roc_auc = auc(fpr, tpr)

    # Plot the ROC curve
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
    ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False positive rate')
    ax.set_ylabel('True positive rate')
    ax.set_title('ROC curve')
    ax.legend(loc="lower right")

    # Return the trained model and the Axes object
    return model, ax