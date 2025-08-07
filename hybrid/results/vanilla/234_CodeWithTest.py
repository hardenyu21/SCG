import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Drop rows with duplicate names
    df_unique = df.drop_duplicates(subset='name')
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(df_unique['age'], df_unique['score'])
    
    # Create the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df_unique['age'], df_unique['score'], label='Data points')
    
    # Plot the regression line
    regression_line = slope * df_unique['age'] + intercept
    ax.plot(df_unique['age'], regression_line, color='red', label='Regression line')
    
    # Set the title and labels
    ax.set_title('Linear Regression')
    ax.set_xlabel('Age')
    ax.set_ylabel('Score')
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the plot and axes objects
    return plt, ax
import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_correct_data_handling(self):
        data = pd.DataFrame([
            {'Name': 'Alice', 'Age': 25, 'Score': 80},
            {'Name': 'Bob', 'Age': 30, 'Score': 85},
            {'Name': 'Alice', 'Age': 25, 'Score': 80},
            {'Name': 'Eve', 'Age': 35, 'Score': 90}
        ])
        plt, ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 1)  # Only one line for the regression
        self.assertEqual(len(ax.collections), 1)  # Only one collection for scatter plot
    def test_linear_regression(self):
        data = pd.DataFrame([
            {'Name': 'Alice', 'Age': 20, 'Score': 70},
            {'Name': 'Bob', 'Age': 25, 'Score': 75},
            {'Name': 'Eve', 'Age': 30, 'Score': 80}
        ])
        plt, ax = task_func(data)
        line = ax.lines[0]
        x_data, y_data = line.get_xdata(), line.get_ydata()
        self.assertTrue((y_data[1] - y_data[0]) / (x_data[1] - x_data[0]) > 0)  # Positive slope
    def test_plotting_elements(self):
        data = pd.DataFrame([
            {'Name': 'Alice', 'Age': 20, 'Score': 70},
            {'Name': 'Bob', 'Age': 25, 'Score': 75}
        ])
        plt, ax= task_func(data)
        self.assertEqual(ax.get_xlabel(), 'Age')
        self.assertEqual(ax.get_ylabel(), 'Score')
        self.assertEqual(ax.get_title(), 'Linear Regression')
    def test_empty_dataframe(self):
        data = pd.DataFrame([
            {'Name': 'Alice', 'Age': 20, 'Score': 70},
            {'Name': 'Bob', 'Age': 25, 'Score': 75}
        ])
        plt, ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 1)  # No line for regression
        self.assertGreater(len(ax.collections), 0)
    def test_missing_columns(self):
        data = pd.DataFrame([
            {'Name': 'Alice', 'Age': 20},
            {'Name': 'Bob', 'Age': 25}
        ])
        with self.assertRaises(KeyError):
            task_func(data)
    
    def test_non_df(self):
        with self.assertRaises(ValueError):
            task_func("non_df")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)