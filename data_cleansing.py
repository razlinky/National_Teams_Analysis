import pandas as pd

goalscorers= pd.read_csv("goalscorers.csv")
results= pd.read_csv("results.csv")
shootouts= pd.read_csv("shootouts.csv")

# joined_df = results.merge(goalscorers, on='date'and'home_team', how='left').merge(shootouts, on='date'and 'home_team', how='left')

goalscorers_copy=goalscorers
results_copy=results
shootouts_copy=shootouts

# all varchar to lowe case function
def lowercase_text(column):
  """Function to convert text values in a column to lowercase."""
  return column.str.lower()  

# cleansing function remove duplicates,empty rows ,and create boolean column for winning/loosing
def cleansing():

    # drop duplicates rows 
    goalscorers_copy.drop_duplicates(inplace=True)
    results_copy.drop_duplicates(inplace=True)
    shootouts_copy.drop_duplicates(inplace=True)

    # Drop empty rows
    goalscorers_copy.dropna()
    results_copy.dropna()
    shootouts_copy.dropna()

    results_copy    ['is_home_win']                  = results_copy    ['home_score'] > results_copy['away_score']
    shootouts_copy  ['is_home_win']                  = shootouts_copy  ['home_team'] == shootouts_copy['winner']
    shootouts_copy  ['is_home_team_first_shooter']   = shootouts_copy  ['home_team'] == shootouts_copy['first_shooter']

 
#  the user will choose specific team in order to see the statistic 
def team_analyzer():
    team=input(""" Enter home team:\n""")
# ---need to check how can i do or home team or away tem 
    filtered_df = results_copy.query(f"home_team=={team}")
    # filtered_df = results_copy.query(f"(home_team == '{str(home_team)}') | (away_team == '{home_team}')")

    print(filtered_df)







goalscorers_copy = goalscorers_copy.apply(lowercase_text, axis=1)
results_copy = results_copy.apply(lowercase_text, axis=1)
shootouts_copy = shootouts_copy.apply(lowercase_text, axis=1)

cleansing()

team_analyzer()









