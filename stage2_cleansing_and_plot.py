import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import NumPy
from seaborn import kdeplot
import sys

goalscorers= pd.read_csv("goalscorers.csv")
results= pd.read_csv("results.csv")
shootouts= pd.read_csv("shootouts.csv")

# -------------------------------------------------------------------------------------------------------------------------
def drop_duplicates_empty_rows(df):
    df_copy = df.copy() 
    df_clean = df_copy.drop_duplicates().dropna()
    return df_clean

goalscorers = drop_duplicates_empty_rows(goalscorers)
results = drop_duplicates_empty_rows(results)
shootouts = drop_duplicates_empty_rows(shootouts)
# -------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------
# from functions_data_frames import results_df_with_boolean_columns

def results_df_with_boolean_columns():
    results    ['is_home_win']                  = results    ['home_score'] > results['away_score']
    results    ['is_away_win']                  = results    ['home_score'] < results['away_score']

    return results


# -------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------

while True:
    num_of_teams = int(input("How many teams do you want to see (between 1 and 5)? "))
    if 1 <= num_of_teams <= 5:
        break  # Exit the loop if input is valid (between 1 and 5)
    else:
        print("Invalid input. Please enter a number between 1 and 5.")

print(f"Processing data for {num_of_teams} teams.")
# -------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------
# from functions_data_frames import top_team_chooser
def top_team_chooser():
    specific_value = True
    # true is winning !!!!
    # Filter for the specific value in 'is_home_win' before grouping
    filtered_df_home = results_df_with_boolean_columns()[results_df_with_boolean_columns()['is_home_win'] == specific_value]
    filtered_df_away = results_df_with_boolean_columns()[results_df_with_boolean_columns()['is_away_win'] == specific_value]
    # Group by 'home_team' and count occurrences(bollean as i added before) and rename the column to team 
    home_win_count = filtered_df_home.groupby('home_team').size().to_frame(name="Winshome").rename_axis('team')
    away_win_count = filtered_df_away.groupby('away_team' ).size().to_frame(name="Winsaway").rename_axis('team')
    # mergin the two home win and away team inner join on team key
    # for each team how many wins away and home
    team_wins_df = pd.merge(home_win_count, away_win_count, how='inner', on='team').reset_index()
    team_wins_df.fillna(0, inplace=True)
    # Add 'Total_Wins' column by summing 'Winshome' and 'Winsaway'
    team_wins_df['Total_Wins'] = team_wins_df['Winshome'] + team_wins_df['Winsaway']
    # as the input of the user will see only the top teams 
    top_teams_chooser = team_wins_df.sort_values(by='Total_Wins', ascending=False).head(num_of_teams)
    # Print the DataFrame with top 5 Total_Wins
    # print(top_teams_chooser)
    return top_teams_chooser

print(top_team_chooser())
# -------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------


def team_goal_per_min():

    merged_df = top_team_chooser().merge(goalscorers, how='inner', on='team')

    # will want only the teams the user choose and minute of the goal 
    team_goal_minutes=merged_df.loc[:, ['team','minute']]

    # print a table column team and column minute of a goal
     
    return team_goal_minutes
    

team_goal_per_min()

# ----------------------------------------------add new column minutes 0-120 into 4 groups 
def team_goal_per_min_with_group_column():
  """
  Adds a new column 'group' to the DataFrame 'df' that categorizes minutes into 4 groups (0-30, 31-60, 61-90, 91-120).

  Args:
      df (pandas.DataFrame): The DataFrame containing 'team' and 'minute' columns.

  Returns:
      pandas.DataFrame: The DataFrame with the added 'group' column.
  """
  df=team_goal_per_min()
  # Define group boundaries based on minute range (0-120)
  group_boundaries = [0, 30, 60, 90, 120]

  # Create a function to assign group based on minute
  def assign_group(minute):
    for i in range(len(group_boundaries) - 1):
      if group_boundaries[i] <= minute < group_boundaries[i + 1]:
        return f"Group {i+1}"
    return "Group 4"  # Handle minutes at the upper limit (120)

  # Add a new column 'group' using apply
  df['group'] = df['minute'].apply(assign_group)
  print(df)
  return df
team_goal_per_min_with_group_column()
# Assuming you have your DataFrame named 'df'
  # Avoid modifying the original DataFrame










# -----------------------------------------------------------------------
def plot_total_wins():
  """Creates a scatter plot with team names on the x-axis and wins away on the y-axis.

  Args:
      df (pandas.DataFrame): The DataFrame containing 'team', 'winshome', 'winsaway', and 'total_wins' columns.
  """
  df=top_team_chooser()
  # Extract data for plotting
  team_names =df['team'].to_numpy()
  wins_away = df['Total_Wins'].to_numpy()

  # Create the plot
  plt.figure(figsize=(10, 6))  # Adjust figure size as needed
  plt.scatter(team_names, wins_away, s=80, color='royalblue', edgecolor='black', linewidth=1)
  plt.xlabel('Team')
  plt.ylabel('Total Wins ')
  plt.title('Total Wins  by Team')
  plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
  plt.grid(True, linestyle='--', alpha=0.6)  # Add grid lines for reference
  plt.tight_layout()
  plt.show()

plot_total_wins()





# away wins for top teams plot-------------------------------------------------



def plot_team_winsaway():
  """Creates a scatter plot with team names on the x-axis and wins away on the y-axis.

  Args:
      df (pandas.DataFrame): The DataFrame containing 'team', 'winshome', 'winsaway', and 'total_wins' columns.
  """
  df=top_team_chooser()
  # Extract data for plotting
  team_names =df['team'].to_numpy()
  wins_away = df['Winsaway'].to_numpy()

  # Create the plot
  plt.figure(figsize=(10, 6))  # Adjust figure size as needed
  plt.scatter(team_names, wins_away, s=80, color='royalblue', edgecolor='black', linewidth=1)
  plt.xlabel('Team')
  plt.ylabel('Wins Away')
  plt.title('Wins Away by Team')
  plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
  plt.grid(True, linestyle='--', alpha=0.6)  # Add grid lines for reference
  plt.tight_layout()
  plt.show()

# Assuming you have your DataFrame named 'df'

plot_team_winsaway()





def plot_grouped_minute_per_Team():
  """Creates a grouped bar chart to visualize teams by group.

  Args:
      df (pandas.DataFrame): The DataFrame containing 'team' and 'group' (object type) columns.
  """
  df=team_goal_per_min_with_group_column()
  # Use crosstab to create a contingency table
  group_counts = pd.crosstab(df['team'], df['group'])

  # Create the grouped bar chart
  group_counts.plot(kind='bar', stacked=False, colormap='tab20')
  plt.xlabel('Team')
  plt.ylabel('goals')
  plt.title('0-120 minutes divides to 4 groups\n first 30mins is group1')
  plt.legend(title='Group', loc='upper left', bbox_to_anchor=(1.05, 1))  # Adjust legend position
  plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
  plt.grid(True, linestyle='--', alpha=0.6)
  plt.tight_layout()
  plt.show()

plot_grouped_minute_per_Team()





def menu2():
    user_menu=int(input("""\n Enter 1 if you want start over\n Enter 2 if you want  to exit: """))
    if user_menu==1:
        import stage1_data_frames 
    elif user_menu==2:
        print("bye bye ")
        sys.exit(0)
    else:
        print("\nplease enter valid number.\n")

menu2()