import re
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Check if the DataFrame is empty or lacks the required columns
    if df.empty or not {'Title', 'Views', 'Likes'}.issubset(df.columns):
        fig, ax = plt.subplots()
        return ax

    # Filter videos with titles containing "how" or "what"
    pattern = re.compile(r'\b(how|what)\b', re.IGNORECASE)
    filtered_df = df[df['Title'].apply(lambda title: bool(pattern.search(title)))]

    # Check if there are any entries matching the search criteria
    if filtered_df.empty:
        fig, ax = plt.subplots()
        return ax

    # Calculate the like ratio for each video
    filtered_df['Like Ratio'] = filtered_df['Likes'] / filtered_df['Views']

    # Create a bar plot of the like ratios
    fig, ax = plt.subplots()
    filtered_df.plot(kind='bar', x='Title', y='Like Ratio', ax=ax)
    ax.set_title('Like Ratios for Videos with "How" or "What" in Title')
    ax.set_xlabel('Title')
    ax.set_ylabel('Like Ratio')
    ax.set_xticklabels(filtered_df['Title'], rotation=45, ha='right')

    return ax
# Integrating the test_cases function into the TestCases class methods and running the tests
import pandas as pd
import unittest
import matplotlib
matplotlib.use('Agg')
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data_1 = pd.DataFrame({
            'Title': ['How to code?', 'What is Python?', 'The art of programming', 'How to cook?', 'What is life?'],
            'Views': [1000, 500, 200, 300, 800],
            'Likes': [500, 250, 100, 150, 600]
        })
        ax = task_func(data_1)
        self.assertIsInstance(ax, matplotlib.axes.Axes, "The returned object should be of type Axes.")
        y_data = [rect.get_height() for rect in ax.patches]
        expected_y_data = [0.5, 0.5, 0.5, 0.75]
        self.assertEqual(y_data, expected_y_data, f"Expected {expected_y_data}, but got {y_data}")
    def test_case_2(self):
        data_2 = pd.DataFrame({
            'Title': ['How to swim?', 'What is Java?', 'The beauty of nature', 'How to paint?', 'What is art?'],
            'Views': [1200, 400, 250, 350, 900],
            'Likes': [600, 200, 125, 175, 450]
        })
        ax = task_func(data_2)
        self.assertIsInstance(ax, matplotlib.axes.Axes, "The returned object should be of type Axes.")
        y_data = [rect.get_height() for rect in ax.patches]
        expected_y_data = [0.5, 0.5, 0.5, 0.5]
        self.assertEqual(y_data, expected_y_data, f"Expected {expected_y_data}, but got {y_data}")
    def test_case_3(self):
        data_3 = pd.DataFrame({
            'Title': [],
            'Views': [],
            'Likes': []
        })
        ax = task_func(data_3)
        self.assertIsInstance(ax, matplotlib.axes.Axes, "The returned object should be of type Axes.")
    def test_case_4(self):
        data_4 = pd.DataFrame({
            'Title': ['Learning to code', 'Python basics', 'Advanced programming', 'Cooking basics',
                      'Life and philosophy'],
            'Views': [1100, 450, 220, 320, 850],
            'Likes': [550, 225, 110, 160, 425]
        })
        ax = task_func(data_4)
        self.assertIsInstance(ax, matplotlib.axes.Axes, "The returned object should be of type Axes.")
    def test_case_5(self):
        data_5 = pd.DataFrame({
            'Title': ['How to sing?', 'What is C++?', 'The mysteries of the universe', 'How to dance?',
                      'What is time?'],
            'Views': [1300, 420, 270, 370, 950],
            'Likes': [650, 210, 135, 185, 475]
        })
        ax = task_func(data_5)
        self.assertIsInstance(ax, matplotlib.axes.Axes, "The returned object should be of type Axes.")
        y_data = [rect.get_height() for rect in ax.patches]
        expected_y_data = [0.5, 0.5, 0.5, 0.5]
        self.assertEqual(y_data, expected_y_data, f"Expected {expected_y_data}, but got {y_data}")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)