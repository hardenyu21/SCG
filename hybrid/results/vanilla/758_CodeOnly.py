import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
              ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    # Check if num_samples is an integer
    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer.")
    
    # Initialize the random number generator
    rng = np.random.default_rng(seed=rng_seed)
    
    # Sample countries
    sampled_countries = rng.choice(countries, size=num_samples)
    
    # Sample ages
    sampled_ages = rng.choice(ages, size=num_samples)
    
    # Encode genders
    label_encoder = LabelEncoder()
    label_encoder.fit(genders)
    encoded_genders = label_encoder.transform(rng.choice(genders, size=num_samples))
    
    # Create a DataFrame
    demographics = pd.DataFrame({
        'Country': sampled_countries,
        'Age': sampled_ages,
        'Gender': encoded_genders
    })
    
    return demographics

# Example usage
demographics = task_func(5, countries=['Austria', 'Germany'], rng_seed=3)
print(demographics)