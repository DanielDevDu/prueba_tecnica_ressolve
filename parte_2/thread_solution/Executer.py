"""Executer class for thread solution"""
import json
import csv
import time
import glob
import pickle
import pandas as pd
from time import sleep
import concurrent.futures
from threading import Thread
from thread_solution.ManageData import ThreadManageData
from ConfigFile import ConfigFile
from threading import current_thread


class ThreadExecuter:

    def write(self, threads=[]):
        """
        ------------------------------
        Write dataframe to pickle
        Run all threads for each file
        ------------------------------
        """
        for thread in threads:
            thread.start()
            thread.join()
            # sleep(5)

    def read(self, threads=[]):
        """Read dataframe from pickle"""

        df_print = pd.DataFrame()
        for thread in threads:
            df = thread.read_dataframe()
            df_print = pd.concat([df_print, df], ignore_index=True)

        print("\n Total Dataframe: \n\n", df_print)
