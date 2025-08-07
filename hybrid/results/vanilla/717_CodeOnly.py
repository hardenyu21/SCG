import sys
from configparser import ConfigParser

# Constants
PATH_TO_APPEND = '/path/to/whatever'
CONFIG_FILE = '/path/to/config.ini'

def task_func(path_to_append=PATH_TO_APPEND, config_file=CONFIG_FILE):
    # Add the specific path to sys.path
    if path_to_append not in sys.path:
        sys.path.append(path_to_append)
    
    # Update the configuration file with the new path
    config = ConfigParser()
    config.read(config_file)
    
    # Assuming there is a section named 'Paths' in the config file
    if 'Paths' not in config:
        config['Paths'] = {}
    
    # Update or add the path in the configuration
    config['Paths']['additional_path'] = path_to_append
    
    # Write the changes back to the configuration file
    with open(config_file, 'w') as configfile:
        config.write(configfile)
    
    # Return the updated configuration object and the path to the configuration file
    return config, config_file

# Example usage
if __name__ == "__main__":
    updated_config, config_path = task_func()
    print(f"Configuration updated: {updated_config}")
    print(f"Configuration file path: {config_path}")