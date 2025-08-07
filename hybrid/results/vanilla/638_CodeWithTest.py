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
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = task_func()
        self.assertEqual(df.shape, (5, 100))
    def test_case_2(self):
        df = task_func(num_teams=3, num_games=10)
        self.assertEqual(df.shape, (3, 10))
        
    def test_case_3(self):
        df = task_func(num_teams=4, num_games=20)
        self.assertListEqual(list(df.index), ['Team1', 'Team2', 'Team3', 'Team4'])
        
    def test_case_4(self):
        df = task_func(num_teams=2, num_games=5)
        self.assertListEqual(list(df.columns), ['Game1', 'Game2', 'Game3', 'Game4', 'Game5'])
        
    def test_case_5(self):
        df = task_func(num_teams=2, num_games=5)
        self.assertTrue((df.dtypes == 'int64').all())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)