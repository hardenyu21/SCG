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