import collections
import random

def task_func(number_teams=5):
    # Create a dictionary with team names and random points
    teams = {f"Team {i}": random.randint(0, 100) for i in range(1, number_teams + 1)}
    
    # Sort the dictionary by points in descending order
    sorted_teams = sorted(teams.items(), key=lambda item: item[1], reverse=True)
    
    # Convert the sorted list of tuples back to an OrderedDict
    ordered_teams = collections.OrderedDict(sorted_teams)
    
    return ordered_teams

# Example usage
print(task_func(5))
import unittest
import random
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test if the return type is OrderedDict."""
        random.seed(0)
        result = task_func()
        self.assertIsInstance(result, collections.OrderedDict, "Return type should be OrderedDict.")
    def test_length_of_return(self):
        """Test if the returned OrderedDict has the correct length."""
        random.seed(0)
        result = task_func(5)
        self.assertEqual(len(result), 5, "Returned OrderedDict should have the same length as TEAMS.")
    def test_inclusion_of_teams(self):
        """Test if all predefined teams are included."""
        random.seed(0)
        result = task_func(5)
        TEAMS = []
        for i in range(1, 5+1):
            TEAMS.append("Team "+str(i))
        self.assertTrue(all(team in result for team in TEAMS), "All predefined teams should be included in the result.")
    def test_ordering_of_points(self):
        """Test if points are in descending order."""
        random.seed(0)
        result = task_func()
        points = list(result.values())
        self.assertTrue(all(points[i] >= points[i + 1] for i in range(len(points) - 1)), "Points should be in descending order.")
    def test_data_types_in_return(self):
        """Test if keys and values in the returned OrderedDict are of correct data types."""
        random.seed(0)
        result = task_func()
        self.assertTrue(all(isinstance(team, str) for team in result.keys()), "All keys in the result should be strings.")
        self.assertTrue(all(isinstance(points, int) for points in result.values()), "All values in the result should be integers.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)