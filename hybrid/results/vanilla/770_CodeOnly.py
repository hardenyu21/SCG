import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate a single feature dataset
    X = np.random.rand(num_samples, 1)
    
    # Define a linear relation with some true parameters
    true_slope = 2.5
    true_intercept = 1.0
    
    # Compute the target variable with added Gaussian noise
    y = true_slope * X + true_intercept + noise_strength * np.random.randn(num_samples, 1)
    
    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_seed)
    
    # Check if the test set size is smaller than 2
    if len(X_test) < 2:
        raise ValueError("Test set size is smaller than 2.")
    
    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Calculate the R-squared score on the test set
    r_squared = model.score(X_test, y_test)
    
    # Return the R-squared score and the trained model
    return r_squared, model