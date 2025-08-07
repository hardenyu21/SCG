import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['Date', 'Value']

def task_func(df, plot=False):
    # Check for required columns
    if not all(column in df.columns for column in COLUMNS):
        raise KeyError("DataFrame must contain 'Date' and 'Value' columns.")
    
    # Convert 'Date' column to datetime and set it as the index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Split the 'Value' column into separate columns
    value_df = df['Value'].apply(pd.Series)
    
    # Scale the values using StandardScaler
    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(value_df)
    
    # Create a DataFrame with the scaled values
    scaled_df = pd.DataFrame(scaled_values, index=df.index, columns=[f'Value_{i}' for i in range(value_df.shape[1])])
    
    # Plot the scaled values if plot is True
    ax = None
    if plot:
        ax = scaled_df.plot(kind='bar', figsize=(10, 6))
        ax.set_title("Scaled Values Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Scaled Value")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    return scaled_df, ax
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_normal_case(self):
        # Normal case with valid DataFrame
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result= task_func(df)
        self.assertEqual(result.shape, (2, 4))  # Checking if the DataFrame has the correct shape
        plt.close()
    def test_varying_length_lists(self):
        # DataFrame where 'Value' contains lists of varying lengths
        df = pd.DataFrame([['2021-01-01', [8, 10]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result = task_func(df)
        self.assertEqual(result.shape, (2, 4))  # The function should handle varying lengths
        plt.close()
    def test_varying_length_list_2(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result = task_func(df)
        self.assertEqual(result.empty, False)  
        plt.close()
    def test_missing_columns(self):
        # DataFrame missing 'Value' column
        df = pd.DataFrame([['2021-01-01'], ['2021-01-02']], columns=['Date'])
        with self.assertRaises(KeyError):
            task_func(df)  # Expecting a KeyError due to missing 'Value' column
        plt.close()
    def test_empty(self):
        df = pd.DataFrame()
        with self.assertRaises(KeyError):
            task_func(df)  
        plt.close()
    def test_plot_attributes(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        _, ax = task_func(df, True)
        self.assertEqual(ax.get_title(), 'Scaled Values Over Time')
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel(), 'Scaled Value')
        plt.close()
    def test_plot_point(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result, ax = task_func(df, True)
        list_result = []
        for column in result:
            if column != "Date":
                columnSeriesObj = result[column]
                list_result.extend(columnSeriesObj.values)
        bar_heights = [rect.get_height() for rect in ax.patches]
        self.assertListEqual(bar_heights, list_result)
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)