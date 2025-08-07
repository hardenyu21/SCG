import random
from scipy import stats

def task_func(animals, mean):
    # Determine the number of customers using a Poisson distribution
    num_customers = stats.poisson.rvs(mu=mean)
    
    # Initialize a dictionary to keep track of sales
    sales_summary = {animal: 0 for animal in animals}
    
    # Simulate each customer's purchase
    for _ in range(num_customers):
        # Randomly choose an animal for the customer to buy
        chosen_animal = random.choice(animals)
        # Increment the count for the chosen animal
        sales_summary[chosen_animal] += 1
    
    # Display the sales summary
    print("Sales Summary:")
    for animal, count in sales_summary.items():
        print(f"{animal}: {count} sales")
    
    # Return the sales summary dictionary
    return sales_summary

# Example usage:
animals = ['dog', 'cat', 'bird', 'fish']
mean_customers = 10
sales = task_func(animals, mean_customers)
import unittest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def setUp(self):
        self.animals = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_typical_case(self, mock_poisson, mock_choice):
        """Test typical case with mock number of customers and sales."""
        mock_poisson.return_value.rvs.return_value = 100
        mock_choice.side_effect = lambda x: x[0]  # always choose the first animal
        expected = {'Dog': 100, 'Cat': 0, 'Bird': 0, 'Fish': 0, 'Hamster': 0}
        result = task_func(self.animals, 100)
        self.assertEqual(result, expected)
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_zero_customers(self, mock_poisson, mock_choice):
        """Test the scenario where zero customers arrive."""
        mock_poisson.return_value.rvs.return_value = 0
        expected = {'Dog': 0, 'Cat': 0, 'Bird': 0, 'Fish': 0, 'Hamster': 0}
        result = task_func(self.animals, 0)
        self.assertEqual(result, expected)
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_large_number_of_customers(self, mock_poisson, mock_choice):
        """Test the function with a very large number of customers."""
        mock_poisson.return_value.rvs.return_value = 1000
        mock_choice.side_effect = lambda x: 'Dog'  # simulate all choosing 'Dog'
        expected = {'Dog': 1000, 'Cat': 0, 'Bird': 0, 'Fish': 0, 'Hamster': 0}
        result = task_func(self.animals, 500)
        self.assertEqual(result, expected)
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_random_animal_selection(self, mock_poisson, mock_choice):
        """Test random selection of animals."""
        mock_poisson.return_value.rvs.return_value = 5
        mock_choice.side_effect = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
        result = task_func(self.animals, 5)
        expected = {'Dog': 1, 'Cat': 1, 'Bird': 1, 'Fish': 1, 'Hamster': 1}
        self.assertEqual(result, expected)
    def test_empty_animal_list(self):
        """Test with an empty list of animals."""
        result = task_func([], 10)
        self.assertEqual(result, {})
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_return_type(self, mock_poisson, mock_random):
        """Test that the function returns a dictionary."""
        mock_poisson.return_value.rvs.return_value = 5
        mock_random.side_effect = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
        result = task_func(self.animals, 120)
        self.assertIsInstance(result, dict)
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_sales_content(self, mock_poisson, mock_random):
        """Test the content of the sales dictionary matches the expected distribution of one each."""
        mock_poisson.return_value.rvs.return_value = 5
        mock_random.side_effect = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
        result = task_func(self.animals, 120)
        self.assertEqual(result, {'Dog': 1, 'Cat': 1, 'Bird': 1, 'Fish': 1, 'Hamster': 1})
    @patch('scipy.stats.poisson')
    def test_no_customer(self, mock_poisson):
        """Test the function with zero customers."""
        mock_poisson.return_value.rvs.return_value = 0
        result = task_func(self.animals, 120)
        self.assertEqual(result, {animal: 0 for animal in self.animals})
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_all_animals_sold(self, mock_poisson, mock_random):
        """Test that all animal types are considered in sales."""
        mock_poisson.return_value.rvs.return_value = 5
        mock_random.side_effect = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
        result = task_func(self.animals, 120)
        self.assertTrue(all(animal in result for animal in self.animals))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)