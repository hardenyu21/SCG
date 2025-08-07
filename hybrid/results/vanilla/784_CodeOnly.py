import pandas as pd
import random
import csv

def task_func(n, 
              categories=['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'],
              news_sites=['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'],
              likert_scale=['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'],
              file_path='news_survey_data.csv',
              random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        random.seed(random_seed)
    
    # Generate random survey data
    data = []
    for _ in range(n):
        site = random.choice(news_sites)
        category = random.choice(categories)
        response = random.choice(likert_scale)
        value = likert_scale.index(response) + 1  # Assign numerical value starting from 1
        data.append([site, category, response, value])
    
    # Write the data to a CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Site', 'Category', 'Response', 'Value'])
        writer.writerows(data)
    
    # Read the data back into a Pandas DataFrame
    df = pd.read_csv(file_path)
    
    return df

# Example usage
df = task_func(8, ['test', 'fun'], likert_scale=['true', 'false'], news_sites=['cat', 'dog'], random_seed=12)
print(df)