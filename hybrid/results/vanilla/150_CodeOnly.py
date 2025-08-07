import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(product_dict, product_keys):
    # Initialize lists to store product data
    products = []
    quantities = []
    prices = []
    profits = []

    # Iterate over the specified product keys
    for key in product_keys:
        if key in product_dict:
            product = product_dict[key]
            products.append(key)
            quantities.append(product.get('quantity', 0))
            prices.append(product.get('price', 0))
            profits.append(product.get('profit', 0))

    # Create a DataFrame from the collected data
    df = pd.DataFrame({
        'Product': products,
        'Quantity': quantities,
        'Price': prices,
        'Profit': profits
    })

    # Calculate average price and profit
    if not df.empty:
        average_price = df['Price'].mean()
        average_profit = df['Profit'].mean()
        df['Average Price'] = average_price
        df['Average Profit'] = average_profit
    else:
        df['Average Price'] = np.nan
        df['Average Profit'] = np.nan

    # Plot a bar chart of the profit for each product
    fig, ax = plt.subplots()
    if not df.empty:
        df.plot(kind='bar', x='Product', y='Profit', ax=ax, legend=False)
        ax.set_ylabel('Profit')
        ax.set_title('Profit for Each Product')
    else:
        ax = None

    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
product_dict = {
    'ProductA': {'quantity': 10, 'price': 20, 'profit': 5},
    'ProductB': {'quantity': 15, 'price': 25, 'profit': 7},
    'ProductC': {'quantity': 20, 'price': 30, 'profit': 10}
}

product_keys = ['ProductA', 'ProductB', 'ProductC']
df, ax = task_func(product_dict, product_keys)
print(df)
plt.show()