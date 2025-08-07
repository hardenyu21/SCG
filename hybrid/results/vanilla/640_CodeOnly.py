import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]

def task_func():
    # Generate a DataFrame with random sales figures
    np.random.seed(0)  # For reproducibility
    sales_data = np.random.randint(100, 1000, size=(12, 5))
    df = pd.DataFrame(sales_data, index=MONTHS, columns=PRODUCTS)
    
    # Calculate total sales per product
    total_sales = df.sum(axis=0)
    
    # Plot total sales per product using a line plot
    plt.figure(figsize=(10, 5))
    total_sales.plot(kind='line', marker='o', color='b')
    plt.title('Total Sales per Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
    
    # Plot sales figures across products and months using a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Sales'})
    plt.title('Sales Heatmap')
    plt.xlabel('Product')
    plt.ylabel('Month')
    plt.xticks(rotation=45)
    plt.show()
    
    return df

# Call the function to generate the DataFrame and visualize the data
df = task_func()
print(df)