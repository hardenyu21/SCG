from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd

# Constants (they can be overridden with default parameters)
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    # Set the random seed for reproducibility if provided
    if rng_seed is not None:
        seed(rng_seed)
    
    # Generate random goals and penalties for each team
    data = {
        'Team': teams,
        'Goals': [randint(0, goals) for _ in teams],
        'Penalties': [randint(0, penalties) for _ in teams]
    }
    
    # Calculate the penalty costs
    data['Penalty Cost'] = [penalties * penalty_cost for penalties in data['Penalties']]
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(kind='bar', x='Team', y=['Goals', 'Penalty Cost'], ax=ax, color=['green', 'red'])
    ax.set_title('Football Match Results')
    ax.set_ylabel('Goals and Penalty Cost ($)')
    ax.set_xlabel('Teams')
    ax.legend(['Goals', 'Penalty Cost'])
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return df, ax

# Example usage
df, ax = task_func(goals=5, penalties=3, rng_seed=42)