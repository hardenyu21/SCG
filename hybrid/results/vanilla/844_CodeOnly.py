import csv
import random
from faker import Faker

def task_func(file_path, num_rows, random_seed=None):
    # Validate num_rows
    if not isinstance(num_rows, int) or num_rows < 0:
        raise ValueError("num_rows must be an integer >= 0.")
    
    # Initialize Faker
    fake = Faker()
    if random_seed is not None:
        Faker.seed(random_seed)
        random.seed(random_seed)
    
    # Prepare data
    data = []
    for _ in range(num_rows):
        name = fake.name()
        age = random.randint(20, 60)
        address = fake.address().replace('\n', ', ')
        email = fake.email()
        data.append([name, str(age), address, email])
    
    # Write to CSV
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age', 'Address', 'Email'])
        writer.writerows(data)
    
    return file_path