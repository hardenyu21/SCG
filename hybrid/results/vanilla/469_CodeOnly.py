import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    # Normalize grades to be case-insensitive
    normalized_grades = [grade.strip().upper() for grade in student_grades]
    
    # Filter out grades that are not in the possible grades list
    valid_grades = [grade for grade in normalized_grades if grade in possible_grades]
    
    # Count the occurrences of each grade
    grade_counts = Counter(valid_grades)
    
    # Create a DataFrame with the grade counts
    grade_df = pd.DataFrame(list(grade_counts.items()), columns=['Grade', 'Count'])
    grade_df.set_index('Grade', inplace=True)
    
    # Plot the bar chart
    fig, ax = plt.subplots()
    grade_df.plot(kind='bar', y='Count', ax=ax, legend=False)
    ax.set_title('Grade Distribution')
    ax.set_xlabel('Grade')
    ax.set_ylabel('Number of Students')
    plt.xticks(rotation=0)
    
    # Return the DataFrame and the Axes object
    return grade_df, ax

# Example usage:
# student_grades = ["A", "b", "C", "d", "F", "A", "B", "c", "d", "E", "F", "A", "B", "C", "D", "F"]
# df, ax = task_func(student_grades)
# plt.show()