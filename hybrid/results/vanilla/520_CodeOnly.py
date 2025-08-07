import collections
import matplotlib.pyplot as plt

def task_func(data):
    # Check if data is empty
    if not data:
        return {}, None

    # Initialize a defaultdict to accumulate total sales
    total_sales = collections.defaultdict(int)

    # Define a list of colors for the fruits
    colors = ['red', 'yellow', 'green', 'blue', 'purple']

    # Iterate over each dictionary in the list
    for entry in data:
        for fruit, sales in entry.items():
            if sales < 0:
                raise ValueError(f"Sales quantity for {fruit} cannot be negative.")
            total_sales[fruit] += sales

    # Convert defaultdict to a regular dictionary
    total_sales = dict(total_sales)

    # Prepare data for plotting
    fruits = list(total_sales.keys())
    sales_values = list(total_sales.values())

    # Create a bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(fruits, sales_values, color=colors[:len(fruits)])

    # Set labels and title
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Total Sales')
    ax.set_title('Total Fruit Sales')

    # Return the total sales dictionary and the bar chart axes
    return total_sales, bars

# Example usage:
# data = [
#     {'apple': 10, 'banana': 5},
#     {'apple': 15, 'orange': 8},
#     {'banana': 3, 'orange': 7}
# ]
# total_sales, ax = task_func(data)
# plt.show()