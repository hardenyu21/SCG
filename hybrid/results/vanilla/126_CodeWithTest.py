import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np
import matplotlib.pyplot as plt

def task_func(animals=None, seed=42):
    if animals is None:
        animals = ['Lion', 'Tiger', 'Bear', 'Giraffe', 'Elephant', 'Zebra', 'Kangaroo', 'Penguin', 'Panda', 'Koala']
    
    random_seed(seed)
    
    data = []
    
    for animal in animals:
        counts = [randint(1, 100) for _ in range(10)]
        mean_count = statistics.mean(counts)
        median_count = statistics.median(counts)
        std_dev_count = statistics.stdev(counts)
        
        data.append({
            'Animal': animal,
            'Mean': mean_count,
            'Median': median_count,
            'Standard Deviation': std_dev_count
        })
    
    df = pd.DataFrame(data)
    
    # Plotting the bar chart
    plt.figure(figsize=(10, 6))
    for i, animal in enumerate(animals):
        plt.bar(animal, df.loc[i, 'Mean'], yerr=df.loc[i, 'Standard Deviation'], capsize=5, label=animal)
    
    plt.xlabel('Animal')
    plt.ylabel('Mean Count ± Standard Deviation')
    plt.title('Animal Counts in the Zoo')
    plt.xticks(rotation=45)
    plt.legend(title='Animals')
    plt.tight_layout()
    plt.show()
    
    return df

# Example usage
df = task_func()
print(df)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_default_animals(self):
        report = task_func()
        
        self.assertEqual(len(report), 5)  # Default number of animals
        self.assertListEqual(list(report['Animal']), ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda'])
        df_list = report.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        with open('df_contents.txt', 'w') as file:
            file.write(str(df_list))
            
        expect = ['Lion,42.0,30.5,95,33.250563904992646', 'Elephant,44.4,41.5,12,34.1970758983864', 'Tiger,61.1,71.0,30,28.76264939118092', 'Giraffe,51.8,54.5,54,29.208902752414375', 'Panda,35.8,32.0,44,24.595934623429134']
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")
    def test_custom_animals(self):
        custom_animals = ['Dog', 'Cat']
        report = task_func(custom_animals)
        self.assertEqual(len(report), len(custom_animals))
        self.assertListEqual(list(report['Animal']), custom_animals)
    def test_statistics_columns(self):
        report = task_func()
        expected_columns = ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
        self.assertListEqual(list(report.columns), expected_columns)
    def test_positive_counts(self):
        report = task_func()
        self.assertTrue(all(report['Mean'] > 0))
        self.assertTrue(all(report['Median'] > 0))
        self.assertTrue(all(report['Mode'] > 0))
        self.assertTrue(all(report['Standard Deviation'] >= 0))
    def test_data_frame_structure(self):
        report = task_func()
        self.assertIsInstance(report, pd.DataFrame)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)