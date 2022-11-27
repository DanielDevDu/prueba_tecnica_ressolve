"""ThreadManageData"""
import os
import json
import glob
import pickle
import pandas as pd
from time import sleep
from threading import Thread
from threading import current_thread
from ConfigFile import ConfigFile


class ThreadManageData(Thread):

    __df = None

    def __init__(self, current_file=None):
        Thread.__init__(self, daemon=True)
        self.__df = pd.DataFrame()
        self.current_file = current_file

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
            self.to_dataframe(df)
        return df

    def run(self):
        """
        --------------------------------
        Override Thread.run() method
        Read file and save to dataframe
        with a thread for each file
        --------------------------------
        """

        # # Show information about threads
        # Thread = current_thread()
        # print("Thread name: ", Thread.name)
        # print("Thread ident: ", Thread.ident)
        # print("Thread daemon: ", Thread.daemon)

        if self.current_file.endswith(".csv"):
            self.read_csv(self.current_file)
            self.save_dataframe()
        elif self.current_file.endswith(".json"):
            self.read_json(self.current_file)
            self.save_dataframe()
