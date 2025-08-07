import numpy as np
import matplotlib.pyplot as plt

# Constants
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']

def task_func(city_dict, max_range=1000000, seed=0):
    # Seed the random number generator
    np.random.seed(seed)
    
    # Initialize the dictionary for city populations
    city_populations = {}
    
    # Generate random populations for cities in the CITIES list
    for city in CITIES:
        if city in city_dict.values():
            city_populations[city] = np.random.randint(1, max_range + 1)
        else:
            city_populations[city] = -1
    
    # Plot the population data
    fig, ax = plt.subplots()
    ax.bar(city_populations.keys(), city_populations.values(), color='skyblue')
    ax.set_xlabel('City')
    ax.set_ylabel('Population')
    ax.set_title('City Populations')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Return the dictionary and the Axes object
    return city_populations, ax

# Example usage:
# city_dict = {'Alice': 'New York', 'Bob': 'Tokyo', 'Charlie': 'Paris'}
# populations, ax = task_func(city_dict)
# plt.show()