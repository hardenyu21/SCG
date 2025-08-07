import pandas as pd
import numpy as np
import codecs
import re
import datetime

def task_func(start_year=1980, end_year=2000, email_domain='example.com',
              latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
              other_names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], 
              rng_seed=None):
    # Set the random seed for reproducibility
    if rng_seed is not None:
        np.random.seed(rng_seed)
    
    # Combine names and shuffle them
    all_names = latin_names + other_names
    np.random.shuffle(all_names)
    
    # Generate random dates of birth
    dates_of_birth = pd.date_range(start=f'{start_year}-01-01', end=f'{end_year}-12-31', freq='D')
    np.random.shuffle(dates_of_birth)
    
    # Create a DataFrame
    data = {
        'ID': np.arange(1, 101),
        'Name': all_names[:100],
        'Date of Birth': dates_of_birth[:100]
    }
    
    # Function to clean and encode names
    def clean_name(name):
        # Replace accented characters with their non-accented counterparts
        name = re.sub(r'[áéíóúÁÉÍÓÚ]', lambda m: {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                                                  'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}[m.group(0)], name)
        return name
    
    # Clean names
    data['Name'] = data['Name'].apply(clean_name)
    
    # Generate emails
    data['Email'] = data.apply(lambda row: f"{row['Name'].lower()}{row['Date of Birth'].year}@{email_domain}", axis=1)
    
    # Create the DataFrame
    df = pd.DataFrame(data)
    
    return df

# Example usage
df = task_func(start_year=0, end_year=1200, email_domain='test.at', rng_seed=3)
print(df)