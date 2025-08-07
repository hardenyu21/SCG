from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd

def task_func(data, column1, column2):
    # Check if the specified columns exist in the DataFrame
    if column1 not in data.columns or column2 not in data.columns:
        raise ValueError("The specified columns do not exist in the DataFrame.")
    
    # Extract the data for the specified columns
    x = data[column1]
    y = data[column2]
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data points')
    ax.plot(x, slope * x + intercept, color='red', label='Fitted line')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.legend()
    
    # Return the regression results and the Axes object
    return (slope, intercept, r_value, p_value, std_err), ax
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'Column1': [14, 1, 7, 10, 5],
            'Column2': [25, 22, 8, 15, 11]
        })
    def test_regression_results(self):
        result, _ = task_func(self.data, 'Column1', 'Column2')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 5)
    def test_invalid_columns(self):
        with self.assertRaises(ValueError):
            task_func(self.data, 'Invalid1', 'Column2')
    def test_plot_axes(self):
        _, ax = task_func(self.data, 'Column1', 'Column2')
        self.assertEqual(len(ax.lines), 2)  # Original data and fitted line
    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame(), 'Column1', 'Column2')
    def test_single_point_regression(self):
        single_point_data = pd.DataFrame({'Column1': [1], 'Column2': [2]})
        result, ax = task_func(single_point_data, 'Column1', 'Column2')
        # self.assertEqual(result[0], np.nan)
        self.assertEqual(result[2], 0)  # Slope should be 0 for single point
    
    def test_return_values(self):
        result, ax = task_func(self.data, 'Column1', 'Column2')
        # print(result)
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(result))
        expect = (0.3456790123456789, 13.641975308641975, 0.23699046752221187, 0.7011032163730078, 0.8181438416490141)
        for res, exp in zip(result, expect):
            self.assertAlmostEqual(res, exp, places=7)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)