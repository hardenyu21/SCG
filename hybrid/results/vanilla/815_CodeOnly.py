import pandas as pd
import numpy as np

def task_func(test_scores, student):
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(test_scores)
    
    # Check if the student is present in the DataFrame
    if student not in df['Student'].values:
        raise ValueError("student is not present in the test_scores dataframe")
    
    # Filter the DataFrame for the specific student
    student_scores = df[df['Student'] == student]['Score']
    
    # Calculate the average score and standard deviation
    average_score = student_scores.mean()
    std_deviation = student_scores.std()
    
    # Return the results as a numpy array and the DataFrame
    return np.array([average_score, std_deviation]), df

# Example usage:
# scores = {'Student': [1, 2, 1, 1], 'Score': [10, 1, 1, 1]}
# result, df = task_func(scores, 1)
# print(result)
# print(df)