import pandas as pd
import numpy as np
import folium

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Validate input dictionary
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("Dictionary must contain 'Lon' and 'Lat' keys.")
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("'Lon' and 'Lat' values must be tuples.")
    
    # Generate random coordinates for each city
    longitudes = np.random.uniform(dic['Lon'][0], dic['Lon'][1], size=len(cities))
    latitudes = np.random.uniform(dic['Lat'][0], dic['Lat'][1], size=len(cities))
    
    # Create a DataFrame with city names and their coordinates
    data = {
        'City': cities,
        'Longitude': longitudes,
        'Latitude': latitudes
    }
    df = pd.DataFrame(data)
    
    # Create a folium map centered at the average of the generated coordinates
    map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
    m = folium.Map(location=map_center, zoom_start=2)
    
    # Add markers for each city on the map
    for index, row in df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['City']
        ).add_to(m)
    
    # Return the map and the DataFrame
    return m, df

# Example usage:
# map_obj, df = task_func()
# map_obj.save('map.html')
# print(df)
import unittest
import numpy as np
import pandas as pd
import folium
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        np.random.seed(42)
        map_obj, city_data = task_func()
        self.assertEqual(len(city_data), 5)  # Default 5 cities
        self.assertIsInstance(city_data, pd.DataFrame)
        self.assertIn('New York', city_data['City'].values)
        
        df_list = city_data.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        with open('df_contents.txt', 'w') as file:
            file.write(str(df_list))
            
        expect = ['New York,-45.1655572149495,81.12857515378491', 'London,83.51781905210584,17.758527155466595', 'Beijing,-123.83328944072285,-61.92098633948352', 'Tokyo,-159.0898996194482,65.91170623948832', 'Sydney,36.40140422755516,37.45306400328819']
        
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")
    def test_custom_cities(self):
        custom_cities = ['Paris', 'Berlin']
        _, city_data = task_func(cities=custom_cities)
        self.assertEqual(len(city_data), 2)
        self.assertTrue(all(city in city_data['City'].values for city in custom_cities))
    def test_invalid_dic(self):
        with self.assertRaises(ValueError):
            task_func(dic={'Lon': 'invalid', 'Lat': (-90, 90)})
    def test_coordinate_ranges(self):
        _, city_data = task_func(dic={'Lon': (0, 10), 'Lat': (0, 10)})
        self.assertTrue(all(0 <= lon <= 10 for lon in city_data['Longitude']))
        self.assertTrue(all(0 <= lat <= 10 for lat in city_data['Latitude']))
    def test_return_types(self):
        map_obj, city_data = task_func()
        self.assertIsInstance(map_obj, folium.Map)
        self.assertIsInstance(city_data, pd.DataFrame)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)