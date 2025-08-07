import pandas as pd
from sklearn.decomposition import PCA

def task_func(df):
    # Initialize PCA with 2 components
    pca = PCA(n_components=2)
    
    # Fit and transform the data
    principal_components = pca.fit_transform(df)
    
    # Create a DataFrame with the first two principal components
    df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
    
    return df_pca
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame([[0, 0], [0, 0]], columns = ['x', 'y'])
        df_pca = task_func(df)
        self.assertTrue('PC1' in df_pca.columns)
        self.assertTrue('PC2' in df_pca.columns)
        self.assertEqual(df_pca.shape, (2, 2))
        self.assertEqual(df_pca['PC1'].iloc[0], 0)
        self.assertEqual(df_pca['PC2'].iloc[0], 0)
        self.assertEqual(df_pca['PC1'].iloc[1], 0)
        self.assertEqual(df_pca['PC2'].iloc[1], 0)
    def test_case_2(self):
        df = pd.DataFrame([[1, 1], [1, 1]], columns = ['x', 'y'])
        df_pca = task_func(df)
        self.assertTrue('PC1' in df_pca.columns)
        self.assertTrue('PC2' in df_pca.columns)
        self.assertEqual(df_pca.shape, (2, 2))
        self.assertEqual(df_pca['PC1'].iloc[0], 0)
        self.assertEqual(df_pca['PC2'].iloc[0], 0)
        self.assertEqual(df_pca['PC1'].iloc[1], 0)
        self.assertEqual(df_pca['PC2'].iloc[1], 0)
    def test_case_3(self):
        df = pd.DataFrame([[1, 0], [0, 1]], columns = ['x', 'y'])
        df_pca = task_func(df)
        self.assertTrue('PC1' in df_pca.columns)
        self.assertTrue('PC2' in df_pca.columns)
        self.assertEqual(df_pca.shape, (2, 2))
        pca_new = PCA(n_components=2)
        df_pca_new = pca_new.fit_transform(df)
        self.assertEqual(df_pca['PC1'].iloc[0], df_pca_new[0, 0])
        self.assertEqual(df_pca['PC2'].iloc[0], df_pca_new[0, 1])
        self.assertEqual(df_pca['PC1'].iloc[1], df_pca_new[1, 0])
        self.assertEqual(df_pca['PC2'].iloc[1], df_pca_new[1, 1])
    def test_case_4(self):
        df = pd.DataFrame([[4, 3, 2, 1], [1, 2, 3, 4]], columns = ['x', 'y', 'z', 'w'])
        df_pca = task_func(df)
        self.assertTrue('PC1' in df_pca.columns)
        self.assertTrue('PC2' in df_pca.columns)
        self.assertEqual(df_pca.shape, (2, 2))
        pca_new = PCA(n_components=2)
        df_pca_new = pca_new.fit_transform(df)
        self.assertEqual(df_pca['PC1'].iloc[0], df_pca_new[0, 0])
    def test_case_5(self):
        df = pd.DataFrame([[1, 2, 3, 4], [4, 3, 2, 1]], columns = ['x', 'y', 'z', 'w'])
        df_pca = task_func(df)
        self.assertTrue('PC1' in df_pca.columns)
        self.assertTrue('PC2' in df_pca.columns)
        self.assertEqual(df_pca.shape, (2, 2))
        pca_new = PCA(n_components=2)
        df_pca_new = pca_new.fit_transform(df)
        self.assertEqual(df_pca['PC1'].iloc[0], df_pca_new[0, 0])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)