from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties):
    # Generate random data for goals and penalties
    data = {
        'Team': TEAMS * goals,
        'Goals': [randint(0, 5) for _ in range(goals * len(TEAMS))],
        'Penalties': [randint(0, 3) for _ in range(penalties * len(TEAMS))]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Calculate penalty costs
    df['Penalty Cost'] = df['Penalties'] * PENALTY_COST
    
    # Plotting
    plt.figure(figsize=(12, 6))
    
    # Plot for Goals
    ax1 = plt.subplot(1, 2, 1)
    sns.barplot(x='Team', y='Goals', data=df, ax=ax1)
    ax1.set_title('Goals Scored by Teams')
    ax1.set_ylabel('Goals')
    
    # Plot for Penalty Costs
    ax2 = plt.subplot(1, 2, 2)
    sns.barplot(x='Team', y='Penalty Cost', data=df, ax=ax2)
    ax2.set_title('Penalty Costs by Teams')
    ax2.set_ylabel('Penalty Cost ($)')
    
    plt.tight_layout()
    
    return df, [ax1, ax2]

# Example usage
df, plots = task_func(goals=10, penalties=5)
plt.show()