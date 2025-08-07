import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    # Create a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate a synthetic sales time-series
    np.random.seed(0)  # For reproducibility
    trend = np.linspace(100, 500, periods)  # Linear trend
    seasonal = np.sin(np.linspace(0, 2 * np.pi, periods)) * 50  # Seasonal component
    noise = np.random.normal(0, 10, periods)  # Random noise
    
    if model == 'additive':
        sales = trend + seasonal + noise
    elif model == 'multiplicative':
        sales = trend * (1 + seasonal / 100) * (1 + noise / 100)
    else:
        raise ValueError("Model must be either 'additive' or 'multiplicative'")
    
    # Create a DataFrame
    sales_series = pd.Series(sales, index=date_range)
    
    # Decompose the time-series
    decomposition = seasonal_decompose(sales_series, model=model, period=12)
    
    # Extract components
    trend_component = decomposition.trend
    seasonal_component = decomposition.seasonal
    residual_component = decomposition.resid
    
    # Return the components as a dictionary
    return {
        'trend': trend_component,
        'seasonal': seasonal_component,
        'residual': residual_component
    }

# Example usage
result = task_func('2020-01-01', 24, 'M', 'multiplicative')
print(len(result['seasonal']))  # Should output 24
import unittest
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        np.random.seed(42)  # For reproducibility
        result = task_func(periods=24)  # Adjust to meet the minimum requirement for decomposition
        self.assertTrue(all(key in result for key in ['trend', 'seasonal', 'residual']))
    def test_multiplicative_model(self):
        np.random.seed(0)  # For reproducibility
        result = task_func('2020-01-01', 24, 'M', 'multiplicative')
        self.assertTrue(all(key in result for key in ['trend', 'seasonal', 'residual']))
    def test_custom_parameters(self):
        np.random.seed(55)  # For reproducibility
        result = task_func('2017-01-01', 36, 'M')
        self.assertEqual(len(result['trend']), 36)
    def test_weekly_frequency(self):
        np.random.seed(1)  # For reproducibility
        result = task_func('2022-01-01', 104, 'W', 'additive')
        self.assertTrue(all(key in result for key in ['trend', 'seasonal', 'residual']))
        self.assertEqual(len(result['seasonal']), 104)
        
    def test_insufficient_periods_error(self):
        np.random.seed(66)  # For reproducibility
        result = task_func('2022-01-01', 12, 'M')
        self.assertIn('error', result)
        
    def test_additive_decomposition_properties(self):
        np.random.seed(42)  # For reproducibility
        periods = 36
        result = task_func('2020-01-01', periods, 'M')
        reconstructed = result['trend'].fillna(0) + result['seasonal'].fillna(0) + result['residual'].fillna(0)
        self.assertTrue(np.allclose(reconstructed.head(12), reconstructed.head(12), atol=1))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)