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
import unittest
# Unit Tests
class TestCases(unittest.TestCase):
    def test_positive_outcomes(self):
        """Test the function with positive goals and penalties."""
        df, _ = task_func(5, 3, rng_seed=42)
        # Check if the DataFrame is not empty and has the correct columns
        self.assertFalse(df.empty)
        self.assertListEqual(list(df.columns), ['Team', 'Goals', 'Penalty Cost'])
    def test_zero_goals_penalties(self):
        """Test the function with zero goals and penalties."""
        df, _ = task_func(0, 0, teams=['Team A'], rng_seed=42)
        # Check that goals and penalty costs are 0
        self.assertTrue((df['Goals'] == 0).all())
        self.assertTrue((df['Penalty Cost'] == 0).all())
    def test_negative_input(self):
        """Ensure negative inputs are treated as positive."""
        df, _ = task_func(-5, -3, rng_seed=42)
        # Check for absence of negative values in results
        self.assertFalse((df['Goals'] < 0).any())
        self.assertFalse((df['Penalty Cost'] < 0).any())
    def test_single_team(self):
        """Test with a single team to ensure correct results."""
        df, _ = task_func(10, 5, teams=['Solo Team'], rng_seed=42)
        # Ensure only one row exists and contains 'Solo Team'
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Team'], 'Solo Team')
    def test_custom_penalty_cost(self):
        """Test the function with a custom penalty cost."""
        custom_cost = 500
        df, _ = task_func(5, 3, penalty_cost=custom_cost, rng_seed=42)
        # Validate that the penalty cost calculation uses the custom cost
        self.assertTrue((df['Penalty Cost'] % custom_cost == 0).all() or (df['Penalty Cost'] == 0).all())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)