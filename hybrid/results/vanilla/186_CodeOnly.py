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