import random
import matplotlib.pyplot as plt

def task_func(points: int):
    # Generate a list of random numbers
    random_numbers = [random.random() for _ in range(points)]
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(range(points), random_numbers, marker='o')
    
    # Set labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Random Number')
    ax.set_title('Plot of Random Numbers')
    
    # Show the plot
    plt.show()
    
    # Return the list of random numbers and the Axes object
    return random_numbers, ax

# Example usage:
# random_numbers, ax = task_func(10)
import unittest
import random
class TestCases(unittest.TestCase):
    def test_case_1(self):
        random.seed(0)
        y, _ = task_func(5)
        # Test correct number of points are generated
        self.assertEqual(len(y), 5)
    def test_case_2(self):
        random.seed(0)
        y, _ = task_func(5)
        # Test expected values
        self.assertTrue(all(0 <= num <= 1 for num in y))
        self.assertAlmostEqual(
            y,
            [
                0.8444218515250481,
                0.7579544029403025,
                0.420571580830845,
                0.25891675029296335,
                0.5112747213686085,
            ],
        )
    def test_case_3(self):
        random.seed(0)
        # Test incorrect data types
        with self.assertRaises(TypeError):
            task_func("5")
        with self.assertRaises(TypeError):
            task_func([])
        with self.assertRaises(TypeError):
            task_func(None)
    def test_case_4(self):
        random.seed(0)
        # Test handling 1 number
        y, ax = task_func(1)
        # Assert that 1 random number is generated
        self.assertEqual(len(y), 1)
        # Assert that the plot has the correct x and y data
        self.assertEqual(list(ax.lines[0].get_xdata()), [0])
        self.assertEqual(list(ax.lines[0].get_ydata()), y)
    def test_case_5(self):
        random.seed(0)
        # Test handling no random numbers
        y, ax = task_func(0)
        self.assertEqual(len(y), 0)
        # Assert that the plot has no data
        self.assertEqual(list(ax.lines[0].get_xdata()), [])
        self.assertEqual(list(ax.lines[0].get_ydata()), [])
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)