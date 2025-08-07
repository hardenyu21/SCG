import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(goals, penalties):
    # Create a DataFrame from the input data
    data = {
        'Team': list(goals.keys()),
        'Goals': list(goals.values()),
        'Penalties': list(penalties.values())
    }
    df = pd.DataFrame(data)
    
    # Create a pairplot using seaborn
    pairplot = sns.pairplot(df, vars=['Goals', 'Penalties'], hue='Team', diag_kind='kde')
    
    # Return the DataFrame and the Axes object
    return df, pairplot

# Example usage:
goals = {
    'Team A': 20,
    'Team B': 15,
    'Team C': 18,
    'Team D': 25
}

penalties = {
    'Team A': 5,
    'Team B': 3,
    'Team C': 4,
    'Team D': 6
}

df, pairplot = task_func(goals, penalties)
plt.show()