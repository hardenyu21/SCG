import pandas as pd
import numpy as np

def task_func(fruit_data):
    if not fruit_data:
        return pd.DataFrame(columns=['Total Count', 'Average Count'])

    # Create a dictionary to store total and count for each fruit
    fruit_totals = {}

    for fruit, count in fruit_data:
        if fruit in fruit_totals:
            fruit_totals[fruit]['total'] += count
            fruit_totals[fruit]['count'] += 1
        else:
            fruit_totals[fruit] = {'total': count, 'count': 1}

    # Calculate total and average counts
    data = {
        'Total Count': [],
        'Average Count': []
    }
    for fruit, values in fruit_totals.items():
        total_count = values['total']
        average_count = total_count / values['count']
        data['Total Count'].append(total_count)
        data['Average Count'].append(average_count)

    # Create a DataFrame
    df = pd.DataFrame(data, index=fruit_totals.keys())
    return df