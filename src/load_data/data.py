import os
import yaml

def load_config(config_name, path):
    """Function to load yaml configuration file.

    Args:
        config_name (string): Name of yaml config file.
        path (string): Path to yaml config file.

    Returns:
        dict: Returns dictionary containing data stored in config file
    """
    # Function to load yaml configuration file
    with open(os.path.join(path, config_name)) as file:
        config = yaml.safe_load(file)

    return config

