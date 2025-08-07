import numpy as np
import geopandas as gpd
from shapely.geometry import Point

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Check if 'Lon' and 'Lat' keys are present and their values are tuples
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("Dictionary must contain 'Lon' and 'Lat' keys.")
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("'Lon' and 'Lat' values must be tuples.")
    
    # Generate random coordinates for each city
    coordinates = []
    for city in cities:
        lon = np.random.uniform(dic['Lon'][0], dic['Lon'][1])
        lat = np.random.uniform(dic['Lat'][0], dic['Lat'][1])
        coordinates.append(Point(lon, lat))
    
    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame({'City': cities, 'Coordinates': coordinates}, geometry='Coordinates')
    
    return gdf

# Example usage
gdf = task_func()
print(gdf)