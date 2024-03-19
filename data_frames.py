# import libraries
import pandas as pd 


# the user choose which table to see
user_input = int(input(""" Hello user how are you?\n Enter 1 if you want to see all the data for football analysis\n Enter 2 if you want to see only goalscorers data
 Enter 3 if you want to see only results data\n Enter 4 if you want to see only shootouts data: """))

# create disctionary for table name and it's own dataframe
data_dict = {
    "goalscorers": pd.read_csv("goalscorers.csv"),
    "results": pd.read_csv("results.csv"),
    "shootouts": pd.read_csv("shootouts.csv")
            }

# if the user enter not a valid number , he will get a msg to enter again
while user_input not in range(1,5):
    user_input=int(input(""" please enter valid number\n Enter 1 if you want to see all the data for football analysis\n Enter 2 if you want to see only goalscorers data
 Enter 3 if you want to see only results data\n Enter 4 if you want to see only shootouts data: """))
    
#  if the user choose 1 it will print all the tables with it's own meta data   
if user_input==1:    
        for key,value in data_dict.items():
            print(f"{key} table below\n")
            print(value.head(), "\n")
            print(f"{key} table contain {value.shape[0]} rows and {value.shape[1]} columns.\n")
            print(f"The types of the columns are:\n {value.dtypes}\n")
            print(f"The number of missing values in each columns are:\n {value.isna().sum()}\n")
            print(f"The number of duplicate rows are: \n {value.duplicated().sum()}\n")
            print(f"The number of empty rows(all nulls) are: \n{value.isna().all(axis=1).sum()}")

# 2 means user wants to see meta data only on goal scorers
elif user_input==2:    
            print("\ngoalscorers table below\n")
            print(pd.read_csv("goalscorers.csv").head(), "\n")
            print(f"goalscorers table contain {pd.read_csv("goalscorers.csv").shape[0]} rows and {pd.read_csv("goalscorers.csv").shape[1]} columns.\n")
            print(f"The types of the columns are:\n {pd.read_csv("goalscorers.csv").dtypes}\n")
            print(f"The number of missing values in each columns are:\n {pd.read_csv("goalscorers.csv").isna().sum()}\n")
            print(f"The number of duplicate rows are: \n {pd.read_csv("goalscorers.csv").duplicated().sum()}\n")
            print(f"The number of empty rows(all nulls) are: \n{pd.read_csv("goalscorers.csv").isna().all(axis=1).sum()}")  

# 3 means user wants to see meta data only on results
elif user_input==3:    
            print("\nresults table below\n")
            print(pd.read_csv("results.csv").head(), "\n")
            print(f"results table contain {pd.read_csv("results.csv").shape[0]} rows and {pd.read_csv("results.csv").shape[1]} columns.\n")
            print(f"The types of the columns are:\n {pd.read_csv("results.csv").dtypes}\n")
            print(f"The number of missing values in each columns are:\n {pd.read_csv("results.csv").isna().sum()}\n")
            print(f"The number of duplicate rows are: \n {pd.read_csv("results.csv").duplicated().sum()}\n")
            print(f"The number of empty rows(all nulls) are: \n{pd.read_csv("results.csv").isna().all(axis=1).sum()}") 
            
# 4 means user wants to see meta data only on shootouts
elif user_input==4:    
            print("\nshootouts table below\n")
            print(pd.read_csv("shootouts.csv").head(), "\n")
            print(f"shootouts table contain {pd.read_csv("shootouts.csv").shape[0]} rows and {pd.read_csv("shootouts.csv").shape[1]} columns.\n")
            print(f"The types of the columns are:\n {pd.read_csv("shootouts.csv").dtypes}\n")
            print(f"The number of missing values in each columns are:\n {pd.read_csv("shootouts.csv").isna().sum()}\n")
            print(f"The number of duplicate rows are: \n {pd.read_csv("shootouts.csv").duplicated().sum()}\n")
            print(f"The number of empty rows(all nulls) are: \n{pd.read_csv("shootouts.csv").isna().all(axis=1).sum()}") 



