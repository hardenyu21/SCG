import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(json_data: str, data_key: str):
    try:
        # Load JSON data
        data = json.loads(json_data)
        
        # Extract numerical data using the provided key
        if data_key not in data:
            raise KeyError(f"Key '{data_key}' not found in the JSON data.")
        
        # Convert the extracted data to a pandas Series
        original_data = pd.Series(data[data_key], dtype='float64')
        
        # Check if the data is empty
        if original_data.empty:
            return original_data, None, None
        
        # Min-Max normalize the data
        scaler = MinMaxScaler()
        normalized_data = pd.Series(scaler.fit_transform(original_data.values.reshape(-1, 1)).flatten(), dtype='float64')
        
        # Create a line plot
        fig, ax = plt.subplots()
        ax.plot(original_data.index, original_data, label='Original Data', marker='o')
        ax.plot(normalized_data.index, normalized_data, label='Normalized Data', marker='x')
        
        # Set plot title and labels
        ax.set_title('Comparison of Original and Normalized Data')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        ax.legend()
        
        # Return the results
        return original_data, normalized_data, ax
    
    except KeyError as e:
        raise KeyError(str(e))
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None
import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_data_extraction(self):
        json_str = '{"data": {"values": [0.5, 10, 15, 20]}}'
        data_key = "data.values"
        original_data, _, _ = task_func(json_str, data_key)
        expected_series = pd.Series([0.5, 10, 15, 20], dtype=pd.Float64Dtype)
        pd.testing.assert_series_equal(original_data, expected_series, check_dtype=False)
    def test_data_normalization(self):
        json_str = '{"data": {"values": [0, 10, 20, 30, 40]}}'
        data_key = "data.values"
        _, normalized_data, _ = task_func(json_str, data_key)
        expected_normalized = pd.Series(
            [0.0, 0.25, 0.5, 0.75, 1.0], dtype=pd.Float64Dtype
        )
        pd.testing.assert_series_equal(normalized_data, expected_normalized, check_dtype=False)
    def test_plot_properties(self):
        json_str = '{"data": {"values": [1, 2, 3, 4, 5]}}'
        data_key = "data.values"
        _, _, ax = task_func(json_str, data_key)
        self.assertEqual(ax.get_title(), "Comparison of Original and Normalized Data")
        self.assertEqual(ax.get_xlabel(), "Index")
        self.assertEqual(ax.get_ylabel(), "Value")
        legend_texts = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertIn("Original Data", legend_texts)
        self.assertIn("Normalized Data", legend_texts)
    def test_empty_data(self):
        json_str = '{"data": {"values": []}}'
        data_key = "data.values"
        original_data, normalized_data, ax = task_func(json_str, data_key)
        self.assertTrue(original_data.empty)
        self.assertIsNone(normalized_data)
        self.assertIsNone(ax)
    def test_non_uniform_data_spacing(self):
        json_str = '{"data": {"values": [1, 1, 2, 3, 5, 8]}}'
        data_key = "data.values"
        _, normalized_data, _ = task_func(json_str, data_key)
        expected_normalized = pd.Series(
            [0.0, 0.0, 0.142857, 0.285714, 0.571429, 1.0], dtype=pd.Float64Dtype
        )
        pd.testing.assert_series_equal(normalized_data, expected_normalized, atol=1e-6, check_dtype=False)
    def test_negative_values(self):
        json_str = '{"data": {"values": [-50, -20, 0, 20, 50]}}'
        data_key = "data.values"
        _, normalized_data, _ = task_func(json_str, data_key)
        expected_normalized = pd.Series(
            [0.0, 0.3, 0.5, 0.7, 1.0], dtype=pd.Float64Dtype
        )
        pd.testing.assert_series_equal(normalized_data, expected_normalized, atol=1e-5, check_dtype=False)
    def test_nested_json_structure(self):
        json_str = '{"data": {"deep": {"deeper": {"values": [2, 4, 6, 8, 10]}}}}'
        data_key = "data.deep.deeper.values"
        original_data, _, _ = task_func(json_str, data_key)
        expected_series = pd.Series([2, 4, 6, 8, 10], dtype=pd.Float64Dtype)
        pd.testing.assert_series_equal(original_data, expected_series, check_dtype=False)
    def test_complex_json_structure(self):
        json_str = """
        {
            "metadata": {
                "source": "sensor_array",
                "timestamp": "2023-04-11"
            },
            "readings": {
                "temperature": [20, 22, 21, 23, 24],
                "humidity": [30, 32, 31, 33, 34],
                "data": {
                    "deep": {
                        "deeper": {
                            "values": [100, 200, 300, 400, 500]
                        },
                        "another_level": {
                            "info": "This should not be processed"
                        }
                    }
                }
            }
        }"""
        data_key = "readings.data.deep.deeper.values"
        original_data, normalized_data, ax = task_func(json_str, data_key)
        expected_series = pd.Series([100, 200, 300, 400, 500], dtype=pd.Float64Dtype)
        pd.testing.assert_series_equal(original_data, expected_series, check_dtype=False)
        expected_normalized = pd.Series(
            [0.0, 0.25, 0.5, 0.75, 1.0], dtype=pd.Float64Dtype
        )
        pd.testing.assert_series_equal(normalized_data, expected_normalized, atol=1e-5, check_dtype=False)
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)