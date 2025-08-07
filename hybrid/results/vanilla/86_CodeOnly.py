import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(students=["Alice", "Bob", "Charlie", "David", "Eve"], seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random scores for each student
    scores = np.random.randint(0, 100, size=len(students))
    
    # Create a DataFrame with students and their scores
    df = pd.DataFrame({'Student': students, 'Score': scores})
    
    # Sort the DataFrame by scores in ascending order
    df_sorted = df.sort_values(by='Score')
    
    # Plot the scores as a bar plot
    fig, ax = plt.subplots()
    ax.bar(df_sorted['Student'], df_sorted['Score'], color='skyblue')
    ax.set_xlabel('Student')
    ax.set_ylabel('Score')
    ax.set_title('Student Scores')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the sorted DataFrame and the Axes object
    return df_sorted, ax

# Example usage
df_sorted, ax = task_func()
print(df_sorted)
plt.show()