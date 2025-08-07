import numpy as np
import pandas as pd

def task_func(country_dict):
    # Extract the country names from the dictionary keys
    countries = list(country_dict.keys())
    
    # Generate random GDP values for each country
    gdp_values = np.random.randint(1_000_000_000, 100_000_000_000, size=len(countries))
    
    # Create a DataFrame with countries as the index and GDP values as the column
    df = pd.DataFrame(data=gdp_values, index=countries, columns=['GDP'])
    
    return df

# Example usage:
country_dict = {
    'USA': 'Washington, D.C.',
    'Germany': 'Berlin',
    'Japan': 'Tokyo',
    'China': 'Beijing',
    'India': 'New Delhi'
}

df = task_func(country_dict)
print(df)