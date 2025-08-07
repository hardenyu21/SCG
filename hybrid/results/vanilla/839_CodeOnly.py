import csv
import random
import string

def task_func(file_path,
              num_rows,
              gender=['Male', 'Female', 'Non-Binary'],
              countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
              seed=None):
    # Set the random seed for reproducibility
    if seed is not None:
        random.seed(seed)
    
    # Define the headers for the CSV file
    headers = ['Name', 'Age', 'Gender', 'Country']
    
    # Generate random data
    data = []
    for _ in range(num_rows):
        name = ''.join(random.choices(string.ascii_uppercase, k=5))
        age = random.randint(20, 60)
        selected_gender = random.choice(gender)
        selected_country = random.choice(countries)
        data.append([name, age, selected_gender, selected_country])
    
    # Write the data to a CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    
    # Return the file path
    return file_path

# Example usage
# print(task_func('/test.csv', 100, gender=['test'], countries=['Albania', 'Germany', 'Austria'], seed=12))