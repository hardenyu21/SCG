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
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        self.students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    def test_random_reproducibility(self):
        df1, _ = task_func(self.students, 42)
        df2, _ = task_func(self.students, 42)
        pd.testing.assert_frame_equal(df1, df2)
    def test_dataframe_columns(self):
        df, _ = task_func(self.students)
        self.assertListEqual(list(df.columns), ["Student", "Score"])
    def test_scores_within_range(self):
        df, _ = task_func(self.students)
        self.assertTrue(df["Score"].between(0, 100).all())
    def test_plot_labels(self):
        _, ax = task_func(self.students)
        self.assertEqual(ax.get_ylabel(), "Score")
        self.assertEqual(ax.get_xlabel(), "Student")
    def test_different_seeds_produce_different_scores(self):
        df1, _ = task_func(self.students, 42)
        df2, _ = task_func(self.students, 43)
        self.assertFalse(df1.equals(df2))
    
    def test_dataframe_value(self):
        df, _ = task_func(self.students)                
        df_list = df.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        expect = ['Charlie,14', 'Alice,51', 'Eve,60', 'David,71', 'Bob,92']
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(df_list))
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)