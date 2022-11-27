"""Executer class for simple solution"""

from simple_solution.ManageData import SimpleManageData


class SimpleExecuter:

    __manage_data = None

    def __init__(self, manage_data: SimpleManageData):
        self.__manage_data = manage_data

    def write(self, all_files=[]):
        """
        ------------------------------
        Write data from file to pickle
        ------------------------------
        """

        for file in all_files:
            self.__manage_data.read(file)
            self.__manage_data.save_dataframe()

    def read(self):
        """Read dataframe from pickle"""
        df = self.__manage_data.read_dataframe()
        print("\n Total Dataframe: \n\n", df)
