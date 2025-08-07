import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    # Check if the input data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    
    # Check if the DataFrame contains a 'job' column
    if 'job' not in data.columns:
        raise ValueError("DataFrame must contain a 'job' column.")
    
    # Count the occurrences of each job
    job_counts = data['job'].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(job_counts, labels=job_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Return the Figure object
    return fig
import unittest
import matplotlib.pyplot as plt
import pandas as pd
class TestCases(unittest.TestCase):
    def test_empty_data(self):
        data = pd.DataFrame(columns=['Name', 'Date', 'Job'])
        fig = task_func(data)
        self.assertIsInstance(fig, plt.Figure)
        plt.close()
    def test_single_job(self):
        data = pd.DataFrame({'Name': ['John'], 'Date': ['01/03/2012'], 'Job': ['Engineer']})
        fig = task_func(data)
        self.assertIsInstance(fig, plt.Figure)
        # Check pie sizes
        sizes = fig.axes[0].patches
        self.assertEqual(len(sizes), 1)  # There should be only one slice
        plt.close()
    def test_multiple_jobs(self):
        data = pd.DataFrame({'Name': ['John', 'Jane'], 'Date': ['01/03/2012', '02/05/2013'], 'Job': ['Engineer', 'Doctor']})
        fig = task_func(data)
        self.assertIsInstance(fig, plt.Figure)
        # Check pie sizes
        sizes = fig.axes[0].patches
        self.assertEqual(len(sizes), 2)  # There should be two slices
        plt.close()
    def test_repeated_jobs(self):
        data = pd.DataFrame({'Name': ['John', 'Jane', 'Joe'], 'Date': ['01/03/2012', '02/05/2013', '03/08/2014'], 'Job': ['Engineer', 'Engineer', 'Lawyer']})
        fig = task_func(data)
        self.assertIsInstance(fig, plt.Figure)
        plt.close()
    def test_large_dataset(self):
        data = pd.DataFrame({'Name': ['Person' + str(i) for i in range(100)], 'Date': ['01/01/2020' for _ in range(100)], 'Job': ['Job' + str(i % 3) for i in range(100)]})
        fig = task_func(data)
        self.assertIsInstance(fig, plt.Figure)
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)