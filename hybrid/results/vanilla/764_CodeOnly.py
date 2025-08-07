import csv
import random

def task_func(csv_file='names.csv', 
              latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
              names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
              encoding='latin-1', rng_seed=None):
    # Validate input types
    if not isinstance(csv_file, str):
        raise TypeError("csv_file must be a string.")
    if not isinstance(latin_names, list):
        raise TypeError("latin_names must be a list.")
    if not isinstance(names, list):
        raise TypeError("names must be a list.")
    
    # Set the random seed if provided
    if rng_seed is not None:
        random.seed(rng_seed)
    
    # Determine the total number of entries
    total_entries = 100
    half_entries = total_entries // 2
    
    # Generate random names and ages
    data = []
    for _ in range(half_entries):
        if latin_names:
            name = random.choice(latin_names)
        else:
            name = ''
        age = random.randint(20, 50)
        data.append([name, age])
    
    for _ in range(half_entries):
        if names:
            name = random.choice(names)
        else:
            name = ''
        age = random.randint(20, 50)
        data.append([name, age])
    
    # Write to CSV file
    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerows(data)
    
    return csv_file