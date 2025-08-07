import os
import csv
import random
from statistics import mean

# Constants
COLUMNS = ['Name', 'Age', 'Height', 'Weight']
PEOPLE_COUNT = 100

def task_func(filename):
    # Generate simulated data
    data = []
    for _ in range(PEOPLE_COUNT):
        name = f"Person_{random.randint(1, 1000)}"
        age = random.randint(18, 80)
        height = round(random.uniform(150, 200), 2)  # in cm
        weight = round(random.uniform(50, 150), 2)  # in kg
        data.append([name, age, height, weight])

    # Calculate averages
    ages = [person[1] for person in data]
    heights = [person[2] for person in data]
    weights = [person[3] for person in data]
    average_age = mean(ages)
    average_height = mean(heights)
    average_weight = mean(weights)

    # Append averages to data
    data.append(['Average', average_age, average_height, average_weight])

    # Write data to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(COLUMNS)
        writer.writerows(data)

    # Return the path of the created CSV file
    return os.path.abspath(filename)

# Example usage
# print(task_func('simulated_data.csv'))