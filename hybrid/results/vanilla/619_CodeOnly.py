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