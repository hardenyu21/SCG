import pandas as pd
import random

def task_func(df):
    # Define a function to determine the winner of a match
    def determine_winner(row):
        if row['score_team1'] > row['score_team2']:
            return row['team1']
        elif row['score_team2'] > row['score_team1']:
            return row['team2']
        else:
            # If scores are equal, randomly choose a winner
            return random.choice([row['team1'], row['team2']])
    
    # Apply the function to each row to determine the winner
    df['winner'] = df.apply(determine_winner, axis=1)
    
    return df

# Example usage:
# df = pd.DataFrame({
#     'team1': ['A', 'B', 'C'],
#     'team2': ['D', 'E', 'F'],
#     'score_team1': [3, 2, 1],
#     'score_team2': [2, 2, 3]
# })
# result_df = task_func(df)
# print(result_df)
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        random.seed(42)
    def test_case_1(self):
        df = pd.DataFrame({'team1': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                           'team2': ['Team B', 'Team C', 'Team D', 'Team E', 'Team A'],
                            'score1': [1, 2, 3, 4, 5],
                            'score2': [2, 3, 4, 5, 6]})
        df = task_func(df)
        self.assertTrue('winner' in df.columns)
        self.assertTrue(df['winner'].equals(pd.Series(['Team B', 'Team C', 'Team D', 'Team E', 'Team A'])))
    def test_case_2(self):
        df = pd.DataFrame({'team1': ['Team C', 'Team D', 'Team E', 'Team A', 'Team B'],
                           'team2': ['Team D', 'Team E', 'Team A', 'Team B', 'Team C'],
                           'score1': [99, 99, 99, 99, 99],
                           'score2': [99, 99, 99, 99, 99]})
        df = task_func(df)
        self.assertTrue('winner' in df.columns)
        self.assertTrue(df['winner'].equals(pd.Series(['Team C', 'Team D', 'Team A', 'Team A', 'Team B'])))
    def test_case_3(self):
        df = pd.DataFrame({'team1': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                            'team2': ['Team B', 'Team C', 'Team D', 'Team E', 'Team A'],
                             'score1': [0, 0, 0, 0, 0],
                             'score2': [0, 0, 0, 0, 0]})
        df = task_func(df)
        self.assertTrue('winner' in df.columns)
        self.assertTrue(df['winner'].equals(pd.Series(['Team A', 'Team B', 'Team D', 'Team D', 'Team E'])))
    
    def test_case_4(self):
        df = pd.DataFrame({'team1': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                            'team2': ['Team B', 'Team C', 'Team D', 'Team E', 'Team A'],
                             'score1': [10, 9, 8, 7, 6],
                             'score2': [9, 8, 7, 6, 5]})
        df = task_func(df)
        self.assertTrue('winner' in df.columns)
        self.assertTrue(df['winner'].equals(pd.Series(['Team A', 'Team B', 'Team C', 'Team D', 'Team E'])))
    
    def test_case_5(self):
        df = pd.DataFrame({'team1': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                            'team2': ['Team B', 'Team C', 'Team D', 'Team E', 'Team A'],
                             'score1': [10, 9, 8, 7, 6],
                             'score2': [11, 12, 13, 14, 15]})
        df = task_func(df)
        self.assertTrue('winner' in df.columns)
        self.assertTrue(df['winner'].equals(pd.Series(['Team B', 'Team C', 'Team D', 'Team E', 'Team A'])))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)