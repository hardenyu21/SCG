from geopy.distance import geodesic
import folium

def task_func(dic):
    if not dic:
        raise ValueError("The input dictionary is empty.")
    
    # Create a Folium map centered at the first location
    locations = list(dic.keys())
    first_location = locations[0]
    first_coords = dic[first_location]
    m = folium.Map(location=first_coords, zoom_start=10)
    
    # Add markers for each location
    for name, coords in dic.items():
        folium.Marker(location=coords, popup=name).add_to(m)
    
    # Calculate geodesic distances between each pair of locations
    distances = {}
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            loc1 = locations[i]
            loc2 = locations[j]
            coords1 = dic[loc1]
            coords2 = dic[loc2]
            distance_km = geodesic(coords1, coords2).kilometers
            distances[(loc1, loc2)] = distance_km
    
    return m, distances

# Example usage:
# locations = {
#     "Location A": (52.5200, 13.4050),  # Berlin
#     "Location B": (48.8566, 2.3522),   # Paris
#     "Location C": (51.5074, -0.1278)   # London
# }
# map_obj, distances = task_func(locations)
# map_obj.save("map.html")
# print(distances)
import unittest
from unittest.mock import patch
import folium  # Assuming the function task_func and folium are imported or defined appropriately.
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a tuple with a map and a dictionary."""
        result = task_func({'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': {'Lat': 1, 'Lon': 1}})
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], folium.folium.Map)
        self.assertIsInstance(result[1], dict)
    def test_distances_calculation(self):
        """Test the accuracy of the distance calculation. Assumes the distance is reasonable for nearby points."""
        _, distances = task_func({'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': {'Lat': 0, 'Lon': 1}})
        self.assertTrue(0 < distances[('Loc1', 'Loc2')] < 200)  # Rough check for distance in kilometers
    def test_multiple_locations(self):
        """Test functionality with multiple locations."""
        _, distances = task_func({'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': {'Lat': 0, 'Lon': 1}, 'Loc3': {'Lat': 1, 'Lon': 1}})
        self.assertEqual(len(distances), 3)  # Expecting 3 pairs of locations
    def test_marker_addition(self):
        """Test that markers are correctly added to the map. Assumes 1 TileLayer present."""
        folium_map, _ = task_func({'Loc1': {'Lat': 0, 'Lon': 0}})
        self.assertEqual(len(folium_map._children), 2)  # One for TileLayer and one for Marker
    @patch('geopy.distance.geodesic')
    def test_distance_dict_structure(self, mock_geodesic):
        """Ensure the distance dictionary has the correct key-value structure."""
        mock_geodesic.return_value.kilometers = 100  # Mock distance as 100 km
        _, distances = task_func({'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': {'Lat': 0, 'Lon': 1}})
        self.assertTrue(all(isinstance(key, tuple) and isinstance(value, float) for key, value in distances.items()))
    def test_empty_input(self):
        """Test function behavior with an empty dictionary input raises ValueError."""
        with self.assertRaises(ValueError):
            task_func({})
    def test_single_location(self):
        """Test handling of a single location input."""
        folium_map, distances = task_func({'Loc1': {'Lat': 0, 'Lon': 0}})
        self.assertEqual(len(distances), 0)  # No distances calculated
        self.assertEqual(len(folium_map._children), 2)  # One for TileLayer and one for Marker
    def test_negative_lat_lon(self):
        """Test handling of negative latitude and longitude values."""
        _, distances = task_func({'Loc1': {'Lat': -34, 'Lon': -58}, 'Loc2': {'Lat': -33, 'Lon': -70}})
        self.assertTrue(all(value >= 0 for value in distances.values()))  # Distance should be positive
    def test_large_distance_calculation(self):
        """Test accuracy for large distances, e.g., antipodal points."""
        _, distances = task_func({'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': {'Lat': 0, 'Lon': 180}})
        self.assertTrue(distances[('Loc1', 'Loc2')] > 10000)  # Expecting a large distance


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)