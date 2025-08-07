import csv
import collections

def task_func(csv_file_path):
    # Initialize a dictionary to keep track of total sales per product
    sales_data = collections.defaultdict(int)
    
    # Open the CSV file and read the data
    with open(csv_file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Iterate over each row in the CSV file
        for row in reader:
            product = row['product']
            quantity = int(row['quantity'])
            
            # Update the total sales for the product
            sales_data[product] += quantity
    
    # Find the product with the highest total sales
    top_selling_product = max(sales_data.items(), key=operator.itemgetter(1))[0]
    
    return top_selling_product