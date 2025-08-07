import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_types=5, integer_range=(0, 100)):
    # Generate random data
    categories = [f'Category_{i+1}' for i in range(num_types)]
    data = {category: [randint(*integer_range) for _ in range(num_types)] for category in categories}
    
    # Create a DataFrame
    df = pd.DataFrame(data, index=categories)
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(kind='barh', stacked=True, ax=ax)
    
    # Set labels and title
    ax.set_xlabel('Values')
    ax.set_ylabel('Categories')
    ax.set_title('Horizontal Stacked Bar Chart')
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    return fig, ax

# Example usage
fig, ax = task_func()
import unittest
import matplotlib
matplotlib.use('Agg')
class TestCases(unittest.TestCase):
    def test_case_1(self):
        fig, ax = task_func()
        self.assertEqual(len(ax.patches), 25)
    def test_case_2(self):
        fig, ax = task_func(3, (0, 50))
        self.assertEqual(len(ax.patches), 9)
    def test_case_3(self):
        fig, ax = task_func(10)
        self.assertEqual(len(ax.patches), 100)
    def test_case_4(self):
        fig, ax = task_func(1, (10, 20))
        self.assertEqual(len(ax.patches), 1)
    def test_case_5(self):
        fig, ax = task_func(2, (5, 15))
        self.assertEqual(len(ax.patches), 4)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)