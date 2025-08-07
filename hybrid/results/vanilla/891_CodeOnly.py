import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def task_func(csv_file_path, attribute, test_size=0.2, random_state=42):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Separate the features and the target attribute
    X = df.drop(columns=[attribute])
    y = df[attribute]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Initialize the Linear Regression model
    model = LinearRegression()
    
    # Train the model on the training data
    model.fit(X_train, y_train)
    
    # Predict the values for the test set
    predictions = model.predict(X_test)
    
    # Return the trained model and the predictions
    return model, predictions