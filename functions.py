# import libraries
import pandas as pd 



def table_viewer(table_name):
    file = table_name + ".csv"
    print(f"\n{table_name} table below\n")
    print(pd.read_csv(file).head(), "\n")
    print(f"{file} table contain {pd.read_csv(file).shape[0]} rows and {pd.read_csv(file).shape[1]} columns.\n")
    print(f"The types of the columns are:\n {pd.read_csv(file).dtypes}\n")
    print(f"The number of missing values in each columns are:\n {pd.read_csv(file).isna().sum()}\n")
    print(f"The number of duplicate rows are: \n {pd.read_csv(file).duplicated().sum()}\n")
    print(f"The number of empty rows(all nulls) are: \n{pd.read_csv(file).isna().all(axis=1).sum()}")  






import pandas as pd


df = pd.read_csv("your_file.csv")  # Assuming you have a CSV file to read

def lowercase_text(column):
  """Function to convert text values in a column to lowercase."""
  return column.str.lower()

# Apply the function to all string columns using apply
df = df.apply(lowercase_text, axis=1)

# Now all text-like columns in 'df' are in lowercase
print(df)

