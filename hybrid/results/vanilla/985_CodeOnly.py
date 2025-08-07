import pandas as pd
import json
import os
import math

def task_func(json_data, output_dir=".", file_name="country_population_report.csv"):
    # Validate and parse JSON data
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        raise ValueError("The JSON data is malformed.")
    
    if not isinstance(data, list) or not data:
        raise ValueError("The JSON data is empty or not in the expected format.")
    
    # Prepare data for DataFrame
    countries = []
    populations = []
    
    for item in data:
        if not isinstance(item, dict) or "Country" not in item or "Population" not in item:
            raise ValueError("Each item in JSON data must be a dictionary with 'Country' and 'Population' keys.")
        
        country = item["Country"]
        population = item["Population"]
        
        if not isinstance(country, str):
            raise ValueError("Country names must be strings.")
        
        if not isinstance(population, (int, float)) or population < 0:
            raise ValueError("Populations must be non-negative numbers.")
        
        # Round down float populations to the nearest integer
        if isinstance(population, float):
            population = math.floor(population)
        
        countries.append(country)
        populations.append(population)
    
    # Create DataFrame
    df = pd.DataFrame({"Country": countries, "Population": populations})
    
    # Define file path
    file_path = os.path.join(output_dir, file_name)
    
    # Write DataFrame to CSV
    try:
        df.to_csv(file_path, index=False)
    except IOError:
        raise IOError("The file cannot be written to the specified directory.")
    
    return file_path, df