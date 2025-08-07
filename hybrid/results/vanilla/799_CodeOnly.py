import pandas as pd
from random import seed, choices, sample

def task_func(L, num_dataframes=5, random_seed=None):
    if not L:
        return pd.DataFrame(), []

    if random_seed is not None:
        seed(random_seed)

    column_names = [chr(i) for i in range(97, 123)]  # Lowercase English letters
    df_list = []

    for _ in range(num_dataframes):
        # Randomly choose 3 rows from L
        sampled_rows = sample(L, min(3, len(L)))
        # Randomly choose 3 column names
        columns = choices(column_names, k=3)
        # Create a DataFrame with the sampled rows and columns
        df = pd.DataFrame(sampled_rows, columns=columns)
        df_list.append(df)

    # Find the common rows between all DataFrames
    common_rows = df_list[0]
    for df in df_list[1:]:
        common_rows = pd.merge(common_rows, df, how='inner')

    return common_rows, df_list

# Example usage
L = [[1, '65', 76], [2, '5', 6]]
common_rows, df_list = task_func(L, num_dataframes=1, random_seed=1)
print(common_rows)
print(df_list)