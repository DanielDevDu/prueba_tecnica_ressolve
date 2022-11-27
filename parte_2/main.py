"""Main function"""
import json
import time
import glob
import pandas as pd
from ConfigFile import ConfigFile
from thread_solution.ManageData import ThreadManageData
from thread_solution.Executer import ThreadExecuter
from simple_solution.ManageData import SimpleManageData
from simple_solution.Executer import SimpleExecuter
from thread_pool_solution.ManageData import ThreadPoolManageData
from thread_pool_solution.Executer import PoolExecuter


if __name__ == "__main__":

    # List of files
    all_files_csv = glob.glob(ConfigFile.files_folder_path + "/*.csv")
    all_files_json = glob.glob(ConfigFile.files_folder_path + "/*.json")
    all_files = all_files_csv + all_files_json

    print("\n Total files to Read: ", len(all_files))

    ###########################################################################################
    # # Write dataframe to pickle without threads
    # print("\n==========================  Simple Solution  ==========================\n")
    # simple_manage = SimpleManageData()
    # simple_executer = SimpleExecuter(simple_manage)
    # start_time = time.time()
    # simple_executer.write(all_files)
    # print("Time to write dataframe without threads: ", time.time() - start_time)
    # simple_executer.read()
    ###########################################################################################

    ###########################################################################################
    # # Write dataframe to pickle with threads

    # # Create a thread for each file
    # threads = [ThreadManageData(file) for file in all_files]

    # # Execute threads
    # print("\n==========================  Thread Solution  ==========================\n")
    # thread_executer = ThreadExecuter()
    # start_time = time.time()
    # thread_executer.write(threads)
    # print("Time to write dataframe with threads: ", time.time() - start_time)
    # thread_executer.read(threads)
    ###########################################################################################

    ###########################################################################################
    # Write dataframe to pickle with threads Pool
    print("\n==========================  Thread Pool Solution  ==========================\n")
    pool_manage = ThreadPoolManageData()
    pool_executer = PoolExecuter(pool_manage)
    start_time = time.time()
    pool_executer.write(all_files)
    print("Time to write dataframe with threads pool: ", time.time() - start_time)
    pool_executer.read()
    ###########################################################################################

    # Update config_file.json from class ConfigFile with pickle
    with open('parte_2/config_file.json', 'w') as f:
        config_obj = ConfigFile()
        config_obj.csv_jobs = len(all_files_csv)
        config_obj.json_jobs = len(all_files_json)

        json.dump(config_obj.to_dict(), f)

    print("\n==========================  Done  ==========================\n")
