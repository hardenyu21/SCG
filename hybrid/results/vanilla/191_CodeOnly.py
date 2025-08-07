import random
from scipy import stats

def task_func(animals, mean):
    # Determine the number of customers using a Poisson distribution
    num_customers = stats.poisson.rvs(mu=mean)
    
    # Initialize a dictionary to keep track of sales
    sales_summary = {animal: 0 for animal in animals}
    
    # Simulate each customer's purchase
    for _ in range(num_customers):
        # Randomly choose an animal for the customer to buy
        chosen_animal = random.choice(animals)
        # Increment the count for the chosen animal
        sales_summary[chosen_animal] += 1
    
    # Display the sales summary
    print("Sales Summary:")
    for animal, count in sales_summary.items():
        print(f"{animal}: {count} sales")
    
    # Return the sales summary dictionary
    return sales_summary

# Example usage:
animals = ['dog', 'cat', 'bird', 'fish']
mean_customers = 10
sales = task_func(animals, mean_customers)