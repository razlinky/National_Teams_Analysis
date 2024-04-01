import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import NumPy

goalscorers= pd.read_csv("goalscorers.csv")
results= pd.read_csv("results.csv")
shootouts= pd.read_csv("shootouts.csv")

# joined_df = results.merge(goalscorers, on='date'and'home_team', how='left').merge(shootouts, on='date'and 'home_team', how='left')


goalscorers_copy=goalscorers
results_copy=results
shootouts_copy=shootouts



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





# Specific value to check (True or False depending on your need)
specific_value = True
# Filter for the specific value in 'is_home_win' before grouping
filtered_df_home = results_copy[results_copy['is_home_win'] == specific_value]
filtered_df_away = results_copy[results_copy['is_away_win'] == specific_value]
# Group by 'home_team' and count occurrences (assuming specific_value is a boolean)
home_win_count = filtered_df_home.groupby('home_team').size().to_frame(name="Winshome").rename_axis('team')
away_win_count = filtered_df_home.groupby('away_team' ).size().to_frame(name="Winsaway").rename_axis('team')
# Print the grouped data (count of occurrences of the specific value for each team)
team_wins_df = pd.merge(home_win_count, away_win_count, how='inner', on='team').reset_index()
team_wins_df.fillna(0, inplace=True)
# Add 'Total Wins' column by summing 'Winshome' and 'Winsaway'
team_wins_df['Total Wins'] = team_wins_df['Winshome'] + team_wins_df['Winsaway']
# Print the DataFrame with total wins
top_10_wins_df = team_wins_df.sort_values(by='Total Wins', ascending=False).head(10)

# Print the DataFrame with top 5 total wins
print(top_10_wins_df)



color_map = plt.cm.get_cmap('tab10')
# Extract data for the scatter plot
team_names = top_10_wins_df['team'].to_numpy()
total_wins = top_10_wins_df.sort_values(by='team')['Total Wins'].to_numpy()  # Sort by team for line connection

# Create the scatter plot with lines and annotations
plt.figure(figsize=(12, 8))  # Adjust figure size as desired
for i, (team_name, total_win) in enumerate(zip(team_names, total_wins)):
    color = color_map(i % len(color_map.colors))  # Assign color based on team index
    plt.scatter(team_name, total_win, s=100, color=color, label=team_name, edgecolor='black', linewidth=1)
    if i < len(total_wins) - 1:  # Connect points with lines (except the last one)
        plt.plot([team_name, team_names[i + 1]], [total_win, total_wins[i + 1]], color=color, linewidth=2)

    # Add annotation for total wins above each data point (adjusted positioning)
    plt.annotate(f"{total_win} Wins", (team_name, total_win + 2),  # Smaller vertical offset
                 xycoords='data',  # Use data coordinates for placement
                 horizontalalignment='center',
                 verticalalignment='bottom',
                 fontsize=8, color=color)

# Customize plot elements
plt.xlabel('Team')
plt.ylabel('Total Wins')
plt.title('Total Wins for Top 5 Teams (Filtered Data)')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()  # Add a legend to identify teams with colors

# Display the plot
plt.tight_layout()
plt.show()





# ------------------------------------------------------------------------------------------------------------
color_map = plt.cm.get_cmap('tab10')  # Use 'tab10' colormap or choose another

# Extract data for the scatter plot
team_names = top_10_wins_df['team'].to_numpy()
wins_away = top_10_wins_df.sort_values(by='team')['Winsaway'].to_numpy()  # Use 'Winsaway' column

# Create the scatter plot with lines and annotations
plt.figure(figsize=(12, 8))  # Adjust figure size as desired
for i, (team_name, wins_away_value) in enumerate(zip(team_names, wins_away)):
    color = color_map(i % len(color_map.colors))  # Assign color based on team index
    plt.scatter(team_name, wins_away_value, s=100, color=color, label=team_name, edgecolor='black', linewidth=1)
    if i < len(wins_away) - 1:  # Connect points with lines (except the last one)
        plt.plot([team_name, team_names[i + 1]], [wins_away_value, wins_away[i + 1]], color=color, linewidth=2)

    # Add annotation for wins away above each data point (adjusted positioning)
    plt.annotate(f"{wins_away_value} Wins Away", (team_name, wins_away_value + 2),  # Smaller vertical offset
                 xycoords='data',  # Use data coordinates for placement
                 horizontalalignment='center',
                 verticalalignment='bottom',
                 fontsize=8, color=color)

# Customize plot elements
plt.xlabel('Team')
plt.ylabel('Wins Away')  # Update label
plt.title('Wins Away for Top 5 Teams (Filtered Data)')  # Update title
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()  # Add a legend to identify teams with colors

# Display the plot
plt.tight_layout()
plt.show()












