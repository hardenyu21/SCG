import random
import pandas as pd
import numpy as np

def task_func(n,
              domain="samplewebsite.com",
              categories=['Sports', 'Technology', 'Health', 'Science', 'Business'],
              random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
        np.random.seed(random_seed)
    
    titles = [f"Article {i}" for i in range(n)]
    urls = [f"{domain}/Article_{i}" for i in range(n)]
    ids = list(range(n))
    selected_categories = random.choices(categories, k=n)
    views = np.random.poisson(lam=1000, size=n)
    
    data = {
        'title': titles,
        'title_url': urls,
        'id': ids,
        'category': selected_categories,
        'views': views
    }
    
    df = pd.DataFrame(data)
    return df

# Example usage:
df = task_func(3, categories=['A', 'B'], domain='test.de', random_seed=12)
print(df)