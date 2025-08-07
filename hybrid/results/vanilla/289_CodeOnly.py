import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler

def task_func(X, y, n_splits, batch_size, epochs):
    # Initialize the KFold cross-validator
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    
    # Initialize the MinMaxScaler for feature scaling
    scaler = MinMaxScaler()
    
    # List to store the training history for each fold
    histories = []
    
    # Iterate over each fold
    for train_index, val_index in kf.split(X):
        # Split the data into training and validation sets
        X_train, X_val = X[train_index], X[val_index]
        y_train, y_val = y[train_index], y[val_index]
        
        # Scale the features
        X_train = scaler.fit_transform(X_train)
        X_val = scaler.transform(X_val)
        
        # Define the model
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(20, activation='relu', input_shape=(X_train.shape[1],)),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        
        # Compile the model
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        
        # Train the model
        history = model.fit(X_train, y_train,
                            validation_data=(X_val, y_val),
                            batch_size=batch_size,
                            epochs=epochs,
                            verbose=0)
        
        # Append the history to the list
        histories.append(history.history)
    
    return histories