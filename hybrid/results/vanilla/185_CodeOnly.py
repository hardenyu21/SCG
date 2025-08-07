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