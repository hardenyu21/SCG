import numpy as np
import pandas as pd

def task_func(num_teams=5, num_games=100):
    # Generate random team names
    teams = [f'Team_{i+1}' for i in range(num_teams)]
    
    # Generate random game names
    games = [f'Game_{j+1}' for j in range(num_games)]
    
    # Generate random scores for each team in each game
    scores = np.random.randint(0, 101, size=(num_teams, num_games))
    
    # Create a DataFrame with teams as index and games as columns
    df = pd.DataFrame(scores, index=teams, columns=games)
    
    return df

# Example usage
df = task_func()
print(df)