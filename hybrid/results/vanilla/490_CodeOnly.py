import xmltodict
import json

def task_func(s, file_path):
    """
    Converts an XML string into a dictionary representation and saves it as a JSON file.

    Parameters:
    s (str): The XML string to be converted.
    file_path (str): The file path where the JSON file will be saved.

    Returns:
    dict: A dictionary representation of the XML string.
    """
    # Convert the XML string to a dictionary
    xml_dict = xmltodict.parse(s)
    
    # Save the dictionary as a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(xml_dict, json_file, indent=4)
    
    # Return the dictionary representation
    return xml_dict