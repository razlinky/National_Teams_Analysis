import pandas as pd 

goalscorers= pd.read_csv("goalscorers.csv")
results= pd.read_csv("results.csv")
shootouts= pd.read_csv("shootouts.csv")

# joined_df = results.merge(goalscorers, on='date'and'home_team', how='left').merge(shootouts, on='date'and 'home_team', how='left')

goalscorers_copy=goalscorers
results_copy=results
shootouts_copy=shootouts



def lowercase_text(column):
  """Function to convert text values in a column to lowercase."""
  return column.str.lower()

# Exclude columns to avoid lowercase conversion (modify this list as needed)
exclude_cols = ['home_team']

# Filter out the columns to exclude before applying the function
filtered_df = goalscorers_copy.filter(like=r'^[^_]')  # Filter columns that don't start with underscore

# Apply the function to the filtered DataFrame
lowercase_df = filtered_df.apply(lowercase_text)

# Combine the original DataFrame with the lowercase DataFrame
goalscorers_copy = goalscorers_copy[exclude_cols].join(lowercase_df)




