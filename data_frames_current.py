# import libraries
import pandas as pd 
import sys
# define the function to print the date regarding the csvs 
def table_viewer(table_name):
    file = table_name + ".csv"
    print(f"\n{table_name} table below\n")
    print(pd.read_csv(file).head(), "\n")
    print(f"{file} table contain {pd.read_csv(file).shape[0]} rows and {pd.read_csv(file).shape[1]} columns.\n")
    print(f"The types of the columns are:\n {pd.read_csv(file).dtypes}\n")
    print(f"The number of missing values in each columns are:\n {pd.read_csv(file).isna().sum()}\n")
    print(f"The number of duplicate rows are: \n {pd.read_csv(file).duplicated().sum()}\n")
    print(f"The number of empty rows(all nulls) are: \n{pd.read_csv(file).isna().all(axis=1).sum()}")  


# for each input from the user will have the name of the table in order to print the details of it to the user
user_input_dict={1:"all",2:"goalscorers",3:"results",4:"shootouts"}

print("Hello user how are you?\n")


# choose the table u want to see 
def table_chooser():

    user_input = int(input("""Enter 1 if you want to see all the data for football analysis \nEnter 2 if you want to see only goalscorers data
Enter 3 if you want to see only results data \nEnter 4 if you want to see only shootouts data: """))
    
# if the user enter not a valid number , he will get a msg to enter again
    while user_input not in range(1,5):
        user_input=int(input("""\nplease enter a valid number\n """))

# different from 1 means only one table to show the user
    if user_input!=1:
        table_viewer(user_input_dict[user_input])
    else:
        for i in range(2,5):
            table_viewer(user_input_dict[i])

# choose the table u want to see --print
table_chooser()


# after the user saw the data he choosed he is getting menu


def menu():
    user_menu=int(input(""" Enter 1 if you want start over\n Enter 2 if you want continue to data cleansing\n Enter 3 to exit: """))

    if user_menu==1:
        table_chooser() 
        
    elif user_menu==2:
        print("cleansing")
    elif user_menu==3:
        print("bye :)")
        sys.exit(0)
    else:
        print("\nplease enter valid number.\n")
    menu()



menu()




