import pandas as pd
import random

def task_func(
    n, 
    countries=['USA', 'UK', 'China', 'India', 'Germany'], 
    products=['Product A', 'Product B', 'Product C', 'Product D', 'Product E'], 
    output_path=None,
    random_seed=None):
    
    # Set the random seed for reproducibility if provided
    if random_seed is not None:
        random.seed(random_seed)
    
    # Generate random sales data
    data = {
        'Country': [random.choice(countries) for _ in range(n)],
        'Product': [random.choice(products) for _ in range(n)],
        'Sales': [random.randint(1, 100) for _ in range(n)]
    }
    
    # Create a DataFrame from the generated data
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file if an output path is provided
    if output_path:
        df.to_csv(output_path, index=False)
    
    # Return the DataFrame
    return df

# Example usage
df = task_func(7, products=['tea', 'coffee'], countries=['Austria', 'Australia'], random_seed=12)
print(df)