import pandas as pd
from random import choices, seed

def task_func(products, ratings, weights, random_seed=42):
    # Set the random seed for reproducibility
    seed(random_seed)
    
    # Generate random ratings for each product based on the provided weights
    assigned_ratings = choices(ratings, weights=weights, k=len(products))
    
    # Create a DataFrame with the products and their assigned ratings
    df = pd.DataFrame({'Product': products, 'Rating': assigned_ratings})
    
    # Sort the DataFrame by 'Rating' in descending order
    df_sorted = df.sort_values(by='Rating', ascending=False)
    
    return df_sorted

# Example usage:
products = ['Product A', 'Product B', 'Product C', 'Product D']
ratings = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.2, 0.2]

df = task_func(products, ratings, weights)
print(df)