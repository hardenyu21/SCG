import pandas as pd
from sklearn.linear_model import LinearRegression

DATA = {
    "Area_String": ["1,000", "2,000", "3,000", "4,000", "5,000"],
    "Price": [100, 200, 300, 400, 500],
}

def task_func(area_string, data=DATA):
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)
    
    # Clean the 'Area_String' column by removing commas and converting to integer
    df['Area'] = df['Area_String'].str.replace(',', '').astype(int)
    
    # Drop the original 'Area_String' column
    df.drop(columns=['Area_String'], inplace=True)
    
    # Define the features (X) and target (y)
    X = df[['Area']]
    y = df['Price']
    
    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Convert the input area_string to an integer
    area = int(area_string.replace(',', ''))
    
    # Predict the price for the given area
    predicted_price = model.predict([[area]])
    
    # Return the predicted price as a float
    return float(predicted_price[0])

# Example usage:
# predicted_price = task_func("3,500")
# print(predicted_price)
import unittest
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_correctness(self):
        """Test correctness."""
        self.assertAlmostEqual(task_func("6,000"), 600, delta=10)
        self.assertAlmostEqual(task_func("7,000"), 700, delta=10)
    def test_input_formats(self):
        """Test input formats."""
        self.assertAlmostEqual(task_func("6,500"), 650, delta=10)
        self.assertAlmostEqual(task_func("6500"), 650, delta=10)
    def test_custom_data(self):
        """Test custom data."""
        custom_data = {
            "Area_String": ["10", "20", "30", "40", "50"],
            "Price": [1, 2, 3, 4, 5],
        }
        self.assertAlmostEqual(task_func("60", data=custom_data), 6, delta=0.1)
    def test_existing_area(self):
        """Test existing area."""
        self.assertAlmostEqual(task_func("5,000"), 500, delta=5)
    def test_large_area(self):
        """Test large area."""
        self.assertAlmostEqual(task_func("100,000"), 10000, delta=100)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)