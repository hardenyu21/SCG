import math
from random import randint
import pandas as pd

def task_func(cities_list):
    # Generate random population data for each city
    population_data = []
    for city in cities_list:
        # Generate a random population between 10,000 and 1,000,000
        random_population = randint(10, 1000) * 1000
        # Round up to the next thousand
        rounded_population = math.ceil(random_population / 1000) * 1000
        population_data.append({'City': city, 'Population': rounded_population})
    
    # Create a DataFrame from the population data
    df = pd.DataFrame(population_data)
    
    return df

# Example usage:
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
df = task_func(cities)
print(df)