from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

def task_func(X, Y, learning_rate=0.01, epochs=100):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
    
    # Construct the Sequential model
    model = Sequential()
    model.add(Dense(1, input_dim=2, activation='sigmoid'))
    
    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer=SGD(learning_rate=learning_rate), metrics=['accuracy'])
    
    # Fit the model
    history = model.fit(X_train, Y_train, epochs=epochs, verbose=0, validation_data=(X_test, Y_test))
    
    # Plot the training and validation loss
    fig, ax = plt.subplots()
    ax.plot(history.history['loss'], label='Train')
    ax.plot(history.history['val_loss'], label='Test')
    ax.set_title('Model loss')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    ax.legend()
    
    # Return the trained model and the Axes object
    return model, ax