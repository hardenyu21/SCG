import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

def task_func(num_samples=100, n_estimators=100, random_seed=None, cv=5):
    # Check if the condition num_samples / cv < 2 is met
    if num_samples / cv < 2:
        raise ValueError("num_samples / cv must be at least 2.")
    
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate the dataset
    X = np.random.randn(num_samples, 5)  # 5 features
    noise = np.random.randn(num_samples)
    y = np.sum(X, axis=1) + noise  # Target variable
    
    # Initialize the RandomForestRegressor model
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_seed)
    
    # Perform cross-validation
    scores = cross_val_score(model, X, y, cv=cv, scoring='r2')
    
    # Calculate the mean cross-validation score
    mean_score = np.mean(scores)
    
    # Return the mean score and the trained model
    return mean_score, model

# Example usage
results = task_func(random_seed=1)
print(results)