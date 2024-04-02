import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import NumPy
from seaborn import kdeplot


def step_2():
    # creat the df for all the 3 files 
    goalscorers= pd.read_csv("goalscorers.csv")
    results= pd.read_csv("results.csv")
    shootouts= pd.read_csv("shootouts.csv")


    # i will work on the copies 
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

    # creating new  boolean column for winnings or loosing 
        results_copy    ['is_home_win']                  = results_copy    ['home_score'] > results_copy['away_score']
        results_copy    ['is_away_win']                  = results_copy    ['home_score'] < results_copy['away_score']


        shootouts_copy  ['is_home_win']                  = shootouts_copy  ['home_team'] == shootouts_copy['winner']
        shootouts_copy  ['is_home_team_first_shooter']   = shootouts_copy  ['home_team'] == shootouts_copy['first_shooter']

    cleansing() 



    # --------begin results  data :::::::::::::::::::::
    # ------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------


    # the user will choose how top teams he wants to see the data on 
    # num_of_teams = int(input("How many teams do you want to see? "))

    # the user can choose max of 5 teams
    while True:
        num_of_teams = int(input("How many teams do you want to see (between 1 and 5)? "))
        if 1 <= num_of_teams <= 5:
            break  # Exit the loop if input is valid (between 1 and 5)
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

    # Your code to process the number of teams (replace with your logic)
    print(f"Processing data for {num_of_teams} teams.")




    # i did it in order to count how many wins on our boolean new columns 
    specific_value = True
    # Filter for the specific value in 'is_home_win' before grouping
    filtered_df_home = results_copy[results_copy['is_home_win'] == specific_value]
    filtered_df_away = results_copy[results_copy['is_away_win'] == specific_value]
    # Group by 'home_team' and count occurrences(bollean as i added before) and rename the column to team 
    home_win_count = filtered_df_home.groupby('home_team').size().to_frame(name="Winshome").rename_axis('team')
    away_win_count = filtered_df_home.groupby('away_team' ).size().to_frame(name="Winsaway").rename_axis('team')
    # mergin the two home win and away team inner join on team key
    team_wins_df = pd.merge(home_win_count, away_win_count, how='inner', on='team').reset_index()
    team_wins_df.fillna(0, inplace=True)
    # Add 'Total Wins' column by summing 'Winshome' and 'Winsaway'
    team_wins_df['Total Wins'] = team_wins_df['Winshome'] + team_wins_df['Winsaway']
    # as the input of the user will see only the top teams 
    top_teams_chooser = team_wins_df.sort_values(by='Total Wins', ascending=False).head(num_of_teams)

    # Print the DataFrame with top 5 total wins
    print(top_teams_chooser)


    # -------LETS MAKE some GARPHS FOR RESULTS 
    # -----------------------------------------------------------------------------------------------------
    color_map = plt.cm.get_cmap('tab10')
    # Extract data for the scatter plot
    team_names = top_teams_chooser['team'].to_numpy()
    total_wins = top_teams_chooser.sort_values(by='team')['Total Wins'].to_numpy()  # add lines to connect teams 

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
    team_names = top_teams_chooser['team'].to_numpy()
    wins_away = top_teams_chooser.sort_values(by='team')['Winsaway'].to_numpy()  # Use 'Winsaway' column

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


    # --------end results  data :::::::::::::::::::::
    # ------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------



    # --------begin goalscores  data :::::::::::::::::::::
    # ------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------




    # Assuming you have the DataFrames created

    # Perform an inner join to keep only matching teams number of teams will be as the user choose (max 5 )
    merged_df = top_teams_chooser.merge(goalscorers_copy, how='inner', on='team')

    # will want only the teams the user choose and minute of the goal 
    merged_df1=merged_df.loc[:, ['team','minute']]

    print(merged_df1)



    # Define a function to create the combined density and histogram plot for each team
    def plot_goal_distribution(team_data, team_name):
        # Extract minute of goal for the current team
        goal_minutes = team_data['minute']

        # Create the combined plot
        plt.figure(figsize=(8, 6))  # Adjust figure size as needed

        # Density plot with transparency
        kdeplot(goal_minutes, shade=True, alpha=0.7, label=f"Team {team_name} Density")

        # Histogram on top (adjust bins as needed)
        plt.hist(goal_minutes, bins=8, edgecolor='black', alpha=0.7, label=f"Team {team_name} Frequency")

        plt.xlabel("Minute of Goal")
        plt.ylabel("Goals")
        plt.title(f"Distribution of Goal Per Minutes for Team: {team_name}")
        plt.xlim(0, max(goal_minutes) + 1)  # Adjust x-axis limits based on data
        plt.legend()
        plt.grid(True)  # Add grid lines for better readability
        plt.tight_layout()  # Adjust spacing between elements
        plt.show()

    # Group data by team and create combined plots
    for team, team_data in merged_df1.groupby('team'):
        plot_goal_distribution(team_data.copy(), team)  # Pass a copy to avoid modifying original data




    # Assuming you have the 'merged_df1' DataFrame

    # Group data by team
    grouped_data = merged_df1.groupby('team')
    print(grouped_data)
    # An    alyze various statistics for each team per minute 
    team_stats = grouped_data['minute'].agg(['describe', 'mean', 'median', 'std', 'max', 'min'])

    print(team_stats)





    # Assuming you have the 'merged_df1' DataFrame and 'team_stats' DataFrame from previous analysis

    # mean time of goal for each team (max 5 teams )
    statistic_to_plot = 'mean'

    # Extract the desired statistic for each team
    team_means = team_stats[statistic_to_plot]

    # Create a bar chart
    team_means.plot(kind='bar', color='skyblue', edgecolor='black')
    min_value = team_means.min() - 10
    max_value = team_means.max() + 10
    # Customize the plot
    plt.xlabel("team")
    plt.ylabel(f"{statistic_to_plot.capitalize()} minute  ")
    plt.title(f"{statistic_to_plot.capitalize()} Minute of Goal per Team")
    plt.xticks(rotation=5)  # Rotate x-axis labels for better readability (optional)
    plt.tight_layout()
    plt.show()



step_2()