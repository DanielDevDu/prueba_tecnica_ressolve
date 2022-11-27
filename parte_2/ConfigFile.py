"""ConfigFile Class"""

import json

def read_json():
    with open('parte_2/config_file.json', 'r') as f:
        config = json.load(f)
        return config

class ConfigFile:
    """Class to read and write config file"""
    
    csv_jobs: int = 5
    json_jobs: int = 5
    files_folder_path: str = read_json()["files_folder_path"]
    dataframe_path: str = read_json()["dataframe_path"]

    def to_dict(self):
        """Save class attributes to json file"""
        repr_dict = {}
        repr_dict["csv_jobs"] = self.csv_jobs
        repr_dict["json_jobs"] = self.json_jobs
        repr_dict["files_folder_path"] = self.files_folder_path
        repr_dict["dataframe_path"] = self.dataframe_path

        return repr_dict
