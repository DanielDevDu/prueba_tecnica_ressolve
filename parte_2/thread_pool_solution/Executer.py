"""Executer class for simple solution"""

from thread_pool_solution.ManageData import ThreadPoolManageData
from concurrent.futures import ThreadPoolExecutor


class PoolExecuter:

    __manage_data = None

    def __init__(self, manage_data: ThreadPoolManageData):
        self.__manage_data = manage_data

    def write(self, all_files=[]):
        """
        ------------------------------
        Write data from file to pickle
        ------------------------------
        """
        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.map(self.__manage_data.read, all_files)
            executor.submit(self.__manage_data.save_dataframe)

    def read(self):
        """Read dataframe from pickle with threadsPoolExecutor"""
        with ThreadPoolExecutor(max_workers=1) as executor:
            df = executor.submit(self.__manage_data.read_dataframe)

        print("\n Total Dataframe: \n\n", df.result())
