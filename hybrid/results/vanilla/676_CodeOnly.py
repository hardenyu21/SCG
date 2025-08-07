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