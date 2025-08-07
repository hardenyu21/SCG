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
import unittest
class TestCases(unittest.TestCase):
    def test_rng(self):
        'test rng reproducability'
        df1 = task_func(300, random_seed=42)
        df2 = task_func(300, random_seed=42)
        self.assertTrue(pd.testing.assert_frame_equal(df1, df2) is None)
    
    def test_case_1(self):
        'default params'
        df = task_func(400, random_seed=10)
        self.assertEqual(len(df), 400)
        self.assertTrue(df['title_url'].str.startswith("samplewebsite.com/Article_").all())
        self.assertEqual(len(df['id'].unique()), 400)
        self.assertTrue(df['category'].isin(['Sports', 'Technology', 'Health', 'Science', 'Business']).all())
        self.assertTrue(df['views'].dtype, int)
    def test_case_2(self):
        'custom params'
        df = task_func(330, domain="testdomain.com", categories=['A', 'B', 'C'])
        self.assertEqual(len(df), 330)
        self.assertTrue(df['title_url'].str.startswith("testdomain.com/Article_").all())
        self.assertEqual(len(df['id'].unique()), 330)
        self.assertTrue(df['category'].isin(['A', 'B', 'C']).all())
        self.assertTrue(df['views'].dtype, int)
    def test_case_3(self):
        '0 articles'
        df = task_func(0)
        self.assertEqual(len(df), 0)
    def test_case_4(self):
        df = task_func(1000, random_seed=1)
        self.assertEqual(len(df), 1000)
        self.assertEqual(len(df['id'].unique()), 1000)
        self.assertTrue(df['views'].dtype, int)
    def test_case_5(self):
        df = task_func(7, domain="anotherdomain.com", random_seed=3)
        self.assertEqual(len(df), 7)
        self.assertTrue(df['title_url'].str.startswith("anotherdomain.com/Article_").all())
        self.assertEqual(len(df['id'].unique()), 7)
        self.assertTrue(df['category'].isin(['Sports', 'Technology', 'Health', 'Science', 'Business']).all())
        self.assertTrue(df['views'].dtype, int)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)