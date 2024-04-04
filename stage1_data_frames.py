# import libraries
import pandas as pd 
import sys


# def check_populated_columns in percentages (df, df_name):
from functions_data_frames import check_populated_pct




# will check the quality of the data 

from functions_data_frames import table_viewer

# types,duplicate rows,emptyrows,emptycolumn
# def table_viewer(table_name):
#     file = table_name + ".csv"
#     print(f"\n{table_name} table below\n")
#     print(pd.read_csv(file).head(), "\n")
#     print(f"{file} table contain {pd.read_csv(file).shape[0]} rows and {pd.read_csv(file).shape[1]} columns.\n")
#     print(f"The types of the columns are:\n {pd.read_csv(file).dtypes}\n")
#     print(f"The number of missing values in each columns are:\n {pd.read_csv(file).isna().sum()}\n")
#     print(f"The number of duplicate rows are: \n {pd.read_csv(file).duplicated().sum()}\n")
#     print(f"The number of empty rows(all nulls) are: \n{pd.read_csv(file).isna().all(axis=1).sum()}") 
#     check_populated_pct(pd.read_csv(file), table_name)
    
# for each input from the user will have the name of the table in order to print the details of it to the user



# choose the table u want to see 

from functions_data_frames import table_chooser
table_chooser()



# after the user saw the data he choosed he is getting menu

from functions_data_frames import menu
# def menu():
#     user_menu=int(input("""\n Enter 1 if you want start over\n Enter 2 if you want continue to data cleansing\n Enter 3 to exit: """))
#     if user_menu==1:
#         table_chooser() 
#     elif user_menu==2:
#         import cleansing_and_plot 
#     elif user_menu==3:
#         print("bye :)")
#         sys.exit(0)
#     else:
#         print("\nplease enter valid number.\n")
#     menu()
menu()





