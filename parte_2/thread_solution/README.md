In this solution I use the custom Thread class(ThreadManageData) to create deamons for each file

- Each File run with its own thread(an instance of the custom class)
- With ThreadManageData class we can:

  - read files with pandas or json
  - convert to Dataframe with pandas
  - save in a file with pickle
  - read dataframe from pickle file

- The Executer class is the form in we can execute the methos of the class
