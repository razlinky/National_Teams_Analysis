import pandas as pd

goalscorers= pd.read_csv("goalscorers.csv")
results= pd.read_csv("results.csv")
shootouts= pd.read_csv("shootouts.csv")

# joined_df = results.merge(goalscorers, on='date'and'home_team', how='left').merge(shootouts, on='date'and 'home_team', how='left')

goalscorers_copy=goalscorers
results_copy=results
shootouts_copy=shootouts

# all varchar to lowe case function
# def lowercase_text(column):
#   """Function to convert text values in a column to lowercase."""
#   return column.str.lower()  


# goalscorers_copy = goalscorers_copy.apply(lowercase_text, axis=1)
# results_copy = results_copy.apply(lowercase_text, axis=1)
# shootouts_copy = shootouts_copy.apply(lowercase_text, axis=1)



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
    results_copy    ['is_away_win']                  = results_copy    ['home_score'] < results_copy['away_score']


    shootouts_copy  ['is_home_win']                  = shootouts_copy  ['home_team'] == shootouts_copy['winner']
    shootouts_copy  ['is_home_team_first_shooter']   = shootouts_copy  ['home_team'] == shootouts_copy['first_shooter']

cleansing() 



#  the user will choose specific team in order to see the statistic 
def team_analyzer():
    team=input(""" Enter  team:\n""")
    filtered_df = results_copy.query(f"home_team  == {team} | away_team == {team}")
    winnings    = results_copy.query(f"(home_team == {team} & is_home_win==True)  | (away_team == {team} & is_away_win==True)").shape[0]
    losing      =results_copy.query(f"(home_team  == {team} & is_home_win==False) | (away_team == {team} & is_away_win==False)").shape[0]
    total_games = winnings + losing if winnings + losing > 0 else 1  # Avoid division by zero
    print(filtered_df)
    print(f"{team} has {winnings} winnings")
    print(f"{team} has {losing} losing")
    print(f"the winning percentage of {team} is " + f"{(winnings/(total_games))*100:.3f}%")


team_analyzer()






