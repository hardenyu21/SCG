import pandas as pd
import collections

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame.")
    
    # Remove duplicate customer names
    df_unique_customers = df.drop_duplicates(subset='Customer Name')
    
    # Calculate total sales
    total_sales = df_unique_customers['Sales'].sum()
    
    # Find the most popular sales category
    category_counts = collections.Counter(df_unique_customers['Category'])
    most_common_categories = category_counts.most_common()
    
    # In case of a tie, select the first category in alphabetical order
    max_count = most_common_categories[0][1]
    most_popular_categories = [category for category, count in most_common_categories if count == max_count]
    most_popular_category = sorted(most_popular_categories)[0]
    
    # Create the report dictionary
    report = {
        'Total Sales': total_sales,
        'Most Popular Category': most_popular_category
    }
    
    return report