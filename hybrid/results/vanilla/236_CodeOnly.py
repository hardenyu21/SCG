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