"""SimpleManageData"""

import os
import json
import glob
import pickle
import pandas as pd
from time import sleep
from ConfigFile import ConfigFile


class ThreadPoolManageData:

    __df = None

    def __init__(self):
        self.__df = pd.DataFrame()

    def read(self, file_name: str):
        """Read file and save to dataframe"""
        if file_name.endswith('.csv'):
            self.read_csv(file_name)
        elif file_name.endswith('.json'):
            self.read_json(file_name)
        else:
            print("File not supported")

    def read_csv(self, file_name: str) -> pd.DataFrame:
        """Read csv file and save to dataframe"""
        df = pd.read_csv(file_name)
        self.to_dataframe(df)

    def read_json(self, file_name: str) -> pd.DataFrame:
        """Read json file and save to dataframe"""
        with open(file_name) as f:
            data = json.load(f)
        df = pd.json_normalize(data)
        self.to_dataframe(df)

    def to_dataframe(self, df) -> pd.DataFrame:
        """Add dataframe to class attributte self.__df"""
        self.__df = pd.concat([self.__df, df], ignore_index=True)
        return self.__df

    def save_dataframe(self):
        """Save dataframe to pickle"""
        with open(ConfigFile.dataframe_path, 'wb') as f:
            pickle.dump(self.__df, f)

    def read_dataframe(self) -> pd.DataFrame:
        """Read dataframe from pickle"""
        with open(ConfigFile.dataframe_path, 'rb') as f:
            df = pickle.load(f)
            # self.to_dataframe(df)
        return df
