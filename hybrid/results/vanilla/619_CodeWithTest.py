from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, rng_seed=None):
    # Set the random seed for reproducibility
    if rng_seed is not None:
        seed(rng_seed)
    
    # Initialize lists to store data
    team_data = []
    
    # Simulate match results for each team
    for team in TEAMS:
        # Randomly generate goals and penalties for each team
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        
        # Calculate penalty cost
        penalty_cost = team_penalties * PENALTY_COST
        
        # Append data to the list
        team_data.append({
            'Team': team,
            'Goals': team_goals,
            'Penalty Cost': penalty_cost
        })
    
    # Create a DataFrame from the collected data
    df = pd.DataFrame(team_data)
    
    # Prepare data for linear regression
    X = df[['Goals']]  # Features
    y = df['Penalty Cost']  # Target variable
    
    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Return the DataFrame and the trained model
    return df, model

# Example usage
df, model = task_func(goals=10, penalties=5, rng_seed=42)
print(df)
print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)
import unittest
import numpy as np
# Unit Tests
class TestCases(unittest.TestCase):
    """A set of unit tests to ensure the functionality of task_func."""
    def test_dataframe_structure(self):
        """Ensures the DataFrame has the correct structure."""
        df, _ = task_func(5, 3, rng_seed=42)
        self.assertListEqual(list(df.columns), ['Team', 'Goals', 'Penalty Cost'])
    def test_model_type(self):
        """Checks if the returned model is a LinearRegression instance."""
        _, model = task_func(5, 3, rng_seed=42)
        self.assertIsInstance(model, LinearRegression)
    def test_predictions_type(self):
        """Verifies that model predictions return a numpy array."""
        _, model = task_func(5, 3, rng_seed=42)
        predictions = model.predict(np.array([[2], [3]]))
        self.assertIsInstance(predictions, np.ndarray)
    def test_positive_goals_and_penalties(self):
        """Confirms goals and penalty costs are non-negative."""
        df, _ = task_func(5, 3, rng_seed=42)
        self.assertTrue((df['Goals'] >= 0).all())
        self.assertTrue((df['Penalty Cost'] >= 0).all())
    def test_regression_coefficients_sign(self):
        """Checks that the regression model produces a coefficient."""
        df, model = task_func(5, 3, rng_seed=42)
        self.assertIsNotNone(model.coef_[0])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)